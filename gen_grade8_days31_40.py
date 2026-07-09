#!/usr/bin/env python3
"""Phase 3: Grade 8, Days 31-40 (first Grade 8 batch, continuing the
10-day pattern used for Grades 3-7). Topics chosen to avoid any overlap
with the existing Day 1-30 set (see data/grade8.json): advanced
punctuation, satire, systems by substitution, intro trigonometry,
genetics/Punnett squares, evolution, DNA structure, and Canadian history
topics not yet covered (Fenian Raids, Northwest Resistance, Winnipeg
General Strike, Japanese Canadian internment, the October Crisis).

IMPORTANT: unlike Grades 3-7, Grade 8's fourth subject key is
"History" (not "SocialStudies") -- confirmed by grepping the existing
data/grade8.ts file before writing this batch.

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

L8 = 'https://tvolearn.com/pages/grade-8-language'
M8 = 'https://tvolearn.com/pages/grade-8-mathematics'
S8 = 'https://tvolearn.com/pages/grade-8-science-and-technology'
H8 = 'https://tvolearn.com/pages/grade-8-social-studies'
RL, RM, RS, RH = (
    'TVO Learn: Grade 8 Language',
    'TVO Learn: Grade 8 Mathematics',
    'TVO Learn: Grade 8 Science & Technology',
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


g8_31_40 = [
day(31, [
L('Grammar: Advanced Punctuation (Em Dashes, Colons, Semicolons)',
  'Grade 8 Writing strand: advanced punctuation marks like em dashes, colons, and semicolons each serve distinct purposes, such as adding emphasis, introducing a list, or joining closely related independent clauses.',
  [('An em dash is often used to ___.', ['Add emphasis or a dramatic pause', 'Replace every period in a text', 'Indicate the end of a paragraph only', 'Never appear in formal writing'], 0),
   ('A colon is commonly used to ___.', ['Introduce a list or explanation', 'End every sentence', 'Replace a comma in every instance', 'Begin a sentence'], 0),
   ('A semicolon can be used to ___.', ['Join two closely related independent clauses', 'Replace all periods in a paragraph', 'Separate unrelated ideas with no connection', 'Begin every sentence'], 0),
   ('Which sentence correctly uses a semicolon?', ['I love writing; it helps me think clearly.', 'I love writing, it helps me think clearly;', 'I love; writing it helps me think clearly.', 'I love writing it helps; me think clearly.'], 0),
   ('Why might a skilled writer use varied punctuation like em dashes and semicolons?', ['To add clarity, emphasis, and variety to sentence structure', 'Punctuation choice never affects a sentence’s tone or clarity', 'Advanced punctuation should always be avoided', 'These marks serve no grammatical purpose'], 0)]),
M('Solving Systems of Equations by Substitution',
  'Grade 8 Algebra strand: the substitution method solves a system of equations by solving one equation for a variable, then substituting that expression into the other equation.',
  [('The substitution method involves ___.', ['Solving one equation for a variable, then substituting it into the other equation', 'Graphing both equations with no algebraic steps', 'Ignoring one of the two equations entirely', 'Adding both equations together with no other steps'], 0),
   ('Solve the system using substitution: y = x + 2 and x + y = 10.', ['x = 4, y = 6', 'x = 2, y = 4', 'x = 6, y = 8', 'x = 8, y = 10'], 0),
   ('Why might substitution be a useful method when one equation is already solved for a variable?', ['It allows that expression to be directly substituted into the other equation', 'Substitution never works when a variable is isolated', 'This situation requires graphing instead of substitution', 'Substitution can only be used with three or more equations'], 0),
   ('Solve the system using substitution: y = 2x and x + y = 12.', ['x = 4, y = 8', 'x = 6, y = 12', 'x = 3, y = 6', 'x = 2, y = 4'], 0),
   ('After finding one variable’s value using substitution, the next step is typically to ___.', ['Substitute that value back into one of the original equations to find the other variable', 'Stop, since only one variable ever needs to be found', 'Ignore the second variable completely', 'Start the entire process over with new equations'], 0)]),
Sc('Genetics: Punnett Squares and Inheritance Patterns',
   'Grade 8 Science Life Systems strand: a Punnett square is a diagram used to predict the possible combinations of genes offspring might inherit from their parents, based on dominant and recessive traits.',
   [('A Punnett square is used to ___.', ['Predict possible gene combinations in offspring', 'Measure the size of an organism', 'Calculate an organism’s age', 'Determine an organism’s habitat'], 0),
    ('A dominant trait is one that ___.', ['Is expressed even if only one copy of the gene is present', 'Is never expressed under any circumstances', 'Only appears when two recessive genes are present', 'Has no connection to genetics'], 0),
    ('A recessive trait typically appears only when ___.', ['Two copies of the recessive gene are present', 'A single dominant gene is present', 'No genes are inherited at all', 'The trait is inherited from only one parent'], 0),
    ('If both parents carry one dominant and one recessive gene for a trait, a Punnett square can help predict ___.', ['The probability of each possible trait combination in their offspring', 'The exact traits every single offspring will have with certainty', 'Nothing useful about inheritance', 'Only traits unrelated to genetics'], 0),
    ('Why are Punnett squares a useful tool in genetics?', ['They provide a visual way to predict the probability of inherited traits', 'They have no practical use in studying genetics', 'They can guarantee exact outcomes with no uncertainty', 'They are unrelated to dominant and recessive traits'], 0)]),
H('The Fenian Raids and Early Canadian Defence',
  'Grade 8 History strand: the Fenian Raids were a series of attacks on British North America in the 1860s by Irish-American groups, which highlighted the need for stronger colonial defence and contributed to discussions about Confederation.',
  [('The Fenian Raids occurred primarily during which decade?', ['1810s', '1860s', '1900s', '1950s'], 1),
   ('The Fenian Raids were carried out by ___.', ['Irish-American groups', 'The French government', 'The Spanish military', 'A Canadian political party'], 0),
   ('The Fenian Raids targeted ___.', ['British North America', 'The United States', 'France', 'Mexico'], 0),
   ('Why are the Fenian Raids considered relevant to the discussion of Confederation?', ['They highlighted the need for stronger, unified colonial defence', 'They had no connection to Confederation discussions', 'They occurred after Confederation was already complete', 'They discouraged any consideration of uniting the colonies'], 0),
   ('Why do historians study events like the Fenian Raids when examining the path to Confederation?', ['They help explain some of the practical motivations behind uniting the colonies', 'These events have no historical significance', 'The Fenian Raids never actually took place', 'They are unrelated to Canadian colonial history'], 0)])]),

day(32, [
L('Writing: The Personal Statement',
  'Grade 8 Writing strand: a personal statement highlights a writer’s experiences, values, and goals, often used in applications, and requires clear, authentic, and well-organized writing.',
  [('A personal statement is meant to highlight a writer’s ___.', ['Experiences, values, and goals', 'Only their favourite foods', 'A completely unrelated topic', 'Someone else’s achievements'], 0),
   ('Why is authenticity important in a personal statement?', ['It helps the writing genuinely reflect who the writer is', 'Authenticity has no value in this type of writing', 'Personal statements should never reflect the actual writer', 'It replaces the need for clear organization'], 0),
   ('A well-organized personal statement typically includes ___.', ['A clear structure connecting experiences to goals or values', 'No structure of any kind', 'Only a list of unrelated random facts', 'Information about someone other than the writer'], 0),
   ('Why might a personal statement include specific examples from the writer’s life?', ['Specific examples make the writing more genuine and memorable', 'Examples are unnecessary in a personal statement', 'Personal statements should avoid all specific details', 'Specific examples always make writing weaker'], 0),
   ('What is one purpose of writing a personal statement?', ['To communicate who the writer is and what matters to them', 'To describe an entirely fictional character', 'To avoid any self-reflection', 'To copy someone else’s writing style exactly'], 0)]),
M('Introduction to Trigonometric Ratios (SOH-CAH-TOA)',
  'Grade 8 Geometry strand (pre-high-school extension): the trigonometric ratios sine, cosine, and tangent relate the angles of a right triangle to the ratios of its side lengths, often remembered using SOH-CAH-TOA.',
  [('In a right triangle, sine is defined as ___.', ['Opposite over hypotenuse', 'Adjacent over hypotenuse', 'Opposite over adjacent', 'Hypotenuse over opposite'], 0),
   ('In a right triangle, cosine is defined as ___.', ['Opposite over hypotenuse', 'Adjacent over hypotenuse', 'Opposite over adjacent', 'Hypotenuse over adjacent'], 1),
   ('In a right triangle, tangent is defined as ___.', ['Adjacent over hypotenuse', 'Opposite over hypotenuse', 'Opposite over adjacent', 'Hypotenuse over opposite'], 2),
   ('The acronym SOH-CAH-TOA helps students remember ___.', ['The definitions of sine, cosine, and tangent', 'The steps to solve a linear equation', 'A rule for factoring polynomials', 'The formula for a circle’s area'], 0),
   ('Trigonometric ratios apply specifically to ___.', ['Right triangles', 'Any triangle with no restrictions', 'Only equilateral triangles', 'Shapes with no angles at all'], 0)]),
Sc('Evolution and Natural Selection: An Introduction',
   'Grade 8 Science Life Systems strand: evolution describes how species change over generations, and natural selection is the process by which traits that improve survival and reproduction become more common over time.',
   [('Evolution describes how species ___.', ['Change over many generations', 'Never change at all', 'Instantly transform within a single lifetime', 'Have no connection to genetics'], 0),
    ('Natural selection favours traits that ___.', ['Improve an organism’s chances of survival and reproduction', 'Have no effect on survival', 'Always decrease an organism’s chances of survival', 'Are unrelated to an organism’s environment'], 0),
    ('Which is an example of a trait that might be favoured by natural selection in a cold climate?', ['Thicker fur for insulation', 'A trait that provides no benefit', 'A trait unrelated to survival', 'A trait that decreases warmth'], 0),
    ('Why might a population’s traits change over many generations?', ['Individuals with advantageous traits are more likely to survive and pass them on', 'Traits never change across generations', 'Natural selection has no connection to genetics', 'All individuals in a population are always identical'], 0),
    ('Why is natural selection considered a key concept in biology?', ['It helps explain how species adapt to their environments over time', 'It has no connection to how species change', 'Natural selection only applies to extinct species', 'This concept has no scientific basis'], 0)]),
H('The Northwest Resistance and Louis Riel',
  'Grade 8 History strand: the Northwest Resistance of 1885, led in part by Louis Riel, was a response by Métis and First Nations peoples to concerns over land rights and government policy in the Canadian West.',
  [('The Northwest Resistance took place in which year?', ['1867', '1885', '1914', '1931'], 1),
   ('Louis Riel played a significant role in leading resistance related to ___.', ['Métis and First Nations concerns over land rights', 'A conflict unrelated to Canadian history', 'European colonization of Africa', 'A war fought entirely overseas'], 0),
   ('The Northwest Resistance was partly a response to ___.', ['Concerns over land rights and government policy', 'A celebration with no underlying conflict', 'An agreement with no disputes involved', 'A conflict unrelated to Canadian expansion westward'], 0),
   ('Why is Louis Riel considered a significant, though controversial, figure in Canadian history?', ['He is seen by many as a defender of Métis rights amid a complex and disputed legacy', 'He has no connection to Canadian history', 'He is remembered with no controversy at all', 'His role in Canadian history is entirely unknown'], 0),
   ('Why do historians continue to study the Northwest Resistance today?', ['It highlights ongoing questions about land rights, government policy, and Indigenous relations', 'This event has no relevance to understanding Canada today', 'It was a minor event with no lasting significance', 'This event has no connection to Indigenous history'], 0)])]),

day(33, [
L('Reading: Analyzing Satire and Social Commentary',
  'Grade 8 Reading strand: satire uses humour, irony, and exaggeration to critique society, and analyzing it requires identifying the underlying message beneath the humour.',
  [('Satire is used to ___.', ['Critique society using humour, irony, or exaggeration', 'Present only literal, factual statements with no commentary', 'Avoid any deeper meaning', 'Praise society with no criticism at all'], 0),
   ('Why might analyzing satire require careful reading?', ['The critique is often hidden beneath humour or exaggeration', 'Satire always states its message directly with no interpretation needed', 'Satire never contains any deeper meaning', 'Satire is identical to purely factual writing'], 0),
   ('Which is an example of a technique used in satire?', ['Exaggerating a societal flaw to highlight it', 'Presenting only neutral, unbiased facts', 'Avoiding humour entirely', 'Removing all critique from the writing'], 0),
   ('Social commentary in satire often focuses on ___.', ['Issues within society, politics, or culture', 'Random, unrelated topics with no message', 'Only positive aspects with no criticism', 'Fictional worlds with no connection to real issues'], 0),
   ('Why might satire be considered a powerful tool for social critique?', ['Humour can make a serious critique more engaging and memorable', 'Satire has no persuasive power at all', 'Serious critique is always more effective without any humour', 'Satire removes all meaning from a critique'], 0)]),
M('Standard Deviation: An Introduction',
  'Grade 8 Data Management strand (pre-high-school extension): standard deviation measures how spread out data values are from the mean, with a larger standard deviation indicating more variability in the data.',
  [('Standard deviation measures ___.', ['How spread out data values are from the mean', 'The exact middle value of a data set', 'The most frequently occurring value', 'The total number of values in a data set'], 0),
   ('A larger standard deviation indicates ___.', ['More variability in the data', 'Less variability in the data', 'That all values are identical', 'That the mean cannot be calculated'], 0),
   ('A smaller standard deviation indicates that data values are generally ___.', ['Closer to the mean', 'Farther from the mean', 'Impossible to measure', 'Unrelated to the mean'], 0),
   ('Why might standard deviation be a useful statistic alongside the mean?', ['It shows how consistent or spread out the data really is', 'Standard deviation has no connection to understanding data', 'It always equals the mean, providing no new information', 'It should never be calculated alongside the mean'], 0),
   ('If two data sets have the same mean but different standard deviations, the set with the higher standard deviation ___.', ['Has more variability among its values', 'Has identical values to the other set', 'Cannot be compared to the other set', 'Always has a smaller range'], 0)]),
Sc('The Structure of DNA',
   'Grade 8 Science Life Systems strand: DNA is a molecule shaped like a double helix that carries genetic instructions, made up of four bases -- adenine, thymine, guanine, and cytosine -- that pair in specific combinations.',
   [('DNA is shaped like a ___.', ['Double helix', 'Perfect square', 'Flat sheet', 'Single straight line with no structure'], 0),
    ('DNA carries ___.', ['Genetic instructions for an organism', 'No useful information', 'Only information about diet', 'Information unrelated to biology'], 0),
    ('Which of these is one of the four bases found in DNA?', ['Adenine', 'Oxygen', 'Hydrogen', 'Carbon dioxide'], 0),
    ('In DNA, bases pair in specific combinations, such as adenine pairing with ___.', ['Thymine', 'Cytosine', 'Itself', 'No other base at all'], 0),
    ('Why is understanding DNA’s structure important in biology?', ['It helps explain how genetic information is stored and passed on', 'DNA structure has no connection to genetics', 'DNA plays no role in inherited traits', 'This structure has no scientific significance'], 0)]),
H('Women’s Suffrage in Canada: The Fight for the Vote',
  'Grade 8 History strand: the women’s suffrage movement in Canada fought for women’s right to vote, achieving major milestones at the federal level in 1918, though the timeline varied for different groups of women.',
  [('Women’s suffrage refers to the movement advocating for ___.', ['Women’s right to vote', 'The elimination of voting rights entirely', 'A movement unrelated to voting rights', 'Rights unrelated to political participation'], 0),
   ('Canadian women gained the right to vote in federal elections in which year?', ['1867', '1918', '1950', '1982'], 1),
   ('The timeline for women gaining the right to vote in Canada ___.', ['Varied for different groups of women', 'Was identical for every woman in Canada with no variation', 'Never actually changed over time', 'Has no connection to Canadian history'], 0),
   ('Why is the women’s suffrage movement considered a significant part of Canadian history?', ['It represented a major step toward expanding political rights and equality', 'It had no lasting impact on Canadian society', 'It occurred with no organized advocacy involved', 'This movement never actually took place'], 0),
   ('Why might historians note that suffrage timelines varied among different groups of Canadian women?', ['Not all women gained voting rights at the same time due to differing laws and barriers', 'All Canadian women gained the right to vote on the exact same day', 'This variation has no historical significance', 'Suffrage was never a contested or gradual process'], 0)])]),

day(34, [
L('Vocabulary: Etymology and Word Formation',
  'Grade 8 Language strand: understanding etymology (word origins) and word formation processes, such as compounding or blending, helps readers and writers build and interpret a stronger vocabulary.',
  [('Etymology is the study of ___.', ['A word’s origin and history', 'A word’s exact length', 'How to pronounce a word', 'Grammar rules for verbs'], 0),
   ('Compounding as a word formation process involves ___.', ['Combining two existing words to form a new one', 'Removing all letters from a word', 'Creating a word with no connection to existing words', 'Only shortening words with no combination'], 0),
   ('Blending as a word formation process involves ___.', ['Combining parts of two words into a new word, like brunch from breakfast and lunch', 'Using only whole, unaltered words', 'Removing all vowels from a word', 'A process unrelated to vocabulary'], 0),
   ('Why is understanding etymology useful when encountering unfamiliar words?', ['Recognizing familiar roots can help readers infer meaning', 'Etymology has no connection to understanding word meaning', 'Etymology only applies to very short words', 'Word origins never provide any useful clues'], 0),
   ('Which is an example of a blended word?', ['Smog (from smoke and fog)', 'Notebook', 'Basketball', 'Sunflower'], 0)]),
M('Rational Exponents and Radical Form',
  'Grade 8 Number strand (pre-high-school extension): a rational exponent, such as x to the power of one-half, represents a radical expression, such as the square root of x, connecting exponent and radical notation.',
  [('x to the power of one-half is equivalent to ___.', ['The square root of x', 'x squared', 'x times one-half', 'x to the power of two'], 0),
   ('x to the power of one-third is equivalent to ___.', ['The cube root of x', 'The square root of x', 'x divided by three', 'x to the power of three'], 0),
   ('A rational exponent connects which two mathematical concepts?', ['Exponents and radicals', 'Fractions and decimals only', 'Angles and triangles', 'Probability and statistics'], 0),
   ('What is 8 to the power of one-third?', ['2', '4', '8', '24'], 0),
   ('Why is it useful to understand the connection between rational exponents and radicals?', ['It allows expressions to be rewritten in whichever form is most useful for a given problem', 'Rational exponents have no connection to radicals', 'Radicals can never be expressed using exponents', 'This connection has no mathematical use'], 0)]),
Sc('Fluid Dynamics: Bernoulli’s Principle',
   'Grade 8 Science Structures and Mechanisms strand: Bernoulli’s Principle states that faster-moving fluid exerts less pressure than slower-moving fluid, a concept used to explain phenomena like airplane lift.',
   [('Bernoulli’s Principle states that faster-moving fluid exerts ___ pressure than slower-moving fluid.', ['More', 'Less', 'Exactly equal', 'Unpredictable'], 1),
    ('Bernoulli’s Principle helps explain how ___.', ['Airplane wings generate lift', 'Rocks form over time', 'Plants perform photosynthesis', 'Sound travels through solids'], 0),
    ('An airplane wing is shaped so that air travels ___ over the top of the wing than underneath.', ['Faster', 'Slower', 'At exactly the same speed', 'Not at all'], 0),
    ('According to Bernoulli’s Principle, if air moves faster over the top of a wing, the pressure there is ___.', ['Lower than below the wing, helping create lift', 'Higher than below the wing', 'Exactly equal to the pressure below the wing', 'Unrelated to lift generation'], 0),
    ('Why is Bernoulli’s Principle important in engineering fields like aviation?', ['It helps explain and predict how fluid movement affects pressure and lift', 'This principle has no real-world engineering applications', 'It only applies to solids, not fluids', 'Bernoulli’s Principle has no connection to flight'], 0)]),
H('The Winnipeg General Strike and Labour Movements',
  'Grade 8 History strand: the Winnipeg General Strike of 1919 was one of the largest labour strikes in Canadian history, reflecting broader worker concerns over wages, working conditions, and the right to organize.',
  [('The Winnipeg General Strike took place in which year?', ['1885', '1919', '1945', '1970'], 1),
   ('The Winnipeg General Strike is considered one of the largest examples of ___ in Canadian history.', ['Labour strikes', 'Elections', 'Immigration waves', 'Natural disasters'], 0),
   ('Workers involved in the strike were concerned about issues such as ___.', ['Wages and working conditions', 'Nothing related to labour concerns', 'Only unrelated political issues', 'Issues with no connection to employment'], 0),
   ('Why is the Winnipeg General Strike significant to the history of labour movements in Canada?', ['It reflected growing worker demands for fair treatment and the right to organize', 'It had no connection to labour rights', 'It discouraged any future labour organizing', 'This event never actually took place'], 0),
   ('Why do historians study labour movements like the Winnipeg General Strike?', ['They help explain the historical struggle for workers’ rights in Canada', 'Labour movements have no historical significance', 'Workers’ rights have never been a topic of historical concern', 'This event has no connection to Canadian history'], 0)])]),

day(35, [
L('Reading: Comparing Film and Text Adaptations',
  'Grade 8 Reading and Media Literacy strands: comparing a text to its film adaptation involves examining how elements like plot, character, and tone are preserved or changed when a story is adapted to a different medium.',
  [('Comparing a text to its film adaptation involves examining ___.', ['How elements like plot and tone are preserved or changed', 'Only the film’s runtime', 'Nothing related to the original text', 'The actors’ personal lives'], 0),
   ('Why might a film adaptation change certain details from the original text?', ['Different mediums may require different storytelling techniques or time constraints', 'Adaptations always follow the text exactly with no changes', 'Film adaptations never make any creative choices', 'Changes are always made with no purpose or reasoning'], 0),
   ('Which is an example of a change that might occur when adapting a novel into a film?', ['Combining or removing minor characters to fit the film’s length', 'The story remaining word-for-word identical to the book', 'No visual elements being added to the story', 'The film ignoring the story’s plot entirely'], 0),
   ('Why is comparing adaptations considered a valuable media literacy skill?', ['It helps readers understand how creative choices shape meaning across different formats', 'This comparison has no educational value', 'Adaptations are always identical to their source material', 'Media literacy has no connection to comparing formats'], 0),
   ('Tone in a film adaptation might be conveyed differently than in a text through ___.', ['Music, lighting, and visual effects', 'Only written description', 'No creative elements at all', 'A method identical to written text'], 0)]),
M('Volume and Surface Area of Spheres and Cones',
  'Grade 8 Geometry strand: the volume of a sphere is found using four-thirds pi r cubed, while the volume of a cone is found using one-third times the base area times height.',
  [('The formula for the volume of a sphere is ___.', ['Four-thirds pi r cubed', 'Pi r squared', 'One-third base area times height', 'Two pi r'], 0),
   ('The formula for the volume of a cone is ___.', ['One-third times base area times height', 'Base area times height', 'Four-thirds pi r cubed', 'Two times base area times height'], 0),
   ('A cone’s volume is what fraction of a cylinder’s volume with the same base and height?', ['One-half', 'One-third', 'Two-thirds', 'Equal to the cylinder’s volume'], 1),
   ('If a sphere has a radius of 3 units, which expression represents its volume?', ['Four-thirds pi times 3 cubed', 'Pi times 3 squared', 'One-third pi times 3 squared', 'Two pi times 3'], 0),
   ('Why might understanding the volume of cones and spheres be useful in real-world design?', ['Many real objects, like ice cream cones or balls, are based on these shapes', 'These shapes never appear in real-world objects', 'Volume calculations have no practical design applications', 'Cones and spheres have no measurable volume'], 0)]),
Sc('Robotics and Mechatronics',
   'Grade 8 Science and Technology strand: mechatronics combines mechanical engineering, electronics, and programming to design and build robotic systems that can sense, process, and respond to their environment.',
   [('Mechatronics combines which fields?', ['Mechanical engineering, electronics, and programming', 'Only art and music', 'Only agriculture and farming', 'A single unrelated field'], 0),
    ('A robotic system typically uses sensors to ___.', ['Gather information about its environment', 'Ignore all surrounding conditions', 'Prevent any interaction with its environment', 'Replace the need for programming'], 0),
    ('Programming plays a role in robotics by ___.', ['Instructing the robot on how to respond to different situations', 'Having no connection to robotic function', 'Replacing the need for mechanical parts', 'Preventing the robot from functioning'], 0),
    ('Why might mechatronics be considered an interdisciplinary field?', ['It combines knowledge and skills from multiple areas of engineering and technology', 'It relies on only a single area of study with no overlap', 'Mechatronics has no connection to engineering', 'This field only involves art and design'], 0),
    ('Which is an example of a real-world application of mechatronics?', ['An automated manufacturing robot', 'A simple hand-powered tool with no automation', 'A book with no technological components', 'A drawing with no mechanical elements'], 0)]),
H('Japanese Canadian Internment During WWII',
  'Grade 8 History strand: during World War II, the Canadian government forcibly relocated and interned thousands of Japanese Canadians, an action now widely recognized as a violation of their civil rights.',
  [('During World War II, the Canadian government forcibly relocated and interned ___.', ['Thousands of Japanese Canadians', 'No civilians of any background', 'Only foreign visitors to Canada', 'A group unrelated to Canadian history'], 0),
   ('Japanese Canadian internment is now widely recognized as ___.', ['A violation of civil rights', 'A fair and justified policy with no controversy', 'An event with no lasting historical significance', 'A policy that had no effect on those involved'], 0),
   ('Internment during this period often involved ___.', ['The loss of homes, property, and freedoms for those affected', 'No impact on the daily lives of those interned', 'Full protection of all rights and property', 'A policy welcomed by all those affected'], 0),
   ('Why is studying Japanese Canadian internment important for understanding Canadian history?', ['It highlights a significant instance of injustice and the importance of protecting civil rights', 'This event has no relevance to Canadian history', 'It reflects a policy with no lasting consequences', 'Internment never actually occurred in Canada'], 0),
   ('Why has the Canadian government formally acknowledged this period in more recent history?', ['To recognize the injustice experienced by Japanese Canadians and work toward reconciliation', 'The government has never acknowledged this event', 'This acknowledgment has no connection to historical injustice', 'The event required no formal recognition'], 0)])]),

day(36, [
L('Writing: The Extended Definition Essay',
  'Grade 8 Writing strand: an extended definition essay explores the deeper meaning of a complex or abstract term, such as courage or success, using examples, comparisons, and explanations beyond a simple dictionary definition.',
  [('An extended definition essay explores ___.', ['The deeper meaning of a complex or abstract term', 'Only a simple dictionary definition', 'A completely unrelated topic', 'A term with no meaningful complexity'], 0),
   ('Which is an example of a term suited for an extended definition essay?', ['Courage', 'The number three', 'A single letter of the alphabet', 'A random punctuation mark'], 0),
   ('An extended definition essay often uses ___.', ['Examples, comparisons, and explanations', 'Only a one-sentence definition with no elaboration', 'No supporting details at all', 'A definition copied directly from a dictionary'], 0),
   ('Why might a writer use a personal example to help define an abstract term like kindness?', ['Personal examples can make an abstract idea more concrete and relatable', 'Personal examples always weaken an extended definition', 'Abstract terms should never be explained with examples', 'Examples have no connection to definitions'], 0),
   ('Why is an extended definition essay more complex than a simple dictionary entry?', ['It explores multiple dimensions of meaning through detailed explanation and examples', 'It is exactly the same as a dictionary definition', 'Extended definitions never require any elaboration', 'Complex terms have no need for deeper explanation'], 0)]),
M('Introduction to Graphing Quadratic Functions',
  'Grade 8 Algebra strand (pre-high-school extension): a quadratic function, such as y equals x squared, produces a U-shaped graph called a parabola, with a vertex representing its minimum or maximum point.',
  [('The graph of a quadratic function is called a ___.', ['Parabola', 'Straight line', 'Circle', 'Triangle'], 0),
   ('The vertex of a parabola represents ___.', ['The minimum or maximum point of the graph', 'A random unrelated point', 'The starting point of the x-axis', 'The steepest possible slope'], 0),
   ('The graph of y equals x squared opens ___.', ['Upward', 'Downward only', 'Sideways only', 'In no particular direction'], 0),
   ('If a quadratic function’s graph opens downward, its vertex represents a ___.', ['Maximum point', 'Minimum point', 'Point with no significance', 'The y-intercept only'], 0),
   ('Why might quadratic functions be used to model real-world situations, like the path of a thrown ball?', ['Their U-shaped graph can represent situations that rise and then fall, or vice versa', 'Quadratic functions can never model real-world situations', 'Only straight-line graphs can represent real-world motion', 'Parabolas have no practical applications'], 0)]),
Sc('Renewable Energy Systems: Design and Efficiency',
   'Grade 8 Science and Technology strand: designing renewable energy systems, such as solar panel arrays or wind turbines, involves balancing energy output, cost, and environmental impact to maximize efficiency.',
   [('Designing a renewable energy system involves balancing ___.', ['Energy output, cost, and environmental impact', 'Nothing related to efficiency', 'Only the system’s colour', 'A single unrelated factor'], 0),
    ('Efficiency in a renewable energy system refers to ___.', ['How effectively the system converts a resource into usable energy', 'The system’s exact physical size', 'A factor unrelated to energy production', 'The system’s manufacturing date'], 0),
    ('Which factor might engineers consider when placing solar panels for maximum efficiency?', ['The amount and angle of sunlight exposure', 'The colour of nearby buildings only', 'Factors completely unrelated to sunlight', 'The panels’ weight alone'], 0),
    ('Why might engineers test multiple designs before finalizing a renewable energy system?', ['To determine which design offers the best balance of efficiency, cost, and impact', 'Testing designs serves no useful purpose', 'The first design attempted is always the most efficient', 'Multiple designs are never compared in engineering'], 0),
    ('Why is designing efficient renewable energy systems considered valuable?', ['It can help maximize energy production while reducing environmental impact and cost', 'Efficient design has no real-world benefits', 'Renewable energy systems cannot be designed for efficiency', 'This design process has no connection to environmental impact'], 0)]),
H('The Underground Railroad and Black History in Canada',
  'Grade 8 History strand: the Underground Railroad was a network that helped formerly enslaved people escape to freedom, with many settling in Canada, contributing significantly to Black Canadian history and communities.',
  [('The Underground Railroad was a network that helped ___.', ['Formerly enslaved people escape to freedom', 'Explorers travel to new territories', 'Immigrants travel by an actual railway system', 'Soldiers move during wartime'], 0),
   ('Many people who used the Underground Railroad settled in ___.', ['Canada', 'A country with no historical connection to this network', 'A location unrelated to this history', 'No location at all'], 0),
   ('Black Canadian communities established through this history contributed to ___.', ['Canada’s cultural and historical development', 'Nothing of historical significance', 'A history unrelated to Canada', 'A community with no lasting impact'], 0),
   ('Why is the history of the Underground Railroad significant to Canadian history?', ['It highlights an important chapter in Black Canadian history and the pursuit of freedom', 'It has no connection to Canadian history', 'This network never actually reached Canada', 'This history has no lasting significance'], 0),
   ('Why might learning about Black Canadian history be an important part of understanding Canada’s past?', ['It provides a fuller and more accurate understanding of Canada’s diverse history', 'Black Canadian history has no connection to Canada’s broader history', 'This history has no relevance to Canadian identity', 'Canada’s history should be studied with no consideration of diverse communities'], 0)])]),

day(37, [
L('Media Literacy: Deconstructing Clickbait and Digital Media',
  'Grade 8 Media Literacy strand: clickbait uses sensational or misleading headlines to attract clicks, often exaggerating or distorting the actual content, and recognizing these techniques helps readers evaluate digital media critically.',
  [('Clickbait is designed to ___.', ['Attract clicks using sensational or misleading headlines', 'Provide only accurate, neutral information', 'Avoid persuading readers to click at all', 'Always match the actual content exactly'], 0),
   ('Why might a clickbait headline exaggerate the actual content of an article?', ['To create curiosity or excitement that encourages clicks', 'Exaggeration never increases reader interest', 'Clickbait headlines are always completely accurate', 'This technique has no persuasive purpose'], 0),
   ('Which is a common sign of a clickbait headline?', ['Vague or sensational language that withholds key details', 'A headline that clearly and accurately summarizes the content', 'A headline with no emotional appeal whatsoever', 'A headline written entirely in plain, factual language'], 0),
   ('Why is it useful for readers to recognize clickbait techniques?', ['It helps them evaluate whether content is trustworthy before engaging with it', 'Recognizing these techniques has no practical value', 'All digital headlines are equally reliable', 'Clickbait techniques are impossible to identify'], 0),
   ('Which strategy can help a reader avoid falling for clickbait?', ['Reading beyond the headline to verify the actual content', 'Sharing an article based on the headline alone', 'Assuming every headline is completely accurate', 'Avoiding all critical evaluation of digital media'], 0)]),
M('Introduction to Permutations and Combinations',
  'Grade 8 Data Management strand (pre-high-school extension): a permutation counts arrangements where order matters, while a combination counts selections where order does not matter.',
  [('A permutation counts arrangements where ___.', ['Order matters', 'Order never matters', 'Only one arrangement is possible', 'No arrangement is being counted'], 0),
   ('A combination counts selections where ___.', ['Order does not matter', 'Order always matters', 'Only a single item can be selected', 'No selection is being made'], 0),
   ('Choosing 3 students from a group of 5 to form an unordered team is an example of ___.', ['A combination', 'A permutation', 'Neither a permutation nor a combination', 'An operation unrelated to counting'], 0),
   ('Arranging 3 students from a group of 5 in a specific order for a race is an example of ___.', ['A permutation', 'A combination', 'Neither a permutation nor a combination', 'An operation unrelated to counting'], 0),
   ('Why is it useful to distinguish between permutations and combinations?', ['It helps determine the correct method for counting different types of outcomes', 'These two concepts are always identical in every situation', 'This distinction has no real mathematical significance', 'Order never matters in any counting problem'], 0)]),
Sc('Space Science: Exoplanets and the Search for Life',
   'Grade 8 Science Earth and Space Systems strand: exoplanets are planets that orbit stars outside our solar system, and scientists study them to learn more about planetary systems and the possibility of life beyond Earth.',
   [('An exoplanet is a planet that orbits ___.', ['A star outside our solar system', 'Only our own Sun', 'No star at all', 'A planet within our own solar system'], 0),
    ('Scientists study exoplanets partly to explore the possibility of ___.', ['Life beyond Earth', 'Nothing related to life in the universe', 'Only the physical characteristics of our own Sun', 'A topic unrelated to space science'], 0),
    ('Which of these might scientists look for when studying whether an exoplanet could support life?', ['The presence of conditions suitable for liquid water', 'The exoplanet’s exact colour, with no other factors', 'A characteristic unrelated to habitability', 'The distance from Earth alone, with no other factors'], 0),
    ('Why is studying exoplanets valuable to our understanding of the universe?', ['It broadens knowledge of planetary systems and the potential for life elsewhere', 'Exoplanets provide no useful scientific information', 'This research has no connection to space science', 'Exoplanets do not actually exist'], 0),
    ('Which technology has helped scientists detect and study exoplanets?', ['Advanced telescopes', 'Simple household tools', 'Equipment unrelated to astronomy', 'No technology has ever been used for this purpose'], 0)]),
H('The October Crisis and Canadian Federalism',
  'Grade 8 History strand: the October Crisis of 1970 involved a series of kidnappings by the Front de libération du Québec (FLQ) and the federal government’s invocation of the War Measures Act, raising significant questions about civil liberties and federalism.',
  [('The October Crisis took place in which year?', ['1919', '1945', '1970', '2000'], 2),
   ('The October Crisis involved actions by a group known as ___.', ['The Front de libération du Québec (FLQ)', 'A group with no connection to Canadian history', 'An international organization unrelated to Quebec', 'A group active only outside of Canada'], 0),
   ('During the October Crisis, the federal government invoked ___.', ['The War Measures Act', 'No formal legal measures at all', 'A law unrelated to this crisis', 'An agreement with a foreign country'], 0),
   ('The October Crisis raised important questions about ___.', ['Civil liberties and the balance of federal power', 'Topics unrelated to Canadian governance', 'A subject with no historical significance', 'Issues unrelated to federalism'], 0),
   ('Why is the October Crisis significant to discussions of Canadian federalism?', ['It highlighted tensions and questions about federal authority during a national crisis', 'It had no connection to federal or provincial relations', 'This event has no lasting historical importance', 'The October Crisis never actually took place'], 0)])]),

day(38, [
L('Grammar: Style and Voice in Writing',
  'Grade 8 Writing strand: style and voice refer to the distinctive way a writer expresses ideas, shaped by choices in word choice, sentence structure, and tone, giving writing its own unique personality.',
  [('Voice in writing refers to ___.', ['The distinctive personality and expression of a writer', 'A rule about verb tense', 'A type of punctuation mark', 'The exact number of words in a sentence'], 0),
   ('Style in writing is shaped by choices such as ___.', ['Word choice, sentence structure, and tone', 'Only the colour of ink used', 'The page number of a piece of writing', 'A factor unrelated to language choices'], 0),
   ('Why might two writers describe the same event very differently?', ['Their individual style and voice shape how they express the same ideas', 'All writers are required to describe events identically', 'Style and voice have no effect on writing', 'Word choice never varies between writers'], 0),
   ('Which is an example of a stylistic choice a writer might make?', ['Using short, punchy sentences for a dramatic effect', 'Avoiding any consideration of sentence length', 'Writing with no consistent tone at all', 'Ignoring word choice entirely'], 0),
   ('Why is developing a personal writing voice considered valuable for a writer?', ['It helps make their writing distinctive and authentic', 'A personal voice has no value in writing', 'All writers should sound exactly the same', 'Voice only matters in poetry, not other forms of writing'], 0)]),
M('Number Systems: Classifying Real Numbers',
  'Grade 8 Number strand (pre-high-school extension): real numbers include natural numbers, whole numbers, integers, rational numbers, and irrational numbers, each nested within broader categories.',
  [('Which set of numbers includes both positive and negative whole numbers, along with zero?', ['Integers', 'Natural numbers', 'Irrational numbers only', 'A set unrelated to whole numbers'], 0),
   ('A rational number can always be expressed as ___.', ['A fraction of two integers', 'A number that cannot be written as a fraction', 'Only a whole number with no fractions allowed', 'A number unrelated to fractions'], 0),
   ('An irrational number, such as pi, ___.', ['Cannot be expressed exactly as a simple fraction', 'Can always be written as a simple fraction', 'Is always a whole number', 'Is not considered a real number'], 0),
   ('Which set of numbers includes 1, 2, 3, and so on, but not zero or negative numbers?', ['Natural numbers', 'Integers', 'Irrational numbers', 'Rational numbers only'], 0),
   ('Why is it useful to classify numbers into different categories, such as rational and irrational?', ['It helps clarify the properties and relationships between different types of numbers', 'Classifying numbers serves no mathematical purpose', 'All numbers belong to exactly the same single category', 'Number classification has no connection to mathematics'], 0)]),
Sc('Nanotechnology: An Introduction',
   'Grade 8 Science and Technology strand: nanotechnology involves designing and manipulating materials at an extremely small scale, often at the level of atoms and molecules, to create new materials and technologies.',
   [('Nanotechnology involves working at the scale of ___.', ['Atoms and molecules', 'Entire planets', 'Large buildings', 'A scale unrelated to materials science'], 0),
    ('Nanotechnology can be used to create ___.', ['New materials with unique properties', 'Nothing of practical use', 'Materials identical to all existing ones with no changes', 'Objects unrelated to science or technology'], 0),
    ('Which is a potential application of nanotechnology?', ['Developing stronger, lighter materials for various industries', 'A field with no real-world applications', 'A concept unrelated to material design', 'Technology that has no connection to materials'], 0),
    ('Why might scientists be interested in manipulating materials at such a small scale?', ['Materials can exhibit different, sometimes improved properties at the nanoscale', 'Materials behave identically regardless of their scale', 'Nanoscale manipulation has no scientific benefit', 'This scale of research has no real applications'], 0),
    ('Why is nanotechnology considered an emerging and significant field of study?', ['It has the potential to impact many industries, from medicine to engineering', 'Nanotechnology has no real-world significance', 'This field has no connection to modern technology', 'It only applies to a single, narrow application'], 0)]),
H('Canada’s Peacekeeping Legacy',
  'Grade 8 History strand: Canada developed a significant reputation for international peacekeeping in the mid-to-late 20th century, contributing personnel and resources to United Nations missions around the world.',
  [('Canada developed a significant reputation for ___ during the mid-to-late 20th century.', ['International peacekeeping', 'Avoiding all international involvement', 'A role unrelated to global affairs', 'Isolating itself from world events'], 0),
   ('Canadian peacekeeping efforts have often involved contributing to ___.', ['United Nations missions', 'No international organizations at all', 'A group unrelated to peacekeeping', 'Only domestic Canadian issues'], 0),
   ('Why might Canada have developed a strong reputation for peacekeeping?', ['Its consistent contributions of personnel and resources to international missions', 'Canada has never participated in any peacekeeping missions', 'This reputation has no connection to Canadian history', 'Peacekeeping missions have no international significance'], 0),
   ('Why is Canada’s peacekeeping legacy considered an important part of its national identity?', ['It reflects a value many Canadians associate with their country’s role in the world', 'This legacy has no connection to Canadian identity', 'Peacekeeping has no significance to Canada’s history', 'Canada’s international role has remained completely unknown'], 0),
   ('Studying Canada’s peacekeeping history helps students understand ___.', ['How Canada has positioned itself within international relations', 'That Canada has no history of international involvement', 'A topic with no relevance to Canadian history', 'That peacekeeping missions never actually occurred'], 0)])]),

day(39, [
L('Writing: The Extended Argumentative Research Paper',
  'Grade 8 Writing strand: an extended argumentative research paper presents a well-developed position on a complex issue, supported by thoroughly researched evidence from multiple credible sources.',
  [('An extended argumentative research paper is built around ___.', ['A well-developed position supported by thoroughly researched evidence', 'A single unsupported opinion', 'Random, unrelated information', 'A summary with no argument at all'], 0),
   ('Why is it important to use multiple credible sources in this type of paper?', ['It strengthens the argument with well-supported, reliable evidence', 'Multiple sources are never necessary', 'Using more than one source always weakens an argument', 'Credibility of sources has no bearing on the paper’s quality'], 0),
   ('Which is a feature commonly included in an extended argumentative research paper?', ['Properly cited sources supporting the argument', 'No structure or organization at all', 'Only casual, informal language throughout', 'A complete absence of evidence'], 0),
   ('Why might this type of paper address counterarguments?', ['Addressing other viewpoints can strengthen the credibility of the overall argument', 'Counterarguments should never be included in a research paper', 'Addressing other viewpoints always weakens an argument', 'This type of paper should ignore all opposing views'], 0),
   ('A strong conclusion in an extended argumentative research paper should ___.', ['Reinforce the main argument and its significance', 'Introduce a completely unrelated new topic', 'Contain no connection to the rest of the paper', 'Be identical to the paper’s introduction'], 0)]),
M('Proportional Reasoning: Similar Figures and Indirect Measurement',
  'Grade 8 Geometry strand: similar figures have proportional side lengths, which can be used for indirect measurement, such as calculating the height of a tall object using shadows and proportions.',
  [('Similar figures have side lengths that are ___.', ['Proportional to each other', 'Always identical in length', 'Completely unrelated to each other', 'Impossible to compare'], 0),
   ('Indirect measurement uses proportional relationships to ___.', ['Estimate a measurement that is difficult to measure directly', 'Replace the need for any measurement at all', 'Only measure objects that are easy to reach directly', 'Avoid using proportions entirely'], 0),
   ('If a 2-metre-tall person casts a 3-metre shadow, and a nearby tree casts a 12-metre shadow, how tall is the tree, using proportional reasoning?', ['6 metres', '8 metres', '9 metres', '18 metres'], 1),
   ('Why might indirect measurement be useful for measuring something like the height of a building?', ['It allows for an estimate without needing to physically measure the entire height directly', 'Indirect measurement can never be used for tall objects', 'This method has no real-world application', 'Proportional reasoning has no connection to measurement'], 0),
   ('For indirect measurement using shadows to work accurately, the objects being compared should ___.', ['Be measured under similar lighting conditions at the same time', 'Be measured under completely different conditions with no consistency', 'Have no proportional relationship at all', 'Never involve any shadows'], 0)]),
Sc('Biomedical Engineering: Innovations in Health Technology',
   'Grade 8 Science and Technology strand: biomedical engineering applies engineering principles to healthcare, developing technologies like prosthetics, medical imaging devices, and implantable devices to improve patient outcomes.',
   [('Biomedical engineering applies engineering principles to ___.', ['Healthcare and medical technology', 'A field unrelated to health or medicine', 'Only entertainment technology', 'Agriculture exclusively'], 0),
    ('Which is an example of a biomedical engineering innovation?', ['A prosthetic limb', 'A musical instrument', 'A type of clothing with no medical purpose', 'A tool unrelated to healthcare'], 0),
    ('Medical imaging devices, developed through biomedical engineering, help doctors ___.', ['See inside the body to diagnose health conditions', 'Have no way of understanding a patient’s condition', 'Avoid any use of technology in diagnosis', 'Replace the need for any medical training'], 0),
    ('Why might biomedical engineers work closely with healthcare professionals?', ['To design technologies that effectively meet real patient and medical needs', 'Biomedical engineers never need input from healthcare professionals', 'This collaboration has no benefit to patient care', 'Medical technology is designed with no consideration of patient needs'], 0),
    ('Why is biomedical engineering considered an important and growing field?', ['It has the potential to significantly improve patient care and health outcomes', 'This field has no impact on healthcare', 'Biomedical engineering has no real-world applications', 'It has no connection to improving medical technology'], 0)]),
H('The Indian Act and Its Historical Impact',
  'Grade 8 History strand: the Indian Act, first passed in 1876, is federal legislation that has significantly controlled many aspects of the lives of First Nations peoples in Canada, with lasting and often harmful effects.',
  [('The Indian Act was first passed in which year?', ['1867', '1876', '1931', '1982'], 1),
   ('The Indian Act is federal legislation that has significantly controlled aspects of the lives of ___.', ['First Nations peoples in Canada', 'A group unrelated to Canadian history', 'Only recent immigrants to Canada', 'No specific group of people'], 0),
   ('The historical effects of the Indian Act are widely recognized as ___.', ['Significant and often harmful', 'Entirely positive with no lasting concerns', 'Having no lasting effect at all', 'Unrelated to Indigenous history'], 0),
   ('Why is understanding the Indian Act important for studying Canadian history?', ['It reveals significant aspects of the relationship between the Canadian government and First Nations peoples', 'This legislation has no historical significance', 'The Indian Act never actually existed', 'It has no connection to Indigenous history in Canada'], 0),
   ('Why might discussions of reconciliation in Canada often reference the Indian Act?', ['Understanding its historical impact is seen as important to addressing ongoing challenges', 'The Indian Act has no connection to reconciliation efforts', 'Reconciliation discussions never reference historical legislation', 'This legislation has no relevance to modern Indigenous relations'], 0)])]),

day(40, [
L('Reading: Analyzing Multiple Narrators',
  'Grade 8 Reading strand: some texts use multiple narrators to present different perspectives on the same events, requiring readers to consider how each narrator’s point of view shapes the overall story.',
  [('A text with multiple narrators presents ___.', ['Different perspectives on the same events', 'Only a single unchanging viewpoint', 'No narration at all', 'A story with no characters'], 0),
   ('Why might an author choose to use multiple narrators?', ['To provide a fuller, more complex understanding of events through different perspectives', 'Multiple narrators always make a story less clear', 'This technique has no effect on how a story is understood', 'A story can never have more than one narrator'], 0),
   ('When reading a text with multiple narrators, readers should consider ___.', ['How each narrator’s perspective and potential bias shape their account', 'Only the very first narrator introduced', 'Nothing related to perspective or bias', 'That all narrators must present identical accounts'], 0),
   ('Which is an example of how using multiple narrators can affect a story?', ['Readers may see the same event interpreted differently by each narrator', 'All narrators always describe events in exactly the same way', 'Multiple narrators eliminate the need for any interpretation', 'This technique removes all perspective from a story'], 0),
   ('Why is analyzing multiple narrators considered an advanced reading skill?', ['It requires tracking and comparing different perspectives throughout a text', 'This skill requires no critical thinking', 'Texts with multiple narrators are always simple to understand', 'Multiple narrators never provide any additional insight'], 0)]),
M('Review: Systems, Trigonometry, and Advanced Number Concepts',
  'Grade 8 Number and Geometry strands review: this lesson revisits solving systems by substitution, introductory trigonometric ratios, standard deviation, rational exponents, and real number classification from recent lessons.',
  [('Solve the system using substitution: y = x + 3 and x + y = 9.', ['x = 3, y = 6', 'x = 4, y = 7', 'x = 6, y = 9', 'x = 9, y = 12'], 0),
   ('In a right triangle, sine is defined as ___.', ['Opposite over hypotenuse', 'Adjacent over hypotenuse', 'Opposite over adjacent', 'Hypotenuse over opposite'], 0),
   ('A larger standard deviation indicates ___.', ['More variability in the data', 'Less variability in the data', 'That all values are identical', 'That the mean cannot be calculated'], 0),
   ('x to the power of one-half is equivalent to ___.', ['The square root of x', 'x squared', 'x times one-half', 'x to the power of two'], 0),
   ('Why is it useful to review systems, trigonometry, and advanced number concepts together?', ['These related math concepts reinforce each other for stronger overall understanding', 'These topics have no connection to each other', 'Review is never useful in math', 'Each topic must be learned in complete isolation'], 0)]),
Sc('Review: Genetics, Evolution, and Emerging Technologies',
   'Grade 8 Science review: this lesson revisits Punnett squares, evolution and natural selection, DNA structure, robotics and mechatronics, and nanotechnology covered across recent lessons.',
   [('A Punnett square is used to ___.', ['Predict possible gene combinations in offspring', 'Measure the size of an organism', 'Calculate an organism’s age', 'Determine an organism’s habitat'], 0),
    ('Natural selection favours traits that ___.', ['Improve an organism’s chances of survival and reproduction', 'Have no effect on survival', 'Always decrease an organism’s chances of survival', 'Are unrelated to an organism’s environment'], 0),
    ('DNA is shaped like a ___.', ['Double helix', 'Perfect square', 'Flat sheet', 'Single straight line with no structure'], 0),
    ('Mechatronics combines mechanical engineering, electronics, and ___.', ['Programming', 'Only art and music', 'Only agriculture', 'A field unrelated to technology'], 0),
    ('Why is it valuable to review genetics, evolution, and emerging technologies together?', ['It helps connect and reinforce related science concepts learned across recent lessons', 'These topics are entirely unrelated to each other', 'Review provides no benefit in science', 'Each topic must always be studied in isolation'], 0)]),
H('Review: 19th and 20th-Century Canadian History',
  'Grade 8 History review: this lesson revisits the Fenian Raids, the Northwest Resistance, women’s suffrage, the Winnipeg General Strike, Japanese Canadian internment, and the October Crisis covered across recent lessons.',
  [('The Fenian Raids were carried out by ___.', ['Irish-American groups', 'The French government', 'The Spanish military', 'A Canadian political party'], 0),
   ('Louis Riel played a significant role in leading resistance related to ___.', ['Métis and First Nations concerns over land rights', 'A conflict unrelated to Canadian history', 'European colonization of Africa', 'A war fought entirely overseas'], 0),
   ('Canadian women gained the right to vote in federal elections in which year?', ['1867', '1918', '1950', '1982'], 1),
   ('During the October Crisis, the federal government invoked ___.', ['The War Measures Act', 'No formal legal measures at all', 'A law unrelated to this crisis', 'An agreement with a foreign country'], 0),
   ('Why is it useful to review 19th and 20th-century Canadian history topics together?', ['It helps reinforce how these historical events connect to shape modern Canada', 'These topics have no meaningful connections', 'Review is never useful in history', 'Each topic must be studied with no connection to the others'], 0)])]),
]

def _rebalance_answer_positions(days, seed=20260719):
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
    _rebalance_answer_positions(g8_31_40)
    append_to(8, g8_31_40)
