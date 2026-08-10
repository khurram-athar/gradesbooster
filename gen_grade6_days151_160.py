#!/usr/bin/env python3
"""Grade 6, Days 151-160 -- extends Grade 6 from 150 to 160 days. Modeled
exactly on gen_grade6_days141_150.py: same L/M/Sc/SS helpers over
gen_curriculum's sub()/day()/append_to(), same TVO Learn placeholder
resourceLabel/resourceUrl convention (videoUrl intentionally left unset,
filled in later by the daily curriculum-video-backfill scheduled task).

Topics chosen to avoid any overlap with the existing Grade 6 Days 1-150
topics (see data/grade6.json), which already densely cover nearly the
entire grade 6 curriculum across all four subjects. New topics: reflexive
and intensive pronouns, identifying cause and effect in nonfiction texts,
synonyms and antonyms in context, writing a fable with a moral, giving and
receiving constructive feedback, understanding algorithms and personalized
feeds, using dashes and parentheses for extra information, comparing
primary and secondary sources, and collective nouns and group terms for
Language; surface area of triangular prisms, quartiles and interquartile
range, designing and running probability simulations, tessellations,
multiplying decimals using the standard algorithm, correlation versus
causation, allowance/saving/spending plans, percents greater than 100 and
less than 1, and finding volume using water displacement for Math; the
screw as a simple machine, DNA, homeostasis, biodegradable versus
non-biodegradable materials, whale migration, how exercise affects the
heart and lungs, desalination, rust and corrosion, and bird beak
adaptations for Science; and the Canadian Human Rights Commission, the
Highway of Heroes, Tommy Douglas and Canadian medicare, the Oka Crisis,
the Multiculturalism Act of 1988, the Fathers of Confederation, Emancipation
Day, the Winnipeg General Strike of 1919, and the Assembly of First Nations
for Social Studies -- none of those exact ideas appear in Days 1-150. Day
160 is a review day across all four subjects, matching the end-of-batch
pattern used in every prior 10-day batch; its four review titles are
worded distinctly from every earlier review days titles even though all
are review days. No embedded ASCII apostrophe or double-quote characters
are used anywhere in title/summary/question/option text -- apostrophes are
dropped entirely (e.g. "Canadas" not "Canada's"), matching the rest of
Grade 6.

Usage: python3 gen_grade6_days151_160.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_curriculum import sub, day, append_to

L6 = 'https://tvolearn.com/pages/grade-6-language'
M6 = 'https://tvolearn.com/pages/grade-6-mathematics'
S6 = 'https://tvolearn.com/pages/grade-6-science-and-technology'
SS6 = 'https://tvolearn.com/pages/grade-6-social-studies'
RL, RM, RS, RSS = (
    'TVO Learn: Grade 6 Language',
    'TVO Learn: Grade 6 Mathematics',
    'TVO Learn: Grade 6 Science and Technology',
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


def _rebalance_answer_positions(days, seed=20260809):
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


g6_151_160 = [
day(151, [
L('Grammar: Reflexive and Intensive Pronouns',
  'Grade 6 Language strand: a reflexive pronoun such as myself, yourself, or themselves refers back to the subject of a sentence, while an intensive pronoun uses the same forms only to add emphasis to a noun or pronoun already mentioned.',
  [('What does a reflexive pronoun do?', ['Refers back to the subject of a sentence', 'Always begins a new independent clause', 'Replaces a verb entirely', 'Joins two unrelated sentences together'], 0),
   ('Which of these is a reflexive pronoun?', ['Herself', 'She', 'Her', 'Hers'], 0),
   ('Which sentence uses an intensive pronoun for emphasis?', ['The principal himself greeted every student.', 'The principal greeted every student.', 'The students greeted the principal.', 'The principal greeted the students kindly.'], 0),
   ('How does an intensive pronoun differ from a reflexive pronoun?', ['An intensive pronoun only adds emphasis and can be removed without changing the meaning', 'An intensive pronoun always changes the meaning of a sentence completely', 'A reflexive pronoun is optional and never required', 'Intensive and reflexive pronouns are always spelled differently'], 0),
   ('Why might a writer choose to include an intensive pronoun?', ['To stress that a particular person, and no one else, performed an action', 'To make a sentence grammatically incomplete', 'To remove the subject from a sentence', 'Intensive pronouns are never used in careful writing'], 0)]),
M('Geometry: Surface Area of Triangular Prisms',
  'Grade 6 Math strand: the surface area of a triangular prism is the sum of the areas of its two triangular bases and its three rectangular faces, found by adding together all the flat surfaces that cover the shape.',
  [('What two kinds of faces make up a triangular prism?', ['Two triangular bases and three rectangular faces', 'Two rectangular bases and three triangular faces', 'Only triangular faces with no rectangles', 'Only rectangular faces with no triangles'], 0),
   ('How many rectangular faces does a triangular prism have?', ['Three', 'Two', 'Four', 'Five'], 0),
   ('Why might each face of a triangular prism need to be calculated separately?', ['The rectangular faces can have different widths depending on the triangles side lengths', 'Every face of a triangular prism is always identical', 'Surface area never requires measuring individual faces', 'Triangular prisms do not have separate measurable faces'], 0),
   ('What unit is the surface area of a triangular prism measured in?', ['Square units', 'Linear units', 'Cubic units', 'No units are needed'], 0),
   ('Why is finding surface area useful when designing a tent shaped like a triangular prism?', ['It helps determine how much fabric is needed to cover the entire structure', 'Surface area has no connection to how much material is needed', 'A tent shaped like a prism requires no fabric calculations', 'Surface area only applies to shapes with no triangular faces'], 0)]),
Sc('Simple Machines: The Screw and How It Works',
   'Grade 6 Science strand: a screw is a simple machine made of an inclined plane wrapped around a cylinder, and turning it converts rotational force into a straight line force that can hold materials together or lift objects.',
   [('What is a screw?', ['An inclined plane wrapped around a cylinder', 'A wheel connected to a rope', 'Two inclined planes joined at their bases', 'A lever with a fixed pivot point'], 0),
    ('What does turning a screw convert rotational force into?', ['A straight line force along the length of the screw', 'A force that only spins in circles forever', 'Heat energy with no other effect', 'Sound energy with no mechanical effect'], 0),
    ('Which everyday object is an example of a screw?', ['A jar lid', 'A seesaw', 'A pulley wheel', 'A wheelbarrow wheel'], 0),
    ('Why does a screw grip materials together effectively as it turns?', ['Its threads dig into the surrounding material, pulling surfaces together', 'A screw never makes contact with surrounding material', 'Screws only work when they are perfectly smooth', 'Turning a screw always loosens materials instead of tightening them'], 0),
    ('Why might a screw be considered a modified inclined plane?', ['Wrapping the incline around a cylinder lets a small turning force do a large amount of work over a short distance', 'A screw has no relationship at all to an inclined plane', 'An inclined plane can never be wrapped around a cylinder', 'Screws require no force to turn at all'], 0)]),
SS('Social Studies: The Canadian Human Rights Commission and Its Role',
   'Grade 6 Social Studies strand: the Canadian Human Rights Commission is a federal body that investigates complaints of discrimination and works to promote equality under Canadian law.',
   [('What is the main role of the Canadian Human Rights Commission?', ['To investigate complaints of discrimination and promote equality', 'To collect federal income taxes', 'To manage national parks and forests', 'To enforce traffic laws on highways'], 0),
    ('At what level of government does the Canadian Human Rights Commission operate?', ['The federal level', 'The municipal level only', 'The provincial level only', 'It operates outside of Canada'], 0),
    ('What might a person do if they experience discrimination covered by federal law?', ['File a complaint with the Commission', 'Ignore the situation entirely', 'Move to another country', 'Wait several years before taking any action'], 0),
    ('Why is it useful to have an independent commission handle discrimination complaints?', ['It can review cases fairly, separate from political influence', 'Independent commissions cannot make fair decisions', 'Only elected officials should handle such complaints', 'Independent bodies have no role in protecting rights'], 0),
    ('Why might promoting equality be considered an ongoing responsibility rather than a finished task?', ['Attitudes and circumstances continue to change, requiring continued education and enforcement', 'Equality was fully achieved as soon as the Commission was created', 'Discrimination no longer exists anywhere in Canada', 'Ongoing responsibilities never require government institutions'], 0)]),
]),
day(152, [
L('Reading: Identifying Cause and Effect in Nonfiction Texts',
  'Grade 6 Language strand: a cause is the reason something happens, while an effect is the result, and nonfiction writers often use signal words such as because, therefore, and as a result to show these relationships clearly.',
  [('What is a cause in a cause and effect relationship?', ['The reason something happens', 'The result of an event', 'A completely unrelated event', 'The title of a nonfiction text'], 0),
   ('What is an effect in a cause and effect relationship?', ['The result of an event', 'The reason something happens', 'The setting of a story', 'A characters opinion'], 0),
   ('Which word often signals a cause and effect relationship?', ['Therefore', 'Meanwhile', 'Previously', 'Yesterday'], 0),
   ('In the sentence The road flooded because of heavy rain, what is the cause?', ['Heavy rain', 'The road flooding', 'The time of year', 'The location of the road'], 0),
   ('Why is recognizing cause and effect important when reading nonfiction?', ['It helps readers understand why events happen and how ideas are connected', 'Cause and effect never appears in nonfiction writing', 'Nonfiction texts never explain why events occur', 'Readers do not need to understand relationships between events'], 0)]),
M('Data Management: Quartiles and Interquartile Range',
  'Grade 6 Math strand: quartiles divide an ordered data set into four equal parts, and the interquartile range is the difference between the third quartile and the first quartile, describing the spread of the middle half of the data.',
  [('What do quartiles do to an ordered data set?', ['Divide it into four equal parts', 'Divide it into two unequal parts', 'Remove the highest and lowest values', 'Rearrange the data set randomly'], 0),
   ('What is the interquartile range?', ['The difference between the third quartile and the first quartile', 'The difference between the highest and lowest values', 'The average of all values in a data set', 'The middle value of a data set'], 0),
   ('Which part of a data set does the interquartile range describe?', ['The spread of the middle half of the data', 'The spread of only the smallest values', 'The spread of only the largest values', 'It describes nothing about the data spread'], 0),
   ('Why might the interquartile range be more useful than the full range for describing spread?', ['It is less affected by extreme outlier values', 'It is always identical to the full range', 'It ignores the middle half of the data entirely', 'Outliers always make the interquartile range less accurate'], 0),
   ('If the first quartile is 10 and the third quartile is 25, what is the interquartile range?', ['15', '35', '10', '25'], 0)]),
Sc('DNA — The Blueprint of Life',
   'Grade 6 Science strand: DNA is a molecule found inside cells that carries the genetic instructions used for the growth, development, and functioning of living things, and is passed from parents to offspring.',
   [('What does DNA carry?', ['Genetic instructions for the growth and functioning of living things', 'Only information about an organisms diet', 'A record of an organisms daily behaviour', 'Energy used directly for muscle movement'], 0),
    ('Where in a cell is DNA typically found?', ['Inside the nucleus', 'Outside the cell entirely', 'Only in muscle tissue', 'Only in the bloodstream'], 0),
    ('How is DNA passed from one generation to the next?', ['It is passed from parents to their offspring', 'It is created new in every individual with no connection to parents', 'It only exists in adult organisms', 'DNA cannot be passed between generations'], 0),
    ('Why do siblings often share similar traits?', ['They inherit similar genetic instructions from their shared parents', 'Siblings never share any genetic similarities', 'Traits are determined entirely by the environment, not DNA', 'DNA has no connection to physical traits'], 0),
    ('Why is DNA sometimes compared to a blueprint?', ['It contains detailed instructions for building and operating a living organism', 'A blueprint and DNA have no meaningful similarities', 'DNA only affects the outward appearance of an organism', 'Blueprints and genetic material are identical substances'], 0)]),
SS('Social Studies: The Highway of Heroes — Honouring Canadian Fallen Soldiers',
   'Grade 6 Social Studies strand: the Highway of Heroes is a stretch of highway in Ontario where members of the public gather on overpasses to honour Canadian soldiers whose remains are being transported home, a tradition that began during the war in Afghanistan.',
   [('What is the Highway of Heroes?', ['A stretch of Ontario highway where the public honours fallen Canadian soldiers', 'A highway built exclusively for military vehicles', 'A monument located in Ottawa', 'A road built during the First World War'], 0),
    ('During what conflict did the Highway of Heroes tradition begin?', ['The war in Afghanistan', 'The First World War', 'The Second World War', 'The Korean War'], 0),
    ('Where do members of the public typically gather to honour fallen soldiers along this route?', ['On overpasses along the highway', 'Inside government buildings', 'At airports outside of Canada', 'Only inside private homes'], 0),
    ('Why might communities choose to gather publicly for this tradition?', ['To show collective respect and gratitude for the sacrifice of soldiers and their families', 'Public gatherings have no connection to honouring soldiers', 'The tradition discourages any public involvement', 'Communities are required by law to participate'], 0),
    ('Why is a tradition like the Highway of Heroes significant to Canadian identity?', ['It reflects a shared national value of honouring service and sacrifice', 'It has no connection to how Canadians view military service', 'Only government officials are permitted to observe the tradition', 'The tradition has no meaning to ordinary citizens'], 0)]),
]),
day(153, [
L('Vocabulary: Synonyms and Antonyms in Context',
  'Grade 6 Language strand: synonyms are words with similar meanings, while antonyms are words with opposite meanings, and choosing precise synonyms or antonyms in context can make writing clearer and more effective.',
  [('What is a synonym?', ['A word with a similar meaning to another word', 'A word with the opposite meaning of another word', 'A word borrowed from another language', 'A word that describes a place'], 0),
   ('What is an antonym?', ['A word with the opposite meaning of another word', 'A word with a similar meaning to another word', 'A word that sounds like another word', 'A word with no clear meaning'], 0),
   ('Which word is a synonym for happy?', ['Joyful', 'Sad', 'Angry', 'Tired'], 0),
   ('Which word is an antonym for generous?', ['Selfish', 'Kind', 'Giving', 'Caring'], 0),
   ('Why might a writer choose a specific synonym instead of repeating the same word?', ['To add variety and precision to their writing', 'Repeating the same word always improves clarity', 'Synonyms always change the meaning of a sentence', 'Using synonyms is never useful in writing'], 0)]),
M('Probability: Designing and Running Simulations',
  'Grade 6 Math strand: a simulation uses a model, such as flipping a coin or drawing coloured tiles, to estimate the probability of a real-world event when repeating the actual event many times would be impractical.',
  [('What is a simulation in probability?', ['A model used to estimate the probability of a real-world event', 'An event that happens only once and is never repeated', 'A guess made without any supporting data', 'A method that removes the need for probability entirely'], 0),
   ('Why might someone use a coin flip to simulate a real-world event with two equally likely outcomes?', ['A coin flip closely models two equally likely outcomes', 'Coin flips can only ever represent unequal probabilities', 'Simulations must always use dice, never coins', 'A coin flip cannot represent probability of any kind'], 0),
   ('Why are simulations useful when an actual event would be impractical to repeat many times?', ['They allow an estimate of probability without needing to repeat the real event repeatedly', 'Simulations always give less accurate results than doing nothing at all', 'Simulations replace the need to understand probability', 'Real events are always easier to repeat than a simulation'], 0),
   ('What might increase the accuracy of a probability simulation?', ['Running more trials of the simulation', 'Running the simulation only a single time', 'Ignoring the results of the simulation', 'Using a model unrelated to the real event'], 0),
   ('Why should the model used in a simulation closely match the real situation being studied?', ['A mismatched model can produce misleading probability estimates', 'The model used in a simulation never needs to relate to the real event', 'Simulations are always accurate regardless of the model chosen', 'Matching the model to the real event has no effect on accuracy'], 0)]),
Sc('Homeostasis — How the Body Maintains Balance',
   'Grade 6 Science strand: homeostasis is the process by which the body maintains a stable internal environment, such as regulating temperature and fluid levels, even when outside conditions change.',
   [('What is homeostasis?', ['The process by which the body maintains a stable internal environment', 'The process by which the body grows taller over time', 'A disease that affects the immune system', 'A type of cell found only in the brain'], 0),
    ('What is one example of something the body regulates through homeostasis?', ['Body temperature', 'Hair colour', 'Eye colour', 'Shoe size'], 0),
    ('What might the body do to cool down when it becomes too warm?', ['Sweat to release heat through evaporation', 'Immediately raise its internal temperature further', 'Stop all bodily functions completely', 'Grow additional hair for insulation'], 0),
    ('Why is maintaining a stable internal environment important for the body?', ['Many bodily processes function properly only within a narrow range of conditions', 'The bodys internal environment has no effect on its functioning', 'A stable internal environment is never necessary for survival', 'Body temperature and fluid levels never need to be regulated'], 0),
    ('Why might a persons body need to adjust differently in a very cold environment compared to a very hot one?', ['Homeostasis requires different responses depending on the outside conditions the body faces', 'The body responds identically no matter the outside temperature', 'Homeostasis only applies to warm environments', 'Cold and hot environments have no effect on the bodys internal balance'], 0)]),
SS('Social Studies: Tommy Douglas and the Origins of Canadian Medicare',
   'Grade 6 Social Studies strand: Tommy Douglas, a premier of Saskatchewan, introduced the first public health insurance program in North America in 1962, laying the foundation for the national Medicare system Canadians rely on today.',
   [('What was Tommy Douglas known for introducing?', ['The first public health insurance program in North America', 'The first Canadian national park', 'Canadas first official flag', 'The first Canadian space program'], 0),
    ('In what province did Tommy Douglas first introduce public health insurance?', ['Saskatchewan', 'Ontario', 'British Columbia', 'Nova Scotia'], 0),
    ('In approximately what year was this public health insurance program introduced?', ['1962', '1867', '1929', '1982'], 0),
    ('What did Tommy Douglass program eventually help create across Canada?', ['A national Medicare system available to all Canadians', 'A private insurance system available only to wealthy citizens', 'A national school system', 'A national transportation network'], 0),
    ('Why is Tommy Douglas often remembered as an important figure in Canadian history?', ['His work helped shape a health care system that continues to benefit Canadians today', 'His program had no lasting impact on Canadian society', 'He is remembered only for events unrelated to health care', 'Public health insurance was abandoned shortly after being introduced'], 0)]),
]),
day(154, [
L('Writing: Writing a Fable with a Moral',
  'Grade 6 Language strand: a fable is a short story, often featuring animal characters, that teaches a lesson called a moral, usually stated directly at the end of the story.',
  [('What is a fable?', ['A short story, often with animal characters, that teaches a lesson', 'A long novel with many chapters', 'A poem that must always rhyme', 'A factual newspaper article'], 0),
   ('What is a moral in a fable?', ['The lesson the story teaches', 'The name of the main character', 'The setting of the story', 'The title of the story'], 0),
   ('Where is the moral of a fable usually stated?', ['At the end of the story', 'Only in the title', 'At the very beginning, before any events occur', 'Morals are never stated directly in a fable'], 0),
   ('Why do fables often use animal characters instead of humans?', ['Animal characters can represent human behaviours in a simple, memorable way', 'Fables are never allowed to include animal characters', 'Animal characters make a story impossible to understand', 'Using animals removes the possibility of teaching a lesson'], 0),
   ('Why might a writer choose the fable form to teach a lesson about honesty?', ['A short, memorable story can make an abstract lesson easier to understand and remember', 'Fables are not an effective way to teach any lesson', 'Lessons about honesty cannot be taught through storytelling', 'A fable must always be about a completely unrelated topic'], 0)]),
M('Geometry: Tessellations — Tiling the Plane with Shapes',
  'Grade 6 Math strand: a tessellation is a pattern of shapes that fit together perfectly with no gaps or overlaps to cover a flat surface, and regular tessellations can be made using equilateral triangles, squares, or regular hexagons.',
  [('What is a tessellation?', ['A pattern of shapes that fit together with no gaps or overlaps', 'A single shape drawn on its own', 'A pattern with large gaps between shapes', 'A three-dimensional solid made of many faces'], 0),
   ('Which shape can form a regular tessellation on its own?', ['A square', 'A circle', 'A regular pentagon', 'An oval'], 0),
   ('Why can regular hexagons be used to create a tessellation?', ['Their interior angles allow them to fit together perfectly with no gaps', 'Hexagons always leave large gaps when placed together', 'Hexagons cannot be arranged in a repeating pattern', 'Regular hexagons have curved sides that prevent tiling'], 0),
   ('Why can regular pentagons not form a simple tessellation on their own?', ['Their interior angles do not divide evenly around a point, leaving gaps or overlaps', 'Pentagons have too many sides to ever be used in a pattern', 'Pentagons are not considered polygons', 'Every polygon can always tessellate on its own'], 0),
   ('Where might tessellations be seen in the real world?', ['In floor tiles and honeycomb patterns', 'Only inside computer software', 'Tessellations do not appear anywhere in nature or design', 'Only in three-dimensional sculptures'], 0)]),
Sc('Biodegradable versus Non-Biodegradable Materials',
   'Grade 6 Science strand: biodegradable materials, such as food scraps and paper, break down naturally through the action of decomposers, while non-biodegradable materials, such as many plastics, can persist in the environment for hundreds of years.',
   [('What does it mean for a material to be biodegradable?', ['It breaks down naturally through the action of decomposers', 'It never breaks down under any conditions', 'It can only be broken down by humans', 'It dissolves instantly in water'], 0),
    ('Which of these is an example of a biodegradable material?', ['A banana peel', 'A plastic bottle', 'A metal can', 'A glass jar'], 0),
    ('Approximately how long can some non-biodegradable plastics persist in the environment?', ['Hundreds of years', 'A few hours', 'A single day', 'Less than a week'], 0),
    ('What role do decomposers play in breaking down biodegradable materials?', ['They break down organic matter into simpler substances that return nutrients to the soil', 'Decomposers have no role in breaking down any materials', 'Decomposers only affect non-biodegradable plastics', 'Decomposers destroy soil nutrients rather than releasing them'], 0),
    ('Why is the buildup of non-biodegradable waste a concern for the environment?', ['It can accumulate in ecosystems and harm wildlife over long periods of time', 'Non-biodegradable waste always disappears quickly with no lasting effect', 'This type of waste has no impact on wildlife or ecosystems', 'Non-biodegradable materials break down faster than biodegradable ones'], 0)]),
SS('Social Studies: The Oka Crisis and Indigenous Land Rights',
   'Grade 6 Social Studies strand: the Oka Crisis was a 1990 land dispute between the Mohawk community of Kanesatake and the town of Oka, Quebec, over a proposed development on land considered sacred, drawing national attention to Indigenous land rights in Canada.',
   [('What was the Oka Crisis?', ['A 1990 land dispute between a Mohawk community and the town of Oka, Quebec', 'A federal election dispute in Ontario', 'A trade disagreement between Canada and another country', 'A dispute over a national park in British Columbia'], 0),
    ('In what year did the Oka Crisis take place?', ['1990', '1867', '1929', '1970'], 0),
    ('What was the land in dispute during the Oka Crisis being used for?', ['A proposed development on land considered sacred by the Mohawk community', 'A new national highway', 'A federal government building', 'An international airport'], 0),
    ('Why did the Oka Crisis draw significant national attention?', ['It highlighted ongoing tensions over Indigenous land rights across Canada', 'The event received no media coverage at the time', 'It had no connection to Indigenous rights issues', 'The dispute was resolved privately with no public awareness'], 0),
    ('Why might events like the Oka Crisis continue to be studied in Canadian history classes today?', ['They help explain ongoing discussions about land rights and reconciliation with Indigenous peoples', 'The event has no relevance to modern Canadian society', 'Land rights disputes no longer occur in Canada', 'The Oka Crisis has been completely forgotten by historians'], 0)]),
]),
day(155, [
L('Oral Communication: Giving and Receiving Constructive Feedback',
  'Grade 6 Language strand: constructive feedback identifies specific strengths and areas for improvement in a respectful way, helping a speaker or writer grow, while receiving feedback well involves listening carefully without becoming defensive.',
  [('What is constructive feedback?', ['Feedback that identifies specific strengths and areas for improvement respectfully', 'Feedback that only criticizes without offering any useful direction', 'Feedback that avoids mentioning any strengths or weaknesses', 'Feedback given only after a final grade is assigned'], 0),
   ('Why is it helpful for feedback to be specific rather than general?', ['Specific feedback gives the person clear guidance on what exactly to improve', 'General feedback is always more useful than specific feedback', 'Specific feedback makes it harder to understand what to improve', 'Feedback does not need to explain anything to be useful'], 0),
   ('What is an important skill when receiving feedback?', ['Listening carefully without becoming defensive', 'Immediately arguing against every comment made', 'Ignoring all feedback completely', 'Refusing to consider any suggestions'], 0),
   ('Why might a peer editing group agree on respectful language before giving feedback?', ['It helps ensure feedback is delivered constructively rather than hurtfully', 'Respectful language makes feedback less useful', 'Peer groups should avoid using any language at all', 'Feedback is always effective regardless of how it is delivered'], 0),
   ('Why is constructive feedback considered valuable for improving a piece of writing?', ['It offers an outside perspective that can reveal strengths and weaknesses the writer may not notice', 'Feedback from others is never useful for improving writing', 'Only the original writer can ever identify areas for improvement', 'Constructive feedback always weakens a piece of writing'], 0)]),
M('Number Sense: Multiplying Decimals Using the Standard Algorithm',
  'Grade 6 Math strand: multiplying decimals using the standard algorithm involves multiplying the numbers as if they were whole numbers, then placing the decimal point in the product based on the total number of decimal places in the factors.',
  [('What is the first step when multiplying two decimal numbers using the standard algorithm?', ['Multiply the numbers as if they were whole numbers', 'Immediately place the decimal point before multiplying', 'Round both numbers to the nearest whole number', 'Add the two decimal numbers together'], 0),
   ('How is the position of the decimal point determined in the final product?', ['By counting the total number of decimal places in both factors', 'By always placing it after the first digit', 'By guessing where it looks correct', 'By counting only the decimal places in the larger factor'], 0),
   ('What is the product of 0.4 multiplied by 0.3?', ['0.12', '0.7', '1.2', '0.012'], 0),
   ('If one factor has one decimal place and another has two decimal places, how many decimal places should the product have?', ['Three', 'One', 'Two', 'Four'], 0),
   ('Why is it useful to estimate the product before multiplying two decimals precisely?', ['It helps check whether the final answer and decimal placement are reasonable', 'Estimating always produces the exact same result as multiplying precisely', 'Estimation has no connection to checking the accuracy of an answer', 'Decimal placement never needs to be checked after calculating'], 0)]),
Sc('Whale Migration and Ocean Navigation',
   'Grade 6 Science strand: many whale species migrate thousands of kilometres each year between cold feeding grounds and warm breeding waters, navigating using landmarks, ocean currents, and the Earths magnetic field.',
   [('Why do many whale species migrate long distances each year?', ['To travel between cold feeding grounds and warm breeding waters', 'To avoid all contact with other whales', 'Whales do not actually migrate at all', 'To find colder water for the entire year'], 0),
    ('What is one method scientists believe whales use to navigate during migration?', ['Sensing the Earths magnetic field', 'Following road signs placed in the ocean', 'Using only the position of nearby cities', 'Whales do not use any navigation methods'], 0),
    ('Why might whales migrate toward warmer waters to give birth?', ['Warmer waters may offer safer and more suitable conditions for newborn calves', 'Warmer waters are always more dangerous for newborn calves', 'Whales never give birth in warm waters', 'Water temperature has no effect on newborn whales'], 0),
    ('What might disrupt a whales ability to navigate accurately during migration?', ['Ocean noise pollution from human activity', 'Calm, quiet ocean conditions', 'The presence of other whales nearby', 'Clear water with no obstacles'], 0),
    ('Why is understanding whale migration patterns important for ocean conservation efforts?', ['It helps identify and protect the routes and habitats whales depend on', 'Migration patterns have no connection to conservation efforts', 'Whales do not require any specific habitats to survive', 'Conservation efforts do not need to consider animal behaviour'], 0)]),
SS('Social Studies: The Multiculturalism Act of 1988',
   'Grade 6 Social Studies strand: the Canadian Multiculturalism Act of 1988 formally recognized and promoted the diversity of Canadian society, affirming the right of all citizens to preserve and share their cultural heritage.',
   [('What did the Canadian Multiculturalism Act of 1988 formally recognize?', ['The diversity of Canadian society', 'A single official culture for all of Canada', 'A ban on cultural celebrations', 'A requirement to adopt only one language nationwide'], 0),
    ('In what year was the Multiculturalism Act passed?', ['1988', '1867', '1929', '1960'], 0),
    ('What right did the Act affirm for Canadian citizens?', ['The right to preserve and share their cultural heritage', 'The right to ignore all federal laws', 'The right to vote only in municipal elections', 'The right to avoid paying any taxes'], 0),
    ('Why might a country choose to pass legislation supporting multiculturalism?', ['To formally support and encourage a diverse and inclusive society', 'Such legislation discourages diversity within a country', 'Multiculturalism laws remove all cultural traditions from a country', 'Countries never benefit from recognizing cultural diversity'], 0),
    ('Why is the Multiculturalism Act often seen as connected to Canadian identity today?', ['It reflects a value of inclusion that many Canadians consider central to their national identity', 'The Act has no connection to how Canadians view their country', 'Cultural diversity is not considered part of Canadian identity', 'The Act was repealed shortly after being introduced'], 0)]),
]),
day(156, [
L('Media Literacy: Understanding Algorithms and Personalized Feeds',
  'Grade 6 Language strand: an algorithm is a set of rules a website or app uses to decide what content to show a user, often personalizing feeds based on past clicks and interests, which can create a narrower view of information called a filter bubble.',
  [('What is an algorithm in the context of social media or apps?', ['A set of rules used to decide what content to show a user', 'A type of computer virus', 'A person who manually selects content for every user', 'A device used to connect to the internet'], 0),
   ('What might a personalized feed be based on?', ['A users past clicks and interests', 'Random selection with no pattern at all', 'The order content was originally published', 'Feedback from a users teachers only'], 0),
   ('What is a filter bubble?', ['A narrower view of information caused by seeing only content similar to what a user already likes', 'A tool used to remove all advertisements from a feed', 'A device that blocks internet access entirely', 'A feature that shows every user the exact same content'], 0),
   ('Why might it be important for a user to be aware of how algorithms shape their feed?', ['It helps them recognize that they may be seeing a limited range of perspectives', 'Algorithms have no effect on what content a user sees', 'Being aware of algorithms has no practical benefit', 'All users automatically see identical, unfiltered content'], 0),
   ('What could someone do to see a wider range of perspectives online?', ['Deliberately seek out sources and viewpoints outside their usual feed', 'Only read content recommended by an algorithm', 'Avoid using the internet altogether', 'Read only one single source of information repeatedly'], 0)]),
M('Data Management: Correlation versus Causation',
  'Grade 6 Math strand: correlation means two variables tend to change together, while causation means one variable directly causes a change in another, and data showing correlation does not necessarily prove causation.',
  [('What does correlation mean?', ['Two variables tend to change together', 'One variable always directly causes another', 'Two variables have no relationship at all', 'A single variable stays exactly the same over time'], 0),
   ('What does causation mean?', ['One variable directly causes a change in another', 'Two variables happen to change together with no connection', 'Data can never show a cause and effect relationship', 'Correlation and causation always mean the exact same thing'], 0),
   ('Why does correlation not necessarily prove causation?', ['Two variables might change together because of a third, unrelated factor', 'Correlation always proves that one variable causes the other', 'Causation can never be shown using data', 'Correlated variables are always directly connected by cause and effect'], 0),
   ('If ice cream sales and drowning incidents both rise in summer, what might explain this correlation?', ['A third factor, such as hot weather, affects both variables', 'Ice cream sales directly cause drowning incidents', 'Drowning incidents directly cause higher ice cream sales', 'The two events have no possible explanation at all'], 0),
   ('Why is it important for careful researchers to distinguish correlation from causation?', ['Mistaking correlation for causation can lead to false conclusions about how things are related', 'Researchers never need to consider the difference between the two ideas', 'Correlation and causation always lead to the same accurate conclusion', 'Distinguishing between them has no effect on the validity of research'], 0)]),
Sc('How Exercise Affects the Heart and Lungs',
   'Grade 6 Science strand: physical exercise increases heart rate and breathing rate, strengthening the heart muscle over time and improving the bodys ability to deliver oxygen efficiently to working muscles.',
   [('What happens to heart rate during physical exercise?', ['It increases', 'It decreases', 'It stops completely', 'It stays exactly the same at all times'], 0),
    ('Why does breathing rate increase during exercise?', ['The body needs more oxygen to supply working muscles', 'The body needs less oxygen during exercise', 'Breathing rate never changes during physical activity', 'Exercise stops the lungs from functioning'], 0),
    ('How does regular exercise affect the heart muscle over time?', ['It can strengthen the heart muscle', 'It always weakens the heart muscle permanently', 'Exercise has no effect on the heart muscle', 'It causes the heart to stop growing entirely'], 0),
    ('Why is a stronger heart able to pump blood more efficiently?', ['A stronger heart can pump more blood with each beat, delivering oxygen more effectively', 'A stronger heart pumps less blood with every beat', 'Heart strength has no connection to how efficiently blood is pumped', 'A stronger heart requires more beats to deliver the same amount of oxygen'], 0),
    ('Why might regular physical activity be recommended as part of a healthy lifestyle?', ['It supports the long-term health of the heart and lungs', 'Physical activity has no benefit for the heart or lungs', 'Exercise only affects muscles, never the heart or lungs', 'A healthy lifestyle never includes physical activity'], 0)]),
SS('Social Studies: The Fathers of Confederation and the Road to 1867',
   'Grade 6 Social Studies strand: the Fathers of Confederation were the political leaders who negotiated the union of British North American colonies, leading to the formation of Canada as a country in 1867.',
   [('Who were the Fathers of Confederation?', ['The political leaders who negotiated the union of British North American colonies', 'A group of early explorers who mapped Canada', 'The first monarchs to rule over Canada', 'A group of Indigenous leaders who founded Confederation'], 0),
    ('In what year did Confederation create the country of Canada?', ['1867', '1812', '1929', '1945'], 0),
    ('What did the Fathers of Confederation negotiate?', ['The union of separate British North American colonies into one country', 'A trade agreement with another country', 'The boundaries of the United States', 'A treaty ending a war with France'], 0),
    ('Why might colonies have wanted to unite into a single country in the 1860s?', ['Uniting could provide stronger defense, economic growth, and political stability', 'The colonies had no reason to consider uniting at all', 'Uniting would have weakened every colony involved', 'Confederation was forced entirely by another country'], 0),
    ('Why do the Fathers of Confederation remain significant figures in Canadian history?', ['Their negotiations directly led to the founding of Canada as a country', 'They have no lasting connection to modern Canada', 'Confederation was reversed shortly after it occurred', 'Their work only affected a single small region of Canada'], 0)]),
]),
day(157, [
L('Grammar: Using Dashes and Parentheses for Extra Information',
  'Grade 6 Language strand: dashes and parentheses can both be used to add extra information to a sentence, with dashes often creating a stronger emphasis while parentheses typically set off information considered less essential.',
  [('What is one use of a dash in a sentence?', ['To add extra information with strong emphasis', 'To end every sentence in a paragraph', 'To replace a period at all times', 'To indicate that a sentence is a question'], 0),
   ('What is one use of parentheses in a sentence?', ['To set off information that is considered less essential', 'To replace a subject in a sentence', 'To indicate the loudest word in a sentence', 'To end a sentence permanently'], 0),
   ('Which sentence correctly uses parentheses to add extra information?', ['The trip (which lasted three days) was unforgettable.', 'The trip which lasted three days was unforgettable', 'The trip lasted (three days was unforgettable)', 'The (trip which lasted three days was unforgettable.'], 0),
   ('Why might a writer choose a dash instead of a comma to set off information?', ['A dash can create a stronger, more dramatic pause than a comma', 'A dash always weakens the emphasis of a sentence', 'Dashes are never used to separate extra information', 'Commas always create more emphasis than dashes'], 0),
   ('Why is it important not to overuse dashes and parentheses in formal writing?', ['Overuse can make writing feel cluttered and harder to follow', 'Dashes and parentheses always improve clarity no matter how often they appear', 'Formal writing requires using as many dashes as possible', 'Extra information should never be included in formal writing'], 0)]),
M('Financial Literacy: Understanding Allowance, Saving, and Spending Plans',
  'Grade 6 Math strand: creating a simple spending plan involves dividing money, such as an allowance, into categories like saving, spending, and sharing, helping build habits of tracking income and expenses.',
  [('What is a spending plan?', ['A plan that divides money into categories such as saving, spending, and sharing', 'A plan that requires spending all money immediately', 'A record of only past purchases with no future planning', 'A plan used only by adults with full-time jobs'], 0),
   ('Why might someone divide their allowance into different categories?', ['It helps them balance saving for the future with spending in the present', 'Dividing money into categories makes budgeting impossible', 'All money should always be spent as soon as it is received', 'Categories have no effect on how money is managed'], 0),
   ('If someone receives 20 dollars and saves 25 percent of it, how much do they save?', ['5 dollars', '10 dollars', '15 dollars', '20 dollars'], 0),
   ('Why is tracking income and expenses considered a useful financial habit?', ['It helps a person understand where their money goes and plan more effectively', 'Tracking money has no benefit for personal finance', 'Only businesses need to track their income and expenses', 'Tracking expenses always makes budgeting more difficult'], 0),
   ('What might be one benefit of setting aside a portion of allowance for long-term saving?', ['It builds toward a larger goal that could not be reached by spending immediately', 'Saving money has no long-term benefit', 'Saving always means giving up the ability to buy anything', 'Long-term goals cannot be supported through saving'], 0)]),
Sc('Desalination — Turning Seawater into Fresh Water',
   'Grade 6 Science strand: desalination is the process of removing salt and other minerals from seawater to produce fresh water suitable for drinking or irrigation, often using methods such as distillation or reverse osmosis.',
   [('What does desalination remove from seawater?', ['Salt and other minerals', 'Only dissolved oxygen', 'Only microscopic organisms', 'Only the water itself'], 0),
    ('What is one method used to desalinate seawater?', ['Reverse osmosis', 'Simple filtration through sand only', 'Freezing the water permanently', 'Adding more salt to the water'], 0),
    ('Why might a coastal region with limited fresh water rely on desalination?', ['It provides an alternative source of drinking water when fresh water is scarce', 'Desalination removes the need for any water source', 'Coastal regions never experience water shortages', 'Desalination makes water undrinkable'], 0),
    ('What is one challenge associated with large-scale desalination?', ['It can require significant amounts of energy to operate', 'Desalination requires no energy at all', 'Desalination plants produce no waste products', 'Desalination is always cheaper than every other water source'], 0),
    ('Why might desalination become more important as global fresh water demand increases?', ['It offers a way to access the vast supply of water found in the oceans', 'Ocean water can never be used as a water source', 'Fresh water demand is expected to decrease everywhere', 'Desalination has no connection to global water supply challenges'], 0)]),
SS('Social Studies: Emancipation Day — The End of Slavery in British North America',
   'Grade 6 Social Studies strand: Emancipation Day, observed on August 1, commemorates the 1834 abolition of slavery throughout the British Empire, including British North America, and is marked by celebrations in communities across Canada.',
   [('What does Emancipation Day commemorate?', ['The 1834 abolition of slavery throughout the British Empire', 'The founding of Canada as a country', 'The end of the First World War', 'The signing of the Numbered Treaties'], 0),
    ('On what date is Emancipation Day observed?', ['August 1', 'July 1', 'November 11', 'January 1'], 0),
    ('In approximately what year did slavery become illegal throughout the British Empire?', ['1834', '1867', '1929', '1960'], 0),
    ('Why is Emancipation Day significant to communities across Canada?', ['It honours the end of slavery and recognizes the history of Black communities in Canada', 'It has no connection to Canadian history', 'The day is only recognized outside of Canada', 'It commemorates an event unrelated to slavery'], 0),
    ('Why might learning about Emancipation Day help Canadians understand the countrys history more fully?', ['It highlights an important part of the history of Black communities often left out of standard accounts', 'This history has no bearing on understanding Canada today', 'Slavery never existed anywhere in British North America', 'Emancipation Day is unrelated to Canadian history entirely'], 0)]),
]),
day(158, [
L('Reading: Comparing Primary and Secondary Sources',
  'Grade 6 Language strand: a primary source is firsthand evidence created during the time being studied, such as a letter or photograph, while a secondary source, such as a textbook, analyzes or interprets information from primary sources.',
  [('What is a primary source?', ['Firsthand evidence created during the time being studied', 'A summary written many years after an event', 'A textbook that interprets historical events', 'A source that always contains only opinions'], 0),
   ('Which of these is an example of a primary source?', ['A diary written during a historical event', 'A modern textbook chapter about that event', 'An encyclopedia article summarizing the event', 'A documentary made decades later'], 0),
   ('What is a secondary source?', ['A source that analyzes or interprets information from primary sources', 'A source created at the exact moment an event occurred', 'A photograph taken during a historical event', 'An original letter written by a historical figure'], 0),
   ('Why might historians value using both primary and secondary sources?', ['Primary sources offer firsthand evidence, while secondary sources provide broader context and analysis', 'Only secondary sources are ever useful to historians', 'Primary sources are always less reliable than secondary sources', 'Historians never need more than one type of source'], 0),
   ('Why is it important to consider who created a primary source?', ['The creators perspective can influence what information is included or left out', 'The identity of a sources creator never matters', 'All primary sources are always completely unbiased', 'Considering the source of information is unnecessary'], 0)]),
M('Number Sense: Percents Greater Than 100 and Percents Less Than 1',
  'Grade 6 Math strand: a percent greater than 100 represents an amount larger than the whole, while a percent less than 1 represents a very small fraction of the whole, both calculated using the same percent relationships as any other percent.',
  [('What does a percent greater than 100 represent?', ['An amount larger than the whole', 'An amount exactly equal to the whole', 'An amount that cannot exist mathematically', 'An amount always smaller than the whole'], 0),
   ('If a citys population grows from 100 to 150 people, what percent of the original population does the new population represent?', ['150 percent', '50 percent', '100 percent', '15 percent'], 0),
   ('What does a percent less than 1 represent?', ['A very small fraction of the whole', 'An amount larger than the whole', 'An amount exactly equal to the whole', 'A negative number'], 0),
   ('What is 0.5 percent written as a decimal?', ['0.005', '0.5', '0.05', '5.0'], 0),
   ('Why might percents greater than 100 be used to describe population or sales growth?', ['They show that a new value is larger than the original amount being compared', 'Percents greater than 100 are mathematically impossible to calculate', 'Growth can never be expressed using percents', 'Percents greater than 100 always indicate an error in calculation'], 0)]),
Sc('Rust and Corrosion — A Chemical Reaction',
   'Grade 6 Science strand: rust forms when iron reacts with oxygen and moisture in the air, producing iron oxide, a chemical reaction known as corrosion that gradually weakens metal over time.',
   [('What two substances react with iron to produce rust?', ['Oxygen and moisture', 'Nitrogen and heat', 'Carbon dioxide and sunlight', 'Salt and sand'], 0),
    ('What is the chemical name for rust?', ['Iron oxide', 'Iron nitrate', 'Iron carbonate', 'Iron sulfide'], 0),
    ('What term describes the gradual weakening of metal caused by reactions like rust formation?', ['Corrosion', 'Evaporation', 'Condensation', 'Photosynthesis'], 0),
    ('Why might painting a metal surface help prevent rust?', ['Paint creates a barrier that blocks oxygen and moisture from reaching the metal', 'Paint speeds up the process of rust formation', 'Paint has no effect on preventing corrosion', 'Rust cannot form on metal under any circumstances'], 0),
    ('Why is understanding corrosion important for engineers who design bridges and buildings?', ['It helps them choose materials and protective coatings that reduce long-term structural damage', 'Corrosion never affects large metal structures', 'Engineers do not need to consider chemical reactions when designing structures', 'Bridges and buildings are never made using metal materials'], 0)]),
SS('Social Studies: The Winnipeg General Strike of 1919',
   'Grade 6 Social Studies strand: the Winnipeg General Strike of 1919 was one of the largest labour strikes in Canadian history, with tens of thousands of workers walking off their jobs to demand better wages, working conditions, and the right to collective bargaining.',
   [('What was the Winnipeg General Strike of 1919?', ['One of the largest labour strikes in Canadian history', 'A strike involving only a handful of factory workers', 'A protest against a proposed new Canadian flag', 'A strike that took place outside of Canada'], 0),
    ('In what city did the 1919 general strike take place?', ['Winnipeg', 'Toronto', 'Vancouver', 'Halifax'], 0),
    ('What were striking workers demanding during the Winnipeg General Strike?', ['Better wages, working conditions, and the right to collective bargaining', 'A shorter school year for children', 'Lower taxes on imported goods', 'A new provincial capital city'], 0),
    ('Approximately how many workers are believed to have taken part in the strike?', ['Tens of thousands', 'Fewer than ten', 'About one hundred', 'Around one thousand'], 0),
    ('Why is the Winnipeg General Strike considered an important event in Canadian labour history?', ['It highlighted workers demands for fair treatment and influenced later labour rights movements', 'The strike had no lasting impact on workers rights in Canada', 'It is remembered only as a minor, forgotten event', 'The strike involved no workers demands of any kind'], 0)]),
]),
day(159, [
L('Vocabulary: Collective Nouns and Group Terms',
  'Grade 6 Language strand: a collective noun names a group of people, animals, or things treated as a single unit, such as a flock of birds, a team of players, or a herd of cattle.',
  [('What is a collective noun?', ['A noun that names a group treated as a single unit', 'A noun that names only one single object', 'A verb that shows group action', 'An adjective that describes a group'], 0),
   ('Which of these is a collective noun for a group of birds?', ['Flock', 'Herd', 'Pack', 'School'], 0),
   ('Which of these is a collective noun for a group of fish?', ['School', 'Flock', 'Team', 'Herd'], 0),
   ('In the sentence The team is practicing today, why is the verb is used instead of are?', ['The team is treated as a single unit performing one action', 'Collective nouns are always treated as multiple separate subjects', 'The verb are is never correct in English sentences', 'Team is not considered a collective noun'], 0),
   ('Why might collective nouns be useful when writing about animals or groups of people?', ['They allow a writer to refer to an entire group efficiently with a single word', 'Collective nouns make writing longer and less clear', 'Every group must always be described using multiple separate nouns', 'Collective nouns can only be used to describe inanimate objects'], 0)]),
M('Measurement: Finding Volume Using Water Displacement',
  'Grade 6 Math strand: water displacement is a method for finding the volume of an irregularly shaped object by submerging it in water and measuring the rise in water level, which equals the objects volume.',
  [('What does the water displacement method measure?', ['The volume of an irregularly shaped object', 'The mass of an object', 'The temperature of a liquid', 'The surface area of an object'], 0),
   ('How is the volume of an object determined using water displacement?', ['By measuring how much the water level rises when the object is submerged', 'By measuring how much the water level drops when the object is removed', 'By weighing the object before and after submerging it', 'By measuring the temperature change of the water'], 0),
   ('Why is water displacement especially useful for measuring irregularly shaped objects?', ['Formulas for regular shapes cannot easily be applied to irregular shapes', 'Water displacement only works on perfectly cube-shaped objects', 'Irregular objects have no measurable volume', 'Regular geometric formulas always work better on irregular shapes'], 0),
   ('If water rises from 100 millilitres to 150 millilitres after an object is submerged, what is the volume of the object?', ['50 millilitres', '100 millilitres', '150 millilitres', '250 millilitres'], 0),
   ('Why must an object be fully submerged for water displacement to give an accurate volume measurement?', ['Only the submerged part of an object displaces water, so a partial submersion would underestimate the volume', 'Partial submersion always gives a more accurate volume measurement', 'The amount of an object that is submerged has no effect on the measurement', 'Fully submerging an object always changes its actual volume'], 0)]),
Sc('Bird Beak Adaptations for Different Diets',
   'Grade 6 Science strand: bird beaks have evolved into a wide variety of shapes and sizes suited to different diets, such as long thin beaks for probing flowers, hooked beaks for tearing meat, and short strong beaks for cracking seeds.',
   [('What is one factor that has shaped the variety of bird beak shapes?', ['The different diets birds rely on', 'The colour of a birds feathers', 'The size of a birds nest', 'The migration distance a bird travels'], 0),
    ('Which type of beak would likely belong to a bird that eats seeds?', ['A short, strong beak for cracking shells', 'A long, thin beak for probing flowers', 'A hooked beak for tearing meat', 'A flat, wide beak with no other features'], 0),
    ('Which type of beak would likely belong to a bird of prey that eats meat?', ['A hooked beak for tearing flesh', 'A long, thin beak for sipping nectar', 'A short, wide beak with no point', 'A flat beak used only for filtering water'], 0),
    ('Why might a hummingbirds long, thin beak be well suited to its diet?', ['It allows the bird to reach nectar deep inside flowers', 'A long, thin beak makes it impossible to feed at all', 'This beak shape is only useful for cracking hard seeds', 'Hummingbirds do not rely on any specialized beak shape'], 0),
    ('Why is beak shape considered an example of adaptation?', ['It shows how a physical feature has developed to help a species survive on its specific diet', 'Beak shape has no connection to how a bird survives', 'All bird species have the exact same beak shape', 'Adaptation only applies to body size, never to beak shape'], 0)]),
SS('Social Studies: The Assembly of First Nations — Indigenous Political Leadership',
   'Grade 6 Social Studies strand: the Assembly of First Nations is a national advocacy organization that represents First Nations governments and communities across Canada, working to advance their political, social, and treaty rights.',
   [('What is the Assembly of First Nations?', ['A national advocacy organization representing First Nations governments and communities', 'A branch of the Canadian military', 'A federal government department', 'A private company that manages natural resources'], 0),
    ('What kinds of rights does the Assembly of First Nations work to advance?', ['Political, social, and treaty rights', 'Only rights related to international trade', 'Only rights related to professional sports', 'Only rights related to entertainment media'], 0),
    ('Who does the Assembly of First Nations represent?', ['First Nations governments and communities across Canada', 'Only communities located outside of Canada', 'Only members of the federal government', 'Only a single Indigenous community in one province'], 0),
    ('Why might a national organization like the Assembly of First Nations be important for advocacy?', ['It allows First Nations communities to present unified positions on shared issues', 'National organizations have no role in supporting community advocacy', 'Advocacy organizations are not permitted to represent multiple communities', 'The Assembly of First Nations has no connection to treaty rights'], 0),
    ('Why might understanding organizations like the Assembly of First Nations help explain modern Indigenous political leadership in Canada?', ['It shows how Indigenous communities organize to advocate for their rights at a national level', 'Indigenous political leadership does not exist in modern Canada', 'This organization has no role in Canadian political life', 'National advocacy organizations are unrelated to political leadership'], 0)]),
]),
day(160, [
L('Language Review: Vocabulary, Media Literacy, and Nonfiction Reading',
  'Grade 6 Language strand review: students revisit synonyms and antonyms, cause and effect in nonfiction, algorithms and personalized feeds, primary and secondary sources, and collective nouns.',
  [('What is a synonym?', ['A word with a similar meaning to another word', 'A word with the opposite meaning of another word', 'A word borrowed from another language', 'A word that describes a place'], 0),
   ('What is a cause in a cause and effect relationship?', ['The reason something happens', 'The result of an event', 'A completely unrelated event', 'The title of a nonfiction text'], 0),
   ('What is an algorithm in the context of social media or apps?', ['A set of rules used to decide what content to show a user', 'A type of computer virus', 'A person who manually selects content for every user', 'A device used to connect to the internet'], 0),
   ('What is a primary source?', ['Firsthand evidence created during the time being studied', 'A summary written many years after an event', 'A textbook that interprets historical events', 'A source that always contains only opinions'], 0),
   ('What is a collective noun?', ['A noun that names a group treated as a single unit', 'A noun that names only one single object', 'A verb that shows group action', 'An adjective that describes a group'], 0)]),
M('Math Review: Probability, Measurement, and Financial Literacy',
  'Grade 6 Math strand review: students revisit designing simulations, quartiles and interquartile range, tessellations, percents greater than 100, and finding volume using water displacement.',
  [('What is a simulation in probability?', ['A model used to estimate the probability of a real-world event', 'An event that happens only once and is never repeated', 'A guess made without any supporting data', 'A method that removes the need for probability entirely'], 0),
   ('What is the interquartile range?', ['The difference between the third quartile and the first quartile', 'The difference between the highest and lowest values', 'The average of all values in a data set', 'The middle value of a data set'], 0),
   ('What is a tessellation?', ['A pattern of shapes that fit together with no gaps or overlaps', 'A single shape drawn on its own', 'A pattern with large gaps between shapes', 'A three-dimensional solid made of many faces'], 0),
   ('What does a percent greater than 100 represent?', ['An amount larger than the whole', 'An amount exactly equal to the whole', 'An amount that cannot exist mathematically', 'An amount always smaller than the whole'], 0),
   ('What does the water displacement method measure?', ['The volume of an irregularly shaped object', 'The mass of an object', 'The temperature of a liquid', 'The surface area of an object'], 0)]),
Sc('Science Review: Simple Machines, the Human Body, and Chemistry',
   'Grade 6 Science strand review: students revisit the screw, DNA, homeostasis, how exercise affects the heart and lungs, and rust and corrosion.',
   [('What is a screw?', ['An inclined plane wrapped around a cylinder', 'A wheel connected to a rope', 'Two inclined planes joined at their bases', 'A lever with a fixed pivot point'], 0),
    ('What does DNA carry?', ['Genetic instructions for the growth and functioning of living things', 'Only information about an organisms diet', 'A record of an organisms daily behaviour', 'Energy used directly for muscle movement'], 0),
    ('What is homeostasis?', ['The process by which the body maintains a stable internal environment', 'The process by which the body grows taller over time', 'A disease that affects the immune system', 'A type of cell found only in the brain'], 0),
    ('What happens to heart rate during physical exercise?', ['It increases', 'It decreases', 'It stops completely', 'It stays exactly the same at all times'], 0),
    ('What two substances react with iron to produce rust?', ['Oxygen and moisture', 'Nitrogen and heat', 'Carbon dioxide and sunlight', 'Salt and sand'], 0)]),
SS('Social Studies Review: Canadian Rights, History, and Indigenous Leadership',
   'Grade 6 Social Studies strand review: students revisit the Canadian Human Rights Commission, the Oka Crisis, the Multiculturalism Act, the Winnipeg General Strike, and the Assembly of First Nations.',
   [('What is the main role of the Canadian Human Rights Commission?', ['To investigate complaints of discrimination and promote equality', 'To collect federal income taxes', 'To manage national parks and forests', 'To enforce traffic laws on highways'], 0),
    ('What was the Oka Crisis?', ['A 1990 land dispute between a Mohawk community and the town of Oka, Quebec', 'A federal election dispute in Ontario', 'A trade disagreement between Canada and another country', 'A dispute over a national park in British Columbia'], 0),
    ('What did the Canadian Multiculturalism Act of 1988 formally recognize?', ['The diversity of Canadian society', 'A single official culture for all of Canada', 'A ban on cultural celebrations', 'A requirement to adopt only one language nationwide'], 0),
    ('What was the Winnipeg General Strike of 1919?', ['One of the largest labour strikes in Canadian history', 'A strike involving only a handful of factory workers', 'A protest against a proposed new Canadian flag', 'A strike that took place outside of Canada'], 0),
    ('What is the Assembly of First Nations?', ['A national advocacy organization representing First Nations governments and communities', 'A branch of the Canadian military', 'A federal government department', 'A private company that manages natural resources'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g6_151_160)
    append_to(6, g6_151_160)
