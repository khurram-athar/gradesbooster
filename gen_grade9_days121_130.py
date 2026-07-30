#!/usr/bin/env python3
"""Grade 9, Days 121-130 -- extends Grade 9 from 120 to 130 days. Topics
chosen after dumping and reading the full Day 1-120 title list (data/grade9.json)
to avoid any overlap: the Oxford comma, eponyms, tragic heroes and hamartia,
cover letters, influencer marketing and disclosure, ellipses and em dashes,
the elegy, malapropisms, and the narrative chorus/narrator-commentator;
synthetic division, prime factorization and the Fundamental Theorem of
Arithmetic, the Pythagorean trigonometric identity, three-variable systems
of equations, the dot product of vectors, proof by mathematical induction,
insurance and risk management, conditional probability, and an
introduction to limits; CRISPR gene editing, reaction rates and catalysts,
simple harmonic motion and pendulums, exoplanets and habitable worlds, the
integumentary system, groundwater and aquifers, acid rain, biomimicry, and
fluid dynamics/Bernoullis Principle; the geography of space debris and
orbital congestion, shrinking inland seas, global remittances and migrant
labour, urban transit systems, deserts and desertification, river deltas
and sedimentation, pharmaceutical access and production, national parks
and ecotourism, and waste-to-energy facilities.

Subject keys for Grade 9 are "Language", "Math", "Science",
"SocialStudies" (same as all earlier Grade 9 batches); SocialStudies
content is Geography-focused, matching the existing convention.

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes are avoided entirely (e.g.
"Bernoullis" not "Bernoulli's", "citys" not "city's").
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_curriculum import sub, day, append_to

L9 = 'https://tvolearn.com/pages/grade-9-english'
M9 = 'https://tvolearn.com/pages/grade-9-mathematics'
S9 = 'https://tvolearn.com/pages/grade-9-science'
SS9 = 'https://tvolearn.com/pages/grade-9-geography'
RL, RM, RS, RSS = (
    'TVO Learn: Grade 9 English',
    'TVO Learn: Grade 9 Mathematics',
    'TVO Learn: Grade 9 Science',
    'TVO Learn: Grade 9 Geography',
)


def L(t, s, q):
    return sub('Language', t, s, RL, L9, q)


def M(t, s, q):
    return sub('Math', t, s, RM, M9, q)


def Sc(t, s, q):
    return sub('Science', t, s, RS, S9, q)


def SS(t, s, q):
    return sub('SocialStudies', t, s, RSS, SS9, q)


def _rebalance_answer_positions(days, seed=20260730):
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


g9_121_130 = [
day(121, [
L('Grammar: The Oxford Comma and Clarity in Lists',
  'Grade 9 Language strand: the Oxford, or serial, comma appears before the final conjunction in a list of three or more items; while its use is a matter of style rather than strict rule, omitting it can sometimes create unintended ambiguity.',
  [('What is the Oxford comma?', ['A comma placed before the final conjunction in a list of three or more items', 'A comma that always ends a sentence', 'A comma used only in dialogue', 'A type of semicolon'], 0),
   ('Why might omitting the Oxford comma sometimes cause confusion?', ['It can make it unclear whether the final two items in a list are meant to be grouped together', 'Removing any comma always improves clarity', 'Commas have no effect on meaning', 'The Oxford comma is required in every single sentence'], 0),
   ('Is the Oxford comma required by all English style guides?', ['No, some style guides require it while others treat it as optional', 'Yes, it is mandatory in every context with no exceptions', 'It was banned by all modern grammar authorities', 'It only applies to numbers, never words'], 0),
   ('In a list of exactly two items, is an Oxford comma used?', ['No, the Oxford comma applies only to lists of three or more items', 'Yes, every list requires an Oxford comma regardless of length', 'Only if the items are proper nouns', 'Only in formal legal writing'], 0),
   ('Which example best shows a list written with the Oxford comma?', ['She packed sandwiches, apples, and juice for the trip.', 'She packed sandwiches, apples and juice for the trip and left.', 'She packed sandwiches apples and juice.', 'She packed: sandwiches; apples; juice.'], 0)]),
M('Algebra: Synthetic Division of Polynomials',
  'Grade 9 Math strand: synthetic division is a shortcut method for dividing a polynomial by a linear binomial of the form x-a, using only the coefficients to quickly find the quotient and remainder.',
  [('What does synthetic division provide a shortcut for?', ['Dividing a polynomial by a linear binomial of the form x-a', 'Multiplying two polynomials together', 'Finding the area of a triangle', 'Solving a system of linear equations'], 0),
   ('What does synthetic division primarily use in its calculations?', ['Only the coefficients of the polynomial', 'Only the exponents of the polynomial', 'Only the variable names', 'Only the constant term, with nothing else'], 0),
   ('What two results does synthetic division produce?', ['A quotient and a remainder', 'Only a single sum', 'Only a product', 'Only an average'], 0),
   ('Synthetic division can only be used when dividing by a polynomial of what form?', ['A linear binomial, such as x-a', 'Any polynomial of any degree', 'Only a constant with no variable', 'Only a quadratic expression'], 0),
   ('Why do students learn synthetic division alongside long division of polynomials?', ['It offers a faster, more efficient method for a specific type of division', 'It always produces a different answer than long division', 'It cannot be used to check any results', 'It replaces the need to ever multiply polynomials'], 0)]),
Sc('Gene Editing and CRISPR Technology: An Introduction',
   'Grade 9 Science strand: CRISPR is a gene-editing technology that allows scientists to precisely add, remove, or alter sections of DNA, offering potential applications in medicine, agriculture, and genetic research.',
   [('What does CRISPR technology allow scientists to do?', ['Precisely add, remove, or alter sections of DNA', 'Only observe cells without altering them in any way', 'Permanently prevent any changes to DNA', 'Convert DNA directly into RNA with no other function'], 0),
    ('What is one potential application of CRISPR technology?', ['Treating genetic diseases by correcting mutations in DNA', 'Eliminating the need for any medical research', 'Preventing the study of genetics entirely', 'Creating organisms with no DNA at all'], 0),
    ('Why is precision an important feature of CRISPR gene editing?', ['It allows scientists to target specific sections of DNA with minimal unintended changes', 'Precision has no importance in gene editing', 'CRISPR only works randomly with no targeting ability', 'Precision eliminates the need for any DNA at all'], 0),
    ('In what field, besides medicine, might CRISPR technology be applied?', ['Agriculture, to develop crops with desirable traits', 'Only in space exploration', 'Only in the design of buildings', 'Only in the manufacturing of vehicles'], 0),
    ('Why do ethical questions arise around the use of gene-editing technology like CRISPR?', ['Because altering DNA, especially in humans, raises questions about safety and long-term consequences', 'Gene editing has no ethical implications whatsoever', 'CRISPR cannot be used on any living organism', 'Ethical questions only apply to unrelated fields like architecture'], 0)]),
SS('Social Studies: The Geography of Space Debris and Orbital Congestion',
   'Grade 9 Social Studies (Geography) strand: space debris, including defunct satellites and fragments from past missions, increasingly crowds Earths orbit, raising geographic and policy questions about how nations can safely share and manage orbital space.',
   [('What is space debris?', ['Defunct satellites and fragments left over from past space missions', 'A natural weather pattern found only on Earth', 'A type of ocean current', 'A landform found in mountainous regions'], 0),
    ('Why is orbital congestion becoming an increasing concern?', ['A growing number of satellites and debris fragments increases the risk of collisions', 'There has never been any debris in Earths orbit', 'Space around Earth is considered limitless with no risk of crowding', 'Satellites are banned from being launched into orbit'], 0),
    ('What kind of questions does space debris raise for geographers and policymakers?', ['How nations can safely share and manage orbital space as a shared resource', 'Questions unrelated to any geographic or policy concerns', 'Only questions about ocean territory, not space', 'Space debris raises no questions of any kind'], 0),
    ('What could happen if a piece of space debris collides with a working satellite?', ['It could damage or destroy the satellite and create even more debris', 'The debris would always simply disappear with no effect', 'Collisions in orbit are considered impossible', 'The satellite would automatically repair itself'], 0),
    ('Why can space, despite being far from Earths surface, still be considered a geographic topic?', ['Geography studies how humans use and organize space, including the orbital region around Earth', 'Geography only studies land-based features and nothing else', 'Space has no connection to any human activity', 'Orbital space is entirely outside the scope of geography by definition'], 0)]),
]),
day(122, [
L('Vocabulary: Eponyms and Words Derived From Names',
  'Grade 9 Language strand: an eponym is a word formed from a persons name, a place, or a brand, such as sandwich or boycott, showing how history and biography can shape everyday vocabulary.',
  [('What is an eponym?', ['A word formed from the name of a person, place, or brand', 'A word with no historical origin', 'A word that has only one syllable', 'A punctuation mark'], 0),
   ('Which of these words is a well known eponym?', ['Sandwich, named after the Earl of Sandwich', 'Table', 'Quickly', 'Blue'], 0),
   ('What does the study of eponyms reveal about language?', ['That real people, places, and events can shape everyday vocabulary over time', 'That vocabulary never changes over time', 'That all words are invented randomly with no history', 'That eponyms are limited only to scientific terms'], 0),
   ('Which category can an eponym be derived from?', ['A brand name that becomes a general term, such as thermos', 'Only numbers', 'Only punctuation marks', 'Only foreign alphabets'], 0),
   ('Why might understanding eponyms help a reader with vocabulary?', ['It connects word meanings to memorable stories or origins, aiding recall', 'It has no effect on vocabulary comprehension', 'It makes words harder to remember', 'It only applies to scientific writing'], 0)]),
M('Number Theory: Prime Factorization and the Fundamental Theorem of Arithmetic',
  'Grade 9 Math strand: prime factorization expresses a number as a product of prime numbers, and the Fundamental Theorem of Arithmetic states that every integer greater than one has exactly one such prime factorization, aside from the order of the factors.',
  [('What does prime factorization express a number as?', ['A product of prime numbers', 'A sum of even numbers only', 'A quotient of two fractions', 'A single prime number only'], 0),
   ('What does the Fundamental Theorem of Arithmetic state?', ['Every integer greater than one has exactly one prime factorization, aside from order', 'Every integer has infinitely many different prime factorizations', 'Prime numbers do not exist', 'Only even numbers can be factored into primes'], 0),
   ('What is the prime factorization of 12?', ['2 x 2 x 3', '2 x 6', '3 x 4', '1 x 12'], 0),
   ('Which of these is a prime number?', ['7', '9', '15', '21'], 0),
   ('Why is prime factorization useful in mathematics?', ['It helps find greatest common factors and least common multiples efficiently', 'It has no practical mathematical application', 'It only applies to negative numbers', 'It eliminates the need for multiplication entirely'], 0)]),
Sc('Reaction Rates and Catalysts in Chemical Reactions',
   'Grade 9 Science strand: the rate of a chemical reaction describes how quickly reactants convert into products, and a catalyst is a substance that speeds up a reaction without being consumed in the process.',
   [('What does the rate of a chemical reaction describe?', ['How quickly reactants convert into products', 'The total mass of the reactants only', 'The colour of the final product', 'The temperature of the room where the reaction occurs'], 0),
    ('What is a catalyst?', ['A substance that speeds up a reaction without being consumed', 'A substance that always slows down a reaction', 'A product formed only after a reaction ends', 'A type of container used to store chemicals'], 0),
    ('Which factor can increase the rate of a chemical reaction?', ['Increasing the temperature of the reactants', 'Removing all reactants from the reaction', 'Decreasing the concentration of every reactant to zero', 'Eliminating any contact between reactants'], 0),
    ('Why is a catalyst considered efficient in industrial chemistry?', ['It can be reused repeatedly since it is not consumed by the reaction', 'It must be replaced after every single use', 'It always slows industrial processes significantly', 'It has no effect on reaction speed'], 0),
    ('Increasing the surface area of a solid reactant typically has what effect on reaction rate?', ['It increases the reaction rate by exposing more particles to collide', 'It always stops the reaction completely', 'It has no effect on how particles collide', 'It only affects the reactions colour'], 0)]),
SS('Social Studies: The Geography of Shrinking Inland Seas and Lakes',
   'Grade 9 Social Studies (Geography) strand: inland seas and large lakes, such as the Aral Sea, have shrunk dramatically in some regions due to water diversion for agriculture and climate change, reshaping local economies and ecosystems.',
   [('What has caused some inland seas and lakes to shrink dramatically?', ['Water diversion for agriculture and the effects of climate change', 'An unexplainable natural process with no identifiable cause', 'A sudden and permanent increase in rainfall', 'The complete absence of any human activity nearby'], 0),
    ('What is one example of a dramatically shrinking inland body of water?', ['The Aral Sea', 'The Pacific Ocean', 'The Atlantic Ocean', 'The Arctic Ocean'], 0),
    ('How can a shrinking inland sea affect local economies?', ['Industries like fishing that depend on the water can decline sharply', 'Local economies always improve when a sea shrinks', 'Shrinking water bodies have no economic effect whatsoever', 'Fishing industries always expand as water levels drop'], 0),
    ('What environmental effect can a shrinking lake have on surrounding ecosystems?', ['Loss of habitat for fish and other wildlife dependent on the water', 'Environmental conditions always improve for local wildlife', 'Ecosystems are entirely unaffected by changes in water levels', 'New permanent oceans are created as a direct result'], 0),
    ('Why do geographers study cases like the shrinking of inland seas?', ['To understand the human and environmental consequences of water resource management decisions', 'These cases have no relevance to the study of geography', 'Geography does not study changes in water bodies over time', 'Shrinking water bodies are considered purely a historical topic with no modern relevance'], 0)]),
]),
day(123, [
L('Reading: Analyzing Tragic Heroes and the Concept of Hamartia',
  'Grade 9 Language strand: a tragic hero is a protagonist of noble stature whose hamartia, or fatal flaw, leads to their downfall, a concept originating in classical drama and still shaping literature today.',
  [('What is hamartia?', ['A fatal flaw or error in judgment that leads to a tragic heros downfall', 'A type of happy ending', 'A minor background character', 'A rhyme scheme in poetry'], 0),
   ('What is a defining trait of a tragic hero?', ['Noble stature combined with a flaw that ultimately causes their downfall', 'Complete perfection with no flaws at all', 'A character who never faces any conflict', 'A character who is always victorious'], 0),
   ('In what type of drama did the concept of the tragic hero originate?', ['Classical Greek drama', 'Modern science fiction only', 'Silent films', 'Contemporary comic strips'], 0),
   ('Which is an example of a possible hamartia?', ['Excessive pride, or hubris, that blinds a character to danger', 'A characters kindness with no consequence at all', 'A characters lack of any personality', 'A characters physical height'], 0),
   ('Why do tragic heroes remain a compelling subject in literature?', ['Their flaws make them relatable while their downfall evokes pity and reflection', 'Tragic heroes never evoke any emotion in readers', 'They are always minor, forgettable characters', 'Their stories never involve any conflict'], 0)]),
M('Trigonometry: The Pythagorean Trigonometric Identity',
  'Grade 9 Math strand: the Pythagorean trigonometric identity states that sine squared plus cosine squared of an angle always equals one, a relationship derived directly from the Pythagorean Theorem applied to the unit circle.',
  [('What does the Pythagorean trigonometric identity state?', ['Sine squared plus cosine squared of an angle equals one', 'Sine plus cosine always equals zero', 'Tangent squared always equals negative one', 'Sine minus cosine always equals one'], 0),
   ('From what earlier concept is the Pythagorean trigonometric identity derived?', ['The Pythagorean Theorem applied to the unit circle', 'The quadratic formula', 'The binomial theorem', 'The distance formula only'], 0),
   ('If sine of an angle is 0, what must cosine squared equal, according to the identity?', ['1', '0', '-1', '2'], 0),
   ('Why is this identity considered fundamental in trigonometry?', ['It connects sine and cosine for any angle and supports many other identities', 'It only works for angles greater than 360 degrees', 'It has no use beyond a single specific angle', 'It contradicts the definitions of sine and cosine'], 0),
   ('The Pythagorean trigonometric identity applies to ___.', ['Any angle, since it holds true for all real values', 'Only angles measured in a right triangle', 'Only angles less than 10 degrees', 'Only angles equal to exactly 90 degrees'], 0)]),
Sc('Simple Harmonic Motion and the Physics of Pendulums',
   'Grade 9 Science strand: simple harmonic motion describes a repeating back-and-forth movement, such as that of a swinging pendulum, where a restoring force continually pulls the object back toward a central equilibrium position.',
   [('What does simple harmonic motion describe?', ['A repeating back-and-forth movement around a central equilibrium position', 'A single, non-repeating movement in one direction', 'Motion that only occurs in outer space', 'A completely random and unpredictable movement'], 0),
    ('What force is responsible for pulling a pendulum back toward its resting position?', ['A restoring force, largely due to gravity', 'An entirely random, unpredictable force', 'A force that pushes the pendulum farther away every time', 'No force acts on a pendulum at all'], 0),
    ('Which of these is a real-world example of simple harmonic motion?', ['A swinging pendulum in a clock', 'A car driving in a straight line at constant speed', 'A ball resting motionless on a flat table', 'A rocket travelling in a straight line away from Earth'], 0),
    ('What happens to a pendulums swing over time if energy is lost to friction and air resistance?', ['The swing gradually decreases in amplitude', 'The swing speeds up indefinitely with no limit', 'The swing instantly stops moving in every case', 'The swing changes into a completely different shape of motion'], 0),
    ('Simple harmonic motion is a foundational concept for understanding which broader physics topics?', ['Waves and vibrations', 'Only chemical bonding', 'Only cellular biology', 'Only plate tectonics'], 0)]),
SS('Social Studies: The Geography of Global Remittances and Migrant Labour',
   'Grade 9 Social Studies (Geography) strand: remittances are funds sent by migrant workers back to their home countries, forming a major economic flow that connects global labour migration patterns to development in many regions.',
   [('What are remittances?', ['Funds sent by migrant workers back to their home countries', 'Taxes collected exclusively by national governments', 'Loans given only to large corporations', 'Payments made only between two neighbouring countries with no individuals involved'], 0),
    ('How do remittances connect to global migration patterns?', ['They represent an economic flow tied directly to where migrant workers choose to work', 'Remittances have no connection to migration of any kind', 'They only occur within a single countrys borders', 'Migrant workers never send money to their home countries'], 0),
    ('What impact can remittances have on a migrant workers home country?', ['They can provide a significant source of income supporting families and local development', 'Remittances always harm the economic development of the home country', 'They have no measurable impact on the receiving country', 'They are typically smaller than all other sources of national income combined'], 0),
    ('Why might someone choose to work as a migrant labourer in another country?', ['To access greater economic opportunities than may be available at home', 'Migrant labour never involves seeking better economic opportunities', 'All migrant workers are forced to work with no personal choice involved', 'There is no economic incentive involved in migrant labour'], 0),
    ('Why do geographers study the global flow of remittances?', ['It reveals patterns of economic interdependence between origin and destination countries', 'Remittances have no geographic significance', 'This flow of money is considered entirely random with no patterns', 'Only the destination country is affected by remittances'], 0)]),
]),
day(124, [
L('Writing: Writing a Cover Letter',
  'Grade 9 Language strand: a cover letter introduces a job or program applicant to a potential employer, highlighting relevant skills and experiences in a concise, professional tone that complements a resume.',
  [('What is the purpose of a cover letter?', ['To introduce an applicant and highlight relevant skills for a specific opportunity', 'To replace a resume entirely', 'To list unrelated personal opinions', 'To criticize the employer'], 0),
   ('What tone should a cover letter typically maintain?', ['A concise, professional tone', 'An extremely casual and informal tone', 'A tone with no clear purpose', 'An aggressive and demanding tone'], 0),
   ('What should a strong cover letter highlight?', ['Specific skills and experiences relevant to the opportunity', 'Only the applicants personal hobbies with no connection to the job', 'Nothing related to the applicants qualifications', 'Only complaints about previous employers'], 0),
   ('How does a cover letter typically relate to a resume?', ['It complements the resume by providing context and personality', 'It contradicts everything listed on the resume', 'It replaces the need for a resume completely', 'It has no connection to the resume at all'], 0),
   ('Why is conciseness important in a cover letter?', ['Employers often review many applications and appreciate a clear, focused message', 'Cover letters are always expected to be extremely long', 'Length has no effect on how a cover letter is received', 'Concise writing is never valued professionally'], 0)]),
M('Algebra: Solving Systems of Equations in Three Variables',
  'Grade 9 Math strand: a system of equations in three variables can be solved by systematically eliminating one variable at a time until the system reduces to two equations in two variables, then continuing to substitute back to find all three values.',
  [('What is the goal when solving a system of three equations with three variables?', ['To find the values of all three variables that satisfy every equation', 'To eliminate every variable entirely with no solution remaining', 'To combine all equations into a single variable with no solution', 'To ignore two of the three equations completely'], 0),
   ('What is a common first step in solving a three-variable system?', ['Eliminating one variable to reduce the system to two equations in two variables', 'Immediately guessing random values for each variable', 'Multiplying all three equations by zero', 'Deleting one of the equations without using it'], 0),
   ('How many independent equations are generally needed to solve for three unique variables?', ['Three independent equations', 'Only one equation', 'Exactly five equations', 'No equations are needed'], 0),
   ('What does it mean if a three-variable system has no solution?', ['The equations are inconsistent and their planes do not share a common intersection point', 'The system always has infinitely many solutions instead', 'It means all three variables equal zero', 'It means the system was solved incorrectly by definition'], 0),
   ('Systems of equations in three variables can be used to model real-world situations involving ___.', ['Three unknown quantities that are related by multiple conditions', 'Only situations with a single unknown quantity', 'Situations with no numerical relationships at all', 'Only situations involving geometry, never algebra'], 0)]),
Sc('Exoplanets and the Search for Habitable Worlds',
   'Grade 9 Science strand: an exoplanet is a planet that orbits a star outside our solar system, and astronomers search for exoplanets within a stars habitable zone, where conditions might allow liquid water to exist.',
   [('What is an exoplanet?', ['A planet that orbits a star outside our solar system', 'A planet located within our own solar system only', 'A moon that orbits a planet', 'A star with no orbiting planets'], 0),
    ('What is a habitable zone?', ['The region around a star where conditions might allow liquid water to exist', 'A region with absolutely no stars nearby', 'The exact centre of every galaxy', 'A region where no planets can ever form'], 0),
    ('Why is liquid water an important factor when searching for potentially habitable exoplanets?', ['It is considered essential for life as we understand it', 'Water has no connection to the possibility of life', 'Liquid water always indicates the presence of intelligent life', 'Water is irrelevant to planetary habitability studies'], 0),
    ('What method do astronomers commonly use to detect exoplanets?', ['Observing the slight dimming of a stars light as a planet passes in front of it', 'Listening for radio signals from every planet', 'Sending physical spacecraft to every star in the galaxy', 'Guessing randomly with no supporting evidence'], 0),
    ('Why does the study of exoplanets excite scientists and the public alike?', ['It raises the possibility of finding other habitable worlds or even signs of life', 'Exoplanets have no scientific significance', 'The topic has no connection to the search for life', 'Exoplanets are identical to planets in our own solar system'], 0)]),
SS('Social Studies: The Geography of Urban Transit Systems and Public Transportation',
   'Grade 9 Social Studies (Geography) strand: urban transit systems, including buses, subways, and light rail, shape how efficiently people move through a city and influence patterns of urban development and accessibility.',
   [('What role do urban transit systems play in a city?', ['They shape how efficiently people move through the city and access opportunities', 'They have no influence on how a city functions', 'They only exist in rural farmland with no urban application', 'They eliminate the need for any roads or infrastructure'], 0),
    ('Which of these is an example of public transportation?', ['A subway system', 'A private car owned by one household', 'A bicycle owned by one individual', 'A single-family home'], 0),
    ('How can access to public transit affect a neighbourhoods development?', ['Areas with strong transit access often see increased development and property values', 'Transit access has no effect on neighbourhood development', 'Every neighbourhood develops identically regardless of transit access', 'Public transit always causes a neighbourhoods population to decline'], 0),
    ('What is one benefit of well-developed public transportation for a city?', ['Reduced traffic congestion and lower per-person emissions compared to individual cars', 'Public transportation always increases traffic congestion', 'It has no effect on a citys environmental impact', 'It eliminates the need for any urban planning'], 0),
    ('Why might geographers study the design and equity of transit systems?', ['To understand how transportation access affects opportunity and quality of life across a city', 'Transit systems are unrelated to the study of urban geography', 'Transit design has no connection to social or economic equity', 'Every resident of a city always has identical access to transit'], 0)]),
]),
day(125, [
L('Media Literacy: Analyzing Influencer Marketing and Disclosure',
  'Grade 9 Language strand: influencer marketing involves individuals promoting products to their followers, and ethical practice requires clear disclosure of paid partnerships so audiences can distinguish genuine opinions from sponsored content.',
  [('What is influencer marketing?', ['Individuals promoting products or services to their followers, often for payment', 'A form of advertising banned in all countries', 'A type of grammar rule', 'A citation format for academic essays'], 0),
   ('Why is disclosure important in influencer marketing?', ['It allows audiences to distinguish genuine opinions from paid promotion', 'Disclosure has no effect on how audiences interpret content', 'Disclosure is legally required to be hidden from audiences', 'Influencers are never paid for their content'], 0),
   ('What might indicate that a social media post is a paid partnership?', ['A label such as Paid Partnership or Sponsored near the post', 'The complete absence of any product mention', 'A post with no images at all', 'A post published only once a year'], 0),
   ('Why might followers trust an influencers recommendation?', ['They may view the influencer as relatable or knowledgeable, unlike traditional ads', 'Followers never trust any online content', 'Influencers never have any audience connection', 'Recommendations from influencers are always required by law to be false'], 0),
   ('What is a potential risk of undisclosed influencer marketing?', ['Audiences may be misled into thinking a paid promotion is a genuine opinion', 'There are no risks associated with undisclosed marketing', 'Undisclosed marketing always improves audience trust', 'Audiences always immediately recognize every paid partnership'], 0)]),
M('Geometry: An Introduction to the Dot Product of Vectors',
  'Grade 9 Math strand: the dot product combines two vectors to produce a single scalar value, calculated by multiplying corresponding components and summing the results, and it can reveal the angle between two vectors.',
  [('What type of value does the dot product of two vectors produce?', ['A single scalar value', 'A new vector with a different direction', 'A matrix', 'A complex number'], 0),
   ('How is the dot product of two vectors calculated?', ['By multiplying corresponding components and summing the results', 'By dividing one vector by the other', 'By adding the magnitudes of each vector only', 'By subtracting one vector from the other'], 0),
   ('What can the dot product help determine about two vectors?', ['The angle between them', 'Only their individual lengths, never their relationship', 'Their colour', 'Their location on a map'], 0),
   ('If the dot product of two nonzero vectors equals zero, what does this suggest?', ['The vectors are perpendicular to each other', 'The vectors point in exactly the same direction', 'The vectors have no length at all', 'The vectors cannot be graphed'], 0),
   ('The dot product is a useful tool in fields such as ___.', ['Physics, for calculating work done by a force', 'Only music theory', 'Only literary analysis', 'Only culinary arts'], 0)]),
Sc('The Integumentary System: Skin as a Vital Organ',
   'Grade 9 Science strand: the integumentary system, consisting mainly of the skin, protects the body from pathogens and injury, regulates temperature, and provides sensory information about the external environment.',
   [('What is the primary organ of the integumentary system?', ['The skin', 'The heart', 'The liver', 'The lungs'], 0),
    ('What is one major function of the skin?', ['Protecting the body from pathogens and physical injury', 'Pumping blood throughout the body', 'Digesting food for nutrient absorption', 'Filtering air before it enters the lungs'], 0),
    ('How does skin help regulate body temperature?', ['Through processes like sweating and adjusting blood flow near the surface', 'Skin has no role in regulating body temperature', 'By preventing any heat from ever leaving the body', 'By converting heat directly into sound'], 0),
    ('What sensory information can skin provide about the environment?', ['Touch, pressure, temperature, and pain', 'Only information about light and colour', 'Only information about sound', 'Only information about taste'], 0),
    ('Why is the skin classified as an organ rather than simply a covering?', ['It is composed of multiple tissue types working together to perform specific functions', 'It has no distinct structure or function', 'It performs no measurable biological function', 'It is not connected to any other body system'], 0)]),
SS('Social Studies: The Geography of Deserts and Desertification',
   'Grade 9 Social Studies (Geography) strand: deserts are regions receiving very little precipitation, and desertification is the process by which fertile land becomes increasingly arid, often driven by climate change, overgrazing, and unsustainable land use.',
   [('What defines a desert region?', ['A region that receives very little precipitation', 'A region with the highest rainfall on Earth', 'A region located only near the equator', 'A region with no temperature variation at all'], 0),
    ('What is desertification?', ['The process by which fertile land becomes increasingly arid', 'The process by which deserts turn into rainforests', 'A term with no connection to land or climate', 'The permanent freezing of tropical regions'], 0),
    ('What human activity can contribute to desertification?', ['Overgrazing of livestock on fragile land', 'Planting trees to restore degraded land', 'Reducing water use in agriculture', 'Protecting natural vegetation from being removed'], 0),
    ('How can climate change contribute to desertification?', ['Rising temperatures and shifting precipitation patterns can dry out previously fertile land', 'Climate change always increases rainfall in every region uniformly', 'Climate change has no connection to changes in land fertility', 'Desertification only occurs in regions with no climate variation'], 0),
    ('Why is desertification a significant concern for communities living near affected land?', ['It can threaten agriculture, water supplies, and livelihoods dependent on fertile land', 'Desertification has no effect on nearby human communities', 'Communities always benefit economically from desertification', 'Fertile land is unaffected by any changes in surrounding deserts'], 0)]),
]),
day(126, [
L('Grammar: Ellipsis and the Em Dash in Formal Writing',
  'Grade 9 Language strand: an ellipsis (three spaced or unspaced dots) signals omitted words or a trailing thought, while an em dash creates a strong break to emphasize or interrupt an idea, and formal writing uses both with restraint.',
  [('What does an ellipsis typically signal in writing?', ['Omitted words or a trailing, unfinished thought', 'The end of a formal citation', 'A grammatical error', 'A question being asked'], 0),
   ('What effect does an em dash create in a sentence?', ['A strong break that emphasizes or interrupts an idea', 'No effect on the sentence at all', 'It always ends a sentence with a question', 'It replaces every comma in a sentence'], 0),
   ('How many dots typically make up an ellipsis?', ['Three', 'One', 'Five', 'Seven'], 0),
   ('Why should formal writing use ellipses and em dashes with restraint?', ['Overuse can make writing feel informal or disorganized', 'These marks are banned entirely from formal writing', 'Formal writing requires using them in every sentence', 'They have no effect on tone in formal writing'], 0),
   ('Which sentence correctly uses an em dash for emphasis?', ['The results were clear — the team had succeeded beyond expectations.', 'The results, were, clear the team succeeded.', 'The results were... clear, the, team succeeded', 'The results were cleartheteam succeeded'], 0)]),
M('Algebra: An Introduction to Mathematical Proof by Induction',
  'Grade 9 Math strand: mathematical induction proves a statement is true for all natural numbers by first establishing a base case and then showing that if the statement holds for one value, it must also hold for the next.',
  [('What does mathematical induction prove?', ['That a statement is true for all natural numbers', 'That a statement is false for every number', 'That a single equation has no solution', 'That every polynomial can be factored'], 0),
   ('What is the first step in a proof by induction called?', ['The base case', 'The final conclusion', 'The remainder', 'The coefficient'], 0),
   ('What must be shown in the inductive step of a proof by induction?', ['That if the statement holds for one value, it also holds for the next value', 'That the statement is false for every value tested', 'That no base case is ever required', 'That the statement only applies to negative numbers'], 0),
   ('Why is the base case an essential part of a proof by induction?', ['It establishes the starting point that anchors the entire chain of reasoning', 'It has no importance to the overall proof', 'It replaces the need for an inductive step entirely', 'It only applies to even numbers'], 0),
   ('Mathematical induction is often compared to which everyday image?', ['A chain of falling dominoes, where each one knocks over the next', 'A single isolated event with no connections', 'A random guess with no logical structure', 'A flat, unchanging line with no pattern'], 0)]),
Sc('Groundwater and Aquifer Systems',
   'Grade 9 Science strand: groundwater is water stored beneath the surface within permeable rock or sediment layers called aquifers, and it represents a major source of fresh water for drinking, agriculture, and industry.',
   [('What is groundwater?', ['Water stored beneath the surface within permeable rock or sediment layers', 'Water found only in oceans', 'Water that exists only in the atmosphere', 'Water that has evaporated completely'], 0),
    ('What is an aquifer?', ['An underground layer of permeable rock or sediment that holds groundwater', 'A type of surface river', 'A machine used to purify ocean water', 'A structure built only to store rainwater on the surface'], 0),
    ('What is groundwater commonly used for?', ['Drinking water, agriculture, and industrial processes', 'Only for generating electricity', 'Only for recreational swimming', 'It has no practical human use'], 0),
    ('What can happen to an aquifer if groundwater is withdrawn faster than it is naturally replenished?', ['The water table can drop, potentially depleting the aquifer over time', 'The aquifer instantly refills itself with no consequences', 'Aquifers can never be depleted under any circumstances', 'The surrounding land always rises higher as a result'], 0),
    ('Why is protecting groundwater from contamination especially important?', ['Aquifers are a major source of drinking water and can be difficult to clean once polluted', 'Groundwater has no connection to drinking water supplies', 'Contamination of groundwater is always immediately reversible', 'Aquifers are located far away from any human activity'], 0)]),
SS('Social Studies: The Geography of River Deltas and Sedimentation',
   'Grade 9 Social Studies (Geography) strand: a river delta forms where a river deposits sediment as it slows and meets a larger body of water, creating fertile, low-lying land that supports dense agriculture and settlement but faces risks from flooding and rising seas.',
   [('What is a river delta?', ['Landform created where a river deposits sediment as it meets a larger body of water', 'A mountain range formed by tectonic activity', 'A dry region with almost no water present', 'A type of underground cave system'], 0),
    ('Why do river deltas typically have very fertile soil?', ['Rivers deposit nutrient-rich sediment as they slow down and spread out', 'Deltas never receive any sediment from rivers', 'Fertile soil in deltas comes exclusively from volcanic activity', 'Delta soil is considered among the least fertile on Earth'], 0),
    ('Why have many river deltas historically attracted dense human settlement?', ['Fertile land and access to water support agriculture and trade', 'Deltas are typically the driest regions on any continent', 'Historically, people have avoided settling near deltas entirely', 'Deltas offer no advantages for farming or trade'], 0),
    ('What risk do many low-lying river deltas face today?', ['Increased flooding risk linked to rising sea levels and land subsidence', 'Deltas face no environmental risks of any kind', 'Deltas are the least likely landform to ever flood', 'Rising sea levels have no effect on delta regions'], 0),
    ('How can upstream dam construction affect a river delta downstream?', ['It can reduce the sediment reaching the delta, contributing to land loss over time', 'Dams always increase the amount of sediment reaching a delta', 'Upstream dams have no effect on downstream delta regions', 'Dam construction guarantees a deltas long-term stability'], 0)]),
]),
day(127, [
L('Writing: The Elegy and Occasional Writing',
  'Grade 9 Language strand: an elegy is a reflective poem or piece of writing that mourns a loss, often a persons death, using formal, contemplative language to express grief and honour memory.',
  [('What is an elegy?', ['A reflective poem or piece of writing that mourns a loss', 'A humorous poem with no serious tone', 'A type of business letter', 'A scientific report format'], 0),
   ('What tone does an elegy typically use?', ['A formal, contemplative tone expressing grief and reflection', 'An aggressive and mocking tone', 'A tone with no emotional content', 'A purely comedic tone'], 0),
   ('What is an elegy commonly written to honour?', ['The memory of someone who has died', 'A sports victory', 'A new invention', 'A recipe for a meal'], 0),
   ('Occasional writing refers to writing composed for what purpose?', ['A specific event or occasion, such as a memorial or celebration', 'No specific purpose at all', 'Only fictional stories with no real-world connection', 'Only technical manuals'], 0),
   ('Why might a writer choose formal language in an elegy?', ['To convey the seriousness and depth of the loss being honoured', 'To make the subject seem unimportant', 'Formal language is never appropriate for this purpose', 'To confuse the reader intentionally'], 0)]),
M('Financial Literacy: Insurance and Risk Management',
  'Grade 9 Math strand: insurance is a financial product in which individuals pay regular premiums to transfer the risk of significant financial loss to an insurer, a key strategy in personal risk management.',
  [('What is insurance?', ['A financial product where individuals pay premiums to transfer risk of loss to an insurer', 'A guaranteed way to avoid ever losing money', 'A type of loan with no repayment required', 'A tax collected only by the government'], 0),
   ('What is a premium in the context of insurance?', ['The regular payment made to maintain an insurance policy', 'The total amount paid out after a claim', 'A type of penalty for late payments', 'A one-time payment with no future obligation'], 0),
   ('Why might someone choose to purchase insurance?', ['To protect against the financial impact of an unexpected, costly event', 'To guarantee they will never experience any loss', 'Insurance provides no financial benefit at all', 'To avoid paying any future costs whatsoever'], 0),
   ('What is the basic concept behind risk management?', ['Identifying potential risks and taking steps to reduce or transfer their impact', 'Ignoring all potential risks completely', 'Risk management always eliminates risk permanently', 'Risk cannot be planned for in any way'], 0),
   ('Which of these is a common type of insurance?', ['Health insurance, covering medical expenses', 'A grocery store discount card', 'A library membership', 'A student ID card'], 0)]),
Sc('Acid Rain: Causes and Environmental Effects',
   'Grade 9 Science strand: acid rain forms when pollutants such as sulfur dioxide and nitrogen oxides react with water vapour in the atmosphere, producing precipitation with a lower pH that can damage ecosystems, buildings, and water sources.',
   [('What causes acid rain to form?', ['Pollutants like sulfur dioxide and nitrogen oxides reacting with water vapour in the atmosphere', 'Only natural evaporation with no pollutants involved', 'Sudden temperature drops with no chemical reactions', 'Increased sunlight with no connection to pollution'], 0),
    ('What happens to the pH of precipitation affected by acid rain?', ['It becomes more acidic, or lower in pH', 'It becomes more basic, or higher in pH', 'The pH remains completely unchanged', 'pH has no relevance to acid rain'], 0),
    ('What is one environmental effect of acid rain?', ['Damage to forests, lakes, and aquatic ecosystems', 'Immediate improvement of soil fertility everywhere', 'Elimination of all pollution in the atmosphere', 'Increased growth in every affected ecosystem with no harm'], 0),
    ('Besides ecosystems, what else can acid rain damage?', ['Buildings and monuments made of certain materials like limestone', 'Only objects located deep underground', 'Only items made entirely of glass', 'Acid rain causes no damage to any human-made structures'], 0),
    ('What human activities are major contributors to the pollutants that cause acid rain?', ['Burning fossil fuels in vehicles and power plants', 'Planting trees and restoring forests', 'Recycling paper products', 'Conserving water during droughts'], 0)]),
SS('Social Studies: The Geography of Pharmaceutical Access and Production',
   'Grade 9 Social Studies (Geography) strand: the global geography of pharmaceutical production and distribution is uneven, with manufacturing concentrated in certain regions and many lower-income countries facing significant barriers to accessing essential medicines.',
   [('What does the geography of pharmaceutical production reveal?', ['That manufacturing is concentrated in certain regions rather than distributed evenly worldwide', 'That every country produces an identical share of the worlds medicine', 'That pharmaceutical production has no geographic pattern at all', 'That medicine is produced entirely without any regional concentration'], 0),
    ('What barrier might lower-income countries face in accessing essential medicines?', ['High costs and limited local manufacturing or distribution infrastructure', 'Lower-income countries face no barriers to medical access whatsoever', 'Essential medicines are always freely available everywhere in the world', 'Access to medicine has no connection to a countrys income level'], 0),
    ('Why might a country want to develop its own pharmaceutical manufacturing capacity?', ['To reduce dependence on imports and improve access during global supply disruptions', 'Local manufacturing always increases costs with no benefit', 'Countries never benefit from producing their own medicine', 'Pharmaceutical manufacturing has no connection to supply chain resilience'], 0),
    ('How did global supply chains for medicine face challenges during recent global health crises?', ['Disruptions in production and shipping made some medicines and supplies harder to access', 'Global supply chains for medicine are never affected by health crises', 'Health crises always improve global access to medicine', 'Medicine supply chains operate independently of any global events'], 0),
    ('Why do geographers study patterns of pharmaceutical access around the world?', ['To understand how location and economic development shape health outcomes', 'Pharmaceutical access has no connection to geography', 'This topic is considered purely a medical issue with no geographic dimension', 'Every region of the world has identical access to medicine'], 0)]),
]),
day(128, [
L('Vocabulary: Malapropisms and Commonly Confused Words',
  'Grade 9 Language strand: a malapropism occurs when a similar-sounding word is mistakenly used in place of the intended word, often creating an unintentionally humorous or nonsensical effect, such as saying dance a flamingo instead of flamenco.',
  [('What is a malapropism?', ['The mistaken use of a similar-sounding word in place of the intended word', 'A word borrowed directly from another language', 'A formal grammatical rule', 'A type of punctuation mark'], 0),
   ('What effect do malapropisms often create?', ['An unintentionally humorous or nonsensical effect', 'Perfect clarity with no confusion', 'A completely serious and formal tone', 'No effect on meaning at all'], 0),
   ('Which is an example of a malapropism?', ['Saying prescription instead of description, because the words sound alike', 'Using the correct word in every context', 'Using no words at all', 'Speaking only in complete silence'], 0),
   ('Why do malapropisms commonly occur?', ['The intended word and the word actually used sound similar', 'The words have completely different sounds and spellings', 'Malapropisms are always used intentionally for formal effect', 'They only occur in written text, never speech'], 0),
   ('Why is it useful to recognize commonly confused words?', ['It helps writers and speakers communicate their intended meaning clearly', 'Confusing words always improves clarity', 'Recognizing confused words has no communicative benefit', 'Confused words are never actually a problem in communication'], 0)]),
M('Data Management: An Introduction to Conditional Probability',
  'Grade 9 Math strand: conditional probability calculates the likelihood of an event occurring given that another event has already happened, refining the probability estimate based on new information.',
  [('What does conditional probability calculate?', ['The likelihood of an event occurring given that another event has already happened', 'The probability of an event with no other information considered', 'The total number of possible outcomes only', 'The average of two unrelated probabilities'], 0),
   ('How does new information affect a conditional probability calculation?', ['It can refine and change the probability estimate for the second event', 'New information never changes any probability calculation', 'It always makes an event impossible', 'It has no mathematical effect on probability'], 0),
   ('If drawing a card from a standard deck, how might conditional probability apply?', ['Calculating the probability of drawing a king, given that the card drawn is a face card', 'Calculating the probability without ever looking at the deck', 'Ignoring the type of card drawn entirely', 'Assuming every card has an identical fixed probability with no conditions'], 0),
   ('Conditional probability is often written using what kind of notation?', ['P(A given B), showing the probability of A occurring given B', 'Only whole numbers with no variables', 'Roman numerals exclusively', 'A single unlabeled percentage'], 0),
   ('Why is conditional probability useful in real-world contexts, like medical testing?', ['It helps estimate the likelihood of a condition given a specific test result', 'It has no real-world applications', 'It is only theoretical with no practical use', 'It always guarantees a certain outcome with no uncertainty'], 0)]),
Sc('Biomimicry: Engineering Solutions Inspired by Nature',
   'Grade 9 Science strand: biomimicry is the practice of studying natural structures and processes, such as a birds wings or a lotus leafs surface, to inspire innovative engineering and design solutions.',
   [('What is biomimicry?', ['The practice of studying natural structures and processes to inspire engineering solutions', 'A process that eliminates all connection between science and nature', 'A method for destroying natural ecosystems', 'A type of chemical reaction only'], 0),
    ('Which is an example of a biomimicry-inspired design?', ['Aircraft wing designs inspired by the structure of bird wings', 'A material with no connection to any natural structure', 'A design created with no reference to nature whatsoever', 'An invention that ignores all natural principles'], 0),
    ('Why might engineers look to nature for design inspiration?', ['Natural structures have often been refined by evolution to be highly efficient', 'Nature provides no useful information for engineering', 'Biomimicry always produces less efficient designs than traditional methods', 'Studying nature is unrelated to solving engineering problems'], 0),
    ('What natural feature has inspired self-cleaning surface technology?', ['The water-repelling surface of a lotus leaf', 'The colour of autumn leaves', 'The sound produced by ocean waves', 'The taste of tree bark'], 0),
    ('Biomimicry connects which two broad fields of study?', ['Biology and engineering', 'Only mathematics and history', 'Only music and art', 'Only geography and language arts'], 0)]),
SS('Social Studies: The Geography of National Parks and Ecotourism',
   'Grade 9 Social Studies (Geography) strand: national parks preserve significant natural or cultural landscapes, and ecotourism, or travel focused on experiencing these protected areas responsibly, can generate revenue for conservation while posing challenges if visitor numbers grow too large.',
   [('What is the purpose of a national park?', ['To preserve significant natural or cultural landscapes', 'To maximize industrial development in a region', 'To eliminate all wildlife from a protected area', 'To prevent any form of tourism whatsoever'], 0),
    ('What is ecotourism?', ['Travel focused on experiencing natural areas responsibly', 'Travel focused exclusively on large urban shopping centres', 'A type of tourism that ignores environmental impact entirely', 'Travel that always damages the areas being visited intentionally'], 0),
    ('How can ecotourism benefit conservation efforts?', ['It can generate revenue that supports the protection and maintenance of natural areas', 'Ecotourism always reduces the funding available for conservation', 'Ecotourism has no connection to conservation funding', 'Conservation efforts never benefit from any form of tourism'], 0),
    ('What challenge can arise if a national park receives too many visitors?', ['Overcrowding can damage fragile ecosystems and trails', 'Additional visitors always improve the parks ecological health', 'There is no upper limit to how many visitors a park can sustainably host', 'Overcrowding has no effect on natural environments'], 0),
    ('Why might geographers study the balance between tourism and conservation in national parks?', ['To understand how to sustain both economic benefits and environmental protection', 'This balance has no relevance to geographic study', 'Tourism and conservation are always in perfect balance with no conflict', 'National parks have no economic impact on surrounding regions'], 0)]),
]),
day(129, [
L('Reading: Analyzing the Function of a Chorus or Narrator-Commentator',
  'Grade 9 Language strand: a chorus or narrator-commentator figure stands outside the main action of a story to provide context, commentary, or moral reflection, a technique originating in ancient drama and still used in modern narratives.',
  [('What role does a chorus or narrator-commentator typically play?', ['Providing context, commentary, or moral reflection from outside the main action', 'Serving as the storys main antagonist', 'Remaining completely silent throughout the story', 'Replacing the need for any plot at all'], 0),
   ('Where did the use of a chorus as a narrative device originate?', ['Ancient Greek drama', 'Twentieth century science fiction films', 'Modern social media', 'Contemporary video games only'], 0),
   ('Why might an author include a narrator-commentator figure?', ['To offer the audience insight or perspective the characters themselves may lack', 'To eliminate all perspective from the story', 'To confuse the audience with irrelevant information', 'To remove the need for any characters'], 0),
   ('How does a chorus typically relate to the main action of a story?', ['It comments on events from outside the main action rather than participating directly', 'It is always the main character driving the plot', 'It has no connection to the story whatsoever', 'It only appears in the very last line of a story'], 0),
   ('Which is a modern example of a narrator-commentator technique?', ['A film narrator who provides background information and reflection between scenes', 'A character who never speaks at all', 'A silent background prop with no narrative role', 'A blank page with no content'], 0)]),
M('Calculus Preview: An Introduction to Limits',
  'Grade 9 Math strand: a limit describes the value a function approaches as its input gets closer to a specific point, forming the conceptual foundation for derivatives and the broader study of calculus.',
  [('What does a limit describe?', ['The value a function approaches as its input gets closer to a specific point', 'The exact maximum value of any function', 'A fixed number that never changes across all functions', 'The total area under every curve'], 0),
   ('What foundational concept in calculus relies on the idea of a limit?', ['The derivative', 'Basic addition', 'Simple counting', 'Long division only'], 0),
   ('Can a function have a limit at a point even if it is undefined at that exact point?', ['Yes, a limit can exist even if the function itself is undefined there', 'No, a limit only exists if the function is defined at that exact point', 'Limits are unrelated to whether a function is defined', 'A function can never have any limit under any circumstance'], 0),
   ('As x approaches 2, what does the limit of the function f(x)=x+1 approach?', ['3', '2', '1', '0'], 0),
   ('Why do mathematicians consider limits a foundational concept in calculus?', ['They provide a precise way to describe behaviour near a point without requiring the function be defined there', 'They have no connection to any other calculus concept', 'They only apply to whole numbers with no fractions', 'They eliminate the need to study functions entirely'], 0)]),
Sc('Fluid Dynamics and Bernoullis Principle',
   'Grade 9 Science strand: fluid dynamics studies how liquids and gases move, and Bernoullis Principle states that as the speed of a moving fluid increases, its internal pressure decreases, helping explain phenomena such as lift on an airplane wing.',
   [('What does fluid dynamics study?', ['How liquids and gases move', 'Only the properties of solid materials', 'Only the temperature of the sun', 'Only electrical circuits'], 0),
    ('What does Bernoullis Principle state about a moving fluid?', ['As the speed of a moving fluid increases, its internal pressure decreases', 'As the speed of a moving fluid increases, its pressure always increases equally', 'Fluid speed and pressure have no relationship at all', 'A fluids pressure never changes regardless of its speed'], 0),
    ('How does Bernoullis Principle help explain lift on an airplane wing?', ['Air moving faster over the curved top of the wing creates lower pressure than beneath it', 'Airplane wings generate lift with no connection to air pressure or speed', 'Lift is created only by the engines, with no role for the wings shape', 'Bernoullis Principle applies only to boats, never aircraft'], 0),
    ('Which of these is an example of a fluid, in the scientific sense?', ['Air, since it is a gas that flows', 'A solid block of steel', 'A wooden chair', 'A brick wall'], 0),
    ('Fluid dynamics is important in the design of which real-world objects?', ['Airplanes, boats, and pipelines', 'Only picture frames', 'Only pieces of furniture', 'Only articles of clothing with no moving parts'], 0)]),
SS('Social Studies: The Geography of Waste-to-Energy Facilities and Urban Waste Management',
   'Grade 9 Social Studies (Geography) strand: waste-to-energy facilities convert municipal solid waste into usable electricity or heat through controlled combustion, offering cities a way to manage waste while raising questions about air quality and the balance with recycling programs.',
   [('What do waste-to-energy facilities do?', ['Convert municipal solid waste into usable electricity or heat', 'Permanently store waste underground with no processing at all', 'Convert waste directly into drinking water', 'Eliminate the need for any waste collection in a city'], 0),
    ('What method do waste-to-energy facilities typically use to process waste?', ['Controlled combustion', 'Freezing waste at extremely low temperatures', 'Simply burying waste with no further treatment', 'Releasing waste directly into rivers'], 0),
    ('What concern is sometimes raised about waste-to-energy facilities?', ['Potential impacts on local air quality from emissions', 'These facilities are universally considered to have zero environmental impact', 'They eliminate the possibility of any air pollution everywhere', 'They have no connection to environmental policy at all'], 0),
    ('How might waste-to-energy facilities interact with a citys recycling programs?', ['Cities must balance diverting recyclable materials with supplying enough waste to the facility', 'Waste-to-energy facilities always eliminate the need for any recycling', 'Recycling and waste-to-energy programs have no relationship to one another', 'Recycling programs are banned in cities that use waste-to-energy facilities'], 0),
    ('Why might a densely populated city consider building a waste-to-energy facility?', ['To manage large volumes of waste while generating usable energy in the process', 'Densely populated cities never produce any waste requiring management', 'These facilities are only ever built in areas with no waste at all', 'Waste management is not a concern in urban geography'], 0)]),
]),
day(130, [
L('Language Review: Grammar, Vocabulary, Reading, and Writing Skills',
  'Grade 9 Language strand review: students revisit the Oxford comma, eponyms, tragic heroes and hamartia, cover letters, influencer marketing, ellipses and em dashes, elegies, malapropisms, and the function of a narrative chorus.',
  [('What is the Oxford comma?', ['A comma placed before the final conjunction in a list of three or more items', 'A comma that always ends a sentence', 'A comma used only in dialogue', 'A type of semicolon'], 0),
   ('What is hamartia?', ['A fatal flaw or error in judgment that leads to a tragic heros downfall', 'A type of happy ending', 'A minor background character', 'A rhyme scheme in poetry'], 0),
   ('What does an ellipsis typically signal in writing?', ['Omitted words or a trailing, unfinished thought', 'The end of a formal citation', 'A grammatical error', 'A question being asked'], 0),
   ('What is a malapropism?', ['The mistaken use of a similar-sounding word in place of the intended word', 'A word borrowed directly from another language', 'A formal grammatical rule', 'A type of punctuation mark'], 0),
   ('What role does a chorus or narrator-commentator typically play?', ['Providing context, commentary, or moral reflection from outside the main action', 'Serving as the storys main antagonist', 'Remaining completely silent throughout the story', 'Replacing the need for any plot at all'], 0)]),
M('Math Review: Advanced Algebra, Number Theory, and Calculus Preview',
  'Grade 9 Math strand review: students revisit synthetic division, prime factorization, the Pythagorean trigonometric identity, three-variable systems, the dot product, mathematical induction, insurance and risk, conditional probability, and limits.',
  [('What does synthetic division provide a shortcut for?', ['Dividing a polynomial by a linear binomial of the form x-a', 'Multiplying two polynomials together', 'Finding the area of a triangle', 'Solving a system of linear equations'], 0),
   ('What does the Fundamental Theorem of Arithmetic state?', ['Every integer greater than one has exactly one prime factorization, aside from order', 'Every integer has infinitely many different prime factorizations', 'Prime numbers do not exist', 'Only even numbers can be factored into primes'], 0),
   ('What does the Pythagorean trigonometric identity state?', ['Sine squared plus cosine squared of an angle equals one', 'Sine plus cosine always equals zero', 'Tangent squared always equals negative one', 'Sine minus cosine always equals one'], 0),
   ('What type of value does the dot product of two vectors produce?', ['A single scalar value', 'A new vector with a different direction', 'A matrix', 'A complex number'], 0),
   ('What does a limit describe?', ['The value a function approaches as its input gets closer to a specific point', 'The exact maximum value of any function', 'A fixed number that never changes across all functions', 'The total area under every curve'], 0)]),
Sc('Science Review: Biotechnology, Physics, and Earth Systems',
   'Grade 9 Science strand review: students revisit CRISPR gene editing, reaction rates and catalysts, simple harmonic motion, exoplanets, the integumentary system, groundwater, acid rain, biomimicry, and fluid dynamics.',
   [('What does CRISPR technology allow scientists to do?', ['Precisely add, remove, or alter sections of DNA', 'Only observe cells without altering them in any way', 'Permanently prevent any changes to DNA', 'Convert DNA directly into RNA with no other function'], 0),
    ('What is a catalyst?', ['A substance that speeds up a reaction without being consumed', 'A substance that always slows down a reaction', 'A product formed only after a reaction ends', 'A type of container used to store chemicals'], 0),
    ('What does simple harmonic motion describe?', ['A repeating back-and-forth movement around a central equilibrium position', 'A single, non-repeating movement in one direction', 'Motion that only occurs in outer space', 'A completely random and unpredictable movement'], 0),
    ('What is an exoplanet?', ['A planet that orbits a star outside our solar system', 'A planet located within our own solar system only', 'A moon that orbits a planet', 'A star with no orbiting planets'], 0),
    ('What does Bernoullis Principle state about a moving fluid?', ['As the speed of a moving fluid increases, its internal pressure decreases', 'As the speed of a moving fluid increases, its pressure always increases equally', 'Fluid speed and pressure have no relationship at all', 'A fluids pressure never changes regardless of its speed'], 0)]),
SS('Social Studies Review: Global Geography and Modern Challenges',
   'Grade 9 Social Studies (Geography) strand review: students revisit space debris, shrinking inland seas, global remittances, urban transit systems, desertification, river deltas, pharmaceutical access, national parks and ecotourism, and waste-to-energy facilities.',
   [('What is space debris?', ['Defunct satellites and fragments left over from past space missions', 'A natural weather pattern found only on Earth', 'A type of ocean current', 'A landform found in mountainous regions'], 0),
    ('What is one example of a dramatically shrinking inland body of water?', ['The Aral Sea', 'The Pacific Ocean', 'The Atlantic Ocean', 'The Arctic Ocean'], 0),
    ('What are remittances?', ['Funds sent by migrant workers back to their home countries', 'Taxes collected exclusively by national governments', 'Loans given only to large corporations', 'Payments made only between two neighbouring countries with no individuals involved'], 0),
    ('What human activity can contribute to desertification?', ['Overgrazing of livestock on fragile land', 'Planting trees to restore degraded land', 'Reducing water use in agriculture', 'Protecting natural vegetation from being removed'], 0),
    ('What is the purpose of a national park?', ['To preserve significant natural or cultural landscapes', 'To maximize industrial development in a region', 'To eliminate all wildlife from a protected area', 'To prevent any form of tourism whatsoever'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g9_121_130)
    append_to(9, g9_121_130)
