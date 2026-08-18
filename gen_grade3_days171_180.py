#!/usr/bin/env python3
"""Grade 3, Days 171-180 -- extends Grade 3 from 170 to 180 days. Modeled
exactly on gen_grade3_days161_170.py: same L/M/Sc/SS helpers over
gen_curriculums sub()/day()/append_to(), same TVO Learn placeholder
resourceLabel/resourceUrl convention (videoUrl intentionally left unset,
filled in later by the daily curriculum-video-backfill scheduled task),
and the same title convention used throughout Grade 3 of a category
prefix baked into the title itself (Grammar:, Vocabulary:, Reading:,
Writing:, Oral Communication: for Language; Science: for Science; Social
Studies: for SocialStudies).

Topics chosen to avoid any overlap with the existing Grade 3 Days 1-170
topics (see data/grade3.json), which already densely cover nearly the
entire grade 3 Ontario curriculum many times over. Every (subject, title)
pair below was checked against a full dump of Days 1-170 (all subject/
title pairs printed and reviewed) and confirmed to be new. New topics for
this batch: common and proper nouns, using hyphens in compound
adjectives, idioms about weather, distinguishing first-person and
third-person narration, identifying the climax of a story, writing a set
of directions for a treasure hunt, using ellipses to show a pause or
omission, writing an advertisement script for the radio, and words with
silent letters for Language; comparing numbers using greater than, less
than, and equal to symbols, using a number line to multiply, dividing
with arrays, naming and writing fractions in words, tessellations and
tiling patterns, introducing the kilometre for long distances, comparing
two data sets side by side, identifying errors in a pattern, and
splitting a bill fairly among friends for Math; beavers and how they
build dams, moose, polar bears, jellyfish, crustaceans (crabs, lobsters,
shrimp), the life cycle of a mosquito, monarch butterfly migration, how
icicles and frost form, and how skyscrapers withstand wind for Science;
and the Order of Canada, the Parliament Buildings and Peace Tower, how
Ottawa became the capital, the Confederation Bridge, school crossing
guards, grain elevators and the Prairie wheat economy, lighthouse
keepers, the role of a translator, and the Canadian Snowbirds for Social
Studies -- none of those exact ideas appear in Days 1-170. Day 180 is a
review day across all four subjects, matching the end-of-batch pattern
used in every prior 10-day batch, with review titles written to be
textually distinct from every earlier review days title (e.g. Day 160s
and Day 170s). No embedded ASCII double-quote or straight apostrophe
characters are used anywhere in title/summary/question/option text;
apostrophes are dropped entirely (e.g. Canadas instead of Canada with an
apostrophe s), matching the convention established in Days 111-170.

Invocation (matches the 161-170 script):
  cd ~/gradesbooster && python3 gen_grade3_days171_180.py
followed by:
  cd ~/gradesbooster && python3 build_json.py --grade 3
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_curriculum import sub, day, append_to

L3 = 'https://tvolearn.com/pages/grade-3-language'
M3 = 'https://tvolearn.com/pages/grade-3-mathematics'
S3 = 'https://tvolearn.com/pages/grade-3-science-and-technology'
SS3 = 'https://tvolearn.com/pages/grade-3-social-studies'
RL, RM, RS, RSS = (
    'TVO Learn: Grade 3 Language',
    'TVO Learn: Grade 3 Mathematics',
    'TVO Learn: Grade 3 Science and Technology',
    'TVO Learn: Grade 3 Social Studies',
)


def L(t, s, q):
    return sub('Language', t, s, RL, L3, q)


def M(t, s, q):
    return sub('Math', t, s, RM, M3, q)


def Sc(t, s, q):
    return sub('Science', t, s, RS, S3, q)


def SS(t, s, q):
    return sub('SocialStudies', t, s, RSS, SS3, q)


def _rebalance_answer_positions(days, seed=20260818):
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


g3_171_180 = [
day(171, [
L('Grammar: Common and Proper Nouns',
  'Grade 3 Language strand: a common noun names a general person, place, or thing, while a proper noun names a specific person, place, or thing and begins with a capital letter.',
  [('What is a common noun?', ['A general person, place, or thing', 'A word that is always capitalized', 'A word that describes an action', 'A word used only in questions'], 0),
   ('What is a proper noun?', ['A specific person, place, or thing that begins with a capital letter', 'A word with no capital letter ever', 'A word that only appears in math', 'A type of punctuation mark'], 0),
   ('Which of these is a proper noun?', ['Toronto', 'city', 'river', 'school'], 0),
   ('Which of these is a common noun?', ['school', 'Canada', 'Toronto', 'Ontario'], 0),
   ('Why do proper nouns begin with a capital letter?', ['To show that they name something specific', 'Because all words begin with capital letters', 'To make the sentence longer', 'Because proper nouns are always plural'], 0)]),
M('Number: Comparing Numbers Using Greater Than, Less Than, and Equal To Symbols',
  'Grade 3 Math strand: the symbols greater than, less than, and equal to are used to compare two numbers and show their relationship.',
  [('What does the greater than symbol mean?', ['Greater than', 'Less than', 'Equal to', 'Not equal to'], 0),
   ('What does the less than symbol mean?', ['Less than', 'Greater than', 'Equal to', 'Plus'], 0),
   ('Which comparison correctly compares 45 and 54?', ['45 is less than 54', '45 is greater than 54', '45 is equal to 54', '45 plus 54'], 0),
   ('Which symbol would you use to compare 100 and 100?', ['Equal to', 'Greater than', 'Less than', 'Plus'], 0),
   ('Why are comparison symbols useful in math?', ['They quickly show how two numbers relate to each other', 'They replace the need for numbers entirely', 'They only work with fractions', 'They are used only in geometry'], 0)]),
Sc('Science: Beavers and How They Build Dams',
   'Grade 3 Science strand: beavers are large rodents that use their strong teeth to cut down trees and branches, building dams and lodges that change the flow of water in a habitat.',
   [('What do beavers use to cut down trees?', ['Their strong teeth', 'Their tail only', 'Their claws only', 'Tools they build'], 0),
    ('What do beavers build using trees and branches?', ['Dams and lodges', 'Nests high in trees', 'Underground tunnels only', 'Sandcastles'], 0),
    ('How can a beaver dam change a habitat?', ['It can change the flow of water and create a pond', 'It has no effect on the habitat at all', 'It stops all water from moving forever', 'It removes water from the habitat completely'], 0),
    ('What kind of animal is a beaver?', ['A large rodent', 'A reptile', 'A bird', 'An insect'], 0),
    ('Why might a beaver build a lodge?', ['To create a safe shelter to live in', 'To store food for other animals only', 'To block sunlight from the forest', 'To attract predators'], 0)]),
SS('Social Studies: The Order of Canada and Honouring Citizens Who Make a Difference',
   'Grade 3 Social Studies strand: the Order of Canada is one of the countrys highest honours, given to citizens who have made an outstanding difference in their community or country.',
   [('What is the Order of Canada?', ['One of the countrys highest honours for citizens', 'A type of Canadian currency', 'A law passed by Parliament', 'A holiday celebrated every year'], 0),
    ('Who might receive the Order of Canada?', ['A citizen who has made an outstanding difference in their community or country', 'Only people who work in government', 'Only professional athletes', 'Only people born outside Canada'], 0),
    ('Why might a country create an honour like the Order of Canada?', ['To recognize and celebrate the achievements of its citizens', 'To punish citizens for breaking rules', 'To replace the need for elections', 'Because honours have no purpose'], 0),
    ('What kind of contributions might be honoured by the Order of Canada?', ['Contributions to science, the arts, or community service', 'Only contributions to a single sport', 'Only contributions made by children', 'Only contributions made in one city'], 0),
    ('Why is it meaningful for a community when one of its members receives a national honour?', ['It celebrates the positive impact that person has had on others', 'It has no meaning to the community at all', 'It means the community must move away', 'It replaces the need for local government'], 0)]),
]),
day(172, [
L('Grammar: Using Hyphens in Compound Adjectives',
  'Grade 3 Language strand: a hyphen can join two or more words to form a compound adjective that describes a noun, such as a well-known author or a five-year-old child.',
  [('What does a hyphen do in a compound adjective?', ['Joins two or more words together to describe a noun', 'Ends a sentence', 'Separates a paragraph into two parts', 'Replaces a comma in a list'], 0),
   ('Which is an example of a compound adjective using a hyphen?', ['A well-known author', 'A book that is known', 'An author who writes books', 'A famous library'], 0),
   ('In the phrase a five-year-old child, what does the hyphenated phrase describe?', ['The age of the child', 'The colour of the child', 'The location of the child', 'The name of the child'], 0),
   ('Why might a writer use a hyphen to join words before a noun?', ['To show that the words work together as a single description', 'To make the sentence impossible to read', 'To remove the noun from the sentence', 'Hyphens are never used before nouns'], 0),
   ('Which sentence correctly uses a hyphenated compound adjective?', ['She read a well-written story.', 'She read a well written story that.', 'She read a, well known story.', 'She read a wellknown story'], 0)]),
M('Multiplication: Using a Number Line to Multiply',
  'Grade 3 Math strand: a number line can be used to multiply by drawing equal jumps, where the size and number of jumps represent the factors being multiplied.',
  [('On a number line, what does each equal jump represent when multiplying?', ['One group being counted', 'A subtraction step', 'A fraction of the whole', 'The remainder of the problem'], 0),
   ('To show 4 times 3 on a number line, how many jumps of 3 would you make?', ['4 jumps', '3 jumps', '7 jumps', '12 jumps'], 0),
   ('Where does a multiplication number line usually start?', ['At zero', 'At the largest factor', 'At the product', 'At the smallest possible number'], 0),
   ('What number does the number line land on after showing 5 times 2?', ['10', '7', '5', '2'], 0),
   ('Why might a number line help a student understand multiplication?', ['It shows multiplication as repeated equal jumps', 'It removes the need to know multiplication facts', 'It only works for division problems', 'It replaces the need for numbers'], 0)]),
Sc('Science: Moose and Canadas Largest Deer Species',
   'Grade 3 Science strand: the moose is the largest member of the deer family, with long legs, a large body, and antlers on males that help it survive in Canadian forests and wetlands.',
   [('What family of animals does the moose belong to?', ['The deer family', 'The bear family', 'The cat family', 'The bird family'], 0),
    ('Which body part do male moose grow to help them survive?', ['Antlers', 'Wings', 'Gills', 'A shell'], 0),
    ('Where might a moose commonly be found in Canada?', ['Forests and wetlands', 'Deserts', 'Ocean coral reefs', 'City sidewalks'], 0),
    ('How does the moose compare in size to other deer species?', ['It is the largest member of the deer family', 'It is the smallest member of the deer family', 'It is not related to other deer at all', 'It is exactly the same size as all deer'], 0),
    ('Why might long legs help a moose in its wetland habitat?', ['They help it wade through deep water and mud', 'They prevent it from ever entering water', 'They make it unable to walk on land', 'They have no purpose for the moose'], 0)]),
SS('Social Studies: The Parliament Buildings and the Peace Tower in Ottawa',
   'Grade 3 Social Studies strand: the Parliament Buildings in Ottawa, topped by the Peace Tower, are where Canadas federal government meets and are one of the countrys most recognized landmarks.',
   [('In which city are the Parliament Buildings located?', ['Ottawa', 'Toronto', 'Vancouver', 'Montreal'], 0),
    ('What tower is part of the Parliament Buildings?', ['The Peace Tower', 'The CN Tower', 'The Water Tower', 'The Clock Tower of Toronto'], 0),
    ('What happens inside the Parliament Buildings?', ['Canadas federal government meets and makes decisions', 'Local groceries are sold', 'Provincial sports games are played', 'Mail is sorted for the whole country'], 0),
    ('Why are the Parliament Buildings considered an important landmark?', ['They are a recognized symbol of Canadas federal government', 'They have no connection to government at all', 'They are used only for storage', 'They are located outside of Canada'], 0),
    ('What might visitors see when they visit the Parliament Buildings?', ['Historic architecture and the Peace Tower', 'A large shopping mall', 'A private farm', 'An empty field with no buildings'], 0)]),
]),
day(173, [
L('Vocabulary: Idioms About Weather',
  'Grade 3 Language strand: idioms about weather, such as it is raining cats and dogs or under the weather, use weather words to express an idea that is different from their literal meaning.',
  [('What does the idiom it is raining cats and dogs mean?', ['It is raining very heavily', 'Animals are falling from the sky', 'The weather is sunny and clear', 'It is snowing lightly'], 0),
   ('What does the idiom under the weather usually mean?', ['Feeling sick or unwell', 'Standing outside in the rain', 'Feeling extremely happy', 'Wearing a raincoat'], 0),
   ('Do weather idioms usually mean exactly what their words say?', ['No, they mean something different from their literal words', 'Yes, they always describe real weather', 'Weather idioms have no meaning at all', 'They are only used in science reports'], 0),
   ('Why might a reader need to think carefully about a weather idiom?', ['Because its meaning is different from what the words literally say', 'Because idioms are always about the weather forecast', 'Because idioms only appear in poetry', 'Because idioms are always confusing with no meaning'], 0),
   ('Which is an example of a weather idiom?', ['Steal someones thunder', 'Open the door', 'Read a book', 'Walk to school'], 0)]),
M('Division: Dividing with Arrays',
  'Grade 3 Math strand: an array of rows and columns can be used to model division by showing how a total number of objects can be split evenly into equal groups.',
  [('What does an array show when used to model division?', ['How a total can be split evenly into equal groups', 'A single random number', 'Only multiplication facts', 'A list of fractions'], 0),
   ('If 12 objects are arranged into an array with 3 rows, how many objects are in each row?', ['4', '3', '6', '12'], 0),
   ('What do the rows in a division array usually represent?', ['The equal groups being made', 'The remainder of the problem', 'The total number of objects only', 'A random arrangement with no meaning'], 0),
   ('If 20 objects are divided into an array with 4 equal rows, how many objects are in each row?', ['5', '4', '10', '20'], 0),
   ('Why might an array help someone understand a division problem?', ['It visually shows equal groups being formed from a total', 'It removes the need to divide at all', 'It only works with multiplication, never division', 'It hides the total number of objects'], 0)]),
Sc('Science: Polar Bears and Life on Arctic Sea Ice',
   'Grade 3 Science strand: polar bears have thick fur, a layer of fat, and large paws that help them survive and hunt on the cold sea ice of the Arctic.',
   [('What helps keep a polar bear warm in the Arctic?', ['Thick fur and a layer of fat', 'A thin coat of feathers', 'A shell covering its body', 'Scales like a fish'], 0),
    ('What do polar bears use their large paws for?', ['Walking on ice and swimming', 'Flying short distances', 'Digging deep underground tunnels', 'Climbing tall trees'], 0),
    ('Where do polar bears mainly live and hunt?', ['On Arctic sea ice', 'In hot deserts', 'In tropical rainforests', 'In deep ocean trenches'], 0),
    ('Why is sea ice important to a polar bears way of life?', ['It provides a place to hunt for food, such as seals', 'It has no connection to how polar bears find food', 'Sea ice prevents polar bears from ever hunting', 'Polar bears never go near sea ice'], 0),
    ('What colour is a polar bears fur, and why might that help it?', ['White, which helps it blend into the snow and ice', 'Bright orange, which helps it stand out', 'Green, which helps it hide in forests', 'Black, which helps it hide in caves'], 0)]),
SS('Social Studies: How Ottawa Became Canadas Capital City',
   'Grade 3 Social Studies strand: Ottawa was chosen as Canadas capital city partly because of its location between English and French speaking regions, and it is now where the federal government is based.',
   [('What is Ottawa known as?', ['Canadas capital city', 'A small fishing village', 'A province of Canada', 'A neighbouring country'], 0),
    ('Why was Ottawas location considered helpful when it was chosen as the capital?', ['It sits between English and French speaking regions', 'It is located outside of Canada', 'It has no connection to any region', 'It is the smallest town in Canada'], 0),
    ('What is based in Ottawa today?', ['The federal government', 'A single small business', 'A provincial park only', 'A private farm'], 0),
    ('Why do countries usually choose one city to be their capital?', ['To have a central place where the government meets and makes decisions', 'Because capitals have no real purpose', 'To prevent the government from ever meeting', 'Because every city must be a capital'], 0),
    ('What might visitors find in Canadas capital city?', ['Government buildings and national landmarks', 'Only farmland with no buildings', 'A capital with no government activity', 'A city with no visitors allowed'], 0)]),
]),
day(174, [
L('Reading: Distinguishing First-Person and Third-Person Narration',
  'Grade 3 Language strand: a story told in first person uses words like I and we from a character inside the story, while a story told in third person uses words like he, she, and they to describe characters from outside the story.',
  [('Which pronoun signals that a story is told in first person?', ['I', 'He', 'They', 'She'], 0),
   ('Which pronoun signals that a story is told in third person?', ['She', 'I', 'We', 'My'], 0),
   ('In first-person narration, who is telling the story?', ['A character inside the story', 'A narrator with no connection to the story', 'No one is telling the story', 'A character who never appears'], 0),
   ('In third-person narration, how does the narrator usually describe characters?', ['From outside the story, using words like he, she, and they', 'Only using the word I', 'Only using numbers', 'The narrator never describes characters'], 0),
   ('Why might an author choose first-person narration for a story?', ['To let readers experience the story through one characters thoughts and feelings', 'To remove all characters from the story', 'Because first person can never be used in fiction', 'To make the story impossible to understand'], 0)]),
M('Fractions: Naming and Writing Fractions in Words',
  'Grade 3 Math strand: fractions can be written in words as well as numbers, such as writing three quarters as three-fourths, using the numerator as a number word and the denominator as a fraction word.',
  [('How would you write three quarters using words?', ['Three-fourths', 'Three-fours', 'Fourth-threes', 'Three over four only'], 0),
   ('How would you write one half using words?', ['One-half', 'One-second', 'Half-one', 'Two-ones'], 0),
   ('In the fraction two fifths, which number is used as a number word and which becomes a fraction word?', ['The numerator (2) is a number word and the denominator (5) becomes fifths', 'The denominator is always ignored', 'Both numbers are always written the same way', 'Neither number is written as a word'], 0),
   ('How would you write five sixths using words?', ['Five-sixths', 'Five-sixes', 'Sixth-fives', 'Five over six only'], 0),
   ('Why might writing fractions in words be a useful skill?', ['It helps connect the symbols of a fraction to its meaning in everyday language', 'It removes the need to ever use fraction symbols', 'It only works for fractions equal to one', 'It has no connection to understanding fractions'], 0)]),
Sc('Science: Jellyfish and Their Stinging Cells',
   'Grade 3 Science strand: jellyfish are simple ocean animals with soft, see-through bodies and tentacles lined with stinging cells that they use to catch food and defend themselves.',
   [('What do jellyfish use their tentacles for?', ['Catching food and defending themselves using stinging cells', 'Digging burrows in the sand', 'Building nests on the ocean floor', 'Flying above the water'], 0),
    ('What kind of body does a jellyfish have?', ['A soft, see-through body', 'A hard shell like a crab', 'A body covered in fur', 'A body covered in feathers'], 0),
    ('What are the stinging parts of a jellyfish called?', ['Stinging cells on its tentacles', 'Teeth in its mouth', 'Claws on its body', 'Spikes on its back'], 0),
    ('Where do jellyfish live?', ['In oceans around the world', 'Only in freshwater lakes', 'Only in deserts', 'Only underground'], 0),
    ('Why might a jellyfish see-through body be helpful in the ocean?', ['It can help the jellyfish blend in and avoid predators', 'It makes the jellyfish impossible to see for other jellyfish', 'It has no connection to survival', 'It prevents the jellyfish from ever moving'], 0)]),
SS('Social Studies: The Confederation Bridge Connecting Prince Edward Island',
   'Grade 3 Social Studies strand: the Confederation Bridge is a long bridge that connects Prince Edward Island to the rest of Canada, allowing cars and trucks to cross the water instead of relying only on a ferry.',
   [('What does the Confederation Bridge connect?', ['Prince Edward Island to the rest of Canada', 'Ontario to Quebec', 'British Columbia to Alberta', 'Two cities within the same province'], 0),
    ('What can cross the Confederation Bridge?', ['Cars and trucks', 'Only bicycles', 'Only pedestrians', 'Nothing is allowed to cross'], 0),
    ('What method of travel did people rely on more before the bridge was built?', ['A ferry', 'An airplane only', 'A train only', 'A hot air balloon'], 0),
    ('Why might a bridge like this be helpful to Prince Edward Island?', ['It provides a reliable way to travel to and from the mainland', 'It prevents anyone from ever leaving the island', 'It has no benefit to the island', 'It replaces the need for the island to have roads'], 0),
    ('What kind of structure is the Confederation Bridge?', ['A long bridge crossing open water', 'A short bridge crossing a small stream', 'A tunnel under a mountain', 'A dirt path through a forest'], 0)]),
]),
day(175, [
L('Writing: Writing a Set of Directions for a Treasure Hunt',
  'Grade 3 Language strand: directions for a treasure hunt use clear, ordered steps and location words to guide someone from a starting point to a hidden object.',
  [('What should directions for a treasure hunt include?', ['Clear, ordered steps and location words', 'A list of unrelated facts', 'A single confusing sentence', 'No information about location at all'], 0),
   ('Why is the order of steps important in treasure hunt directions?', ['Following the wrong order could lead the person to the wrong place', 'The order never matters in directions', 'Steps are always identical to each other', 'Directions never need to be in order'], 0),
   ('Which is an example of a location word used in directions?', ['Behind', 'Quickly', 'Happily', 'Loudly'], 0),
   ('What is the purpose of writing a treasure hunt starting point?', ['So the person knows exactly where to begin following the directions', 'So the person never begins the hunt', 'To confuse the person following the directions', 'Starting points are never included in directions'], 0),
   ('Why might numbering the steps of a treasure hunt be helpful?', ['It shows the exact order the steps should be followed', 'It makes the directions impossible to follow', 'It removes the need for clear steps', 'Numbers are never used in directions'], 0)]),
M('Geometry: Tessellations and Tiling Patterns',
  'Grade 3 Math strand: a tessellation is a pattern made of shapes that fit together perfectly with no gaps or overlaps, covering a surface completely, such as tiles on a floor.',
  [('What is a tessellation?', ['A pattern of shapes that fit together with no gaps or overlaps', 'A single shape drawn alone', 'A pattern with large gaps between shapes', 'A shape that never repeats'], 0),
   ('Which shape is commonly used to create a simple tessellation?', ['A square', 'A shape with no straight sides', 'A shape that changes size every time', 'A shape that cannot be repeated'], 0),
   ('Where might you see a tessellation in everyday life?', ['Tiles covering a floor', 'A single cloud in the sky', 'A drawing with only one shape', 'An empty piece of paper'], 0),
   ('What happens to the shapes in a tessellation when they are placed together?', ['They cover a surface completely with no gaps or overlaps', 'They leave large empty spaces', 'They overlap on top of each other', 'They disappear when placed together'], 0),
   ('Why might an artist or builder use a tessellation pattern?', ['To cover a surface evenly using a repeating design', 'To leave most of the surface uncovered', 'To use only one single shape with no pattern', 'Tessellations are never used by artists or builders'], 0)]),
Sc('Science: Crustaceans — Crabs, Lobsters, and Shrimp',
   'Grade 3 Science strand: crustaceans, such as crabs, lobsters, and shrimp, are animals with hard outer shells, jointed legs, and antennae that mostly live in water.',
   [('What covers the body of a crustacean?', ['A hard outer shell', 'Soft fur', 'Feathers', 'Smooth, wet skin only'], 0),
    ('Which of these is an example of a crustacean?', ['A crab', 'A robin', 'A frog', 'A wolf'], 0),
    ('What kind of legs do crustaceans have?', ['Jointed legs', 'No legs at all', 'Wings instead of legs', 'A single leg'], 0),
    ('Where do most crustaceans live?', ['In water', 'In deserts only', 'In the sky', 'In caves with no water'], 0),
    ('What sensory body part helps a crustacean explore its surroundings?', ['Antennae', 'Fur on its back', 'Feathers on its head', 'A trunk like an elephant'], 0)]),
SS('Social Studies: School Crossing Guards and Traffic Safety Near Schools',
   'Grade 3 Social Studies strand: school crossing guards help students safely cross busy streets near schools by signalling to traffic and guiding pedestrians across at the right time.',
   [('What is the main job of a school crossing guard?', ['Helping students safely cross busy streets near schools', 'Teaching math lessons', 'Repairing school buses', 'Selling tickets for school events'], 0),
    ('How does a crossing guard help control traffic?', ['By signalling to drivers and guiding pedestrians', 'By driving the school bus', 'By painting the road', 'By closing the school for the day'], 0),
    ('Why are crossing guards often placed near schools?', ['To help keep students safe while crossing busy streets', 'Because schools have no students walking nearby', 'To prevent any students from arriving at school', 'Because crossing guards work only at night'], 0),
    ('What should a pedestrian do when a crossing guard signals it is safe to cross?', ['Cross the street following the guards signal', 'Ignore the guard completely', 'Run across without looking', 'Wait for a different signal entirely'], 0),
    ('Why is traffic safety near schools especially important?', ['Many children are walking and may be harder for drivers to see', 'Traffic safety has no connection to schools', 'Schools are always located far from any roads', 'No vehicles are ever near a school'], 0)]),
]),
day(176, [
L('Grammar: Using Ellipses to Show a Pause or Omission',
  'Grade 3 Language strand: an ellipsis, made of three dots, can show a pause in speech, a trailing thought, or that words have been left out of a quoted sentence.',
  [('What does an ellipsis look like?', ['Three dots in a row', 'A single dash', 'A question mark', 'A pair of parentheses'], 0),
   ('What can an ellipsis show in a sentence?', ['A pause in speech or a trailing thought', 'The end of a paragraph only', 'A brand new topic', 'A loud exclamation'], 0),
   ('Which sentence correctly uses an ellipsis to show a trailing thought?', ['I was going to say something, but... never mind.', 'I was going to say something but never mind', 'I was going to say something... but, never... mind', 'I was, going to say something but never mind...'], 0),
   ('What can an ellipsis show when used in a quoted sentence?', ['That some words have been left out', 'That the entire sentence has been added', 'That the sentence is a question', 'That the sentence must be read loudly'], 0),
   ('Why might a writer use an ellipsis instead of finishing a sentence?', ['To show hesitation or an unfinished thought', 'To make the sentence longer than needed', 'Because ellipses are never used in writing', 'To replace every period in a story'], 0)]),
M('Measurement: Introducing the Kilometre for Long Distances',
  'Grade 3 Math strand: a kilometre is a unit of length used to measure long distances, such as the distance between two towns, and is made up of 1000 metres.',
  [('What is a kilometre used to measure?', ['Long distances', 'The mass of a small object', 'The capacity of a cup', 'The temperature outside'], 0),
   ('How many metres are in one kilometre?', ['1000 metres', '100 metres', '10 metres', '10 000 metres'], 0),
   ('Which distance would most likely be measured in kilometres?', ['The distance between two towns', 'The length of a pencil', 'The height of a book', 'The width of a coin'], 0),
   ('Why is the kilometre a more useful unit than the metre for very long distances?', ['It allows large distances to be described using smaller numbers', 'It makes long distances impossible to measure', 'It is only used for measuring liquids', 'It replaces the need for any measurement'], 0),
   ('Which would likely be measured in kilometres rather than centimetres?', ['The distance a car travels on a road trip', 'The length of a paperclip', 'The width of a book', 'The height of a cup'], 0)]),
Sc('Science: The Life Cycle of a Mosquito',
   'Grade 3 Science strand: a mosquito goes through complete metamorphosis, changing from egg to larva to pupa to adult, with the early stages taking place in water.',
   [('What are the four stages of a mosquitos life cycle?', ['Egg, larva, pupa, adult', 'Egg, caterpillar, cocoon, butterfly', 'Seed, sprout, plant, flower', 'Tadpole, frog, egg, adult'], 0),
    ('Where do the early stages of a mosquitos life cycle take place?', ['In water', 'In the desert', 'Underground in soil', 'High in the mountains'], 0),
    ('What kind of metamorphosis does a mosquito go through?', ['Complete metamorphosis', 'No metamorphosis at all', 'A single unchanging stage', 'Metamorphosis only as an adult'], 0),
    ('Which stage comes right after the egg stage for a mosquito?', ['Larva', 'Pupa', 'Adult', 'Cocoon'], 0),
    ('Why might mosquitoes often be found near still water?', ['They lay their eggs in water and the early stages develop there', 'Mosquitoes never go near water', 'Water prevents mosquitoes from ever hatching', 'Mosquitoes only live in dry deserts'], 0)]),
SS('Social Studies: Grain Elevators and the Prairie Wheat Economy',
   'Grade 3 Social Studies strand: grain elevators are tall storage buildings found across the Canadian Prairies that store wheat and other grains grown by farmers before they are shipped to market.',
   [('What is a grain elevator used for?', ['Storing wheat and other grains before they are shipped', 'Storing cars for a dealership', 'Housing farm animals', 'Selling clothing to farmers'], 0),
    ('In which region of Canada are grain elevators commonly found?', ['The Prairies', 'The Arctic', 'Coastal British Columbia', 'Downtown Toronto'], 0),
    ('What crop is closely associated with the Prairie economy?', ['Wheat', 'Coffee beans', 'Rice grown in flooded fields', 'Bananas'], 0),
    ('Why might grain elevators be built tall?', ['To store large amounts of grain in one building', 'To block the wind on the Prairies', 'To act as a lookout tower only', 'Tall buildings have no connection to grain storage'], 0),
    ('What happens to grain after it leaves a grain elevator?', ['It is shipped to market to be sold or processed', 'It is thrown away completely', 'It is buried underground permanently', 'It disappears with no further use'], 0)]),
]),
day(177, [
L('Reading: Identifying the Climax of a Story',
  'Grade 3 Language strand: the climax of a story is the most exciting or important moment, often where a problem reaches its peak before being resolved.',
  [('What is the climax of a story?', ['The most exciting or important moment in the story', 'The very first sentence of the story', 'A list of characters at the end', 'The title of the story'], 0),
   ('When does the climax usually happen in a story?', ['Near the point where a problem reaches its peak', 'Before the story has even started', 'Only in the very first paragraph', 'The climax never happens in a story'], 0),
   ('What often happens after the climax of a story?', ['The problem begins to be resolved', 'The story restarts from the beginning', 'A brand new story begins with no connection', 'The climax always ends the story with no resolution'], 0),
   ('Why is the climax considered an important part of a story?', ['It is the turning point that leads toward the resolution', 'It has no real importance to the plot', 'It always happens at the very beginning', 'It is unrelated to the main problem'], 0),
   ('Which is an example of a climax in a story?', ['The moment a character finally faces the biggest challenge', 'The moment the book is closed', 'The name of the author on the cover', 'The list of chapters in the table of contents'], 0)]),
M('Data: Comparing Two Data Sets Side by Side',
  'Grade 3 Math strand: comparing two data sets side by side, such as two double bar graphs or two tables, helps students see similarities and differences between two groups of information.',
  [('Why might two data sets be compared side by side?', ['To see similarities and differences between two groups of information', 'To make the data impossible to understand', 'To remove all information from a graph', 'Because data sets can never be compared'], 0),
   ('Which tool could help compare two sets of data visually?', ['A double bar graph', 'A single word', 'A blank page', 'A pencil with no drawing'], 0),
   ('If Class A collected more data points than Class B, what might that show?', ['Class A gathered more information in their data set', 'Class A collected no data at all', 'Class B always has more information', 'The size of a data set never matters'], 0),
   ('What should you check first when comparing two data sets?', ['That both sets are measuring the same kind of information', 'The colour of the paper used', 'The time the data was written down', 'Nothing needs to be checked first'], 0),
   ('Why is comparing data useful in everyday life?', ['It helps people make informed decisions based on evidence', 'It has no real use in everyday decisions', 'It only matters for scientists', 'Comparing data always leads to confusion'], 0)]),
Sc('Science: Monarch Butterflies and Their Long Migration',
   'Grade 3 Science strand: monarch butterflies migrate thousands of kilometres each year between Canada and Mexico, using environmental cues to guide their long journey.',
   [('What is special about the monarch butterfly yearly journey?', ['It migrates thousands of kilometres between Canada and Mexico', 'It never leaves the same tree its whole life', 'It only travels a few metres each year', 'It migrates only within one backyard'], 0),
    ('What might help guide monarch butterflies on their long migration?', ['Environmental cues, such as the position of the sun', 'A map they carry with them', 'A leader butterfly giving spoken directions', 'Monarchs never use any cues to migrate'], 0),
    ('Why might monarch butterflies migrate to warmer areas?', ['To survive conditions they could not survive in a cold climate', 'They migrate for no particular reason', 'To find colder temperatures only', 'Monarch butterflies never migrate at all'], 0),
    ('Which two general regions are connected by monarch migration mentioned here?', ['Canada and Mexico', 'Africa and Europe', 'Australia and Antarctica', 'Asia and South America'], 0),
    ('Why is studying monarch butterfly migration important to scientists?', ['It helps them understand and protect the species and its habitat', 'It has no scientific value at all', 'Monarch butterflies are not studied by scientists', 'It only matters for one single butterfly'], 0)]),
SS('Social Studies: Canadas Lighthouse Keepers and Coastal Safety History',
   'Grade 3 Social Studies strand: lighthouse keepers historically maintained lights along Canadas coastlines to warn ships of dangerous rocks and guide them safely into harbour.',
   [('What was a lighthouse keeper job?', ['Maintaining the light to warn ships of danger', 'Selling tickets to tourists', 'Repairing roads near the coast', 'Delivering mail to nearby towns'], 0),
    ('Why were lighthouses built along Canadas coastlines?', ['To warn ships of dangerous rocks and guide them safely', 'To block ships from ever entering the water', 'To provide housing for farmers', 'To replace the need for any ships'], 0),
    ('What might happen to a ship without the warning of a lighthouse?', ['It could be in danger of hitting rocks or getting lost', 'It would always travel faster', 'Lighthouses have no effect on ship safety', 'Ships never need any warning at all'], 0),
    ('How has lighthouse technology changed over time?', ['Many lighthouses now use automated lights instead of a keeper', 'Lighthouses have never changed since they were built', 'Lighthouses no longer exist anywhere in Canada', 'Every lighthouse still requires a keeper today'], 0),
    ('Why might coastal safety be especially important for a country with many harbours?', ['It helps protect ships, sailors, and goods travelling by water', 'Coastal safety has no connection to shipping', 'Harbours are never used for travel or trade', 'Ships never need protection near the coast'], 0)]),
]),
day(178, [
L('Writing: Writing an Advertisement Script for the Radio',
  'Grade 3 Language strand: a radio advertisement script uses spoken words, sound effects, and a catchy message to persuade listeners, since there are no pictures to rely on.',
  [('Why does a radio advertisement rely heavily on spoken words and sound?', ['Because there are no pictures for listeners to see', 'Because radio advertisements are always silent', 'Because radio listeners can always see a screen', 'Because sound is never allowed in advertisements'], 0),
   ('What is the goal of an advertisement script?', ['To persuade listeners about a product or idea', 'To confuse the listener completely', 'To remove all information about a product', 'To read a list of unrelated facts'], 0),
   ('What might a radio advertisement include to grab attention?', ['A catchy message or sound effect', 'Complete silence for the entire advertisement', 'A blank page with no words', 'A single number repeated once'], 0),
   ('Why might a writer repeat a key phrase in a radio advertisement?', ['To help listeners remember the message', 'To make the advertisement forgettable', 'Because repetition is never used in advertising', 'To confuse the listener on purpose'], 0),
   ('What is one difference between a radio advertisement and a poster advertisement?', ['A radio advertisement uses only sound, while a poster uses images', 'A poster advertisement can never use words', 'A radio advertisement always includes a picture', 'There is no difference between the two'], 0)]),
M('Financial Literacy: Splitting a Bill Fairly Among Friends',
  'Grade 3 Math strand: when a group of friends shares a cost, such as a pizza, the total amount can be divided evenly among everyone to figure out how much each person should pay.',
  [('If a pizza costs 12 dollars and is shared evenly among 4 friends, how much does each friend pay?', ['3 dollars', '4 dollars', '2 dollars', '6 dollars'], 0),
   ('What operation is used to split a bill evenly among a group?', ['Division', 'Multiplication only', 'Rounding only', 'Estimating only'], 0),
   ('If a total cost is 20 dollars and it is split evenly among 5 friends, how much does each person owe?', ['4 dollars', '5 dollars', '10 dollars', '2 dollars'], 0),
   ('Why might friends want to split a bill fairly?', ['So everyone pays an equal, fair share of the total cost', 'So one person pays for everything alone', 'To avoid ever sharing a cost', 'Because splitting a bill is never fair'], 0),
   ('If a total cost is 18 dollars split evenly among 3 friends, how much does each friend pay?', ['6 dollars', '9 dollars', '3 dollars', '18 dollars'], 0)]),
Sc('Science: How Icicles and Frost Form in Winter',
   'Grade 3 Science strand: icicles form when dripping water freezes as it flows downward in cold temperatures, while frost forms when water vapour in the air freezes directly onto a cold surface.',
   [('How does an icicle usually form?', ['Dripping water freezes as it flows downward in cold temperatures', 'Warm air suddenly turns solid', 'Snow falls straight down without melting', 'Ice melts and disappears completely'], 0),
    ('How does frost form on a cold surface?', ['Water vapour in the air freezes directly onto the surface', 'Rain falls and immediately boils', 'Snow is swept into a pile by wind', 'Sunlight melts ice completely'], 0),
    ('What condition is needed for both icicles and frost to form?', ['Cold temperatures', 'Very hot temperatures', 'No moisture in the air at all', 'Bright sunshine with no clouds'], 0),
    ('Where might you commonly see icicles forming?', ['Hanging from a roof or gutter', 'Floating in the middle of the ocean', 'Growing underground', 'Inside a warm oven'], 0),
    ('Why might frost appear on a car windshield on a cold morning?', ['Water vapour in the air freezes onto the cold glass overnight', 'The windshield produces its own water', 'Frost only forms in the summer', 'The car engine creates frost on purpose'], 0)]),
SS('Social Studies: The Role of a Translator in Canadas Multilingual Communities',
   'Grade 3 Social Studies strand: translators help people who speak different languages understand one another, supporting communication in Canadas many multilingual communities.',
   [('What does a translator do?', ['Helps people who speak different languages understand one another', 'Builds roads between communities', 'Delivers packages across the country', 'Repairs vehicles for a living'], 0),
    ('Why might translators be important in a multilingual country like Canada?', ['They support communication among people who speak different languages', 'They have no role in communities at all', 'They prevent people from ever speaking to each other', 'Translators are only needed in one province'], 0),
    ('Where might a translator help someone in daily life?', ['At a hospital, school, or government office', 'Only inside a video game', 'Only in outer space', 'Nowhere, translators are never needed'], 0),
    ('What skill does a translator need to do their job well?', ['Understanding more than one language', 'Knowing how to fix cars', 'Knowing how to farm crops', 'Knowing how to fly airplanes'], 0),
    ('Why might a community value having access to translators?', ['It helps everyone access services and information, no matter what language they speak', 'It has no benefit to a community', 'It prevents people from receiving any services', 'Translators only work with one single language'], 0)]),
]),
day(179, [
L('Vocabulary: Words with Silent Letters',
  'Grade 3 Language strand: some English words contain silent letters that are written but not pronounced, such as the k in knee, the b in comb, and the w in write.',
  [('What is a silent letter?', ['A letter that is written but not pronounced', 'A letter that is always pronounced loudly', 'A letter used only in numbers', 'A letter that changes the whole meaning of a word'], 0),
   ('Which letter is silent in the word knee?', ['K', 'N', 'E', 'The last E'], 0),
   ('Which letter is silent in the word comb?', ['B', 'C', 'O', 'M'], 0),
   ('Which letter is silent in the word write?', ['W', 'R', 'I', 'T'], 0),
   ('Why might silent letters make spelling tricky for readers?', ['The letter appears in the spelling but is not heard when the word is spoken', 'Silent letters are always pronounced clearly', 'Silent letters never appear in English words', 'Silent letters only appear in numbers'], 0)]),
M('Patterning: Identifying Errors in a Pattern',
  'Grade 3 Math strand: checking a pattern carefully for errors means comparing each term to the rule to find any place where the pattern was not followed correctly.',
  [('What does it mean to identify an error in a pattern?', ['Finding a place where the pattern rule was not followed', 'Adding random numbers with no rule', 'Removing the pattern completely', 'Ignoring the rule of the pattern'], 0),
   ('In the pattern 2, 4, 6, 9, 10, which number breaks the add 2 rule?', ['9', '2', '4', '10'], 0),
   ('What should you do first to check a pattern for errors?', ['Identify the rule the pattern is supposed to follow', 'Erase the entire pattern', 'Ignore the first few numbers', 'Guess the answer with no checking'], 0),
   ('In the pattern 5, 10, 15, 21, 25, which number does not follow the add 5 rule?', ['21', '5', '15', '25'], 0),
   ('Why is it useful to be able to find errors in a pattern?', ['It helps confirm the pattern is correct and consistent', 'It removes the need to ever check a pattern', 'Patterns never contain errors', 'It has no connection to understanding patterns'], 0)]),
Sc('Science: How Skyscrapers Are Designed to Withstand Wind',
   'Grade 3 Science strand: skyscrapers are tall structures engineered with strong materials, wide bases, and flexible frames that allow them to safely sway slightly in strong winds.',
   [('Why must skyscrapers be designed to handle wind?', ['Tall buildings can be pushed by strong winds high above the ground', 'Wind never affects tall buildings', 'Skyscrapers are never built in windy places', 'Wind only affects short buildings'], 0),
    ('What might help a skyscraper stay stable?', ['A wide base and strong materials', 'No foundation at all', 'A frame made only of paper', 'Removing all support from the building'], 0),
    ('Why might a skyscraper be designed to sway slightly in the wind?', ['A flexible frame helps the building absorb the force of the wind safely', 'Swaying means the building is about to fall down', 'Buildings should never move even slightly', 'Swaying has no connection to engineering design'], 0),
    ('What kind of materials are commonly used to build strong skyscrapers?', ['Steel and reinforced concrete', 'Paper and cardboard', 'Ice and snow', 'Sand with no other materials'], 0),
    ('Why do engineers study wind and structures before building a skyscraper?', ['To design a building that stays safe and stable in different weather conditions', 'Because wind has no effect on any building', 'To make the building collapse on purpose', 'Engineers never study wind before building'], 0)]),
SS('Social Studies: The Canadian Snowbirds and Canadas Air Force Aerobatic Team',
   'Grade 3 Social Studies strand: the Canadian Snowbirds are an aerobatic flying team from the Royal Canadian Air Force that performs precision air shows across the country to celebrate Canadian identity and skill.',
   [('What is the Canadian Snowbirds team known for?', ['Performing precision aerobatic air shows', 'Delivering mail by airplane', 'Building new airports', 'Selling airplane tickets to the public'], 0),
    ('Which branch of the military are the Snowbirds part of?', ['The Royal Canadian Air Force', 'The Royal Canadian Navy', 'The Canadian Coast Guard', 'A private airline company'], 0),
    ('Where do the Snowbirds typically perform?', ['At air shows across the country', 'Only inside a single hangar', 'Only outside of Canada', 'Only underwater'], 0),
    ('What might the Snowbirds air shows help celebrate?', ['Canadian identity and flying skill', 'A single towns local bakery', 'A foreign countrys holiday', 'A private business opening'], 0),
    ('Why might precision be important for an aerobatic flying team?', ['The pilots must fly closely together with accuracy and safety', 'Precision has no connection to flying', 'Aerobatic teams never need to be accurate', 'Only one plane flies during the show'], 0)]),
]),
day(180, [
L('Language Review: Nouns, Narration, and Feedback Skills',
  'Grade 3 Language strand review: students revisit common and proper nouns, hyphens in compound adjectives, idioms about weather, first-person and third-person narration, identifying the climax of a story, writing directions for a treasure hunt, ellipses, writing an advertisement script, and words with silent letters.',
  [('What is a common noun?', ['A general person, place, or thing', 'A word that is always capitalized', 'A word that describes an action', 'A word used only in questions'], 0),
   ('What does a hyphen do in a compound adjective?', ['Joins two or more words together to describe a noun', 'Ends a sentence', 'Separates a paragraph into two parts', 'Replaces a comma in a list'], 0),
   ('What does the idiom under the weather usually mean?', ['Feeling sick or unwell', 'Standing outside in the rain', 'Feeling extremely happy', 'Wearing a raincoat'], 0),
   ('Which pronoun signals that a story is told in first person?', ['I', 'He', 'They', 'She'], 0),
   ('What is the climax of a story?', ['The most exciting or important moment in the story', 'The very first sentence of the story', 'A list of characters at the end', 'The title of the story'], 0)]),
M('Math Review: Number Sense, Multiplication, and Geometry',
  'Grade 3 Math strand review: students revisit comparing numbers with greater than, less than, and equal to symbols, using a number line to multiply, dividing with arrays, tessellations, the kilometre, and identifying errors in a pattern.',
  [('What does the greater than symbol mean?', ['Greater than', 'Less than', 'Equal to', 'Not equal to'], 0),
   ('On a number line, what does each equal jump represent when multiplying?', ['One group being counted', 'A subtraction step', 'A fraction of the whole', 'The remainder of the problem'], 0),
   ('What does an array show when used to model division?', ['How a total can be split evenly into equal groups', 'A single random number', 'Only multiplication facts', 'A list of fractions'], 0),
   ('What is a tessellation?', ['A pattern of shapes that fit together with no gaps or overlaps', 'A single shape drawn alone', 'A pattern with large gaps between shapes', 'A shape that never repeats'], 0),
   ('What is a kilometre used to measure?', ['Long distances', 'The mass of a small object', 'The capacity of a cup', 'The temperature outside'], 0)]),
Sc('Science Review: Canadian Wildlife, Insects, and Winter Weather',
   'Grade 3 Science strand review: students revisit beavers, polar bears, jellyfish, the life cycle of a mosquito, and how icicles and frost form in winter.',
   [('What do beavers use to cut down trees?', ['Their strong teeth', 'Their tail only', 'Their claws only', 'Tools they build'], 0),
    ('What helps keep a polar bear warm in the Arctic?', ['Thick fur and a layer of fat', 'A thin coat of feathers', 'A shell covering its body', 'Scales like a fish'], 0),
    ('What do jellyfish use their tentacles for?', ['Catching food and defending themselves using stinging cells', 'Digging burrows in the sand', 'Building nests on the ocean floor', 'Flying above the water'], 0),
    ('What are the four stages of a mosquitos life cycle?', ['Egg, larva, pupa, adult', 'Egg, caterpillar, cocoon, butterfly', 'Seed, sprout, plant, flower', 'Tadpole, frog, egg, adult'], 0),
    ('How does an icicle usually form?', ['Dripping water freezes as it flows downward in cold temperatures', 'Warm air suddenly turns solid', 'Snow falls straight down without melting', 'Ice melts and disappears completely'], 0)]),
SS('Social Studies Review: Landmarks, Honours, and Community Roles',
   'Grade 3 Social Studies strand review: students revisit the Order of Canada, the Parliament Buildings, the Confederation Bridge, school crossing guards, and the role of a translator.',
   [('What is the Order of Canada?', ['One of the countrys highest honours for citizens', 'A type of Canadian currency', 'A law passed by Parliament', 'A holiday celebrated every year'], 0),
    ('In which city are the Parliament Buildings located?', ['Ottawa', 'Toronto', 'Vancouver', 'Montreal'], 0),
    ('What does the Confederation Bridge connect?', ['Prince Edward Island to the rest of Canada', 'Ontario to Quebec', 'British Columbia to Alberta', 'Two cities within the same province'], 0),
    ('What is the main job of a school crossing guard?', ['Helping students safely cross busy streets near schools', 'Teaching math lessons', 'Repairing school buses', 'Selling tickets for school events'], 0),
    ('What does a translator do?', ['Helps people who speak different languages understand one another', 'Builds roads between communities', 'Delivers packages across the country', 'Repairs vehicles for a living'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g3_171_180, seed=20260818)
    append_to(3, g3_171_180)
