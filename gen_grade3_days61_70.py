#!/usr/bin/env python3
"""Phase 3 extension: Grade 3, Days 61-70 (pushes Grade 3 from 60 to 70
days, continuing toward the full 157-day year). Topics chosen to avoid
any overlap with the existing Day 1-60 set (see data/grade3.json):
idioms, contractions, homophones, division with remainders, the screw
and wedge, weather instruments, Canada's provinces and capitals, and
elections.

Subject keys for Grade 3 are "Language", "Math", "Science",
"SocialStudies" (same as all earlier Grade 3 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes and quotation marks use the
curly Unicode form (’ “ ”).
"""
import sys
sys.path.insert(0, '/sessions/happy-laughing-ritchie/mnt/gradesbooster')
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


g3_61_70 = [
day(61, [
L('Reading: Understanding Idioms and Expressions',
  'Grade 3 Language strand: an idiom is a group of words whose meaning is different from what the words say on their own, like “it’s raining cats and dogs,” which really means it is raining hard.',
  [('An idiom is a group of words whose meaning is ___.', ['Different from what the words say on their own', 'Always exactly what the words say', 'A concept unrelated to word meaning', 'Only found in math, not in language'], 0),
   ('The idiom “it’s raining cats and dogs” really means ___.', ['It is raining very hard', 'Cats and dogs are falling from the sky', 'A phrase unrelated to weather', 'The weather is calm and sunny'], 0),
   ('Why might an idiom confuse a reader who has never heard it before?', ['The words used do not literally match the idiom’s real meaning', 'Idioms are always written using their exact literal meaning', 'Idioms never appear in everyday spoken or written language', 'This concept has no connection to understanding language'], 0),
   ('If someone says “break a leg” before a play, what do they likely mean?', ['Good luck with your performance', 'They want the person to actually get hurt', 'A phrase unrelated to wishing someone well', 'The person should stop performing immediately'], 0),
   ('Why is it helpful to learn common idioms when reading stories?', ['It helps the reader understand meanings that are not stated literally', 'Idioms never appear in stories that children read', 'Understanding idioms has no connection to reading comprehension', 'Every idiom always has only one possible interpretation with no context needed'], 0)]),
M('Division: Understanding Remainders',
  'Grade 3 Math strand: when a number cannot be divided evenly, the amount left over is called the remainder, and it must always be smaller than the number you are dividing by.',
  [('When a number cannot be divided evenly, the amount left over is called the ___.', ['Remainder', 'Quotient, with no connection to leftover amounts', 'A concept unrelated to division', 'Product, which is the answer to a multiplication problem'], 0),
   ('What is 13 ÷ 4, including the remainder?', ['3 remainder 1', '4 remainder 1', '3 remainder 2', '4 remainder 0'], 0),
   ('A remainder must always be ___ than the number you are dividing by.', ['Smaller', 'Larger, with no connection to the divisor', 'A concept unrelated to the size of the divisor', 'Exactly equal to, with no exceptions'], 0),
   ('If 17 stickers are shared equally among 5 friends, how many stickers are left over?', ['2', '1', '3', '0'], 0),
   ('Why might understanding remainders be useful when sharing items in real life, like cookies among friends?', ['It shows how many items are left over after sharing them as evenly as possible', 'Remainders never occur when sharing items among friends', 'This concept has no connection to real-world sharing situations', 'Remainders only apply to multiplication, never to division'], 0)]),
Sc('Science: Simple Machines: Screw and Wedge',
   'Grade 3 Science strand: a screw is a simple machine made from an inclined plane wrapped around a pole, and a wedge is a simple machine made from two inclined planes joined together to push things apart.',
   [('A screw is a simple machine made from an inclined plane wrapped around a ___.', ['Pole', 'Flat surface, with no connection to a pole', 'A concept unrelated to simple machines', 'Wheel, which is a completely different simple machine'], 0),
    ('A wedge is made from two inclined planes joined together to ___.', ['Push things apart', 'Always hold things perfectly still', 'A concept unrelated to how a wedge works', 'Spin around a central pole'], 0),
    ('Which is an example of a wedge being used in everyday life?', ['An axe splitting a piece of wood', 'A concept unrelated to simple machines', 'An object that never applies any force', 'A wheel rolling smoothly along the ground'], 0),
    ('Why might a screw be useful for holding two pieces of wood together?', ['Its spiral shape grips the wood tightly as it turns, making it hard to pull out', 'Screws never actually hold objects together', 'This concept has no connection to how screws are used', 'A screw always falls out immediately no matter how it is used'], 0),
    ('Why are the screw and wedge both considered types of inclined planes?', ['They are both based on a sloped surface that makes it easier to do work', 'They have no connection to the inclined plane at all', 'A screw and wedge are always classified as completely separate types of machines', 'This concept has no relevance to understanding simple machines'], 0)]),
SS('Social Studies: Canada’s Provinces and Capital Cities',
   'Grade 3 Social Studies strand: Canada is made up of ten provinces and three territories, and each province has its own capital city where its provincial government meets.',
   [('Canada is made up of ten provinces and ___ territories.', ['Three', 'Ten, with no distinction from provinces', 'A concept unrelated to how Canada is divided', 'Zero, since Canada has no territories'], 0),
    ('Each province has its own capital city where its ___ meets.', ['Provincial government', 'National government of another country', 'A concept unrelated to government', 'Only its sports teams, with no government connection'], 0),
    ('What is the capital city of Ontario?', ['Toronto', 'Ottawa', 'Montreal', 'Vancouver'], 0),
    ('Why does each province have its own capital city, separate from Canada’s national capital?', ['Each province needs a place for its own provincial government to meet and make decisions', 'Provinces never have their own separate governments', 'This concept has no connection to how Canada is organized', 'Every province in Canada always shares the exact same capital city'], 0),
    ('Why might learning the provinces and their capital cities help students understand Canada better?', ['It builds a clearer picture of how the country is organized and governed', 'Learning about provinces and capitals provides no useful understanding of Canada', 'Provinces and capital cities have no connection to Canadian geography', 'This concept has no relevance to social studies learning'], 0)])]),

day(62, [
L('Grammar: Contractions',
  'Grade 3 Language strand: a contraction is a shortened form of two words joined together, using an apostrophe to show where letters have been left out, such as “don’t” for “do not.”',
  [('A contraction is a shortened form of two words joined together using ___.', ['An apostrophe to show missing letters', 'A comma to separate the two words', 'A concept unrelated to combining words', 'A hyphen with no missing letters at all'], 0),
   ('The contraction “don’t” is a shortened form of ___.', ['Do not', 'Does not', 'Did not', 'A phrase unrelated to “don’t”'], 0),
   ('Which is the correct contraction for “I am”?', ['I’m', 'Im', 'I’am', 'Iam'], 0),
   ('Why does a contraction use an apostrophe?', ['It shows exactly where one or more letters have been left out', 'An apostrophe has no connection to forming a contraction', 'Apostrophes are only used to show ownership, never in contractions', 'This concept has no relevance to how contractions are written'], 0),
   ('Why might a writer use contractions in a story’s dialogue?', ['Contractions can make characters’ speech sound more natural and conversational', 'Contractions always make writing sound less natural', 'This concept has no connection to how dialogue is written', 'Contractions are never used in spoken or written English'], 0)]),
M('Multiplication: Multiplying Multiples of Ten',
  'Grade 3 Math strand: multiplying a number by a multiple of ten, like 20 or 30, can be done by multiplying the basic fact first and then adding a zero to the answer.',
  [('Multiplying a number by a multiple of ten can be done by multiplying the basic fact first and then ___.', ['Adding a zero to the answer', 'Removing a zero from the original number', 'A method unrelated to multiplying by tens', 'Dividing the answer by ten'], 0),
   ('What is 3 × 20?', ['60', '23', '6', '600'], 0),
   ('What is 4 × 30?', ['120', '34', '12', '43'], 0),
   ('Why does multiplying 5 × 40 give the same first step as multiplying 5 × 4?', ['Because 40 is 4 tens, so the basic fact 5 × 4 is solved first and then a zero is added', 'Multiplying by tens has no connection to basic multiplication facts', 'The digits 5 and 4 never relate to solving 5 × 40', 'This strategy only works for multiplying by ones, never by tens'], 0),
   ('If a store sells pencils in packs of 20 and a class buys 6 packs, how many pencils is that in total?', ['120', '26', '86', '20'], 0)]),
Sc('Science: Weather: Instruments and Tools',
   'Grade 3 Science strand: scientists use tools like thermometers, rain gauges, and wind vanes to measure and record different parts of the weather, such as temperature, rainfall, and wind direction.',
   [('Scientists use tools like thermometers, rain gauges, and wind vanes to measure ___.', ['Different parts of the weather', 'A concept unrelated to weather at all', 'Only the time of day, with no connection to weather', 'The number of people in a community'], 0),
    ('A rain gauge is used to measure ___.', ['How much rain has fallen', 'Wind direction, with no connection to rain', 'Air temperature, with no connection to rainfall', 'A concept unrelated to weather measurement'], 0),
    ('Which tool would help you find out which direction the wind is blowing?', ['A wind vane', 'A thermometer, which measures temperature instead', 'A rain gauge, which measures rainfall instead', 'A tool unrelated to measuring wind'], 0),
    ('Why is it useful for scientists to record weather measurements every day?', ['Tracking measurements over time can reveal patterns and help predict future weather', 'Daily weather measurements never provide any useful information', 'Weather patterns can never be tracked using scientific tools', 'This concept has no connection to understanding weather'], 0),
    ('Why might a thermometer placed in direct sunlight give a less accurate air temperature reading?', ['Direct sunlight can heat the thermometer itself, making the reading higher than the actual air temperature', 'Sunlight never affects how a thermometer measures temperature', 'Thermometers always give the exact same reading no matter where they are placed', 'This concept has no relevance to accurately measuring weather'], 0)]),
SS('Social Studies: How Elections Work: Voting for Leaders',
   'Grade 3 Social Studies strand: an election is a process where citizens vote to choose their leaders, and the candidate who receives the most votes is usually the one who wins.',
   [('An election is a process where citizens vote to choose their ___.', ['Leaders', 'Favourite sports team, with no connection to government', 'A concept unrelated to government', 'Weather forecast for the week'], 0),
    ('In most elections, the candidate who receives the most votes is usually the one who ___.', ['Wins', 'Automatically loses, regardless of the vote count', 'A concept unrelated to how elections work', 'Is disqualified from participating further'], 0),
    ('Which is an example of something citizens might do during an election?', ['Cast a vote for their preferred candidate', 'A concept unrelated to participating in an election', 'Ignore the election entirely with no involvement', 'Choose a leader with no voting process at all'], 0),
    ('Why might it be important for many citizens to vote in an election?', ['A larger number of voters helps ensure the outcome reflects the views of more people in the community', 'Voting has no effect on who is chosen as a leader', 'Elections are decided with no connection to how citizens vote', 'This concept has no relevance to understanding government'], 0),
    ('Why do communities hold elections instead of simply choosing a leader without any input from citizens?', ['Elections allow citizens to have a say in who represents and makes decisions for them', 'Elections have no connection to how citizens are represented', 'Choosing a leader without any voting process is always the same as holding an election', 'This concept has no relevance to social studies learning'], 0)])]),

day(63, [
L('Vocabulary: Homophones',
  'Grade 3 Language strand: homophones are words that sound the same but have different spellings and different meanings, such as “their,” “there,” and “they’re.”',
  [('Homophones are words that sound the same but have different ___.', ['Spellings and meanings', 'Lengths, with no connection to spelling or meaning', 'A concept unrelated to how words sound', 'Number of syllables exclusively, with no connection to meaning'], 0),
   ('Which pair of words are homophones?', ['Flower and flour', 'Happy and sad', 'Big and small', 'A pair of words unrelated in sound'], 0),
   ('In the sentence “___ going to the park,” which homophone correctly completes the sentence?', ['They’re', 'Their', 'There', 'A word unrelated to any of these homophones'], 0),
   ('Why might homophones sometimes be tricky for writers to use correctly?', ['Even though they sound identical, using the wrong spelling changes the sentence’s meaning', 'Homophones are always spelled exactly the same way', 'Homophones never cause any confusion in writing', 'This concept has no connection to correct spelling'], 0),
   ('Why is it helpful to think about a sentence’s meaning when choosing between homophones like “to,” “too,” and “two”?', ['The meaning of the sentence shows which spelling correctly fits the intended word', 'Meaning has no connection to choosing the correct homophone', 'All three spellings can always be used interchangeably with no difference', 'This concept has no relevance to writing clearly'], 0)]),
M('Fractions: Subtracting Fractions with the Same Denominator',
  'Grade 3 Math strand: to subtract fractions that have the same denominator, subtract the numerators and keep the denominator the same.',
  [('To subtract fractions with the same denominator, subtract the numerators and ___.', ['Keep the denominator the same', 'Subtract the denominators as well', 'A method unrelated to subtracting fractions', 'Multiply the denominators together instead'], 0),
   ('What is 4/5 − 2/5?', ['2/5', '2/10', '6/5', '2/0'], 0),
   ('What is 7/8 − 3/8?', ['4/8', '10/8', '4/16', '4/0'], 0),
   ('Why does the denominator stay the same when subtracting fractions like 3/4 and 1/4?', ['The denominator shows the size of the equal parts, which does not change during subtraction', 'The denominator always changes when subtracting fractions', 'This concept has no connection to how fractions represent parts of a whole', 'Denominators are only used when adding fractions, never when subtracting'], 0),
   ('If a pizza is cut into 6 equal slices and 1/6 of it is eaten, how much of the pizza is left?', ['5/6', '6/6', '1/6', '4/6'], 0)]),
Sc('Science: Weather: Clouds and Precipitation',
   'Grade 3 Science strand: clouds form when water vapour in the air cools and turns into tiny droplets, and precipitation, such as rain, snow, or hail, happens when these droplets become too heavy to stay in the air.',
   [('Clouds form when water vapour in the air cools and turns into ___.', ['Tiny droplets', 'Solid rock, with no connection to water', 'A concept unrelated to how clouds form', 'Pure oxygen, with no connection to water vapour'], 0),
    ('Precipitation happens when water droplets in a cloud become too heavy to ___.', ['Stay in the air', 'Ever fall to the ground at all', 'A concept unrelated to how precipitation forms', 'Turn into a completely different type of matter'], 0),
    ('Which is an example of precipitation?', ['Snow', 'Sunshine, which is not a form of precipitation', 'Wind, which is not a form of precipitation', 'A concept unrelated to weather'], 0),
    ('Why might snow fall instead of rain during very cold weather?', ['Cold temperatures can cause water droplets to freeze into ice crystals as they fall', 'Temperature has no effect on the type of precipitation that falls', 'Snow only ever forms during warm weather', 'This concept has no connection to how precipitation forms'], 0),
    ('Why is understanding how clouds and precipitation form useful for predicting weather?', ['Knowing how these processes work can help explain and anticipate upcoming rain, snow, or other weather', 'Clouds and precipitation have no connection to predicting future weather', 'Weather can never be predicted using knowledge of clouds or precipitation', 'This concept has no relevance to understanding weather patterns'], 0)]),
SS('Social Studies: Time Zones Across Canada',
   'Grade 3 Social Studies strand: Canada is so wide that it is divided into six time zones, meaning the time of day can be different in different parts of the country at the very same moment.',
   [('Canada is divided into six ___, meaning the time of day can differ across the country.', ['Time zones', 'Provinces, with no connection to time', 'A concept unrelated to how Canada is organized', 'Languages, with no connection to time differences'], 0),
    ('Canada has multiple time zones because the country is very ___.', ['Wide, stretching across a large distance', 'Small, with almost no distance from coast to coast', 'A concept unrelated to Canada’s size', 'Cold, with no connection to its size or shape'], 0),
    ('If it is 3:00pm in Ontario, the time in a province further west, like British Columbia, would likely be ___.', ['Earlier than 3:00pm', 'Exactly 3:00pm, with no difference at all', 'Later than 3:00pm', 'A concept unrelated to time zones'], 0),
    ('Why might having multiple time zones be useful for a country as large as Canada?', ['It helps keep the time of day more closely matched to the actual position of the sun in each region', 'Time zones have no connection to a country’s size or geography', 'Every part of a large country should always share the exact same time', 'This concept has no relevance to understanding Canada’s geography'], 0),
    ('Why might someone need to consider time zones when calling a friend who lives in a different part of Canada?', ['The time of day could be quite different in the other time zone, even at the same moment', 'Time zones never affect what time it is in another part of the country', 'Every phone call across Canada happens at the exact same local time', 'This concept has no relevance to communicating across the country'], 0)])]),

day(64, [
L('Writing: Writing a Postcard to a Friend',
  'Grade 3 Language strand: a postcard is a short piece of writing that describes a place or an experience, usually including a greeting, a few interesting details, and a friendly closing.',
  [('A postcard is a short piece of writing that describes ___.', ['A place or an experience', 'A concept unrelated to sharing information with someone', 'Only a list of random numbers', 'A topic with no connection to the writer’s own experience'], 0),
   ('A postcard usually includes a greeting, a few interesting details, and a ___.', ['Friendly closing', 'A concept unrelated to how a postcard ends', 'A long list of complaints, with no friendly tone', 'Nothing at all, since postcards do not need an ending'], 0),
   ('Which is an example of an interesting detail that might appear on a postcard from the beach?', ['The sand was warm and the waves were huge', 'A detail entirely unrelated to a beach visit', 'A sentence with no connection to any experience', 'Something the writer did not actually see or do'], 0),
   ('Why might a postcard include only a few short sentences, rather than several paragraphs?', ['A postcard has limited space, so writers must choose their most interesting details', 'A postcard always has unlimited space for writing', 'The amount of space available has no connection to how a postcard is written', 'This concept has no relevance to writing a postcard'], 0),
   ('Why might someone send a postcard to a friend while on a trip?', ['It is a fun way to share highlights of the trip while staying connected with someone back home', 'Postcards are never used to share experiences with others', 'This concept has no connection to communicating with friends', 'A postcard cannot be used to describe a trip in any way'], 0)]),
M('Data: Sorting and Classifying Objects',
  'Grade 3 Math strand: sorting and classifying objects means grouping them by a shared attribute, such as colour, shape, or size, which helps organize information before it is displayed in a chart or graph.',
  [('Sorting and classifying objects means grouping them by a shared ___.', ['Attribute, such as colour, shape, or size', 'Location on a page, with no connection to the object itself', 'A concept unrelated to organizing objects', 'Random order, with no shared characteristic at all'], 0),
   ('Which is an example of sorting a group of buttons?', ['Grouping the buttons by colour', 'A method unrelated to organizing objects', 'Throwing the buttons away with no organization', 'Counting only one button and ignoring the rest'], 0),
   ('Why might sorting objects be a helpful first step before creating a graph?', ['Sorting organizes the information clearly, making it easier to count and display', 'Sorting objects never helps with creating a graph', 'A graph can only be made without any sorting or organizing beforehand', 'This concept has no connection to organizing data'], 0),
   ('If a group of shapes is sorted by number of sides, which two shapes might be placed in the same group?', ['A square and a rectangle', 'A triangle and a circle', 'A concept unrelated to sorting shapes', 'Two shapes chosen with no attention to their properties'], 0),
   ('Why might two people sort the same group of objects in different ways?', ['They may choose to group the objects by different attributes, like colour instead of size', 'Objects can only ever be sorted in a single correct way', 'Sorting objects never depends on which attribute is chosen', 'This concept has no relevance to understanding data management'], 0)]),
Sc('Science: Structures Found in Nature',
   'Grade 3 Science strand: many living things build natural structures, such as spider webs, bird nests, and beehives, that are specially suited to keep them safe and help them survive.',
   [('Natural structures like spider webs, bird nests, and beehives are specially suited to help living things ___.', ['Stay safe and survive', 'Always be destroyed quickly', 'A concept unrelated to how animals survive', 'Move faster than any other animal'], 0),
    ('Which is an example of a natural structure built by an animal?', ['A beehive', 'A concept unrelated to structures built by living things', 'A structure that no living thing has ever built', 'An object built entirely by humans, with no connection to nature'], 0),
    ('Why might a spider build a web in a shape that stretches across an open space?', ['A wide web increases the chance of catching flying insects for food', 'A web’s shape has no connection to how a spider catches food', 'Spiders never build webs to help them find food', 'This concept has no relevance to how natural structures function'], 0),
    ('Why might a bird build its nest high in a tree, rather than on the ground?', ['A higher location can help protect the nest and eggs from predators', 'The height of a nest has no connection to protecting it from predators', 'Birds never consider safety when building a nest', 'This concept has no relevance to understanding natural structures'], 0),
    ('Why might engineers sometimes study natural structures, like beehives, when designing buildings?', ['Natural structures can show strong, efficient designs that have developed over a very long time', 'Natural structures have no connection to human-made designs', 'Engineers never look to nature for ideas about building design', 'This concept has no relevance to understanding structures'], 0)]),
SS('Social Studies: Starting a Small Business: Entrepreneurs in the Community',
   'Grade 3 Social Studies strand: an entrepreneur is a person who starts their own business, taking on the risk of the idea in the hope of providing a helpful product or service to the community.',
   [('An entrepreneur is a person who ___.', ['Starts their own business', 'Never takes any risks with a new idea', 'A concept unrelated to starting a business', 'Only works for someone else’s existing business'], 0),
    ('An entrepreneur takes on the risk of a new idea in the hope of providing a helpful ___ to the community.', ['Product or service', 'A concept unrelated to what a business offers', 'Nothing at all, since businesses provide no benefit', 'Only entertainment, with no other possible purpose'], 0),
    ('Which is an example of something an entrepreneur might do to start a business?', ['Come up with an idea and figure out how to sell it', 'A concept unrelated to starting a business', 'Wait for someone else to start the business for them', 'Ignore whether the community needs the product or service'], 0),
    ('Why might starting a small business be considered a risk for an entrepreneur?', ['There is no guarantee the business will succeed, so the entrepreneur could lose money or time', 'Starting a business is never risky in any way', 'Entrepreneurs are always guaranteed success with no possible risk', 'This concept has no connection to understanding how businesses start'], 0),
    ('Why might a small business started by an entrepreneur benefit the local community?', ['It can provide new products, services, or jobs that help meet community needs', 'Small businesses never provide any benefit to a community', 'This concept has no connection to understanding local economies', 'A small business always has a negative effect on its community'], 0)])]),

day(65, [
L('Reading: Making Predictions',
  'Grade 3 Language strand: making a prediction means using clues from the text, pictures, or prior knowledge to make a sensible guess about what might happen next in a story.',
  [('Making a prediction means using clues to make a sensible ___ about what might happen next.', ['Guess', 'Concept unrelated to reading a story', 'Random decision, with no connection to any clues', 'Rule that will always be exactly correct with no exceptions'], 0),
   ('Which is a good source of clues a reader can use to make a prediction?', ['Details already given in the story', 'A concept unrelated to reading a story', 'Information from a completely different book', 'A guess with no connection to the story at all'], 0),
   ('Why might looking at the pictures in a book help a reader make a prediction?', ['Pictures can show hints about characters, settings, or events that help suggest what might happen next', 'Pictures never provide any useful information about a story', 'This concept has no connection to making predictions', 'A reader should always ignore the pictures in a book'], 0),
   ('If a story shows dark storm clouds gathering, what might a reader predict will happen next?', ['A storm is likely about to happen', 'The weather will definitely stay perfectly sunny', 'A concept unrelated to using clues from the story', 'Nothing at all will happen in the story'], 0),
   ('Why is it useful for readers to check their predictions as they continue reading a story?', ['It helps readers stay engaged and adjust their thinking based on new information', 'Checking predictions never helps a reader understand a story better', 'A prediction should never be checked or changed once it is made', 'This concept has no relevance to reading comprehension'], 0)]),
M('Time: Reading a Calendar',
  'Grade 3 Math strand: a calendar organizes days into weeks and months, helping people track dates, plan events, and figure out how many days are between two events.',
  [('A calendar organizes days into weeks and ___.', ['Months', 'Minutes, with no connection to how a calendar is organized', 'A concept unrelated to tracking dates', 'Only hours, with no connection to days'], 0),
   ('How many days are typically in one week?', ['7', '5', '10', '30'], 0),
   ('If today is Monday, what day will it be in 3 days?', ['Thursday', 'Wednesday', 'Friday', 'Tuesday'], 0),
   ('Why might someone use a calendar to plan for an upcoming event, like a birthday party?', ['A calendar helps track exactly which date the event will happen and how many days remain', 'A calendar has no connection to planning events', 'Calendars are only useful for showing the current day, with no other purpose', 'This concept has no relevance to organizing time'], 0),
   ('If a school trip is on March 10th and today is March 3rd, how many days away is the trip?', ['7 days', '10 days', '3 days', '13 days'], 0)]),
Sc('Science: Sound: How Animals Use Sound to Communicate',
   'Grade 3 Science strand: many animals use sound to communicate, such as birds singing to attract a mate or warn of danger, and whales calling to one another across long distances underwater.',
   [('Many animals use sound to ___.', ['Communicate with one another', 'Always stay completely silent, with no communication at all', 'A concept unrelated to how animals interact', 'Change their physical appearance permanently'], 0),
    ('A bird might sing to attract a mate or to ___.', ['Warn of danger', 'Always confuse other birds with no clear purpose', 'A concept unrelated to why birds sing', 'Change the weather around it'], 0),
    ('Which is an example of an animal using sound to communicate over a long distance?', ['A whale calling to other whales underwater', 'A concept unrelated to animal communication', 'An animal that never makes any sound at all', 'A situation where sound has no useful purpose'], 0),
    ('Why might it be useful for an animal to warn others of danger using sound?', ['A warning sound can quickly alert nearby animals to a threat, helping them stay safe', 'Sound has no connection to warning other animals of danger', 'Animals never use sound to communicate about danger', 'This concept has no relevance to understanding animal behaviour'], 0),
    ('Why might different animals use different types of sounds to communicate?', ['Different sounds can be suited to different environments, distances, or messages', 'All animals always use the exact same sound to communicate every message', 'The type of sound an animal makes has no connection to its purpose', 'This concept has no relevance to understanding how animals communicate'], 0)]),
SS('Social Studies: Public Transportation in Communities',
   'Grade 3 Social Studies strand: public transportation, such as buses, subways, and trains, helps move many people around a community at once, reducing the number of cars on the road.',
   [('Public transportation, such as buses and trains, helps move many people around a community ___.', ['At once', 'One person at a time exclusively, with no other passengers', 'A concept unrelated to moving people', 'Only outside the community, never within it'], 0),
    ('Using public transportation can help reduce the number of ___ on the road.', ['Cars', 'Pedestrians, with no connection to reducing traffic', 'A concept unrelated to transportation', 'Buildings, which are not vehicles on the road'], 0),
    ('Which is an example of a type of public transportation?', ['A subway', 'A concept unrelated to moving people around a community', 'A private car owned by a single family', 'A form of transportation that does not actually exist'], 0),
    ('Why might a large city rely heavily on public transportation?', ['It helps move large numbers of people efficiently without requiring everyone to drive their own car', 'Public transportation has no benefit for cities with many people', 'Large cities never need any form of transportation system', 'This concept has no relevance to understanding urban communities'], 0),
    ('Why might using public transportation instead of individual cars be helpful for the environment?', ['Moving many people together in one vehicle can reduce overall traffic and pollution compared to many separate cars', 'Public transportation always creates more pollution than individual cars', 'This concept has no connection to understanding the environment', 'The number of vehicles on the road has no effect on the environment'], 0)])]),

day(66, [
L('Grammar: Quotation Marks in Dialogue',
  'Grade 3 Language strand: quotation marks show exactly which words a character is speaking out loud, helping readers tell the difference between dialogue and the rest of the story.',
  [('Quotation marks show exactly which words a character is ___.', ['Speaking out loud', 'Thinking silently, with no words spoken aloud', 'A concept unrelated to dialogue in a story', 'Writing in a letter, with no connection to speech'], 0),
   ('Quotation marks help readers tell the difference between dialogue and ___.', ['The rest of the story', 'A concept unrelated to reading a story', 'Only the story’s title, with no other connection', 'Nothing at all, since quotation marks serve no purpose'], 0),
   ('Which sentence correctly uses quotation marks to show dialogue?', ['“I am ready to go,” said Maya.', 'I am ready to go, said Maya.', 'A sentence with no quotation marks at all around the spoken words', '“I am ready to go, said Maya.'], 0),
   ('Why might a writer use quotation marks when writing a story with characters talking to each other?', ['It clearly shows the reader exactly which words are being spoken aloud by a character', 'Quotation marks have no connection to writing dialogue', 'A story can never include characters speaking to one another', 'This concept has no relevance to writing clear stories'], 0),
   ('Why is it important to place quotation marks correctly around only the spoken words in a sentence?', ['Placing them incorrectly could confuse the reader about what was actually said versus described', 'The placement of quotation marks never affects how a sentence is understood', 'Quotation marks can be placed anywhere in a sentence with no effect on meaning', 'This concept has no relevance to writing clear dialogue'], 0)]),
M('Geometry: Plotting Points on a Grid',
  'Grade 3 Math strand: a grid is made of rows and columns, and a point can be located on it by using a pair of numbers or letters, such as moving across and then up.',
  [('A point can be located on a grid by using a pair of numbers or letters, such as moving across and then ___.', ['Up', 'Sideways only, with no vertical movement at all', 'A concept unrelated to locating a point', 'Backward in time, with no connection to a grid'], 0),
   ('On a grid, moving across before moving up or down helps to ___.', ['Correctly locate a specific point', 'Always end up in the exact same place no matter where you start', 'A concept unrelated to using a grid', 'Erase the grid entirely'], 0),
   ('If you are told to move 3 spaces right and 2 spaces up on a grid, what have you been given?', ['Directions to locate a specific point', 'A concept unrelated to using a grid', 'A rule with no connection to finding a location', 'Instructions for solving a subtraction problem'], 0),
   ('Why is it important to move across the grid before moving up or down, rather than in a random order?', ['Following a consistent order helps everyone locate the same point accurately every time', 'The order of movement on a grid never matters', 'This concept has no connection to correctly reading a grid', 'A grid can never be used to locate a specific point'], 0),
   ('Why might a grid with labelled rows and columns be useful for describing a location, like on a simple map?', ['It gives a clear, consistent way to describe exactly where something is placed', 'A grid provides no useful information about location', 'Labelled rows and columns have no connection to finding a location', 'This concept has no relevance to understanding grids'], 0)]),
Sc('Science: Energy: Sources of Light, Natural and Artificial',
   'Grade 3 Science strand: light can come from natural sources, like the sun and fire, or from artificial sources, like lightbulbs and flashlights that people have created.',
   [('Light can come from natural sources or from ___ sources that people have created.', ['Artificial', 'A concept unrelated to where light comes from', 'Only imaginary, with no connection to real light sources', 'Underground, with no connection to how light is produced'], 0),
    ('Which is an example of a natural source of light?', ['The sun', 'A flashlight, which is an artificial source of light', 'A lightbulb, which is an artificial source of light', 'A concept unrelated to sources of light'], 0),
    ('Which is an example of an artificial source of light?', ['A lightbulb', 'The sun, which is a natural source of light', 'A campfire, which is a natural source of light', 'A concept unrelated to sources of light'], 0),
    ('Why might people rely on artificial light sources at night?', ['Natural light from the sun is not available after it sets, so artificial sources help provide light', 'Artificial light sources are never needed at any time of day', 'The sun continues to provide light even after it sets', 'This concept has no connection to how people use light'], 0),
    ('Why might a campfire be considered a natural source of light, even though people often start it themselves?', ['The fire itself produces light through a natural burning process, unlike a manufactured device like a lightbulb', 'Campfires are always classified as artificial light sources', 'This concept has no connection to understanding sources of light', 'Fire never actually produces any light at all'], 0)]),
SS('Social Studies: Community Infrastructure: Roads, Water, and Power',
   'Grade 3 Social Studies strand: community infrastructure includes systems like roads, water pipes, and power lines that work together behind the scenes to keep a community running smoothly.',
   [('Community infrastructure includes systems like roads, water pipes, and ___ that keep a community running.', ['Power lines', 'A concept unrelated to how a community functions', 'Only decorations, with no connection to essential services', 'Nothing at all, since infrastructure has no real purpose'], 0),
    ('Infrastructure systems often work ___ to keep a community running smoothly.', ['Behind the scenes', 'In a way that is always visible and obvious to everyone', 'A concept unrelated to how a community operates', 'Only during special community events, with no ongoing purpose'], 0),
    ('Which is an example of community infrastructure?', ['A water pipe system bringing clean water to homes', 'A concept unrelated to community infrastructure', 'A single person’s personal opinion, with no connection to infrastructure', 'An event held once a year, with no ongoing structure'], 0),
    ('Why might a community struggle if its roads were poorly maintained?', ['Poorly maintained roads could make it harder and less safe to travel, deliver goods, or reach services', 'Roads have no connection to how well a community functions', 'A community can function perfectly well with no roads or infrastructure at all', 'This concept has no relevance to understanding community needs'], 0),
    ('Why is infrastructure like power lines important, even though many people rarely think about it?', ['It provides an essential service, like electricity, that many parts of daily life depend on', 'Power lines have no connection to daily life in a community', 'Infrastructure is never actually necessary for a community to function', 'This concept has no relevance to social studies learning'], 0)])]),

day(67, [
L('Oral Communication: Asking Clarifying Questions',
  'Grade 3 Language strand: a clarifying question is a question asked to better understand something that was unclear, helping a listener make sure they correctly understood what was said.',
  [('A clarifying question is asked to better understand something that was ___.', ['Unclear', 'Already perfectly understood, with no confusion at all', 'A concept unrelated to listening', 'Completely unrelated to the conversation'], 0),
   ('Asking a clarifying question helps a listener make sure they ___.', ['Correctly understood what was said', 'Never actually listen to the speaker at all', 'A concept unrelated to understanding a conversation', 'Change the topic completely, with no connection to what was said'], 0),
   ('Which is an example of a clarifying question someone might ask after receiving confusing instructions?', ['Could you explain that step again, please?', 'A statement unrelated to asking for clarification', 'A question with no connection to understanding instructions', 'Comment with no question involved at all'], 0),
   ('Why might asking a clarifying question be helpful during a class discussion?', ['It can prevent misunderstandings by making sure everyone has the same, correct understanding', 'Clarifying questions never help with understanding a discussion', 'Asking questions during a discussion is never appropriate', 'This concept has no relevance to effective communication'], 0),
   ('Why might it be better to ask a clarifying question rather than guessing what someone meant?', ['Guessing could lead to a misunderstanding, while asking ensures accurate understanding', 'Guessing is always more accurate than asking a clarifying question', 'Clarifying questions never lead to a better understanding of a conversation', 'This concept has no connection to effective oral communication'], 0)]),
M('Patterning: Patterns on a Hundred Chart',
  'Grade 3 Math strand: a hundred chart arranges the numbers 1 to 100 in rows of ten, and this arrangement makes visual patterns, like skip counting or multiples, easier to see.',
  [('A hundred chart arranges the numbers 1 to 100 in rows of ___.', ['Ten', 'One hundred, with no connection to smaller rows', 'A concept unrelated to how numbers are arranged', 'Two, with no connection to a hundred chart’s structure'], 0),
   ('On a hundred chart, the numbers directly below one another differ by ___.', ['10', '1', '100', 'A value unrelated to the chart’s structure'], 0),
   ('If you highlight every multiple of 5 on a hundred chart, what pattern would you likely see?', ['A straight, evenly spaced pattern going down and across the chart', 'A completely random and unpredictable arrangement of highlighted numbers', 'A concept unrelated to visualizing multiples', 'No pattern would ever appear on a hundred chart'], 0),
   ('Why might a hundred chart make it easier to spot patterns in skip counting?', ['The organized rows and columns make repeated jumps in number easy to see visually', 'A hundred chart has no connection to visualizing number patterns', 'Skip counting patterns can never be shown using a hundred chart', 'This concept has no relevance to understanding number patterns'], 0),
   ('Why might a hundred chart be a useful tool for a student who is still learning multiplication facts?', ['Seeing the visual pattern of multiples can help reinforce and support understanding of multiplication', 'A hundred chart has no connection to learning multiplication', 'Multiplication facts can never be supported using a visual tool like a hundred chart', 'This concept has no relevance to understanding math patterns'], 0)]),
Sc('Science: Classifying Animals: Vertebrates and Invertebrates',
   'Grade 3 Science strand: animals can be classified as vertebrates, which have a backbone, or invertebrates, which do not have a backbone, such as insects and worms.',
   [('Animals can be classified as vertebrates, which have a ___.', ['Backbone', 'Concept unrelated to how animals are classified', 'Set of wings, with no connection to having a backbone', 'Shell, with no connection to a backbone'], 0),
    ('Invertebrates are animals that ___.', ['Do not have a backbone', 'Always have a backbone, with no exceptions', 'A concept unrelated to animal classification', 'Can never be classified in any way'], 0),
    ('Which is an example of an invertebrate?', ['A worm', 'A dog, which has a backbone', 'A fish, which has a backbone', 'A concept unrelated to classifying animals'], 0),
    ('Why might scientists use the presence or absence of a backbone to help classify animals?', ['It is a clear, shared physical feature that groups animals into two broad, useful categories', 'A backbone has no connection to how animals are classified', 'Classifying animals never depends on any physical feature', 'This concept has no relevance to understanding animal classification'], 0),
    ('Why might insects, despite being very different from worms, still both be classified as invertebrates?', ['Neither insects nor worms have a backbone, which is the shared feature used for this classification', 'Insects and worms are always classified into two completely separate categories', 'This concept has no connection to how animals are grouped', 'Classifying animals never considers whether they have a backbone'], 0)]),
SS('Social Studies: Preserving Ontario’s Historic Buildings and Sites',
   'Grade 3 Social Studies strand: Ontario has many historic buildings and sites that communities work to preserve, protecting these places so future generations can learn about the past.',
   [('Communities work to preserve historic buildings and sites, protecting these places so ___ can learn about the past.', ['Future generations', 'No one at all, since preservation serves no purpose', 'Only the people who built the site originally', 'A concept unrelated to protecting historic places'], 0),
    ('A historic building or site is one that has ___.', ['An important connection to the past', 'No connection to any past event or time period', 'A concept unrelated to history', 'Only been built within the last year'], 0),
    ('Which is an example of something a community might do to preserve a historic building?', ['Repair and maintain it carefully instead of tearing it down', 'A concept unrelated to preserving historic places', 'Ignore the building until it eventually falls apart', 'Replace the building entirely with something brand new'], 0),
    ('Why might a community choose to preserve an old building instead of replacing it with something new?', ['The building may hold important historical or cultural value that would be lost if it were removed', 'Preserving old buildings never has any value to a community', 'Historic buildings have no connection to a community’s past', 'This concept has no relevance to understanding heritage'], 0),
    ('Why is learning about historic buildings and sites valuable for students studying Ontario’s past?', ['These places can offer real, physical connections to how people lived and worked long ago', 'Historic buildings provide no useful information about the past', 'This concept has no connection to understanding Ontario’s history', 'Learning about historic sites has no relevance to social studies'], 0)])]),

day(68, [
L('Writing: Writing Riddles and Jokes',
  'Grade 3 Language strand: a riddle is a puzzling question with a clever answer, and a joke often uses wordplay or a surprising twist to make the audience laugh.',
  [('A riddle is a puzzling question with a ___ answer.', ['Clever', 'Completely obvious answer with no cleverness involved', 'A concept unrelated to solving a puzzle', 'Answer that has no connection to the question at all'], 0),
   ('A joke often uses wordplay or a ___ to make the audience laugh.', ['Surprising twist', 'A concept unrelated to humour', 'A completely predictable, boring ending', 'A serious, sad ending with no humour at all'], 0),
   ('Which is an example of a riddle?', ['What has hands but cannot clap? A clock.', 'A statement with a completely obvious, unclever answer', 'A concept unrelated to puzzling questions', 'A sentence with no question or answer at all'], 0),
   ('Why might a good riddle keep its answer hidden until the very end?', ['Keeping the answer hidden builds curiosity and makes solving the riddle more fun and surprising', 'Hiding the answer has no connection to how a riddle works', 'A riddle should always reveal its answer at the very beginning', 'This concept has no relevance to writing an engaging riddle'], 0),
   ('Why does wordplay, like using a word with two meanings, often make a joke funny?', ['The unexpected second meaning creates a surprising twist that makes the audience laugh', 'Wordplay never has any connection to what makes a joke funny', 'A joke can never use more than one meaning of a word', 'This concept has no relevance to understanding humour in writing'], 0)]),
M('Measurement: Comparing and Ordering Length, Mass, and Capacity',
  'Grade 3 Math strand: comparing and ordering measurements means arranging objects from least to greatest, or greatest to least, based on their length, mass, or capacity.',
  [('Comparing and ordering measurements means arranging objects from least to greatest, or ___.', ['Greatest to least', 'Randomly, with no particular order at all', 'A concept unrelated to measurement', 'Only alphabetically, with no connection to size'], 0),
   ('If a pencil is 15 cm long and a marker is 12 cm long, which object has the greater length?', ['The pencil', 'The marker', 'Both objects are exactly the same length', 'Length cannot be compared between these two objects'], 0),
   ('When ordering objects by mass from lightest to heaviest, which should be listed first?', ['The object with the smallest mass', 'The object with the largest mass', 'A concept unrelated to ordering by mass', 'The object that was measured most recently'], 0),
   ('Why is it important to use the same unit of measurement when comparing the length of two different objects?', ['Using the same unit allows for a fair and accurate comparison between the two objects', 'The unit of measurement used never affects how objects are compared', 'Objects can always be compared accurately even using completely different units', 'This concept has no relevance to comparing measurements'], 0),
   ('If three containers hold 2 litres, 5 litres, and 3 litres of water, what is the correct order from least to greatest capacity?', ['2 litres, 3 litres, 5 litres', '5 litres, 3 litres, 2 litres', '3 litres, 2 litres, 5 litres', '2 litres, 5 litres, 3 litres'], 0)]),
Sc('Science: Earth’s Layers: Crust, Mantle, and Core',
   'Grade 3 Science strand: the Earth is made up of layers, including the crust on the outside, the mantle beneath it, and the core at the very centre of the planet.',
   [('The Earth is made up of layers, including the crust, the mantle, and the ___.', ['Core', 'Atmosphere, with no connection to the Earth’s internal layers', 'A concept unrelated to the structure of the Earth', 'Ocean, with no connection to the Earth’s internal structure'], 0),
    ('The crust is the layer of the Earth found ___.', ['On the outside', 'At the very centre of the planet', 'A concept unrelated to the Earth’s layers', 'Floating above the Earth’s surface, with no connection to it'], 0),
    ('Which layer of the Earth is found at the very centre of the planet?', ['The core', 'The crust, which is the outermost layer', 'The mantle, which is found beneath the crust', 'A concept unrelated to the Earth’s structure'], 0),
    ('Why is the crust considered the layer of the Earth that people are most familiar with?', ['It is the outer layer where people live, build, and walk on every day', 'People never interact with the Earth’s crust in any way', 'The crust has no connection to daily life on Earth', 'This concept has no relevance to understanding the Earth’s layers'], 0),
    ('Why might scientists find it difficult to directly study the Earth’s core?', ['The core is located extremely deep beneath the surface, making it very hard to reach directly', 'The core is located right at the surface of the Earth, making it easy to study', 'Scientists have no interest in studying the Earth’s internal layers', 'This concept has no relevance to understanding Earth’s structure'], 0)]),
SS('Social Studies: Ontario’s Farmland and Agriculture Today',
   'Grade 3 Social Studies strand: agriculture is an important part of Ontario’s economy today, with farmland used to grow crops and raise animals that provide food for communities across the province.',
   [('Farmland in Ontario is used to grow crops and raise animals that provide ___ for communities.', ['Food', 'A concept unrelated to what farms produce', 'Only decorations, with no connection to farming', 'Nothing useful at all, since farms serve no purpose'], 0),
    ('Agriculture is an important part of Ontario’s ___ today.', ['Economy', 'A concept unrelated to how Ontario supports itself', 'Weather system, with no connection to farming', 'Government structure, with no connection to farming'], 0),
    ('Which is an example of a crop that might be grown on Ontario farmland?', ['Corn', 'A concept unrelated to farming or agriculture', 'A material that cannot be grown on farmland', 'An item unrelated to food production'], 0),
    ('Why might farmland be considered an important resource for a province like Ontario?', ['It allows the province to produce food for its own communities and potentially for other places too', 'Farmland has no connection to producing food or supporting an economy', 'Provinces never need farmland to support their communities', 'This concept has no relevance to understanding Ontario’s economy'], 0),
    ('Why might farmers in Ontario need to consider factors like soil quality and weather when growing crops?', ['These factors can significantly affect how well crops grow and how much food is produced', 'Soil quality and weather have no effect on farming success', 'Crops always grow the exact same way no matter the conditions', 'This concept has no relevance to understanding agriculture'], 0)])]),

day(69, [
L('Reading: Text Structure — Problem and Solution',
  'Grade 3 Language strand: some non-fiction texts are organized using a problem-and-solution structure, where the text first describes a problem and then explains one or more ways it might be solved.',
  [('A problem-and-solution text structure first describes a problem and then explains ___.', ['One or more ways it might be solved', 'A completely unrelated topic with no connection to the problem', 'Nothing further, since the text always ends at the problem', 'Only another, different problem, with no solution given'], 0),
   ('Which is an example of a problem that might be described in a problem-and-solution text?', ['Litter is polluting a local park', 'A concept unrelated to identifying a problem', 'A sentence with no issue described at all', 'A topic that has no connection to problem-solving'], 0),
   ('Why might an author use a problem-and-solution structure to organize information about pollution?', ['It clearly shows both the issue and possible ways people could help address it', 'This structure never helps organize information about an issue', 'A problem-and-solution structure has no connection to informational writing', 'This concept has no relevance to understanding non-fiction texts'], 0),
   ('Why is it helpful for a reader to recognize a problem-and-solution structure while reading?', ['It helps the reader understand how the information in the text is organized and connected', 'Recognizing text structure never helps a reader understand a text', 'A problem-and-solution structure has no connection to reading comprehension', 'This concept has no relevance to understanding non-fiction texts'], 0),
   ('Which signal word might suggest a text is using a problem-and-solution structure?', ['Solution', 'A word entirely unrelated to organizing a text', 'A word that only ever appears in a story with no informational purpose', 'A concept unrelated to how texts are structured'], 0)]),
M('Multiplication: Doubling and Halving Strategy',
  'Grade 3 Math strand: the doubling and halving strategy makes some multiplication problems easier by doubling one factor and halving the other, since this keeps the product the same.',
  [('The doubling and halving strategy makes multiplication easier by doubling one factor and ___ the other.', ['Halving', 'Also doubling, with no connection to halving', 'A concept unrelated to changing factors in multiplication', 'Multiplying, with no connection to halving a number'], 0),
   ('Using the doubling and halving strategy, 16 × 5 can be rewritten as ___.', ['8 × 10', '32 × 2.5', '16 × 10', '8 × 5'], 0),
   ('Why does doubling one factor and halving the other keep the product the same?', ['The increase from doubling one number balances out the decrease from halving the other', 'Doubling and halving always change the final product', 'This strategy has no connection to how multiplication works', 'The product always changes no matter how the factors are adjusted'], 0),
   ('Using the doubling and halving strategy, what is 14 × 5 rewritten as an easier problem?', ['7 × 10', '28 × 10', '7 × 5', '14 × 10'], 0),
   ('Why might the doubling and halving strategy be especially useful when one factor is an even number close to a friendly number like 10 or 20?', ['Halving an even number often creates a simpler, more manageable multiplication problem', 'This strategy is never useful for solving multiplication problems', 'Even numbers can never be halved evenly', 'This concept has no connection to choosing helpful multiplication strategies'], 0)]),
Sc('Science: Technology Inspired by Nature (Biomimicry)',
   'Grade 3 Science strand: biomimicry means designing new technology by imitating ideas found in nature, such as designing swimsuits inspired by shark skin or building materials inspired by spider silk.',
   [('Biomimicry means designing new technology by ___ ideas found in nature.', ['Imitating', 'Completely ignoring, with no connection to nature', 'A concept unrelated to inventing new technology', 'Destroying, with no connection to design or invention'], 0),
    ('Which is an example of biomimicry?', ['A swimsuit designed to imitate the texture of shark skin', 'A concept unrelated to nature-inspired design', 'An invention with no connection to any living thing', 'A technology that has never been inspired by nature'], 0),
    ('Why might engineers study spider silk when trying to design a new strong material?', ['Spider silk is naturally very strong and lightweight, offering useful ideas for new designs', 'Spider silk has no useful properties that could inspire new materials', 'Engineers never look to nature when designing new materials', 'This concept has no relevance to understanding biomimicry'], 0),
    ('Why is biomimicry considered a useful approach to solving design problems?', ['Nature has developed many effective solutions over a very long time that people can learn from', 'Nature has no useful solutions that could help with human design problems', 'Biomimicry never actually leads to any useful inventions', 'This concept has no relevance to understanding technology and science'], 0),
    ('Why might a builder study how honeycomb is structured when designing a lightweight but strong material?', ['A honeycomb’s hexagonal pattern is naturally strong while using very little material', 'Honeycomb structures have no connection to strength or building design', 'Studying nature never provides any useful engineering ideas', 'This concept has no relevance to understanding biomimicry'], 0)]),
SS('Social Studies: Canada’s Currency: Coins and Bills',
   'Grade 3 Social Studies strand: Canada’s currency includes coins, like the loonie and toonie, and paper bills, each showing important Canadian symbols and images.',
   [('Canada’s currency includes coins and ___.', ['Paper bills', 'A concept unrelated to Canadian money', 'Only foreign money, with no connection to Canada', 'Nothing else, since coins are the only form of currency'], 0),
    ('The Canadian one-dollar coin is commonly called the ___.', ['Loonie', 'Toonie, which is the two-dollar coin instead', 'Dime, which is a much smaller coin', 'A concept unrelated to Canadian currency'], 0),
    ('Canadian coins and bills often show important ___.', ['Canadian symbols and images', 'A concept unrelated to Canadian identity', 'Only random, unrelated pictures', 'Foreign symbols with no connection to Canada'], 0),
    ('Why might Canadian currency feature images of important people, places, or symbols?', ['These images can represent and celebrate parts of Canada’s history, identity, and achievements', 'Currency images have no connection to a country’s identity', 'Canadian currency never includes any meaningful images or symbols', 'This concept has no relevance to understanding Canadian culture'], 0),
    ('Why is it useful for students to learn about the different forms of Canadian currency?', ['It helps build understanding of how money is used and represented in Canada', 'Learning about currency provides no useful understanding of Canada', 'Currency has no connection to everyday life in Canada', 'This concept has no relevance to social studies learning'], 0)])]),

day(70, [
L('Review: Idioms, Grammar, and Reading Strategies',
  'Grade 3 Language strand review: this lesson revisits idioms and expressions, contractions, homophones, quotation marks in dialogue, and making predictions while reading.',
  [('The idiom “it’s raining cats and dogs” really means ___.', ['It is raining very hard', 'Cats and dogs are falling from the sky', 'A phrase unrelated to weather', 'The weather is calm and sunny'], 0),
   ('The contraction “don’t” is a shortened form of ___.', ['Do not', 'Does not', 'Did not', 'A phrase unrelated to “don’t”'], 0),
   ('Which pair of words are homophones?', ['Flower and flour', 'Happy and sad', 'Big and small', 'A pair of words unrelated in sound'], 0),
   ('Making a prediction means using clues to make a sensible ___ about what might happen next.', ['Guess', 'Concept unrelated to reading a story', 'Random decision, with no connection to any clues', 'Rule that will always be exactly correct with no exceptions'], 0),
   ('Why is it useful to review reading and language skills like idioms, contractions, and predictions together?', ['These skills all help readers understand language and texts more deeply', 'These skills have no connection to each other', 'Review is never useful for language learning', 'Each skill must always be learned with no connection to any other'], 0)]),
M('Review: Division, Fractions, and Multiplication Strategies',
  'Grade 3 Math strand review: this lesson revisits division with remainders, multiplying multiples of ten, subtracting fractions with the same denominator, and the doubling and halving strategy.',
  [('What is 13 ÷ 4, including the remainder?', ['3 remainder 1', '4 remainder 1', '3 remainder 2', '4 remainder 0'], 0),
   ('What is 3 × 20?', ['60', '23', '6', '600'], 0),
   ('What is 4/5 − 2/5?', ['2/5', '2/10', '6/5', '2/0'], 0),
   ('Using the doubling and halving strategy, 16 × 5 can be rewritten as ___.', ['8 × 10', '32 × 2.5', '16 × 10', '8 × 5'], 0),
   ('Why is it useful to review division, fractions, and multiplication strategies together?', ['These related math skills reinforce each other for a stronger overall understanding', 'These topics have no connection to each other', 'Review is never useful in math', 'Each topic must be learned in complete isolation'], 0)]),
Sc('Review: Simple Machines, Weather, and Earth Science',
   'Grade 3 Science strand review: this lesson revisits the screw and wedge, weather instruments, vertebrates and invertebrates, and Earth’s layers.',
   [('A screw is a simple machine made from an inclined plane wrapped around a ___.', ['Pole', 'Flat surface, with no connection to a pole', 'A concept unrelated to simple machines', 'Wheel, which is a completely different simple machine'], 0),
    ('A rain gauge is used to measure ___.', ['How much rain has fallen', 'Wind direction, with no connection to rain', 'Air temperature, with no connection to rainfall', 'A concept unrelated to weather measurement'], 0),
    ('Invertebrates are animals that ___.', ['Do not have a backbone', 'Always have a backbone, with no exceptions', 'A concept unrelated to animal classification', 'Can never be classified in any way'], 0),
    ('The Earth is made up of layers, including the crust, the mantle, and the ___.', ['Core', 'Atmosphere, with no connection to the Earth’s internal layers', 'A concept unrelated to the structure of the Earth', 'Ocean, with no connection to the Earth’s internal structure'], 0),
    ('Why is it useful to review machines, weather, and Earth’s structure together?', ['It reinforces how these science concepts each help explain the physical world around us', 'These topics have no connection to each other', 'Review is never useful in science', 'Each topic must be studied with no connection to the others'], 0)]),
SS('Review: Government, Geography, and Economy',
   'Grade 3 Social Studies strand review: this lesson revisits Canada’s provinces and capitals, elections, entrepreneurs, and Ontario’s farmland and agriculture.',
   [('What is the capital city of Ontario?', ['Toronto', 'Ottawa', 'Montreal', 'Vancouver'], 0),
    ('An election is a process where citizens vote to choose their ___.', ['Leaders', 'Favourite sports team, with no connection to government', 'A concept unrelated to government', 'Weather forecast for the week'], 0),
    ('An entrepreneur is a person who ___.', ['Starts their own business', 'Never takes any risks with a new idea', 'A concept unrelated to starting a business', 'Only works for someone else’s existing business'], 0),
    ('Farmland in Ontario is used to grow crops and raise animals that provide ___ for communities.', ['Food', 'A concept unrelated to what farms produce', 'Only decorations, with no connection to farming', 'Nothing useful at all, since farms serve no purpose'], 0),
    ('Why is it useful to review government, economy, and geography topics together at this point in the year?', ['It helps students see how these different aspects of Canada and Ontario connect and support one another', 'These topics have no meaningful connection to each other', 'Bringing lessons together never provides any additional understanding', 'Each topic must always be learned with no connection to any other'], 0)])]),
]

def _rebalance_answer_positions(days, seed=20260810):
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
    _rebalance_answer_positions(g3_61_70)
    append_to(3, g3_61_70)
