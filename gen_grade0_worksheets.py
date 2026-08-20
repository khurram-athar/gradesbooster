#!/usr/bin/env python3
"""Kindergarten (Grade 0) standalone optional-worksheet content, per Project
Plan item 8. This is a NEW, separate content pipeline from data/grade0.ts
(the 187-day lesson sequence) -- these worksheets are supplementary
practice material, not new lessons, and are free to reinforce/overlap
topics already covered across the 187 days.

Produces exactly 40 worksheets: 10 per subject x 4 subjects (Language,
Math, Science, SocialStudies), 15 free-response questions each (fr()
only -- Kindergarten is free-response-only per gen_worksheets.py). Each
subject's 10 worksheets are organized around 10 distinct practice
themes/strands spanning the grade, loosely progressing from foundational
to more advanced within that subject, so each worksheet has a clear,
distinct focus and a title that does not repeat within its subject.

No embedded straight double-quotes or apostrophes anywhere in title/q
text -- contractions and possessives are avoided entirely (e.g. "does
not" not "doesnt", "the students name" not "the student's name"), same
convention as the rest of this project's generated content.
"""
import sys
sys.path.insert(0, '.')
from gen_worksheets import fr, worksheet, write_worksheets

all_worksheets = []

# ---------------------------------------------------------------------------
# LANGUAGE (10 worksheets)
# ---------------------------------------------------------------------------

all_worksheets.append(worksheet('Language', 1, 'Letter Recognition: A to M', [
    fr('Say the name of the letter A.'),
    fr('Say the name of the letter B.'),
    fr('Point to a letter in the alphabet that comes right after C.'),
    fr('Name a word that starts with the letter D.'),
    fr('Say the name of the letter E.'),
    fr('Name a word that starts with the letter F.'),
    fr('Say the name of the letter G.'),
    fr('Name a word that starts with the letter H.'),
    fr('Say the letter that comes right before J.'),
    fr('Name a word that starts with the letter K.'),
    fr('Say the name of the letter L.'),
    fr('Name a word that starts with the letter M.'),
    fr('Which letter looks like a triangle with a line across it, A or B?'),
    fr('Say two letters that come between H and M.'),
    fr('Name your favourite letter and one word that starts with it.'),
]))

all_worksheets.append(worksheet('Language', 2, 'Letter Recognition: N to Z', [
    fr('Say the name of the letter N.'),
    fr('Name a word that starts with the letter O.'),
    fr('Say the name of the letter P.'),
    fr('Name a word that starts with the letter Q.'),
    fr('Say the name of the letter R.'),
    fr('Name a word that starts with the letter S.'),
    fr('Say the name of the letter T.'),
    fr('Name a word that starts with the letter U.'),
    fr('Say the name of the letter V.'),
    fr('Name a word that starts with the letter W.'),
    fr('Say the letter that comes right after X.'),
    fr('Name a word that starts with the letter Z.'),
    fr('Say the last letter of the alphabet.'),
    fr('Say two letters that come between P and T.'),
    fr('Name three letters near the end of the alphabet.'),
]))

all_worksheets.append(worksheet('Language', 3, 'Short Vowel Sounds', [
    fr('Say the short sound the letter A makes, like in cat.'),
    fr('Name a word with the short a sound.'),
    fr('Say the short sound the letter E makes, like in bed.'),
    fr('Name a word with the short e sound.'),
    fr('Say the short sound the letter I makes, like in pig.'),
    fr('Name a word with the short i sound.'),
    fr('Say the short sound the letter O makes, like in dog.'),
    fr('Name a word with the short o sound.'),
    fr('Say the short sound the letter U makes, like in sun.'),
    fr('Name a word with the short u sound.'),
    fr('Which word has the short a sound, hat or hot?'),
    fr('Which word has the short i sound, sit or sat?'),
    fr('Say a word that rhymes with pig using a short i sound.'),
    fr('Say a word that rhymes with sun using a short u sound.'),
    fr('Name one word for each of the five short vowel sounds.'),
]))

all_worksheets.append(worksheet('Language', 4, 'Beginning and Ending Sounds', [
    fr('Say the beginning sound in the word ball.'),
    fr('Say the ending sound in the word cat.'),
    fr('Say the beginning sound in the word sun.'),
    fr('Say the ending sound in the word dog.'),
    fr('Name a word that starts with the same sound as milk.'),
    fr('Name a word that ends with the same sound as bag.'),
    fr('Say the beginning sound in the word fish.'),
    fr('Say the ending sound in the word map.'),
    fr('Which word starts with the same sound as top, tap or cup?'),
    fr('Which word ends with the same sound as hop, top or run?'),
    fr('Name a word that begins with the letter B.'),
    fr('Name a word that ends with the letter N.'),
    fr('Say the beginning sound in your own name.'),
    fr('Name a word that starts and ends with different sounds than dog.'),
    fr('Say the beginning sound and the ending sound in the word pin.'),
]))

all_worksheets.append(worksheet('Language', 5, 'Rhyming Words', [
    fr('Name a word that rhymes with cat.'),
    fr('Name a word that rhymes with dog.'),
    fr('Name a word that rhymes with sun.'),
    fr('Do the words hen and pen rhyme?'),
    fr('Do the words cup and dog rhyme?'),
    fr('Name a word that rhymes with pig.'),
    fr('Name a word that rhymes with hop.'),
    fr('Say two words that rhyme with each other.'),
    fr('Name a word that rhymes with bed.'),
    fr('Do the words map and cap rhyme?'),
    fr('Name a word that rhymes with fan.'),
    fr('Finish the rhyme: I saw a bee sitting on a ___.'),
    fr('Finish the rhyme: The cat sat on the ___.'),
    fr('Name a word that rhymes with your own name if you can.'),
    fr('Say a short rhyme with two words that sound alike.'),
]))

all_worksheets.append(worksheet('Language', 6, 'Word Families: -at, -an, -ig', [
    fr('Name a word from the -at family, like cat or hat.'),
    fr('Name a word from the -an family, like man or fan.'),
    fr('Name a word from the -ig family, like pig or big.'),
    fr('Does bat belong to the -at family?'),
    fr('Does van belong to the -an family?'),
    fr('Does dig belong to the -ig family?'),
    fr('Name another word from the -at family besides cat and hat.'),
    fr('Name another word from the -an family besides man and fan.'),
    fr('Name another word from the -ig family besides pig and big.'),
    fr('What ending sound do cat and hat share?'),
    fr('What ending sound do man and fan share?'),
    fr('Say a sentence using a word from the -at family.'),
    fr('Say a sentence using a word from the -an family.'),
    fr('Sort these words into families: cat, man, pig, hat, fan.'),
    fr('Name one word from each of the three families in this worksheet.'),
]))

all_worksheets.append(worksheet('Language', 7, 'Sight Words in Sentences', [
    fr('Read the word the out loud.'),
    fr('Read the word and out loud.'),
    fr('Read the word is out loud.'),
    fr('Say a short sentence using the word the.'),
    fr('Say a short sentence using the word and.'),
    fr('Read the word you out loud.'),
    fr('Read the word see out loud.'),
    fr('Say a short sentence using the word see.'),
    fr('Read the word like out loud.'),
    fr('Say a short sentence using the word like.'),
    fr('Read the word go out loud.'),
    fr('Say a short sentence using the word go.'),
    fr('Point to the word the in a book near you.'),
    fr('Name one sight word you already know well.'),
    fr('Say a sentence that uses two sight words together.'),
]))

all_worksheets.append(worksheet('Language', 8, 'Listening and Story Comprehension', [
    fr('Listen to a short story and name the main character.'),
    fr('Where did the story take place?'),
    fr('What happened at the beginning of the story?'),
    fr('What happened in the middle of the story?'),
    fr('What happened at the end of the story?'),
    fr('Name one thing that happened in the story.'),
    fr('How did the main character feel in the story?'),
    fr('Was the story happy, sad, or funny?'),
    fr('Name another character from the story if there was one.'),
    fr('What was your favourite part of the story?'),
    fr('Why do you think the character made that choice?'),
    fr('Retell the story in your own words.'),
    fr('What might happen next if the story continued?'),
    fr('Would you have made the same choice as the character?'),
    fr('Draw or describe a picture that shows what happened in the story.'),
]))

all_worksheets.append(worksheet('Language', 9, 'Simple Sentences and Naming Words', [
    fr('Name a person, place, or thing, which is called a naming word.'),
    fr('Say a sentence with just two words, like Dogs run.'),
    fr('Name the naming word in the sentence The dog runs.'),
    fr('Say a sentence about your family.'),
    fr('Say a sentence about your favourite food.'),
    fr('Name a naming word for an animal.'),
    fr('Name a naming word for a place.'),
    fr('Say a sentence that starts with a capital letter.'),
    fr('Why does a sentence start with a capital letter?'),
    fr('Say a sentence that ends with a period.'),
    fr('Name the action word in the sentence The bird flies.'),
    fr('Say a sentence with a naming word and an action word.'),
    fr('Name three naming words you can see around you right now.'),
    fr('Say a sentence describing what you did today.'),
    fr('Say a full sentence about your best friend.'),
]))

all_worksheets.append(worksheet('Language', 10, 'Language Skills Review', [
    fr('Say the name of a letter near the start of the alphabet.'),
    fr('Say the name of a letter near the end of the alphabet.'),
    fr('Name a word with the short a sound.'),
    fr('Name a word with the short o sound.'),
    fr('Say the beginning sound in the word sun.'),
    fr('Name a word that rhymes with cat.'),
    fr('Name a word from the -ig word family.'),
    fr('Read the sight word the out loud.'),
    fr('Say a short sentence using the sight word like.'),
    fr('Name the main character from a story you know.'),
    fr('Say a full sentence about your day.'),
    fr('Name a naming word for a person.'),
    fr('Name an action word for something you do every day.'),
    fr('Say two words that rhyme with each other.'),
    fr('Say your favourite letter, word, and story from this year.'),
]))

# ---------------------------------------------------------------------------
# MATH (10 worksheets)
# ---------------------------------------------------------------------------

all_worksheets.append(worksheet('Math', 1, 'Counting to 20', [
    fr('Count out loud from 1 to 10.'),
    fr('Count out loud from 11 to 20.'),
    fr('What number comes right after 7?'),
    fr('What number comes right before 15?'),
    fr('Count five toys or objects near you.'),
    fr('What number comes between 12 and 14?'),
    fr('Count backward from 5 to 1.'),
    fr('What number comes right after 19?'),
    fr('Show ten fingers and say the number.'),
    fr('What number comes right before 10?'),
    fr('Count out loud from 1 to 20 without stopping.'),
    fr('Which is greater, 8 or 12?'),
    fr('Which is smaller, 6 or 3?'),
    fr('Count a group of eight objects and say the total.'),
    fr('What number comes right after 20?'),
]))

all_worksheets.append(worksheet('Math', 2, 'Number Recognition and Writing', [
    fr('Say the number 4 out loud.'),
    fr('Say the number 7 out loud.'),
    fr('Say the number 12 out loud.'),
    fr('Point to the numeral 5 if you see a row of numbers.'),
    fr('Name a number that has two digits.'),
    fr('Say the number that comes after 9.'),
    fr('Say the number 15 out loud.'),
    fr('Write or trace the numeral 3.'),
    fr('Write or trace the numeral 8.'),
    fr('Say the numbers from 1 to 5 in order.'),
    fr('Say which number is bigger, 10 or 1.'),
    fr('Name a number between 6 and 9.'),
    fr('Say the number 20 out loud.'),
    fr('Write or trace the numeral 11.'),
    fr('Say your age as a number.'),
]))

all_worksheets.append(worksheet('Math', 3, 'Simple Addition to 10', [
    fr('What is 1 plus 1?'),
    fr('What is 2 plus 3?'),
    fr('What is 4 plus 1?'),
    fr('What is 3 plus 3?'),
    fr('What is 5 plus 2?'),
    fr('What is 2 plus 2?'),
    fr('What is 4 plus 4?'),
    fr('What is 6 plus 1?'),
    fr('What is 3 plus 4?'),
    fr('What is 5 plus 5?'),
    fr('If you have 2 apples and get 3 more, how many do you have?'),
    fr('What is 7 plus 2?'),
    fr('What is 1 plus 8?'),
    fr('What is 6 plus 3?'),
    fr('What two numbers can you add together to make 9?'),
]))

all_worksheets.append(worksheet('Math', 4, 'Simple Subtraction to 10', [
    fr('What is 5 minus 1?'),
    fr('What is 4 minus 2?'),
    fr('What is 7 minus 3?'),
    fr('What is 6 minus 4?'),
    fr('What is 9 minus 5?'),
    fr('What is 8 minus 2?'),
    fr('What is 3 minus 1?'),
    fr('What is 10 minus 6?'),
    fr('If you have 6 balloons and 2 pop, how many are left?'),
    fr('What is 9 minus 9?'),
    fr('What is 7 minus 0?'),
    fr('What is 8 minus 5?'),
    fr('What is 10 minus 10?'),
    fr('What is 6 minus 3?'),
    fr('Which is bigger, the answer to 8 minus 2 or 5 minus 1?'),
]))

all_worksheets.append(worksheet('Math', 5, 'Shapes All Around Us', [
    fr('Name a shape with three sides.'),
    fr('Name a shape with four equal sides.'),
    fr('How many sides does a triangle have?'),
    fr('How many corners does a square have?'),
    fr('Name a shape that is round with no corners.'),
    fr('Name an object shaped like a circle.'),
    fr('Name an object shaped like a rectangle.'),
    fr('How many sides does a rectangle have?'),
    fr('Name a shape with five sides.'),
    fr('Name a shape with six sides.'),
    fr('Which shape has more sides, a triangle or a square?'),
    fr('Name a solid shape that looks like a ball.'),
    fr('Name a solid shape that looks like a box.'),
    fr('Find a circle-shaped object near you and name it.'),
    fr('Draw or describe a picture using at least three different shapes.'),
]))

all_worksheets.append(worksheet('Math', 6, 'Measurement: Big and Small, Long and Short', [
    fr('Name something that is big.'),
    fr('Name something that is small.'),
    fr('Which is longer, a pencil or a crayon?'),
    fr('Name something that is short.'),
    fr('Name something that is tall.'),
    fr('Which is heavier, a book or a feather?'),
    fr('Name something that is light.'),
    fr('Name something that is heavy.'),
    fr('Which holds more water, a cup or a bathtub?'),
    fr('Name something that is empty.'),
    fr('Name something that is full.'),
    fr('Compare your height to a doorway, which is taller?'),
    fr('Name two objects and say which one is longer.'),
    fr('Name something at home that is very tall.'),
    fr('Put three objects in order from shortest to tallest.'),
]))

all_worksheets.append(worksheet('Math', 7, 'Patterns and Sorting', [
    fr('Name what comes next in the pattern red, blue, red, blue.'),
    fr('Sort a group of toys by colour.'),
    fr('Name what comes next in the pattern circle, square, circle, square.'),
    fr('Sort a group of objects by size.'),
    fr('Name two objects that belong in the same group.'),
    fr('Name what comes next in the pattern 1, 2, 1, 2.'),
    fr('Sort a group of shapes by their number of sides.'),
    fr('Name a pattern you see in your clothing.'),
    fr('Make a simple pattern using two colours.'),
    fr('Name what does not belong in this group: apple, banana, shoe.'),
    fr('Sort a group of objects by whether they are big or small.'),
    fr('Name what comes next in the pattern clap, stomp, clap, stomp.'),
    fr('Explain why you sorted your objects the way you did.'),
    fr('Name a pattern you notice outside or at home.'),
    fr('Make a pattern using three different shapes.'),
]))

all_worksheets.append(worksheet('Math', 8, 'Coins and Simple Money', [
    fr('Name a Canadian coin.'),
    fr('How much is one penny worth?'),
    fr('How much is one nickel worth?'),
    fr('How much is one dime worth?'),
    fr('How much is one quarter worth?'),
    fr('Which coin is worth more, a dime or a nickel?'),
    fr('Name the coin that is worth 25 cents.'),
    fr('How many pennies equal one nickel?'),
    fr('Name something you might buy with a few coins.'),
    fr('Which coin is the smallest in size?'),
    fr('Count two pennies and say how many cents that is.'),
    fr('Which coin is worth the most out of a penny, nickel, and dime?'),
    fr('Name a coin that is silver in colour.'),
    fr('Name a coin that is copper in colour.'),
    fr('If you have one dime, how many cents do you have?'),
]))

all_worksheets.append(worksheet('Math', 9, 'Telling Time and Calendar Basics', [
    fr('Name the two hands on a clock.'),
    fr('What time is shown when both hands point straight up?'),
    fr('Name a day of the week.'),
    fr('How many days are in one week?'),
    fr('Name the day that comes after Monday.'),
    fr('Name the month you were born in.'),
    fr('How many months are in one year?'),
    fr('Name a season of the year.'),
    fr('What season comes after winter?'),
    fr('Is it usually daytime or nighttime when you eat breakfast?'),
    fr('Name something you do in the morning.'),
    fr('Name something you do at night before bed.'),
    fr('Which is longer, one hour or one minute?'),
    fr('Name the day that comes before Saturday.'),
    fr('Name a special day or holiday and the season it happens in.'),
]))

all_worksheets.append(worksheet('Math', 10, 'Math Skills Review', [
    fr('Count out loud from 1 to 20.'),
    fr('What is 3 plus 2?'),
    fr('What is 5 minus 2?'),
    fr('Name a shape with three sides.'),
    fr('Which is longer, a pencil or a paperclip?'),
    fr('Name what comes next in the pattern red, blue, red, blue.'),
    fr('How much is one dime worth?'),
    fr('Name a day of the week.'),
    fr('What number comes right after 10?'),
    fr('Name a shape with four equal sides.'),
    fr('What is 4 plus 4?'),
    fr('Sort three objects by size, from smallest to biggest.'),
    fr('How many days are in one week?'),
    fr('What is 6 minus 3?'),
    fr('Name your favourite number and why you like it.'),
]))

# ---------------------------------------------------------------------------
# SCIENCE (10 worksheets)
# ---------------------------------------------------------------------------

all_worksheets.append(worksheet('Science', 1, 'My Five Senses', [
    fr('Name the five senses.'),
    fr('Which body part do you use to see?'),
    fr('Which body part do you use to hear?'),
    fr('Which body part do you use to smell?'),
    fr('Which body part do you use to taste?'),
    fr('Which body part do you use to touch?'),
    fr('Name something that smells good.'),
    fr('Name something that feels soft.'),
    fr('Name something that tastes sweet.'),
    fr('Name something that is loud.'),
    fr('Name something that looks colourful.'),
    fr('Which sense would you use to tell if soup is hot?'),
    fr('Which sense would you use to enjoy music?'),
    fr('Name a food and describe its taste.'),
    fr('Why are our senses helpful to us every day?'),
]))

all_worksheets.append(worksheet('Science', 2, 'Animals Around Us', [
    fr('Name an animal that lives on a farm.'),
    fr('Name an animal that lives in the ocean.'),
    fr('Name an animal that can fly.'),
    fr('Name an animal that swims.'),
    fr('Name an animal that has fur.'),
    fr('Name an animal that has feathers.'),
    fr('Name an animal that lives in a forest.'),
    fr('Name a pet that people keep at home.'),
    fr('What sound does a dog make?'),
    fr('What sound does a cat make?'),
    fr('Name an animal that lays eggs.'),
    fr('Name an animal that is very big.'),
    fr('Name an animal that is very small.'),
    fr('How do animals use their legs, wings, or fins to move?'),
    fr('Name your favourite animal and one fact about it.'),
]))

all_worksheets.append(worksheet('Science', 3, 'Plants and How They Grow', [
    fr('Name a part of a plant.'),
    fr('What do plants need to grow?'),
    fr('Does a plant need water to grow?'),
    fr('Does a plant need sunlight to grow?'),
    fr('Name something that grows from a seed.'),
    fr('What part of the plant is usually underground?'),
    fr('What part of the plant makes food using sunlight?'),
    fr('Name a fruit that grows on a tree.'),
    fr('Name a vegetable that grows in the ground.'),
    fr('What colour are most plant leaves?'),
    fr('Name a flower you have seen.'),
    fr('What happens to a seed after you plant and water it?'),
    fr('Why do plants need soil?'),
    fr('Name a tool a person might use to care for a garden.'),
    fr('Draw or describe how a tiny seed grows into a tall plant.'),
]))

all_worksheets.append(worksheet('Science', 4, 'Weather and the Seasons', [
    fr('Name a type of weather, like sunny or rainy.'),
    fr('What season comes after winter?'),
    fr('What do you wear outside when it is cold?'),
    fr('What do you wear outside when it is sunny and hot?'),
    fr('Name something you might see in the sky on a rainy day.'),
    fr('What falls from the sky in winter?'),
    fr('Name a season when leaves change colour and fall.'),
    fr('Is it hotter in summer or winter?'),
    fr('Name something you might do outside on a snowy day.'),
    fr('Name something you might do outside on a sunny day.'),
    fr('What tool helps you know if it will rain today?'),
    fr('Name a piece of clothing you wear when it rains.'),
    fr('How many seasons are there in one year?'),
    fr('Name your favourite season and why you like it.'),
    fr('Describe the weather outside right now.'),
]))

all_worksheets.append(worksheet('Science', 5, 'Day and Night Sky', [
    fr('Name something you can see in the sky during the day.'),
    fr('Name something you can see in the sky at night.'),
    fr('Is the sun out during the day or at night?'),
    fr('Is the moon usually seen at night or during the day?'),
    fr('Name something twinkly you might see at night.'),
    fr('Why do we need to sleep at night?'),
    fr('What activity do you usually do during the daytime?'),
    fr('Is the sky usually brighter during the day or at night?'),
    fr('Name a shape the moon can look like in the sky.'),
    fr('What happens to the sky when the sun goes down?'),
    fr('Name something that helps you see in the dark.'),
    fr('Why should you never look directly at the sun?'),
    fr('Name one thing that is different between day and night.'),
    fr('What time of day do you usually eat dinner?'),
    fr('Describe what the sky looks like on a clear night.'),
]))

all_worksheets.append(worksheet('Science', 6, 'My Body and Staying Healthy', [
    fr('Name a part of your body.'),
    fr('What do you use to walk?'),
    fr('What do you use to hold and pick things up?'),
    fr('Name something healthy to eat.'),
    fr('Why is it important to wash your hands?'),
    fr('Why is it important to brush your teeth?'),
    fr('Name something you do to stay active and exercise.'),
    fr('How many fingers do you have on one hand?'),
    fr('Why is sleep important for your body?'),
    fr('Name a healthy drink.'),
    fr('What body part helps you think and learn?'),
    fr('Why do you wear a helmet when riding a bike?'),
    fr('Name something you do every morning to get ready for the day.'),
    fr('Why is it important to eat different kinds of healthy food?'),
    fr('Name one way you take care of your body.'),
]))

all_worksheets.append(worksheet('Science', 7, 'Materials: Solids, Liquids, and Water Play', [
    fr('Name something that is a solid.'),
    fr('Name something that is a liquid.'),
    fr('Does water take the shape of its container?'),
    fr('Name something made of wood.'),
    fr('Name something made of metal.'),
    fr('Name something made of plastic.'),
    fr('Does a rock keep its shape or change shape?'),
    fr('Name a liquid you drink.'),
    fr('What happens to water if you freeze it?'),
    fr('What happens to ice if you leave it in the sun?'),
    fr('Name something that floats in water.'),
    fr('Name something that sinks in water.'),
    fr('Is milk a solid or a liquid?'),
    fr('Name a material that feels hard.'),
    fr('Name a material that feels soft.'),
]))

all_worksheets.append(worksheet('Science', 8, 'Insects and Small Creatures', [
    fr('Name an insect you have seen outside.'),
    fr('How many legs does an insect have?'),
    fr('Name an insect that makes honey.'),
    fr('Name an insect that can fly.'),
    fr('What does a caterpillar turn into?'),
    fr('Name a small creature that lives in soil.'),
    fr('Name an insect that has colourful wings.'),
    fr('Where might you find a spider web?'),
    fr('Is a spider an insect?'),
    fr('Name a bug that glows at night.'),
    fr('Name a place where you might find insects outside.'),
    fr('What sound does a cricket make?'),
    fr('Why are bees helpful to flowers?'),
    fr('Name your favourite small creature and one fact about it.'),
    fr('Describe how a tiny insect moves from place to place.'),
]))

all_worksheets.append(worksheet('Science', 9, 'Caring for Our Earth', [
    fr('Name something you can recycle.'),
    fr('Why is it important to put garbage in a bin?'),
    fr('Name something you can reuse instead of throwing away.'),
    fr('Why should we turn off lights we are not using?'),
    fr('Name a way to save water at home.'),
    fr('Why is it important to keep parks and beaches clean?'),
    fr('Name something green, like a tree, that helps our air.'),
    fr('What can you do to help keep your neighbourhood clean?'),
    fr('Name an animal that could be harmed by litter.'),
    fr('Why do we plant trees?'),
    fr('Name one way your family cares for the environment.'),
    fr('Why is it good to walk or bike instead of drive sometimes?'),
    fr('Name a bin colour used for recycling.'),
    fr('What happens to plastic that is left outside for a long time?'),
    fr('Name one thing you will do to help take care of the Earth.'),
]))

all_worksheets.append(worksheet('Science', 10, 'Science Skills Review', [
    fr('Name the five senses.'),
    fr('Name an animal that lives in the ocean.'),
    fr('What do plants need to grow?'),
    fr('What season comes after winter?'),
    fr('Name something you can see in the sky at night.'),
    fr('Why is it important to wash your hands?'),
    fr('Name something that is a liquid.'),
    fr('How many legs does an insect have?'),
    fr('Name something you can recycle.'),
    fr('Name a part of a plant.'),
    fr('Name an animal that can fly.'),
    fr('What falls from the sky in winter?'),
    fr('Name something healthy to eat.'),
    fr('Name something that floats in water.'),
    fr('Name one thing you will do to help take care of the Earth.'),
]))

# ---------------------------------------------------------------------------
# SOCIAL STUDIES (10 worksheets)
# ---------------------------------------------------------------------------

all_worksheets.append(worksheet('SocialStudies', 1, 'My Family and Home', [
    fr('Name a member of your family.'),
    fr('Name a job someone in your family does at home.'),
    fr('What is the name of the street or area you live on?'),
    fr('Name a room in your home.'),
    fr('Name something your family does together.'),
    fr('Who takes care of you at home?'),
    fr('Name a family tradition or celebration you enjoy.'),
    fr('Name a pet or animal that lives with your family, if you have one.'),
    fr('What is one rule your family has at home?'),
    fr('Name someone who helps take care of your family.'),
    fr('Name a meal your family likes to eat together.'),
    fr('What do you like to do with your family on weekends?'),
    fr('Name a family member who lives far away, if you have one.'),
    fr('Why is it important to help out at home?'),
    fr('Describe what makes your family special.'),
]))

all_worksheets.append(worksheet('SocialStudies', 2, 'Community Helpers', [
    fr('Name a community helper.'),
    fr('What does a firefighter do?'),
    fr('What does a police officer do?'),
    fr('What does a doctor do?'),
    fr('What does a teacher do?'),
    fr('What does a mail carrier do?'),
    fr('Why do we need community helpers?'),
    fr('Name a helper who works at a hospital.'),
    fr('Name a helper who works at a school.'),
    fr('Name a helper who keeps our streets safe.'),
    fr('What tool might a firefighter use?'),
    fr('Why is it important to say thank you to community helpers?'),
    fr('Name a helper who delivers food or packages.'),
    fr('Which community helper would you call in an emergency?'),
    fr('Name your favourite community helper and explain why.'),
]))

all_worksheets.append(worksheet('SocialStudies', 3, 'My School and Classroom', [
    fr('Name a room in your school.'),
    fr('Name a person who works at your school.'),
    fr('Name a rule you follow in your classroom.'),
    fr('What do you do at recess?'),
    fr('Name a subject you learn about at school.'),
    fr('Why is it important to listen to your teacher?'),
    fr('Name a friend you play with at school.'),
    fr('What do you do in the library at school?'),
    fr('Why is it important to share with classmates?'),
    fr('Name something you use for learning at school, like a book or pencil.'),
    fr('What do you do when the school day starts?'),
    fr('Name a place in the school where you eat lunch.'),
    fr('Why should you clean up after activities at school?'),
    fr('Name something you are proud of learning at school.'),
    fr('Describe your favourite part of the school day.'),
]))

all_worksheets.append(worksheet('SocialStudies', 4, 'Being a Good Friend', [
    fr('Name something a good friend does.'),
    fr('Why is it important to share with friends?'),
    fr('What should you say if you accidentally bump into a friend?'),
    fr('Name a way to include someone who is playing alone.'),
    fr('Why is it important to take turns?'),
    fr('What should you do if a friend is feeling sad?'),
    fr('Name a kind word you can say to a friend.'),
    fr('Why is it important to listen when a friend is talking?'),
    fr('What should you do if you and a friend disagree?'),
    fr('Name a game you like to play with friends.'),
    fr('Why is it important to say sorry when you make a mistake?'),
    fr('Name a way to help a friend who is hurt.'),
    fr('Why should you not laugh at a friend who makes a mistake?'),
    fr('Name one way you can be a good friend today.'),
    fr('Describe a time you helped a friend.'),
]))

all_worksheets.append(worksheet('SocialStudies', 5, 'Rules and Safety', [
    fr('Name a rule you follow at home.'),
    fr('Name a rule you follow at school.'),
    fr('Why is it important to follow rules?'),
    fr('What colour on a traffic light means stop?'),
    fr('What colour on a traffic light means go?'),
    fr('Why should you hold an adult hand when crossing the street?'),
    fr('What should you do if there is a fire drill at school?'),
    fr('Why do we wear a seatbelt in a car?'),
    fr('Name a safety rule for playing outside.'),
    fr('Who should you talk to if you feel unsafe?'),
    fr('Why is it important to wear a helmet when biking?'),
    fr('Name a rule that helps keep everyone safe at a playground.'),
    fr('What number do you call in an emergency in Canada?'),
    fr('Why do we have rules in a classroom?'),
    fr('Name one safety rule you always try to follow.'),
]))

all_worksheets.append(worksheet('SocialStudies', 6, 'My Neighbourhood and City', [
    fr('Name a building you might see in a neighbourhood.'),
    fr('Name a place where people buy food.'),
    fr('Name a place where people go to learn.'),
    fr('Name a place where people go when they are sick.'),
    fr('Name a way people travel around a city.'),
    fr('Name a place where people play outside.'),
    fr('What is the name of the city or town you live in?'),
    fr('Name a place where books are kept for people to borrow.'),
    fr('Name something you might see on a street.'),
    fr('Why do neighbourhoods have parks?'),
    fr('Name a place of worship someone in your community might visit.'),
    fr('Name a way people get mail delivered to their home.'),
    fr('Why is it helpful to know your address?'),
    fr('Name a favourite place in your neighbourhood.'),
    fr('Describe what you might see on a walk around your neighbourhood.'),
]))

all_worksheets.append(worksheet('SocialStudies', 7, 'Canada: Our Country', [
    fr('What is the name of the country we live in?'),
    fr('Name the capital city of Canada.'),
    fr('What colour is the maple leaf on the Canadian flag?'),
    fr('Name an animal often connected with Canada.'),
    fr('What season in Canada has lots of snow?'),
    fr('Name something Canada is known for.'),
    fr('What is the name of the province or territory you live in?'),
    fr('Name a language spoken in Canada.'),
    fr('What shape is the red symbol on the Canadian flag?'),
    fr('Name a Canadian city you have heard of.'),
    fr('Why do people fly the Canadian flag on special days?'),
    fr('Name a food that is popular in Canada.'),
    fr('What is Canada Day and when is it celebrated?'),
    fr('Name something you like about living in Canada.'),
    fr('Describe the Canadian flag using colours and shapes.'),
]))

all_worksheets.append(worksheet('SocialStudies', 8, 'Then and Now: Old and New Things', [
    fr('Name something people used a long time ago to travel.'),
    fr('Name something people use today to travel.'),
    fr('Name a toy that children played with long ago.'),
    fr('Name a toy that children play with today.'),
    fr('How did people send messages before phones were invented?'),
    fr('Name something that has changed about schools over time.'),
    fr('Name something people used long ago to light their homes.'),
    fr('What do we use today to light our homes?'),
    fr('Name a chore that was harder to do long ago than it is now.'),
    fr('Ask a grandparent or older person about something from their childhood.'),
    fr('Name something that has stayed mostly the same over time.'),
    fr('Why do things change over time?'),
    fr('Name an old object you have seen in a museum or picture.'),
    fr('Name a new invention that helps people today.'),
    fr('Describe one way life today is different from life long ago.'),
]))

all_worksheets.append(worksheet('SocialStudies', 9, 'Celebrations and Traditions', [
    fr('Name a celebration your family enjoys.'),
    fr('Name a celebration that happens in winter.'),
    fr('Name a food that is part of a celebration you know.'),
    fr('Name a decoration used during a celebration.'),
    fr('Why do families celebrate birthdays?'),
    fr('Name a tradition your family has.'),
    fr('Name a celebration where people give gifts.'),
    fr('Name a celebration where people wear special clothing.'),
    fr('Why is it fun to learn about celebrations from other families?'),
    fr('Name a song you sing during a celebration.'),
    fr('Name a celebration that involves fireworks or lights.'),
    fr('Why do people gather with family and friends during celebrations?'),
    fr('Name your favourite celebration of the year.'),
    fr('Describe how your family celebrates a special day.'),
    fr('Name a celebration that happens in a different season than winter.'),
]))

all_worksheets.append(worksheet('SocialStudies', 10, 'Social Studies Skills Review', [
    fr('Name a member of your family.'),
    fr('Name a community helper.'),
    fr('Name a rule you follow at school.'),
    fr('What colour on a traffic light means stop?'),
    fr('Name the capital city of Canada.'),
    fr('Name something a good friend does.'),
    fr('Name a place where people buy food.'),
    fr('Name a celebration your family enjoys.'),
    fr('Name something people used long ago to travel.'),
    fr('Why is it important to follow rules?'),
    fr('Name a room in your school.'),
    fr('What is the name of the city or town you live in?'),
    fr('Name a way to include someone who is playing alone.'),
    fr('Why do we have rules in a classroom?'),
    fr('Name one thing you learned this year about your community.'),
]))

if __name__ == '__main__':
    write_worksheets(0, all_worksheets)
