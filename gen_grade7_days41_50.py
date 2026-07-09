#!/usr/bin/env python3
"""Phase 3: Grade 7, Days 41-50 (second Grade 7 batch, continuing the
10-day pattern). Topics chosen to avoid any overlap with the existing Day
1-40 set (see data/grade7.json after the Days 31-40 batch): unreliable
narrators, gerunds/infinitives, linear systems, exponent laws, the
endocrine system, biomes, WHMIS symbols, and 20th-century global history
(Vietnam War, fall of the Berlin Wall, apartheid) alongside refugee
crises, trade agreements, and active citizenship.

As with the earlier batches: videoUrl is intentionally left unset for
every subject -- fetch_video_ids.py fills these in automatically on its
next daily run. No embedded ASCII double-quote characters are used
anywhere in question/summary/option text; apostrophes use the curly
Unicode form (’) so they never collide with the single-quoted Python
string literals used here.
"""
import sys
sys.path.insert(0, '/sessions/modest-compassionate-lamport/mnt/gradesbooster')
from gen_curriculum import sub, day, append_to

L7 = 'https://tvolearn.com/pages/grade-7-language'
M7 = 'https://tvolearn.com/pages/grade-7-mathematics'
S7 = 'https://tvolearn.com/pages/grade-7-science-and-technology'
SS7 = 'https://tvolearn.com/pages/grade-7-social-studies'
RL, RM, RS, RSS = (
    'TVO Learn: Grade 7 Language',
    'TVO Learn: Grade 7 Mathematics',
    'TVO Learn: Grade 7 Science & Technology',
    'TVO Learn: Grade 7 Social Studies',
)


def L(t, s, q):
    return sub('Language', t, s, RL, L7, q)


def M(t, s, q):
    return sub('Math', t, s, RM, M7, q)


def Sc(t, s, q):
    return sub('Science', t, s, RS, S7, q)


def SS(t, s, q):
    return sub('SocialStudies', t, s, RSS, SS7, q)


g7_41_50 = [
day(41, [
L('Reading: Analyzing Unreliable Narrators',
  'Ontario Grade 7 Reading strand: an unreliable narrator is a storyteller whose account may be biased, mistaken, or dishonest, requiring readers to critically evaluate what is really happening in the story.',
  [('An unreliable narrator is one whose account may be ___.', ['Completely accurate at all times', 'Biased, mistaken, or dishonest', 'Written by someone other than the author', 'Impossible to include in a story'], 1),
   ('Why might an author choose to use an unreliable narrator?', ['To create suspense or challenge readers to question what is really happening', 'Unreliable narrators are never used in literature', 'It always makes a story less interesting', 'It removes the need for any plot'], 0),
   ('Which is a clue that a narrator might be unreliable?', ['Inconsistencies between their account and other details in the story', 'A narrator who never says anything at all', 'A narrator who is always proven completely correct', 'A story with no narrator present'], 0),
   ('Reading critically when a narrator seems unreliable involves ___.', ['Questioning the narrator’s claims and looking for supporting or contradicting evidence', 'Accepting every statement without question', 'Ignoring the narrator completely', 'Assuming the story has no deeper meaning'], 0),
   ('Why is recognizing an unreliable narrator considered an advanced reading skill?', ['It requires careful analysis of tone, consistency, and perspective', 'It requires no critical thinking at all', 'Unreliable narrators are always obvious immediately', 'This skill has no connection to comprehension'], 0)]),
M('Systems of Two Linear Relations: A Graphical Introduction',
  'Ontario Grade 7 Algebra strand: a system of two linear relations can be solved graphically by finding the point where their two lines intersect, representing the values that satisfy both relations.',
  [('The solution to a system of two linear relations, solved graphically, is ___.', ['The point where the two lines intersect', 'Any point on either line separately', 'A point that never exists', 'The origin of the graph in every case'], 0),
   ('If two lines on a graph never intersect, the system has ___.', ['Exactly one solution', 'No solution', 'Infinitely many solutions', 'A solution at the origin only'], 1),
   ('If two lines on a graph are identical, the system has ___.', ['No solution', 'Exactly one solution', 'Infinitely many solutions', 'A solution only at the origin'], 2),
   ('Why is finding the point of intersection useful when solving a system of linear relations?', ['It represents the values of the variables that satisfy both relations at once', 'It has no meaning in the context of the two relations', 'It only matters for one of the two lines', 'Intersection points are unrelated to solving systems'], 0),
   ('Graphing two linear relations on the same grid allows you to ___.', ['Visually identify where their solutions overlap', 'Prevent any comparison between the relations', 'Automatically solve unrelated equations', 'Remove the need for any calculations'], 0)]),
Sc('The Endocrine System: Hormones and Regulation',
   'Ontario Grade 7 Science Human Body Systems strand: the endocrine system uses glands to release hormones into the bloodstream, regulating processes like growth, metabolism, and stress response.',
   [('The endocrine system regulates the body using ___.', ['Hormones released into the bloodstream', 'Only physical touch', 'Sound waves', 'Light signals only'], 0),
    ('Hormones are produced by structures called ___.', ['Glands', 'Bones', 'Muscles only', 'Blood vessels only'], 0),
    ('Which of these processes might the endocrine system help regulate?', ['Growth and metabolism', 'Nothing related to body function', 'Only hair colour', 'Only eye colour'], 0),
    ('How does the endocrine system typically differ from the nervous system in how it sends signals?', ['It relies on hormones travelling through the bloodstream rather than fast electrical signals', 'It has no way of sending any signals', 'It always works faster than the nervous system', 'It has no connection to body regulation'], 0),
    ('Why is the endocrine system important for maintaining balance in the body?', ['It helps regulate many internal processes needed for healthy functioning', 'The endocrine system has no role in maintaining balance', 'The body functions with no hormonal regulation at all', 'It affects only external appearance, not internal processes'], 0)]),
SS('The Vietnam War and Its Global Impact',
   'Ontario Grade 7 Social Studies Heritage and Identity strand: the Vietnam War, fought primarily during the 1960s and 1970s, was a significant Cold War-era conflict that had lasting political and social effects around the world, including in Canada.',
   [('The Vietnam War took place primarily during which decades?', ['The 1960s and 1970s', 'The 1800s', 'The 1930s', 'The 2000s'], 0),
    ('The Vietnam War is often considered connected to which broader global conflict?', ['The Cold War', 'The War of 1812', 'World War I', 'The Napoleonic Wars'], 0),
    ('The Vietnam War had lasting effects on ___.', ['Political and social attitudes in many countries, including Canada', 'No countries outside of Vietnam', 'Only ancient history', 'Nations with no involvement or connection to the war'], 0),
    ('Why is the Vietnam War often studied in the context of Cold War history?', ['It reflected broader tensions between opposing political systems during that era', 'It had no connection to Cold War tensions', 'It occurred before the Cold War began', 'It was completely unrelated to global politics'], 0),
    ('Why might a war fought primarily in one country still have a significant global impact?', ['International alliances and public opinion can be affected far beyond the location of the conflict', 'Wars never have any impact beyond their immediate location', 'Global impact is impossible from a single regional conflict', 'Only wars fought on multiple continents matter internationally'], 0)])]),

day(42, [
L('Writing: Writing a Satirical Piece',
  'Ontario Grade 7 Writing strand: satire uses humour, irony, or exaggeration to criticize or draw attention to flaws in society, people, or ideas.',
  [('Satire is a form of writing that uses ___.', ['Humour, irony, or exaggeration to critique something', 'Only straightforward, literal statements', 'No persuasive or critical elements at all', 'Purely factual reporting with no commentary'], 0),
   ('Why might a writer choose satire instead of a direct, serious critique?', ['Humour and exaggeration can make a critique more engaging or memorable', 'Satire always weakens an argument', 'Satire removes all meaning from a piece of writing', 'Direct critique is always more effective than satire'], 0),
   ('Which is an example of a technique commonly used in satire?', ['Exaggerating a flaw to make it seem absurd', 'Presenting only neutral, factual statements', 'Avoiding any criticism of the subject', 'Removing all humour from the piece'], 0),
   ('Satire is often used to draw attention to ___.', ['Flaws in society, people, or ideas', 'Nothing of significance', 'Only positive qualities with no criticism', 'Random, unrelated topics with no purpose'], 0),
   ('Why might readers need to think carefully when reading satire?', ['The exaggerated or ironic tone might not be immediately obvious', 'Satire is always completely literal with no hidden meaning', 'Satire requires no interpretation at all', 'Readers never need to consider tone in satire'], 0)]),
M('Exponent Laws: Multiplying and Dividing Powers',
  'Ontario Grade 7 Number strand: when multiplying powers with the same base, add the exponents; when dividing powers with the same base, subtract the exponents.',
  [('Simplify: x cubed times x squared.', ['x to the fifth power', 'x to the sixth power', 'x squared', 'x to the first power'], 0),
   ('Simplify: x to the fifth power divided by x squared.', ['x to the seventh power', 'x to the third power', 'x squared', 'x to the tenth power'], 1),
   ('When multiplying powers with the same base, you should ___.', ['Add the exponents', 'Multiply the exponents', 'Subtract the exponents', 'Divide the exponents'], 0),
   ('When dividing powers with the same base, you should ___.', ['Multiply the exponents', 'Add the exponents', 'Subtract the exponents', 'Divide the bases'], 2),
   ('Simplify: 2 to the fourth power times 2 to the third power.', ['2 to the seventh power', '2 to the twelfth power', '2 to the first power', '4 to the seventh power'], 0)]),
Sc('Biomes of the World',
   'Ontario Grade 7 Science Earth and Space Systems strand: biomes are large regions characterized by distinct climate and communities of plants and animals adapted to those conditions, such as deserts, rainforests, and tundra.',
   [('A biome is best described as ___.', ['A large region with a distinct climate and community of organisms', 'A single individual animal', 'A type of rock formation', 'A man-made structure'], 0),
    ('Which biome is characterized by very low precipitation and extreme temperatures?', ['Rainforest', 'Desert', 'Wetland', 'Coral reef'], 1),
    ('The tropical rainforest biome is known for its ___.', ['High biodiversity and warm, wet climate', 'Extremely dry, sandy conditions', 'Permanent ice cover', 'Cold, treeless landscape'], 0),
    ('The tundra biome is characterized mainly by ___.', ['Warm, tropical conditions', 'Cold temperatures and a lack of trees', 'Dense rainforest vegetation', 'Coral reef ecosystems'], 1),
    ('Why do organisms in different biomes have different adaptations?', ['They must adjust to the specific climate and conditions of their biome', 'All biomes have identical conditions requiring no adaptation', 'Adaptations have no connection to climate', 'Organisms never adapt to their environment'], 0)]),
SS('The Fall of the Berlin Wall and the End of the Cold War',
   'Ontario Grade 7 Social Studies Heritage and Identity strand: the fall of the Berlin Wall in 1989 symbolized the end of the Cold War era, leading to significant political changes in Europe, including German reunification.',
   [('The Berlin Wall fell in which year?', ['1945', '1989', '1917', '2001'], 1),
    ('The fall of the Berlin Wall is often seen as symbolizing ___.', ['The end of the Cold War era', 'The beginning of World War II', 'The founding of the United Nations', 'The start of the Cold War'], 0),
    ('Following the fall of the Berlin Wall, Germany experienced ___.', ['Reunification', 'Permanent division into more countries', 'No political change of any kind', 'A return to conflict with no resolution'], 0),
    ('Why is the fall of the Berlin Wall considered a major turning point in world history?', ['It marked significant political change and reduced Cold War tensions in Europe', 'It had no lasting political significance', 'It caused the Cold War to begin', 'It was unrelated to Cold War tensions'], 0),
    ('The Berlin Wall had originally divided the city of Berlin into ___.', ['Eastern and Western sections', 'North and South sections only', 'Four unrelated countries', 'No divisions at all'], 0)])]),

day(43, [
L('Grammar: Gerunds and Infinitives',
  'Ontario Grade 7 Writing strand: a gerund is a verb form ending in -ing used as a noun (Swimming is fun), while an infinitive is the base form of a verb preceded by to (I want to swim).',
  [('A gerund is a verb form that ___.', ['Ends in -ing and is used as a noun', 'Always begins with the word to', 'Is never used in a sentence', 'Only functions as an adjective'], 0),
   ('An infinitive is typically formed by ___.', ['Placing to before the base form of a verb', 'Adding -ing to a verb', 'Removing the verb entirely', 'Adding -ed to a verb'], 0),
   ('Which sentence contains a gerund?', ['Swimming is my favourite activity.', 'I want to swim today.', 'She swims every morning.', 'They will swim later.'], 0),
   ('Which sentence contains an infinitive?', ['I want to swim today.', 'Swimming is relaxing.', 'She enjoys swimming.', 'Swimming builds strength.'], 0),
   ('Why might a writer choose to use a gerund instead of a regular noun?', ['A gerund can add a sense of ongoing action to a sentence', 'Gerunds are never grammatically correct', 'Gerunds always replace the need for a subject', 'There is no functional difference between a gerund and any noun'], 0)]),
M('Volume and Surface Area of Composite 3D Shapes',
  'Ontario Grade 7 Geometry strand: a composite 3D shape is made up of two or more basic solids combined, and its volume or surface area can be found by breaking it into simpler shapes and adding or subtracting their measurements.',
  [('A composite 3D shape is made up of ___.', ['Two or more basic solids combined', 'A single, simple shape only', 'No identifiable shapes at all', 'Only flat, 2D shapes'], 0),
   ('To find the volume of a composite shape, you can ___.', ['Break it into simpler shapes and add their volumes', 'Ignore parts of the shape entirely', 'Measure only the tallest point', 'Avoid any calculations'], 0),
   ('If a composite shape is made of a rectangular prism with volume 40 cubic units and a triangular prism with volume 15 cubic units attached, what is the total volume?', ['25 cubic units', '55 cubic units', '40 cubic units', '600 cubic units'], 1),
   ('Why might a real-world object, like a house-shaped storage shed, be considered a composite shape?', ['It combines multiple basic shapes, such as a rectangular prism and a triangular prism roof', 'It is made of only one simple shape', 'Composite shapes never appear in real life', 'A shed has no identifiable geometric shape'], 0),
   ('When calculating the surface area of a composite shape, it is important to ___.', ['Account for any internal faces that are not part of the outer surface', 'Ignore all internal considerations completely', 'Only measure the shape’s volume, not surface area', 'Assume all composite shapes have identical surface areas'], 0)]),
Sc('Chemical Safety and WHMIS Symbols',
   'Ontario Grade 7 Science Matter and Energy strand: WHMIS (Workplace Hazardous Materials Information System) symbols communicate important safety information about hazardous materials, helping people handle chemicals safely.',
   [('WHMIS stands for ___.', ['Workplace Hazardous Materials Information System', 'World Health and Medical Information Standard', 'Weather Hazard Measurement and Identification System', 'A system unrelated to chemical safety'], 0),
    ('WHMIS symbols are designed to ___.', ['Communicate important safety information about hazardous materials', 'Provide no useful safety information', 'Only apply to non-hazardous materials', 'Replace the need for any safety training'], 0),
    ('Why is it important to recognize WHMIS symbols in a lab or workplace setting?', ['They help people understand risks and handle materials safely', 'These symbols have no practical safety purpose', 'WHMIS symbols are purely decorative', 'Safety symbols are never used in real workplaces'], 0),
    ('A WHMIS symbol indicating a flammable material would likely warn about ___.', ['The risk of the material catching fire', 'No risk at all', 'A material that is completely safe to burn', 'A material unrelated to fire hazards'], 0),
    ('Why might students learn about WHMIS symbols as part of science class?', ['To build safe habits when working with materials in labs and other settings', 'Chemical safety has no connection to science education', 'WHMIS symbols are only relevant to a single profession', 'Safety information is unnecessary in a classroom setting'], 0)]),
SS('Apartheid and the Struggle for Equality in South Africa',
   'Ontario Grade 7 Social Studies Heritage and Identity strand: apartheid was a system of racial segregation and discrimination in South Africa, and its end in the early 1990s followed decades of resistance and advocacy for equality.',
   [('Apartheid was a system of ___.', ['Racial segregation and discrimination', 'Equal treatment for all citizens', 'A government with no policies on race', 'A system unrelated to South Africa'], 0),
    ('Apartheid was officially practiced in which country?', ['South Africa', 'Canada', 'France', 'Japan'], 0),
    ('Apartheid came to an end in the early ___.', ['1900s', '1950s', '1990s', '2010s'], 2),
    ('The end of apartheid followed decades of ___.', ['Resistance and advocacy for equality', 'No opposition of any kind', 'Complete indifference from the global community', 'Immediate, effortless political change'], 0),
    ('Why is the history of apartheid studied as part of world history?', ['It illustrates the impact of systemic discrimination and the importance of the struggle for equality', 'It has no historical significance', 'Apartheid never actually occurred', 'It has no connection to global discussions on equality'], 0)])]),

day(44, [
L('Vocabulary: Technical and Academic Vocabulary',
  'Ontario Grade 7 Language strand: technical and academic vocabulary consists of specialized words used within specific subjects or fields, and understanding these terms is important for reading and writing in those areas.',
  [('Technical vocabulary refers to ___.', ['Specialized words used within specific subjects or fields', 'Words used only in casual conversation', 'Words with no specific meaning', 'Vocabulary that never appears in academic writing'], 0),
   ('Why is understanding academic vocabulary important for reading textbooks?', ['It helps readers understand subject-specific concepts accurately', 'Academic vocabulary has no connection to understanding a subject', 'Textbooks never use specialized vocabulary', 'Understanding vocabulary is unnecessary for comprehension'], 0),
   ('Which is an example of technical vocabulary specific to science?', ['Photosynthesis', 'Happy', 'Quickly', 'Nice'], 0),
   ('Why might a student need to learn new vocabulary when starting a new subject, like geometry?', ['New subjects often introduce specialized terms essential to understanding key concepts', 'New subjects never require any new vocabulary', 'Vocabulary has no connection to understanding a subject', 'Technical vocabulary is identical across every subject'], 0),
   ('A glossary in a textbook is useful because it ___.', ['Provides definitions for specialized or technical terms used in the text', 'Contains no useful information', 'Replaces the need to read the textbook itself', 'Only lists unrelated general vocabulary'], 0)]),
M('Data: Outliers and Their Effect on Statistics',
  'Ontario Grade 7 Data Management strand: an outlier is a data value that is significantly higher or lower than the rest of a data set, and it can strongly affect statistics like the mean.',
  [('An outlier is a data value that is ___.', ['Significantly higher or lower than the rest of the data set', 'Always exactly equal to the mean', 'The same as every other value in the set', 'Impossible to identify in any data set'], 0),
   ('Which statistic is most affected by an outlier?', ['The mean', 'The mode, in most typical cases', 'Neither statistic is ever affected', 'Only the median, and never the mean'], 0),
   ('In the data set 2, 3, 4, 5, 50, which value is the outlier?', ['2', '3', '4', '50'], 3),
   ('Why might statisticians examine a data set for outliers before calculating the mean?', ['An outlier can skew the mean and make it less representative of the typical values', 'Outliers have no effect on any calculation', 'The mean should always be calculated without checking for outliers', 'Outliers should never be considered in statistics'], 0),
   ('Compared to the mean, the median is generally ___ affected by outliers.', ['More', 'Less', 'Equally', 'Never'], 1)]),
Sc('Robotics and Automation in Technology',
   'Ontario Grade 7 Science and Technology strand: robotics involves designing machines that can perform tasks automatically, often using sensors and programming to interact with their environment.',
   [('Robotics involves designing machines that can ___.', ['Perform tasks automatically', 'Never interact with their environment', 'Function without any programming', 'Only operate manually with no automation'], 0),
    ('Sensors in a robot are used to ___.', ['Detect and respond to information from the environment', 'Prevent the robot from functioning at all', 'Replace the need for any programming', 'Have no role in robotic function'], 0),
    ('Automation refers to ___.', ['Technology performing tasks with little or no human intervention', 'Tasks that always require constant human control', 'A process with no connection to technology', 'Machines that can never repeat a task'], 0),
    ('Which is an example of a real-world application of robotics?', ['A robotic arm assembling products in a factory', 'A basic hand tool with no automation', 'A book with no technological components', 'A drawing made without any technology'], 0),
    ('Why is understanding robotics increasingly relevant in today’s world?', ['Automation and robotics are used across many industries and everyday technologies', 'Robotics has no real-world applications', 'Robots are used exclusively in fictional stories', 'Robotics has no connection to modern technology'], 0)]),
SS('The United Nations and Peacekeeping',
   'Ontario Grade 7 Social Studies People and Environments strand: United Nations peacekeeping missions involve international forces working to maintain or restore peace in regions affected by conflict, with Canada historically playing a notable role.',
   [('United Nations peacekeeping missions aim to ___.', ['Maintain or restore peace in regions affected by conflict', 'Increase conflict in affected regions', 'Avoid any involvement in international conflicts', 'Replace all national governments'], 0),
    ('Peacekeeping forces are typically made up of ___.', ['Personnel from multiple member countries', 'Only a single country’s military', 'No organized personnel at all', 'Civilians with no formal role'], 0),
    ('Canada has historically been recognized for its role in ___.', ['United Nations peacekeeping efforts', 'Avoiding all international involvement', 'Opposing the United Nations entirely', 'A role unrelated to international peace efforts'], 0),
    ('Why might the United Nations organize peacekeeping missions instead of relying on a single country to act alone?', ['International cooperation can bring broader legitimacy and shared resources to peace efforts', 'Peacekeeping missions never require cooperation between countries', 'A single country always resolves conflicts more effectively alone', 'International cooperation has no benefit in peacekeeping efforts'], 0),
    ('Why is learning about peacekeeping relevant to understanding international relations?', ['It shows how countries can work together to address global conflicts', 'Peacekeeping has no connection to international relations', 'Conflicts are never addressed through international cooperation', 'Peacekeeping missions have never actually taken place'], 0)])]),

day(45, [
L('Reading: Evaluating Counterarguments in Persuasive Texts',
  'Ontario Grade 7 Reading strand: a counterargument acknowledges an opposing viewpoint, and evaluating how effectively a writer addresses it helps readers judge the overall strength of a persuasive text.',
  [('A counterargument in persuasive writing is used to ___.', ['Acknowledge an opposing viewpoint', 'Ignore all opposing viewpoints', 'Remove the writer’s original argument entirely', 'Avoid presenting any evidence'], 0),
   ('Why might a writer include a counterargument in a persuasive essay?', ['To show they have considered other perspectives, which can strengthen their credibility', 'Including a counterargument always weakens an essay', 'Counterarguments should never appear in persuasive writing', 'It replaces the need for the writer’s own argument'], 0),
   ('An effective response to a counterargument typically ___.', ['Explains why the writer’s position still holds despite the opposing view', 'Simply restates the counterargument with no response', 'Ignores the counterargument completely after mentioning it', 'Contradicts the writer’s own argument'], 0),
   ('Why is evaluating how a writer handles counterarguments useful for readers?', ['It helps readers judge how well-reasoned and balanced the argument truly is', 'This evaluation has no value for readers', 'Counterarguments are never relevant to understanding an argument', 'Readers should never question a persuasive text’s reasoning'], 0),
   ('Which is an example of effectively addressing a counterargument?', ['Acknowledging the opposing view, then explaining why the evidence still supports the writer’s position', 'Refusing to mention any opposing views', 'Changing the topic entirely to avoid the opposing view', 'Agreeing completely with the opposing view with no further explanation'], 0)]),
M('Geometry: Angle Relationships in Polygons',
  'Ontario Grade 7 Geometry strand: the sum of interior angles in a polygon can be calculated using the formula (n minus 2) times 180 degrees, where n represents the number of sides.',
  [('What is the sum of interior angles in a triangle?', ['90 degrees', '180 degrees', '270 degrees', '360 degrees'], 1),
   ('What is the sum of interior angles in a quadrilateral?', ['180 degrees', '270 degrees', '360 degrees', '450 degrees'], 2),
   ('The formula for the sum of interior angles in a polygon is ___.', ['(n minus 2) times 180 degrees', 'n times 180 degrees', 'n times 360 degrees', '(n plus 2) times 90 degrees'], 0),
   ('What is the sum of interior angles in a pentagon (5 sides)?', ['360 degrees', '540 degrees', '720 degrees', '450 degrees'], 1),
   ('Why is the interior angle sum formula useful when working with polygons?', ['It allows you to calculate missing angles without measuring each one directly', 'It has no practical use in geometry', 'It only applies to triangles', 'Angle sums are always identical for every polygon regardless of sides'], 0)]),
Sc('The Respiratory and Circulatory Systems',
   'Ontario Grade 7 Science Human Body Systems strand: the respiratory system brings oxygen into the body and removes carbon dioxide, while the circulatory system transports that oxygen and other nutrients throughout the body.',
   [('The main role of the respiratory system is to ___.', ['Bring oxygen into the body and remove carbon dioxide', 'Digest food', 'Filter waste from the blood', 'Control body movement'], 0),
    ('The main role of the circulatory system is to ___.', ['Transport oxygen and nutrients throughout the body', 'Digest food', 'Filter air only', 'Control emotions'], 0),
    ('The heart is the main organ of the ___ system.', ['Circulatory', 'Respiratory', 'Digestive', 'Excretory'], 0),
    ('The lungs are the main organs of the ___ system.', ['Respiratory', 'Circulatory', 'Digestive', 'Excretory'], 0),
    ('How do the respiratory and circulatory systems work together?', ['Oxygen brought in by the respiratory system is transported through the body by the circulatory system', 'They function with no connection to each other', 'The circulatory system brings in air directly', 'The respiratory system pumps blood throughout the body'], 0)]),
SS('Canada’s Multiculturalism Policy in Depth',
   'Ontario Grade 7 Social Studies Heritage and Identity strand: Canada became the first country to adopt an official multiculturalism policy in 1971, aiming to recognize and support the cultural diversity of its population.',
   [('Canada adopted an official multiculturalism policy in which year?', ['1867', '1931', '1971', '2000'], 2),
    ('Canada’s multiculturalism policy was notable for making Canada ___.', ['The first country to adopt an official multiculturalism policy', 'The last country to consider cultural diversity', 'A country with no cultural diversity at all', 'The only country ever to have immigrants'], 0),
    ('The goal of Canada’s multiculturalism policy is to ___.', ['Recognize and support the cultural diversity of its population', 'Eliminate all cultural diversity', 'Require all citizens to share an identical culture', 'Ignore the cultural backgrounds of Canadians'], 0),
    ('Why might Canada’s multiculturalism policy be seen as connected to its identity as a nation?', ['It reflects Canada’s history of immigration and diverse population', 'It has no connection to Canada’s history or identity', 'Canada has never had a diverse population', 'The policy was created with no consideration of Canadian history'], 0),
    ('Why is studying multiculturalism policy relevant to understanding modern Canada?', ['It helps explain how Canada approaches diversity and inclusion as a country', 'This policy has no relevance to modern Canadian society', 'Multiculturalism has no connection to Canadian identity', 'The policy has never influenced Canadian society'], 0)])]),

day(46, [
L('Writing: Writing a Speech for a Specific Audience',
  'Ontario Grade 7 Writing strand: writing an effective speech requires considering the specific audience’s interests, knowledge, and expectations to choose appropriate language, tone, and content.',
  [('Writing a speech for a specific audience requires considering ___.', ['The audience’s interests, knowledge, and expectations', 'Nothing about who will be listening', 'Only the speaker’s personal preferences', 'A random, unrelated topic'], 0),
   ('Why might a speech for young children use different language than a speech for adults?', ['Language should be appropriate to the audience’s age and understanding', 'Language never needs to change based on audience', 'All speeches should use identical vocabulary regardless of audience', 'Audience consideration has no effect on speech writing'], 0),
   ('Which is an example of adapting a speech for a specific audience?', ['Using relevant examples the audience is likely to understand and connect with', 'Ignoring who will be listening to the speech', 'Using only complex vocabulary regardless of the audience', 'Avoiding any connection to the audience’s interests'], 0),
   ('Why is tone an important consideration when writing a speech for a particular audience?', ['The right tone helps the message resonate and be well received', 'Tone has no effect on how a speech is received', 'Speeches should always sound exactly the same regardless of audience', 'Tone only matters in written essays, not speeches'], 0),
   ('Considering audience expectations can help a speech writer decide ___.', ['What content and structure will be most effective and appropriate', 'Nothing useful about how to write the speech', 'To ignore the purpose of the speech entirely', 'That audience has no connection to speech writing'], 0)]),
M('Financial Literacy: Currency Exchange and Conversion',
  'Ontario Grade 7 Financial Literacy strand: currency exchange involves converting money from one currency to another using an exchange rate, which represents how much one currency is worth compared to another.',
  [('An exchange rate represents ___.', ['How much one currency is worth compared to another', 'The total amount of money in a country', 'A fixed amount that never changes', 'Only how much tax is charged'], 0),
   ('If the exchange rate is 1 Canadian dollar equals 0.75 US dollars, how many US dollars would you get for 100 Canadian dollars?', ['$75 US', '$100 US', '$133 US', '$25 US'], 0),
   ('Why might exchange rates change over time?', ['They are influenced by economic factors that can shift regularly', 'Exchange rates always stay exactly the same forever', 'Exchange rates have no connection to economics', 'Currency values never change under any circumstances'], 0),
   ('Why is understanding currency exchange useful when travelling to another country?', ['It helps travellers understand the real value and cost of items in a foreign currency', 'Currency exchange has no relevance when travelling', 'All countries use the exact same currency value', 'Understanding exchange rates serves no practical purpose'], 0),
   ('If 1 Canadian dollar equals 1.5 units of another currency, how many units would 20 Canadian dollars convert to?', ['15 units', '20 units', '30 units', '35 units'], 2)]),
Sc('Renewable vs. Non-Renewable Resources: Global Perspectives',
   'Ontario Grade 7 Science Matter and Energy strand: countries around the world rely differently on renewable resources, like solar and wind, and non-renewable resources, like coal and oil, based on geography, technology, and economic factors.',
   [('A country’s reliance on renewable versus non-renewable resources can depend on ___.', ['Its geography, technology, and economic factors', 'Nothing related to its location or economy', 'A completely random, unrelated factor', 'Only the size of the country, with no other influence'], 0),
    ('Which is an example of a renewable resource used differently around the world?', ['Solar energy, which is more effective in sunnier regions', 'Coal, which is considered renewable', 'Oil, which is considered renewable', 'A resource that never varies by region'], 0),
    ('Non-renewable resources, such as oil and coal, are considered limited because they ___.', ['Take an extremely long time to form and can eventually run out', 'Can be replenished within days', 'Are available in unlimited supply everywhere', 'Have no connection to geography'], 0),
    ('Why might some countries invest more heavily in renewable energy than others?', ['Available natural resources, technology, and economic priorities can vary by country', 'Every country has identical access to every energy source', 'Renewable energy investment is unrelated to geography or economics', 'All countries rely on the exact same energy sources'], 0),
    ('Why is understanding global resource use important when studying environmental science?', ['It helps explain differences in energy policy and environmental impact around the world', 'Global resource use has no connection to environmental science', 'All countries use resources in an identical way', 'This topic has no real-world relevance'], 0)]),
SS('Trade Agreements and Their Effects on Canada',
   'Ontario Grade 7 Social Studies People and Environments strand: trade agreements between countries establish rules for buying and selling goods and services, affecting Canada’s economy, industries, and international relationships.',
   [('A trade agreement is best described as ___.', ['An agreement establishing rules for trade between countries', 'A rule that prevents all trade between countries', 'An agreement unrelated to buying or selling goods', 'A policy that only applies within a single country'], 0),
    ('Trade agreements can affect Canada’s ___.', ['Economy and industries', 'Nothing related to its economy', 'Only its weather patterns', 'Only its population size'], 0),
    ('Why might Canada choose to enter into a trade agreement with another country?', ['To create more favourable conditions for trade, such as reduced tariffs', 'Trade agreements provide no economic benefit', 'Trade agreements are illegal for Canada to enter', 'They have no connection to international relationships'], 0),
    ('Which is a potential effect of a trade agreement on a specific Canadian industry?', ['Increased access to new markets or increased competition', 'No effect on any industry whatsoever', 'The complete elimination of that industry with no other outcome', 'A guaranteed benefit with no possible drawbacks'], 0),
    ('Why is it useful for citizens to understand how trade agreements affect their economy?', ['It helps them understand economic changes that may affect jobs and prices', 'Trade agreements have no connection to daily economic life', 'Citizens do not need to understand economic policy', 'Trade agreements never have any real-world effects'], 0)])]),

day(47, [
L('Media Literacy: Analyzing Documentary Techniques',
  'Ontario Grade 7 Media Literacy strand: documentaries use techniques such as interviews, narration, and selective editing to present information, and recognizing these choices helps viewers evaluate a documentary’s perspective.',
  [('Documentaries often use techniques such as ___.', ['Interviews, narration, and selective editing', 'Only fictional dialogue with no factual basis', 'Random unrelated footage with no structure', 'No editing of any kind'], 0),
   ('Selective editing in a documentary can ___.', ['Shape how viewers understand the topic being presented', 'Have no effect on how information is perceived', 'Always present a fully neutral, unbiased account', 'Remove the need for any narration'], 0),
   ('Why might a documentary filmmaker choose to include specific interviews?', ['To support the perspective or argument the documentary is presenting', 'Interviews are never included in documentaries', 'Interviews always represent every possible viewpoint equally', 'Interviews have no connection to a documentary’s message'], 0),
   ('Why is it valuable for viewers to consider a documentary’s perspective critically?', ['Even factual media can present information selectively to support a particular viewpoint', 'All documentaries present completely neutral, unbiased information', 'Critical thinking is unnecessary when watching documentaries', 'Documentaries never involve any creative choices'], 0),
   ('Narration in a documentary is used to ___.', ['Guide viewers’ understanding of the events and information shown', 'Remove all context from the footage', 'Confuse the viewer intentionally with no purpose', 'Replace the need for any visual content'], 0)]),
M('Rational and Irrational Numbers: An Introduction',
  'Ontario Grade 7 Number strand: a rational number can be written as a fraction of two integers, while an irrational number, such as pi, cannot be expressed exactly as a simple fraction.',
  [('A rational number can be expressed as ___.', ['A fraction of two integers', 'Only a whole number with no fractions allowed', 'A number that never terminates or repeats', 'A number unrelated to fractions'], 0),
   ('Which of these is an example of an irrational number?', ['Pi (approximately 3.14159...)', '1/2', '3', '0.75'], 0),
   ('An irrational number, when written as a decimal, is ___.', ['Non-terminating and non-repeating', 'Always a whole number', 'Always able to be written as a simple fraction', 'Always equal to zero'], 0),
   ('Which of these is an example of a rational number?', ['3/4', 'Pi', 'The square root of 2', 'A non-repeating, non-terminating decimal'], 0),
   ('Why might the square root of a non-perfect-square number, like the square root of 7, be considered irrational?', ['It cannot be expressed exactly as a simple fraction and its decimal never terminates or repeats', 'It is always a whole number', 'It can always be written as a simple fraction', 'All square roots are automatically rational'], 0)]),
Sc('The Immune System and Disease Prevention',
   'Ontario Grade 7 Science Human Body Systems strand: the immune system defends the body against pathogens, and practices like vaccination, handwashing, and proper nutrition can help support the immune system and prevent disease.',
   [('The immune system’s main role is to ___.', ['Defend the body against harmful pathogens', 'Digest food', 'Pump blood throughout the body', 'Control body movement'], 0),
    ('Which is a practice that can help prevent the spread of disease?', ['Regular handwashing', 'Avoiding all hygiene practices', 'Ignoring signs of illness completely', 'Sharing contaminated items without concern'], 0),
    ('Vaccines work by helping the immune system ___.', ['Recognize and respond more quickly to specific pathogens in the future', 'Stop functioning altogether', 'Ignore all future infections', 'Weaken permanently'], 0),
    ('Proper nutrition can support the immune system by ___.', ['Providing the body with resources needed for healthy immune function', 'Having no connection to immune health', 'Weakening the immune system intentionally', 'Replacing the need for any immune response'], 0),
    ('Why is understanding disease prevention considered important for public health?', ['Preventive practices can help reduce the spread of illness within communities', 'Disease prevention has no effect on public health', 'Preventing illness has no connection to community wellbeing', 'Public health has no relationship to individual health practices'], 0)]),
SS('Refugee Crises and International Response',
   'Ontario Grade 7 Social Studies People and Environments strand: a refugee crisis occurs when large numbers of people are forced to flee their home country due to conflict or persecution, often requiring coordinated international humanitarian response.',
   [('A refugee is generally someone who ___.', ['Has been forced to flee their home country due to conflict or persecution', 'Chooses to move for purely recreational reasons', 'Has never left their home country', 'Has no connection to conflict or persecution'], 0),
    ('A refugee crisis often requires ___.', ['Coordinated international humanitarian response', 'No response from any country', 'A single country acting entirely alone with no support', 'Complete indifference from the global community'], 0),
    ('Which organization might be involved in responding to a refugee crisis?', ['The United Nations', 'A local, unrelated sports club', 'An organization with no connection to humanitarian issues', 'A group uninvolved in international affairs'], 0),
    ('Why might countries choose to accept refugees during a crisis?', ['To provide safety and support for people fleeing dangerous conditions', 'Accepting refugees provides no humanitarian benefit', 'Countries are never involved in refugee resettlement', 'Refugee crises have no connection to international cooperation'], 0),
    ('Why is understanding refugee crises important in studying global issues?', ['It highlights the human impact of conflict and the importance of international cooperation', 'Refugee crises have no connection to global issues', 'This topic has no relevance to social studies', 'Refugee crises never require any international attention'], 0)])]),

day(48, [
L('Grammar: Correcting Dangling and Misplaced Modifiers',
  'Ontario Grade 7 Writing strand: a dangling modifier lacks a clear word to describe, while a misplaced modifier is positioned too far from the word it describes, both of which can create confusing or unintended meanings.',
  [('A dangling modifier is a modifier that ___.', ['Has no clear word in the sentence to describe', 'Is always placed correctly in a sentence', 'Never causes any confusion', 'Only appears in formal writing'], 0),
   ('A misplaced modifier is one that is ___.', ['Positioned too far from the word it is meant to describe', 'Always placed correctly next to the word it describes', 'Never used in writing', 'Only found at the beginning of a sentence'], 0),
   ('Which sentence contains a dangling modifier? Running quickly, the finish line came into view.', ['This sentence', 'The runner crossed the finish line quickly.', 'She ran quickly toward the finish line.', 'The finish line was near the runner.'], 0),
   ('Why is it important to fix dangling and misplaced modifiers in writing?', ['To avoid confusing or unintended meanings in a sentence', 'These issues never affect a sentence’s meaning', 'Modifiers should always be placed randomly', 'Clarity has no connection to modifier placement'], 0),
   ('Which is a corrected version of a sentence with a misplaced modifier? Wearing a red jacket, I saw my friend.', ['I saw my friend wearing a red jacket.', 'Wearing a red jacket, my friend I saw.', 'Both versions mean the exact same thing with no ambiguity.', 'Neither sentence contains a modifier.'], 0)]),
M('Solving Equations with Variables on Both Sides',
  'Ontario Grade 7 Algebra strand: solving an equation with variables on both sides involves first combining variable terms onto one side, then using inverse operations to isolate the variable.',
  [('Solve for x: 3x + 4 = x + 10.', ['x = 2', 'x = 3', 'x = 7', 'x = 14'], 1),
   ('Solve for y: 5y minus 2 = 2y + 7.', ['y = 3', 'y = 5', 'y = 9', 'y = 1'], 0),
   ('When solving an equation with variables on both sides, the first step is often to ___.', ['Combine the variable terms onto one side', 'Immediately guess the answer', 'Ignore one side of the equation entirely', 'Multiply both sides by zero'], 0),
   ('Solve for n: 4n + 6 = 2n + 16.', ['n = 5', 'n = 10', 'n = 3', 'n = 22'], 0),
   ('Solve for m: 6m minus 3 = 3m + 12.', ['m = 3', 'm = 5', 'm = 9', 'm = 15'], 1)]),
Sc('Space Exploration: Missions and Technology',
   'Ontario Grade 7 Science Earth and Space Systems strand: space exploration relies on missions and technologies such as rockets, satellites, and space stations to study space and expand human understanding of the universe.',
   [('Space missions often rely on technologies such as ___.', ['Rockets and satellites', 'Only bicycles and cars', 'No technology at all', 'Tools unrelated to space travel'], 0),
    ('A space station allows astronauts to ___.', ['Live and conduct research in space for extended periods', 'Immediately return to Earth after a few minutes', 'Avoid conducting any scientific research', 'Travel to another galaxy instantly'], 0),
    ('Satellites launched into space are often used for ___.', ['Communication and scientific observation', 'No practical purpose', 'Only entertainment, with no other function', 'Preventing all forms of communication'], 0),
    ('Why is space exploration considered valuable to scientific understanding?', ['It expands knowledge about the universe, other planets, and Earth itself', 'Space exploration provides no scientific benefit', 'It has no connection to expanding human knowledge', 'Space missions never gather any useful information'], 0),
    ('Which is an example of a real space exploration technology?', ['A robotic rover exploring the surface of Mars', 'A device with no connection to space exploration', 'A tool used only for underwater exploration', 'A vehicle designed only for use on Earth’s roads'], 0)]),
SS('Technology’s Impact on Modern Society and Government',
   'Ontario Grade 7 Social Studies People and Environments strand: technology has significantly influenced modern society and government, affecting communication, access to information, and how citizens engage with political processes.',
   [('Technology has significantly influenced modern society by affecting ___.', ['Communication and access to information', 'Nothing related to daily life', 'Only entertainment, with no other effects', 'A completely unrelated area of life'], 0),
    ('How has technology changed the way citizens engage with government?', ['It has made information about government actions more accessible', 'Technology has had no effect on citizen engagement', 'Citizens can no longer access any government information', 'Technology has eliminated all forms of citizen participation'], 0),
    ('Which is an example of technology’s impact on communication with government?', ['Citizens accessing government services or information online', 'A complete absence of any online government services', 'Technology preventing all communication with government', 'No connection between technology and government services'], 0),
    ('Why might increased access to information through technology be significant for democracy?', ['Informed citizens can more effectively participate in democratic processes', 'Access to information has no connection to democratic participation', 'Technology has no role in supporting democratic engagement', 'Democracy functions identically with or without access to information'], 0),
    ('Why is it useful to study the relationship between technology and government?', ['It helps explain how modern tools are reshaping civic participation and governance', 'This relationship has no relevance to social studies', 'Technology and government have no meaningful connection', 'Governance has remained completely unaffected by technology'], 0)])]),

day(49, [
L('Writing: Writing an Op-Ed (Opinion Editorial)',
  'Ontario Grade 7 Writing strand: an op-ed presents a writer’s opinion on a current issue, supported by reasoning and evidence, often published to persuade or inform public opinion.',
  [('An op-ed is written to ___.', ['Present the writer’s opinion on a current issue', 'Report only neutral facts with no opinion', 'Avoid discussing any current issues', 'Copy information without any analysis'], 0),
   ('A strong op-ed typically includes ___.', ['Reasoning and evidence to support the writer’s opinion', 'No supporting evidence at all', 'Only the writer’s name and nothing else', 'Random, unrelated information'], 0),
   ('Why might a writer choose to write an op-ed about a current issue?', ['To persuade or inform public opinion on a topic they care about', 'Op-eds never discuss real or current issues', 'Op-eds are always purely factual with no opinion involved', 'Writing an op-ed serves no persuasive purpose'], 0),
   ('Which is an example of a strong op-ed opening?', ['Our city urgently needs improved public transportation, and here is why.', 'This is an article.', 'Some things happen sometimes.', 'This piece has no clear topic.'], 0),
   ('Why is it useful for an op-ed to consider opposing viewpoints?', ['Addressing other perspectives can strengthen the credibility of the writer’s argument', 'Considering other viewpoints always weakens an op-ed', 'Op-eds should never mention any opposing views', 'This consideration has no effect on persuasive writing'], 0)]),
M('Probability: Expected Value',
  'Ontario Grade 7 Data Management strand: expected value is the average outcome you would predict over many trials, calculated by multiplying each possible outcome by its probability and adding the results together.',
  [('Expected value represents ___.', ['The average outcome predicted over many trials', 'A single guaranteed outcome every time', 'A value with no connection to probability', 'The highest possible outcome only'], 0),
   ('To calculate expected value, you ___.', ['Multiply each outcome by its probability and add the results', 'Only consider the highest possible outcome', 'Ignore probability completely', 'Divide all outcomes by two'], 0),
   ('If a game has a 50 percent chance of winning $10 and a 50 percent chance of winning $0, what is the expected value?', ['$0', '$5', '$10', '$20'], 1),
   ('Why might a business use expected value when evaluating a decision involving risk?', ['It helps estimate the average outcome over many repeated situations', 'Expected value has no practical business application', 'Expected value guarantees an exact outcome every single time', 'Businesses never consider probability in decision-making'], 0),
   ('If a raffle ticket has a 1 in 100 chance of winning $200 and otherwise wins $0, what is its expected value?', ['$2', '$200', '$100', '$0'], 0)]),
Sc('Erosion, Deposition, and Landform Change',
   'Ontario Grade 7 Science Earth and Space Systems strand: erosion moves weathered rock and soil, while deposition occurs when that material settles in a new location, together gradually reshaping landforms over time.',
   [('Erosion refers to the process of ___.', ['Moving weathered rock and soil to a new location', 'Creating brand new mountains instantly', 'Only affecting rocks underground', 'Preventing any landform changes'], 0),
    ('Deposition occurs when eroded material ___.', ['Settles in a new location', 'Disappears completely', 'Instantly turns into a mountain', 'Has no effect on landforms'], 0),
    ('Which of these can cause both erosion and deposition?', ['Rivers and wind', 'Only complete stillness', 'Only artificial materials', 'Nothing natural causes these processes'], 0),
    ('A river delta is often formed through the process of ___.', ['Deposition', 'Only erosion, with no deposition involved', 'Neither erosion nor deposition', 'A process unrelated to rivers'], 0),
    ('Why might erosion and deposition together take thousands of years to significantly reshape a landform?', ['These processes typically occur gradually rather than instantly', 'Landform changes always occur within a single day', 'These processes have no connection to landform formation', 'Landforms cannot change through natural processes'], 0)]),
SS('Climate Change Policy and International Agreements',
   'Ontario Grade 7 Social Studies People and Environments strand: countries often work together through international agreements to address climate change, setting shared goals for reducing greenhouse gas emissions and supporting sustainable development.',
   [('International agreements on climate change often aim to ___.', ['Set shared goals for reducing greenhouse gas emissions', 'Prevent any country from taking environmental action', 'Ignore the causes of climate change completely', 'Increase greenhouse gas emissions worldwide'], 0),
    ('Why might countries choose to cooperate through international climate agreements?', ['Climate change is a global issue requiring coordinated international action', 'Climate change only affects a single country', 'International cooperation provides no benefit for environmental issues', 'Countries never need to work together on environmental policy'], 0),
    ('Which is an example of a goal commonly included in climate policy agreements?', ['Reducing greenhouse gas emissions over time', 'Increasing pollution with no limits', 'Ignoring environmental impact entirely', 'Eliminating all forms of international cooperation'], 0),
    ('Sustainable development, often connected to climate policy, focuses on ___.', ['Meeting current needs without compromising the ability of future generations to meet theirs', 'Ignoring the needs of future generations entirely', 'Development that has no connection to environmental impact', 'A concept unrelated to climate policy'], 0),
    ('Why is it useful for students to study international climate policy?', ['It helps them understand how countries collaborate to address a shared global challenge', 'Climate policy has no connection to global issues', 'This topic has no relevance to social studies', 'International climate agreements have never actually existed'], 0)])]),

day(50, [
L('Reading: Synthesizing Multiple Perspectives into a Cohesive Argument',
  'Ontario Grade 7 Reading strand: synthesizing multiple perspectives means combining ideas and evidence from several sources or viewpoints to form a well-supported, cohesive argument or understanding.',
  [('Synthesizing multiple perspectives means ___.', ['Combining ideas and evidence from several sources into a cohesive understanding', 'Reading only one source and ignoring all others', 'Copying one text exactly with no analysis', 'Ignoring all available sources completely'], 0),
   ('Why might a reader consult multiple perspectives on the same issue?', ['To build a more complete and balanced understanding of the topic', 'One perspective always provides a complete understanding', 'Consulting multiple perspectives is unnecessary', 'Additional perspectives never add useful information'], 0),
   ('When synthesizing perspectives, a reader should look for ___.', ['Connections, agreements, and disagreements across sources', 'Only identical information repeated in every source', 'Nothing related to the sources’ content', 'Random, unrelated facts with no connections'], 0),
   ('Which is an example of synthesizing multiple perspectives?', ['Combining ideas from several articles to form a well-rounded argument', 'Reading only the title of one article', 'Ignoring every source except one', 'Copying a single paragraph exactly with no analysis'], 0),
   ('Why is synthesizing considered an advanced reading and writing skill?', ['It requires understanding, comparing, and combining ideas from multiple sources into a new argument', 'It requires no understanding of any source', 'It only involves reading a single sentence', 'It has no connection to critical thinking'], 0)]),
M('Review: Algebra, Exponents, Probability, and Geometry',
  'Ontario Grade 7 Number and Geometry strands review: this lesson revisits systems of linear relations, exponent laws, expected value, angle relationships in polygons, and equations with variables on both sides.',
  [('Simplify: x squared times x to the fourth power.', ['x to the sixth power', 'x to the eighth power', 'x squared', 'x to the second power'], 0),
   ('Solve for x: 2x + 5 = x + 12.', ['x = 5', 'x = 7', 'x = 17', 'x = 2'], 1),
   ('What is the sum of interior angles in a hexagon (6 sides)?', ['360 degrees', '540 degrees', '720 degrees', '900 degrees'], 2),
   ('If a raffle ticket has a 1 in 50 chance of winning $100, what is its expected value?', ['$1', '$2', '$50', '$100'], 1),
   ('Why is it useful to review algebra, exponents, probability, and geometry together?', ['These related math concepts reinforce each other for stronger overall understanding', 'These topics have no connection to each other', 'Review is never useful in math', 'Each topic must be learned in complete isolation'], 0)]),
Sc('Review: Body Systems, Technology, and Earth Processes',
   'Ontario Grade 7 Science review: this lesson revisits the endocrine, respiratory, circulatory, and immune systems, robotics, WHMIS symbols, space exploration, and erosion and deposition covered across recent lessons.',
   [('Which body system regulates the body using hormones released into the bloodstream?', ['The endocrine system', 'The respiratory system', 'The circulatory system', 'The excretory system'], 0),
    ('Which body system defends the body against harmful pathogens?', ['The immune system', 'The skeletal system', 'The muscular system', 'The digestive system'], 0),
    ('WHMIS symbols are used to communicate information about ___.', ['Hazardous materials', 'Weather patterns', 'Space missions', 'Musical instruments'], 0),
    ('Erosion and deposition together gradually reshape ___.', ['Landforms', 'The solar system', 'The human body', 'Robotic technology'], 0),
    ('Why is it valuable to review body systems, technology, and Earth processes together?', ['It helps connect and reinforce related science concepts learned across recent lessons', 'These topics are entirely unrelated to each other', 'Review provides no benefit in science', 'Each topic must always be studied in isolation'], 0)]),
SS('Review: 20th-Century History and Global Citizenship',
   'Ontario Grade 7 Social Studies review: this lesson revisits the Vietnam War, the fall of the Berlin Wall, apartheid, peacekeeping, multiculturalism, trade agreements, refugee crises, technology and government, and climate policy.',
   [('The fall of the Berlin Wall in 1989 symbolized the end of ___.', ['The Cold War era', 'World War I', 'The founding of the United Nations', 'Confederation'], 0),
    ('Apartheid was a system of racial segregation practiced in ___.', ['South Africa', 'Canada', 'France', 'Japan'], 0),
    ('United Nations peacekeeping missions aim to ___.', ['Maintain or restore peace in regions affected by conflict', 'Increase global conflict', 'Avoid any international involvement', 'Replace national governments'], 0),
    ('A refugee is generally someone forced to flee their home country due to ___.', ['Conflict or persecution', 'A vacation choice', 'A school field trip', 'A routine work assignment'], 0),
    ('Why is it useful to review 20th-century history and global citizenship topics together?', ['It helps reinforce how historical events connect to ongoing global cooperation and citizenship today', 'These topics have no meaningful connections', 'Review is never useful in social studies', 'Each topic must be studied with no connection to the others'], 0)])]),
]

def _rebalance_answer_positions(days, seed=20260718):
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
    _rebalance_answer_positions(g7_41_50)
    append_to(7, g7_41_50)
