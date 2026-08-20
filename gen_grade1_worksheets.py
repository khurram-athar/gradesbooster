#!/usr/bin/env python3
"""Grade 1 standalone optional-worksheet content -- Project Plan item 8.

Generates data/grade1_worksheets.ts: 40 worksheets total (10 per subject x 4
subjects: Language, Math, Science, SocialStudies), exactly 15 free-response
(fr()) questions each, using the shared helpers in gen_worksheets.py.

This is a NEW, separate content pipeline from the day-based curriculum
(data/grade1.ts, the 187-day lesson sequence) -- that file is untouched by
this script.

Grade 1 uses free-response only (per gen_worksheets.py docstring), matching
the style of the required 3-item worksheet field already embedded in each
day of grade1.ts. Each subject's 10 worksheets are organized around 10
distinct practice themes/strands spanning the grade, roughly progressing
from foundational to more advanced skills within that subject. These are
supplementary practice worksheets, not new lessons, so overlap with topics
already covered across the 187 days is expected and fine.

No embedded ASCII double-quote or straight apostrophe characters are used
anywhere in title/q text -- contractions and possessives are avoided
entirely (e.g. "does not" not "doesnt", "the students book" instead of a
possessive with an apostrophe), matching this project's convention, since
this text gets embedded directly into TypeScript string literals.
"""
import sys

sys.path.insert(0, '.')
from gen_worksheets import fr, worksheet, write_worksheets

all_worksheets = []

# ---------------------------------------------------------------------------
# Language (10 worksheets)
# ---------------------------------------------------------------------------

all_worksheets.append(worksheet('Language', 1, 'Letter Sounds and the Alphabet', [
    fr('Say the sound the letter B makes.'),
    fr('Say the sound the letter M makes.'),
    fr('Name a word that starts with the letter S.'),
    fr('Name a word that starts with the letter T.'),
    fr('Which letter comes right after D in the alphabet.'),
    fr('Which letter comes right before K in the alphabet.'),
    fr('Name a word that starts with the letter F.'),
    fr('Say the sound the letter P makes.'),
    fr('Which letter comes at the very beginning of the alphabet.'),
    fr('Which letter comes at the very end of the alphabet.'),
    fr('Name a word that starts with the letter H.'),
    fr('Say the sound the letter R makes.'),
    fr('Name two letters that come between G and L.'),
    fr('Write the letter that starts the word Dog.'),
    fr('Write the letter that starts the word Cat.'),
]))

all_worksheets.append(worksheet('Language', 2, 'Short Vowel Words', [
    fr('Say a word that has the short a sound like in cat.'),
    fr('Say a word that has the short e sound like in bed.'),
    fr('Say a word that has the short i sound like in pig.'),
    fr('Say a word that has the short o sound like in hot.'),
    fr('Say a word that has the short u sound like in sun.'),
    fr('Change the first letter of hat to make a new short a word.'),
    fr('Change the first letter of pig to make a new short i word.'),
    fr('Name a word that rhymes with dog using the short o sound.'),
    fr('Name a word that rhymes with cup using the short u sound.'),
    fr('Name a word that rhymes with bed using the short e sound.'),
    fr('Sort these letters to make a short a word: t, a, m.'),
    fr('Sort these letters to make a short o word: p, o, t.'),
    fr('Name a short vowel word with three letters.'),
    fr('Say a sentence using a short i word.'),
    fr('Say a sentence using a short u word.'),
]))

all_worksheets.append(worksheet('Language', 3, 'Long Vowel Words and Vowel Teams', [
    fr('Say a word with the long a sound like in cake.'),
    fr('Say a word with the long e sound like in tree.'),
    fr('Say a word with the long i sound like in bike.'),
    fr('Say a word with the long o sound like in boat.'),
    fr('Say a word with the long u sound like in cube.'),
    fr('Name a vowel team that makes the long e sound.'),
    fr('Name a vowel team that makes the long a sound.'),
    fr('Give a word that uses the vowel team oa.'),
    fr('Give a word that uses the vowel team ee.'),
    fr('Give a word that uses a silent e to make a long vowel sound.'),
    fr('Compare the words hop and hope. Which one has a long vowel sound.'),
    fr('Compare the words cap and cape. Which one has a long vowel sound.'),
    fr('Say a sentence using a long o word.'),
    fr('Say a sentence using a long e word.'),
    fr('Name a word that rhymes with rain using the long a sound.'),
]))

all_worksheets.append(worksheet('Language', 4, 'Blending and Segmenting Sounds', [
    fr('Blend these sounds together: c, a, t.'),
    fr('Blend these sounds together: s, u, n.'),
    fr('Segment the word dog into its separate sounds.'),
    fr('Segment the word fish into its separate sounds.'),
    fr('How many sounds are in the word run.'),
    fr('How many sounds are in the word stop.'),
    fr('Blend these sounds together: b, i, g.'),
    fr('Say the first sound in the word map.'),
    fr('Say the last sound in the word map.'),
    fr('Say the middle sound in the word pin.'),
    fr('Blend these sounds together: sh, i, p.'),
    fr('Segment the word frog into its separate sounds.'),
    fr('Say a word that starts with the same sound as sun.'),
    fr('Say a word that ends with the same sound as cat.'),
    fr('How many sounds are in the word chip.'),
]))

all_worksheets.append(worksheet('Language', 5, 'Sight Words in Sentences', [
    fr('Use the word the in a sentence.'),
    fr('Use the word said in a sentence.'),
    fr('Use the word was in a sentence.'),
    fr('Use the word they in a sentence.'),
    fr('Use the word have in a sentence.'),
    fr('Use the word like in a sentence.'),
    fr('Use the word are in a sentence.'),
    fr('Use the word with in a sentence.'),
    fr('Use the word for in a sentence.'),
    fr('Use the word you in a sentence.'),
    fr('Name a sight word that has three letters.'),
    fr('Name a sight word that has four letters.'),
    fr('Write a short sentence using two sight words.'),
    fr('Which sight word means the opposite of yes.'),
    fr('Which sight word comes at the start of many questions, like What or Who.'),
]))

all_worksheets.append(worksheet('Language', 6, 'Story Elements: Characters and Setting', [
    fr('Who is the main character in your favourite story.'),
    fr('Where does your favourite story take place.'),
    fr('Name a character from a story you have read.'),
    fr('Describe the setting of a story you know well.'),
    fr('Is the setting of your story indoors or outdoors.'),
    fr('Name one thing the main character wants in the story.'),
    fr('Name a problem the main character faces in a story.'),
    fr('How does the main character solve the problem.'),
    fr('Name another character who helps the main character.'),
    fr('Describe how the main character feels at the start of the story.'),
    fr('Describe how the main character feels at the end of the story.'),
    fr('What time of day does the story take place.'),
    fr('Name a story that takes place in a forest.'),
    fr('Name a story that takes place at school.'),
    fr('Why is the setting important to a story.'),
]))

all_worksheets.append(worksheet('Language', 7, 'Sequencing Events in a Story', [
    fr('What happened first in a story you read recently.'),
    fr('What happened next in that story.'),
    fr('What happened last in that story.'),
    fr('Name a word that shows something happened first, like First or Before.'),
    fr('Name a word that shows something happened last, like Finally or After.'),
    fr('Put these steps in order: wake up, eat breakfast, go to school.'),
    fr('Put these steps in order: plant a seed, water it, watch it grow.'),
    fr('What happens in the middle of most stories.'),
    fr('Why is it important to put events in the correct order.'),
    fr('Retell a story you know using the words first, next, and last.'),
    fr('Name an event that happens at the beginning of a school day.'),
    fr('Name an event that happens at the end of a school day.'),
    fr('Describe the order of steps for making a sandwich.'),
    fr('Describe the order of steps for brushing your teeth.'),
    fr('Why might a story be confusing if the events are out of order.'),
]))

all_worksheets.append(worksheet('Language', 8, 'Nouns and Verbs', [
    fr('Name a noun that is a person.'),
    fr('Name a noun that is a place.'),
    fr('Name a noun that is a thing.'),
    fr('Name a verb that describes something you do at recess.'),
    fr('Name a verb that describes something you do at home.'),
    fr('Pick out the noun in this sentence: The dog runs fast.'),
    fr('Pick out the verb in this sentence: The dog runs fast.'),
    fr('Name a noun that is an animal.'),
    fr('Name a verb that means to move quickly.'),
    fr('Say a sentence with one noun and one verb.'),
    fr('Name a noun that names a food.'),
    fr('Name a verb that describes something a bird can do.'),
    fr('Is the word jump a noun or a verb.'),
    fr('Is the word teacher a noun or a verb.'),
    fr('Say a sentence using the verb sing.'),
]))

all_worksheets.append(worksheet('Language', 9, 'Writing Simple Sentences', [
    fr('Write a sentence that tells what you did this morning.'),
    fr('Write a sentence about your favourite animal.'),
    fr('Write a sentence that starts with a capital letter.'),
    fr('Write a sentence that ends with a period.'),
    fr('Write a question that ends with a question mark.'),
    fr('Write a sentence with three or more words.'),
    fr('Write a sentence about the weather today.'),
    fr('Write a sentence using the word happy.'),
    fr('Write a sentence using the word big.'),
    fr('Write a sentence about your family.'),
    fr('Write a sentence that tells where you live.'),
    fr('Write a sentence using the word fast.'),
    fr('Fix this sentence so it starts with a capital letter: the sun is bright.'),
    fr('Add an end mark to this sentence: I like to read'),
    fr('Write a sentence describing your favourite toy.'),
]))

all_worksheets.append(worksheet('Language', 10, 'Rhyming Words and Word Families', [
    fr('Name a word that rhymes with cat.'),
    fr('Name a word that rhymes with dog.'),
    fr('Name a word that rhymes with sun.'),
    fr('Name a word that rhymes with hen.'),
    fr('Name a word that rhymes with pig.'),
    fr('Name three words in the -at family, like cat, hat, and bat.'),
    fr('Name three words in the -og family, like dog, log, and fog.'),
    fr('Name three words in the -an family, like man, fan, and pan.'),
    fr('Name a word that does not rhyme with cake: rake, lake, or dog.'),
    fr('Add a new beginning sound to og to make a rhyming word.'),
    fr('Add a new beginning sound to ing to make a rhyming word.'),
    fr('Name a word that rhymes with tree.'),
    fr('Name a word that rhymes with book.'),
    fr('Say a short rhyme using two words from the -at family.'),
    fr('Why do rhyming words help us learn to read new words.'),
]))

# ---------------------------------------------------------------------------
# Math (10 worksheets)
# ---------------------------------------------------------------------------

all_worksheets.append(worksheet('Math', 1, 'Counting and Number Order to 100', [
    fr('Count out loud from 1 to 20.'),
    fr('What number comes right after 45.'),
    fr('What number comes right before 60.'),
    fr('Count by tens from 10 to 100.'),
    fr('What number comes between 27 and 29.'),
    fr('Write the numbers from 1 to 10 in order.'),
    fr('What is the largest two digit number you can think of.'),
    fr('What is the smallest two digit number you can think of.'),
    fr('Count backward from 10 to 1.'),
    fr('What number comes right after 99.'),
    fr('Put these numbers in order from smallest to largest: 14, 8, 21.'),
    fr('What number comes right before 100.'),
    fr('Count by fives from 5 to 50.'),
    fr('Which number is greater, 38 or 83.'),
    fr('Write the number that is ten more than 40.'),
]))

all_worksheets.append(worksheet('Math', 2, 'Place Value: Tens and Ones', [
    fr('How many tens and ones are in the number 34.'),
    fr('How many tens and ones are in the number 58.'),
    fr('What number has 3 tens and 2 ones.'),
    fr('What number has 7 tens and 0 ones.'),
    fr('Break the number 46 into tens and ones.'),
    fr('Break the number 21 into tens and ones.'),
    fr('Which digit in the number 65 is in the tens place.'),
    fr('Which digit in the number 65 is in the ones place.'),
    fr('What is 4 tens plus 5 ones equal to.'),
    fr('Add ten to the number 23.'),
    fr('Add one to the number 39.'),
    fr('What number has 9 tens and 9 ones.'),
    fr('Which is greater, a number with 5 tens or a number with 3 tens.'),
    fr('Show the number 72 using tens and ones.'),
    fr('What number is one ten more than 50.'),
]))

all_worksheets.append(worksheet('Math', 3, 'Addition Facts to 20', [
    fr('What is 4 plus 3.'),
    fr('What is 6 plus 5.'),
    fr('What is 8 plus 2.'),
    fr('What is 9 plus 6.'),
    fr('What is 7 plus 7.'),
    fr('What is 10 plus 5.'),
    fr('What is 3 plus 9.'),
    fr('What is 12 plus 4.'),
    fr('What is 6 plus 6.'),
    fr('What is 11 plus 2.'),
    fr('If you have 8 apples and get 5 more, how many apples do you have.'),
    fr('If you have 6 stickers and get 9 more, how many stickers do you have.'),
    fr('What two numbers add up to make 10.'),
    fr('What two numbers add up to make 15.'),
    fr('Write an addition sentence for 7 plus 8.'),
]))

all_worksheets.append(worksheet('Math', 4, 'Subtraction Facts to 20', [
    fr('What is 9 minus 4.'),
    fr('What is 12 minus 5.'),
    fr('What is 15 minus 7.'),
    fr('What is 20 minus 6.'),
    fr('What is 10 minus 3.'),
    fr('What is 18 minus 9.'),
    fr('What is 14 minus 8.'),
    fr('If you have 12 crayons and give away 5, how many crayons are left.'),
    fr('If you have 16 candies and eat 7, how many candies are left.'),
    fr('What is 8 minus 8.'),
    fr('What is 13 minus 6.'),
    fr('Write a subtraction sentence for 17 minus 9.'),
    fr('What number minus 5 equals 5.'),
    fr('What number minus 3 equals 10.'),
    fr('What is 19 minus 10.'),
]))

all_worksheets.append(worksheet('Math', 5, 'Comparing Numbers', [
    fr('Which is greater, 12 or 21.'),
    fr('Which is smaller, 45 or 54.'),
    fr('Use greater than, less than, or equal to compare 30 and 30.'),
    fr('Use greater than, less than, or equal to compare 18 and 81.'),
    fr('Order these numbers from smallest to largest: 9, 90, 19.'),
    fr('Order these numbers from largest to smallest: 66, 6, 60.'),
    fr('Which number is closer to 50, 48 or 55.'),
    fr('Is 25 greater than or less than 52.'),
    fr('Name a number that is greater than 40 but less than 50.'),
    fr('Name a number that is less than 10.'),
    fr('Which is greater, 3 tens or 30 ones.'),
    fr('Compare the number of days in a week to the number of fingers on one hand.'),
    fr('Which is bigger, a group of 7 apples or a group of 12 apples.'),
    fr('Name two numbers that are equal to each other.'),
    fr('Which number is farthest from 100, 10 or 90.'),
]))

all_worksheets.append(worksheet('Math', 6, 'Shapes: 2D and 3D', [
    fr('Name a shape with three sides.'),
    fr('Name a shape with four equal sides.'),
    fr('Name a shape with no straight sides.'),
    fr('How many sides does a rectangle have.'),
    fr('How many corners does a triangle have.'),
    fr('Name a 3D shape that looks like a ball.'),
    fr('Name a 3D shape that looks like a box.'),
    fr('Name a 3D shape that can roll and stack, like a can.'),
    fr('How many faces does a cube have.'),
    fr('Name an object in your classroom shaped like a rectangle.'),
    fr('Name an object in your classroom shaped like a circle.'),
    fr('What shape do you get if you cut a square in half diagonally.'),
    fr('Name a shape with five sides.'),
    fr('Compare a square and a rectangle. How are they alike.'),
    fr('Compare a square and a rectangle. How are they different.'),
]))

all_worksheets.append(worksheet('Math', 7, 'Measurement: Length and Height', [
    fr('Name something in your classroom that is longer than your pencil.'),
    fr('Name something in your classroom that is shorter than your pencil.'),
    fr('How many paper clips long is your notebook, roughly.'),
    fr('Which is taller, a chair or a table.'),
    fr('Which is longer, a pencil or a ruler.'),
    fr('Name a tool we use to measure length.'),
    fr('Put these three objects in order from shortest to longest: a crayon, a book, a door.'),
    fr('How tall are you compared to your best friend.'),
    fr('Name something that is about one metre long.'),
    fr('Name something that is very short, less than an inch.'),
    fr('Which is heavier, a feather or a rock.'),
    fr('Compare the length of your arm to the length of your leg.'),
    fr('Name an object that would be measured in centimetres.'),
    fr('Why do we use measuring tools instead of guessing.'),
    fr('Order these from shortest to tallest: a mouse, a dog, a giraffe.'),
]))

all_worksheets.append(worksheet('Math', 8, 'Telling Time to the Hour and Half Hour', [
    fr('What time is shown when the hour hand points to 3 and the minute hand points to 12.'),
    fr('What time is shown when the hour hand points to 7 and the minute hand points to 12.'),
    fr('Where does the minute hand point when it is half past the hour.'),
    fr('What time is it when a clock shows 9 oclock.'),
    fr('What time is it when a clock shows half past 4.'),
    fr('Name an activity you do in the morning around 8 oclock.'),
    fr('Name an activity you do in the evening around 7 oclock.'),
    fr('How many hours are there in one day.'),
    fr('How many minutes are in one hour.'),
    fr('What time comes half an hour after 2 oclock.'),
    fr('What time comes one hour after 5 oclock.'),
    fr('Draw hands on a clock to show 6 oclock.'),
    fr('Draw hands on a clock to show half past 10.'),
    fr('Which is longer, one hour or one half hour.'),
    fr('What time do you usually go to bed.'),
]))

all_worksheets.append(worksheet('Math', 9, 'Money: Coins and Bills', [
    fr('Name the coin that is worth one cent.'),
    fr('Name the coin that is worth five cents.'),
    fr('Name the coin that is worth ten cents.'),
    fr('Name the coin that is worth twenty five cents.'),
    fr('How many nickels make ten cents.'),
    fr('How many dimes make twenty cents.'),
    fr('How many pennies make one dollar.'),
    fr('If you have two dimes and one nickel, how much money do you have.'),
    fr('If you have one quarter and one dime, how much money do you have.'),
    fr('Name the bill that is worth five dollars.'),
    fr('Name the bill that is worth ten dollars.'),
    fr('How much is three quarters worth in total.'),
    fr('If a toy costs fifteen cents, name coins that add up to that amount.'),
    fr('Which is worth more, a dime or a nickel.'),
    fr('How many one dollar coins make five dollars.'),
]))

all_worksheets.append(worksheet('Math', 10, 'Patterns and Skip Counting', [
    fr('What comes next in this pattern: red, blue, red, blue, red.'),
    fr('What comes next in this pattern: 2, 4, 6, 8.'),
    fr('Skip count by twos from 2 to 20.'),
    fr('Skip count by fives from 5 to 50.'),
    fr('Skip count by tens from 10 to 100.'),
    fr('What comes next in this pattern: circle, square, circle, square.'),
    fr('Create your own repeating pattern using two shapes.'),
    fr('What comes next in this pattern: 5, 10, 15, 20.'),
    fr('What is the rule for this pattern: 1, 3, 5, 7.'),
    fr('Fill in the missing number: 2, 4, __, 8.'),
    fr('Fill in the missing number: 10, 20, __, 40.'),
    fr('What comes next in this pattern: A, B, A, B, A.'),
    fr('Create a growing pattern using blocks of different sizes.'),
    fr('Skip count by twos starting at an odd number, like 1.'),
    fr('What comes next in this pattern: clap, stomp, clap, stomp.'),
]))

# ---------------------------------------------------------------------------
# Science (10 worksheets)
# ---------------------------------------------------------------------------

all_worksheets.append(worksheet('Science', 1, 'Living and Non-Living Things', [
    fr('Name something that is living.'),
    fr('Name something that is non living.'),
    fr('How can you tell if something is alive.'),
    fr('Do plants need food and water to live.'),
    fr('Is a rock a living or non living thing.'),
    fr('Is a tree a living or non living thing.'),
    fr('Name one thing all living things need to survive.'),
    fr('Can non living things grow on their own.'),
    fr('Sort these into living and non living: a bird, a rock, a flower, a chair.'),
    fr('Do living things move on their own.'),
    fr('Name a living thing you might see in a park.'),
    fr('Name a non living thing you might see in a park.'),
    fr('Why is water considered non living even though living things need it.'),
    fr('Give an example of something that used to be living but no longer is.'),
    fr('Explain the difference between living and non living in your own words.'),
]))

all_worksheets.append(worksheet('Science', 2, 'Basic Needs of Plants', [
    fr('What do plants need to grow.'),
    fr('Why do plants need sunlight.'),
    fr('Why do plants need water.'),
    fr('What part of the plant takes in water from the soil.'),
    fr('What happens to a plant if it does not get enough water.'),
    fr('What happens to a plant if it does not get enough sunlight.'),
    fr('Name a place where plants can get good soil to grow in.'),
    fr('Why do plants need air to grow.'),
    fr('Name one plant that grows in a garden.'),
    fr('What might happen to a plant kept in a dark closet.'),
    fr('How often should most garden plants be watered.'),
    fr('Name the part of a plant that grows underground.'),
    fr('Name the part of a plant that makes food using sunlight.'),
    fr('Describe how you would take care of a classroom plant.'),
    fr('Why do farmers make sure their crops get enough water and sunlight.'),
]))

all_worksheets.append(worksheet('Science', 3, 'Basic Needs of Animals', [
    fr('What do animals need to survive.'),
    fr('Why do animals need food.'),
    fr('Why do animals need water.'),
    fr('Why do animals need shelter.'),
    fr('Name a place where a bird might build a shelter.'),
    fr('Name a place where a fish lives.'),
    fr('What might happen to an animal that cannot find food.'),
    fr('Name an animal that needs to drink water often.'),
    fr('How is a pet different from a wild animal in meeting its needs.'),
    fr('Name something a dog needs to stay healthy.'),
    fr('Why do animals need air to breathe.'),
    fr('Compare the needs of a fish and the needs of a bird.'),
    fr('Name a way people help pets meet their basic needs.'),
    fr('What do baby animals need from their parents.'),
    fr('Why is shelter important for animals during winter.'),
]))

all_worksheets.append(worksheet('Science', 4, 'Animal Habitats', [
    fr('What is a habitat.'),
    fr('Name an animal that lives in the forest.'),
    fr('Name an animal that lives in the ocean.'),
    fr('Name an animal that lives in the desert.'),
    fr('Name an animal that lives in the arctic.'),
    fr('Why do polar bears have thick fur.'),
    fr('Why do camels live well in the desert.'),
    fr('Name a habitat that has lots of trees.'),
    fr('Name a habitat that has lots of sand.'),
    fr('Why is a habitat important for an animal.'),
    fr('What might happen if an animal habitat is destroyed.'),
    fr('Name an animal that lives underground.'),
    fr('Name an animal that lives in a pond.'),
    fr('Compare a forest habitat and an ocean habitat.'),
    fr('Why do different animals live in different habitats.'),
]))

all_worksheets.append(worksheet('Science', 5, 'Life Cycles', [
    fr('What is a life cycle.'),
    fr('Name the stages of a butterfly life cycle.'),
    fr('Name the stages of a frog life cycle.'),
    fr('What comes first in a plant life cycle, a seed or a flower.'),
    fr('What is a caterpillar before it becomes a butterfly.'),
    fr('What is a tadpole before it becomes a frog.'),
    fr('Name an animal that hatches from an egg.'),
    fr('Name an animal that is born live, not from an egg.'),
    fr('What does a seed need to begin to grow.'),
    fr('Put these plant stages in order: seed, sprout, flower.'),
    fr('Why do living things go through a life cycle.'),
    fr('Compare the life cycle of a chicken and the life cycle of a frog.'),
    fr('What stage comes after an egg in a bird life cycle.'),
    fr('Name the stage of a butterfly life cycle when it is inside a chrysalis.'),
    fr('Why is a life cycle sometimes shown as a circle instead of a line.'),
]))

all_worksheets.append(worksheet('Science', 6, 'The Four Seasons', [
    fr('Name the four seasons in order.'),
    fr('What season comes after winter.'),
    fr('What season comes before winter.'),
    fr('Describe the weather in summer.'),
    fr('Describe the weather in winter.'),
    fr('Name one activity you do in the fall.'),
    fr('Name one activity you do in the spring.'),
    fr('What happens to some trees in the fall.'),
    fr('Why do people wear warm coats in winter.'),
    fr('Why do people wear light clothing in summer.'),
    fr('Name an animal that hibernates in winter.'),
    fr('What season is it when flowers start to bloom.'),
    fr('How does the weather change from summer to fall.'),
    fr('Name a holiday that happens in winter.'),
    fr('Describe your favourite season and why you like it.'),
]))

all_worksheets.append(worksheet('Science', 7, 'Weather and Sky', [
    fr('Name a type of weather you have seen this week.'),
    fr('What do we call frozen rain that falls from the sky.'),
    fr('What is fog.'),
    fr('What tool do we use to measure temperature.'),
    fr('What causes a rainbow to appear.'),
    fr('Name something you might wear on a rainy day.'),
    fr('Name something you might wear on a sunny day.'),
    fr('What is wind.'),
    fr('Why do we see clouds in the sky.'),
    fr('What is a thunderstorm.'),
    fr('Name a safe place to go during a thunderstorm.'),
    fr('How can you tell if it might rain by looking at the sky.'),
    fr('What is the difference between weather and climate.'),
    fr('Describe todays weather in your own words.'),
    fr('Why is it useful to check the weather before going outside.'),
]))

all_worksheets.append(worksheet('Science', 8, 'Materials and Their Properties', [
    fr('Name something made of wood.'),
    fr('Name something made of metal.'),
    fr('Name something made of plastic.'),
    fr('Which material would you use to make a raincoat, and why.'),
    fr('Which material bends easily, rubber or glass.'),
    fr('Which material is see through, glass or wood.'),
    fr('Name a material that floats in water.'),
    fr('Name a material that sinks in water.'),
    fr('Which material is best for building a strong bridge.'),
    fr('Compare the properties of paper and metal.'),
    fr('Why is glass used to make windows.'),
    fr('Why is rubber used to make tires.'),
    fr('Name a material that feels rough.'),
    fr('Name a material that feels smooth.'),
    fr('Sort these objects by material: a spoon, a shirt, a chair, a window.'),
]))

all_worksheets.append(worksheet('Science', 9, 'Simple Machines and Everyday Objects', [
    fr('What is a simple machine.'),
    fr('Name a simple machine you see at a playground.'),
    fr('How does a ramp make it easier to move something.'),
    fr('What simple machine helps you cut paper, found in scissors.'),
    fr('Name an object that uses a wheel.'),
    fr('How does a lever help us lift heavy things.'),
    fr('Name a simple machine used to raise a flag.'),
    fr('What simple machine is a doorknob an example of.'),
    fr('Why do we use simple machines.'),
    fr('Name a tool that uses a wedge shape, like an axe.'),
    fr('How is a seesaw an example of a lever.'),
    fr('Name a simple machine found on a bicycle.'),
    fr('Compare a ramp to a set of stairs.'),
    fr('Why might a wheelbarrow be easier to push than to carry the same load.'),
    fr('Name a simple machine you use at home.'),
]))

all_worksheets.append(worksheet('Science', 10, 'Taking Care of Our Environment', [
    fr('What does it mean to recycle.'),
    fr('Name something you can recycle.'),
    fr('Why is it important to reduce waste.'),
    fr('Name one way to save water at home.'),
    fr('Name one way to save electricity at home.'),
    fr('What can you do with old paper instead of throwing it away.'),
    fr('Why should we not litter outside.'),
    fr('Name a way to reuse an object instead of throwing it away.'),
    fr('How does planting trees help the environment.'),
    fr('Why is clean water important for people and animals.'),
    fr('Name one thing your class can do to help the environment.'),
    fr('Why should we turn off lights when leaving a room.'),
    fr('What happens to litter left in a park or forest.'),
    fr('Name an animal that could be harmed by pollution.'),
    fr('Describe one change you can make to help protect the earth.'),
]))

# ---------------------------------------------------------------------------
# Social Studies (10 worksheets)
# ---------------------------------------------------------------------------

all_worksheets.append(worksheet('SocialStudies', 1, 'My Family and Community', [
    fr('Name the members of your family.'),
    fr('What is a community.'),
    fr('Name a place in your community that you visit often.'),
    fr('Name one job someone in your family does at home.'),
    fr('Why is it important for family members to help each other.'),
    fr('Name a neighbour or friend who is part of your community.'),
    fr('Describe one way your family celebrates together.'),
    fr('Name a rule that your family follows at home.'),
    fr('Why do communities need people to work together.'),
    fr('Name a building in your community, like a school or library.'),
    fr('What makes your community special.'),
    fr('Name a way you can help your family at home.'),
    fr('Describe your neighbourhood in a few words.'),
    fr('Why is it important to be kind to people in your community.'),
    fr('Name one way your community celebrates together.'),
]))

all_worksheets.append(worksheet('SocialStudies', 2, 'Community Helpers', [
    fr('Name a community helper who puts out fires.'),
    fr('Name a community helper who keeps us safe from crime.'),
    fr('Name a community helper who helps sick people.'),
    fr('Name a community helper who teaches at school.'),
    fr('Name a community helper who delivers mail.'),
    fr('What does a farmer do for the community.'),
    fr('What does a dentist do for the community.'),
    fr('Why are community helpers important.'),
    fr('What tools does a firefighter use.'),
    fr('What tools does a doctor use.'),
    fr('Name a community helper who works at a grocery store.'),
    fr('Name a community helper who drives a bus.'),
    fr('Describe how a police officer helps keep people safe.'),
    fr('Which community helper would you call in an emergency.'),
    fr('Name a community helper you would like to be when you grow up.'),
]))

all_worksheets.append(worksheet('SocialStudies', 3, 'Rules and Responsibilities', [
    fr('Name one rule you follow at school.'),
    fr('Name one rule you follow at home.'),
    fr('Why do we need rules.'),
    fr('What is a responsibility.'),
    fr('Name one responsibility you have at home.'),
    fr('Name one responsibility you have at school.'),
    fr('What might happen if there were no rules at all.'),
    fr('Why is it important to line up quietly in the hallway.'),
    fr('Name a rule that keeps you safe on the playground.'),
    fr('Why do we take turns when playing games.'),
    fr('Name a responsibility that helps take care of a pet.'),
    fr('Describe how following rules helps a classroom run smoothly.'),
    fr('Name one classroom job you could be responsible for.'),
    fr('Why is it important to clean up after yourself.'),
    fr('What rule would you make to help your classroom.'),
]))

all_worksheets.append(worksheet('SocialStudies', 4, 'Maps and Directions', [
    fr('What is a map.'),
    fr('Name the four main directions on a compass.'),
    fr('What does a map key or legend show.'),
    fr('Point to the direction that is north on a compass.'),
    fr('Name a symbol you might see on a classroom map.'),
    fr('Why do maps use symbols instead of words.'),
    fr('Describe the path from your classroom to the front door.'),
    fr('What is the direction opposite of north.'),
    fr('What is the direction opposite of east.'),
    fr('Name a place you could find using a map.'),
    fr('Why are maps useful for travellers.'),
    fr('What is the difference between a map and a globe.'),
    fr('Name something you might find on a map of your school.'),
    fr('Describe how to find a location using a map key.'),
    fr('Why is it helpful to know the four directions.'),
]))

all_worksheets.append(worksheet('SocialStudies', 5, 'Canadian Symbols', [
    fr('Name the national animal of Canada.'),
    fr('What is on the Canadian flag.'),
    fr('What colours are on the Canadian flag.'),
    fr('Name the capital city of Canada.'),
    fr('What is the name of the maple leaf shown on the flag.'),
    fr('Name a Canadian symbol you might see on a coin.'),
    fr('Why do countries have symbols like flags.'),
    fr('Name a famous Canadian landmark.'),
    fr('What animal appears on the Canadian nickel.'),
    fr('Describe what the Canadian flag looks like.'),
    fr('Why is the beaver an important symbol in Canada.'),
    fr('Name something that represents Canada to you.'),
    fr('What is the name of the anthem sung in Canada.'),
    fr('Name a symbol found on Canadian money.'),
    fr('Why do we celebrate Canadian symbols.'),
]))

all_worksheets.append(worksheet('SocialStudies', 6, 'Canadian Holidays and Traditions', [
    fr('Name a Canadian holiday celebrated in July.'),
    fr('What do people celebrate on Canada Day.'),
    fr('Name a holiday celebrated in December.'),
    fr('Name a holiday celebrated in the fall to give thanks.'),
    fr('What do families often do together on Thanksgiving.'),
    fr('Name a tradition your family celebrates.'),
    fr('Why do Canadians celebrate Canada Day.'),
    fr('What colours do people often wear on Canada Day.'),
    fr('Name a winter holiday tradition.'),
    fr('Describe one way people celebrate Thanksgiving in Canada.'),
    fr('Why are holidays important to communities.'),
    fr('Name a holiday that celebrates a change in season.'),
    fr('What is one way your school celebrates a holiday.'),
    fr('Name a food often eaten during a Canadian holiday.'),
    fr('Why do different families celebrate holidays in different ways.'),
]))

all_worksheets.append(worksheet('SocialStudies', 7, 'Indigenous Peoples and Culture', [
    fr('Name a group of Indigenous peoples in Canada.'),
    fr('What is a powwow.'),
    fr('Name a tradition celebrated by Indigenous peoples.'),
    fr('Why is storytelling important in many Indigenous cultures.'),
    fr('Name an instrument used in Indigenous music.'),
    fr('What can we learn from Indigenous peoples about caring for the land.'),
    fr('Name a craft made by Indigenous peoples.'),
    fr('Why is it important to learn about Indigenous cultures.'),
    fr('Name something Indigenous peoples traditionally made from natural materials.'),
    fr('Describe one way Indigenous peoples celebrate their culture.'),
    fr('Why do many Indigenous traditions involve music and dance.'),
    fr('Name a way Indigenous peoples have lived close to nature.'),
    fr('What can visitors learn by attending a powwow.'),
    fr('Why should we respect and learn from Indigenous traditions.'),
    fr('Name one thing you have learned about Indigenous culture this year.'),
]))

all_worksheets.append(worksheet('SocialStudies', 8, 'Transportation Then and Now', [
    fr('Name a way people travelled long ago.'),
    fr('Name a way people travel today.'),
    fr('How is a car different from a horse and wagon.'),
    fr('Name a type of transportation that travels on water.'),
    fr('Name a type of transportation that travels in the air.'),
    fr('Why do we use trains to move many people at once.'),
    fr('Describe how transportation has changed over time.'),
    fr('Name a type of transportation you use to get to school.'),
    fr('Why might a ferry be useful in a city near water.'),
    fr('Compare travelling by bicycle and travelling by car.'),
    fr('Name a type of transportation that does not need fuel.'),
    fr('Why has transportation become faster over time.'),
    fr('Name a rule people follow to stay safe on transportation.'),
    fr('Describe your favourite way to travel.'),
    fr('Why is transportation important for communities.'),
]))

all_worksheets.append(worksheet('SocialStudies', 9, 'Needs and Wants', [
    fr('What is a need.'),
    fr('What is a want.'),
    fr('Name something that is a need.'),
    fr('Name something that is a want.'),
    fr('Is food a need or a want.'),
    fr('Is a toy a need or a want.'),
    fr('Why do people need shelter.'),
    fr('Why do people need clothing.'),
    fr('Sort these items into needs and wants: water, a video game, a house, candy.'),
    fr('Why is it important to know the difference between needs and wants.'),
    fr('Name a need that all living things share.'),
    fr('Describe a time when you wanted something but did not need it.'),
    fr('Why might a family save money instead of buying a want right away.'),
    fr('Name a want that you would like to have someday.'),
    fr('Explain in your own words the difference between a need and a want.'),
]))

all_worksheets.append(worksheet('SocialStudies', 10, 'Celebrating Different Cultures', [
    fr('Name a culture different from your own.'),
    fr('Name a food from a culture different from your own.'),
    fr('Name a tradition celebrated by a different culture.'),
    fr('Why is it good to learn about different cultures.'),
    fr('Name a language other than English spoken by people in Canada.'),
    fr('Describe a celebration from a culture you have learned about.'),
    fr('Name a piece of clothing worn during a cultural celebration.'),
    fr('Why do people from different cultures share their traditions.'),
    fr('Name a holiday celebrated by a culture different from your own.'),
    fr('How can trying new foods help us learn about other cultures.'),
    fr('Why does Canada have people from many different cultures.'),
    fr('Name a way your school celebrates different cultures.'),
    fr('Describe how music can be part of a cultural celebration.'),
    fr('Why is it important to respect traditions that are different from your own.'),
    fr('Name something you would like to learn about another culture.'),
]))

if __name__ == '__main__':
    write_worksheets(1, all_worksheets)
