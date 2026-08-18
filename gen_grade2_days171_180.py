#!/usr/bin/env python3
"""Grade 2, Days 171-180 -- fifteenth batch, extending Grade 2 past Day 170
toward the full ~187-day school year.

Structural note (checked directly before writing this file): the task
brief for this batch described Grade 2 as using a "worksheet-required"
format with its own append_worksheet_days() helper and a 3-item worksheet
field on every subject. That description does NOT match the actual
immediately-prior batch, gen_grade2_days161_170.py, which was read in
full first per the required process. That file's own docstring explicitly
states there is no worksheet argument anywhere in Grade 2's generator
scripts past roughly Day 100, and that append_worksheet_days() only
appears in the Grade 0 and Grade 1 scripts and in Grade 2's much older
Days 31-100 scripts. Grepping every gen_grade2_days*.py file in the repo
for the literal word "worksheet" confirms every hit is inside a docstring
explaining why it is NOT used, never in actual code. So this file follows
the real, current, established Grade 2 pattern instead of the inaccurate
brief: it uses the sub()/day()/append_to() helpers imported directly from
gen_curriculum.py, with Grade 2's exact signature
(subject_key, title, summary, resourceLabel, resourceUrl, quiz) and no
worksheet field of any kind, matching gen_grade2_days161_170.py exactly:

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} grade 2 educational")
- no videoUrl field (filled in later by the video-backfill task)

Topics chosen to avoid overlap with existing Grade 2 Days 1-170 (dumped
and checked against data/grade2.json before writing, which already
densely covers nearly the full grade 2 ELA, math, science, and social
studies curriculum):

Language: limericks, reflexive pronouns, tall tales, onset and rime,
kennings, thank-you notes, fables, diamante poems, and the tch/dge
trigraph sounds -- none of which appear in the existing Days 1-170
Language coverage (which already includes riddles, haiku, shape poems,
list poems, free verse, acrostic poems, possessive nouns, possessive
pronouns, personal pronouns, several consonant blend and digraph
families, and dozens of other topics).

Math: subtracting fractions with the same denominator, circle graphs,
Canadian paper bills, converting minutes to seconds, comparing weight
with a balance scale, points/lines/line segments/rays, reading a
schedule or timetable, skip counting by 6s-9s, and Carroll diagrams for
sorting. (Adding fractions with the same denominator, most other graph
types, Canadian coin values, most other time-conversion and geometry
topics, and most other skip-counting sequences are already covered
across Days 1-170, so new angles distinct from that existing coverage
were chosen instead.)

Science: chameleons, kangaroos, jellyfish, hummingbirds, savanna
habitats, solar eclipses, pulleys, frogs and toads, and wedges/screws --
none of which appear in the very dense existing Days 1-170 science
coverage (which already includes sharks, penguins, bats, octopuses,
turtles, camouflage and mimicry generally, levers, wheels and axles,
compound machines, moon phases, planets, and dozens of other animals,
habitats, and physical-science topics).

Social Studies: the House of Commons, the Canadian passport, National
Indigenous Peoples Day, search and rescue services, the northern lights,
Hudson Bay, the Rocky Mountains, border crossings, and the Royal
Canadian Mint -- distinct from the existing Senate, Governor General,
Truth and Reconciliation Day, Coast Guard, Great Lakes, Niagara Falls,
CN Tower, immigration, and Bank of Canada lessons already in Days 1-170.

Day 180 is a review day across all four subjects, matching the
end-of-batch pattern used in every prior 10-day batch (Day 150, Day 160,
Day 170, etc). Its four review titles are textually distinct from every
earlier review title in Days 1-170. No embedded ASCII double-quote or
straight apostrophe characters are used anywhere in title/summary/quiz
text -- contractions and possessives are avoided entirely (or rewritten
without the apostrophe, e.g. "Canadas" not "Canada's") to keep the
generated .ts string literals valid.
"""
import os
import urllib.parse
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_curriculum import sub, day, append_to


def mk(subject_key, title, summary, quiz):
    rl = f'YouTube: {title}'
    ru = 'https://www.youtube.com/results?search_query=' + urllib.parse.quote(f'{title} grade 2 educational')
    return sub(subject_key, title, summary, rl, ru, quiz)


def L(t, s, q):
    return mk('Language', t, s, q)


def M(t, s, q):
    return mk('Math', t, s, q)


def Sc(t, s, q):
    return mk('Science', t, s, q)


def SS(t, s, q):
    return mk('SocialStudies', t, s, q)


def _rebalance_answer_positions(days, seed=20260818):
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
    return days


g2_171_180 = [
day(171, [
L('Limericks: Silly Rhyming Poems in Five Lines',
  'Grade 2 Language strand: a limerick is a short, funny poem with five lines, where lines one, two, and five rhyme with each other, and lines three and four rhyme with each other.',
  [('How many lines does a limerick have?', ['Five', 'Three', 'Ten', 'One'], 0),
   ('Which lines in a limerick usually rhyme with each other?', ['Lines one, two, and five', 'Only line one', 'Every line rhymes with every other line', 'No lines rhyme'], 0),
   ('What is the tone of most limericks?', ['Funny and playful', 'Very serious', 'Silent', 'Angry'], 0),
   ('Lines three and four of a limerick are usually ___.', ['Shorter and rhyme with each other', 'Longer than every other line', 'Written with no words', 'Identical to line one'], 0),
   ('Why might a writer choose to write a limerick?', ['To tell a short, humorous rhyme', 'To write a serious news report', 'To avoid using any rhyme', 'To write without any lines'], 0)]),
M('Fractions: Subtracting Fractions with the Same Denominator',
  'Grade 2 Math strand: when two fractions share the same denominator, you can subtract them by keeping the denominator the same and subtracting only the numerators.',
  [('When subtracting fractions with the same denominator, what stays the same?', ['The denominator', 'The numerator', 'Both numbers change', 'Nothing stays the same'], 0),
   ('What is three-quarters minus one-quarter?', ['One-half', 'One-quarter', 'Three-quarters', 'One whole'], 0),
   ('To subtract fractions with the same denominator, you subtract the ___.', ['Numerators', 'Denominators', 'Whole numbers only', 'Nothing at all'], 0),
   ('What is four-fifths minus two-fifths?', ['Two-fifths', 'Six-fifths', 'One-fifth', 'Four-fifths'], 0),
   ('Why is it easier to subtract fractions when the denominators match?', ['The parts are already the same size', 'Matching denominators make the problem impossible', 'The numerators disappear', 'Fractions with the same denominator cannot be compared'], 0)]),
Sc('Chameleons: Masters of Camouflage',
   'Grade 2 Science strand: chameleons are lizards known for changing colour to match their surroundings, communicate, and regulate their body temperature.',
   [('What are chameleons best known for?', ['Changing colour', 'Flying through the air', 'Living underwater only', 'Building large nests'], 0),
    ('What kind of animal is a chameleon?', ['A lizard', 'A bird', 'A fish', 'An insect'], 0),
    ('Besides blending in, why else might a chameleon change colour?', ['To communicate or regulate its temperature', 'Colour change has no purpose', 'Only to sleep', 'Only to swim faster'], 0),
    ('Chameleon colour change is an example of an animal ___.', ['Adaptation', 'Habitat', 'Instrument', 'Vehicle'], 0),
    ('Which environment might a chameleon commonly be found in?', ['Trees and shrubs in warm regions', 'Deep ocean trenches', 'Arctic ice sheets', 'Underground tunnels only'], 0)]),
SS('The House of Commons: Where Canadas Laws Begin',
   'Grade 2 Social Studies strand: the House of Commons is the part of the Canadian Parliament where elected Members of Parliament debate and vote on new laws.',
   [('What is the House of Commons?', ['The part of Parliament where MPs debate and vote on laws', 'A type of school', 'A local library', 'A sports arena'], 0),
    ('Who works in the House of Commons?', ['Elected Members of Parliament', 'Only judges', 'Only mayors', 'Only teachers'], 0),
    ('What do Members of Parliament do in the House of Commons?', ['Debate and vote on new laws', 'Deliver mail', 'Build roads', 'Coach sports teams'], 0),
    ('How do people become Members of Parliament?', ['They are elected by voters', 'They are chosen at random', 'They inherit the job', 'They apply online with no vote'], 0),
    ('The House of Commons is part of which larger institution?', ['The Canadian Parliament', 'A city council', 'A school board', 'A local business'], 0)]),
]),
day(172, [
L('Reflexive Pronouns: Myself, Yourself, and Themselves',
  'Grade 2 Language strand: a reflexive pronoun refers back to the subject of a sentence, such as myself, yourself, himself, herself, itself, ourselves, and themselves.',
  [('What does a reflexive pronoun do?', ['Refers back to the subject of the sentence', 'Asks a question', 'Names a place', 'Shows an action only'], 0),
   ('Which word is a reflexive pronoun?', ['Myself', 'Run', 'Blue', 'Quickly'], 0),
   ('In the sentence She made the card herself, which word is the reflexive pronoun?', ['Herself', 'Made', 'Card', 'She'], 0),
   ('Which reflexive pronoun matches with the subject they?', ['Themselves', 'Himself', 'Herself', 'Itself'], 0),
   ('Which sentence uses a reflexive pronoun correctly?', ['I hurt myself while running', 'I hurt himself while running', 'I hurt themselves while running', 'I hurt herself while running'], 0)]),
M('Data: Circle Graphs — Showing Parts of a Whole',
  'Grade 2 Math strand: a circle graph, also called a pie chart, uses slices of a circle to show how a whole amount is divided into different parts.',
  [('What shape is used in a circle graph?', ['A circle', 'A rectangle', 'A triangle', 'A line'], 0),
   ('What does each slice of a circle graph represent?', ['A part of the whole amount', 'A separate unrelated topic', 'The title of the graph', 'A single dot of data'], 0),
   ('A circle graph is also known as a ___.', ['Pie chart', 'Bar graph', 'Line plot', 'Tally chart'], 0),
   ('If one slice of a circle graph is very large, what does that likely mean?', ['That category makes up a big part of the whole', 'That category has no data at all', 'The graph is drawn incorrectly', 'The slice represents zero'], 0),
   ('Circle graphs are especially useful for showing ___.', ['How a whole is divided into parts', 'Only numbers with no meaning', 'A single moment with no comparison', 'Sounds instead of numbers'], 0)]),
Sc('Kangaroos: Hopping Marsupials',
   'Grade 2 Science strand: kangaroos are marsupials, meaning the mother carries her young in a pouch, and they use their strong back legs to hop instead of walk.',
   [('What is a marsupial?', ['An animal that carries its young in a pouch', 'An animal that lives only underwater', 'An animal with no legs', 'An animal that never moves'], 0),
    ('How do kangaroos usually move?', ['By hopping on strong back legs', 'By slithering on their belly', 'By flying', 'By swimming only'], 0),
    ('Where does a baby kangaroo often stay after being born?', ['In its mothers pouch', 'In a nest in a tree', 'In the ocean', 'In a burrow made of ice'], 0),
    ('What continent are kangaroos most closely associated with?', ['Australia', 'Antarctica', 'North America', 'Europe'], 0),
    ('Kangaroos are an example of an animal grouped as a ___.', ['Marsupial', 'Reptile', 'Amphibian', 'Insect'], 0)]),
SS('The Canadian Passport: Traveling as a Canadian Citizen',
   'Grade 2 Social Studies strand: a Canadian passport is an official document that proves citizenship and identity, allowing citizens to travel to and return from other countries.',
   [('What is a Canadian passport?', ['An official document proving citizenship and identity', 'A type of currency', 'A kind of map', 'A school report card'], 0),
    ('What can a passport allow a citizen to do?', ['Travel to and return from other countries', 'Vote in an election', 'Attend a local school', 'Drive a car'], 0),
    ('Who issues Canadian passports?', ['The Canadian government', 'A local school', 'A private company with no rules', 'A sports league'], 0),
    ('Why might border officials ask to see a passport?', ['To confirm a travelers identity and citizenship', 'To collect stamps for fun only', 'Passports are never checked', 'To sell the traveler something'], 0),
    ('A passport is an example of an official ___.', ['Document', 'Toy', 'Meal', 'Building'], 0)]),
]),
day(173, [
L('Tall Tales: Larger-Than-Life Stories',
  'Grade 2 Language strand: a tall tale is a story with a larger-than-life main character who performs impossible or greatly exaggerated feats, often told in a matter-of-fact way.',
  [('What makes a tall tale different from a realistic story?', ['It features exaggerated, impossible feats', 'It only describes true daily events', 'It has no characters at all', 'It is always written as a list'], 0),
   ('How are the feats in a tall tale usually described?', ['As impossible or greatly exaggerated', 'As very ordinary and small', 'As boring and forgettable', 'As things that happen every day'], 0),
   ('What kind of main character often appears in a tall tale?', ['A larger-than-life hero', 'A character with no traits', 'A character who does nothing', 'A silent narrator only'], 0),
   ('Tall tales are often told in a ___ tone, as if the events were normal.', ['Matter-of-fact', 'Confused', 'Apologetic', 'Silent'], 0),
   ('Which of these sounds most like a detail from a tall tale?', ['He could leap over a mountain in one step', 'She walked to the store', 'He ate breakfast at eight', 'She read a book quietly'], 0)]),
M('Money: Canadian Paper Bills — Five, Ten, Twenty, Fifty, and Hundred Dollars',
  'Grade 2 Math strand: Canadian paper bills come in different values, including the five, ten, twenty, fifty, and one hundred dollar bills, each showing a different number and colour.',
  [('What is the value of a five dollar bill?', ['Five dollars', 'Ten dollars', 'Twenty dollars', 'One dollar'], 0),
   ('What is the value of a twenty dollar bill?', ['Twenty dollars', 'Two dollars', 'Two hundred dollars', 'Twelve dollars'], 0),
   ('Which bill has the greatest value: a ten, a twenty, or a fifty?', ['The fifty dollar bill', 'The ten dollar bill', 'The twenty dollar bill', 'They are all equal'], 0),
   ('How can you quickly tell Canadian bills apart?', ['By the number and colour printed on each bill', 'All Canadian bills look exactly the same', 'By their smell', 'By their weight only'], 0),
   ('If you have one ten dollar bill and one five dollar bill, how much money do you have in total?', ['Fifteen dollars', 'Ten dollars', 'Five dollars', 'Fifty dollars'], 0)]),
Sc('Jellyfish: Simple Creatures of the Sea',
   'Grade 2 Science strand: jellyfish are soft-bodied ocean animals made mostly of water, with no brain or bones, that drift with ocean currents and use stinging tentacles to catch food.',
   [('What are jellyfish mostly made of?', ['Water', 'Bone', 'Fur', 'Metal'], 0),
    ('Do jellyfish have a brain or bones?', ['No', 'Yes, both', 'Only a brain', 'Only bones'], 0),
    ('How do jellyfish often move through the ocean?', ['By drifting with ocean currents', 'By running on the seafloor', 'By flying above the waves', 'By digging tunnels'], 0),
    ('What do jellyfish use to catch food?', ['Stinging tentacles', 'Sharp claws', 'Large teeth', 'Wings'], 0),
    ('Jellyfish are an example of an animal that lives ___.', ['In the ocean', 'In deserts', 'In mountain caves', 'In the sky'], 0)]),
SS('National Indigenous Peoples Day: June 21',
   'Grade 2 Social Studies strand: National Indigenous Peoples Day is celebrated on June 21 each year in Canada to honour the heritage, cultures, and achievements of First Nations, Inuit, and Metis peoples.',
   [('On what date is National Indigenous Peoples Day celebrated?', ['June 21', 'January 1', 'July 1', 'December 25'], 0),
    ('What does National Indigenous Peoples Day honour?', ['The heritage, cultures, and achievements of Indigenous peoples', 'A type of weather pattern', 'A sports championship', 'A new type of currency'], 0),
    ('Which groups are recognized on this day?', ['First Nations, Inuit, and Metis peoples', 'Only visitors from other countries', 'Only students in one province', 'Only professional athletes'], 0),
    ('Why might a country set aside a special day to honour a groups heritage?', ['To recognize and celebrate their history and contributions', 'Special days never have a purpose', 'To ignore their history completely', 'To replace their traditions with new ones'], 0),
    ('National Indigenous Peoples Day is an example of a ___.', ['National day of recognition', 'Type of election', 'Kind of currency', 'Sports league'], 0)]),
]),
day(174, [
L('Onset and Rime: Building Words From Sounds',
  'Grade 2 Language strand: in a one-syllable word, the onset is the sound that comes before the vowel, and the rime is the vowel and everything after it, such as c (onset) and at (rime) in cat.',
  [('In the word cat, what is the onset?', ['C', 'At', 'Cat', 'A'], 0),
   ('In the word cat, what is the rime?', ['At', 'C', 'Cat', 'T'], 0),
   ('What does the rime of a word include?', ['The vowel and everything after it', 'Only the first consonant', 'Only punctuation', 'Nothing at all'], 0),
   ('Which word shares the same rime as hat?', ['Bat', 'Hop', 'Sit', 'Run'], 0),
   ('Why is learning onset and rime useful for young readers?', ['It helps readers recognize word families and sound out new words', 'It removes the need to read at all', 'It only applies to silent letters', 'It has no connection to reading'], 0)]),
M('Time: Converting Minutes to Seconds',
  'Grade 2 Math strand: there are sixty seconds in one minute, so to convert minutes to seconds, multiply the number of minutes by sixty.',
  [('How many seconds are in one minute?', ['60', '100', '30', '10'], 0),
   ('How many seconds are in two minutes?', ['120', '60', '90', '20'], 0),
   ('To convert minutes to seconds, what do you do?', ['Multiply the minutes by sixty', 'Divide the minutes by sixty', 'Add ten to the minutes', 'Subtract sixty from the minutes'], 0),
   ('How many seconds are in half a minute?', ['30', '60', '15', '100'], 0),
   ('Which is longer: 90 seconds or one minute?', ['90 seconds', 'One minute', 'They are exactly the same', 'Neither has a length'], 0)]),
Sc('Hummingbirds: The Smallest, Fastest Fliers',
   'Grade 2 Science strand: hummingbirds are tiny birds that beat their wings extremely fast, allowing them to hover in place while sipping nectar from flowers.',
   [('What is special about how fast hummingbirds beat their wings?', ['They beat their wings extremely fast', 'They never move their wings', 'They only flap once per hour', 'Their wings are frozen in place'], 0),
    ('What special flying skill do hummingbirds have?', ['They can hover in place', 'They can only fly backwards', 'They cannot fly at all', 'They can only glide downward'], 0),
    ('What do hummingbirds often drink from flowers?', ['Nectar', 'Saltwater', 'Motor oil', 'Mud'], 0),
    ('Hummingbirds are known for being among the ___ birds.', ['Smallest', 'Largest', 'Slowest', 'Heaviest'], 0),
    ('Why might hovering help a hummingbird while feeding?', ['It lets the bird stay still at a flower to sip nectar', 'Hovering has no benefit to feeding', 'It prevents the bird from ever landing', 'It stops the bird from flying anywhere else'], 0)]),
SS('Search and Rescue: Helping People in Emergencies',
   'Grade 2 Social Studies strand: search and rescue teams in Canada help find and assist people who are lost, injured, or in danger, often in remote areas like mountains, forests, or open water.',
   [('What is the main job of a search and rescue team?', ['To find and assist people who are lost or in danger', 'To deliver mail', 'To teach at a school', 'To sell food at a market'], 0),
    ('In what kinds of areas might search and rescue teams often work?', ['Remote areas like mountains, forests, or open water', 'Only inside a single classroom', 'Only in a grocery store', 'Only in an office building'], 0),
    ('Why is search and rescue an important service?', ['It can help save lives in emergencies', 'It has no real purpose', 'It only happens in stories', 'It replaces the need for hospitals'], 0),
    ('Which of these might a search and rescue team use to find someone?', ['Trained dogs and specialized equipment', 'A cookbook', 'A musical instrument', 'A paintbrush'], 0),
    ('Search and rescue is an example of a ___ service.', ['Community emergency', 'Retail', 'Entertainment', 'Banking'], 0)]),
]),
day(175, [
L('Kennings: Poetic Nicknames for Everyday Things',
  'Grade 2 Language strand: a kenning is a short, two-word poetic nickname that describes something in a creative way, like sky-traveller for a bird or web-spinner for a spider.',
  [('What is a kenning?', ['A short, two-word poetic nickname for something', 'A type of punctuation', 'A silent letter', 'A math equation'], 0),
   ('Which of these is an example of a kenning for a bird?', ['Sky-traveller', 'The blue sky', 'A quiet room', 'A math fact'], 0),
   ('What makes a kenning creative?', ['It describes something in a fresh, imaginative way', 'It always uses the exact same word twice', 'It has no meaning at all', 'It never describes anything'], 0),
   ('Which kenning might describe a spider?', ['Web-spinner', 'Fast-runner', 'Loud-singer', 'Deep-sleeper'], 0),
   ('Why might a poet choose to use kennings in a poem?', ['To add vivid, playful description', 'To remove all imagery from the poem', 'To make the poem impossible to read', 'To avoid describing the subject'], 0)]),
M('Measurement: Comparing Weight with a Balance Scale',
  'Grade 2 Math strand: a balance scale compares the weight of two objects by seeing which side tips lower, showing which object is heavier or if the two objects weigh the same.',
  [('What does a balance scale help you compare?', ['The weight of two objects', 'The colour of two objects', 'The shape of two objects', 'The name of two objects'], 0),
   ('If one side of a balance scale tips lower, what does that side hold?', ['The heavier object', 'The lighter object', 'Nothing at all', 'An object with no weight'], 0),
   ('If both sides of a balance scale stay level, what does that mean?', ['The objects weigh the same', 'One object is much heavier', 'The scale is broken', 'The objects have no weight'], 0),
   ('Which of these could you compare using a balance scale?', ['An apple and an orange', 'The colour red and the colour blue', 'A loud sound and a quiet sound', 'Yesterday and today'], 0),
   ('A balance scale is a tool used to measure ___.', ['Weight', 'Time', 'Temperature', 'Length only'], 0)]),
Sc('Savanna Habitats: Grasslands With Scattered Trees',
   'Grade 2 Science strand: a savanna is a warm grassland habitat with scattered trees and a wet and dry season, home to animals such as lions, elephants, and giraffes.',
   [('What kind of habitat is a savanna?', ['A warm grassland with scattered trees', 'A cold, icy tundra', 'A deep ocean trench', 'An underground cave system'], 0),
    ('What kind of seasons does a savanna typically have?', ['A wet season and a dry season', 'Only snow all year', 'Only rain all year with no dry season', 'No seasons at all'], 0),
    ('Which animal might live in a savanna habitat?', ['A giraffe', 'A polar bear', 'A penguin', 'An arctic fox'], 0),
    ('How is a savanna different from a thick rainforest?', ['A savanna has scattered trees instead of a dense canopy', 'A savanna has no plants at all', 'A savanna is always covered in ice', 'A savanna exists only underwater'], 0),
    ('A savanna is best described as a ___ habitat.', ['Warm, grassy', 'Cold, icy', 'Dark, underground', 'Deep, underwater'], 0)]),
SS('The Northern Lights: A Canadian Natural Wonder',
   'Grade 2 Social Studies strand: the northern lights, also called the aurora borealis, are colourful glowing lights sometimes seen in the night sky in northern Canada.',
   [('What are the northern lights also called?', ['The aurora borealis', 'The southern cross', 'The midnight sun', 'The polar vortex'], 0),
    ('In which part of Canada are the northern lights most often seen?', ['Northern Canada', 'Southern Canada only', 'Only over the ocean', 'Only in cities'], 0),
    ('When are the northern lights typically visible?', ['At night', 'Only at noon', 'Only during a storm', 'Only underwater'], 0),
    ('What do the northern lights look like in the sky?', ['Colourful glowing lights', 'A single grey cloud', 'A bright orange sun', 'A dark empty patch'], 0),
    ('The northern lights are an example of a natural ___.', ['Wonder', 'Building', 'Currency', 'Vehicle'], 0)]),
]),
day(176, [
L('Thank-You Notes: Writing to Show Gratitude',
  'Grade 2 Language strand: a thank-you note is a short piece of writing that expresses gratitude to someone for a gift, kindness, or help they provided.',
  [('What is the purpose of a thank-you note?', ['To express gratitude for a gift, kindness, or help', 'To ask a stranger for money', 'To complain about a problem', 'To share a made-up story'], 0),
   ('Which of these might a thank-you note mention?', ['What the gift or kindness was and why it mattered', 'A list of unrelated math facts', 'The weather forecast for next month', 'A recipe for dinner'], 0),
   ('Why might someone choose to write a thank-you note instead of just saying thanks out loud?', ['A written note can be kept and reread later', 'Writing a note is never appropriate', 'Spoken thanks are always better', 'Notes cannot express gratitude'], 0),
   ('A thank-you note is usually ___ in tone.', ['Warm and appreciative', 'Angry and rude', 'Cold and factual only', 'Silent with no words'], 0),
   ('Which sentence sounds like it belongs in a thank-you note?', ['Thank you for the wonderful book you gave me', 'The capital of Canada is Ottawa', 'Two plus two equals four', 'The weather is cloudy today'], 0)]),
M('Geometry: Points, Lines, Line Segments, and Rays',
  'Grade 2 Math strand: a point is an exact location, a line goes on forever in both directions, a line segment has two endpoints, and a ray starts at one point and goes on forever in one direction.',
  [('What is a point in geometry?', ['An exact location', 'A shape with four sides', 'A curved path', 'A type of angle'], 0),
   ('How far does a line extend?', ['Forever in both directions', 'It stops after a short distance', 'Only one centimetre', 'It has no length at all'], 0),
   ('What makes a line segment different from a line?', ['A line segment has two endpoints', 'A line segment goes on forever', 'A line segment has no length', 'A line segment is always curved'], 0),
   ('What is a ray?', ['A path that starts at one point and goes on forever in one direction', 'A path with two endpoints', 'A single dot with no direction', 'A closed shape'], 0),
   ('Which of these best describes a line segment you might draw with a ruler between two dots?', ['A straight path with a clear start and end', 'A path that never ends', 'A curved circle', 'A single point'], 0)]),
Sc('Solar Eclipses: When the Moon Blocks the Sun',
   'Grade 2 Science strand: a solar eclipse happens when the moon passes between the Earth and the Sun, briefly blocking some or all of the suns light from reaching part of the Earth.',
   [('What happens during a solar eclipse?', ['The moon passes between the Earth and the Sun', 'The sun passes between the Earth and the moon', 'The Earth disappears', 'The moon turns into a star'], 0),
    ('What does a solar eclipse briefly block?', ['Some or all of the suns light', 'All sound on Earth', 'The Earths gravity', 'The ocean tides completely'], 0),
    ('Why should people never look directly at a solar eclipse without proper eye protection?', ['The suns light can seriously harm the eyes', 'Solar eclipses are completely harmless to look at', 'Eclipses make everything invisible', 'There is no reason for caution'], 0),
    ('Which three objects line up during a solar eclipse?', ['The Sun, the moon, and the Earth', 'Two moons and a planet', 'The Earth, a comet, and a star', 'Three different planets'], 0),
    ('A solar eclipse is an example of an event in ___.', ['Space and astronomy', 'Underwater biology', 'Local government', 'Sports history'], 0)]),
SS('Hudson Bay: A Great Canadian Waterway',
   'Grade 2 Social Studies strand: Hudson Bay is a huge body of saltwater in northern Canada, important historically for trade routes and still important today for northern communities and wildlife.',
   [('What kind of body of water is Hudson Bay?', ['A huge saltwater bay', 'A small freshwater pond', 'A narrow river', 'A man-made canal'], 0),
    ('In which part of Canada is Hudson Bay located?', ['Northern Canada', 'Southern Ontario only', 'Outside of Canada', 'Central Africa'], 0),
    ('Why was Hudson Bay historically important?', ['It was important for trade routes', 'It has never been used for anything', 'It was only used for farming', 'It has no history at all'], 0),
    ('Which of these might be found living near Hudson Bay?', ['Northern wildlife and communities', 'Desert cactus plants', 'Tropical rainforest animals', 'Coral reef fish only'], 0),
    ('Hudson Bay is an example of a Canadian ___.', ['Geographic feature', 'Type of government', 'Kind of currency', 'National holiday'], 0)]),
]),
day(177, [
L('Fables: Short Stories With a Moral',
  'Grade 2 Language strand: a fable is a short story, often with animal characters, that teaches a lesson or moral at the end.',
  [('What does a fable usually teach?', ['A lesson or moral', 'A math formula', 'A weather forecast', 'A grocery list'], 0),
   ('What kind of characters often appear in fables?', ['Animals that act like people', 'Only real historical figures', 'Only inanimate objects with no traits', 'No characters at all'], 0),
   ('Where in a fable is the lesson usually found?', ['At the end of the story', 'Only in the title', 'Nowhere, fables have no lesson', 'In the middle only, never at the end'], 0),
   ('Which of these is most like a fable?', ['A story about a slow turtle who wins a race through persistence', 'A weather report for tomorrow', 'A list of math problems', 'A recipe for soup'], 0),
   ('Why might a fable use animal characters instead of people?', ['To make the lesson memorable and easy to picture', 'Animal characters remove all meaning from a story', 'Fables never use characters', 'Animals cannot appear in stories'], 0)]),
M('Time: Reading a Schedule or Timetable',
  'Grade 2 Math strand: a schedule or timetable lists events or departures alongside their times, helping people know when something starts, ends, or arrives.',
  [('What does a schedule or timetable show?', ['Events or departures alongside their times', 'Only colours', 'Only shapes', 'Only names with no times'], 0),
   ('If a bus timetable shows a departure at 3:15, what does that tell you?', ['The exact time the bus is expected to leave', 'The bus never leaves', 'The price of the ticket', 'The colour of the bus'], 0),
   ('Why is it useful to read a schedule before an event?', ['It helps you know when to arrive on time', 'Schedules are never useful', 'It removes the need for clocks', 'It only tells you the weather'], 0),
   ('If a class schedule shows math starts at 9:00 and ends at 9:45, how would you find how long math class lasts?', ['Find the difference between the start and end times', 'Add the two times together', 'Ignore both times', 'Multiply the two times'], 0),
   ('A schedule is especially helpful for ___.', ['Planning and staying on time', 'Drawing pictures', 'Cooking a meal', 'Playing a video game'], 0)]),
Sc('Pulleys: Lifting Loads with a Wheel and Rope',
   'Grade 2 Science strand: a pulley is a simple machine made of a wheel and a rope or chain that changes the direction of a pulling force, making it easier to lift heavy loads.',
   [('What is a pulley made of?', ['A wheel and a rope or chain', 'Only a flat board', 'Only a wedge-shaped block', 'A screw with no wheel'], 0),
    ('What does a pulley help change?', ['The direction of a pulling force', 'The colour of an object', 'The temperature of an object', 'The sound an object makes'], 0),
    ('How does a pulley make lifting easier?', ['It lets you pull down to lift something up', 'It removes the need for any force', 'It makes objects lighter by magic', 'It has no effect on lifting'], 0),
    ('Where might you see a pulley used in real life?', ['On a flagpole to raise a flag', 'Inside a refrigerator', 'On a bicycle seat', 'Inside a pencil'], 0),
    ('A pulley is an example of a ___.', ['Simple machine', 'Living thing', 'Type of weather', 'Kind of food'], 0)]),
SS('The Rocky Mountains: Canadas Mountain Range',
   'Grade 2 Social Studies strand: the Rocky Mountains are a large mountain range in western Canada, known for tall snow-capped peaks, national parks, and diverse wildlife.',
   [('In which part of Canada are the Rocky Mountains located?', ['Western Canada', 'Eastern Canada', 'Northern Canada only', 'Outside of Canada'], 0),
    ('What are the Rocky Mountains known for?', ['Tall, snow-capped peaks', 'Flat, sandy deserts', 'Deep ocean trenches', 'Wide, flat prairies with no hills'], 0),
    ('What can often be found within the Rocky Mountains?', ['National parks and diverse wildlife', 'Large cities with no nature', 'Coral reefs', 'Tropical rainforests'], 0),
    ('A mountain range is best described as ___.', ['A large connected group of mountains', 'A single small hill', 'A type of ocean current', 'A kind of cloud'], 0),
    ('The Rocky Mountains are an example of a Canadian ___.', ['Geographic landform', 'Type of government', 'National holiday', 'Kind of currency'], 0)]),
]),
day(178, [
L('Diamante Poems: Poems Shaped Like a Diamond',
  'Grade 2 Language strand: a diamante poem is a seven-line poem shaped like a diamond that often contrasts two opposite ideas, using a set pattern of nouns, adjectives, and verbs.',
  [('What shape does a diamante poem form on the page?', ['A diamond', 'A circle', 'A straight line', 'A square'], 0),
   ('How many lines does a diamante poem usually have?', ['Seven', 'Two', 'Twenty', 'One'], 0),
   ('What do diamante poems often contrast?', ['Two opposite ideas', 'A single unrelated fact', 'Nothing at all', 'A list of numbers'], 0),
   ('Which types of words are used to build a diamante poem?', ['Nouns, adjectives, and verbs in a set pattern', 'Only punctuation marks', 'Only silent letters', 'Only numbers'], 0),
   ('Why might a poet choose the diamante form to write about day and night?', ['The shape and structure suit comparing two opposites', 'Diamante poems cannot compare anything', 'The form only works for one single idea', 'It removes all meaning from the poem'], 0)]),
M('Number Sense: Skip Counting by 6s, 7s, 8s, and 9s',
  'Grade 2 Math strand: skip counting means counting forward by a number other than one, and skip counting by 6s, 7s, 8s, or 9s helps build a foundation for multiplication facts.',
  [('What does skip counting mean?', ['Counting forward by a number other than one', 'Counting only to ten', 'Counting backward only', 'Counting with no pattern at all'], 0),
   ('If you skip count by 6s starting at 6, what comes next: 6, 12, 18, ___?', ['24', '20', '22', '30'], 0),
   ('If you skip count by 7s starting at 7, what comes next: 7, 14, 21, ___?', ['28', '27', '30', '25'], 0),
   ('If you skip count by 9s starting at 9, what comes next: 9, 18, 27, ___?', ['36', '35', '30', '40'], 0),
   ('Why is skip counting by 6s, 7s, 8s, and 9s a useful skill?', ['It helps build a foundation for multiplication facts', 'It has no connection to multiplication', 'It only works with even numbers', 'It replaces the need for addition'], 0)]),
Sc('Frogs and Toads: Spotting the Differences',
   'Grade 2 Science strand: frogs and toads are both amphibians, but frogs usually have smooth, moist skin and long legs for jumping, while toads usually have dry, bumpy skin and shorter legs for hopping.',
   [('What type of animal are both frogs and toads?', ['Amphibians', 'Reptiles', 'Mammals', 'Birds'], 0),
    ('What kind of skin does a frog usually have?', ['Smooth and moist', 'Dry and bumpy', 'Covered in fur', 'Covered in feathers'], 0),
    ('What kind of skin does a toad usually have?', ['Dry and bumpy', 'Smooth and moist', 'Covered in scales like a fish', 'Covered in feathers'], 0),
    ('Why are frogs known for jumping long distances?', ['They usually have longer legs suited for jumping', 'They have no legs at all', 'They have wings instead of legs', 'Frogs cannot move at all'], 0),
    ('Frogs and toads are often found near ___.', ['Water and moist areas', 'Deep deserts only', 'The tops of tall mountains only', 'Frozen glaciers only'], 0)]),
SS('Canadian Border Crossings: Moving Between Countries',
   'Grade 2 Social Studies strand: a border crossing is an official place where people and goods travel between two countries, often with officers who check documents like passports.',
   [('What is a border crossing?', ['An official place where people and goods travel between countries', 'A type of school', 'A kind of holiday', 'A local park'], 0),
    ('What might officers check for at a border crossing?', ['Documents like passports', 'Only shoe size', 'Only favourite colour', 'Only birthday cake flavour'], 0),
    ('What can travel through a border crossing besides people?', ['Goods and products', 'Only sound waves', 'Nothing else at all', 'Only weather'], 0),
    ('Why are border crossings important for countries?', ['They help control and monitor who and what enters a country', 'They have no purpose at all', 'They only exist to slow down traffic for no reason', 'They prevent all travel completely'], 0),
    ('A border crossing is found at the ___ between two countries.', ['Boundary', 'Centre of a city', 'Middle of the ocean with no land', 'Top of a mountain only'], 0)]),
]),
day(179, [
L('Trigraphs: The Sounds of tch and dge',
  'Grade 2 Language strand: a trigraph is three letters that work together to make one sound, such as tch in catch and dge in bridge.',
  [('What is a trigraph?', ['Three letters that work together to make one sound', 'A single silent letter', 'A whole sentence', 'A punctuation mark'], 0),
   ('Which trigraph is found in the word catch?', ['Tch', 'Dge', 'Sh', 'Ch'], 0),
   ('Which trigraph is found in the word bridge?', ['Dge', 'Tch', 'Th', 'Wh'], 0),
   ('Which of these words contains the tch trigraph?', ['Watch', 'Bridge', 'Ship', 'Chip'], 0),
   ('Why might tch and dge be tricky for young readers?', ['Three letters combine to make a single sound', 'They are always silent and make no sound', 'They only appear in numbers', 'They never appear in real words'], 0)]),
M('Data: Sorting Objects with a Carroll Diagram',
  'Grade 2 Math strand: a Carroll diagram sorts objects into a grid based on two different attributes, showing whether each object does or does not have each attribute.',
  [('What does a Carroll diagram help you do?', ['Sort objects by two different attributes', 'Measure the weight of an object', 'Tell the exact time', 'Count money only'], 0),
   ('How is a Carroll diagram organized?', ['As a grid based on attributes', 'As a single circle', 'As a straight line with no sections', 'As a list of random numbers'], 0),
   ('If sorting shapes by colour and by number of sides, what could a Carroll diagram show?', ['Which shapes are red with four sides and which are not', 'Only the shapes names', 'Only the price of each shape', 'Nothing useful at all'], 0),
   ('A Carroll diagram is most similar to which other sorting tool?', ['A Venn diagram', 'A number line', 'A clock face', 'A ruler'], 0),
   ('Why might a Carroll diagram be useful in math class?', ['It helps organize and compare data by attributes', 'It has no real use in math', 'It only works with letters, never numbers or shapes', 'It replaces the need for counting'], 0)]),
Sc('Wedges and Screws: Simple Machines That Cut and Hold',
   'Grade 2 Science strand: a wedge is a simple machine shaped like a triangle used to cut or split things apart, and a screw is a simple machine made of an inclined plane wrapped around a pole, used to hold things together.',
   [('What shape is a wedge?', ['A triangle', 'A perfect circle', 'A flat rectangle', 'A wavy line'], 0),
    ('What is a wedge often used for?', ['Cutting or splitting things apart', 'Measuring temperature', 'Telling time', 'Holding water'], 0),
    ('What simple machine is wrapped around a pole to make a screw?', ['An inclined plane', 'A lever', 'A pulley', 'A wheel and axle'], 0),
    ('What is a screw often used for?', ['Holding things together', 'Cutting food', 'Measuring distance', 'Producing light'], 0),
    ('Wedges and screws are both examples of ___.', ['Simple machines', 'Living things', 'Weather events', 'Musical instruments'], 0)]),
SS('The Royal Canadian Mint: Where Our Coins Are Made',
   'Grade 2 Social Studies strand: the Royal Canadian Mint is the organization responsible for producing all of Canadas coins, using metal, machines, and careful designs.',
   [('What does the Royal Canadian Mint produce?', ['Canadas coins', 'Canadas paper bills', 'Canadas stamps', 'Canadas passports'], 0),
    ('What materials are used to make coins at the mint?', ['Metal', 'Paper', 'Wood', 'Fabric'], 0),
    ('Why might careful designs matter when making coins?', ['To make coins recognizable and hard to copy', 'Designs have no importance for coins', 'Coins are never designed at all', 'Only the weight of a coin matters'], 0),
    ('The word mint, in this context, refers to a place that ___.', ['Manufactures official coins', 'Grows plants for food', 'Repairs vehicles', 'Publishes newspapers'], 0),
    ('The Royal Canadian Mint is an example of a national ___.', ['Institution', 'Sports team', 'Holiday', 'Weather pattern'], 0)]),
]),
day(180, [
L('Language Review: Poetic Forms, Reflexive Pronouns, and Story Genres',
  'Grade 2 Language strand review: students revisit limericks, reflexive pronouns, tall tales, onset and rime, kennings, thank-you notes, fables, diamante poems, and the tch/dge trigraphs.',
  [('How many lines does a limerick have?', ['Five', 'Three', 'Ten', 'One'], 0),
   ('What does a reflexive pronoun do?', ['Refers back to the subject of the sentence', 'Asks a question', 'Names a place', 'Shows an action only'], 0),
   ('What makes a tall tale different from a realistic story?', ['It features exaggerated, impossible feats', 'It only describes true daily events', 'It has no characters at all', 'It is always written as a list'], 0),
   ('What is a kenning?', ['A short, two-word poetic nickname for something', 'A type of punctuation', 'A silent letter', 'A math equation'], 0),
   ('What does a fable usually teach?', ['A lesson or moral', 'A math formula', 'A weather forecast', 'A grocery list'], 0)]),
M('Math Review: Fractions, Money, Time, Geometry, and Data',
  'Grade 2 Math strand review: students revisit subtracting fractions with the same denominator, circle graphs, Canadian paper bills, converting minutes to seconds, points and lines, reading a schedule, skip counting by 6s to 9s, and Carroll diagrams.',
  [('When subtracting fractions with the same denominator, what stays the same?', ['The denominator', 'The numerator', 'Both numbers change', 'Nothing stays the same'], 0),
   ('What does each slice of a circle graph represent?', ['A part of the whole amount', 'A separate unrelated topic', 'The title of the graph', 'A single dot of data'], 0),
   ('How many seconds are in one minute?', ['60', '100', '30', '10'], 0),
   ('What is a ray?', ['A path that starts at one point and goes on forever in one direction', 'A path with two endpoints', 'A single dot with no direction', 'A closed shape'], 0),
   ('What does a Carroll diagram help you do?', ['Sort objects by two different attributes', 'Measure the weight of an object', 'Tell the exact time', 'Count money only'], 0)]),
Sc('Science Review: Animals, Habitats, Space, and Simple Machines',
   'Grade 2 Science strand review: students revisit chameleons, kangaroos, jellyfish, hummingbirds, savanna habitats, solar eclipses, pulleys, frogs and toads, and wedges and screws.',
   [('What are chameleons best known for?', ['Changing colour', 'Flying through the air', 'Living underwater only', 'Building large nests'], 0),
    ('What is a marsupial?', ['An animal that carries its young in a pouch', 'An animal that lives only underwater', 'An animal with no legs', 'An animal that never moves'], 0),
    ('What kind of habitat is a savanna?', ['A warm grassland with scattered trees', 'A cold, icy tundra', 'A deep ocean trench', 'An underground cave system'], 0),
    ('What happens during a solar eclipse?', ['The moon passes between the Earth and the Sun', 'The sun passes between the Earth and the moon', 'The Earth disappears', 'The moon turns into a star'], 0),
    ('What does a pulley help change?', ['The direction of a pulling force', 'The colour of an object', 'The temperature of an object', 'The sound an object makes'], 0)]),
SS('Social Studies Review: Parliament, Geography, and National Institutions',
   'Grade 2 Social Studies strand review: students revisit the House of Commons, the Canadian passport, National Indigenous Peoples Day, search and rescue, the northern lights, Hudson Bay, the Rocky Mountains, border crossings, and the Royal Canadian Mint.',
   [('What is the House of Commons?', ['The part of Parliament where MPs debate and vote on laws', 'A type of school', 'A local library', 'A sports arena'], 0),
    ('What is a Canadian passport?', ['An official document proving citizenship and identity', 'A type of currency', 'A kind of map', 'A school report card'], 0),
    ('On what date is National Indigenous Peoples Day celebrated?', ['June 21', 'January 1', 'July 1', 'December 25'], 0),
    ('What are the northern lights also called?', ['The aurora borealis', 'The southern cross', 'The midnight sun', 'The polar vortex'], 0),
    ('What does the Royal Canadian Mint produce?', ['Canadas coins', 'Canadas paper bills', 'Canadas stamps', 'Canadas passports'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g2_171_180)
    append_to(2, g2_171_180)
