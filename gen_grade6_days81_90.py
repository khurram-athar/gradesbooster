#!/usr/bin/env python3
"""Grade 6, Days 81-90 -- extends Grade 6 from 80 to 90 days. Topics chosen
to avoid any overlap with the existing Day 1-80 set (see data/grade6.json):
allegory, modal verbs, satire writing, loanwords, unreliable narrators,
appositive phrases, editorials, podcast media literacy, book-to-film
adaptations; scale factor, multi-step equations, slope, two-way frequency
tables, cylinder surface area, tree diagrams, percent increase/decrease,
the Pythagorean theorem, comparing loans and savings; renewable vs fossil
fuel power, plate tectonics, cell division, bioluminescence, vaccines,
roller coaster physics, ocean currents, genetic engineering, space debris;
the Green Revolution, the Space Race, refugee crises, trade agreements,
Indigenous self-government today, the Olympic Games, megacities, renewable
energy policy, and social media activism.

Subject keys for Grade 6 are "Language", "Math", "Science",
"SocialStudies" (same as all earlier Grade 6 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes use the curly Unicode form
(’).
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


def _rebalance_answer_positions(days, seed=20260925):
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


g6_81_90 = [
day(81, [
L('Reading: Analyzing Allegory in Literature',
  'Grade 6 Language strand: an allegory is a story in which characters and events represent broader ideas or morals, often used to comment on political or social issues indirectly.',
  [('What do we call a story where characters and events represent broader ideas?', ['An allegory', 'A concept unrelated to reading', 'A biography', 'A recipe'], 0),
   ('Can an allegory be used to comment indirectly on political or social issues?', ['Yes', 'No, allegories never comment on any issues', 'A concept unrelated to allegory', 'Allegories only ever describe literal events'], 0),
   ('In an allegory, do characters often represent something beyond themselves?', ['Yes', 'No, characters in an allegory only represent themselves', 'A concept unrelated to allegory', 'Characters never have any symbolic meaning'], 0),
   ('Why might an author choose to write an allegory instead of directly stating an opinion?', ['It allows readers to draw their own conclusions while still conveying a deeper message', 'Allegories never convey any deeper message', 'This concept has no connection to literature', 'Direct statements are always more effective than allegory'], 0),
   ('Why can reading an allegory sometimes require more careful thought than reading a straightforward story?', ['Readers must recognize the symbolic meaning behind the characters and events', 'Allegories never require any careful thought to understand', 'This concept has no connection to reading comprehension', 'An allegory is always exactly the same as a straightforward story'], 0)]),
M('Scale Factor and Enlargement or Reduction',
  'Grade 6 Math strand: a scale factor describes how much a shape is enlarged or reduced, such as a scale factor of 2 doubling every side length of a shape.',
  [('What does a scale factor describe?', ['How much a shape is enlarged or reduced', 'A concept unrelated to geometry', 'The colour of a shape', 'The number of sides a shape has'], 0),
   ('If a shape has a scale factor of 2 applied, what happens to its side lengths?', ['They double', 'They are cut in half', 'A concept unrelated to scale factor', 'They stay exactly the same'], 0),
   ('If a shape has a scale factor of one half applied, what happens to its side lengths?', ['They are cut in half', 'They double', 'A concept unrelated to scale factor', 'They stay exactly the same'], 0),
   ('If a rectangle with a side of 4 cm is enlarged with a scale factor of 3, what is the new side length?', ['12 cm', '7 cm', '4 cm', '3 cm'], 0),
   ('Why is scale factor an important concept for creating a scale drawing, like a map?', ['It helps represent real-world sizes accurately at a smaller or larger scale', 'Scale factor has no connection to scale drawings', 'This concept has no connection to geometry', 'Maps never use any kind of scale factor'], 0)]),
Sc('Science: Renewable vs Fossil Fuel Power Plants Compared',
   'Grade 6 Science strand: renewable power plants, like solar and wind farms, generate electricity from sources that naturally replenish, while fossil fuel power plants burn coal, oil, or natural gas, which are limited resources.',
   [('Name one example of a renewable power source, such as solar or wind.', ['Solar', 'A concept unrelated to renewable energy', 'Coal', 'Oil'], 0),
    ('Name one example of a fossil fuel, such as coal or oil.', ['Coal', 'A concept unrelated to fossil fuels', 'Solar', 'Wind'], 0),
    ('Do renewable energy sources naturally replenish over time?', ['Yes', 'No, renewable sources never replenish', 'A concept unrelated to renewable energy', 'Only fossil fuels replenish naturally'], 0),
    ('Why are fossil fuels considered a limited resource compared to renewable energy sources?', ['Fossil fuels take millions of years to form and can eventually run out', 'Fossil fuels can be instantly remade whenever needed', 'This concept has no connection to energy sources', 'Fossil fuels are actually more renewable than solar or wind power'], 0),
    ('Why might a country choose to invest more in renewable energy over time?', ['Renewable sources can provide power without depleting limited natural resources', 'Renewable energy has no benefit over fossil fuels', 'This concept has no relevance to science', 'Investing in renewable energy always increases fossil fuel use'], 0)]),
SS('Social Studies: The Green Revolution and Global Food Security',
   'Grade 6 Social Studies strand: the Green Revolution was a period of major agricultural advancement in the mid-1900s that increased crop yields worldwide, helping address global food security concerns.',
   [('What was the Green Revolution?', ['A period of major agricultural advancement that increased crop yields', 'A political revolution that overthrew a government', 'A concept unrelated to history', 'A type of environmental protest movement'], 0),
    ('Around what time period did the Green Revolution mainly take place?', ['The mid-1900s', 'The 1600s', 'A concept unrelated to the Green Revolution', 'The 2020s'], 0),
    ('Did the Green Revolution help increase crop yields worldwide?', ['Yes', 'No, it decreased crop yields worldwide', 'A concept unrelated to agriculture', 'It had no effect on crop yields at all'], 0),
    ('Why was increasing crop yields important for addressing global food security?', ['More food production could help feed growing populations around the world', 'Increasing crop yields never affects food security', 'This concept has no connection to global food security', 'Global food security has no connection to crop production'], 0),
    ('Why might some critics point out downsides to the methods used during the Green Revolution?', ['Some farming methods, like heavy fertilizer and pesticide use, can have environmental costs', 'The Green Revolution had no downsides of any kind', 'This concept has no relevance to social studies', 'Fertilizers and pesticides are never used in modern farming'], 0)]),
]),

day(82, [
L('Grammar: Modal Verbs and Their Uses',
  'Grade 6 Language strand: modal verbs, such as can, should, must, and might, express ability, permission, obligation, or possibility, changing the meaning of the main verb in a sentence.',
  [('Name one modal verb, such as can or should.', ['Can', 'A concept unrelated to grammar', 'Run', 'Happy'], 0),
   ('Does the modal verb must often express obligation?', ['Yes', 'No, must never expresses obligation', 'A concept unrelated to modal verbs', 'Must only expresses possibility'], 0),
   ('Does the modal verb might often express possibility?', ['Yes', 'No, might never expresses possibility', 'A concept unrelated to modal verbs', 'Might only expresses obligation'], 0),
   ('In the sentence You must finish your homework, what does the modal verb must express?', ['Obligation', 'Permission', 'A concept unrelated to grammar', 'Ability'], 0),
   ('Why might a writer choose might instead of must in a sentence?', ['Might expresses a weaker possibility, while must expresses a stronger obligation', 'Might and must always mean exactly the same thing', 'This concept has no connection to grammar', 'Might always expresses a stronger meaning than must'], 0)]),
M('Solving Multi-Step Equations with Variables on Both Sides',
  'Grade 6 Math strand: students learn to solve equations with a variable on both sides, such as 3n plus 2 equals n plus 10, by first combining variable terms on one side.',
  [('To solve 3n plus 2 equals n plus 10, what is a good first step?', ['Subtract n from both sides', 'Add n to both sides', 'A concept unrelated to solving equations', 'Multiply both sides by n'], 0),
   ('After subtracting n from both sides of 3n plus 2 equals n plus 10, what do you get?', ['2n plus 2 equals 10', '2n plus 2 equals n', '3n equals 10', 'n plus 2 equals 10'], 0),
   ('If 2n plus 2 equals 10, what is the value of n?', ['4', '2', '5', '8'], 0),
   ('Why is it useful to combine variable terms on one side before solving an equation?', ['It simplifies the equation into a form that is easier to solve', 'Combining variable terms never simplifies an equation', 'This concept has no connection to solving equations', 'Variables should always stay on both sides forever'], 0),
   ('If 5n minus 3 equals 2n plus 9, what is the value of n?', ['4', '3', '6', '2'], 0)]),
Sc('Science: Plate Tectonics and Continental Drift',
   'Grade 6 Science strand: continental drift is the theory that Earth’s continents slowly move over time due to the motion of tectonic plates beneath them, gradually changing the shape of Earth’s surface.',
   [('What is continental drift?', ['The theory that continents slowly move over time', 'A theory that continents never move at all', 'A concept unrelated to Earth science', 'A weather pattern found only in the ocean'], 0),
    ('What causes continents to slowly move over time?', ['The motion of tectonic plates', 'The motion of ocean waves only', 'A concept unrelated to plate tectonics', 'The rotation of the Moon'], 0),
    ('Does the shape of Earth’s surface gradually change due to plate tectonics?', ['Yes', 'No, Earth’s surface never changes', 'A concept unrelated to plate tectonics', 'Only the ocean floor changes, never land'], 0),
    ('Why might scientists believe that continents were once joined together in the past?', ['The shapes of continents seem to fit together like puzzle pieces, and matching fossils have been found on different continents', 'There is no evidence at all suggesting continents were ever joined', 'This concept has no connection to plate tectonics', 'Continents have always been in their exact current positions'], 0),
    ('Why is understanding plate tectonics useful for predicting natural events like earthquakes?', ['Earthquakes often occur along the boundaries where tectonic plates meet', 'Plate tectonics has no connection to earthquakes', 'This concept has no relevance to science', 'Earthquakes never occur near tectonic plate boundaries'], 0)]),
SS('Social Studies: The Space Race: Cold War Competition',
   'Grade 6 Social Studies strand: the Space Race was a period of intense competition during the Cold War between the United States and the Soviet Union to achieve milestones in space exploration.',
   [('What was the Space Race?', ['A period of competition to achieve milestones in space exploration', 'A sporting event held on the Moon', 'A concept unrelated to history', 'A modern car racing competition'], 0),
    ('Which two countries were the main competitors during the Space Race?', ['The United States and the Soviet Union', 'Canada and Mexico', 'A concept unrelated to the Space Race', 'France and Germany'], 0),
    ('Did the Space Race take place during the Cold War?', ['Yes', 'No, it took place during a completely different era', 'A concept unrelated to history', 'The Space Race and Cold War have no connection'], 0),
    ('Why might achieving a space milestone, like landing on the Moon, have been important during the Cold War?', ['It served as a symbol of technological and political strength between rival countries', 'Space milestones never had any political significance', 'This concept has no connection to the Cold War', 'The Space Race had no connection to competition between countries'], 0),
    ('Why might studying the Space Race help students understand how competition can drive innovation?', ['It shows how rivalry between countries pushed rapid advances in science and technology', 'Competition never leads to any scientific advancement', 'This concept has no relevance to social studies', 'The Space Race never resulted in any new technology'], 0)]),
]),

day(83, [
L('Writing: Writing a Satirical Piece',
  'Grade 6 Language strand: a satirical piece uses humour, irony, or exaggeration to criticize a real issue or behaviour, aiming to entertain readers while making a thoughtful point.',
  [('What kind of writing uses humour or exaggeration to criticize a real issue?', ['A satirical piece', 'A concept unrelated to writing', 'A grocery list', 'A weather report'], 0),
   ('Does a satirical piece aim to entertain readers while making a point?', ['Yes', 'No, satire never entertains readers', 'A concept unrelated to writing', 'Satire only ever states facts with no humour'], 0),
   ('Which of these is most likely an example of satire?', ['An exaggerated news article mocking excessive gadget spending', 'A factual report on weather patterns', 'A recipe for making bread', 'A list of math homework problems'], 0),
   ('Why might a writer choose satire to address a serious issue?', ['Humour can make readers think about an issue without feeling lectured', 'Satire never actually addresses any serious issue', 'This concept has no connection to writing', 'Serious issues can never be discussed through humour'], 0),
   ('Why is it important for readers to recognize when a text is satirical rather than factual?', ['Mistaking satire for a factual report could lead to misunderstanding the writer’s real message', 'Satire and factual reporting are always exactly the same', 'This concept has no connection to reading comprehension', 'Readers never need to consider whether a text is satirical'], 0)]),
M('Introduction to Slope',
  'Grade 6 Math strand: slope describes the steepness of a line, calculated by dividing the vertical change, or rise, by the horizontal change, or run, between two points.',
  [('What does slope describe about a line?', ['Its steepness', 'Its colour', 'A concept unrelated to geometry', 'Its exact length'], 0),
   ('Slope is calculated by dividing what two measurements?', ['Rise by run', 'Run by rise', 'A concept unrelated to slope', 'Height by width only, with no division'], 0),
   ('If a line rises 4 units and runs 2 units, what is its slope?', ['2', '4', '0.5', '6'], 0),
   ('If a line rises 6 units and runs 3 units, what is its slope?', ['2', '3', '6', '9'], 0),
   ('Why is understanding slope useful for describing real-world situations, like a wheelchair ramp?', ['It helps measure how steep or gradual an incline is', 'Slope has no connection to real-world inclines', 'This concept has no connection to math', 'Ramps are never measured using slope'], 0)]),
Sc('Science: Cell Division and Growth',
   'Grade 6 Science strand: cell division is the process by which a cell splits into two new cells, allowing living things to grow, repair damaged tissue, and replace old cells.',
   [('What is cell division?', ['The process by which a cell splits into two new cells', 'A process where cells disappear completely', 'A concept unrelated to biology', 'A process that only happens in plants'], 0),
    ('Does cell division allow living things to grow?', ['Yes', 'No, cell division has no connection to growth', 'A concept unrelated to biology', 'Growth never involves any cell division'], 0),
    ('Can cell division help repair damaged tissue?', ['Yes', 'No, damaged tissue can never be repaired', 'A concept unrelated to cell division', 'Only broken bones can be repaired, never tissue'], 0),
    ('Why is cell division important for healing a cut on your skin?', ['New cells created through cell division help replace and repair the damaged skin', 'Cell division has no connection to healing', 'This concept has no relevance to biology', 'Cuts heal without any new cells being made'], 0),
    ('Why do living things need cell division throughout their entire lives, not just during childhood?', ['Cells continue to wear out and need replacing, and tissues need repair throughout life', 'Cell division only ever happens once, during birth', 'This concept has no connection to biology', 'Adult bodies never need any new cells'], 0)]),
SS('Social Studies: Refugee Crises in the Modern World',
   'Grade 6 Social Studies strand: a refugee crisis occurs when large numbers of people are forced to flee their homes due to conflict, disaster, or persecution, often requiring international humanitarian support.',
   [('What do we call a situation where large numbers of people are forced to flee their homes?', ['A refugee crisis', 'A concept unrelated to global issues', 'A trade agreement', 'A sporting event'], 0),
    ('Name one reason people might be forced to flee their homes, such as conflict.', ['Conflict', 'A concept unrelated to refugee crises', 'A fun vacation', 'A school field trip'], 0),
    ('Does a refugee crisis often require international humanitarian support?', ['Yes', 'No, refugee crises never require any support', 'A concept unrelated to global issues', 'Only one single country is ever affected by a refugee crisis'], 0),
    ('Why might neighbouring countries be significantly affected by a refugee crisis?', ['They often receive large numbers of people needing shelter, food, and support', 'Neighbouring countries are never affected by a refugee crisis', 'This concept has no connection to global issues', 'Refugee crises never cross any international borders'], 0),
    ('Why is international cooperation often necessary to respond to a refugee crisis?', ['The scale of need can be too large for a single country to manage alone', 'International cooperation is never needed for humanitarian crises', 'This concept has no relevance to social studies', 'Refugee crises always resolve on their own without help'], 0)]),
]),

day(84, [
L('Vocabulary: Words Borrowed from Other Languages',
  'Grade 6 Language strand: a loanword is a word borrowed from another language and adopted into English, such as ballet from French or sushi from Japanese, often keeping its original meaning.',
  [('What do we call a word borrowed from another language and adopted into English?', ['A loanword', 'A concept unrelated to vocabulary', 'A synonym', 'A homophone'], 0),
   ('From which language does the word ballet come?', ['French', 'Japanese', 'A concept unrelated to loanwords', 'Spanish'], 0),
   ('From which language does the word sushi come?', ['Japanese', 'French', 'A concept unrelated to loanwords', 'German'], 0),
   ('Does a loanword often keep its original meaning when adopted into English?', ['Yes', 'No, loanwords always lose their original meaning', 'A concept unrelated to loanwords', 'Loanwords never have any original meaning'], 0),
   ('Why might English contain so many loanwords from other languages?', ['English has historically interacted with many cultures through trade, migration, and exchange', 'English has never interacted with any other language or culture', 'This concept has no connection to vocabulary', 'Loanwords are always invented, never actually borrowed'], 0)]),
M('Data: Two-Way Frequency Tables',
  'Grade 6 Math strand: a two-way frequency table organizes data by two categories at once, such as showing how many students of each grade prefer different subjects, making it easier to compare groups.',
  [('What does a two-way frequency table organize data by?', ['Two categories at once', 'Only one single category', 'A concept unrelated to data management', 'No categories at all'], 0),
   ('Why might a two-way frequency table be useful for comparing groups?', ['It allows for easy comparison between two different sets of categories', 'Two-way tables never help with comparing groups', 'This concept has no connection to data management', 'Two-way tables only show one number with no comparison'], 0),
   ('If a two-way frequency table shows subject preference by grade level, what two categories are being compared?', ['Subject preference and grade level', 'Only subject preference, with no other category', 'A concept unrelated to two-way tables', 'Only grade level, with no other category'], 0),
   ('If a two-way table shows 15 students in Grade 6 prefer math and 10 prefer science, which subject is more popular for Grade 6?', ['Math', 'Science', 'They are equally popular', 'Cannot tell from the table'], 0),
   ('Why might a school use a two-way frequency table to plan its course offerings?', ['It could show patterns in student interest across multiple factors, like grade and subject', 'Two-way tables have no use in planning school courses', 'This concept has no relevance to data management', 'Course planning never requires looking at any data'], 0)]),
Sc('Science: Bioluminescence: Living Things That Glow',
   'Grade 6 Science strand: bioluminescence is the ability of some living things, such as fireflies and certain deep-sea fish, to produce their own light through a chemical reaction inside their bodies.',
   [('What do we call the ability of some living things to produce their own light?', ['Bioluminescence', 'A concept unrelated to biology', 'Photosynthesis', 'Migration'], 0),
    ('Name one living thing known for bioluminescence, such as a firefly.', ['A firefly', 'A concept unrelated to bioluminescence', 'A rock', 'A cloud'], 0),
    ('Does bioluminescence happen through a chemical reaction inside an organism’s body?', ['Yes', 'No, bioluminescence has no connection to chemical reactions', 'A concept unrelated to bioluminescence', 'Bioluminescent light comes from an outside light source only'], 0),
    ('Why might a deep-sea fish benefit from bioluminescence in the dark ocean depths?', ['It could help attract prey, find a mate, or avoid predators in a dark environment', 'Bioluminescence provides no benefit to a deep-sea fish', 'This concept has no connection to biology', 'Deep-sea fish never actually need any light at all'], 0),
    ('Why do scientists find bioluminescent organisms interesting to study?', ['Understanding how they produce light could inspire new technologies or medical tools', 'Bioluminescent organisms have no scientific value at all', 'This concept has no relevance to science', 'Bioluminescence has already been completely understood with no more to learn'], 0)]),
SS('Social Studies: The Role of International Trade Agreements',
   'Grade 6 Social Studies strand: international trade agreements, such as those between Canada, the United States, and Mexico, set shared rules that make trading goods and services between countries easier and more predictable.',
   [('What do international trade agreements set between countries?', ['Shared rules for trading goods and services', 'Rules about a single country’s local traffic', 'A concept unrelated to global trade', 'Rules about school curriculum only'], 0),
    ('Name one country that has a trade agreement involving Canada, such as the United States.', ['The United States', 'A concept unrelated to trade agreements', 'A country with no connection to Canada', 'A fictional country'], 0),
    ('Can trade agreements make trading between countries more predictable?', ['Yes', 'No, trade agreements make trading less predictable', 'A concept unrelated to trade', 'Trade agreements have no effect on predictability'], 0),
    ('Why might countries negotiate a trade agreement instead of trading with no shared rules at all?', ['Shared rules can reduce confusion and make trade fairer for everyone involved', 'Trade agreements never actually help with trading goods', 'This concept has no connection to global trade', 'Countries never need any rules to trade with each other'], 0),
    ('Why might a trade agreement affect the prices of goods in a country?', ['Rules about tariffs and trade can change how much it costs to buy or sell goods internationally', 'Trade agreements never have any effect on prices', 'This concept has no relevance to social studies', 'Prices of goods are never affected by international trade'], 0)]),
]),

day(85, [
L('Reading: Understanding Unreliable Narrators',
  'Grade 6 Language strand: an unreliable narrator is a storyteller whose account of events may be inaccurate or biased, requiring readers to question and look for clues about what is really happening.',
  [('What do we call a storyteller whose account of events may be inaccurate or biased?', ['An unreliable narrator', 'A concept unrelated to reading', 'The main character always', 'The author of the book'], 0),
   ('Should readers question the events described by an unreliable narrator?', ['Yes', 'No, readers should never question a narrator', 'A concept unrelated to reading comprehension', 'Every narrator is always completely reliable'], 0),
   ('Why might a story use an unreliable narrator instead of a completely trustworthy one?', ['It can create suspense and encourage readers to think critically about the story', 'Unreliable narrators never add anything interesting to a story', 'This concept has no connection to literature', 'Reliable narrators are always more interesting to read'], 0),
   ('What might be a clue that a narrator is unreliable?', ['Other characters or events in the story contradict what the narrator says', 'Every detail the narrator shares is always completely accurate', 'This concept has no connection to reading comprehension', 'Unreliable narrators never contradict themselves'], 0),
   ('Why is recognizing an unreliable narrator an important reading skill?', ['It helps readers form their own judgment about what is really happening in the story', 'This concept never actually helps with understanding a story', 'This concept has no relevance to reading comprehension', 'Readers should always trust every detail a narrator provides'], 0)]),
M('Percent Increase and Decrease',
  'Grade 6 Math strand: percent increase and decrease describe how much a quantity has grown or shrunk compared to its original amount, expressed as a percentage.',
  [('If a price increases from 20 dollars to 25 dollars, what is the amount of increase?', ['5 dollars', '20 dollars', '25 dollars', '45 dollars'], 0),
   ('If a price increases from 20 dollars to 25 dollars, what is the percent increase?', ['25 percent', '5 percent', '20 percent', '45 percent'], 0),
   ('If a price decreases from 50 dollars to 40 dollars, what is the percent decrease?', ['20 percent', '10 percent', '40 percent', '50 percent'], 0),
   ('To calculate percent increase, you divide the amount of increase by the ___.', ['Original amount', 'Final amount only', 'A concept unrelated to percent', 'Number 100 only, with no other step'], 0),
   ('Why is understanding percent increase and decrease useful for shopping during a sale?', ['It helps calculate exactly how much money is saved or spent', 'Percent increase and decrease never apply to shopping', 'This concept has no connection to math', 'Sales prices are never calculated using percentages'], 0)]),
Sc('Science: Vaccines and How They Work',
   'Grade 6 Science strand: a vaccine trains the immune system to recognize and fight a specific germ by introducing a small, safe piece of it, helping the body build protection before facing a real infection.',
   [('What does a vaccine train the immune system to do?', ['Recognize and fight a specific germ', 'Ignore all germs completely', 'A concept unrelated to the immune system', 'Become weaker over time'], 0),
    ('Does a vaccine introduce a small, safe piece of a germ into the body?', ['Yes', 'No, vaccines never contain any part of a germ', 'A concept unrelated to vaccines', 'Vaccines introduce a fully dangerous germ into the body'], 0),
    ('Does a vaccine help the body build protection before facing a real infection?', ['Yes', 'No, vaccines provide no protection at all', 'A concept unrelated to vaccines', 'Vaccines only work after an infection has already occurred'], 0),
    ('Why might building immunity through a vaccine be safer than getting sick with the actual disease first?', ['A vaccine exposes the body to a controlled, safe version rather than the full illness', 'Vaccines are always more dangerous than the actual disease', 'This concept has no connection to how vaccines work', 'Getting the actual illness is always the safer option'], 0),
    ('Why are vaccines considered an important tool in public health?', ['They can help prevent the spread of diseases within a community', 'Vaccines have no effect on public health', 'This concept has no relevance to science', 'Vaccines only affect a single individual, never a community'], 0)]),
SS('Social Studies: Canada’s Relationship with Indigenous Self-Government Today',
   'Grade 6 Social Studies strand: today, many Indigenous communities in Canada are working toward greater self-government, making their own decisions about governance, land, and resources within their communities.',
   [('What are many Indigenous communities in Canada working toward today?', ['Greater self-government', 'Complete disconnection from Canada', 'A concept unrelated to Indigenous communities', 'No changes of any kind'], 0),
    ('Does self-government involve communities making their own decisions about governance and land?', ['Yes', 'No, self-government has no connection to decision-making', 'A concept unrelated to Indigenous self-government', 'Self-government only applies to decisions made by the federal government'], 0),
    ('Is Indigenous self-government a modern, ongoing process in Canada?', ['Yes', 'No, this process ended many years ago with no more changes', 'A concept unrelated to Canadian history', 'Self-government has never been discussed in Canada'], 0),
    ('Why might greater self-government be important to Indigenous communities?', ['It allows communities to make decisions that reflect their own needs, values, and traditions', 'Self-government has no benefit to any community', 'This concept has no connection to social studies', 'Communities never need to make their own decisions'], 0),
    ('Why is it valuable for students to learn about Indigenous self-government as an ongoing, modern topic?', ['It helps show that Indigenous history and rights continue to evolve today, not just in the past', 'This topic is only relevant to distant history with no modern connection', 'This concept has no relevance to social studies', 'Indigenous self-government has no connection to Canada today'], 0)]),
]),

day(86, [
L('Grammar: Appositive Phrases',
  'Grade 6 Language strand: an appositive phrase renames or gives more information about a nearby noun, such as in Mr. Lee, our science teacher, explained the experiment, where our science teacher describes Mr. Lee.',
  [('What does an appositive phrase do to a nearby noun?', ['Renames or gives more information about it', 'Replaces it completely with a new meaning', 'A concept unrelated to grammar', 'Removes it from the sentence entirely'], 0),
   ('In the sentence Mr. Lee, our science teacher, explained the experiment, what is the appositive phrase?', ['Our science teacher', 'Mr. Lee', 'Explained the experiment', 'The experiment'], 0),
   ('Should an appositive phrase usually be set off with commas?', ['Yes', 'No, appositive phrases should never use commas', 'A concept unrelated to grammar', 'Only question marks should be used, never commas'], 0),
   ('Which sentence correctly uses an appositive phrase?', ['My sister, a talented painter, sold her first artwork.', 'My sister a talented painter sold her first artwork she did.', 'A talented painter my sister sold her first artwork.', 'My sister sold a talented painter her first artwork.'], 0),
   ('Why might a writer use an appositive phrase instead of writing a separate sentence?', ['It combines related information smoothly and efficiently into one sentence', 'Appositive phrases never combine any information', 'This concept has no connection to writing', 'Separate sentences are always clearer than an appositive phrase'], 0)]),
M('Surface Area of Cylinders',
  'Grade 6 Math strand: the surface area of a cylinder is found by adding the areas of its two circular ends to the area of its curved side, which unrolls into a rectangle.',
  [('How many circular ends does a cylinder have?', ['Two', 'One', 'Three', 'Zero'], 0),
   ('What shape does the curved side of a cylinder unroll into?', ['A rectangle', 'A triangle', 'A concept unrelated to cylinders', 'A circle'], 0),
   ('To find the surface area of a cylinder, you add the areas of its two circular ends to the area of its ___.', ['Curved side', 'Only its top', 'A concept unrelated to surface area', 'Only its bottom'], 0),
   ('Why is it useful to know how to calculate a cylinder’s surface area?', ['It can help determine how much material is needed to make or wrap a cylindrical object', 'Surface area calculations never apply to real objects', 'This concept has no connection to geometry', 'Cylinders never actually have any surface area'], 0),
   ('If a cylinder’s two circular ends have a combined area of 20 square cm and its curved side has an area of 30 square cm, what is its total surface area?', ['50 square cm', '30 square cm', '20 square cm', '10 square cm'], 0)]),
Sc('Science: The Physics of Roller Coasters',
   'Grade 6 Science strand: roller coasters use potential and kinetic energy, converting stored energy at the top of a hill into motion energy as the coaster speeds down, following the law of conservation of energy.',
   [('What type of energy does a roller coaster have at the top of a hill, before it moves?', ['Potential energy', 'Kinetic energy only', 'A concept unrelated to energy', 'No energy at all'], 0),
    ('What type of energy does a roller coaster have as it speeds down a hill?', ['Kinetic energy', 'Potential energy only', 'A concept unrelated to energy', 'No energy at all'], 0),
    ('Does a roller coaster follow the law of conservation of energy?', ['Yes', 'No, roller coasters do not follow any energy laws', 'A concept unrelated to physics', 'Energy is created out of nothing on a roller coaster'], 0),
    ('Why does a roller coaster need a tall first hill to build up potential energy?', ['That stored energy converts into the motion energy needed for the rest of the ride', 'The height of the first hill has no connection to the ride’s energy', 'This concept has no connection to physics', 'Roller coasters generate their own energy with no need for hills'], 0),
    ('Why might a roller coaster gradually lose speed and height as the ride continues?', ['Some energy is lost to friction and air resistance along the track', 'Roller coasters never lose any energy during a ride', 'This concept has no relevance to science', 'Energy is only ever gained, never lost, throughout a ride'], 0)]),
SS('Social Studies: The History of the Olympic Games',
   'Grade 6 Social Studies strand: the modern Olympic Games began in 1896, reviving an ancient Greek tradition, and today bring together athletes from around the world to compete and celebrate international friendship.',
   [('In what year did the modern Olympic Games begin?', ['1896', '1776', '1945', '2000'], 0),
    ('Did the modern Olympic Games revive a tradition from ancient Greece?', ['Yes', 'No, the Olympics have no connection to ancient Greece', 'A concept unrelated to the Olympics', 'The Olympics began in ancient Rome instead'], 0),
    ('Do the Olympic Games bring together athletes from around the world?', ['Yes', 'No, only one single country ever participates', 'A concept unrelated to the Olympics', 'The Olympics only include local athletes from one city'], 0),
    ('Why might the Olympic Games be seen as an event that promotes international friendship?', ['It brings together athletes and spectators from many countries to compete and connect', 'The Olympics have no connection to international relationships', 'This concept has no relevance to social studies', 'The Olympics only ever involve conflict between countries'], 0),
    ('Why might hosting the Olympic Games be both an opportunity and a challenge for a city?', ['It can boost tourism and pride, but also requires significant planning and resources', 'Hosting the Olympics never has any effect on a host city', 'This concept has no connection to social studies', 'Cities never need to prepare anything to host the Olympics'], 0)]),
]),

day(87, [
L('Writing: Writing an Editorial',
  'Grade 6 Language strand: an editorial expresses a newspaper’s or writer’s opinion on a current issue, using a clear argument, supporting evidence, and often a call to action for readers.',
  [('What kind of writing expresses an opinion on a current issue in a newspaper?', ['An editorial', 'A concept unrelated to writing', 'A grocery list', 'A weather report'], 0),
   ('Should an editorial include supporting evidence for its argument?', ['Yes', 'No, editorials never include any evidence', 'A concept unrelated to writing', 'Only opinions are allowed, with no evidence at all'], 0),
   ('Does an editorial often end with a call to action for readers?', ['Yes', 'No, editorials never suggest any action to readers', 'A concept unrelated to writing', 'A call to action is only found in fiction stories'], 0),
   ('Why might a newspaper publish an editorial about a local issue?', ['To share an opinion and encourage public discussion or action on the issue', 'Editorials never discuss any real issues', 'This concept has no connection to writing', 'Editorials are always about fictional topics only'], 0),
   ('Which of these is most likely a call to action found at the end of an editorial?', ['We urge our city council to fund more public transportation.', 'Once upon a time, in a faraway kingdom.', 'Add 4 and 5 to get 9.', 'The chemical symbol for gold is Au.'], 0)]),
M('Introduction to the Pythagorean Theorem',
  'Grade 6 Math strand: the Pythagorean theorem states that in a right triangle, the square of the hypotenuse equals the sum of the squares of the two other sides, written as a squared plus b squared equals c squared.',
  [('In a right triangle, what does the Pythagorean theorem relate?', ['The lengths of the three sides', 'The three angles only', 'A concept unrelated to geometry', 'The colour of the triangle'], 0),
   ('What is the longest side of a right triangle called?', ['The hypotenuse', 'The base', 'A concept unrelated to right triangles', 'The height only'], 0),
   ('If a right triangle has legs of 3 and 4, what is the length of the hypotenuse?', ['5', '7', '12', '25'], 0),
   ('The Pythagorean theorem is written as a squared plus b squared equals ___.', ['C squared', 'A squared', 'B squared', 'D squared'], 0),
   ('Why is the Pythagorean theorem useful for solving real-world problems, like finding the shortest distance across a park?', ['It helps calculate an unknown side length when two other sides of a right triangle are known', 'The Pythagorean theorem never applies to any real-world situation', 'This concept has no connection to geometry', 'Right triangles never appear in real-world problems'], 0)]),
Sc('Science: Ocean Currents and Their Effect on Climate',
   'Grade 6 Science strand: ocean currents are large-scale movements of seawater that help distribute heat around the planet, influencing climate patterns in coastal regions.',
   [('What are ocean currents?', ['Large-scale movements of seawater', 'A concept unrelated to oceans', 'A type of cloud formation', 'A kind of rock formation'], 0),
    ('Do ocean currents help distribute heat around the planet?', ['Yes', 'No, ocean currents have no connection to heat distribution', 'A concept unrelated to ocean currents', 'Ocean currents only affect the deepest parts of the ocean'], 0),
    ('Can ocean currents influence the climate of coastal regions?', ['Yes', 'No, ocean currents never affect climate', 'A concept unrelated to ocean currents', 'Only mountains affect coastal climate, never oceans'], 0),
    ('Why might a coastal city have milder winters than an inland city at the same latitude?', ['Nearby ocean currents can help moderate the temperature of coastal areas', 'Ocean currents never have any effect on nearby land temperatures', 'This concept has no connection to climate', 'Coastal cities are always colder than inland cities'], 0),
    ('Why do scientists study ocean currents when researching climate change?', ['Changes in ocean currents could significantly affect global weather patterns', 'Ocean currents have no connection to climate change research', 'This concept has no relevance to science', 'Ocean currents never change over time'], 0)]),
SS('Social Studies: Urbanization: The Growth of Megacities',
   'Grade 6 Social Studies strand: urbanization is the growth of cities as more people move from rural areas to urban centres, sometimes creating megacities, cities with populations over 10 million people.',
   [('What is urbanization?', ['The growth of cities as more people move from rural areas', 'The growth of rural farmland only', 'A concept unrelated to geography', 'The shrinking of cities over time'], 0),
    ('What do we call a city with a population over 10 million people?', ['A megacity', 'A small town', 'A concept unrelated to urbanization', 'A rural village'], 0),
    ('Does urbanization involve people moving from rural areas to urban centres?', ['Yes', 'No, urbanization involves no movement of people at all', 'A concept unrelated to urbanization', 'Urbanization only involves moving from cities to rural areas'], 0),
    ('Why might people choose to move from rural areas to cities?', ['Cities often offer more job opportunities, services, and education options', 'People never have any reason to move to a city', 'This concept has no connection to urbanization', 'Rural areas always offer more opportunities than cities'], 0),
    ('Why might rapid urbanization create challenges for a city’s infrastructure?', ['A fast-growing population can strain housing, transportation, and public services', 'Urbanization never creates any challenges for a city', 'This concept has no relevance to social studies', 'Cities never need to plan for population growth'], 0)]),
]),

day(88, [
L('Media Literacy: Analyzing Podcast and Audio Media',
  'Grade 6 Language strand: podcasts and audio media use sound, tone of voice, and pacing to convey information or opinions, requiring listeners to critically evaluate the content just as they would written text.',
  [('What do podcasts and audio media use to convey information, besides words?', ['Tone of voice and pacing', 'A concept unrelated to audio media', 'Only silence', 'Only written text'], 0),
   ('Should listeners critically evaluate podcast content, just as they would written text?', ['Yes', 'No, audio content never needs to be evaluated critically', 'A concept unrelated to media literacy', 'Only written text requires critical evaluation'], 0),
   ('Can a podcast host’s tone of voice affect how a listener perceives the information?', ['Yes', 'No, tone of voice has no effect on how information is perceived', 'A concept unrelated to podcasts', 'Tone of voice only matters in written text, not audio'], 0),
   ('Why might a listener need to check the accuracy of claims made in a podcast?', ['Podcasts, like any media, can include opinions or information that is not fully verified', 'Every podcast is always completely accurate with no need for checking', 'This concept has no connection to media literacy', 'Audio media is never used to share information or opinions'], 0),
   ('Why is understanding pacing important when analyzing a podcast?', ['Pacing can be used to build suspense or emphasize certain points, shaping the listener’s reaction', 'Pacing never has any effect on how a listener understands a podcast', 'This concept has no relevance to media literacy', 'Podcasts never use any kind of pacing at all'], 0)]),
M('Compound Probability with Tree Diagrams',
  'Grade 6 Math strand: a tree diagram organizes all possible outcomes of two or more events, such as flipping a coin and rolling a die, making it easier to calculate compound probability.',
  [('What does a tree diagram help organize?', ['All possible outcomes of two or more events', 'Only a single outcome', 'A concept unrelated to probability', 'No outcomes at all'], 0),
   ('If you flip a coin and roll a die, how many total outcomes would a tree diagram show?', ['12', '2', '6', '8'], 0),
   ('Why might a tree diagram be helpful for calculating compound probability?', ['It visually organizes every possible combination of outcomes', 'Tree diagrams never help with calculating probability', 'This concept has no connection to math', 'Tree diagrams only show a single outcome, never combinations'], 0),
   ('If a tree diagram shows 4 equally likely outcomes and only 1 matches what you want, what is the probability?', ['1 fourth', '1 half', '4 fourths', '1 third'], 0),
   ('Compound probability involves finding the likelihood of ___.', ['Two or more events happening together', 'Only a single event happening', 'A concept unrelated to probability', 'An event that can never happen'], 0)]),
Sc('Science: Genetic Engineering: An Introduction',
   'Grade 6 Science strand: genetic engineering is a technology that allows scientists to directly modify an organism’s genes, used in areas such as agriculture and medicine to create desired traits.',
   [('What does genetic engineering allow scientists to do?', ['Directly modify an organism’s genes', 'Only observe an organism from a distance', 'A concept unrelated to biology', 'Nothing at all related to genes'], 0),
    ('Name one area where genetic engineering is used, such as agriculture or medicine.', ['Agriculture', 'A concept unrelated to genetic engineering', 'Cooking recipes', 'Weather forecasting'], 0),
    ('Can genetic engineering be used to create desired traits in organisms?', ['Yes', 'No, genetic engineering has no connection to traits', 'A concept unrelated to genetic engineering', 'Traits can never be influenced by genetic engineering'], 0),
    ('Why might scientists use genetic engineering to help crops resist certain diseases?', ['It can directly modify a plant’s genes to build in disease resistance', 'Genetic engineering never affects how a crop grows', 'This concept has no connection to agriculture', 'Crops can never be modified in any way'], 0),
    ('Why do some people have questions or concerns about genetic engineering?', ['Changing genes can raise ethical and safety questions that need careful consideration', 'Genetic engineering has no possible risks or considerations at all', 'This concept has no relevance to science', 'No one has ever raised any questions about genetic engineering'], 0)]),
SS('Social Studies: Renewable Energy Policy Around the World',
   'Grade 6 Social Studies strand: many countries have created renewable energy policies, such as goals for reducing fossil fuel use, to encourage the shift toward cleaner energy sources like solar and wind power.',
   [('What is a renewable energy policy?', ['A government plan encouraging cleaner energy sources', 'A rule about how much homework students must do', 'A concept unrelated to energy', 'A private company’s advertising strategy'], 0),
    ('Name one goal a renewable energy policy might set, such as reducing fossil fuel use.', ['Reducing fossil fuel use', 'A concept unrelated to renewable energy', 'Increasing fossil fuel use', 'Banning all forms of energy'], 0),
    ('Do many countries around the world have renewable energy policies?', ['Yes', 'No, only a single country has ever created such a policy', 'A concept unrelated to renewable energy', 'Renewable energy policies do not exist anywhere'], 0),
    ('Why might governments create policies encouraging renewable energy?', ['To help reduce environmental harm and support cleaner, more sustainable energy use', 'Renewable energy policies never have any environmental purpose', 'This concept has no connection to social studies', 'Governments never create any policies about energy'], 0),
    ('Why might renewable energy policies differ from one country to another?', ['Countries have different resources, needs, and priorities that shape their energy policies', 'Every country in the world has the exact same energy policy', 'This concept has no relevance to social studies', 'Energy policy never depends on a country’s resources or needs'], 0)]),
]),

day(89, [
L('Reading: Comparing Book and Film Adaptations',
  'Grade 6 Language strand: comparing a book to its film adaptation involves examining what details, characters, or events were kept, changed, or removed, and considering why those choices might have been made.',
  [('What does comparing a book to its film adaptation involve examining?', ['What details were kept, changed, or removed', 'Only the book’s cover design', 'A concept unrelated to reading', 'Only the film’s runtime'], 0),
   ('Might a film adaptation change or remove some details from the original book?', ['Yes', 'No, film adaptations are always identical to the book', 'A concept unrelated to adaptations', 'Films can only ever add new details, never remove any'], 0),
   ('Why might a filmmaker choose to remove a minor subplot from a book when adapting it into a film?', ['Film has a limited runtime, so some details may need to be cut for pacing', 'Filmmakers never make any changes when adapting a book', 'This concept has no connection to comparing adaptations', 'Books and films always have the exact same length'], 0),
   ('Why might comparing a book and its film adaptation deepen a reader’s understanding of both?', ['It can reveal different storytelling choices and how each medium conveys a story', 'Comparing adaptations never reveals anything useful', 'This concept has no connection to reading comprehension', 'A book and its film adaptation are always exactly the same'], 0),
   ('Which of these is a reasonable question to ask when comparing a book to its film adaptation?', ['Why might the filmmakers have changed the ending?', 'What colour is the actor’s shirt?', 'How many pages does the book have?', 'What time was the movie released in theatres?'], 0)]),
M('Financial Literacy: Comparing Loan and Savings Options',
  'Grade 6 Math strand: students compare loan options, where interest is paid to a lender, with savings options, where interest is earned, to understand how borrowing and saving money affect finances differently.',
  [('When you take out a loan, do you pay interest or earn interest?', ['Pay interest', 'Earn interest', 'A concept unrelated to loans', 'Neither pay nor earn any interest'], 0),
   ('When you put money into a savings account, do you pay interest or earn interest?', ['Earn interest', 'Pay interest', 'A concept unrelated to savings', 'Neither pay nor earn any interest'], 0),
   ('If a loan has a higher interest rate, will you likely pay more or less over time?', ['More', 'Less', 'A concept unrelated to loans', 'The interest rate never affects total cost'], 0),
   ('Why might someone compare interest rates before choosing a savings account?', ['A higher interest rate means their savings could grow more over time', 'Interest rates never affect how much money grows in a savings account', 'This concept has no connection to financial literacy', 'Savings accounts never earn any interest at all'], 0),
   ('Why is it important to understand the difference between paying and earning interest?', ['It helps people make informed decisions about borrowing and saving money', 'Interest has no connection to borrowing or saving money', 'This concept has no relevance to financial literacy', 'Loans and savings accounts always work in exactly the same way'], 0)]),
Sc('Science: Space Debris and Satellite Safety',
   'Grade 6 Science strand: space debris consists of old satellites, rocket parts, and other objects left in orbit around Earth, posing a safety risk to active satellites and spacecraft.',
   [('What is space debris made up of?', ['Old satellites, rocket parts, and other objects left in orbit', 'Only natural objects like asteroids', 'A concept unrelated to space', 'Nothing at all, since space is always empty'], 0),
    ('Can space debris pose a safety risk to active satellites?', ['Yes', 'No, space debris has no connection to satellite safety', 'A concept unrelated to space debris', 'Space debris only affects objects on Earth, never in orbit'], 0),
    ('Where is space debris typically found?', ['In orbit around Earth', 'Only inside a spacecraft', 'A concept unrelated to space debris', 'Only on the surface of the Moon'], 0),
    ('Why might scientists track the location of space debris carefully?', ['Collisions with debris could damage or destroy working satellites and spacecraft', 'Space debris never poses any risk to spacecraft', 'This concept has no connection to space safety', 'Tracking space debris serves no useful purpose'], 0),
    ('Why is space debris becoming a growing concern as more satellites are launched?', ['More objects in orbit increases the chances of collisions and further debris', 'The number of satellites in orbit never changes', 'This concept has no relevance to science', 'More satellites in orbit always reduces the risk of collisions'], 0)]),
SS('Social Studies: The Role of Social Media in Modern Activism',
   'Grade 6 Social Studies strand: social media has become a tool for modern activism, allowing people to quickly share information, organize events, and raise awareness about social or environmental causes.',
   [('What has social media become a tool for in recent years?', ['Modern activism', 'A concept unrelated to social issues', 'Only entertainment, with no other use', 'Nothing beyond casual conversation'], 0),
    ('Can social media help people organize events and raise awareness about causes?', ['Yes', 'No, social media has no connection to organizing events', 'A concept unrelated to activism', 'Social media can only ever be used for entertainment'], 0),
    ('Does social media allow information to be shared quickly?', ['Yes', 'No, information spreads very slowly through social media', 'A concept unrelated to social media', 'Social media has no connection to sharing information'], 0),
    ('Why might social media be an effective tool for raising awareness about an environmental cause?', ['It can quickly reach large numbers of people and encourage them to take action', 'Social media never actually reaches very many people', 'This concept has no connection to activism', 'Environmental causes are never discussed on social media'], 0),
    ('Why is it important to verify information shared on social media before acting on it?', ['Not all information shared online is accurate or verified', 'Information on social media is always completely accurate', 'This concept has no relevance to social studies', 'Verifying information is never necessary before sharing it further'], 0)]),
]),

day(90, [
L('Review: Literary Devices, Grammar, and Media Literacy (Days 81-89)',
  'Grade 6 Language strand review: students revisit allegory, modal verbs, satire, loanwords, unreliable narrators, appositive phrases, editorials, podcast media literacy, and book-to-film adaptations.',
  [('What do we call a story where characters and events represent broader ideas?', ['An allegory', 'A concept unrelated to reading', 'A biography', 'A recipe'], 0),
   ('Name one modal verb, such as can or should.', ['Can', 'A concept unrelated to grammar', 'Run', 'Happy'], 0),
   ('What do we call a word borrowed from another language and adopted into English?', ['A loanword', 'A concept unrelated to vocabulary', 'A synonym', 'A homophone'], 0),
   ('What do we call a storyteller whose account of events may be inaccurate or biased?', ['An unreliable narrator', 'A concept unrelated to reading', 'The main character always', 'The author of the book'], 0),
   ('What kind of writing expresses an opinion on a current issue in a newspaper?', ['An editorial', 'A concept unrelated to writing', 'A grocery list', 'A weather report'], 0)]),
M('Review: Geometry, Equations, and Probability (Days 81-89)',
  'Grade 6 Math strand review: students revisit scale factor, multi-step equations, slope, two-way frequency tables, cylinder surface area, percent increase and decrease, the Pythagorean theorem, tree diagrams, and financial literacy.',
  [('What does a scale factor describe?', ['How much a shape is enlarged or reduced', 'A concept unrelated to geometry', 'The colour of a shape', 'The number of sides a shape has'], 0),
   ('If 2n plus 2 equals 10, what is the value of n?', ['4', '2', '5', '8'], 0),
   ('What does slope describe about a line?', ['Its steepness', 'Its colour', 'A concept unrelated to geometry', 'Its exact length'], 0),
   ('What is the longest side of a right triangle called?', ['The hypotenuse', 'The base', 'A concept unrelated to right triangles', 'The height only'], 0),
   ('When you take out a loan, do you pay interest or earn interest?', ['Pay interest', 'Earn interest', 'A concept unrelated to loans', 'Neither pay nor earn any interest'], 0)]),
Sc('Review: Earth Science, Biology, and Space (Days 81-89)',
   'Grade 6 Science strand review: students revisit renewable vs fossil fuel power, plate tectonics, cell division, bioluminescence, vaccines, roller coaster physics, ocean currents, genetic engineering, and space debris.',
   [('Name one example of a renewable power source, such as solar or wind.', ['Solar', 'A concept unrelated to renewable energy', 'Coal', 'Oil'], 0),
    ('What is continental drift?', ['The theory that continents slowly move over time', 'A theory that continents never move at all', 'A concept unrelated to Earth science', 'A weather pattern found only in the ocean'], 0),
    ('What does a vaccine train the immune system to do?', ['Recognize and fight a specific germ', 'Ignore all germs completely', 'A concept unrelated to the immune system', 'Become weaker over time'], 0),
    ('What are ocean currents?', ['Large-scale movements of seawater', 'A concept unrelated to oceans', 'A type of cloud formation', 'A kind of rock formation'], 0),
    ('What is space debris made up of?', ['Old satellites, rocket parts, and other objects left in orbit', 'Only natural objects like asteroids', 'A concept unrelated to space', 'Nothing at all, since space is always empty'], 0)]),
SS('Review: Global History and Modern Global Issues (Days 81-89)',
   'Grade 6 Social Studies strand review: students revisit the Green Revolution, the Space Race, refugee crises, trade agreements, Indigenous self-government, the Olympic Games, urbanization, renewable energy policy, and social media activism.',
   [('What was the Green Revolution?', ['A period of major agricultural advancement that increased crop yields', 'A political revolution that overthrew a government', 'A concept unrelated to history', 'A type of environmental protest movement'], 0),
    ('What was the Space Race?', ['A period of competition to achieve milestones in space exploration', 'A sporting event held on the Moon', 'A concept unrelated to history', 'A modern car racing competition'], 0),
    ('What are many Indigenous communities in Canada working toward today?', ['Greater self-government', 'Complete disconnection from Canada', 'A concept unrelated to Indigenous communities', 'No changes of any kind'], 0),
    ('What is urbanization?', ['The growth of cities as more people move from rural areas', 'The growth of rural farmland only', 'A concept unrelated to geography', 'The shrinking of cities over time'], 0),
    ('What has social media become a tool for in recent years?', ['Modern activism', 'A concept unrelated to social issues', 'Only entertainment, with no other use', 'Nothing beyond casual conversation'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g6_81_90)
    append_to(6, g6_81_90)
