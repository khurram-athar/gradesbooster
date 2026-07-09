#!/usr/bin/env python3
"""Phase 3: Grade 10, Days 31-40 (first Grade 10 batch, continuing the
10-day pattern used for Grades 3-9). Topics chosen to avoid any overlap
with the existing Day 1-30 set (see data/grade10.json): postcolonial
literature, magical realism, deepfakes, rational functions, complex
numbers, solutions/concentration, thermodynamics, and 20th/21st-century
Canadian history not yet covered (the Head Tax, the 1995 referendum,
Meech Lake/Charlottetown, the Just Society, Western alienation).

IMPORTANT: Grade 10's subject keys are "English" and "History" (not
"Language" or "SocialStudies") -- confirmed by grepping the existing
data/grade10.ts before writing this batch.

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


g10_31_40 = [
day(31, [
E('Reading: Analyzing Postcolonial Literature',
  'Grade 10 English strand: postcolonial literature explores the experiences, identities, and perspectives of people and cultures affected by colonialism, often examining themes of power, identity, and voice.',
  [('Postcolonial literature often explores themes related to ___.', ['Power, identity, and voice in relation to colonialism', 'Only fictional worlds with no connection to real history', 'A topic entirely unrelated to colonialism', 'Grammar rules with no thematic content'], 0),
   ('Why might postcolonial literature give voice to perspectives historically underrepresented in mainstream literature?', ['It centres the experiences of people and cultures affected by colonial history', 'This genre never addresses historical perspectives', 'Postcolonial literature avoids any connection to real experiences', 'Underrepresented perspectives have no place in this genre'], 0),
   ('Which is an example of a theme commonly explored in postcolonial literature?', ['The complexity of cultural identity after colonial rule', 'A topic entirely unrelated to identity or history', 'Only fictional fantasy worlds with no historical grounding', 'Grammar and punctuation rules exclusively'], 0),
   ('Why is studying postcolonial literature valuable for readers?', ['It broadens understanding of diverse global perspectives and historical experiences', 'This genre has no educational value', 'Postcolonial literature has no connection to real-world history', 'Studying this genre narrows a reader’s perspective'], 0),
   ('Postcolonial authors often write from perspectives shaped by ___.', ['Their own or their community’s experience with colonialism', 'No connection to any historical or cultural context', 'A completely fictional, invented history', 'Perspectives unrelated to identity or culture'], 0)]),
M('Introduction to Rational Functions',
  'Grade 10 Functions strand: a rational function is a fraction where the numerator and denominator are polynomials, often producing graphs with asymptotes where the function is undefined.',
  [('A rational function is best described as ___.', ['A fraction where the numerator and denominator are polynomials', 'A function with no fractions involved', 'A function that is always undefined', 'A linear equation with no fractional component'], 0),
   ('An asymptote on a rational function’s graph represents ___.', ['A value the graph approaches but never actually reaches', 'The exact centre of the graph', 'A point where the graph always crosses the x-axis', 'A value unrelated to the function’s behaviour'], 0),
   ('A rational function is undefined at any x-value where ___.', ['The denominator equals zero', 'The numerator equals zero', 'Both the numerator and denominator equal one', 'The function has no real connection to x-values'], 0),
   ('Why might a rational function’s graph have a vertical asymptote?', ['The function becomes undefined at that x-value, causing the graph to approach infinity', 'Vertical asymptotes never occur in rational functions', 'The graph always crosses through a vertical asymptote', 'This feature has no connection to the denominator'], 0),
   ('Why are rational functions useful for modelling certain real-world situations, like rates?', ['They can represent relationships involving division, such as rates that change based on other values', 'Rational functions can never model real-world situations', 'These functions only apply to whole numbers, not real-world rates', 'This type of function has no practical use'], 0)]),
Sc('Chemistry: Solutions and Concentration',
   'Grade 10 Chemistry strand: a solution is a homogeneous mixture, and its concentration describes how much solute is dissolved in a given amount of solvent, often measured in units like molarity.',
   [('A solution is best described as ___.', ['A homogeneous mixture of substances', 'A mixture that always separates into visible layers', 'A pure substance with only one type of particle', 'A mixture unrelated to dissolving'], 0),
    ('Concentration describes ___.', ['How much solute is dissolved in a given amount of solvent', 'The exact colour of a solution', 'The temperature of a solution only', 'A property unrelated to dissolved substances'], 0),
    ('Molarity is a common unit used to express ___.', ['The concentration of a solution', 'The mass of a solid object', 'The temperature of a reaction', 'The volume of a gas only'], 0),
    ('If more solute is dissolved in the same amount of solvent, the concentration will generally ___.', ['Increase', 'Decrease', 'Remain completely unchanged', 'Become impossible to measure'], 0),
    ('Why is understanding concentration important in fields like medicine or chemistry?', ['Precise concentrations are often critical for safety and effectiveness in these fields', 'Concentration has no real-world importance', 'This concept has no connection to practical applications', 'Concentration is only relevant in purely theoretical chemistry'], 0)]),
H('Canada’s Peacekeeping Missions: Case Studies',
  'Grade 10 History strand: examining specific Canadian peacekeeping missions, such as those in Cyprus or the former Yugoslavia, illustrates the practical challenges and impact of Canada’s international peacekeeping role.',
  [('Case studies of Canadian peacekeeping missions help illustrate ___.', ['The practical challenges and impact of peacekeeping efforts', 'A topic entirely unrelated to Canadian history', 'Missions that never actually took place', 'Issues unrelated to international relations'], 0),
   ('Canadian peacekeeping missions have historically taken place in regions such as ___.', ['Cyprus and the former Yugoslavia', 'No international regions at all', 'Only within Canada’s own borders', 'A location entirely unrelated to peacekeeping efforts'], 0),
   ('Why might studying specific peacekeeping case studies be more informative than a general overview?', ['Case studies reveal specific challenges, decisions, and outcomes in real historical contexts', 'Case studies provide no additional insight beyond a general overview', 'Specific examples have no educational value', 'General overviews always provide more detail than case studies'], 0),
   ('Which is a potential challenge peacekeeping forces might face during a mission?', ['Navigating complex political and security situations in conflict zones', 'Peacekeeping missions never encounter any challenges', 'A challenge entirely unrelated to conflict or security', 'Missions that require no strategic planning at all'], 0),
   ('Why do historians study the outcomes of past peacekeeping missions?', ['To better understand the effectiveness and limitations of international intervention', 'These outcomes have no relevance to historical study', 'Peacekeeping missions have no measurable outcomes', 'This topic has no connection to Canadian history'], 0)])]),

day(32, [
E('Writing: The Personal Narrative for Applications',
  'Grade 10 English strand: a personal narrative written for applications highlights meaningful experiences and personal growth, using vivid detail and reflection to give readers insight into the writer’s character.',
  [('A personal narrative for applications is meant to ___.', ['Highlight meaningful experiences and personal growth', 'Describe a completely unrelated topic', 'Summarize only factual, impersonal information', 'Avoid any reflection on the writer’s experiences'], 0),
   ('Why might this type of narrative use vivid, specific detail?', ['It helps readers connect with and understand the writer’s experience more fully', 'Vivid detail always weakens this type of writing', 'Specific detail has no effect on how a narrative is received', 'This type of writing should avoid all descriptive detail'], 0),
   ('Why is reflection an important element of a personal narrative for applications?', ['It shows how the writer has grown or what they learned from an experience', 'Reflection has no role in this type of writing', 'Personal narratives should never include any reflection', 'This element replaces the need to describe the experience'], 0),
   ('Which is an example of a strong opening for a personal narrative about overcoming a challenge?', ['The first time I failed, I almost gave up -- but that moment changed everything.', 'This essay is about a challenge.', 'Challenges happen sometimes.', 'A sentence with no connection to the topic.'], 0),
   ('Why might readers of application narratives value authenticity over overly polished language?', ['A genuine voice can create a more meaningful and memorable impression', 'Authenticity has no value in this type of writing', 'Overly polished language always creates a stronger impression', 'Readers never care about the authenticity of a narrative'], 0)]),
M('Solving Trigonometric Equations',
  'Grade 10 Trigonometry strand: solving a trigonometric equation involves finding the angle or angles that satisfy a given trigonometric ratio, often using inverse trigonometric functions.',
  [('To solve a trigonometric equation for an unknown angle, you often use ___.', ['An inverse trigonometric function', 'Only addition, with no trigonometry involved', 'The Pythagorean theorem exclusively', 'A method unrelated to trigonometric ratios'], 0),
   ('If sine of an angle equals 0.5, which function would help find the angle?', ['Inverse sine', 'Inverse cosine', 'Inverse tangent', 'A function unrelated to trigonometry'], 0),
   ('Why might a trigonometric equation have more than one possible solution within a given range?', ['Trigonometric functions can produce the same ratio value at multiple angles', 'Trigonometric equations always have exactly one solution', 'Multiple solutions never occur in trigonometry', 'This situation has no connection to how trigonometric functions behave'], 0),
   ('Solving trigonometric equations is useful for problems involving ___.', ['Finding unknown angles in real-world situations, like navigation or engineering', 'Situations entirely unrelated to angles or triangles', 'Only theoretical problems with no practical application', 'Problems that never involve any angle measurements'], 0),
   ('Why is it important to consider the given range of possible angles when solving a trigonometric equation?', ['It helps identify all valid solutions within that specific range', 'The range of angles has no effect on the solutions found', 'Trigonometric equations never require a specified range', 'Considering the range always eliminates all possible solutions'], 0)]),
Sc('Biology: Cellular Respiration and Photosynthesis in Depth',
   'Grade 10 Biology strand: cellular respiration and photosynthesis are complementary processes -- photosynthesis captures and stores energy from sunlight, while cellular respiration releases that stored energy for cells to use.',
   [('Photosynthesis captures and stores energy from ___.', ['Sunlight', 'Only heat, with no connection to light', 'Sound waves', 'A source unrelated to light energy'], 0),
    ('Cellular respiration releases energy stored in ___.', ['Glucose', 'Only water, with no connection to glucose', 'Oxygen alone, with no other molecules involved', 'A source unrelated to stored chemical energy'], 0),
    ('Why are photosynthesis and cellular respiration considered complementary processes?', ['The products of one process are often used as inputs for the other', 'They have no relationship to each other', 'Only plants perform either process', 'These processes always occur completely independently with no connection'], 0),
    ('Which gas is released during photosynthesis and used during cellular respiration?', ['Oxygen', 'Nitrogen', 'Helium', 'A gas unrelated to either process'], 0),
    ('Why is understanding the relationship between these two processes important in biology?', ['It helps explain how energy flows through living systems, from producers to consumers', 'These processes have no connection to energy flow in ecosystems', 'This relationship has no scientific significance', 'Only one of these processes is relevant to understanding energy flow'], 0)]),
H('Constitutional Reform Attempts: Meech Lake and Charlottetown',
  'Grade 10 History strand: the Meech Lake Accord and Charlottetown Accord were failed attempts in the late 1980s and early 1990s to amend Canada’s constitution and address Quebec’s status within Confederation.',
  [('The Meech Lake Accord and Charlottetown Accord were attempts to ___.', ['Amend Canada’s constitution', 'Eliminate Canada’s constitution entirely', 'Create an entirely new country', 'Address issues unrelated to Canadian government'], 0),
   ('These accords were significantly focused on addressing ___.', ['Quebec’s status within Confederation', 'A topic with no connection to Canadian federalism', 'Issues unrelated to Canadian unity', 'A matter unrelated to constitutional change'], 0),
   ('Both the Meech Lake Accord and Charlottetown Accord ultimately ___.', ['Failed to be ratified', 'Were immediately successful with no challenges', 'Had no connection to Canadian politics', 'Were never actually proposed'], 0),
   ('Why are these accords significant to the study of Canadian federalism?', ['They reflect ongoing challenges in balancing regional and national interests within Canada', 'They have no connection to Canadian federalism', 'These accords never actually existed', 'This topic has no relevance to understanding Canadian government'], 0),
   ('Why might failed constitutional negotiations still be historically significant?', ['They reveal important tensions and priorities within a country’s political system', 'Failed negotiations have no historical value', 'Only successful agreements are ever studied in history', 'This topic has no connection to understanding Canadian unity'], 0)])]),

day(33, [
E('Grammar: Advanced Punctuation for Complex Ideas',
  'Grade 10 English strand: advanced punctuation, including semicolons, colons, and em dashes, helps writers express complex or nuanced relationships between ideas with clarity and precision.',
  [('A semicolon can be used to ___.', ['Join two closely related independent clauses', 'Replace all commas in a sentence', 'Separate unrelated ideas with no connection', 'Begin every sentence'], 0),
   ('An em dash is often used to ___.', ['Add emphasis or set off an important idea', 'Replace every period in a text', 'Indicate the end of a paragraph only', 'Never appear in formal writing'], 0),
   ('A colon is commonly used to ___.', ['Introduce a list or explanation', 'End every sentence', 'Replace a comma in every instance', 'Begin a sentence'], 0),
   ('Why might a writer use advanced punctuation to express a complex or nuanced idea?', ['It allows for precise control over how ideas are connected and emphasized', 'Advanced punctuation always makes ideas less clear', 'Complex ideas never benefit from careful punctuation choices', 'These marks serve no meaningful grammatical purpose'], 0),
   ('Why is mastering advanced punctuation valuable for academic and professional writing?', ['It supports clarity and precision when communicating sophisticated ideas', 'Punctuation choice has no effect on writing quality', 'Advanced punctuation should always be avoided in formal writing', 'These marks are only relevant in casual writing'], 0)]),
M('Exponential Functions: Growth and Decay',
  'Grade 10 Functions strand: an exponential function models growth or decay that occurs at a consistent percentage rate over time, distinct from the constant rate of change seen in linear functions.',
  [('An exponential growth function models a quantity that ___.', ['Increases by a consistent percentage rate over time', 'Increases by the same fixed amount each time period', 'Remains completely constant over time', 'Decreases at an unpredictable, random rate'], 0),
   ('An exponential decay function models a quantity that ___.', ['Decreases by a consistent percentage rate over time', 'Increases by a fixed amount each time period', 'Remains completely unchanged over time', 'Changes at a completely random rate'], 0),
   ('Which is an example of a real-world situation modelled by exponential decay?', ['The decreasing amount of a radioactive substance over time', 'A value that increases by the same fixed amount each year', 'A quantity that never changes over time', 'A straight-line decrease by a fixed amount each year'], 0),
   ('How does exponential growth differ from linear growth?', ['Exponential growth increases by a percentage rate, while linear growth increases by a fixed amount', 'They are always identical patterns of growth', 'Linear growth always increases faster than exponential growth', 'Exponential growth never actually increases over time'], 0),
   ('Why might exponential decay be used to model the cooling of a hot object over time?', ['The rate of temperature change often depends on the current temperature difference, similar to percentage-based decay', 'Cooling never follows any predictable mathematical pattern', 'Exponential functions can never model temperature changes', 'This situation is always better modelled with a linear function'], 0)]),
Sc('Physics: Circular Motion and Gravitation',
   'Grade 10 Physics strand: an object in circular motion experiences a centripetal force directed toward the centre of the circle, and gravitation describes the attractive force between objects with mass.',
   [('Centripetal force in circular motion is directed ___.', ['Toward the centre of the circle', 'Away from the centre of the circle', 'In a straight line with no connection to the circle', 'In a direction unrelated to the object’s motion'], 0),
    ('Gravitation describes the attractive force between ___.', ['Objects with mass', 'Only objects with no mass', 'A force unrelated to mass', 'Objects that repel each other, never attract'], 0),
    ('Why does an object moving in a circular path require a continuous centripetal force?', ['Without it, the object would move in a straight line rather than curve around the circle', 'Circular motion requires no force to be maintained', 'Centripetal force has no connection to circular motion', 'Objects naturally curve without any applied force'], 0),
    ('Which is an example of circular motion influenced by gravitation?', ['A planet orbiting the Sun', 'A ball rolling in a straight line on flat ground', 'An object at complete rest with no motion', 'A situation with no connection to gravity'], 0),
    ('Why is understanding gravitation important for explaining planetary orbits?', ['Gravitational attraction between the Sun and planets provides the force that keeps them in orbit', 'Gravitation has no connection to planetary motion', 'Planets orbit with no force acting upon them', 'This concept has no relevance to astronomy or physics'], 0)]),
H('The 1995 Quebec Referendum',
  'Grade 10 History strand: the 1995 Quebec Referendum asked voters whether Quebec should pursue sovereignty, resulting in a very close vote to remain within Canada, highlighting ongoing questions about national unity.',
  [('The 1995 Quebec Referendum asked voters whether Quebec should ___.', ['Pursue sovereignty', 'Immediately separate with no vote required', 'Remain permanently unchanged with no vote on the issue', 'A question entirely unrelated to Quebec’s status'], 0),
   ('The result of the 1995 referendum was ___.', ['A very close vote to remain within Canada', 'An overwhelming vote in favour of sovereignty', 'A vote with no meaningful result', 'A referendum that was never actually held'], 0),
   ('Why is the closeness of the 1995 referendum result considered historically significant?', ['It highlighted deeply divided opinions on Quebec’s status within Canada', 'The result showed universal agreement across Canada', 'Close results are never considered historically important', 'This referendum had no connection to Canadian unity'], 0),
   ('Why do historians continue to study the 1995 referendum today?', ['It reflects ongoing questions about national identity and unity in Canada', 'This event has no lasting historical significance', 'The referendum never actually took place', 'This topic has no connection to Canadian history'], 0),
   ('The 1995 referendum followed an earlier referendum on a similar question in which decade?', ['The 1980s', 'The 1860s', 'The 1930s', 'The 1950s'], 0)])]),

day(34, [
E('Literature: Exploring Magical Realism',
  'Grade 10 English strand: magical realism is a literary genre that blends realistic settings and characters with elements of the fantastical or magical, often used to explore deeper truths about culture and identity.',
  [('Magical realism blends ___.', ['Realistic settings and characters with fantastical elements', 'Only purely factual, non-fictional content', 'Two completely unrelated fictional genres with no connection', 'Only historical events with no fictional elements'], 0),
   ('Why might an author use magical realism to explore themes of culture or identity?', ['Fantastical elements can symbolically represent deeper cultural or emotional truths', 'Magical realism removes all deeper meaning from a story', 'This genre never connects to real cultural themes', 'Fantastical elements always distract from a story’s meaning'], 0),
   ('Which is a characteristic feature of magical realism?', ['Magical events treated as a normal part of an otherwise realistic world', 'A story set entirely in a fantasy world with no realistic elements', 'A completely factual account with no fictional elements', 'The total absence of any magical or fantastical elements'], 0),
   ('Why might readers find magical realism a distinctive literary experience?', ['It challenges typical boundaries between the real and the fantastical', 'This genre is identical to standard realistic fiction', 'Magical realism never differs from other literary genres', 'Readers experience no unique response to this genre'], 0),
   ('Magical realism is often associated with which broader literary tradition?', ['Latin American literature, among others', 'A tradition with no cultural or regional associations', 'Only ancient literature with no modern examples', 'A genre exclusive to a single, unnamed culture'], 0)]),
M('Arithmetic and Geometric Sequences and Series',
  'Grade 10 Number strand: an arithmetic sequence increases or decreases by a constant difference, while a geometric sequence increases or decreases by a constant ratio, and a series is the sum of a sequence’s terms.',
  [('An arithmetic sequence changes by a constant ___.', ['Difference', 'Ratio', 'Percentage that varies each time', 'Random amount'], 0),
   ('A geometric sequence changes by a constant ___.', ['Ratio', 'Difference', 'Random amount', 'A value unrelated to multiplication'], 0),
   ('In the arithmetic sequence 3, 7, 11, 15, what is the common difference?', ['4', '3', '7', '15'], 0),
   ('In the geometric sequence 2, 6, 18, 54, what is the common ratio?', ['3', '2', '4', '6'], 0),
   ('A series, in this context, refers to ___.', ['The sum of the terms in a sequence', 'A single individual term in a sequence', 'A sequence with no defined pattern', 'A concept unrelated to sequences'], 0)]),
Sc('Chemistry: Reaction Rates and Equilibrium',
   'Grade 10 Chemistry strand: reaction rate describes how quickly a chemical reaction occurs, and chemical equilibrium occurs when the rates of the forward and reverse reactions become equal.',
   [('Reaction rate describes ___.', ['How quickly a chemical reaction occurs', 'The exact colour of a chemical reaction', 'The total mass of reactants only', 'A concept unrelated to chemical reactions'], 0),
    ('Chemical equilibrium occurs when ___.', ['The rates of the forward and reverse reactions become equal', 'A reaction stops completely with no further activity', 'Only the forward reaction occurs, with no reverse reaction', 'A concept unrelated to reaction rates'], 0),
    ('Which factor can generally increase the rate of a chemical reaction?', ['Increasing the temperature', 'Removing all reactants from the reaction', 'Decreasing the concentration of reactants to zero', 'A factor unrelated to reaction conditions'], 0),
    ('Why might understanding reaction rates be important in industrial chemistry?', ['It helps optimize processes for efficiency, safety, and cost', 'Reaction rates have no practical relevance to industry', 'This concept only applies to theoretical chemistry', 'Industrial processes never consider reaction speed'], 0),
    ('At equilibrium, the concentrations of reactants and products ___.', ['Remain constant, though the reactions continue to occur', 'Are always exactly equal to each other', 'Become completely unpredictable', 'No longer change because all chemical activity has stopped'], 0)]),
H('Canada’s Immigration Policy: Historical Turning Points',
  'Grade 10 History strand: Canada’s immigration policy has evolved significantly over time, moving from more restrictive and discriminatory practices toward a points-based system emphasizing skills and diversity.',
  [('Canada’s immigration policy has evolved from ___.', ['More restrictive practices toward a points-based system', 'A points-based system toward more restrictive practices', 'No changes at all throughout Canadian history', 'A policy unrelated to immigration'], 0),
   ('A points-based immigration system generally emphasizes ___.', ['Skills and qualifications of prospective immigrants', 'No specific criteria for immigration', 'Only an applicant’s country of origin', 'Random selection with no defined criteria'], 0),
   ('Why is it important to study historical turning points in Canada’s immigration policy?', ['It reveals how Canadian society and values around immigration have changed over time', 'Immigration policy has never changed throughout Canadian history', 'This topic has no relevance to understanding Canadian history', 'Turning points in policy have no historical significance'], 0),
   ('Earlier Canadian immigration policies are now widely recognized as having included ___.', ['Discriminatory practices toward certain groups', 'Completely fair and equal treatment for all applicants throughout history', 'No formal policies of any kind', 'Policies unrelated to immigration'], 0),
   ('Why might reflecting on past immigration policies be valuable for understanding modern Canada?', ['It highlights how societal values and policies can change and improve over time', 'Past policies have no connection to present-day immigration', 'Reflection on this history serves no useful purpose', 'Immigration policy has always remained completely unchanged'], 0)])]),

day(35, [
E('Reading: Analyzing Graphic Novels',
  'Grade 10 English strand: graphic novels combine text and visual images to tell a story, requiring readers to analyze both written language and visual elements, such as panel layout and imagery, to understand meaning.',
  [('Graphic novels combine ___.', ['Text and visual images to tell a story', 'Only text, with no visual elements at all', 'Only images, with no written language', 'Neither text nor images'], 0),
   ('Analyzing a graphic novel requires readers to consider ___.', ['Both written language and visual elements like panel layout', 'Only the written dialogue, with no attention to images', 'Only the illustrations, with no attention to text', 'Neither the text nor the visual components'], 0),
   ('Why might panel layout be significant in a graphic novel?', ['It can influence pacing and how the story unfolds visually', 'Panel layout has no effect on how a story is understood', 'This element has no connection to visual storytelling', 'Panel layout is identical across every graphic novel'], 0),
   ('Which is an example of a visual storytelling technique used in graphic novels?', ['Varying panel size to emphasize a dramatic moment', 'Only using plain, unformatted text with no images', 'Avoiding any visual elements throughout the story', 'A technique unrelated to visual composition'], 0),
   ('Why are graphic novels considered a legitimate and complex literary form?', ['They require sophisticated interpretation of both textual and visual storytelling techniques', 'Graphic novels require no meaningful analysis or interpretation', 'This format has no connection to literary analysis', 'Visual storytelling techniques have no artistic or narrative value'], 0)]),
M('Correlation Coefficient and Line of Best Fit',
  'Grade 10 Data Management strand: the correlation coefficient measures the strength and direction of a linear relationship between two variables, ranging from negative one to positive one.',
  [('The correlation coefficient measures ___.', ['The strength and direction of a linear relationship between two variables', 'The exact number of data points in a set', 'The total sum of all data values', 'A value unrelated to relationships between variables'], 0),
   ('A correlation coefficient close to positive one suggests ___.', ['A strong positive relationship between the two variables', 'A strong negative relationship between the two variables', 'No relationship at all between the variables', 'A relationship that cannot be determined'], 0),
   ('A correlation coefficient close to zero suggests ___.', ['A very weak or no linear relationship between the variables', 'A perfect positive linear relationship', 'A perfect negative linear relationship', 'An undefined relationship'], 0),
   ('Why is the correlation coefficient useful when analyzing a scatter plot?', ['It provides a numerical measure of how closely the data follows a linear pattern', 'It has no connection to interpreting scatter plot data', 'This value can never be calculated from real data', 'The correlation coefficient only applies to non-linear relationships'], 0),
   ('Why is it important to remember that correlation does not necessarily indicate causation?', ['Two variables might be related without one directly causing the other', 'Correlation always proves that one variable causes the other', 'This distinction has no relevance to interpreting data', 'Causation can always be assumed from a correlation coefficient'], 0)]),
Sc('Biology: Biotechnology and Genetic Engineering',
   'Grade 10 Biology strand: biotechnology uses biological systems and organisms to develop products and technologies, with genetic engineering involving the direct manipulation of an organism’s DNA for specific purposes.',
   [('Biotechnology involves using biological systems to ___.', ['Develop products and technologies', 'A process entirely unrelated to biology', 'Only artistic creation, with no scientific basis', 'A field unrelated to any practical application'], 0),
    ('Genetic engineering involves the direct manipulation of an organism’s ___.', ['DNA', 'External appearance only, with no genetic changes', 'Diet, with no connection to genetics', 'A factor unrelated to biology'], 0),
    ('Which is an example of a real-world application of biotechnology?', ['Developing crops with improved resistance to pests', 'A field with no real-world applications', 'A concept unrelated to agriculture or medicine', 'Technology that has no connection to biological organisms'], 0),
    ('Why does genetic engineering raise ethical considerations?', ['It has the potential to significantly alter living organisms, raising questions about appropriate use', 'Genetic engineering has no ethical implications at all', 'This technology has no connection to living organisms', 'Ethical considerations are irrelevant to scientific research'], 0),
    ('Why is biotechnology considered an important and growing field?', ['It has the potential to address challenges in medicine, agriculture, and other industries', 'Biotechnology has no real-world significance', 'This field has no connection to modern science', 'Biotechnology only applies to a single, narrow application'], 0)]),
H('The Head Tax and Chinese Exclusion Act: A Historical Wrong',
  'Grade 10 History strand: the Chinese Head Tax and later Chinese Exclusion Act were discriminatory Canadian immigration policies targeting Chinese immigrants, now widely recognized as historical injustices.',
  [('The Chinese Head Tax was a policy that ___.', ['Required Chinese immigrants to pay a fee to enter Canada', 'Provided free entry for all immigrants', 'Had no connection to immigration policy', 'Applied equally to immigrants from every country'], 0),
   ('The Chinese Exclusion Act ___.', ['Significantly restricted Chinese immigration to Canada', 'Encouraged unlimited Chinese immigration to Canada', 'Had no effect on immigration policy', 'Applied to all immigrant groups equally'], 0),
   ('These policies are now widely recognized as ___.', ['Historical injustices', 'Fair and equal treatment with no lasting criticism', 'Policies with no lasting historical significance', 'Unrelated to Canadian immigration history'], 0),
   ('Why is it important to study historical policies like the Head Tax today?', ['It helps build understanding of past discrimination and its lasting impact', 'This history has no relevance to understanding Canada today', 'These policies never actually existed', 'This topic has no connection to Canadian history'], 0),
   ('Why might the Canadian government have formally acknowledged these historical policies in more recent years?', ['To recognize the injustice experienced by Chinese Canadians and work toward reconciliation', 'The government has never acknowledged this history', 'This acknowledgment has no connection to historical injustice', 'These policies required no formal recognition'], 0)])]),

day(36, [
E('Writing: The Literary Review',
  'Grade 10 English strand: a literary review evaluates a text’s strengths and weaknesses, offering a critical assessment supported by specific evidence and an overall judgment of its quality or significance.',
  [('A literary review offers ___.', ['A critical assessment of a text’s strengths and weaknesses', 'Only a plot summary with no evaluation', 'A completely unrelated topic', 'An assessment with no connection to the actual text'], 0),
   ('Why should a literary review include specific evidence from the text?', ['It supports the reviewer’s evaluation with concrete examples', 'Evidence is unnecessary in a literary review', 'A review should never reference the actual text', 'Evidence always weakens a critical evaluation'], 0),
   ('A well-balanced literary review typically discusses ___.', ['Both strengths and weaknesses of the text', 'Only positive aspects, with no critique', 'Only negative aspects, with no praise', 'Nothing specific about the text at all'], 0),
   ('Why might a literary review consider a text’s significance beyond just personal opinion?', ['It can help situate the text within a broader literary or cultural context', 'Personal opinion is the only valid basis for a review', 'Considering broader significance has no value in a review', 'Literary reviews should never go beyond simple opinion'], 0),
   ('Why is a literary review different from a simple book report?', ['A review involves critical evaluation and judgment, not just summary', 'A review and a book report are exactly the same', 'A review never includes any analysis', 'A book report always includes more critical analysis than a review'], 0)]),
M('Optimization Problems in Three Dimensions',
  'Grade 10 Measurement strand: three-dimensional optimization problems involve finding the dimensions that maximize or minimize a measurement, such as volume or surface area, often subject to given constraints.',
  [('A 3D optimization problem might involve finding dimensions that maximize ___.', ['Volume, subject to a given constraint', 'A completely random, unrelated value', 'Nothing measurable at all', 'Only colour, with no connection to measurement'], 0),
   ('Why might a company want to minimize the surface area of packaging while maintaining a fixed volume?', ['Minimizing surface area can reduce material costs while still holding the required amount of product', 'Surface area has no connection to packaging material costs', 'Minimizing surface area always increases the volume needed', 'This type of optimization has no real-world application'], 0),
   ('Solving a 3D optimization problem typically involves ___.', ['Setting up an equation relating the dimensions and then finding a maximum or minimum value', 'Ignoring all mathematical relationships between dimensions', 'Guessing dimensions with no calculation involved', 'A process unrelated to measurement or geometry'], 0),
   ('Why might real-world design challenges, like container design, be modelled as optimization problems?', ['They often involve balancing multiple factors, like cost and capacity, which optimization can help address', '3D optimization problems have no real-world design applications', 'Design challenges never involve any mathematical modelling', 'This type of problem only applies to purely theoretical situations'], 0),
   ('Why is understanding 3D optimization valuable for engineers and designers?', ['It helps them make efficient use of materials and space in real-world designs', '3D optimization has no practical value for engineering or design', 'Engineers never need to consider efficient use of materials', 'This mathematical skill has no connection to design work'], 0)]),
Sc('Physics: Thermodynamics -- Heat Transfer and Entropy',
   'Grade 10 Physics strand: thermodynamics studies heat and energy transfer, including the concept of entropy, which describes the tendency of energy to spread out and become more disordered over time.',
   [('Thermodynamics primarily studies ___.', ['Heat and energy transfer', 'Only sound waves, with no connection to heat', 'A field unrelated to energy', 'Only light, with no connection to thermal energy'], 0),
    ('Entropy describes ___.', ['The tendency of energy to spread out and become more disordered', 'A process where energy always becomes more concentrated over time', 'A concept unrelated to energy or disorder', 'The complete absence of any energy transfer'], 0),
    ('Heat transfer generally occurs from ___.', ['An area of higher temperature to an area of lower temperature', 'An area of lower temperature to an area of higher temperature, with no exceptions', 'No particular direction, occurring completely randomly', 'A process unrelated to temperature differences'], 0),
    ('Which is an everyday example of heat transfer?', ['A hot cup of coffee cooling down as it sits on a table', 'An object that never changes temperature under any conditions', 'A process unrelated to thermal energy', 'A situation where heat transfer never actually occurs'], 0),
    ('Why is understanding thermodynamics important in engineering, such as designing engines?', ['It helps engineers understand how energy can be transferred and used efficiently', 'Thermodynamics has no real-world engineering applications', 'This field of physics has no connection to energy efficiency', 'Heat transfer has no relevance to engine design'], 0)]),
H('Residential Schools and the Truth and Reconciliation Commission',
  'Grade 10 History strand: the residential school system caused significant harm to Indigenous children and communities across Canada, and the Truth and Reconciliation Commission was established to document this history and guide efforts toward healing.',
  [('The residential school system in Canada caused significant harm to ___.', ['Indigenous children and communities', 'No specific group of people', 'A group entirely unrelated to Canadian history', 'Only adults, with no effect on children'], 0),
   ('The Truth and Reconciliation Commission was established to ___.', ['Document the history of residential schools and guide efforts toward healing', 'Erase historical records completely', 'Ignore the experiences of residential school survivors', 'Prevent any future discussion of this history'], 0),
   ('The Truth and Reconciliation Commission gathered information partly by ___.', ['Listening to the experiences of residential school survivors', 'Refusing to speak with anyone affected', 'Only using fictional accounts', 'Ignoring all historical evidence'], 0),
   ('Why is learning about residential schools and the Truth and Reconciliation Commission important for students today?', ['It helps build understanding of this history and supports ongoing reconciliation efforts', 'This history has no relevance today', 'It should be avoided in schools entirely', 'It has no connection to Canadian identity'], 0),
   ('Reconciliation, in this context, refers to ___.', ['Working to repair relationships and address historical harms', 'Ignoring the effects of past policies', 'A type of sporting event', 'A type of geography lesson only'], 0)])]),

day(37, [
E('Media Literacy: Deepfakes and Digital Manipulation',
  'Grade 10 Media Literacy strand: deepfakes use artificial intelligence to create realistic but fabricated images, video, or audio, raising significant concerns about trust, misinformation, and digital literacy.',
  [('A deepfake is best described as ___.', ['A realistic but fabricated image, video, or audio created using artificial intelligence', 'A completely genuine, unaltered recording', 'A concept unrelated to digital media', 'A traditional photograph with no digital manipulation'], 0),
   ('Deepfakes raise significant concerns about ___.', ['Trust and the spread of misinformation', 'No concerns of any kind', 'Only entertainment value, with no other implications', 'A topic entirely unrelated to media literacy'], 0),
   ('Why might deepfakes be particularly challenging to detect?', ['Advances in technology can make fabricated content appear highly realistic', 'Deepfakes are always immediately obvious to viewers', 'This technology has no connection to realistic media', 'Detecting fabricated content requires no critical evaluation'], 0),
   ('Which strategy might help someone evaluate whether a video could be a deepfake?', ['Checking for verification from multiple credible sources', 'Assuming every video is automatically genuine', 'Ignoring the source of the video entirely', 'Sharing the video immediately without any verification'], 0),
   ('Why is understanding deepfakes considered an important digital literacy skill today?', ['This technology is increasingly capable of creating convincing but false content', 'Deepfakes have no real-world relevance', 'Digital literacy has no connection to evaluating media authenticity', 'This technology has no potential for misuse'], 0)]),
M('Introduction to Complex Numbers',
  'Grade 10 Number strand (extension): a complex number combines a real number and an imaginary number, where the imaginary unit i represents the square root of negative one, extending the number system beyond real numbers.',
  [('A complex number combines ___.', ['A real number and an imaginary number', 'Only whole numbers with no fractions', 'A concept unrelated to numbers', 'Only negative numbers, with no real component'], 0),
   ('The imaginary unit i is defined as ___.', ['The square root of negative one', 'The square root of one', 'A value equal to zero', 'A concept unrelated to square roots'], 0),
   ('Why were complex numbers introduced into mathematics?', ['To allow solutions to equations that have no solution using only real numbers', 'Complex numbers have no mathematical purpose', 'They were introduced to eliminate the need for real numbers', 'This concept has no connection to solving equations'], 0),
   ('Which of these is an example of a complex number?', ['3 plus 4i', 'Only the number 5', 'A number with no imaginary component at all', 'A number unrelated to the concept of i'], 0),
   ('Why might complex numbers be useful in fields like engineering, despite representing an extension beyond real numbers?', ['They can effectively model certain real-world systems, such as electrical circuits', 'Complex numbers have no practical, real-world applications', 'This concept is purely theoretical with no useful applications', 'Complex numbers can never be applied to physical systems'], 0)]),
Sc('Earth Science: Climate Systems and Modelling',
   'Grade 10 Earth Science strand: climate models use scientific data and mathematical relationships to simulate and predict how Earth’s climate system may change over time, informing policy and preparedness efforts.',
   [('Climate models use scientific data to ___.', ['Simulate and predict changes in Earth’s climate system', 'Have no connection to climate prediction', 'Replace the need for any climate data', 'Predict only past climate events, with no future projections'], 0),
    ('Why might climate models be useful for informing policy decisions?', ['They can help predict potential future impacts, guiding preparation and response', 'Climate models provide no useful information for policy', 'This scientific tool has no connection to decision-making', 'Policy decisions never rely on scientific modelling'], 0),
    ('Which factor might a climate model take into account?', ['Greenhouse gas concentrations in the atmosphere', 'A factor entirely unrelated to climate science', 'Only the colour of the sky, with no other data', 'A single, isolated weather event with no broader data'], 0),
    ('Why is climate modelling considered a complex scientific challenge?', ['It involves numerous interacting variables across the atmosphere, oceans, and land', 'Climate modelling involves no complex or interacting factors', 'This process requires no scientific data or calculation', 'Climate systems have no interacting components'], 0),
    ('Why might scientists continue to refine climate models over time?', ['New data and improved understanding can lead to more accurate predictions', 'Climate models never need to be updated or improved', 'Refining models has no connection to prediction accuracy', 'Climate science has no need for ongoing research'], 0)]),
H('Canada’s Role in NATO and International Security',
  'Grade 10 History strand: Canada has been a member of NATO since its founding in 1949, contributing to collective international security efforts alongside other member nations.',
  [('NATO was founded in which year?', ['1919', '1945', '1949', '1989'], 0),
   ('Canada’s membership in NATO involves contributing to ___.', ['Collective international security efforts', 'No international commitments of any kind', 'A topic entirely unrelated to Canadian foreign policy', 'Only domestic security, with no international connection'], 0),
   ('NATO is best described as ___.', ['An alliance of member nations focused on collective security', 'A single country acting entirely alone', 'An organization with no member countries', 'A group unrelated to international security'], 0),
   ('Why might countries choose to join an alliance like NATO?', ['To benefit from collective defence and security cooperation with other member nations', 'Alliances provide no benefit to member countries', 'NATO membership eliminates all need for national defence', 'This type of alliance has no connection to international security'], 0),
   ('Why is studying Canada’s role in NATO relevant to understanding its foreign policy?', ['It illustrates how Canada engages in international cooperation and security commitments', 'Canada has no role in NATO or international security', 'This topic has no connection to Canadian foreign policy', 'NATO membership has no effect on a country’s international relationships'], 0)])]),

day(38, [
E('Oral Communication: Debate and Rebuttal Techniques',
  'Grade 10 English strand: effective debate involves presenting a clear argument and using rebuttal techniques to directly and logically respond to an opposing side’s points.',
  [('A rebuttal in a debate is used to ___.', ['Directly and logically respond to an opposing argument', 'Ignore the opposing side’s points entirely', 'Repeat one’s own argument with no new response', 'Avoid engaging with any counterarguments'], 0),
   ('Why is it important for a debater to listen carefully to the opposing side’s argument?', ['It allows them to formulate an effective, relevant rebuttal', 'Listening has no effect on the quality of a rebuttal', 'Debaters should never consider what the other side says', 'A rebuttal can be effective with no understanding of the opposing argument'], 0),
   ('Which is an example of an effective rebuttal technique?', ['Directly addressing the opposing claim with counter-evidence', 'Ignoring the claim and changing the subject entirely', 'Repeating the same point without any new support', 'Responding with information unrelated to the claim'], 0),
   ('Why might a debater acknowledge a valid point from the opposing side before rebutting it?', ['It can demonstrate credibility and fairness while still defending their position', 'Acknowledging any opposing point always weakens a debater’s position', 'Debaters should never acknowledge points made by the other side', 'This approach has no strategic value in a debate'], 0),
   ('Why are debate and rebuttal skills valuable beyond formal debate settings?', ['They support critical thinking and effective communication in many real-world situations', 'These skills have no application outside of formal debates', 'Debate skills are irrelevant to everyday communication', 'Rebuttal techniques only apply to competitive debate events'], 0)]),
M('Transformations of Exponential Functions',
  'Grade 10 Functions strand: transformations of exponential functions, such as vertical shifts, stretches, and reflections, change the shape or position of the function’s graph in predictable ways.',
  [('A vertical shift of an exponential function’s graph moves it ___.', ['Up or down', 'Only left or right', 'In no particular direction', 'Only diagonally, with no vertical movement'], 0),
   ('A vertical stretch of an exponential function’s graph affects its ___.', ['Steepness or rate of change', 'Colour', 'Only its horizontal position', 'A property unrelated to the graph’s shape'], 0),
   ('A reflection of an exponential function’s graph across the x-axis would ___.', ['Flip the graph vertically', 'Have no effect on the graph at all', 'Only move the graph horizontally', 'Change the function into a linear function'], 0),
   ('Why is it useful to understand how transformations affect an exponential function’s graph?', ['It helps predict and interpret changes in real-world exponential models', 'Transformations have no effect on how a graph should be interpreted', 'This concept has no practical application', 'Exponential functions can never be transformed'], 0),
   ('If an exponential function is shifted up by 3 units, every y-value on the graph will ___.', ['Increase by 3', 'Decrease by 3', 'Remain completely unchanged', 'Become negative'], 0)]),
Sc('Chemistry: Electrochemistry',
   'Grade 10 Chemistry strand: electrochemistry studies the relationship between chemical reactions and electricity, including how batteries generate electric current through controlled chemical reactions.',
   [('Electrochemistry studies the relationship between ___.', ['Chemical reactions and electricity', 'Only sound and chemistry, with no connection to electricity', 'A field unrelated to chemical reactions', 'Only light, with no connection to chemistry'], 0),
    ('A battery generates electric current through ___.', ['Controlled chemical reactions', 'A process entirely unrelated to chemistry', 'Only mechanical movement, with no chemical involvement', 'A method that requires no chemical reaction at all'], 0),
    ('Which is an example of a device that relies on electrochemistry?', ['A battery', 'A device with no connection to chemical reactions', 'An object that generates no electric current', 'A tool unrelated to electricity or chemistry'], 0),
    ('Why is electrochemistry considered a practical application of chemistry?', ['It underlies technologies like batteries that are essential to modern life', 'Electrochemistry has no real-world applications', 'This field of chemistry has no connection to everyday technology', 'Batteries have no connection to chemical reactions'], 0),
    ('Why might scientists research new electrochemical technologies, such as improved batteries?', ['To develop more efficient and sustainable ways to store and use energy', 'Electrochemical research provides no benefit to energy technology', 'This research has no connection to energy storage', 'Improved batteries have no real-world significance'], 0)]),
H('The Just Society: Trudeau-Era Reforms',
  'Grade 10 History strand: Pierre Trudeau’s vision of a Just Society in the late 1960s and 1970s aimed to expand individual rights and reduce inequality, shaping significant social and legal reforms in Canada.',
  [('The Just Society was a vision associated with which Canadian prime minister?', ['Pierre Trudeau', 'A leader unrelated to Canadian history', 'A prime minister from an entirely different era', 'A vision with no specific political leader associated with it'], 0),
   ('The Just Society aimed to ___.', ['Expand individual rights and reduce inequality', 'Reduce individual rights significantly', 'Have no effect on Canadian society or law', 'A goal unrelated to rights or equality'], 0),
   ('Reforms associated with the Just Society era took place mainly during which decades?', ['The late 1960s and 1970s', 'The 1800s', 'The 1930s', 'The 2000s'], 0),
   ('Why is the Just Society considered a significant era in Canadian social history?', ['It contributed to major legal and social changes affecting individual rights', 'This era had no lasting impact on Canadian society', 'The Just Society had no connection to Canadian law or rights', 'This vision was never actually implemented in any way'], 0),
   ('Why might historians study this period alongside the later development of the Charter of Rights and Freedoms?', ['This era’s focus on individual rights helped shape later developments in Canadian rights protections', 'These two topics have no historical connection', 'The Just Society era occurred after the Charter was created', 'This period has no relevance to understanding Canadian rights history'], 0)])]),

day(39, [
E('Writing: Crafting a Personal Manifesto',
  'Grade 10 English strand: a personal manifesto expresses a writer’s core beliefs and values with a strong, declarative voice, clearly articulating what the writer stands for.',
  [('A personal manifesto is meant to express a writer’s ___.', ['Core beliefs and values', 'A completely unrelated topic', 'Someone else’s beliefs and values', 'A summary of unrelated facts'], 0),
   ('A manifesto is often written with a ___ voice.', ['Strong, declarative', 'Extremely vague and uncertain', 'Completely neutral with no personal viewpoint', 'A voice with no connection to the writer'], 0),
   ('Why might a writer use bold, direct statements in a personal manifesto?', ['To clearly and confidently communicate what they believe and stand for', 'Bold statements have no place in a manifesto', 'A manifesto should always avoid expressing clear beliefs', 'Direct statements always weaken this type of writing'], 0),
   ('Which is an example of a statement that might appear in a personal manifesto?', ['I believe curiosity should guide every choice I make.', 'The weather today is mild.', 'This is a random, unrelated fact.', 'A manifesto contains no personal statements.'], 0),
   ('Why might writing a personal manifesto help a writer reflect on their own identity?', ['It requires clearly articulating their values and what matters most to them', 'This type of writing has no connection to self-reflection', 'A manifesto never requires any personal reflection', 'Personal identity has no connection to this type of writing'], 0)]),
M('Solving Problems with the Sine Law and Cosine Law Together',
  'Grade 10 Trigonometry strand: some triangle problems require applying both the sine law and cosine law in sequence, depending on which sides and angles are known.',
  [('The sine law is most useful when you know ___.', ['An angle and its opposite side, along with another angle or side', 'Only two sides with no angle information', 'No information about the triangle at all', 'Three angles with no side information'], 0),
   ('The cosine law is especially useful when you know ___.', ['Two sides and the angle between them, or all three sides', 'Only two angles with no side information', 'No information about the triangle at all', 'A single angle with no other information'], 0),
   ('Why might a triangle problem require using both the sine law and cosine law in sequence?', ['Finding an initial unknown value with one law can provide the information needed to apply the other law next', 'These two laws are always used completely independently, never together', 'The sine law and cosine law can never be applied to the same triangle', 'Solving a triangle only ever requires a single trigonometric law'], 0),
   ('Why is it useful to be able to choose between the sine law and cosine law for a given triangle problem?', ['Different combinations of known information call for different, more efficient approaches', 'Only one of these laws should ever be used regardless of the given information', 'These trigonometric laws provide no practical benefit to solving triangles', 'Choosing between these laws has no effect on solving a problem correctly'], 0),
   ('Which law would generally be used first if you know all three side lengths of a triangle and need to find an angle?', ['The cosine law', 'The sine law', 'Neither law can be applied to this situation', 'The Pythagorean theorem is required instead of either law'], 0)]),
Sc('Biology: Microbiology and Infectious Disease',
   'Grade 10 Biology strand: microbiology studies microorganisms such as bacteria and viruses, including how pathogens cause infectious disease and how the immune system and medical interventions respond to them.',
   [('Microbiology studies ___.', ['Microorganisms such as bacteria and viruses', 'Only large mammals, with no connection to microorganisms', 'A field unrelated to biology', 'Only plants, with no connection to microorganisms'], 0),
    ('A pathogen is best described as ___.', ['A microorganism capable of causing disease', 'A type of healthy cell', 'A part of the skeletal system', 'A vitamin found in food'], 0),
    ('Which is an example of a medical intervention used to help the body respond to a pathogen?', ['A vaccine', 'A method with no connection to disease prevention', 'A tool unrelated to the immune system', 'A process that has no effect on pathogens'], 0),
    ('Why is understanding how infectious diseases spread important for public health?', ['It helps inform strategies to prevent and control outbreaks', 'This understanding has no connection to public health', 'Infectious disease spread cannot be studied or understood', 'Public health has no relevance to microbiology'], 0),
    ('Why might antibiotics be effective against bacterial infections but not viral infections?', ['Antibiotics target processes specific to bacteria, which differ significantly from how viruses function', 'Antibiotics are equally effective against all types of pathogens', 'Bacteria and viruses function in an identical way', 'This distinction has no connection to how these treatments work'], 0)]),
H('Regionalism in Canada: Western Alienation and Maritime Identity',
  'Grade 10 History strand: regionalism in Canada reflects how different parts of the country, such as the West and the Maritimes, have developed distinct political and cultural identities, sometimes leading to feelings of alienation from central Canada.',
  [('Regionalism in Canada refers to ___.', ['Distinct political and cultural identities developing in different parts of the country', 'A single, identical identity shared equally across all of Canada', 'A concept unrelated to Canadian geography or politics', 'The complete absence of any regional differences in Canada'], 0),
   ('Western alienation refers to feelings that ___.', ['Western Canadian interests are not adequately represented by central Canada', 'Western Canada has no distinct political interests', 'All regions of Canada feel equally represented at all times', 'Western Canada has no connection to Canadian politics'], 0),
   ('Maritime identity often reflects the region’s connection to ___.', ['The ocean, fishing industries, and local traditions', 'A factor entirely unrelated to the Maritime provinces', 'No specific historical or cultural influences', 'A concept unrelated to regional identity'], 0),
   ('Why is regionalism considered an important concept in Canadian history and politics?', ['It helps explain differing political priorities and tensions across the country', 'Regionalism has no connection to Canadian political history', 'All regions of Canada have always had identical political priorities', 'This concept has no relevance to understanding Canadian identity'], 0),
   ('Why might understanding regionalism help explain certain political debates in Canada?', ['Regional interests and identities can shape differing perspectives on national policy', 'Regionalism never influences political debates in Canada', 'National policy is always identical in every region', 'Regional identity has no connection to political perspectives'], 0)])]),

day(40, [
E('Reading: Comparative Analysis of Two Poems',
  'Grade 10 English strand: comparing two poems involves examining similarities and differences in theme, tone, structure, and poetic devices to develop a deeper understanding of each poem’s meaning.',
  [('A comparative analysis of two poems examines ___.', ['Similarities and differences in theme, tone, structure, and poetic devices', 'Only the exact number of lines in each poem', 'A single poem in complete isolation', 'The colour of each poem’s printed page'], 0),
   ('Why might comparing two poems on a similar theme deepen understanding of that theme?', ['Different poets’ approaches can reveal varied perspectives and techniques for exploring the same idea', 'Comparing poems never adds any additional insight', 'Poems on the same theme are always identical in approach', 'This comparison has no connection to understanding theme'], 0),
   ('Which is an example of a structural element that might be compared between two poems?', ['Their use of stanza length and rhyme scheme', 'Only the poems’ publication dates', 'The exact price of each poem’s book', 'A factor unrelated to poetic structure'], 0),
   ('Why is tone an important element to consider when comparing two poems?', ['Tone shapes how the reader emotionally experiences the ideas being expressed', 'Tone has no effect on how a poem is understood', 'Poems never differ in tone from one another', 'Comparing tone has no value in poetic analysis'], 0),
   ('Why is comparative analysis considered a valuable literary skill?', ['It develops critical thinking by requiring careful, detailed examination of multiple texts', 'This skill requires no careful analysis of the texts involved', 'Comparative analysis has no connection to critical thinking', 'Only a single poem needs to be considered for meaningful analysis'], 0)]),
M('Review: Functions, Sequences, and Trigonometric Applications',
  'Grade 10 Functions and Trigonometry strands review: this lesson revisits rational functions, exponential functions, arithmetic and geometric sequences, complex numbers, and combined sine/cosine law problems.',
  [('A rational function is best described as ___.', ['A fraction where the numerator and denominator are polynomials', 'A function with no fractions involved', 'A function that is always undefined', 'A linear equation with no fractional component'], 0),
   ('An exponential growth function models a quantity that ___.', ['Increases by a consistent percentage rate over time', 'Increases by the same fixed amount each time period', 'Remains completely constant over time', 'Decreases at an unpredictable, random rate'], 0),
   ('In the geometric sequence 2, 6, 18, 54, what is the common ratio?', ['3', '2', '4', '6'], 0),
   ('The imaginary unit i is defined as ___.', ['The square root of negative one', 'The square root of one', 'A value equal to zero', 'A concept unrelated to square roots'], 0),
   ('Why is it useful to review functions, sequences, and trigonometric applications together?', ['These related math concepts reinforce each other for stronger overall understanding', 'These topics have no connection to each other', 'Review is never useful in math', 'Each topic must be learned in complete isolation'], 0)]),
Sc('Review: Chemistry, Physics, and Biology Applications',
   'Grade 10 Science review: this lesson revisits solutions and concentration, circular motion, thermodynamics, electrochemistry, biotechnology, and microbiology covered across recent lessons.',
   [('Concentration describes ___.', ['How much solute is dissolved in a given amount of solvent', 'The exact colour of a solution', 'The temperature of a solution only', 'A property unrelated to dissolved substances'], 0),
    ('Centripetal force in circular motion is directed ___.', ['Toward the centre of the circle', 'Away from the centre of the circle', 'In a straight line with no connection to the circle', 'In a direction unrelated to the object’s motion'], 0),
    ('Entropy describes ___.', ['The tendency of energy to spread out and become more disordered', 'A process where energy always becomes more concentrated over time', 'A concept unrelated to energy or disorder', 'The complete absence of any energy transfer'], 0),
    ('A pathogen is best described as ___.', ['A microorganism capable of causing disease', 'A type of healthy cell', 'A part of the skeletal system', 'A vitamin found in food'], 0),
    ('Why is it valuable to review chemistry, physics, and biology applications together?', ['It helps connect and reinforce related science concepts learned across recent lessons', 'These topics are entirely unrelated to each other', 'Review provides no benefit in science', 'Each topic must always be studied in isolation'], 0)]),
H('Review: Constitutional Reform and Canadian Identity',
  'Grade 10 History review: this lesson revisits the Meech Lake and Charlottetown Accords, the 1995 referendum, the Head Tax, residential schools and reconciliation, the Just Society, and regionalism in Canada.',
  [('The Meech Lake Accord and Charlottetown Accord were attempts to ___.', ['Amend Canada’s constitution', 'Eliminate Canada’s constitution entirely', 'Create an entirely new country', 'Address issues unrelated to Canadian government'], 0),
   ('The result of the 1995 Quebec Referendum was ___.', ['A very close vote to remain within Canada', 'An overwhelming vote in favour of sovereignty', 'A vote with no meaningful result', 'A referendum that was never actually held'], 0),
   ('The Truth and Reconciliation Commission was established to ___.', ['Document the history of residential schools and guide efforts toward healing', 'Erase historical records completely', 'Ignore the experiences of residential school survivors', 'Prevent any future discussion of this history'], 0),
   ('Western alienation refers to feelings that ___.', ['Western Canadian interests are not adequately represented by central Canada', 'Western Canada has no distinct political interests', 'All regions of Canada feel equally represented at all times', 'Western Canada has no connection to Canadian politics'], 0),
   ('Why is it useful to review constitutional reform and Canadian identity topics together?', ['It helps reinforce how these historical developments connect to shape Canadian identity today', 'These topics have no meaningful connections', 'Review is never useful in history', 'Each topic must be studied with no connection to the others'], 0)])]),
]

def _rebalance_answer_positions(days, seed=20260723):
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
    _rebalance_answer_positions(g10_31_40)
    append_to(10, g10_31_40)
