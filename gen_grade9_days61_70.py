#!/usr/bin/env python3
"""Phase 3 extension: Grade 9, Days 61-70 (fourth Grade 9 batch, continuing
the 10-day pattern past Days 51-60). Topics chosen to avoid any overlap with
the existing Day 1-60 set (see data/grade9.json after the Days 51-60 batch):
setting as a literary element, the narrative essay, appositives, etymology
and word roots, direct/indirect characterization, advertising persuasion
techniques, business letters, active/passive voice, flashback and
foreshadowing, radicals, rational exponents, elimination method for linear
systems, function notation/domain/range, spheres and cones, currency
exchange, probability distributions, logarithms, matrices, solutions and
solubility, the immune system, simple machines, light (reflection and
refraction), the circulatory/respiratory systems, radioactivity and
half-life, ocean currents, friction and terminal velocity, enzymes, and
geography extensions (map projections, time zones, urban heat islands,
wildfire risk, political boundaries in Canada, cultural landscapes/heritage
sites, urban food deserts, space exploration/satellites, light and noise
pollution).

Subject keys for Grade 9 are "Language", "Math", "Science",
"SocialStudies" (same as earlier batches; SocialStudies content is
geography-focused for Grade 9).

videoUrl is intentionally left unset for every subject -- fetch_video_ids.py
fills these in automatically on its next daily run. No embedded ASCII
double-quote characters are used anywhere in question/summary/option text;
apostrophes and quotation marks use the curly Unicode form (’ “ ”) so they
never collide with the single-quoted Python string literals used here.
"""
import sys
sys.path.insert(0, '/sessions/happy-laughing-ritchie/mnt/gradesbooster')
from gen_curriculum import sub, day, append_to

L9 = 'https://tvolearn.com/pages/grade-9-language'
M9 = 'https://tvolearn.com/pages/grade-9-mathematics'
S9 = 'https://tvolearn.com/pages/grade-9-science-and-technology'
SS9 = 'https://tvolearn.com/pages/grade-9-social-studies'
RL, RM, RS, RSS = (
    'TVO Learn: Grade 9 Language',
    'TVO Learn: Grade 9 Mathematics',
    'TVO Learn: Grade 9 Science & Technology',
    'TVO Learn: Grade 9 Social Studies',
)


def L(t, s, q):
    return sub('Language', t, s, RL, L9, q)


def M(t, s, q):
    return sub('Math', t, s, RM, M9, q)


def Sc(t, s, q):
    return sub('Science', t, s, RS, S9, q)


def SS(t, s, q):
    return sub('SocialStudies', t, s, RSS, SS9, q)


g9_61_70 = [
day(61, [
L('Reading: Analyzing Setting as a Literary Element',
  'Grade 9 Reading strand: setting refers to the time and place in which a story occurs, and it can shape mood, influence character behaviour, and reinforce a story’s themes.',
  [('A story’s setting refers to ___.', ['The time and place in which a story occurs', 'Only the names of the characters involved', 'A concept unrelated to literary analysis', 'The order in which events are told'], 0),
   ('How can setting influence the mood of a story?', ['Details like weather, lighting, or location can create a particular emotional atmosphere', 'Setting never has any effect on a story’s mood', 'Mood is determined only by dialogue, never by setting', 'A concept unrelated to a story’s atmosphere'], 0),
   ('Which is an example of setting shaping a character’s behaviour?', ['A character acting fearfully while walking through a dark, isolated forest at night', 'A character whose actions never relate to their surroundings', 'A concept unrelated to setting', 'A character who behaves identically in every possible location'], 0),
   ('Why might an author use a specific historical setting to reinforce a story’s themes?', ['The time period’s social conditions can echo or deepen the story’s central ideas', 'Historical settings never connect to a story’s themes', 'Themes are always unrelated to when or where a story takes place', 'An author’s choice of setting has no effect on meaning'], 0),
   ('Why is analyzing setting an important reading skill?', ['It reveals how time and place shape mood, character, and theme throughout a text', 'Setting has no real connection to how a story is understood', 'This skill is never useful when studying literature', 'Setting only matters in nonfiction texts, not fiction'], 0)]),
M('Simplifying Radicals and Square Roots',
  'Grade 9 Number/Algebra strand: simplifying a radical involves factoring out perfect square factors from beneath a square root sign to express the value in its simplest radical form.',
  [('Simplifying a radical involves factoring out ___ from beneath the square root sign.', ['Perfect square factors', 'Only prime numbers, with no connection to perfect squares', 'A concept unrelated to radicals', 'The entire number, leaving nothing beneath the radical'], 0),
   ('What is the simplified form of the square root of 50?', ['5 times the square root of 2', '25 times the square root of 2', 'A value unrelated to the square root of 50', '10 times the square root of 5'], 0),
   ('Which of these is the largest perfect square factor of 72?', ['36', '72', 'A value unrelated to factors of 72', '9'], 0),
   ('Why is expressing a radical in simplest form useful in algebra?', ['It makes radicals easier to compare, add, and combine with like terms', 'Simplifying radicals never has any mathematical benefit', 'Simplest form always changes a radical’s actual value', 'This concept has no connection to algebraic operations'], 0),
   ('A simplified radical is considered fully simplified when the number remaining under the root has ___.', ['No remaining perfect square factors', 'At least one remaining perfect square factor', 'A property unrelated to simplifying radicals', 'Been multiplied by an unrelated variable'], 0)]),
Sc('Solutions and Solubility: Concentration and Saturation',
   'Grade 9 Science Chemistry strand: a solution forms when a solute dissolves in a solvent, concentration describes the amount of solute relative to solvent, and a saturated solution has dissolved the maximum amount of solute possible at a given temperature.',
   [('A solution forms when a ___ dissolves in a solvent.', ['Solute', 'A substance that never mixes with a solvent', 'A concept unrelated to chemistry', 'Solvent, dissolving into itself'], 0),
    ('Concentration describes the amount of ___ relative to solvent in a solution.', ['Solute', 'Only the solvent, with no connection to solute', 'A property unrelated to solutions', 'Temperature exclusively'], 0),
    ('A saturated solution has dissolved ___.', ['The maximum amount of solute possible at a given temperature', 'No solute whatsoever', 'A concept unrelated to solubility', 'An unlimited amount of solute regardless of temperature'], 0),
    ('Why might increasing the temperature of a solvent, such as water, allow more solute to dissolve?', ['Higher temperatures often increase a solvent’s capacity to dissolve certain solutes', 'Temperature never affects how much solute can dissolve', 'Increasing temperature always decreases solubility for every solute', 'This concept has no connection to solubility'], 0),
    ('Which of these is an example of a solution encountered in everyday life?', ['Salt fully dissolved in water', 'Sand mixed with water that settles to the bottom', 'A concept unrelated to solutions', 'Oil floating on top of water with no mixing'], 0)]),
SS('Cartography: Map Projections and Distortion',
   'Grade 9 Social Studies (Geography) strand: a map projection is a method of representing the curved surface of the Earth on a flat map, and every projection introduces some distortion in shape, area, distance, or direction.',
   [('A map projection is best described as ___.', ['A method of representing the curved surface of the Earth on a flat map', 'A perfectly accurate photograph of the Earth', 'A concept unrelated to geography', 'A map that shows no distortion of any kind'], 0),
    ('Why does every map projection introduce some distortion?', ['Transferring a curved, three-dimensional surface onto a flat, two-dimensional map cannot be done without some trade-off', 'Map projections never introduce any distortion', 'Distortion only occurs on maps of very small areas', 'This concept has no connection to how maps are created'], 0),
    ('Which of these is a type of distortion a map projection might introduce?', ['Distortion in the relative size or area of landmasses', 'A type of distortion unrelated to maps', 'Distortion that never affects a map’s appearance', 'Perfectly accurate distances with no possible error'], 0),
    ('Why might a navigator choose a projection that preserves accurate angles and directions, even if it distorts area?', ['Accurate direction is essential for plotting a reliable course between two points', 'Navigators never consider which type of map projection to use', 'Direction and angles are never distorted on any projection', 'This choice has no connection to a map’s intended purpose'], 0),
    ('Why is understanding map projections important when interpreting a world map?', ['Recognizing a projection’s distortions helps avoid misleading conclusions about size or shape', 'All map projections represent the Earth with complete accuracy', 'This concept has no relevance to interpreting maps', 'World maps never require any special consideration when read'], 0)])]),

day(62, [
L('Writing: The Narrative Essay (Show, Don’t Tell)',
  'Grade 9 Writing strand: a narrative essay tells a true, personal story using vivid scenes and sensory detail, and the “show, don’t tell” technique conveys emotion and meaning through concrete action and imagery rather than direct statement.',
  [('The “show, don’t tell” technique conveys emotion and meaning through ___.', ['Concrete action and sensory imagery rather than direct statement', 'Simply stating a character’s feelings outright with no detail', 'A concept unrelated to narrative writing', 'Avoiding any description of actions or senses'], 0),
   ('Which sentence best demonstrates “showing” rather than “telling”?', ['Her hands trembled as she reread the acceptance letter for the third time.', 'She was very nervous and excited.', 'A sentence with no connection to showing emotion.', 'She felt many different emotions at once.'], 0),
   ('Why might a narrative essay rely on vivid sensory detail?', ['Sensory detail helps a reader experience the story’s events rather than simply being told about them', 'Sensory detail always weakens a narrative essay', 'This technique has no connection to reader engagement', 'Narrative essays should avoid any descriptive detail'], 0),
   ('A narrative essay is typically based on ___.', ['A true, personal experience', 'A completely fictional story with no connection to the writer', 'A concept unrelated to personal writing', 'A summary of someone else’s biography only'], 0),
   ('Why is choosing a specific, well-developed scene often more effective than summarizing an entire experience in a narrative essay?', ['A focused scene allows for the vivid, concrete detail that “show, don’t tell” requires', 'Summarizing an entire experience always produces a stronger narrative essay', 'Specific scenes have no connection to effective narrative writing', 'This choice has no effect on how vivid an essay feels'], 0)]),
M('Rational Exponents and Radical Notation',
  'Grade 9 Number/Algebra strand: a rational exponent expresses a root using exponent notation, such as x to the power of one-half being equivalent to the square root of x.',
  [('A rational exponent expresses a root using ___.', ['Exponent notation', 'Only radical notation, with no connection to exponents', 'A concept unrelated to algebra', 'A notation that never involves roots'], 0),
   ('x to the power of one-half is equivalent to ___.', ['The square root of x', 'x squared', 'A value unrelated to square roots', 'Half of x'], 0),
   ('x to the power of one-third is equivalent to ___.', ['The cube root of x', 'One third of x', 'A value unrelated to cube roots', 'x cubed'], 0),
   ('What is the equivalent radical form of x to the power of two-thirds?', ['The cube root of x squared', 'The square root of x cubed', 'A form unrelated to x to the power of two-thirds', 'Two-thirds of the square root of x'], 0),
   ('Why are rational exponents useful when working with expressions that combine roots and powers?', ['They allow exponent rules to be applied consistently to both roots and powers', 'Rational exponents can never be combined with exponent rules', 'This notation has no connection to simplifying expressions', 'Roots and powers can never be expressed using the same notation'], 0)]),
Sc('The Immune System and Pathogens',
   'Grade 9 Science Biology strand: the immune system defends the body against pathogens, such as bacteria and viruses, using barriers, white blood cells, and antibodies that recognize and respond to specific invaders.',
   [('A pathogen is best described as ___.', ['A microorganism, such as a bacterium or virus, that can cause disease', 'A cell that always protects the body from disease', 'A concept unrelated to biology', 'A nutrient the body requires to survive'], 0),
    ('Which of these is a barrier that helps prevent pathogens from entering the body?', ['Skin', 'A structure unrelated to the immune system', 'The circulatory system exclusively', 'Bones'], 0),
    ('White blood cells help the immune system by ___.', ['Identifying and attacking pathogens that enter the body', 'Transporting oxygen throughout the body', 'A function unrelated to the immune system', 'Producing energy for muscle movement'], 0),
    ('An antibody is best described as a molecule that ___.', ['Recognizes and helps neutralize a specific pathogen', 'Has no role in fighting disease', 'A concept unrelated to the immune system', 'Always attacks the body’s own healthy cells'], 0),
    ('Why might a vaccine help the immune system respond more quickly to a future infection?', ['It trains the immune system to recognize a specific pathogen without causing the actual disease', 'Vaccines have no effect on how the immune system responds to pathogens', 'This concept has no connection to immunity', 'Vaccines always cause the full disease they are meant to prevent'], 0)]),
SS('Time Zones and the Geography of Global Time',
   'Grade 9 Social Studies (Geography) strand: the Earth is divided into time zones based on longitude, and this system allows regions around the world to keep local time roughly aligned with the position of the sun.',
   [('Time zones are primarily based on divisions of ___.', ['Longitude', 'Latitude exclusively, with no connection to longitude', 'A concept unrelated to geography', 'Ocean currents'], 0),
    ('The purpose of dividing the Earth into time zones is to ___.', ['Keep local time roughly aligned with the position of the sun', 'Make every region on Earth share the exact same clock time', 'A purpose unrelated to time or geography', 'Eliminate the need for any standardized time system'], 0),
    ('What is the International Date Line primarily used to mark?', ['The approximate boundary where the calendar day changes', 'The boundary of a single country’s time zone', 'A concept unrelated to time zones', 'The exact centre of every time zone on Earth'], 0),
    ('Why might a country that spans a very wide range of longitude, like Canada, include multiple time zones?', ['A single time zone would cause local clock time to drift noticeably from the sun’s position across such a wide area', 'Wide countries never need more than one time zone', 'Time zones have no connection to a country’s longitude', 'Multiple time zones are chosen at random, with no geographic basis'], 0),
    ('Why is understanding time zones important for global communication and trade?', ['It helps people coordinate schedules and transactions accurately across different regions of the world', 'Time zones have no effect on global communication', 'This concept has no relevance to international trade', 'Global coordination never requires any awareness of time differences'], 0)])]),

day(63, [
L('Grammar: Appositives and Sentence Combining',
  'Grade 9 Writing strand: an appositive is a noun or noun phrase that renames or identifies another noun beside it, and using appositives allows writers to combine short, choppy sentences into more sophisticated ones.',
  [('An appositive is best described as ___.', ['A noun or noun phrase that renames or identifies another noun beside it', 'A verb that shows action within a sentence', 'A concept unrelated to grammar', 'A word that always begins a question'], 0),
   ('Which sentence correctly uses an appositive?', ['My neighbour, a retired firefighter, helped rebuild our fence.', 'My neighbour helped rebuild our fence quickly.', 'A sentence with no appositive at all.', 'My neighbour is a retired firefighter who rebuilt fences.'], 0),
   ('Why might a writer use an appositive to combine two short sentences?', ['It allows extra identifying detail to be added smoothly within a single, more sophisticated sentence', 'Appositives always make writing less clear', 'This technique has no effect on sentence structure', 'Combining sentences with appositives is never useful in writing'], 0),
   ('In the sentence “Toronto, the largest city in Canada, has a diverse population,” the appositive is ___.', ['The largest city in Canada', 'Has a diverse population', 'A phrase unrelated to the sentence’s appositive', 'Toronto has'], 0),
   ('Why are commas typically needed around an appositive in a sentence?', ['They set off the extra identifying information from the rest of the sentence', 'Commas are never used with appositives', 'This punctuation rule has no connection to appositives', 'Appositives should always be separated using a period instead'], 0)]),
M('Solving Systems of Linear Equations by Elimination',
  'Grade 9 Algebra strand: the elimination method solves a system of linear equations by adding or subtracting the equations to cancel out one variable, allowing the remaining variable to be solved directly.',
  [('The elimination method solves a system of linear equations by ___.', ['Adding or subtracting the equations to cancel out one variable', 'Graphing both equations with no algebraic calculation', 'A concept unrelated to systems of equations', 'Ignoring one of the two equations entirely'], 0),
   ('Before adding two equations using elimination, it is sometimes necessary to ___.', ['Multiply one or both equations so that a variable’s coefficients become opposites', 'Remove all variables from both equations first', 'A step unrelated to the elimination method', 'Divide both equations by zero'], 0),
   ('For the system x plus y equals 8 and x minus y equals 2, adding the equations eliminates ___.', ['y', 'x', 'A variable unrelated to this system', 'Both x and y at the same time'], 0),
   ('After eliminating one variable and solving for the other, the next step is to ___.', ['Substitute the solved value back into one of the original equations to find the remaining variable', 'Discard the solved value and start over completely', 'A step unrelated to solving systems of equations', 'Assume the remaining variable equals zero automatically'], 0),
   ('Why might the elimination method be more efficient than substitution for certain systems of equations?', ['When coefficients align well, elimination can cancel a variable directly without rearranging an equation first', 'Elimination is never more efficient than substitution in any case', 'This method has no connection to solving systems of equations', 'Elimination always requires more steps than every other method'], 0)]),
Sc('Simple Machines and Mechanical Advantage',
   'Grade 9 Science Physics strand: a simple machine, such as a lever, pulley, or inclined plane, makes work easier by changing the size or direction of an applied force, and mechanical advantage measures how much a machine multiplies that force.',
   [('A simple machine makes work easier by ___.', ['Changing the size or direction of an applied force', 'Eliminating the need for any force at all', 'A concept unrelated to physics', 'Always increasing the total amount of work required'], 0),
    ('Mechanical advantage measures ___.', ['How much a machine multiplies an applied force', 'The total distance an object travels, with no connection to force', 'A concept unrelated to simple machines', 'The weight of the machine itself'], 0),
    ('Which of these is an example of a simple machine?', ['A lever', 'A smartphone', 'A concept unrelated to simple machines', 'A battery'], 0),
    ('Why might a longer lever arm increase the mechanical advantage of a lever?', ['A longer arm allows a smaller applied force to lift a heavier load around the fulcrum', 'Lever arm length never affects mechanical advantage', 'A longer lever arm always decreases mechanical advantage', 'This concept has no connection to how levers work'], 0),
    ('Why might a pulley system be used to lift heavy objects, such as at a construction site?', ['It can reduce the amount of force needed to lift a load by redirecting or multiplying that force', 'Pulley systems always increase the force required to lift an object', 'This concept has no real-world application', 'Pulleys have no connection to mechanical advantage'], 0)]),
SS('Geography of Urban Heat Islands',
   'Grade 9 Social Studies (Geography) strand: an urban heat island occurs when a city experiences significantly higher temperatures than its surrounding rural areas, largely due to pavement, buildings, and reduced vegetation absorbing and retaining heat.',
   [('An urban heat island occurs when a city experiences ___.', ['Significantly higher temperatures than its surrounding rural areas', 'Significantly lower temperatures than its surrounding rural areas', 'A concept unrelated to urban geography', 'No measurable temperature difference from rural areas'], 0),
    ('Which of these commonly contributes to the urban heat island effect?', ['Large areas of pavement and buildings that absorb and retain heat', 'Extensive tree cover and open green space', 'A factor unrelated to urban temperature patterns', 'Cold ocean currents surrounding the city'], 0),
    ('Why does reduced vegetation in a city contribute to higher urban temperatures?', ['Plants normally provide shade and release moisture that helps cool the surrounding air', 'Vegetation always increases a city’s overall temperature', 'Reduced vegetation has no effect on urban temperature', 'This concept has no connection to urban heat islands'], 0),
    ('Which strategy might a city use to help reduce the urban heat island effect?', ['Increasing green spaces and planting more trees', 'Replacing existing green spaces with additional pavement', 'A strategy unrelated to reducing urban temperatures', 'Removing all rooftop and building insulation'], 0),
    ('Why is the urban heat island effect an important consideration for city planners?', ['Higher urban temperatures can increase energy use and pose health risks during heat waves', 'Urban heat islands have no effect on residents’ health or energy use', 'This topic has no relevance to city planning', 'Urban temperature patterns never need to be considered by planners'], 0)])]),

day(64, [
L('Vocabulary: Etymology and Word Roots',
  'Grade 9 Language strand: etymology is the study of a word’s origin and historical development, and recognizing common Greek and Latin roots can help readers determine the meaning of unfamiliar words.',
  [('Etymology is best described as the study of ___.', ['A word’s origin and historical development', 'A word’s pronunciation only, with no connection to meaning', 'A concept unrelated to vocabulary', 'The number of syllables in a word'], 0),
   ('The Greek root “bio” most closely relates to the meaning ___.', ['Life', 'Water', 'A meaning unrelated to this root', 'Light'], 0),
   ('Knowing that the Latin root “dict” relates to “speak” or “say” would most help a reader understand the word ___.', ['Predict', 'Reptile', 'A word unrelated to this root', 'Aquarium'], 0),
   ('Why is recognizing common word roots a useful reading strategy?', ['It can help a reader infer the meaning of unfamiliar words that share a similar root', 'Word roots never provide any clues about meaning', 'This strategy has no connection to vocabulary development', 'Every word’s meaning is entirely unrelated to its root'], 0),
   ('The word “transport” combines the roots “trans” (across) and “port” (carry), so it most literally means ___.', ['To carry across', 'To carry nothing at all', 'A meaning unrelated to these two roots', 'To stay in one place'], 0)]),
M('Function Notation, Domain, and Range',
  'Grade 9 Algebra strand (non-linear relations): function notation, such as f(x), represents the output of a function for a given input x, while the domain is the set of all possible input values and the range is the set of all possible output values.',
  [('Function notation, such as f(x), represents ___.', ['The output of a function for a given input x', 'Only the input value, with no connection to output', 'A concept unrelated to functions', 'A fixed constant that never changes'], 0),
   ('The domain of a function refers to ___.', ['The set of all possible input values', 'The set of all possible output values', 'A concept unrelated to functions', 'A single specific output value only'], 0),
   ('The range of a function refers to ___.', ['The set of all possible output values', 'The set of all possible input values', 'A concept unrelated to functions', 'A single specific input value only'], 0),
   ('If f(x) equals x squared, what is f(3)?', ['9', '6', 'A value unrelated to this function', '3'], 0),
   ('Why might the domain of a function involving a square root be restricted to non-negative values?', ['The square root of a negative number is not a real number, so those inputs must be excluded', 'Square root functions never have any domain restrictions', 'This concept has no connection to domain and range', 'Negative numbers always produce valid real outputs under a square root'], 0)]),
Sc('Light: Reflection and Refraction',
   'Grade 9 Science Physics strand: reflection occurs when light bounces off a surface, while refraction occurs when light bends as it passes from one medium into another with a different density, such as from air into water.',
   [('Reflection occurs when light ___.', ['Bounces off a surface', 'Bends as it passes into a new medium', 'A concept unrelated to light', 'Is completely absorbed with no remaining energy'], 0),
    ('Refraction occurs when light ___.', ['Bends as it passes from one medium into another with a different density', 'Bounces directly off a surface with no change in direction', 'A concept unrelated to light', 'Disappears entirely upon entering a new medium'], 0),
    ('Which of these is a real-world example of refraction?', ['A straw appearing bent when placed in a glass of water', 'A mirror showing a clear reflection of a person’s face', 'A concept unrelated to refraction', 'A shadow forming behind an object blocking light'], 0),
    ('According to the law of reflection, the angle of incidence is ___ the angle of reflection.', ['Equal to', 'Always greater than', 'A relationship unrelated to reflection', 'Always less than'], 0),
    ('Why does light bend when it passes from air into water?', ['Light changes speed as it moves between materials with different densities, causing its path to bend', 'Light never changes speed when moving between different materials', 'This concept has no connection to refraction', 'Light always travels in a perfectly straight line regardless of the medium'], 0)]),
SS('The Geography of Wildfire Risk and Management',
   'Grade 9 Social Studies (Geography) strand: wildfire risk is shaped by geographic factors such as climate, vegetation, and terrain, and effective wildfire management combines prevention strategies with rapid response to protect communities and ecosystems.',
   [('Wildfire risk is shaped by geographic factors such as ___.', ['Climate, vegetation, and terrain', 'A factor entirely unrelated to geography', 'Only the time of year, with no other geographic influence', 'The presence of large bodies of water exclusively'], 0),
    ('Why might a prolonged drought increase the risk of wildfires in a region?', ['Dry vegetation and soil can ignite and spread fire more easily', 'Drought conditions always decrease the likelihood of wildfires', 'This factor has no connection to wildfire risk', 'Wildfires only occur in regions with abundant rainfall'], 0),
    ('Which of these is a common wildfire prevention strategy?', ['Controlled burns that reduce the buildup of flammable vegetation', 'Allowing flammable vegetation to accumulate indefinitely with no management', 'A strategy unrelated to wildfire management', 'Increasing the density of dry vegetation near communities'], 0),
    ('Why might steep, hilly terrain make wildfires more difficult to control?', ['Fire can spread more quickly uphill, and difficult terrain can limit firefighter access', 'Terrain has no effect on how quickly a wildfire spreads', 'Fire always spreads more slowly on steep terrain', 'Hilly terrain always makes wildfires easier to access and control'], 0),
    ('Why is wildfire management an increasingly important geographic issue in many regions?', ['Changing climate patterns and expanding development near forests can increase both wildfire risk and its impact on communities', 'Wildfire risk has remained completely unchanged in recent decades', 'This topic has no relevance to geography or climate', 'Wildfires never pose any risk to nearby communities'], 0)])]),

day(65, [
L('Reading: Analyzing Direct and Indirect Characterization',
  'Grade 9 Reading strand: direct characterization occurs when a narrator explicitly states a character’s traits, while indirect characterization reveals traits through a character’s actions, dialogue, thoughts, and how other characters respond to them.',
  [('Direct characterization occurs when ___.', ['A narrator explicitly states a character’s traits', 'A character’s traits are only revealed through their actions', 'A concept unrelated to characterization', 'No information about a character is ever provided'], 0),
   ('Indirect characterization reveals a character’s traits through ___.', ['Their actions, dialogue, thoughts, and how others respond to them', 'A narrator directly stating those traits outright', 'A concept unrelated to characterization', 'A method that never involves a character’s behaviour'], 0),
   ('Which of these is an example of indirect characterization?', ['A character slamming a door and refusing to speak to anyone for the rest of the day', 'The narrator stating, “She was furious.”', 'A concept unrelated to characterization', 'A list of a character’s traits with no supporting detail'], 0),
   ('Why might an author rely more on indirect characterization than direct characterization?', ['It allows readers to infer traits themselves, often creating a more engaging reading experience', 'Indirect characterization always makes a story less engaging', 'This technique has no effect on how readers understand a character', 'Authors never intentionally choose between these two methods'], 0),
   ('Why might how other characters react to a character reveal something about that character’s traits?', ['Other characters’ responses can reflect qualities the character possesses, even without a direct statement', 'Other characters’ reactions never provide any insight into a character’s traits', 'This concept has no connection to indirect characterization', 'A character’s traits can only be revealed through direct statement'], 0)]),
M('Surface Area and Volume of Spheres and Cones',
  'Grade 9 Measurement strand: the surface area and volume of a sphere or cone can be calculated using specific formulas involving the radius, and, for a cone, its height and slant height.',
  [('The volume of a sphere can be calculated using a formula involving its ___.', ['Radius', 'Only its diameter, with no connection to radius', 'A concept unrelated to measurement', 'Surface area exclusively, with no formula needed'], 0),
   ('The volume of a cone depends on its radius and its ___.', ['Height', 'Colour', 'A property unrelated to volume', 'Weight'], 0),
   ('If a sphere has a radius of 3 cm, which value is needed to find its volume using the formula four-thirds pi r cubed?', ['The radius cubed', 'The radius squared only, with no cubing involved', 'A value unrelated to this formula', 'The diameter squared'], 0),
   ('The surface area of a cone includes the area of its circular base plus ___.', ['The lateral (slanted) surface area', 'Only the height of the cone, with no area calculation', 'A concept unrelated to surface area', 'The volume of the cone'], 0),
   ('Why might an engineer need to calculate the volume of a spherical or conical storage tank?', ['To determine how much material the tank can hold', 'Volume calculations have no practical engineering application', 'This concept has no connection to real-world storage design', 'Tank shape never affects how much it can hold'], 0)]),
Sc('The Circulatory and Respiratory Systems',
   'Grade 9 Science Biology strand: the circulatory system transports blood, oxygen, and nutrients throughout the body via the heart and blood vessels, while the respiratory system brings oxygen into the body and removes carbon dioxide through the lungs.',
   [('The circulatory system is primarily responsible for ___.', ['Transporting blood, oxygen, and nutrients throughout the body', 'Breaking down food for digestion', 'A function unrelated to body systems', 'Producing hormones exclusively'], 0),
    ('The respiratory system brings oxygen into the body through the ___.', ['Lungs', 'Stomach', 'An organ unrelated to respiration', 'Kidneys'], 0),
    ('Which organ pumps blood throughout the circulatory system?', ['The heart', 'The liver', 'An organ unrelated to circulation', 'The pancreas'], 0),
    ('Why must the circulatory and respiratory systems work closely together?', ['Oxygen absorbed by the lungs must be transported by the blood to cells throughout the body', 'These two systems never interact with one another', 'This concept has no connection to how the body functions', 'The respiratory system operates completely independently of blood transport'], 0),
    ('Why does the body exhale carbon dioxide through the respiratory system?', ['Carbon dioxide is a waste product of cellular respiration that must be removed from the body', 'Carbon dioxide is a nutrient the body needs to retain', 'This concept has no connection to respiration', 'The body never produces carbon dioxide as a waste product'], 0)]),
SS('Political Geography: Federal, Provincial, and Municipal Boundaries in Canada',
   'Grade 9 Social Studies (Geography) strand: political geography examines how administrative boundaries, such as Canada’s federal, provincial, and municipal levels, divide authority and responsibility across different regions of a country.',
   [('Political geography examines how administrative boundaries divide ___.', ['Authority and responsibility across different regions of a country', 'Physical landforms with no connection to governance', 'A concept unrelated to geography', 'Only natural boundaries like rivers and mountains'], 0),
    ('In Canada, which level of government is generally responsible for national issues such as defence and foreign affairs?', ['The federal government', 'The municipal government', 'A level of government unrelated to Canada’s political structure', 'The provincial government exclusively, with no federal role'], 0),
    ('Which of these is typically a responsibility of provincial governments in Canada?', ['Education and healthcare', 'National defence', 'A responsibility unrelated to provincial government', 'Foreign diplomacy'], 0),
    ('Municipal governments in Canada are typically responsible for services such as ___.', ['Local roads, waste collection, and public transit', 'National immigration policy', 'A responsibility unrelated to municipal government', 'International trade agreements'], 0),
    ('Why might understanding the different levels of political boundaries help explain how decisions are made in Canada?', ['Different levels of government have distinct authority over specific issues within their geographic jurisdiction', 'All levels of government in Canada have identical responsibilities', 'Political boundaries have no connection to how decisions are made', 'This topic has no relevance to understanding Canadian geography'], 0)])]),

day(66, [
L('Media Literacy: Analyzing Advertising Techniques and Persuasion',
  'Grade 9 Media Literacy strand: advertisements use persuasive techniques, such as appeals to emotion, celebrity endorsement, and bandwagon appeal, to influence a consumer’s attitudes and purchasing decisions.',
  [('Advertisements often use persuasive techniques to influence a consumer’s ___.', ['Attitudes and purchasing decisions', 'Ability to read, with no connection to persuasion', 'A concept unrelated to media literacy', 'Personal identity in ways that are never intentional'], 0),
   ('Bandwagon appeal in advertising suggests that a consumer should buy a product because ___.', ['Many other people are already using or buying it', 'No one else has ever purchased the product', 'A concept unrelated to persuasive advertising', 'The product has been scientifically proven ineffective'], 0),
   ('Which of these is an example of an emotional appeal in advertising?', ['An ad showing a heartwarming family reunion to promote a phone brand', 'An ad listing only the technical specifications of a product', 'A concept unrelated to advertising techniques', 'An ad providing no persuasive content of any kind'], 0),
   ('Why might a company use a celebrity endorsement in an advertisement?', ['Association with a well-known, admired figure can make a product seem more appealing or trustworthy', 'Celebrity endorsements never influence a consumer’s perception of a product', 'This technique has no connection to persuasive advertising', 'Companies always avoid featuring well-known figures in ads'], 0),
   ('Why is it important to critically evaluate advertising techniques rather than accepting a message at face value?', ['Recognizing persuasive techniques helps consumers make more informed decisions rather than being simply influenced by emotion', 'Critically evaluating advertisements never changes how a consumer responds', 'This skill has no relevance to media literacy', 'Advertisements never attempt to persuade their audience'], 0)]),
M('Financial Literacy: Currency Exchange and Purchasing Power',
  'Grade 9 Financial Literacy strand: currency exchange rates determine how much one country’s currency is worth in terms of another, and purchasing power describes how much a given amount of money can actually buy.',
  [('A currency exchange rate determines ___.', ['How much one country’s currency is worth in terms of another', 'The total population of a country', 'A concept unrelated to finance', 'A fixed value that never changes over time'], 0),
   ('Purchasing power describes ___.', ['How much a given amount of money can actually buy', 'The total amount of money a person earns in a year', 'A concept unrelated to currency or spending', 'The exact exchange rate between two currencies'], 0),
   ('If 1 Canadian dollar can be exchanged for 0.75 US dollars, how many US dollars would 100 Canadian dollars be worth?', ['75 US dollars', '100 US dollars', 'A value unrelated to this exchange rate', '125 US dollars'], 0),
   ('Why might a traveller’s purchasing power change when visiting a country with a different currency?', ['The exchange rate determines how much local currency, and therefore goods, their money can obtain', 'Purchasing power never changes based on currency exchange', 'This concept has no connection to international travel', 'Exchange rates have no effect on how much a traveller can buy'], 0),
   ('Why do businesses that trade internationally need to monitor currency exchange rates closely?', ['Fluctuating exchange rates can significantly affect the cost of imports and the value of international sales', 'Exchange rates have no impact on international business', 'This concept has no connection to global trade', 'Businesses never need to consider currency values when trading internationally'], 0)]),
Sc('Radioactivity and Half-Life',
   'Grade 9 Science Chemistry/Physics strand: radioactive decay occurs when an unstable atomic nucleus releases energy and particles over time, and an isotope’s half-life is the time it takes for half of a radioactive sample to decay.',
   [('Radioactive decay occurs when ___.', ['An unstable atomic nucleus releases energy and particles over time', 'An atom becomes permanently stable with no further change', 'A concept unrelated to atomic structure', 'A molecule dissolves completely in a solvent'], 0),
    ('An isotope’s half-life refers to ___.', ['The time it takes for half of a radioactive sample to decay', 'The total time before any decay begins', 'A concept unrelated to radioactivity', 'The complete lifespan of every atom in a sample'], 0),
    ('If an isotope has a half-life of 10 years, how much of an original sample remains after 20 years?', ['One quarter of the original sample', 'Half of the original sample', 'A value unrelated to this half-life', 'None of the original sample'], 0),
    ('Which of these is a practical application of understanding radioactive half-life?', ['Using radiocarbon dating to estimate the age of ancient organic materials', 'An application unrelated to radioactivity', 'Radioactivity has no practical, real-world uses', 'Half-life calculations are never used outside of theoretical chemistry'], 0),
    ('Why is radioactive material considered potentially hazardous to living organisms?', ['The energy and particles released during decay can damage living cells and tissue', 'Radioactive decay never has any effect on living organisms', 'This concept has no connection to radioactivity', 'Radioactive material is always completely harmless to living cells'], 0)]),
SS('Geography of Cultural Landscapes and Heritage Sites',
   'Grade 9 Social Studies (Geography) strand: a cultural landscape reflects the interaction between people and their environment over time, and heritage sites are recognized and protected for their historical, cultural, or natural significance.',
   [('A cultural landscape reflects ___.', ['The interaction between people and their environment over time', 'A landscape entirely untouched by human activity', 'A concept unrelated to geography', 'Only natural features with no human influence'], 0),
    ('A heritage site is typically recognized and protected for its ___.', ['Historical, cultural, or natural significance', 'Economic value exclusively, with no other significance', 'A concept unrelated to heritage protection', 'Complete lack of historical or cultural importance'], 0),
    ('Which of these is an example of a cultural landscape?', ['Terraced rice fields shaped by generations of farming practices', 'A landscape with absolutely no connection to human activity', 'A concept unrelated to cultural geography', 'An uninhabited region never altered by people'], 0),
    ('Why might a community work to protect a local heritage site?', ['To preserve its historical or cultural significance for future generations', 'Heritage sites are never considered worth protecting', 'This concept has no connection to cultural geography', 'Communities always prioritize development over heritage preservation'], 0),
    ('Why do geographers study cultural landscapes when examining a region?', ['They reveal how human activity and the natural environment have shaped each other over time', 'Cultural landscapes have no connection to a region’s geography', 'This topic has no relevance to studying human-environment interaction', 'Geographers never consider the influence of human activity on landscapes'], 0)])]),

day(67, [
L('Writing: The Business Letter and Email Etiquette',
  'Grade 9 Writing strand: a business letter or professional email follows a clear, formal structure and tone, including a proper greeting, concise purpose, and polite closing, appropriate for communicating in academic or workplace settings.',
  [('A business letter or professional email should generally use a ___ tone.', ['Clear, formal, and polite', 'Casual and full of slang', 'A concept unrelated to professional writing', 'Overly emotional and unstructured'], 0),
   ('Which of these is an appropriate greeting for a formal business email?', ['Dear Ms. Chen,', 'Hey there,', 'A greeting unrelated to professional communication', 'Yo,'], 0),
   ('Why should a professional email state its purpose clearly and concisely near the beginning?', ['It respects the reader’s time and ensures the main point is not missed', 'Clarity is never important in professional communication', 'This concept has no connection to email etiquette', 'A purpose should always be buried at the very end of a message'], 0),
   ('Which of these is an example of a polite, professional closing?', ['Sincerely,', 'See ya,', 'A closing unrelated to professional writing', 'Whatever,'], 0),
   ('Why is proofreading especially important before sending a formal business email?', ['Errors can create an unprofessional impression and undermine the message’s credibility', 'Proofreading has no effect on how a professional email is received', 'This step is never necessary for business communication', 'Spelling and grammar mistakes always improve a message’s credibility'], 0)]),
M('Probability Distributions and Expected Value',
  'Grade 9 Data Management strand: a probability distribution shows all possible outcomes of an event along with their probabilities, and expected value is the long-run average outcome calculated by weighting each outcome by its probability.',
  [('A probability distribution shows ___.', ['All possible outcomes of an event along with their probabilities', 'Only the single most likely outcome, with no other information', 'A concept unrelated to probability', 'The total number of trials conducted, with no connection to outcomes'], 0),
   ('Expected value is calculated by ___.', ['Weighting each possible outcome by its probability and summing the results', 'Choosing the outcome with the highest individual probability only', 'A concept unrelated to probability distributions', 'Adding all outcomes together with no consideration of probability'], 0),
   ('If a game gives a 50 percent chance of winning 10 dollars and a 50 percent chance of winning nothing, what is the expected value?', ['5 dollars', '10 dollars', 'A value unrelated to this probability distribution', '0 dollars'], 0),
   ('Why is expected value described as a long-run average rather than a guaranteed outcome for any single event?', ['Expected value predicts the average result over many repeated trials, not any one specific outcome', 'Expected value always guarantees the exact same result every single time', 'This concept has no connection to probability', 'A single trial always matches the calculated expected value exactly'], 0),
   ('Why might a business use expected value when deciding whether a risky investment is worthwhile?', ['It helps estimate the average financial outcome across many possible scenarios', 'Expected value has no practical application in business decisions', 'This concept has no connection to evaluating risk', 'Businesses never use probability when making financial decisions'], 0)]),
Sc('Ocean Currents and Their Effect on Climate',
   'Grade 9 Science Earth and Space Systems strand: ocean currents are large-scale movements of seawater driven by wind, temperature, and salinity differences, and they play a major role in distributing heat and shaping regional climate patterns.',
   [('Ocean currents are large-scale movements of seawater driven by factors such as ___.', ['Wind, temperature, and salinity differences', 'A factor entirely unrelated to ocean water movement', 'Only the position of the moon, with no other influence', 'Random, unpredictable movement with no identifiable cause'], 0),
    ('Ocean currents play a major role in distributing ___ around the planet.', ['Heat', 'Only sunlight, with no connection to temperature', 'A factor unrelated to climate', 'Land elevation'], 0),
    ('A warm ocean current flowing toward a coastal region generally has what effect on nearby land temperatures?', ['It tends to warm the climate of that coastal region', 'It always cools the climate of that coastal region significantly', 'A concept unrelated to ocean currents', 'It has no effect whatsoever on nearby land temperatures'], 0),
    ('Why might a disruption to a major ocean current, such as changes linked to climate change, significantly affect regional weather patterns?', ['Ocean currents help regulate heat distribution, so changes to them can shift established climate patterns', 'Ocean currents have no connection to regional weather or climate', 'Disruptions to ocean currents never have any noticeable effects', 'This concept has no relevance to studying Earth systems'], 0),
    ('Why do scientists study ocean currents when researching global climate systems?', ['Currents significantly influence how heat and energy are distributed across the planet', 'Ocean currents are considered irrelevant to global climate research', 'This topic has no connection to Earth and space systems', 'Climate patterns are never influenced by ocean water movement'], 0)]),
SS('The Geography of Urban Food Deserts',
   'Grade 9 Social Studies (Geography) strand: an urban food desert is an area, often within a city, where residents have limited access to affordable, healthy food due to a lack of nearby grocery stores or fresh food retailers.',
   [('An urban food desert is best described as an area where residents have limited access to ___.', ['Affordable, healthy food', 'Any form of transportation', 'A concept unrelated to urban geography', 'Unlimited amounts of fresh food from every nearby store'], 0),
    ('A common contributing factor to urban food deserts is ___.', ['A lack of nearby grocery stores or fresh food retailers', 'An abundance of grocery stores offering only fresh produce', 'A factor unrelated to food access', 'Excessive regulation preventing any food sales in a city'], 0),
    ('Why might residents of a food desert rely more heavily on convenience stores or fast food?', ['These options may be more accessible nearby than stores offering fresh, affordable groceries', 'Convenience stores are always the healthiest available option', 'This factor has no connection to food access in a neighbourhood', 'Residents in food deserts always have equal access to every type of food retailer'], 0),
    ('Which strategy might a city use to help address a food desert?', ['Supporting the development of a new grocery store or community garden in an underserved area', 'Removing existing grocery stores from underserved neighbourhoods', 'A strategy unrelated to addressing food access', 'Ignoring the issue of food access entirely'], 0),
    ('Why is studying urban food deserts relevant to understanding geographic inequality within cities?', ['It shows how access to essential resources like food can vary significantly between neighbourhoods in the same city', 'Food access is always identical across every neighbourhood in a city', 'This topic has no connection to geographic inequality', 'Urban geography never considers differences in resource access'], 0)])]),

day(68, [
L('Grammar: Active and Passive Voice',
  'Grade 9 Writing strand: in the active voice, the subject of a sentence performs the action, while in the passive voice, the subject receives the action, often shifting emphasis and requiring a form of the verb “to be.”',
  [('In the active voice, the subject of a sentence ___.', ['Performs the action', 'Always receives the action', 'A concept unrelated to grammar', 'Is never mentioned in the sentence'], 0),
   ('In the passive voice, the subject of a sentence ___.', ['Receives the action', 'Always performs the action', 'A concept unrelated to grammar', 'Is always the same as the object'], 0),
   ('Which sentence is written in the active voice?', ['The committee approved the new policy.', 'The new policy was approved by the committee.', 'A sentence with no clear subject performing an action.', 'The policy, approved previously, exists now.'], 0),
   ('Why might a writer choose the passive voice when the person performing an action is unknown or unimportant?', ['It allows the sentence to focus on the action or the receiver of the action instead of the performer', 'The passive voice always requires naming the performer of the action', 'This choice has no effect on a sentence’s emphasis', 'Passive voice is never appropriate in any writing situation'], 0),
   ('Why is active voice often preferred in clear, direct writing, such as many business or academic contexts?', ['It typically produces more concise, direct sentences than the passive voice', 'Active voice always makes writing less clear', 'This concept has no connection to effective writing', 'Passive voice is always shorter and more direct than active voice'], 0)]),
M('Introduction to Logarithms as Inverse of Exponents',
  'Grade 9 Algebra strand (enrichment): a logarithm answers the question of what exponent a given base must be raised to in order to produce a certain number, making logarithms the inverse operation of exponentiation.',
  [('A logarithm answers the question of ___.', ['What exponent a given base must be raised to in order to produce a certain number', 'What number results from multiplying a base by itself repeatedly with no exponent involved', 'A concept unrelated to exponents', 'What the square root of a number is'], 0),
   ('Logarithms are considered the inverse operation of ___.', ['Exponentiation', 'Addition', 'A concept unrelated to logarithms', 'Subtraction'], 0),
   ('What is the value of log base 2 of 8?', ['3, since 2 to the power of 3 equals 8', '8, since 2 to the power of 8 equals a much larger number', 'A value unrelated to this logarithm', '4, since 2 times 4 equals 8'], 0),
   ('If log base 10 of 1000 equals 3, this means ___.', ['10 to the power of 3 equals 1000', '10 divided by 3 equals 1000', 'A relationship unrelated to this logarithm', '3 to the power of 10 equals 1000'], 0),
   ('Why are logarithms useful for solving equations where the unknown variable is an exponent?', ['They allow the exponent itself to be isolated and solved for directly', 'Logarithms can never be used to solve equations involving exponents', 'This concept has no connection to exponential equations', 'Logarithms only apply to equations with no exponents at all'], 0)]),
Sc('Friction, Air Resistance, and Terminal Velocity',
   'Grade 9 Science Physics strand: friction is a force that opposes motion between surfaces in contact, air resistance is a form of friction from air molecules, and terminal velocity occurs when a falling object’s speed becomes constant as air resistance balances gravity.',
   [('Friction is best described as a force that ___.', ['Opposes motion between surfaces in contact', 'Always increases an object’s speed', 'A concept unrelated to physics', 'Has no effect on moving objects'], 0),
    ('Air resistance is a form of friction caused by ___.', ['Air molecules interacting with a moving object', 'A vacuum with no molecules present at all', 'A concept unrelated to friction', 'Gravity acting alone, with no connection to air'], 0),
    ('Terminal velocity occurs when a falling object’s speed becomes ___.', ['Constant, as air resistance balances the force of gravity', 'Continuously increasing with no upper limit', 'A concept unrelated to falling objects', 'Zero, as the object stops moving entirely'], 0),
    ('Why might a skydiver reach terminal velocity before opening a parachute?', ['Air resistance eventually increases enough to balance the force of gravity pulling them downward', 'Gravity stops acting on the skydiver at a certain height', 'This concept has no connection to falling objects', 'Air resistance has no effect on a skydiver’s speed'], 0),
    ('Why does a flat sheet of paper fall more slowly than a crumpled ball of the same paper?', ['The flat sheet has more surface area, increasing air resistance and slowing its fall', 'Surface area has no effect on how air resistance acts on a falling object', 'This concept has no connection to friction or air resistance', 'A crumpled ball always experiences greater air resistance than a flat sheet'], 0)]),
SS('Geography of Space Exploration and Satellite Technology',
   'Grade 9 Social Studies (Geography) strand: space exploration and satellite technology rely on carefully chosen launch sites and orbital paths, and satellites support geographic applications such as weather forecasting, communication, and Earth observation.',
   [('The choice of a launch site for space exploration is often influenced by geographic factors such as ___.', ['Proximity to the equator and access to open airspace or ocean', 'A factor entirely unrelated to geography', 'Only the average temperature of a region, with no other consideration', 'The presence of large freshwater lakes exclusively'], 0),
    ('Satellites in orbit around Earth support geographic applications such as ___.', ['Weather forecasting and Earth observation', 'A function unrelated to geography', 'Only entertainment broadcasting, with no other purpose', 'Underground mineral extraction'], 0),
    ('Why might launch sites located closer to the equator provide an advantage for certain space launches?', ['The Earth’s rotational speed is greatest near the equator, providing an added boost to a launched rocket', 'Equatorial regions always have the coldest possible launch conditions', 'This factor has no connection to launching satellites or spacecraft', 'Proximity to the equator always makes a launch site less effective'], 0),
    ('How do weather satellites benefit geographic study and forecasting?', ['They provide continuous images and data used to track and predict weather patterns', 'Weather satellites have no connection to forecasting', 'This technology has no relevance to geography', 'Satellites only track ocean currents, with no connection to weather'], 0),
    ('Why is satellite technology considered valuable for geographic research on a global scale?', ['It allows continuous observation of large or remote areas of the Earth that would be difficult to study directly', 'Satellite technology has no practical use in geographic research', 'This concept has no connection to studying the Earth’s surface', 'Remote or large areas can never be studied using satellite data'], 0)])]),

day(69, [
L('Reading: Analyzing Flashback and Foreshadowing',
  'Grade 9 Reading strand: a flashback interrupts a story’s present action to show an earlier event, while foreshadowing hints at events that will occur later, and both techniques shape a reader’s understanding of a narrative’s timeline and meaning.',
  [('A flashback is best described as a technique that ___.', ['Interrupts a story’s present action to show an earlier event', 'Reveals events that will occur later in the story', 'A concept unrelated to narrative structure', 'Always occurs at the very end of a story'], 0),
   ('Foreshadowing is best described as a technique that ___.', ['Hints at events that will occur later in a story', 'Interrupts the story to reveal a past event', 'A concept unrelated to narrative structure', 'Removes any sense of suspense from a story'], 0),
   ('Which is an example of foreshadowing?', ['A character noticing dark storm clouds gathering just before a major conflict begins', 'A character recalling their childhood in a scene set entirely in the past', 'A concept unrelated to foreshadowing', 'A scene with no connection to future events in the story'], 0),
   ('Why might an author use a flashback rather than simply telling events in chronological order?', ['A flashback can provide important context or background at a moment when it is most meaningful to the reader', 'Flashbacks are never used intentionally by authors', 'This technique always confuses a reader with no narrative purpose', 'Chronological order is always required in every story'], 0),
   ('Why does recognizing foreshadowing enhance a reader’s engagement with a story?', ['It can build anticipation and reward readers who notice subtle clues about what is to come', 'Foreshadowing has no effect on how a reader experiences a story', 'This technique never connects to later events in a narrative', 'Recognizing foreshadowing always reduces a story’s suspense'], 0)]),
M('Introduction to Matrices: Rows, Columns, and Operations',
  'Grade 9 Algebra strand (enrichment): a matrix is a rectangular array of numbers organized into rows and columns, and matrices can be added, subtracted, or multiplied following specific rules based on their dimensions.',
  [('A matrix is best described as ___.', ['A rectangular array of numbers organized into rows and columns', 'A single number with no structure', 'A concept unrelated to algebra', 'A type of graph with no numerical values'], 0),
   ('The dimensions of a matrix are described using its number of ___.', ['Rows and columns', 'Only its total value, with no reference to structure', 'A property unrelated to matrices', 'Diagonals exclusively'], 0),
   ('To add two matrices together, they must ___.', ['Have the same dimensions', 'Always have completely different dimensions', 'A requirement unrelated to matrix addition', 'Contain only positive numbers'], 0),
   ('In a matrix with 2 rows and 3 columns, how many total entries does the matrix contain?', ['6', '5', 'A value unrelated to this matrix’s dimensions', '2'], 0),
   ('Why might matrices be useful for organizing and solving real-world data problems?', ['They allow large sets of related numerical data to be organized and manipulated systematically', 'Matrices have no practical application for organizing data', 'This concept has no connection to solving real-world problems', 'Numerical data can never be represented using rows and columns'], 0)]),
Sc('Enzymes and Biological Catalysts',
   'Grade 9 Science Biology strand: an enzyme is a biological catalyst, typically a protein, that speeds up chemical reactions in living organisms without being consumed in the process.',
   [('An enzyme is best described as ___.', ['A biological catalyst that speeds up chemical reactions in living organisms', 'A molecule that always slows down chemical reactions', 'A concept unrelated to biology', 'A type of cell found only in plants'], 0),
    ('Enzymes are typically composed of ___.', ['Proteins', 'Only water molecules, with no other component', 'A substance unrelated to biological catalysts', 'Pure carbon with no other elements'], 0),
    ('A defining feature of an enzyme is that it ___.', ['Is not consumed or permanently changed during the reaction it catalyzes', 'Is always destroyed after catalyzing a single reaction', 'A feature unrelated to how enzymes function', 'Slows down every reaction it interacts with'], 0),
    ('Why might an enzyme’s shape be important to its function?', ['Its shape allows it to bind specifically to a particular substrate molecule', 'An enzyme’s shape has no connection to its function', 'Enzymes can bind to any molecule regardless of shape', 'This concept has no relevance to biological catalysts'], 0),
    ('Why might extreme heat cause an enzyme to stop functioning properly?', ['High temperatures can change an enzyme’s shape, preventing it from binding to its substrate', 'Heat never has any effect on an enzyme’s structure or function', 'This concept has no connection to enzyme activity', 'Enzymes always function more effectively at extremely high temperatures'], 0)]),
SS('Geography of Light and Noise Pollution in Cities',
   'Grade 9 Social Studies (Geography) strand: light and noise pollution are byproducts of urban development that can disrupt ecosystems, obscure the night sky, and affect the health and well-being of city residents.',
   [('Light and noise pollution are commonly associated with ___.', ['Urban development', 'Entirely untouched, uninhabited wilderness', 'A concept unrelated to urban geography', 'Regions with no human population whatsoever'], 0),
    ('Light pollution can make it more difficult for city residents to ___.', ['See stars and other objects in the night sky', 'See during the daytime', 'A concept unrelated to light pollution', 'Access electricity in their homes'], 0),
    ('Why might excessive noise pollution in a city affect residents’ well-being?', ['Persistent noise can contribute to stress and disrupted sleep', 'Noise pollution never has any effect on human health', 'This concept has no connection to urban geography', 'Noise pollution always improves residents’ overall well-being'], 0),
    ('How might light pollution disrupt local ecosystems?', ['Artificial light can interfere with the natural behaviour of nocturnal animals, such as migration or feeding patterns', 'Light pollution has no effect on animal behaviour', 'This concept has no connection to ecosystems', 'Nocturnal animals are never affected by artificial lighting'], 0),
    ('Which strategy might a city use to help reduce light pollution?', ['Using shielded outdoor lighting that directs light downward rather than outward', 'Increasing the number of unshielded lights throughout the city', 'A strategy unrelated to reducing light pollution', 'Removing all lighting regulations entirely'], 0)])]),

day(70, [
L('Review: Setting, Characterization, Advertising, and Active/Passive Voice',
  'Grade 9 Reading and Writing strands review: this lesson revisits analyzing setting, direct and indirect characterization, advertising persuasion techniques, and active and passive voice from Days 61-69.',
  [('A story’s setting refers to ___.', ['The time and place in which a story occurs', 'Only the names of the characters involved', 'A concept unrelated to literary analysis', 'The order in which events are told'], 0),
   ('Direct characterization occurs when ___.', ['A narrator explicitly states a character’s traits', 'A character’s traits are only revealed through their actions', 'A concept unrelated to characterization', 'No information about a character is ever provided'], 0),
   ('Bandwagon appeal in advertising suggests that a consumer should buy a product because ___.', ['Many other people are already using or buying it', 'No one else has ever purchased the product', 'A concept unrelated to persuasive advertising', 'The product has been scientifically proven ineffective'], 0),
   ('In the active voice, the subject of a sentence ___.', ['Performs the action', 'Always receives the action', 'A concept unrelated to grammar', 'Is never mentioned in the sentence'], 0),
   ('Why is it useful to review reading and writing concepts like setting, characterization, persuasion, and voice together?', ['These related literacy skills reinforce one another for stronger overall comprehension and communication', 'These topics have no meaningful connection to one another', 'Review is never useful for reading and writing skills', 'Each concept must always be studied in complete isolation'], 0)]),
M('Review: Radicals, Systems, Spheres/Cones, and Logarithms',
  'Grade 9 Algebra and Measurement strands review: this lesson revisits simplifying radicals, solving systems of linear equations by elimination, the surface area and volume of spheres and cones, and logarithms from Days 61-69.',
  [('Simplifying a radical involves factoring out ___ from beneath the square root sign.', ['Perfect square factors', 'Only prime numbers, with no connection to perfect squares', 'A concept unrelated to radicals', 'The entire number, leaving nothing beneath the radical'], 0),
   ('The elimination method solves a system of linear equations by ___.', ['Adding or subtracting the equations to cancel out one variable', 'Graphing both equations with no algebraic calculation', 'A concept unrelated to systems of equations', 'Ignoring one of the two equations entirely'], 0),
   ('The volume of a sphere can be calculated using a formula involving its ___.', ['Radius', 'Only its diameter, with no connection to radius', 'A concept unrelated to measurement', 'Surface area exclusively, with no formula needed'], 0),
   ('A logarithm answers the question of ___.', ['What exponent a given base must be raised to in order to produce a certain number', 'What number results from multiplying a base by itself repeatedly with no exponent involved', 'A concept unrelated to exponents', 'What the square root of a number is'], 0),
   ('Why is it useful to review radicals, systems of equations, measurement formulas, and logarithms together?', ['These related algebra and measurement concepts build on and reinforce one another for deeper understanding', 'These topics have no connection to each other', 'Review is never useful in mathematics', 'Each topic must be learned with no connection to the others'], 0)]),
Sc('Review: Solutions, Immune System, Circulatory/Respiratory, and Radioactivity',
   'Grade 9 Science strand review: this lesson revisits solutions and solubility, the immune system, the circulatory and respiratory systems, and radioactivity and half-life from Days 61-69.',
   [('A solution forms when a ___ dissolves in a solvent.', ['Solute', 'A substance that never mixes with a solvent', 'A concept unrelated to chemistry', 'Solvent, dissolving into itself'], 0),
    ('A pathogen is best described as ___.', ['A microorganism, such as a bacterium or virus, that can cause disease', 'A cell that always protects the body from disease', 'A concept unrelated to biology', 'A nutrient the body requires to survive'], 0),
    ('The circulatory system is primarily responsible for ___.', ['Transporting blood, oxygen, and nutrients throughout the body', 'Breaking down food for digestion', 'A function unrelated to body systems', 'Producing hormones exclusively'], 0),
    ('Radioactive decay occurs when ___.', ['An unstable atomic nucleus releases energy and particles over time', 'An atom becomes permanently stable with no further change', 'A concept unrelated to atomic structure', 'A molecule dissolves completely in a solvent'], 0),
    ('Why is it valuable to review chemistry, biology, and physics concepts like solutions, immunity, body systems, and radioactivity together?', ['It helps connect and reinforce related science concepts learned across recent lessons', 'These topics are entirely unrelated to each other', 'Review provides no benefit in science', 'Each topic must always be studied in isolation'], 0)]),
SS('Review: Map Projections, Urban Heat Islands, Political Boundaries, and Food Deserts',
   'Grade 9 Social Studies (Geography) review: this lesson revisits map projections, urban heat islands, political geography in Canada, and urban food deserts from Days 61-69.',
   [('A map projection is best described as ___.', ['A method of representing the curved surface of the Earth on a flat map', 'A perfectly accurate photograph of the Earth', 'A concept unrelated to geography', 'A map that shows no distortion of any kind'], 0),
    ('An urban heat island occurs when a city experiences ___.', ['Significantly higher temperatures than its surrounding rural areas', 'Significantly lower temperatures than its surrounding rural areas', 'A concept unrelated to urban geography', 'No measurable temperature difference from rural areas'], 0),
    ('Political geography examines how administrative boundaries divide ___.', ['Authority and responsibility across different regions of a country', 'Physical landforms with no connection to governance', 'A concept unrelated to geography', 'Only natural boundaries like rivers and mountains'], 0),
    ('An urban food desert is best described as an area where residents have limited access to ___.', ['Affordable, healthy food', 'Any form of transportation', 'A concept unrelated to urban geography', 'Unlimited amounts of fresh food from every nearby store'], 0),
    ('Why is it useful to review map projections, urban heat islands, political boundaries, and food deserts together?', ['It reinforces how these interconnected geographic and spatial issues shape regions and communities', 'These topics have no meaningful connections', 'Review is never useful in social studies', 'Each topic must be studied with no connection to the others'], 0)])]),
]

def _rebalance_answer_positions(days, seed=20260816):
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
    _rebalance_answer_positions(g9_61_70)
    append_to(9, g9_61_70)
