#!/usr/bin/env python3
"""Grade 6, Days 161-170 -- extends Grade 6 from 160 to 170 days. Modeled
exactly on gen_grade6_days151_160.py: same L/M/Sc/SS helpers over
gen_curriculum's sub()/day()/append_to(), same TVO Learn placeholder
resourceLabel/resourceUrl convention (videoUrl intentionally left unset,
filled in later by the daily curriculum-video-backfill scheduled task).

Topics chosen to avoid any overlap with the existing Grade 6 Days 1-160
topics (see data/grade6.json), which already densely cover nearly the
entire grade 6 curriculum across all four subjects. New topics: conditional
sentences and if-then statements, static and dynamic characters in
fiction, homographs and multiple-meaning words, writing an opinion piece
for a school newsletter, recognizing deepfakes and digital manipulation,
techniques for effective oral storytelling, comparing multiple accounts of
the same event, dangling and misplaced modifiers, and writing a persuasive
product review for Language; dividing decimals using the standard
algorithm, line plots and frequency distributions, the Cartesian plane and
four quadrants, representing real-world situations with equations, making
predictions from experimental data, understanding GST and HST in everyday
purchases, estimating and measuring angles with a protractor, exponent
laws for multiplying and dividing powers, and recursive versus explicit
pattern rules for Math; gears and how they change speed and force,
physical versus chemical changes in matter, how solar panels convert
sunlight into electricity, the International Space Station and living in
microgravity, animal hibernation and torpor, lightning and thunderstorms,
glaciers and their role in shaping landscapes, food preservation methods,
and tidal and wave power for Science; and the Bank of Canada and monetary
policy, the Charlottetown and Quebec Conferences, the Statute of
Westminster and Canadian independence, Lester B. Pearson and the Nobel
Peace Prize, the Alaska Boundary Dispute, the League of Nations, the
Boundary Waters Treaty, the Rideau Canal as a UNESCO World Heritage Site,
and David Thompson and the mapping of western Canada for Social Studies --
none of those exact ideas appear in Days 1-160. Day 170 is a review day
across all four subjects, matching the end-of-batch pattern used in every
prior 10-day batch; its four review titles are worded distinctly from
every earlier review days titles even though all are review days. No
embedded ASCII apostrophe or double-quote characters are used anywhere in
title/summary/question/option text -- apostrophes are dropped entirely
(e.g. "Canadas" not "Canada's"), matching the rest of Grade 6.

Usage: python3 gen_grade6_days161_170.py
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


def _rebalance_answer_positions(days, seed=20260816):
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


g6_161_170 = [
day(161, [
L('Grammar: Conditional Sentences and If-Then Statements',
  'Grade 6 Language strand: a conditional sentence expresses a condition and its result, often built with an if clause and a result clause, such as If it rains, the game will be cancelled.',
  [('What are the two main parts of a conditional sentence?', ['An if clause and a result clause', 'A subject and a predicate only', 'A prefix and a suffix', 'A quotation and a citation'], 0),
   ('Which sentence is a conditional sentence?', ['If you study, you will pass the test.', 'You studied for the test.', 'The test was difficult.', 'She passed the test easily.'], 0),
   ('In the sentence If it rains, the game will be cancelled, what is the condition?', ['It rains', 'The game will be cancelled', 'The weather is nice', 'The game continues as planned'], 0),
   ('Why might a writer use a conditional sentence to explain a rule?', ['It clearly shows what result follows from a specific situation', 'Conditional sentences never explain rules', 'Conditional sentences remove all information from a sentence', 'A rule can never be expressed using an if clause'], 0),
   ('Why is word order important in a conditional sentence?', ['Swapping the clauses can change which part is the condition and which is the result', 'Word order never affects the meaning of a conditional sentence', 'Conditional sentences do not need a result clause', 'The if clause must always come after the result clause'], 0)]),
M('Number Sense: Dividing Decimals Using the Standard Algorithm',
  'Grade 6 Math strand: dividing decimals using the standard algorithm often involves shifting the decimal point in the divisor to make it a whole number, shifting the decimal point in the dividend the same number of places, then dividing as usual.',
  [('What is the first step often used when dividing by a decimal?', ['Shift the decimal point in the divisor to make it a whole number', 'Round both numbers to the nearest whole number', 'Add the two decimal numbers together', 'Immediately place the decimal point in the answer'], 0),
   ('If the divisor is shifted two places to become a whole number, what else must be shifted two places?', ['The decimal point in the dividend', 'The decimal point in the final answer only', 'Nothing else needs to be shifted', 'The digits of the divisor a second time'], 0),
   ('What is 4.8 divided by 0.6?', ['8', '0.8', '80', '0.08'], 0),
   ('Why does shifting both decimal points the same number of places keep the division problem accurate?', ['Multiplying both numbers by the same power of ten does not change the value of the quotient', 'Shifting decimal points always changes the actual answer', 'Only the divisor can ever be shifted, never the dividend', 'Decimal division does not require any shifting at all'], 0),
   ('Why is it useful to estimate before dividing two decimals precisely?', ['It helps check that the placement of the decimal point in the final answer is reasonable', 'Estimating always gives the exact same value as the precise answer', 'Estimation has no connection to checking decimal division', 'The decimal point never needs to be checked after dividing'], 0)]),
Sc('Simple Machines: Gears and How They Change Speed and Force',
   'Grade 6 Science strand: a gear is a wheel with teeth that interlocks with other gears to transmit motion, and connecting gears of different sizes can change the speed or force of a rotating system.',
   [('What is a gear?', ['A wheel with teeth that interlocks with other gears', 'A straight bar that pivots on a fixed point', 'A rope wrapped around a wheel', 'A ramp used to lift heavy objects'], 0),
    ('What happens when a small gear turns a much larger gear?', ['The larger gear turns more slowly but with more force', 'The larger gear always turns faster with less force', 'Gears of different sizes cannot be connected', 'The larger gear stops turning completely'], 0),
    ('What can connecting gears of different sizes change?', ['The speed or force of a rotating system', 'Only the colour of the gears', 'The temperature of the machine', 'The weight of the gears themselves'], 0),
    ('Why do bicycles use different sized gears?', ['To let a rider trade speed for force depending on the terrain', 'Gears on a bicycle have no effect on riding', 'Bicycles never use more than one gear', 'Different gear sizes only change the appearance of a bicycle'], 0),
    ('Why might engineers use a system of gears instead of a single wheel in a machine?', ['A system of gears can precisely control how speed and force are transmitted between parts', 'A single wheel always transmits force more precisely than a system of gears', 'Gears cannot be combined into a larger system', 'Using multiple gears always wastes mechanical advantage'], 0)]),
SS('Social Studies: The Bank of Canada and Monetary Policy',
   'Grade 6 Social Studies strand: the Bank of Canada is the countrys central bank, responsible for issuing currency, setting interest rates, and working to keep inflation low and stable through monetary policy.',
   [('What is the Bank of Canada?', ['The countrys central bank', 'A private bank that only serves large businesses', 'A branch of a foreign bank operating in Canada', 'A museum dedicated to Canadian history'], 0),
    ('What is one responsibility of the Bank of Canada?', ['Setting interest rates', 'Collecting property taxes', 'Issuing drivers licences', 'Managing national parks'], 0),
    ('What does monetary policy aim to keep low and stable?', ['Inflation', 'The number of banks in Canada', 'The size of the population', 'The number of holidays each year'], 0),
    ('Why might the Bank of Canada raise interest rates when prices are rising quickly?', ['Higher interest rates can slow spending and help control inflation', 'Raising interest rates always increases inflation further', 'Interest rates have no connection to prices in the economy', 'The Bank of Canada cannot change interest rates'], 0),
    ('Why is having an independent central bank considered important for a countrys economy?', ['It allows economic decisions to be made based on long-term stability rather than short-term political pressure', 'An independent central bank has no effect on a countrys economy', 'Central banks are only responsible for printing currency', 'Political pressure should always determine interest rates'], 0)]),
]),
day(162, [
L('Reading: Static and Dynamic Characters in Fiction',
  'Grade 6 Language strand: a static character remains largely unchanged throughout a story, while a dynamic character undergoes significant internal change, often as a result of the storys events.',
  [('What is a static character?', ['A character who remains largely unchanged throughout a story', 'A character who changes significantly by the end of a story', 'A character who never appears in the story', 'A character who narrates the entire story'], 0),
   ('What is a dynamic character?', ['A character who undergoes significant internal change', 'A character who never speaks in the story', 'A character who appears only in the title', 'A character who remains exactly the same throughout'], 0),
   ('What often causes a dynamic character to change?', ['The events and challenges of the story', 'The title of the book', 'The number of chapters in the story', 'The setting alone, without any events'], 0),
   ('Why might a main character in a novel often be dynamic rather than static?', ['Character growth driven by the plot tends to make a story more engaging', 'Dynamic characters are never used as main characters', 'Static characters always play the largest role in a plot', 'A story cannot include any character change'], 0),
   ('Why might a writer include static characters alongside a dynamic main character?', ['They can highlight how much the main character has changed by contrast', 'Static characters always confuse the reader', 'A story is not allowed to include more than one type of character', 'Static characters remove all meaning from a story'], 0)]),
M('Data Management: Line Plots and Frequency Distributions',
  'Grade 6 Math strand: a line plot displays data along a number line using marks such as dots or Xs to show how often each value occurs, making it easy to see the frequency distribution of a data set.',
  [('What does a line plot use to display data?', ['Marks such as dots or Xs placed along a number line', 'Bars of varying height', 'Slices of a circle', 'Connected line segments only'], 0),
   ('What does a line plot make easy to see?', ['How often each value occurs in a data set', 'The exact average of a data set', 'The colour of each data point', 'The location where data was collected'], 0),
   ('What is a frequency distribution?', ['A summary of how often each value occurs in a data set', 'A list of values with no information about how often they occur', 'A single number describing an entire data set', 'A graph that shows only the largest value in a data set'], 0),
   ('Why might a line plot be useful for a small data set with repeated values?', ['It quickly shows which values are most and least common', 'Line plots can only be used with very large data sets', 'Line plots hide all information about repeated values', 'A line plot cannot display more than one data point'], 0),
   ('Why is it helpful to look at the shape of a frequency distribution?', ['It can reveal patterns, such as clusters or gaps, within the data', 'The shape of a distribution never reveals any useful pattern', 'Frequency distributions are always shaped exactly the same', 'Patterns in data can only be found using averages'], 0)]),
Sc('Physical versus Chemical Changes in Matter',
   'Grade 6 Science strand: a physical change alters the form or appearance of matter without changing its chemical makeup, while a chemical change produces a new substance with different properties.',
   [('What happens during a physical change?', ['The form or appearance of matter changes without changing its chemical makeup', 'A completely new substance with different properties is created', 'Matter disappears entirely with no trace', 'The chemical makeup of matter always changes'], 0),
    ('What happens during a chemical change?', ['A new substance with different properties is produced', 'Only the shape of the original substance changes', 'Nothing about the matter changes at all', 'The matter always returns to its original form afterward'], 0),
    ('Which of these is an example of a physical change?', ['Melting ice into water', 'Burning wood into ash', 'Rusting metal', 'Baking a cake'], 0),
    ('Which of these is an example of a chemical change?', ['Burning paper', 'Tearing paper', 'Folding paper', 'Freezing water into ice'], 0),
    ('Why might bubbling, a colour change, or the release of heat suggest a chemical change is occurring?', ['These signs often indicate that a new substance with different properties has formed', 'These signs always indicate a physical change instead', 'Bubbling and colour changes never occur during any reaction', 'These signs show that no change has taken place'], 0)]),
SS('Social Studies: The Charlottetown and Quebec Conferences — Building Confederation',
   'Grade 6 Social Studies strand: in 1864, representatives from British North American colonies met at the Charlottetown Conference and later the Quebec Conference to discuss uniting into a single country, laying the groundwork for Confederation in 1867.',
   [('What was discussed at the Charlottetown Conference in 1864?', ['Uniting British North American colonies into a single country', 'A trade agreement with another country', 'The boundaries of the United States', 'A plan to separate Ontario from Quebec'], 0),
    ('In what year did the Charlottetown and Quebec Conferences take place?', ['1864', '1867', '1812', '1931'], 0),
    ('What conference followed the Charlottetown Conference to continue discussions about union?', ['The Quebec Conference', 'The Berlin Conference', 'The Halifax Conference', 'The Toronto Conference'], 0),
    ('Why might representatives from separate colonies have needed multiple conferences to reach an agreement?', ['Working out the details of a new political union required extensive negotiation among many parties', 'A single meeting was always enough to settle every detail instantly', 'The colonies had no interest in discussing union at all', 'Conferences were held only for ceremonial purposes'], 0),
    ('Why are the Charlottetown and Quebec Conferences considered important steps toward Confederation?', ['They produced the early proposals and agreements that shaped the eventual union of Canada in 1867', 'These conferences had no connection to the eventual formation of Canada', 'Confederation happened immediately with no prior discussion', 'The conferences only concerned trade, not political union'], 0)]),
]),
day(163, [
L('Vocabulary: Homographs and Multiple-Meaning Words',
  'Grade 6 Language strand: a homograph is a word that is spelled the same as another word but may have a different meaning and sometimes a different pronunciation, such as the word tear meaning to rip or a drop of water from crying.',
  [('What is a homograph?', ['A word spelled the same as another word but with a different meaning', 'A word that sounds the same as another word but is spelled differently', 'A word that only has one possible meaning', 'A word used exclusively in formal writing'], 0),
   ('Which word is an example of a homograph with two different meanings?', ['Bat', 'Cat', 'Sun', 'Dog'], 0),
   ('In the sentence She will tear the paper, what does tear mean?', ['To rip', 'A drop of water from crying', 'A type of fabric', 'A kind of paper'], 0),
   ('Why is context important when reading a sentence with a homograph?', ['Context helps a reader determine which meaning of the word is intended', 'Context never changes the meaning of a homograph', 'Homographs always have only one possible meaning', 'A sentence with a homograph cannot be understood at all'], 0),
   ('Why might multiple-meaning words sometimes create confusion for readers?', ['The same spelling can represent very different ideas depending on how it is used', 'Multiple-meaning words are always immediately clear with no possible confusion', 'These words are never used in everyday language', 'Readers never need to consider context when reading'], 0)]),
M('Geometry: The Cartesian Plane and Four Quadrants',
  'Grade 6 Math strand: the Cartesian plane is divided by a horizontal x-axis and a vertical y-axis into four quadrants, and the signs of the x and y coordinates determine which quadrant a point is located in.',
  [('What two axes divide the Cartesian plane?', ['The x-axis and the y-axis', 'The p-axis and the q-axis', 'Only a single diagonal axis', 'The north axis and the south axis'], 0),
   ('How many quadrants does the Cartesian plane have?', ['Four', 'Two', 'Three', 'Six'], 0),
   ('In which quadrant are both the x and y coordinates positive?', ['Quadrant I', 'Quadrant II', 'Quadrant III', 'Quadrant IV'], 0),
   ('In which quadrant would the point negative three, negative five be located?', ['Quadrant III', 'Quadrant I', 'Quadrant II', 'Quadrant IV'], 0),
   ('Why is it useful to know which quadrant a coordinate point falls in before plotting it?', ['It helps quickly estimate the correct location of a point on the plane', 'The quadrant of a point never affects how it should be plotted', 'Every point on the Cartesian plane is located in the same quadrant', 'Knowing the quadrant makes plotting a point impossible'], 0)]),
Sc('How Solar Panels Convert Sunlight into Electricity',
   'Grade 6 Science strand: a solar panel is made of photovoltaic cells that absorb sunlight and convert its energy directly into electrical energy, offering a renewable alternative to fossil fuel power sources.',
   [('What are solar panels made of?', ['Photovoltaic cells', 'Copper wires only', 'Glass with no other materials', 'Magnets connected by cables'], 0),
    ('What do photovoltaic cells convert sunlight into?', ['Electrical energy', 'Sound energy', 'Chemical energy stored in fuel', 'Wind energy'], 0),
    ('Why are solar panels considered a renewable energy source?', ['Sunlight is a naturally replenished resource that will not run out', 'Sunlight is a limited resource that will eventually run out completely', 'Solar panels create energy without using sunlight at all', 'Renewable energy sources cannot use sunlight'], 0),
    ('Why might solar panels produce less electricity on a cloudy day?', ['Less sunlight reaches the photovoltaic cells to be converted into electricity', 'Clouds always increase the amount of electricity solar panels produce', 'Solar panels do not require sunlight to generate electricity', 'Cloud cover has no effect on how solar panels function'], 0),
    ('Why might a homeowner choose to install solar panels despite the upfront cost?', ['Solar panels can lower long-term electricity costs and reduce reliance on fossil fuels', 'Solar panels always increase electricity costs with no benefit', 'Installing solar panels has no effect on electricity bills', 'Solar panels cannot be used to power a home'], 0)]),
SS('Social Studies: The Statute of Westminster and Canadian Independence',
   'Grade 6 Social Studies strand: the Statute of Westminster, passed in 1931, granted Canada and other Dominions greater legislative independence from Britain, marking an important step in Canadas growth as an independent country.',
   [('What did the Statute of Westminster grant to Canada?', ['Greater legislative independence from Britain', 'Complete separation from the British monarchy', 'A new national flag', 'Ownership of new overseas territories'], 0),
    ('In what year was the Statute of Westminster passed?', ['1931', '1867', '1812', '1982'], 0),
    ('Besides Canada, what other kinds of territories did the Statute of Westminster apply to?', ['Other Dominions of the British Empire', 'Only colonies located in Africa', 'Only territories in Asia', 'No other territories were included'], 0),
    ('Why is the Statute of Westminster considered an important step in Canadian history?', ['It expanded Canadas ability to make its own laws separate from Britain', 'It had no effect on how Canada was governed', 'It ended all connections between Canada and Britain immediately', 'It only applied to trade agreements, not lawmaking'], 0),
    ('Why might a countrys move toward greater independence happen gradually over many years rather than all at once?', ['Political and legal changes often build on earlier agreements and require ongoing negotiation', 'Independence always happens in a single instant with no earlier steps', 'Gradual change is never part of how countries gain independence', 'The Statute of Westminster was the very first step toward Canadian government of any kind'], 0)]),
]),
day(164, [
L('Writing: Writing an Opinion Piece for a School Newsletter',
  'Grade 6 Language strand: an opinion piece states a clear position on a topic and supports it with reasons and evidence, while using a tone appropriate for its intended audience, such as a school newsletter.',
  [('What does an opinion piece state?', ['A clear position on a topic', 'Only facts with no personal viewpoint', 'A list of unrelated events', 'A summary of another persons opinion piece'], 0),
   ('What should support the position taken in an opinion piece?', ['Reasons and evidence', 'Random unrelated details', 'Only the writers feelings with no explanation', 'A list of dictionary definitions'], 0),
   ('Why is it important to consider the audience when writing for a school newsletter?', ['The tone and content should suit the readers who will see the newsletter', 'The audience of a newsletter never matters when writing', 'A school newsletter has no specific audience', 'Considering the audience makes an opinion piece weaker'], 0),
   ('Why might a writer include a counterargument in an opinion piece?', ['Addressing an opposing view can make the writers own position appear more convincing', 'Counterarguments always weaken an opinion piece', 'Opinion pieces are not allowed to mention opposing views', 'Including a counterargument removes the writers main position'], 0),
   ('Why should an opinion piece for a school newsletter avoid overly formal or technical language?', ['Clear, accessible language helps the intended readers understand and engage with the writers position', 'Formal language always makes an opinion piece easier to understand', 'A newsletter is only ever read by expert adults', 'Accessible language weakens the strength of an argument'], 0)]),
M('Algebra: Representing Real-World Situations with Equations',
  'Grade 6 Math strand: real-world situations, such as the cost of buying several items, can be represented using algebraic equations that model the relationship between a variable quantity and a known cost or rate.',
  [('What can algebraic equations be used to represent?', ['Real-world situations, such as the cost of buying several items', 'Only situations with no numbers involved', 'Situations that have no possible mathematical solution', 'Only equations found in a textbook with no real application'], 0),
   ('If one notebook costs 3 dollars, which equation represents the total cost c for n notebooks?', ['c equals 3 times n', 'c equals 3 plus n', 'c equals n divided by 3', 'c equals 3 minus n'], 0),
   ('In the equation c equals 3n, what does the variable n represent?', ['The number of notebooks purchased', 'The total cost in dollars', 'The price of a single notebook', 'The name of the store'], 0),
   ('Why is it useful to translate a real-world situation into an algebraic equation?', ['It allows the situation to be solved systematically for different values', 'Translating a situation into an equation removes all useful information', 'Equations can never represent real-world situations', 'A real-world situation never needs to be solved mathematically'], 0),
   ('Why might a store use an equation to calculate the total cost of a customers order?', ['An equation can quickly calculate the cost for any quantity of items purchased', 'Equations cannot be used to calculate the cost of multiple items', 'Stores never need to calculate the total cost of an order', 'An equation only works for a single specific quantity and no others'], 0)]),
Sc('The International Space Station and Living in Microgravity',
   'Grade 6 Science strand: the International Space Station is a research laboratory orbiting Earth where astronauts live and work in microgravity, conducting experiments that would be difficult or impossible to perform on the ground.',
   [('What is the International Space Station?', ['A research laboratory orbiting Earth', 'A telescope located on the surface of the Moon', 'A weather satellite that orbits only over Canada', 'A rocket used for a single launch into space'], 0),
    ('What condition do astronauts experience while living on the International Space Station?', ['Microgravity', 'Extremely high gravity', 'No air pressure changes at all', 'Constant darkness with no daylight'], 0),
    ('Why do astronauts conduct experiments aboard the International Space Station?', ['Some experiments are difficult or impossible to perform on the ground', 'Experiments conducted in space always fail', 'The station has no scientific purpose', 'Ground-based laboratories are always better suited for every experiment'], 0),
    ('Why might muscles and bones weaken during long periods in microgravity?', ['Without the pull of normal gravity, muscles and bones do not work as hard as they do on Earth', 'Microgravity always makes muscles and bones stronger than on Earth', 'Muscles and bones are not affected by gravity in any way', 'Astronauts stop using their muscles entirely while in space'], 0),
    ('Why is international cooperation important for maintaining the International Space Station?', ['Multiple countries share the resources, funding, and expertise needed to operate it', 'The station is operated entirely by a single country with no outside help', 'International cooperation has no role in space exploration', 'The station requires no ongoing maintenance or support'], 0)]),
SS('Social Studies: Lester B. Pearson and the Nobel Peace Prize',
   'Grade 6 Social Studies strand: Lester B. Pearson, a Canadian diplomat and later prime minister, won the Nobel Peace Prize in 1957 for helping resolve the Suez Crisis through the creation of a United Nations peacekeeping force.',
   [('What prize did Lester B. Pearson win in 1957?', ['The Nobel Peace Prize', 'The Order of Canada', 'An Academy Award', 'The Victoria Cross'], 0),
    ('What crisis was Lester B. Pearson recognized for helping resolve?', ['The Suez Crisis', 'The October Crisis', 'The Oka Crisis', 'The Cuban Missile Crisis'], 0),
    ('What did Pearsons plan help create to help resolve the crisis?', ['A United Nations peacekeeping force', 'A new Canadian territory', 'A trade agreement between Egypt and Britain', 'A new branch of the Canadian military'], 0),
    ('What Canadian political role did Lester B. Pearson later hold?', ['Prime Minister', 'Governor General', 'Chief Justice', 'Premier of Ontario'], 0),
    ('Why is Lester B. Pearsons Nobel Peace Prize significant to Canadian history?', ['It highlighted Canadas emerging role in international diplomacy and peacekeeping', 'It had no connection to Canadas role in world affairs', 'Pearson received the award for actions unrelated to diplomacy', 'Peacekeeping has never been associated with Canada'], 0)]),
]),
day(165, [
L('Media Literacy: Recognizing Deepfakes and Digital Manipulation',
  'Grade 6 Language strand: a deepfake is a digitally altered video or image, often created using artificial intelligence, that can make it appear as though someone said or did something they never actually did.',
  [('What is a deepfake?', ['A digitally altered video or image that can misrepresent what someone said or did', 'A completely unedited video with no digital changes', 'A printed newspaper article', 'A handwritten letter sent through the mail'], 0),
   ('What technology is often used to create deepfakes?', ['Artificial intelligence', 'A typewriter', 'A telephone', 'A paper map'], 0),
   ('Why can deepfakes be dangerous when shared online?', ['They can spread false information that looks convincingly real', 'Deepfakes are always immediately obvious to every viewer', 'Deepfakes have no effect on what people believe', 'Digitally altered videos can never mislead anyone'], 0),
   ('What is one strategy for identifying a possible deepfake video?', ['Checking for unnatural movements or inconsistencies around the face', 'Assuming every video seen online is automatically real', 'Ignoring the source of the video entirely', 'Trusting a video simply because it has many views'], 0),
   ('Why is it important for viewers to verify a video with other trusted sources before believing it?', ['Cross-checking helps confirm whether the video accurately represents real events', 'Verifying a video with other sources is never necessary', 'A single video is always enough evidence on its own', 'Trusted sources never provide any useful information about a videos accuracy'], 0)]),
M('Probability: Making Predictions from Experimental Data',
  'Grade 6 Math strand: experimental probability is calculated from the actual results of repeated trials, and this data can be used to make predictions about the likely outcomes of future events.',
  [('How is experimental probability calculated?', ['From the actual results of repeated trials', 'By guessing without collecting any data', 'By assuming every outcome is equally likely with no testing', 'By using only theoretical probability with no experiment'], 0),
   ('What can experimental data be used to do?', ['Make predictions about the likely outcomes of future events', 'Guarantee the exact outcome of every future event', 'Remove the need for any further testing', 'Prove that probability never applies to real situations'], 0),
   ('If a coin lands on heads 18 times out of 30 flips, what is the experimental probability of heads?', ['18 out of 30', '30 out of 18', '12 out of 30', '18 out of 12'], 0),
   ('Why might increasing the number of trials improve the accuracy of a probability prediction?', ['A larger number of trials tends to produce results closer to the true probability', 'More trials always make predictions less accurate', 'A single trial always gives the most accurate prediction', 'The number of trials has no effect on prediction accuracy'], 0),
   ('Why might experimental probability differ from theoretical probability?', ['Random variation in a limited number of trials can cause results to differ from the expected value', 'Experimental and theoretical probability are always exactly equal', 'Experimental probability never involves any randomness', 'Theoretical probability is calculated using real trial results'], 0)]),
Sc('Animal Hibernation and Torpor: Surviving Winter',
   'Grade 6 Science strand: hibernation is a state of greatly reduced activity, heart rate, and body temperature that some animals enter to conserve energy during winter when food is scarce, while torpor is a shorter, less extreme version of this state.',
   [('What is hibernation?', ['A state of greatly reduced activity, heart rate, and body temperature', 'A period of increased activity during winter', 'A process where animals grow new fur every season', 'A migration pattern used only by birds'], 0),
    ('Why do some animals hibernate during winter?', ['To conserve energy when food is scarce', 'To find more food than usual', 'To increase their body temperature', 'Hibernation has no connection to food availability'], 0),
    ('What is torpor?', ['A shorter, less extreme version of hibernation', 'A permanent state that never ends', 'The opposite of hibernation', 'A behaviour found only in fish'], 0),
    ('Why might an animals heart rate drop significantly during hibernation?', ['A slower heart rate uses less energy, helping the animal survive on stored fat', 'A slower heart rate always uses more energy than normal', 'Heart rate has no connection to how much energy an animal uses', 'Animals cannot survive with a reduced heart rate'], 0),
    ('Why might scientists study hibernation to better understand energy conservation?', ['Hibernating animals show extreme examples of how a body can reduce its energy use safely', 'Hibernation has no relevance to understanding energy use', 'Animals that hibernate never conserve any energy', 'Studying hibernation provides no scientific insight'], 0)]),
SS('Social Studies: The Alaska Boundary Dispute',
   'Grade 6 Social Studies strand: the Alaska Boundary Dispute was an early 1900s disagreement between Canada, Britain, and the United States over the exact border between Alaska and British Columbia, settled by a tribunal in a decision many Canadians viewed as unfair.',
   [('What was the Alaska Boundary Dispute about?', ['The exact border between Alaska and British Columbia', 'A trade disagreement over fishing rights in the Atlantic Ocean', 'The location of the capital of British Columbia', 'A disagreement over railway construction in Ontario'], 0),
    ('Which three parties were involved in the Alaska Boundary Dispute?', ['Canada, Britain, and the United States', 'Canada, France, and Mexico', 'Britain, Russia, and the United States', 'Canada, Japan, and the United States'], 0),
    ('How was the Alaska Boundary Dispute ultimately settled?', ['By a decision from a tribunal', 'By a direct vote of Canadian citizens', 'By immediate military conflict', 'The dispute was never resolved'], 0),
    ('How did many Canadians view the tribunals decision?', ['As unfair to Canadian interests', 'As entirely favourable to Canada', 'As having no effect on Canada at all', 'As a decision that ignored Britain completely'], 0),
    ('Why might the Alaska Boundary Dispute have influenced how Canadians viewed their relationship with Britain?', ['It highlighted that Britain sometimes prioritized its own interests over Canadas in international decisions', 'The dispute strengthened Canadians trust in Britain completely', 'The dispute had no effect on Canada-Britain relations', 'Canada had no relationship with Britain at the time of the dispute'], 0)]),
]),
day(166, [
L('Oral Communication: Techniques for Effective Storytelling',
  'Grade 6 Language strand: effective oral storytelling uses techniques such as vocal expression, pacing, and gestures to engage an audience and bring a narrative to life.',
  [('What is one technique used in effective oral storytelling?', ['Vocal expression', 'Reading in a flat, unchanging tone', 'Speaking as quickly as possible at all times', 'Avoiding eye contact with the audience'], 0),
   ('Why might a storyteller change their pacing during a story?', ['To build suspense or emphasize an important moment', 'Pacing has no effect on how a story is received', 'Changing pacing always confuses the audience', 'A storyteller should always speak at exactly the same speed'], 0),
   ('What is one way gestures can support oral storytelling?', ['They can help illustrate actions or emotions described in the story', 'Gestures always distract from a story with no benefit', 'Gestures should never be used while telling a story', 'Gestures replace the need for spoken words entirely'], 0),
   ('Why might a storyteller vary their volume while speaking?', ['To create emphasis and reflect changes in the storys mood', 'Volume has no connection to how a story is understood', 'A storyteller should always speak in a whisper', 'Varying volume always confuses an audience'], 0),
   ('Why is engaging an audience considered an important goal of oral storytelling?', ['A more engaged audience is more likely to understand and remember the story', 'Audience engagement has no effect on how well a story is received', 'Storytelling does not require any audience at all', 'An engaged audience always misunderstands the story being told'], 0)]),
M('Financial Literacy: Understanding GST and HST in Everyday Purchases',
  'Grade 6 Math strand: GST is a federal sales tax applied across Canada, while HST combines the federal tax with a provincial sales tax into a single rate, and both are calculated as a percent added to the price of many purchases.',
  [('What does GST stand for?', ['Goods and Services Tax', 'General Spending Total', 'Government Sales Total', 'Gross Sales Tariff'], 0),
   ('What does HST combine into a single rate?', ['A federal tax and a provincial sales tax', 'Two different federal taxes', 'A tax and a discount', 'An income tax and a property tax'], 0),
   ('How is a sales tax such as GST or HST usually calculated?', ['As a percent added to the price of a purchase', 'As a fixed dollar amount regardless of price', 'By subtracting a percent from the price', 'Sales tax is never calculated using a percent'], 0),
   ('If an item costs 50 dollars and the sales tax rate is 13 percent, approximately how much tax is added?', ['6.50 dollars', '5.00 dollars', '13.00 dollars', '50.00 dollars'], 0),
   ('Why is it useful for shoppers to understand how sales tax is calculated?', ['It helps them estimate the true total cost of a purchase before paying', 'Sales tax never affects the total amount paid for an item', 'Understanding sales tax has no practical use for shoppers', 'The listed price of an item always includes every tax automatically'], 0)]),
Sc('Lightning and Thunderstorms: How They Form',
   'Grade 6 Science strand: thunderstorms form when warm, moist air rises rapidly and cools, building tall storm clouds in which electrical charges separate, eventually discharging as lightning, with thunder created by the rapid expansion of air heated by the strike.',
   [('What kind of air rises to help form a thunderstorm?', ['Warm, moist air', 'Cold, dry air', 'Air with no moisture at all', 'Air that never changes temperature'], 0),
    ('What builds up inside storm clouds and eventually discharges as lightning?', ['Electrical charges', 'Extra oxygen', 'Falling snow', 'Sound waves'], 0),
    ('What causes the sound of thunder?', ['The rapid expansion of air heated suddenly by a lightning strike', 'Wind blowing through the clouds', 'Rain hitting the ground', 'The formation of ice crystals in the clouds'], 0),
    ('Why does thunder often arrive after the flash of lightning is seen?', ['Light travels much faster than sound, so the sound reaches an observer later', 'Sound travels faster than light in the atmosphere', 'Thunder and lightning always happen at the exact same moment', 'Lightning always happens after thunder is heard'], 0),
    ('Why is it dangerous to be outdoors in an open area during a thunderstorm?', ['Tall, exposed objects and people can attract a lightning strike', 'Lightning never strikes open outdoor areas', 'Thunderstorms have no connection to lightning danger', 'Standing outdoors during a storm removes all risk of being struck'], 0)]),
SS('Social Studies: The League of Nations and Its Legacy',
   'Grade 6 Social Studies strand: the League of Nations was an international organization formed after the First World War to help prevent future conflicts through cooperation and diplomacy, though it ultimately failed to stop the outbreak of the Second World War.',
   [('When was the League of Nations formed?', ['After the First World War', 'After the Second World War', 'Before Confederation', 'During the Cold War'], 0),
    ('What was the main goal of the League of Nations?', ['To help prevent future conflicts through cooperation and diplomacy', 'To create a single global currency', 'To establish new colonies around the world', 'To organize international sporting events'], 0),
    ('What eventually happened despite the League of Nations existing?', ['The Second World War broke out', 'All wars around the world ended permanently', 'Every country in the world joined immediately', 'The League successfully prevented every future conflict'], 0),
    ('Why might the League of Nations be considered an important predecessor to the United Nations?', ['It represented an early attempt at international cooperation that later organizations built upon', 'It has no historical connection to the United Nations', 'The League of Nations and the United Nations were founded in the same year', 'International cooperation began only after the League of Nations was dissolved'], 0),
    ('Why might historians study the failures of the League of Nations?', ['Understanding its weaknesses can help explain why later international organizations were designed differently', 'The League of Nations had no weaknesses of any kind', 'Failures of past organizations provide no useful historical lessons', 'The League of Nations succeeded in every one of its goals'], 0)]),
]),
day(167, [
L('Reading: Comparing Multiple Accounts of the Same Event',
  'Grade 6 Language strand: comparing multiple accounts of the same event, such as different news reports or eyewitness descriptions, helps readers notice differences in perspective, detail, and emphasis.',
  [('Why might a reader compare multiple accounts of the same event?', ['To notice differences in perspective, detail, and emphasis', 'Comparing accounts always produces identical information', 'Multiple accounts of an event never differ from one another', 'Reading only one account always provides a complete picture'], 0),
   ('What might cause two eyewitness accounts of the same event to differ?', ['Each witness may have noticed or focused on different details', 'Eyewitnesses always describe events in exactly the same way', 'Eyewitness accounts are never useful for understanding an event', 'Differences between accounts are always caused by lying'], 0),
   ('Why might two news reports about the same event use different emphasis?', ['Different reporters or outlets may choose to highlight different aspects of the story', 'All news reports about the same event are always identical', 'Emphasis has no effect on how an event is understood', 'News reports are not permitted to differ from one another'], 0),
   ('Why is it valuable to read more than one source when researching a historical event?', ['It can provide a more complete and balanced understanding of what happened', 'Reading additional sources always adds unnecessary confusion', 'A single source always provides a complete and unbiased account', 'Comparing sources has no value when researching history'], 0),
   ('Why might a critical reader consider the perspective of the person or organization behind an account?', ['A creators perspective and purpose can shape which details are included or left out', 'The identity of a source never affects its content', 'All accounts are created with the exact same purpose', 'Considering a sources perspective is unnecessary for understanding it'], 0)]),
M('Measurement: Estimating and Measuring Angles with a Protractor',
  'Grade 6 Math strand: a protractor is a tool used to measure the size of an angle in degrees, and estimating an angles size before measuring helps check whether a measurement is reasonable.',
  [('What tool is used to measure the size of an angle?', ['A protractor', 'A ruler', 'A compass for drawing circles', 'A scale for weighing objects'], 0),
   ('What unit is used to measure the size of an angle?', ['Degrees', 'Centimetres', 'Litres', 'Kilograms'], 0),
   ('Why might someone estimate the size of an angle before measuring it with a protractor?', ['It helps check whether the measured value is reasonable', 'Estimating always gives a more accurate value than measuring', 'A protractor cannot be used unless an estimate is made first', 'Estimating an angle has no connection to checking a measurement'], 0),
   ('About how many degrees is a right angle?', ['90 degrees', '45 degrees', '180 degrees', '360 degrees'], 0),
   ('Why is it important to align a protractors baseline correctly with one side of the angle before reading the measurement?', ['Misalignment can cause an inaccurate angle measurement to be read', 'The baseline of a protractor never needs to be aligned with anything', 'A protractor gives an accurate reading no matter how it is placed', 'Alignment only matters when measuring angles larger than 180 degrees'], 0)]),
Sc('Glaciers and Their Role in Shaping Landscapes',
   'Grade 6 Science strand: a glacier is a large, slow-moving mass of ice that can carve valleys, move rocks and sediment, and reshape landscapes over long periods of time as it advances and retreats.',
   [('What is a glacier?', ['A large, slow-moving mass of ice', 'A fast-flowing river of warm water', 'A type of cloud found only in winter', 'A small pond that freezes every year'], 0),
    ('What can a glacier carve into the land as it moves?', ['Valleys', 'Volcanoes', 'Deserts', 'Coral reefs'], 0),
    ('What does a glacier often carry along with it as it moves?', ['Rocks and sediment', 'Only fallen leaves', 'Only ocean water', 'Nothing at all'], 0),
    ('Why might a landscape look very different after a glacier has retreated?', ['The movement of the glacier can carve, scrape, and deposit material, permanently reshaping the land', 'Glaciers never have any effect on the land they move across', 'A retreating glacier always leaves the landscape completely unchanged', 'Glaciers can only affect landscapes while advancing, never while retreating'], 0),
    ('Why might scientists study glaciers to understand past climate conditions?', ['Layers within glacial ice can preserve a long-term record of past climate and atmospheric conditions', 'Glaciers contain no information about past climate conditions', 'Ice never preserves any historical information', 'Studying glaciers only reveals information about current weather'], 0)]),
SS('Social Studies: The Boundary Waters Treaty and Canada-US Relations',
   'Grade 6 Social Studies strand: the Boundary Waters Treaty of 1909 established rules for sharing waterways along the Canada-United States border and created the International Joint Commission to help resolve disputes over these shared waters.',
   [('What did the Boundary Waters Treaty establish rules for?', ['Sharing waterways along the Canada-United States border', 'Sharing farmland between Canada and the United States', 'Building railways between the two countries', 'Trading goods across the Pacific Ocean'], 0),
    ('In what year was the Boundary Waters Treaty signed?', ['1909', '1867', '1931', '1812'], 0),
    ('What organization did the Boundary Waters Treaty help create?', ['The International Joint Commission', 'The United Nations', 'The League of Nations', 'The World Health Organization'], 0),
    ('What is one purpose of the International Joint Commission?', ['To help resolve disputes over waters shared between Canada and the United States', 'To manage trade agreements with countries outside North America', 'To organize elections in both countries', 'To build new highways along the border'], 0),
    ('Why might a treaty about shared waterways be important for two neighbouring countries?', ['Shared resources can lead to disputes without clear, agreed-upon rules for managing them', 'Neighbouring countries never need to share any natural resources', 'Waterways along a border never require any formal agreements', 'A treaty about water has no effect on relations between two countries'], 0)]),
]),
day(168, [
L('Grammar: Dangling and Misplaced Modifiers',
  'Grade 6 Language strand: a modifier describes or gives more information about another word in a sentence, and a dangling or misplaced modifier occurs when it is positioned so that it unclearly or incorrectly describes the wrong word.',
  [('What does a modifier do in a sentence?', ['Describes or gives more information about another word', 'Replaces the subject of a sentence entirely', 'Always ends a sentence', 'Joins two unrelated sentences together'], 0),
   ('What is a misplaced modifier?', ['A modifier positioned so it unclearly or incorrectly describes the wrong word', 'A modifier that is always placed correctly', 'A modifier that has been completely removed from a sentence', 'A word that never describes anything in a sentence'], 0),
   ('Which sentence contains a misplaced modifier?', ['Running down the street, the bus was missed by Sam.', 'Sam missed the bus while running down the street.', 'Running down the street, Sam missed the bus.', 'Sam, running down the street, missed the bus.'], 0),
   ('Why can a dangling modifier confuse a reader?', ['It can make it unclear which word in the sentence is actually being described', 'Dangling modifiers always make a sentence perfectly clear', 'Modifiers never have any connection to the words around them', 'A dangling modifier always improves the clarity of a sentence'], 0),
   ('Why is it important to revise sentences with misplaced or dangling modifiers?', ['Correcting them helps ensure the sentence clearly expresses the intended meaning', 'Misplaced modifiers never need to be corrected', 'Revising a sentence always makes its meaning less clear', 'Modifiers have no effect on the clarity of a sentence'], 0)]),
M('Number Sense: Exponent Laws — Multiplying and Dividing Powers',
  'Grade 6 Math strand: when multiplying powers with the same base, the exponents are added together, and when dividing powers with the same base, the exponents are subtracted.',
  [('What rule applies when multiplying two powers with the same base?', ['The exponents are added together', 'The exponents are multiplied together', 'The bases are added together', 'The exponents are subtracted from each other'], 0),
   ('What rule applies when dividing two powers with the same base?', ['The exponents are subtracted', 'The exponents are added', 'The bases are divided and the exponents stay the same', 'The exponents are multiplied together'], 0),
   ('What is the value of 2 to the power of 3 multiplied by 2 to the power of 2, expressed as a single power?', ['2 to the power of 5', '2 to the power of 6', '2 to the power of 1', '4 to the power of 5'], 0),
   ('What is the value of 5 to the power of 6 divided by 5 to the power of 2, expressed as a single power?', ['5 to the power of 4', '5 to the power of 8', '5 to the power of 3', '5 to the power of 12'], 0),
   ('Why must the bases of two powers be the same before adding or subtracting their exponents?', ['The exponent rules for multiplying and dividing powers only apply when the bases match', 'The bases of powers never need to match for these rules to work', 'Exponent rules apply equally well regardless of the base used', 'Exponents can always be combined even with completely different bases'], 0)]),
Sc('Food Preservation: How Refrigeration, Canning, and Drying Prevent Spoilage',
   'Grade 6 Science strand: food preservation methods such as refrigeration, canning, and drying slow or stop the growth of the microorganisms that cause food to spoil, helping keep food safe to eat for longer periods of time.',
   [('What do food preservation methods such as refrigeration and drying slow or stop?', ['The growth of microorganisms that cause food to spoil', 'The growth of the plants used to make the food', 'The colour of the food', 'The weight of the food'], 0),
    ('How does refrigeration help preserve food?', ['Cold temperatures slow the growth of bacteria and other microorganisms', 'Cold temperatures speed up the growth of bacteria', 'Refrigeration removes all water from food', 'Refrigeration has no effect on microorganisms'], 0),
    ('How does drying help preserve food?', ['Removing moisture makes it harder for microorganisms to grow', 'Adding moisture helps preserve food for longer', 'Drying always destroys the nutrients in food completely', 'Drying has no connection to microorganism growth'], 0),
    ('Why might canning allow food to be stored safely for a long time without refrigeration?', ['Sealing food in an airtight container after heating can prevent microorganisms from growing inside', 'Canned food is never sealed in an airtight container', 'Canning always increases the growth of microorganisms', 'Heating food before canning has no effect on spoilage'], 0),
    ('Why have humans developed multiple methods of food preservation throughout history?', ['Different methods allow food to be safely stored for longer periods in different situations and climates', 'A single method of food preservation works equally well in every situation', 'Food preservation methods have no connection to safely storing food', 'Humans have never needed to preserve food for later use'], 0)]),
SS('Social Studies: The Rideau Canal — A UNESCO World Heritage Site in Canada',
   'Grade 6 Social Studies strand: the Rideau Canal, built between 1826 and 1832 to connect Kingston and Ottawa, was originally constructed for military defense purposes and is now recognized as a UNESCO World Heritage Site, famous today for winter skating.',
   [('What two cities does the Rideau Canal connect?', ['Kingston and Ottawa', 'Toronto and Montreal', 'Halifax and Quebec City', 'Winnipeg and Regina'], 0),
    ('During what years was the Rideau Canal built?', ['1826 to 1832', '1867 to 1870', '1900 to 1905', '1931 to 1935'], 0),
    ('What was the original purpose of building the Rideau Canal?', ['Military defense', 'Tourism and recreation only', 'Transporting oil and gas', 'Generating hydroelectric power'], 0),
    ('What international recognition has the Rideau Canal received?', ['It is recognized as a UNESCO World Heritage Site', 'It has been declared a national capital', 'It received an Olympic medal', 'It was renamed after a foreign country'], 0),
    ('Why might a structure originally built for military purposes become an important recreational site today?', ['Its original design and location can make it well suited for new uses, such as winter skating, once its military role ends', 'Structures built for military purposes can never be used for anything else', 'The Rideau Canal has never been used for any purpose other than defense', 'Recreational uses always existed before the canal was built for defense'], 0)]),
]),
day(169, [
L('Writing: Writing a Persuasive Product Review',
  'Grade 6 Language strand: a persuasive product review states a clear opinion about a product, supports it with specific reasons and examples, and considers the needs of readers who are deciding whether to make a purchase.',
  [('What does a persuasive product review state?', ['A clear opinion about a product', 'Only the price of a product with no opinion', 'A list of unrelated products', 'Instructions for manufacturing the product'], 0),
   ('What should support the opinion given in a persuasive product review?', ['Specific reasons and examples', 'Vague statements with no explanation', 'Information about a completely different product', 'A summary of someone elses opinion with no personal view'], 0),
   ('Why might a writer consider the needs of readers when writing a product review?', ['Readers are often deciding whether to make a purchase and want helpful, relevant information', 'The needs of readers never matter when writing a review', 'Product reviews are never read by anyone making a purchase decision', 'Considering readers needs always weakens a review'], 0),
   ('Why might a strong product review mention both strengths and weaknesses of a product?', ['Acknowledging weaknesses can make the review seem more balanced and trustworthy', 'Mentioning weaknesses always makes a review less convincing', 'A persuasive review must never mention any weaknesses', 'Balanced reviews are never useful to readers'], 0),
   ('Why is specific detail, such as measurements or comparisons, valuable in a persuasive product review?', ['Specific details give readers concrete information to help them evaluate the product', 'Specific details always make a review more confusing', 'Vague descriptions are always more persuasive than specific details', 'Readers never benefit from concrete information in a review'], 0)]),
M('Patterning and Algebra: Recursive versus Explicit Pattern Rules',
  'Grade 6 Math strand: a recursive pattern rule describes how to find the next term using the term before it, while an explicit pattern rule describes how to calculate any term directly using its position in the pattern.',
  [('What does a recursive pattern rule describe?', ['How to find the next term using the term before it', 'How to calculate any term directly from its position', 'A rule that only applies to the first term of a pattern', 'A pattern with no relationship between its terms'], 0),
   ('What does an explicit pattern rule describe?', ['How to calculate any term directly using its position in the pattern', 'How to find the next term using only the previous term', 'A rule that cannot be used to find any term', 'A pattern that never has a position for its terms'], 0),
   ('If a pattern rule is start at 4 and add 3 each time, what kind of rule is this?', ['Recursive', 'Explicit', 'Neither recursive nor explicit', 'Both at the same time with no distinction'], 0),
   ('Why might an explicit rule be more useful than a recursive rule for finding a term far along in a pattern?', ['An explicit rule can calculate the term directly without finding every term before it', 'A recursive rule always finds distant terms more quickly than an explicit rule', 'Explicit rules can never be used to find distant terms', 'Recursive and explicit rules always require the exact same amount of work'], 0),
   ('Why is it useful to be able to describe a pattern using both recursive and explicit rules?', ['Each type of rule offers a different way to understand and apply the pattern', 'Only one type of rule can ever be used to describe a pattern', 'Recursive and explicit rules always produce different, unrelated patterns', 'Understanding a pattern in more than one way provides no benefit'], 0)]),
Sc('Renewable Energy: Tidal and Wave Power',
   'Grade 6 Science strand: tidal power captures energy from the rise and fall of ocean tides, while wave power captures energy from the motion of waves at the oceans surface, both offering renewable alternatives to fossil fuels.',
   [('What does tidal power capture energy from?', ['The rise and fall of ocean tides', 'The heat of the Sun', 'The motion of wind across land', 'Underground heat from the Earths core'], 0),
    ('What does wave power capture energy from?', ['The motion of waves at the oceans surface', 'The rise and fall of tides only', 'The heat stored in ocean water', 'The growth of underwater plants'], 0),
    ('Why are tidal and wave power considered renewable energy sources?', ['They rely on ongoing natural ocean movements that are not used up', 'They rely on a limited fuel supply that will eventually run out', 'Ocean movements stop permanently once energy is captured', 'Renewable energy sources cannot come from the ocean'], 0),
    ('Why might a coastal region be well suited for generating tidal or wave power?', ['Its direct access to ocean tides and waves provides a consistent source of energy', 'Coastal regions never experience any tides or waves', 'Tidal and wave power can only be generated far from any coastline', 'Access to the ocean has no connection to generating this type of energy'], 0),
    ('Why might tidal and wave power be considered more predictable than some other renewable sources, such as wind?', ['Ocean tides follow regular, well-understood cycles that can be forecast in advance', 'Ocean tides occur completely randomly with no pattern at all', 'Wind is always more predictable than ocean tides', 'Tidal and wave patterns can never be forecast or understood'], 0)]),
SS('Social Studies: David Thompson and the Mapping of Western Canada',
   'Grade 6 Social Studies strand: David Thompson was a fur trader and surveyor who mapped vast areas of western North America in the early 1800s, producing detailed maps that were used for decades after his expeditions.',
   [('What two roles did David Thompson hold during his expeditions?', ['Fur trader and surveyor', 'Soldier and sailor', 'Farmer and blacksmith', 'Judge and lawyer'], 0),
    ('What part of North America did David Thompson help map?', ['Western North America', 'Only the east coast', 'Only present-day Quebec', 'Territories outside of North America'], 0),
    ('During what general time period did David Thompson complete most of his mapping expeditions?', ['The early 1800s', 'The late 1900s', 'The 1600s', 'The 1930s'], 0),
    ('Why were David Thompsons maps considered valuable for many years after they were created?', ['They provided detailed and accurate geographic information used by later travellers and settlers', 'His maps were considered inaccurate and were never used by anyone', 'Maps of western Canada were not needed by anyone after Thompsons expeditions', 'His maps only covered a single small town'], 0),
    ('Why might exploring and mapping unfamiliar territory have been an important part of the fur trade economy?', ['Accurate maps helped traders navigate efficiently and locate new areas for trade', 'Mapping had no connection to the success of the fur trade', 'Fur traders never needed to travel through unfamiliar territory', 'The fur trade did not rely on geographic knowledge of any kind'], 0)]),
]),
day(170, [
L('Language Review: Grammar, Storytelling, and Media Literacy',
  'Grade 6 Language strand review: students revisit conditional sentences, homographs and multiple-meaning words, opinion writing, deepfakes and digital manipulation, and oral storytelling techniques.',
  [('What are the two main parts of a conditional sentence?', ['An if clause and a result clause', 'A subject and a predicate only', 'A prefix and a suffix', 'A quotation and a citation'], 0),
   ('What is a homograph?', ['A word spelled the same as another word but with a different meaning', 'A word that sounds the same as another word but is spelled differently', 'A word that only has one possible meaning', 'A word used exclusively in formal writing'], 0),
   ('What does an opinion piece state?', ['A clear position on a topic', 'Only facts with no personal viewpoint', 'A list of unrelated events', 'A summary of another persons opinion piece'], 0),
   ('What is a deepfake?', ['A digitally altered video or image that can misrepresent what someone said or did', 'A completely unedited video with no digital changes', 'A printed newspaper article', 'A handwritten letter sent through the mail'], 0),
   ('What is one technique used in effective oral storytelling?', ['Vocal expression', 'Reading in a flat, unchanging tone', 'Speaking as quickly as possible at all times', 'Avoiding eye contact with the audience'], 0)]),
M('Math Review: Decimals, Data, and Algebraic Reasoning',
  'Grade 6 Math strand review: students revisit dividing decimals, line plots, the Cartesian plane, representing situations with equations, and experimental probability.',
  [('What is the first step often used when dividing by a decimal?', ['Shift the decimal point in the divisor to make it a whole number', 'Round both numbers to the nearest whole number', 'Add the two decimal numbers together', 'Immediately place the decimal point in the answer'], 0),
   ('What does a line plot use to display data?', ['Marks such as dots or Xs placed along a number line', 'Bars of varying height', 'Slices of a circle', 'Connected line segments only'], 0),
   ('What two axes divide the Cartesian plane?', ['The x-axis and the y-axis', 'The p-axis and the q-axis', 'Only a single diagonal axis', 'The north axis and the south axis'], 0),
   ('What can algebraic equations be used to represent?', ['Real-world situations, such as the cost of buying several items', 'Only situations with no numbers involved', 'Situations that have no possible mathematical solution', 'Only equations found in a textbook with no real application'], 0),
   ('How is experimental probability calculated?', ['From the actual results of repeated trials', 'By guessing without collecting any data', 'By assuming every outcome is equally likely with no testing', 'By using only theoretical probability with no experiment'], 0)]),
Sc('Science Review: Machines, Matter, and Space Exploration',
   'Grade 6 Science strand review: students revisit gears, physical versus chemical changes, solar panels, the International Space Station, and hibernation.',
   [('What is a gear?', ['A wheel with teeth that interlocks with other gears', 'A straight bar that pivots on a fixed point', 'A rope wrapped around a wheel', 'A ramp used to lift heavy objects'], 0),
    ('What happens during a physical change?', ['The form or appearance of matter changes without changing its chemical makeup', 'A completely new substance with different properties is created', 'Matter disappears entirely with no trace', 'The chemical makeup of matter always changes'], 0),
    ('What are solar panels made of?', ['Photovoltaic cells', 'Copper wires only', 'Glass with no other materials', 'Magnets connected by cables'], 0),
    ('What is the International Space Station?', ['A research laboratory orbiting Earth', 'A telescope located on the surface of the Moon', 'A weather satellite that orbits only over Canada', 'A rocket used for a single launch into space'], 0),
    ('What is hibernation?', ['A state of greatly reduced activity, heart rate, and body temperature', 'A period of increased activity during winter', 'A process where animals grow new fur every season', 'A migration pattern used only by birds'], 0)]),
SS('Social Studies Review: Canadian Institutions, History, and Exploration',
   'Grade 6 Social Studies strand review: students revisit the Bank of Canada, the Charlottetown Conference, the Statute of Westminster, Lester B. Pearson, and the Alaska Boundary Dispute.',
   [('What is the Bank of Canada?', ['The countrys central bank', 'A private bank that only serves large businesses', 'A branch of a foreign bank operating in Canada', 'A museum dedicated to Canadian history'], 0),
    ('What was discussed at the Charlottetown Conference in 1864?', ['Uniting British North American colonies into a single country', 'A trade agreement with another country', 'The boundaries of the United States', 'A plan to separate Ontario from Quebec'], 0),
    ('What did the Statute of Westminster grant to Canada?', ['Greater legislative independence from Britain', 'Complete separation from the British monarchy', 'A new national flag', 'Ownership of new overseas territories'], 0),
    ('What prize did Lester B. Pearson win in 1957?', ['The Nobel Peace Prize', 'The Order of Canada', 'An Academy Award', 'The Victoria Cross'], 0),
    ('What was the Alaska Boundary Dispute about?', ['The exact border between Alaska and British Columbia', 'A trade disagreement over fishing rights in the Atlantic Ocean', 'The location of the capital of British Columbia', 'A disagreement over railway construction in Ontario'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g6_161_170)
    append_to(6, g6_161_170)
