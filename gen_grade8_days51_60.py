#!/usr/bin/env python3
"""Phase 3: Grade 8, Days 51-60 (third Grade 8 batch, continuing past the
Day 50 milestone toward a longer school year). Topics chosen to avoid any
overlap with the existing Day 1-50 set (see data/grade8.json): symbolism
and irony in literature, systems of linear inequalities and exponential
growth, plate tectonics and electromagnetism, and the Acadian Expulsion
through the Multiculturalism Act of 1988.

Grade 8's fourth subject key remains "History" (not "SocialStudies"),
consistent with the Days 31-40 and 41-50 batches and the pre-existing
data/grade8.ts.

As with the earlier batches: videoUrl is intentionally left unset for
every subject -- fetch_video_ids.py fills these in automatically on its
next daily run. No embedded ASCII double-quote characters are used
anywhere in question/summary/option text; apostrophes and quotation marks
use the curly Unicode form (’ “ ”) so they never collide with the
double-quoted TS string literals the generator embeds them in.
"""
import sys
sys.path.insert(0, '/sessions/happy-laughing-ritchie/mnt/gradesbooster')
from gen_curriculum import sub, day, append_to

L8 = 'https://tvolearn.com/pages/grade-8-language'
M8 = 'https://tvolearn.com/pages/grade-8-mathematics'
S8 = 'https://tvolearn.com/pages/grade-8-science-and-technology'
H8 = 'https://tvolearn.com/pages/grade-8-social-studies'
RL, RM, RS, RH = (
    'TVO Learn: Grade 8 Language',
    'TVO Learn: Grade 8 Mathematics',
    'TVO Learn: Grade 8 Science & Technology',
    'TVO Learn: Grade 8 History',
)


def L(t, s, q):
    return sub('Language', t, s, RL, L8, q)


def M(t, s, q):
    return sub('Math', t, s, RM, M8, q)


def Sc(t, s, q):
    return sub('Science', t, s, RS, S8, q)


def H(t, s, q):
    return sub('History', t, s, RH, H8, q)


g8_51_60 = [
day(51, [
L('Reading: Analyzing Symbolism in Literature',
  'Grade 8 Reading strand: symbolism is a literary device in which an object, person, or colour represents a deeper idea beyond its literal meaning, adding layers of meaning to a text.',
  [('Symbolism is a literary device in which ___.', ['An object or image represents a deeper idea beyond its literal meaning', 'Every word in a text is taken only at face value', 'A concept unrelated to literary devices', 'A story contains no hidden or deeper meaning at all'], 0),
   ('Which is an example of a common symbol in literature?', ['A dove representing peace', 'A character’s literal grocery list', 'A concept unrelated to symbolism', 'A footnote citing a source'], 0),
   ('Why might an author use symbolism instead of stating an idea directly?', ['It allows readers to engage more deeply by uncovering meaning themselves', 'Symbolism always makes a text less meaningful', 'A reason unrelated to literary analysis', 'Authors never use symbolism for any purpose'], 0),
   ('How can a reader identify a possible symbol in a text?', ['By noticing an object or image that recurs or is given special emphasis', 'Symbols never repeat or receive any special emphasis', 'A concept unrelated to identifying symbols', 'Symbols are always explicitly labelled by the author'], 0),
   ('Why is understanding symbolism useful when analyzing a novel’s themes?', ['Symbols often reinforce or reveal a text’s central themes', 'Symbolism has no connection to a text’s themes', 'A reason unrelated to reading comprehension', 'Themes and symbols are always completely unrelated to each other'], 0)]),
M('Graphing Systems of Linear Inequalities',
  'Grade 8 Math strand (pre-high-school extension): graphing a system of linear inequalities involves shading the solution region for each inequality, where the overlapping shaded area represents all solutions that satisfy every inequality at once.',
  [('Graphing a linear inequality involves shading ___.', ['The region of the graph that contains all solutions to the inequality', 'Only the single line itself, with no shading', 'A concept unrelated to graphing inequalities', 'The entire graph regardless of the inequality'], 0),
   ('In a system of linear inequalities, the solution region is ___.', ['The area where the shaded regions of all inequalities overlap', 'Any area shaded by at least one inequality', 'A concept unrelated to systems of inequalities', 'The area with no shading of any kind'], 0),
   ('A solid line on a graph of an inequality indicates ___.', ['The points on the line are included in the solution', 'The points on the line are never included in the solution', 'A concept unrelated to graphing inequalities', 'There is no solution to the inequality at all'], 0),
   ('A dashed line on a graph of an inequality indicates ___.', ['The points on the line are not included in the solution', 'The points on the line are always included in the solution', 'A concept unrelated to graphing inequalities', 'The inequality has no boundary line at all'], 0),
   ('Why might a business use a system of linear inequalities to model a real-world problem?', ['It can represent multiple limiting conditions, like budget and time, at once', 'Systems of inequalities have no real-world applications', 'A reason unrelated to systems of inequalities', 'A single inequality always models every real-world situation'], 0)]),
Sc('Plate Tectonics and Earthquakes',
   'Grade 8 Science strand: plate tectonics describes how Earth’s crust is divided into large plates that slowly move, and the sudden release of built-up stress along plate boundaries causes earthquakes.',
   [('Plate tectonics describes how ___.', ['Earth’s crust is divided into large plates that slowly move', 'Earth’s crust never moves or changes at all', 'A concept unrelated to plate tectonics', 'The atmosphere circulates around the planet'], 0),
    ('Earthquakes are typically caused by ___.', ['The sudden release of built-up stress along plate boundaries', 'Changes in ocean temperature alone', 'A cause unrelated to earthquakes', 'The rotation of Earth on its axis'], 0),
    ('A fault line is best described as ___.', ['A fracture in Earth’s crust where movement can occur', 'A region with no connection to earthquakes', 'A concept unrelated to plate tectonics', 'An area where no tectonic activity ever occurs'], 0),
    ('Why do earthquakes often occur near plate boundaries?', ['Stress builds up as plates grind, collide, or slide past one another', 'Plate boundaries have no connection to earthquake activity', 'A reason unrelated to plate tectonics', 'Earthquakes only occur far away from any plate boundary'], 0),
    ('Why do scientists study plate tectonics when assessing earthquake risk?', ['It helps identify regions where stress is likely to build and be released', 'Plate tectonics has no connection to earthquake risk', 'A reason unrelated to earth science', 'Earthquake risk cannot be assessed using any scientific method'], 0)]),
H('The Acadian Expulsion (Le Grand Dérangement)',
  'Grade 8 History strand: the Acadian Expulsion was the forced removal of thousands of French-speaking Acadians from their homes in the Maritimes by the British in the mid-1700s, causing widespread suffering and displacement.',
  [('The Acadian Expulsion refers to the forced removal of ___.', ['French-speaking Acadians from their homes in the Maritimes', 'British settlers from Upper Canada', 'A group unrelated to the Acadian Expulsion', 'Indigenous peoples from the Prairies'], 0),
   ('The Acadian Expulsion was carried out by ___.', ['The British', 'The French government', 'A group unrelated to the Acadian Expulsion', 'The government of the United States'], 0),
   ('The Acadian Expulsion took place primarily during ___.', ['The mid-1700s', 'The early 1900s', 'A time period unrelated to the Acadian Expulsion', 'The late 1800s'], 0),
   ('Why were Acadians expelled from their homes, according to British authorities at the time?', ['Concerns over Acadian loyalty during conflict with France', 'Acadians had voluntarily requested to leave the region', 'A reason unrelated to the Acadian Expulsion', 'The expulsion had no connection to any conflict'], 0),
   ('Why is the Acadian Expulsion still remembered as a significant event in Canadian history?', ['It caused immense suffering and permanently reshaped Acadian communities', 'The event had no lasting impact on any communities', 'A reason unrelated to its historical significance', 'It is remembered only as a minor and forgettable event'], 0)])]),
day(52, [
L('Grammar: Active and Passive Voice',
  'Grade 8 Language strand: in active voice, the subject performs the action, while in passive voice, the subject receives the action, often shifting emphasis or omitting who performed it.',
  [('In active voice, the subject ___.', ['Performs the action', 'Receives the action', 'A concept unrelated to voice', 'Never appears in the sentence at all'], 0),
   ('In passive voice, the subject ___.', ['Receives the action', 'Performs the action', 'A concept unrelated to voice', 'Always performs multiple actions at once'], 0),
   ('Which sentence is written in active voice?', ['The dog chased the ball.', 'The ball was chased by the dog.', 'A sentence unrelated to voice', 'The ball has been chased.'], 0),
   ('Which sentence is written in passive voice?', ['The report was written by the committee.', 'The committee wrote the report.', 'A sentence unrelated to voice', 'The committee is writing the report.'], 0),
   ('Why might a writer choose passive voice in a sentence?', ['To emphasize the action or result rather than who performed it', 'Passive voice is never used for any reason', 'A reason unrelated to grammar', 'Active voice always accomplishes the exact same purpose as passive voice'], 0)]),
M('The Discriminant and the Nature of Roots',
  'Grade 8 Math strand (pre-high-school extension): the discriminant, b² - 4ac, reveals whether a quadratic equation has two real roots, one real root, or no real roots.',
  [('The discriminant of a quadratic equation is calculated as ___.', ['b² - 4ac', 'a + b + c', 'A formula unrelated to the discriminant', 'b² + 4ac'], 0),
   ('If the discriminant is positive, the quadratic equation has ___.', ['Two real roots', 'No real roots', 'A result unrelated to the discriminant', 'Exactly one real root'], 0),
   ('If the discriminant equals zero, the quadratic equation has ___.', ['Exactly one real root', 'Two real roots', 'A result unrelated to the discriminant', 'No real roots'], 0),
   ('If the discriminant is negative, the quadratic equation has ___.', ['No real roots', 'Exactly one real root', 'A result unrelated to the discriminant', 'Two real roots'], 0),
   ('Why is the discriminant useful before fully solving a quadratic equation?', ['It quickly reveals how many real solutions to expect', 'The discriminant provides no useful information', 'A reason unrelated to quadratic equations', 'It always guarantees the equation has two real roots'], 0)]),
Sc('The Rock Cycle: Igneous, Sedimentary, Metamorphic',
   'Grade 8 Science strand: the rock cycle describes how igneous, sedimentary, and metamorphic rocks continuously transform into one another through processes like heat, pressure, weathering, and erosion.',
   [('Igneous rock forms when ___.', ['Molten rock cools and solidifies', 'Layers of sediment are compressed over time', 'A process unrelated to igneous rock', 'Existing rock is transformed by heat and pressure alone'], 0),
    ('Sedimentary rock forms when ___.', ['Layers of sediment are compressed and cemented together over time', 'Molten rock cools and solidifies', 'A process unrelated to sedimentary rock', 'Rock is melted completely into magma'], 0),
    ('Metamorphic rock forms when ___.', ['Existing rock is transformed by intense heat and pressure', 'Molten rock cools quickly at Earth’s surface', 'A process unrelated to metamorphic rock', 'Sediment is deposited with no further change'], 0),
    ('Why is the rock cycle described as continuous rather than one-directional?', ['Rocks can transform from one type to another repeatedly over long periods of time', 'Once formed, a rock can never become a different type of rock', 'A reason unrelated to the rock cycle', 'The rock cycle only occurs once in Earth’s history'], 0),
    ('Which of these could cause sedimentary rock to become metamorphic rock?', ['Intense heat and pressure deep within Earth’s crust', 'Simple exposure to rainfall at the surface', 'A process unrelated to the rock cycle', 'Cooling of molten rock at the surface'], 0)]),
H('The Rebellions of 1837-38 (Upper and Lower Canada)',
  'Grade 8 History strand: the Rebellions of 1837-38 were armed uprisings in Upper and Lower Canada against colonial governments, driven by demands for greater political representation and reform.',
  [('The Rebellions of 1837-38 took place in ___.', ['Upper and Lower Canada', 'The Maritime colonies', 'A region unrelated to the Rebellions of 1837-38', 'Western Canada'], 0),
   ('A major cause of the Rebellions of 1837-38 was ___.', ['Demands for greater political representation and reform', 'A demand to expel all British colonial settlers immediately', 'A cause unrelated to the Rebellions of 1837-38', 'A dispute over territory with the United States'], 0),
   ('Which leader is closely associated with the rebellion in Upper Canada?', ['William Lyon Mackenzie', 'John A. Macdonald', 'A leader unrelated to the Rebellions of 1837-38', 'George Brown'], 0),
   ('Which leader is closely associated with the rebellion in Lower Canada?', ['Louis-Joseph Papineau', 'Wilfrid Laurier', 'A leader unrelated to the Rebellions of 1837-38', 'Robert Baldwin'], 0),
   ('Why are the Rebellions of 1837-38 considered significant in Canadian history?', ['They contributed to later reforms, including the movement toward responsible government', 'They had no lasting influence on Canadian political development', 'A reason unrelated to their historical significance', 'They immediately resulted in full independence for the colonies'], 0)])]),
day(53, [
L('Writing: The Editorial/Op-Ed',
  'Grade 8 Writing strand: an editorial or op-ed presents a writer’s opinion on a current issue, supported by evidence and reasoning, and often aims to persuade readers or prompt action.',
  [('An editorial or op-ed is written to ___.', ['Present a writer’s opinion on a current issue', 'Report only neutral facts with no opinion at all', 'A concept unrelated to this type of writing', 'Tell a completely fictional story'], 0),
   ('An effective editorial supports its opinion with ___.', ['Evidence and reasoning', 'No support of any kind', 'A concept unrelated to editorials', 'Only unsupported personal feelings'], 0),
   ('Which is a common purpose of an editorial?', ['To persuade readers or prompt them to take action', 'To avoid taking any position on an issue', 'A purpose unrelated to editorials', 'To present only opposing viewpoints with no clear stance'], 0),
   ('Which of these would be an appropriate topic for an op-ed?', ['A current issue affecting a community, such as a new local policy', 'A private conversation with no public relevance', 'A concept unrelated to op-eds', 'A completely invented, fictional event'], 0),
   ('Why might a writer address a counterargument in an editorial?', ['It strengthens their argument by showing they have considered other viewpoints', 'Addressing a counterargument always weakens an editorial', 'A reason unrelated to persuasive writing', 'Editorials should never mention any other viewpoint'], 0)]),
M('Exponential Growth and Decay',
  'Grade 8 Math strand: exponential growth occurs when a quantity increases by a consistent percentage over equal time periods, while exponential decay occurs when a quantity decreases the same way, both modelled with the form y = a(b)^x.',
  [('Exponential growth occurs when a quantity ___.', ['Increases by a consistent percentage over equal time periods', 'Increases by the same fixed amount every time period', 'A concept unrelated to exponential growth', 'Remains exactly the same over time'], 0),
   ('Exponential decay occurs when a quantity ___.', ['Decreases by a consistent percentage over equal time periods', 'Increases by a consistent percentage over equal time periods', 'A concept unrelated to exponential decay', 'Decreases by the same fixed amount every time period'], 0),
   ('In the exponential formula y = a(b)^x, if b is greater than 1, the situation represents ___.', ['Growth', 'Decay', 'A situation unrelated to this formula', 'No change at all'], 0),
   ('In the exponential formula y = a(b)^x, if b is between 0 and 1, the situation represents ___.', ['Decay', 'Growth', 'A situation unrelated to this formula', 'No change at all'], 0),
   ('Which of these is a real-world example of exponential growth?', ['A population of bacteria doubling every hour', 'A car losing a fixed dollar amount of value every year', 'A concept unrelated to exponential growth', 'A temperature that stays constant all day'], 0)]),
Sc('Electromagnetism: Fields and Electromagnets',
   'Grade 8 Science strand: an electric current moving through a wire creates a magnetic field, and coiling the wire around an iron core strengthens this field, forming an electromagnet.',
   [('An electric current moving through a wire creates ___.', ['A magnetic field', 'A permanent change in the wire’s colour', 'A concept unrelated to electromagnetism', 'No effect of any kind on the surrounding space'], 0),
    ('An electromagnet is created by ___.', ['Coiling a current-carrying wire around an iron core', 'Placing two permanent magnets next to each other with no current', 'A concept unrelated to electromagnets', 'Removing all metal from a circuit'], 0),
    ('Which of these would increase the strength of an electromagnet?', ['Increasing the number of coils of wire around the core', 'Removing the iron core entirely', 'A change unrelated to electromagnet strength', 'Decreasing the electric current flowing through the wire'], 0),
    ('Unlike a permanent magnet, an electromagnet’s magnetic field can be ___.', ['Turned on and off by controlling the electric current', 'Never changed under any circumstances', 'A property unrelated to electromagnets', 'Only activated by extreme heat'], 0),
    ('Why are electromagnets useful in devices like electric motors and doorbells?', ['Their magnetic field can be controlled and changed as needed', 'Electromagnets provide no practical use in technology', 'A reason unrelated to electromagnetism', 'They function identically to permanent magnets with no advantages'], 0)]),
H('The Chinese Head Tax and Exclusion Act',
  'Grade 8 History strand: the Chinese Head Tax and later Chinese Exclusion Act were discriminatory Canadian policies that restricted and eventually nearly banned Chinese immigration in the late 1800s and early 1900s.',
  [('The Chinese Head Tax was a policy that required ___.', ['Chinese immigrants to pay a fee to enter Canada', 'All immigrants entering Canada to pay an equal fee', 'A policy unrelated to the Chinese Head Tax', 'Chinese immigrants to receive free passage to Canada'], 0),
   ('The Chinese Exclusion Act of 1923 largely ___.', ['Banned Chinese immigration to Canada', 'Eliminated all restrictions on Chinese immigration', 'A policy unrelated to the Chinese Exclusion Act', 'Encouraged unrestricted immigration from every country'], 0),
   ('Why were these policies enacted, according to the discriminatory attitudes of the time?', ['Prejudice against Chinese immigrants and economic competition fears', 'A shortage of workers led the government to welcome all immigrants equally', 'A reason unrelated to these policies', 'These policies were requested by Chinese immigrant communities themselves'], 0),
   ('The Canadian government has since ___ for the Chinese Head Tax.', ['Formally apologized', 'Never acknowledged or discussed it', 'A response unrelated to the Chinese Head Tax', 'Reinstated the same policy'], 0),
   ('Why is it important to study the history of the Chinese Head Tax and Exclusion Act?', ['It highlights past discrimination and informs efforts toward a more inclusive Canada', 'This history has no connection to understanding Canada today', 'A reason unrelated to social studies learning', 'These events never actually occurred in Canadian history'], 0)])]),
day(54, [
L('Vocabulary: Connotation vs Denotation',
  'Grade 8 Language strand: denotation is a word’s literal dictionary definition, while connotation is the emotional or cultural association attached to a word, which can be positive, negative, or neutral.',
  [('Denotation refers to ___.', ['A word’s literal dictionary definition', 'A word’s emotional association', 'A concept unrelated to word meaning', 'A word with no meaning at all'], 0),
   ('Connotation refers to ___.', ['The emotional or cultural association attached to a word', 'A word’s literal dictionary definition only', 'A concept unrelated to connotation', 'A word that has no possible associations'], 0),
   ('Which word has a more positive connotation than “stubborn,” despite a similar denotation?', ['Determined', 'Rigid', 'A word unrelated to this comparison', 'Bossy'], 0),
   ('Why might a writer carefully choose words based on their connotation?', ['To create a specific tone or emotional effect for the reader', 'Connotation never affects how a reader interprets a text', 'A reason unrelated to word choice', 'Denotation and connotation always mean exactly the same thing'], 0),
   ('Which pair of words has similar denotations but different connotations?', ['“Slender” and “skinny”', '“Book” and “car”', 'A pair of words unrelated to this concept', '“Run” and “jump”'], 0)]),
M('Direct and Partial Variation',
  'Grade 8 Math strand: in direct variation, y = kx and the graph passes through the origin, while in partial variation, y = kx + b and the graph has a y-intercept other than zero.',
  [('In direct variation, the relationship between x and y follows the form ___.', ['y = kx', 'y = kx + b, where b is not zero', 'A form unrelated to direct variation', 'y = k, a constant with no variable'], 0),
   ('The graph of a direct variation relationship always passes through ___.', ['The origin (0, 0)', 'A point unrelated to direct variation', 'The point (1, 1) only', 'A point that is never on the y-axis'], 0),
   ('In partial variation, the relationship between x and y follows the form ___.', ['y = kx + b, where b is not zero', 'y = kx only, with no constant', 'A form unrelated to partial variation', 'x = ky, with y as the independent variable'], 0),
   ('If a taxi charges a flat fee plus a rate per kilometre, this relationship represents ___.', ['Partial variation', 'Direct variation', 'A relationship unrelated to variation', 'No variation at all'], 0),
   ('Why does a partial variation graph not pass through the origin?', ['Because of the constant value, b, added to the equation', 'Partial variation graphs always pass through the origin', 'A reason unrelated to partial variation', 'The variable x is never used in partial variation'], 0)]),
Sc('Circuits: Series and Parallel',
   'Grade 8 Science strand: in a series circuit, components are connected along a single path so current has only one route, while in a parallel circuit, components are connected along multiple paths, allowing current to flow through more than one route.',
   [('In a series circuit, components are connected ___.', ['Along a single path, so current has only one route', 'Along multiple separate paths at once', 'A concept unrelated to series circuits', 'With no connection to one another at all'], 0),
    ('In a parallel circuit, components are connected ___.', ['Along multiple paths, allowing current to flow through more than one route', 'Along a single path only', 'A concept unrelated to parallel circuits', 'With no complete path for current at all'], 0),
    ('If one bulb burns out in a series circuit, the rest of the circuit typically ___.', ['Stops working, since the single path is broken', 'Continues working normally with no effect', 'A result unrelated to series circuits', 'Becomes brighter than before'], 0),
    ('If one bulb burns out in a parallel circuit, the rest of the circuit typically ___.', ['Continues working, since other paths remain complete', 'Stops working entirely', 'A result unrelated to parallel circuits', 'Becomes permanently damaged'], 0),
    ('Why are household electrical systems typically wired in parallel rather than series?', ['So that one device failing does not cause all other devices to lose power', 'Parallel wiring provides no advantage over series wiring', 'A reason unrelated to circuits', 'Series wiring is always safer for households'], 0)]),
H('The Komagata Maru Incident',
  'Grade 8 History strand: the Komagata Maru incident of 1914 involved a ship of South Asian passengers who were denied entry to Canada under discriminatory immigration laws and forced to return overseas, resulting in tragedy.',
  [('The Komagata Maru was a ship carrying passengers primarily from ___.', ['South Asia', 'Western Europe', 'A region unrelated to the Komagata Maru incident', 'The Caribbean'], 0),
   ('The passengers of the Komagata Maru were ___ entry into Canada.', ['Largely denied', 'Immediately and fully granted', 'A response unrelated to the Komagata Maru incident', 'Offered citizenship without any restrictions'], 0),
   ('The Komagata Maru incident occurred in ___.', ['1914', '1867', 'A year unrelated to the Komagata Maru incident', '1950'], 0),
   ('The Komagata Maru incident is often cited as an example of ___.', ['Discriminatory Canadian immigration policy in the early 20th century', 'A completely fair and welcoming immigration process', 'A concept unrelated to the Komagata Maru incident', 'A modern immigration policy with no historical roots'], 0),
   ('Why does the Canadian government now formally acknowledge the Komagata Maru incident?', ['To recognize past discrimination and its lasting impact on affected communities', 'The incident has no connection to Canadian immigration history', 'A reason unrelated to the Komagata Maru incident', 'The event has been officially declared to have never happened'], 0)])]),
day(55, [
L('Reading: Analyzing Irony (Verbal, Situational, Dramatic)',
  'Grade 8 Reading strand: verbal irony occurs when a speaker means the opposite of what they say, situational irony occurs when an outcome contradicts expectations, and dramatic irony occurs when the audience knows something a character does not.',
  [('Verbal irony occurs when ___.', ['A speaker says the opposite of what they actually mean', 'A speaker always says exactly what they mean', 'A concept unrelated to irony', 'A character speaks with no possible hidden meaning'], 0),
   ('Situational irony occurs when ___.', ['An outcome contradicts what was expected to happen', 'An outcome always matches exactly what was expected', 'A concept unrelated to situational irony', 'Nothing unexpected ever happens in a story'], 0),
   ('Dramatic irony occurs when ___.', ['The audience knows something a character in the story does not', 'A character knows more than the audience at all times', 'A concept unrelated to dramatic irony', 'Neither the audience nor the characters know anything'], 0),
   ('Which is an example of situational irony?', ['A fire station burning down', 'A character stating they are happy while smiling', 'A concept unrelated to situational irony', 'A character accurately predicting a simple event'], 0),
   ('Why might an author use dramatic irony to build tension in a story?', ['Readers may feel anticipation or dread knowing more than a character does', 'Dramatic irony never affects a reader’s emotional engagement', 'A reason unrelated to dramatic irony', 'Readers always know exactly as much as every character'], 0)]),
M('Venn Diagrams and Set Notation in Probability',
  'Grade 8 Math strand: a Venn diagram visually represents overlapping and non-overlapping sets, and set notation, such as union (∪) and intersection (∩), can be used to calculate probabilities involving multiple events.',
  [('A Venn diagram is used to visually represent ___.', ['Overlapping and non-overlapping sets', 'A single unchanging value with no sets involved', 'A concept unrelated to Venn diagrams', 'Only sets that can never overlap in any way'], 0),
   ('The union of two sets (A ∪ B) includes ___.', ['All elements in either set A, set B, or both', 'Only elements found in both sets at the same time', 'A concept unrelated to set notation', 'No elements from either set'], 0),
   ('The intersection of two sets (A ∩ B) includes ___.', ['Only elements found in both set A and set B', 'All elements in either set, whether or not they overlap', 'A concept unrelated to set notation', 'Elements found in neither set'], 0),
   ('In a Venn diagram, the overlapping region between two circles represents ___.', ['The intersection of the two sets', 'The union of the two sets', 'A concept unrelated to Venn diagrams', 'Elements belonging to neither set'], 0),
   ('Why are Venn diagrams useful when calculating probabilities involving multiple events?', ['They help visualize which outcomes belong to one, both, or neither event', 'Venn diagrams provide no useful information for probability', 'A reason unrelated to probability', 'They can only be used with a single event at a time'], 0)]),
Sc('Chemical Reactions: Types and Balancing Equations',
   'Grade 8 Science strand: a chemical reaction rearranges atoms into new substances, and a balanced chemical equation shows equal numbers of each type of atom on both sides, reflecting the law of conservation of mass.',
   [('A chemical reaction occurs when ___.', ['Atoms rearrange to form new substances', 'Atoms are created or destroyed entirely', 'A concept unrelated to chemical reactions', 'No change happens to any substance involved'], 0),
    ('A balanced chemical equation must show ___.', ['Equal numbers of each type of atom on both sides', 'A different number of atoms on each side of the equation', 'A concept unrelated to balancing equations', 'No atoms represented on either side'], 0),
    ('The law of conservation of mass states that ___.', ['Mass is neither created nor destroyed in a chemical reaction', 'Mass is always created during a chemical reaction', 'A law unrelated to chemical reactions', 'Mass always disappears completely during a reaction'], 0),
    ('In a synthesis reaction, ___.', ['Two or more substances combine to form a single new substance', 'A single substance breaks down into simpler substances', 'A type of reaction unrelated to synthesis', 'No new substance is ever formed'], 0),
    ('In a decomposition reaction, ___.', ['A single substance breaks down into two or more simpler substances', 'Two or more substances combine into a single substance', 'A type of reaction unrelated to decomposition', 'No change occurs to the original substance'], 0)]),
H('The Regina Manifesto and the Rise of the CCF',
  'Grade 8 History strand: the Regina Manifesto of 1933 outlined the founding principles of the Co-operative Commonwealth Federation (CCF), a political party advocating for social welfare programs and economic reform during the Great Depression.',
  [('The Regina Manifesto outlined the founding principles of ___.', ['The Co-operative Commonwealth Federation (CCF)', 'The Conservative Party of Canada', 'A group unrelated to the Regina Manifesto', 'The government of Quebec'], 0),
   ('The Regina Manifesto was created in ___.', ['1933', '1867', 'A year unrelated to the Regina Manifesto', '1982'], 0),
   ('The CCF primarily advocated for ___.', ['Social welfare programs and economic reform', 'The complete elimination of all government programs', 'A concept unrelated to the CCF', 'A return to earlier colonial economic policies'], 0),
   ('The Regina Manifesto was created largely in response to ___.', ['Widespread hardship during the Great Depression', 'A period of significant economic prosperity', 'An event unrelated to the Regina Manifesto', 'The end of the Second World War'], 0),
   ('Why is the CCF significant in Canadian political history?', ['Its ideas influenced later social programs and Canadian political parties', 'It had no lasting influence on Canadian politics', 'A reason unrelated to its historical significance', 'It is remembered only as a fictional political movement'], 0)])]),
day(56, [
L('Writing: The Personal Narrative Essay',
  'Grade 8 Writing strand: a personal narrative essay recounts a meaningful experience from the writer’s life, using descriptive detail, a clear sequence of events, and reflection on what the experience taught them.',
  [('A personal narrative essay recounts ___.', ['A meaningful experience from the writer’s own life', 'A completely fictional story with no connection to the writer', 'A concept unrelated to this type of writing', 'Only factual, impersonal information with no story involved'], 0),
   ('An effective personal narrative often includes ___.', ['Descriptive detail and a clear sequence of events', 'No details or descriptions of any kind', 'A concept unrelated to personal narratives', 'A random, unordered collection of unrelated events'], 0),
   ('Why might a writer include reflection at the end of a personal narrative?', ['To explain what they learned or how the experience changed them', 'Reflection never adds any value to a personal narrative', 'A reason unrelated to this type of writing', 'A personal narrative should never include the writer’s own thoughts'], 0),
   ('Which of these would be an appropriate topic for a personal narrative essay?', ['A time the writer overcame a challenge', 'A set of unrelated historical facts', 'A concept unrelated to personal narratives', 'An essay arguing a persuasive position with no personal story'], 0),
   ('Why is using sensory and descriptive detail important in a personal narrative?', ['It helps the reader vividly picture and connect with the experience', 'Descriptive detail always distracts from the main story', 'A reason unrelated to narrative writing', 'Sensory detail has no effect on how a reader experiences a story'], 0)]),
M('Simplifying Complex Radical Expressions',
  'Grade 8 Math strand (pre-high-school extension): simplifying a radical expression involves factoring out perfect squares from under the radical sign and combining like radical terms.',
  [('Simplifying a radical expression often involves factoring out ___.', ['Perfect squares from under the radical sign', 'Only prime numbers with no other factors', 'A concept unrelated to simplifying radicals', 'The entire expression with no factoring at all'], 0),
   ('Simplify: √50.', ['5√2', '25√2', 'A value unrelated to the calculation', '10√5'], 0),
   ('Simplify: √18.', ['3√2', '9√2', 'A value unrelated to the calculation', '6√3'], 0),
   ('Like radical terms can be combined by ___.', ['Adding or subtracting their coefficients while keeping the radical the same', 'Multiplying the radicals together directly', 'A method unrelated to combining radicals', 'Ignoring the radical portion entirely'], 0),
   ('Simplify: 2√3 + 5√3.', ['7√3', '7√6', 'A value unrelated to the calculation', '10√3'], 0)]),
Sc('The Periodic Table: Trends and Organization',
   'Grade 8 Science strand: the periodic table organizes elements by increasing atomic number into rows called periods and columns called groups, with elements in the same group sharing similar chemical properties.',
   [('The periodic table organizes elements by ___.', ['Increasing atomic number', 'Alphabetical order of their names', 'A concept unrelated to the periodic table', 'Random order with no organizing pattern'], 0),
    ('A row on the periodic table is called a ___.', ['Period', 'Group', 'A term unrelated to the periodic table', 'Isotope'], 0),
    ('A column on the periodic table is called a ___.', ['Group', 'Period', 'A term unrelated to the periodic table', 'Compound'], 0),
    ('Elements within the same group on the periodic table tend to ___.', ['Share similar chemical properties', 'Have no properties in common with one another', 'A concept unrelated to periodic table groups', 'Always have identical atomic numbers'], 0),
    ('Why is the periodic table considered a valuable tool in chemistry?', ['It organizes elements in a way that reveals patterns in their properties', 'The periodic table provides no useful scientific information', 'A reason unrelated to chemistry', 'Elements on the periodic table show no patterns of any kind'], 0)]),
H('The National Energy Program and Western Alienation',
  'Grade 8 History strand: the National Energy Program of 1980 was a federal policy aimed at increasing Canadian control over the oil industry, which fuelled resentment in Western provinces and heightened feelings of Western alienation.',
  [('The National Energy Program was introduced in ___.', ['1980', '1867', 'A year unrelated to the National Energy Program', '2005'], 0),
   ('The National Energy Program aimed to ___.', ['Increase Canadian control over the oil industry', 'Eliminate the oil industry entirely', 'A goal unrelated to the National Energy Program', 'Transfer full control of resources to foreign companies'], 0),
   ('The National Energy Program was especially unpopular in ___.', ['Western provinces, particularly Alberta', 'Atlantic Canada', 'A region unrelated to the National Energy Program', 'Northern territories only'], 0),
   ('Western alienation refers to ___.', ['A sense that Western provinces’ interests are overlooked by the federal government', 'Complete agreement between Western provinces and the federal government', 'A concept unrelated to Western alienation', 'A feeling shared equally by every region of Canada'], 0),
   ('Why is the National Energy Program still discussed in relation to Canadian federalism?', ['It illustrates ongoing tensions between regional interests and federal policy', 'It has no connection to understanding Canadian federalism', 'A reason unrelated to its historical significance', 'It resolved all regional tensions in Canada permanently'], 0)])]),
day(57, [
L('Media Literacy: Analyzing Advertising Techniques',
  'Grade 8 Language strand: advertisers use techniques such as emotional appeal, bandwagon effect, and celebrity endorsement to persuade audiences to buy a product or adopt a particular viewpoint.',
  [('Emotional appeal in advertising works by ___.', ['Triggering feelings, such as happiness or fear, to influence a decision', 'Presenting only neutral, unbiased facts with no persuasive intent', 'A concept unrelated to advertising techniques', 'Avoiding any connection to the audience’s emotions'], 0),
   ('The bandwagon effect in advertising suggests that ___.', ['A person should do or buy something because many others are already doing so', 'No one else is using or buying the product', 'A concept unrelated to the bandwagon effect', 'A product’s popularity has no influence on consumer choices'], 0),
   ('Celebrity endorsement in advertising relies on ___.', ['A well-known person’s association with a product to build trust or appeal', 'Complete anonymity with no recognizable figures involved', 'A concept unrelated to celebrity endorsement', 'Scientific data with no connection to any public figure'], 0),
   ('Why might recognizing advertising techniques help consumers make informed decisions?', ['It helps them evaluate whether a persuasive claim is based on genuine value', 'Recognizing these techniques never affects consumer decision-making', 'A reason unrelated to media literacy', 'All advertisements present entirely objective, unbiased information'], 0),
   ('Which is an example of an emotional appeal in an advertisement?', ['An ad showing a family’s joy while using a product', 'An ad listing only a product’s technical specifications', 'A concept unrelated to emotional appeal', 'An ad with no images, music, or persuasive language at all'], 0)]),
M('Weighted Averages',
  'Grade 8 Math strand: a weighted average accounts for the varying importance, or weight, of each value in a data set, unlike a simple average where every value counts equally.',
  [('A weighted average differs from a simple average because it ___.', ['Accounts for the varying importance, or weight, of each value', 'Treats every value in a data set with equal importance', 'A concept unrelated to weighted averages', 'Ignores every value except the highest one'], 0),
   ('If a test is worth 70% of a grade and a project is worth 30%, this is an example of ___.', ['Weighted averaging', 'A simple average with no weighting involved', 'A concept unrelated to weighted averages', 'A calculation with no connection to grades'], 0),
   ('If a student scores 80% on a test worth 60% of their grade and 90% on a project worth 40%, what is their weighted average?', ['84%', '85%', 'A value unrelated to the calculation', '80%'], 0),
   ('Why might a teacher use a weighted average instead of a simple average to calculate final grades?', ['Some assignments, like exams, may reflect learning more heavily than others', 'A weighted average always produces exactly the same result as a simple average', 'A reason unrelated to weighted averages', 'Weighted averages are never used to calculate grades'], 0),
   ('Why are weighted averages also useful outside of school, such as in finance?', ['They can reflect the varying significance of different values, like investment amounts', 'Weighted averages have no real-world applications', 'A reason unrelated to weighted averages', 'They can only be used to calculate school grades'], 0)]),
Sc('Homeostasis and the Endocrine System',
   'Grade 8 Science strand: homeostasis is the body’s process of maintaining a stable internal environment, and the endocrine system uses hormones released into the bloodstream to help regulate processes like growth, metabolism, and mood.',
   [('Homeostasis refers to the body’s process of ___.', ['Maintaining a stable internal environment', 'Constantly changing its internal environment with no regulation', 'A concept unrelated to homeostasis', 'Shutting down all bodily systems'], 0),
    ('The endocrine system regulates the body using ___.', ['Hormones released into the bloodstream', 'Electrical signals sent only through nerves', 'A concept unrelated to the endocrine system', 'No chemical messengers of any kind'], 0),
    ('Which of these is an example of a process regulated by the endocrine system?', ['Growth and metabolism', 'The colour of a person’s eyes', 'A process unrelated to the endocrine system', 'The number of bones in the body'], 0),
    ('Why is maintaining homeostasis important for the body?', ['It allows the body’s systems to function properly despite external changes', 'Homeostasis has no effect on how the body functions', 'A reason unrelated to homeostasis', 'The body functions best when its internal environment is unstable'], 0),
    ('Why might a malfunctioning endocrine gland affect multiple body systems?', ['Hormones can influence many different processes throughout the body', 'The endocrine system only affects a single, isolated body part', 'A reason unrelated to the endocrine system', 'Hormones have no measurable effect on the body at all'], 0)]),
H('The Oka Crisis',
  'Grade 8 History strand: the Oka Crisis of 1990 was a land dispute and armed standoff between Mohawk protesters and Canadian authorities near Oka, Quebec, that drew national attention to Indigenous land rights.',
  [('The Oka Crisis took place in ___.', ['1990', '1867', 'A year unrelated to the Oka Crisis', '1950'], 0),
   ('The Oka Crisis was primarily a dispute over ___.', ['Land rights near Oka, Quebec', 'A trade agreement with the United States', 'A dispute unrelated to the Oka Crisis', 'Federal funding for education'], 0),
   ('The Oka Crisis involved a standoff between ___.', ['Mohawk protesters and Canadian authorities', 'Two Canadian provinces disputing a border', 'A conflict unrelated to the Oka Crisis', 'Two foreign governments with no Canadian involvement'], 0),
   ('The Oka Crisis drew national attention to ___.', ['Indigenous land rights and relations with the Canadian government', 'International trade policy', 'A concept unrelated to the Oka Crisis', 'Environmental regulations with no connection to land rights'], 0),
   ('Why is the Oka Crisis considered an important event in the history of Indigenous relations in Canada?', ['It highlighted long-standing land rights issues and increased public awareness', 'It had no impact on public awareness of Indigenous issues', 'A reason unrelated to its historical significance', 'It fully resolved all land disputes involving Indigenous communities'], 0)])]),
day(58, [
L('Grammar: Modifiers and Misplaced Modifiers',
  'Grade 8 Language strand: a modifier describes or adds detail to another word in a sentence, and a misplaced modifier is positioned so far from the word it describes that it creates confusion or an unintended meaning.',
  [('A modifier is a word or phrase that ___.', ['Describes or adds detail to another word in a sentence', 'Has no connection to any other word in a sentence', 'A concept unrelated to modifiers', 'Always functions as the main verb of a sentence'], 0),
   ('A misplaced modifier occurs when ___.', ['A modifier is positioned so it creates confusion or an unintended meaning', 'A modifier is placed directly next to the word it describes', 'A concept unrelated to misplaced modifiers', 'A sentence contains no modifiers of any kind'], 0),
   ('Which sentence contains a misplaced modifier?', ['Running down the street, the bus was missed by the man.', 'The man missed the bus while running down the street.', 'A sentence unrelated to misplaced modifiers', 'Running down the street, the man missed the bus.'], 0),
   ('Why can a misplaced modifier create an unintentionally humorous or confusing sentence?', ['It can make a description appear to apply to the wrong noun', 'Misplaced modifiers never affect a sentence’s clarity', 'A reason unrelated to grammar', 'A misplaced modifier always makes a sentence perfectly clear'], 0),
   ('How can a misplaced modifier typically be corrected?', ['By moving the modifier closer to the word it is meant to describe', 'By removing every modifier from the sentence entirely', 'A method unrelated to correcting misplaced modifiers', 'By adding more modifiers to the sentence'], 0)]),
M('Solving Rational Equations',
  'Grade 8 Math strand (pre-high-school extension): solving a rational equation involves eliminating the denominators, often by finding a common denominator or cross-multiplying, then solving the resulting equation.',
  [('A rational equation is an equation that contains ___.', ['At least one fraction with a variable in the denominator', 'No fractions of any kind', 'A concept unrelated to rational equations', 'Only whole numbers with no variables'], 0),
   ('A common first step in solving a rational equation is to ___.', ['Eliminate the denominators by finding a common denominator or cross-multiplying', 'Immediately ignore all denominators in the equation', 'A step unrelated to solving rational equations', 'Add the numerators without addressing the denominators'], 0),
   ('Solve for x: x/2 = 6.', ['x = 12', 'x = 3', 'A value unrelated to the calculation', 'x = 8'], 0),
   ('Solve for x: 3/x = 1/4.', ['x = 12', 'x = 4', 'A value unrelated to the calculation', 'x = 3'], 0),
   ('Why must a solution to a rational equation be checked against the original equation?', ['To ensure the solution does not make any denominator equal to zero', 'Checking a solution is never necessary for rational equations', 'A reason unrelated to rational equations', 'Solutions to rational equations are never affected by their denominators'], 0)]),
Sc('Biomes and Global Ecosystems',
   'Grade 8 Science strand: a biome is a large geographic region characterized by a distinct climate and the plant and animal communities adapted to survive there, such as deserts, rainforests, and tundra.',
   [('A biome is best described as ___.', ['A large geographic region with a distinct climate and adapted living things', 'A single organism living in isolation', 'A concept unrelated to biomes', 'A region with no connection to climate at all'], 0),
    ('Which of these is an example of a biome?', ['Tundra', 'A single backyard garden', 'A concept unrelated to biomes', 'A single species of animal'], 0),
    ('Organisms living in a particular biome are typically ___.', ['Adapted to survive its specific climate and conditions', 'Unaffected by the climate of the biome they live in', 'A concept unrelated to biome adaptation', 'Identical to organisms living in every other biome'], 0),
    ('Why might a cactus be well-adapted to a desert biome?', ['It can store water and survive with very little rainfall', 'Cacti require large amounts of rainfall to survive', 'A reason unrelated to desert adaptation', 'Desert biomes receive the same rainfall as rainforest biomes'], 0),
    ('Why is studying different global biomes valuable for understanding biodiversity?', ['It shows how climate shapes the variety of life found in different regions', 'Biomes have no connection to global biodiversity', 'A reason unrelated to environmental science', 'Every biome on Earth supports the exact same forms of life'], 0)]),
H('Canada’s Role in the Korean War',
  'Grade 8 History strand: Canada contributed troops and naval support to the United Nations forces during the Korean War (1950-1953), marking one of Canada’s significant military commitments after the Second World War.',
  [('Canada contributed troops and naval support to ___ during the Korean War.', ['United Nations forces', 'Only its own domestic defence, with no international involvement', 'A group unrelated to the Korean War', 'The opposing side against the United Nations'], 0),
   ('The Korean War took place primarily between ___.', ['1950 and 1953', 'A time period unrelated to the Korean War', '1914 and 1918', '1980 and 1985'], 0),
   ('Canada’s involvement in the Korean War came ___.', ['After the Second World War', 'Before the First World War', 'A time period unrelated to the Korean War', 'During the Great Depression'], 0),
   ('Why is Canada’s role in the Korean War considered historically significant?', ['It marked one of Canada’s significant military commitments after WWII', 'Canada had no involvement in the Korean War at all', 'A reason unrelated to its historical significance', 'It marked the only time Canada has ever contributed troops internationally'], 0),
   ('Why might Canada have chosen to support United Nations forces during the Korean War?', ['To uphold international cooperation and collective security commitments', 'Canada had no interest in international cooperation at the time', 'A reason unrelated to Canada’s involvement', 'Canada was required to participate with no choice involved'], 0)])]),
day(59, [
L('Reading: Comparing Perspectives Across Texts',
  'Grade 8 Reading strand: comparing perspectives across texts involves examining how different authors or characters view the same event or issue, revealing how background and purpose can shape a viewpoint.',
  [('Comparing perspectives across texts involves examining ___.', ['How different authors or characters view the same event or issue', 'Only a single, unchanging viewpoint shared by every text', 'A concept unrelated to comparing perspectives', 'Texts that have no connection to one another at all'], 0),
   ('Why might two authors present different perspectives on the same historical event?', ['Their background, purpose, or available evidence may shape their viewpoint', 'Authors always share the exact same perspective on every event', 'A reason unrelated to comparing perspectives', 'Historical events can only ever be described in one true way'], 0),
   ('Why is it valuable for readers to compare multiple perspectives on an issue?', ['It helps develop a more complete and balanced understanding of the issue', 'Comparing perspectives never adds any value to understanding a topic', 'A reason unrelated to reading comprehension', 'A single perspective always provides a complete understanding'], 0),
   ('Which of these might indicate that a text presents a particular perspective?', ['The specific language, tone, and details the author chooses to include', 'A text that includes absolutely no language or details at all', 'A concept unrelated to perspective', 'Every text is entirely free of any perspective or bias'], 0),
   ('Why might comparing a primary source and a secondary source on the same topic be useful?', ['It can reveal differences in immediacy, purpose, and interpretation of events', 'Primary and secondary sources always present identical information', 'A reason unrelated to comparing texts', 'Secondary sources never provide any interpretation of events'], 0)]),
M('Transformations of Quadratic Functions',
  'Grade 8 Math strand (pre-high-school extension): transformations of a quadratic function, such as y = a(x - h)² + k, shift, stretch, or reflect its graph compared to the parent function y = x².',
  [('In the equation y = a(x - h)² + k, the value of h shifts the graph ___.', ['Horizontally', 'Vertically', 'A direction unrelated to this transformation', 'Diagonally, at a fixed angle'], 0),
   ('In the equation y = a(x - h)² + k, the value of k shifts the graph ___.', ['Vertically', 'Horizontally', 'A direction unrelated to this transformation', 'Diagonally, at a fixed angle'], 0),
   ('If the value of a in y = a(x - h)² + k is negative, the parabola ___.', ['Opens downward', 'Opens upward', 'A result unrelated to this transformation', 'Becomes a straight line'], 0),
   ('The parent function for a quadratic transformation is typically written as ___.', ['y = x²', 'y = x', 'A function unrelated to quadratic transformations', 'y = 1/x'], 0),
   ('Why are transformations useful for understanding families of quadratic functions?', ['They show how changing values in an equation predictably affects the graph’s shape and position', 'Transformations have no effect on a quadratic function’s graph', 'A reason unrelated to transformations', 'Every quadratic function has an identical graph regardless of its equation'], 0)]),
Sc('Energy Transformations and Conservation of Energy',
   'Grade 8 Science strand: energy can be transformed from one form to another, such as chemical energy into kinetic energy, and the law of conservation of energy states that energy is never created or destroyed, only converted.',
   [('The law of conservation of energy states that energy ___.', ['Is never created or destroyed, only converted from one form to another', 'Is constantly being created out of nothing', 'A law unrelated to energy conservation', 'Disappears completely once it is used'], 0),
    ('Which of these is an example of an energy transformation?', ['Chemical energy in food converting into kinetic energy during exercise', 'Energy remaining in exactly the same form forever', 'A concept unrelated to energy transformations', 'A situation with no energy involved at all'], 0),
    ('A light bulb transforms electrical energy into ___.', ['Light and heat energy', 'Only sound energy, with no light produced', 'A form of energy unrelated to light bulbs', 'Chemical energy exclusively'], 0),
    ('Why might some energy transformations be considered less efficient than others?', ['A portion of the energy is often converted into unwanted heat rather than the intended form', 'All energy transformations are always perfectly efficient with no loss', 'A reason unrelated to energy transformations', 'Energy is never lost as heat during any transformation'], 0),
    ('Why is understanding energy transformations important for designing efficient technology?', ['It helps engineers minimize energy loss and maximize useful output', 'Energy transformations have no connection to technology design', 'A reason unrelated to energy conservation', 'Efficient technology never involves any transformation of energy'], 0)]),
H('The Multiculturalism Act of 1988',
  'Grade 8 History strand: the Canadian Multiculturalism Act of 1988 formally recognized and promoted multiculturalism as a defining feature of Canadian identity, affirming the value of cultural diversity within a unified nation.',
  [('The Canadian Multiculturalism Act was passed in ___.', ['1988', '1867', 'A year unrelated to the Multiculturalism Act', '1950'], 0),
   ('The Multiculturalism Act formally recognized multiculturalism as ___.', ['A defining feature of Canadian identity', 'A temporary policy with no lasting significance', 'A concept unrelated to the Multiculturalism Act', 'A concept rejected by the Canadian government'], 0),
   ('The Multiculturalism Act affirmed the value of ___.', ['Cultural diversity within a unified nation', 'A single, uniform culture for all Canadians', 'A concept unrelated to the Multiculturalism Act', 'Eliminating cultural differences across Canada'], 0),
   ('Canada was among the first countries to adopt an official policy of ___.', ['Multiculturalism', 'Isolationism', 'A policy unrelated to the Multiculturalism Act', 'Strict cultural assimilation'], 0),
   ('Why is the Multiculturalism Act often referenced when discussing Canadian identity?', ['It reflects an official commitment to embracing cultural diversity as part of being Canadian', 'It has no connection to how Canadian identity is understood', 'A reason unrelated to its historical significance', 'It formally rejected the idea of a diverse Canadian society'], 0)])]),
day(60, [
L('Review: Language Arts Days 51-60',
  'Grade 8 Language strand: this review lesson revisits key ideas from Days 51-59, including symbolism, active and passive voice, editorials, connotation versus denotation, irony, personal narratives, advertising techniques, misplaced modifiers, and comparing perspectives.',
  [('Symbolism is a literary device in which ___.', ['An object or image represents a deeper idea beyond its literal meaning', 'Every word in a text is taken only at face value', 'A concept unrelated to literary devices', 'A story contains no hidden or deeper meaning at all'], 0),
   ('In active voice, the subject ___.', ['Performs the action', 'Receives the action', 'A concept unrelated to voice', 'Never appears in the sentence at all'], 0),
   ('Verbal irony occurs when ___.', ['A speaker says the opposite of what they actually mean', 'A speaker always says exactly what they mean', 'A concept unrelated to irony', 'A character speaks with no possible hidden meaning'], 0),
   ('A misplaced modifier occurs when ___.', ['A modifier is positioned so it creates confusion or an unintended meaning', 'A modifier is placed directly next to the word it describes', 'A concept unrelated to misplaced modifiers', 'A sentence contains no modifiers of any kind'], 0),
   ('Why is it useful to review symbolism, voice, irony, and reading strategies together?', ['It reinforces how these language and literacy skills connect and build on one another', 'These topics have no connection to each other', 'A reason unrelated to reviewing language arts', 'Review never helps strengthen understanding of language skills'], 0)]),
M('Review: Days 51-60 Math Concepts',
  'Grade 8 Math strand review: this lesson revisits systems of linear inequalities, the discriminant, exponential growth and decay, direct and partial variation, and transformations of quadratic functions from recent lessons.',
  [('In a system of linear inequalities, the solution region is ___.', ['The area where the shaded regions of all inequalities overlap', 'Any area shaded by at least one inequality', 'A concept unrelated to systems of inequalities', 'The area with no shading of any kind'], 0),
   ('If the discriminant of a quadratic equation is positive, the equation has ___.', ['Two real roots', 'No real roots', 'A result unrelated to the discriminant', 'Exactly one real root'], 0),
   ('Exponential growth occurs when a quantity ___.', ['Increases by a consistent percentage over equal time periods', 'Increases by the same fixed amount every time period', 'A concept unrelated to exponential growth', 'Remains exactly the same over time'], 0),
   ('The graph of a direct variation relationship always passes through ___.', ['The origin (0, 0)', 'A point unrelated to direct variation', 'The point (1, 1) only', 'A point that is never on the y-axis'], 0),
   ('Why is it useful to review inequalities, quadratics, and variation together?', ['These related algebraic concepts reinforce each other for stronger overall understanding', 'These topics have no connection to each other', 'These topics have no connection to each other in mathematics', 'Review is never useful in math'], 0)]),
Sc('Review: Days 51-60 Science Concepts',
   'Grade 8 Science strand review: this lesson revisits plate tectonics, the rock cycle, electromagnetism, circuits, chemical reactions, the periodic table, homeostasis, biomes, and energy transformations from recent lessons.',
   [('Earthquakes are typically caused by ___.', ['The sudden release of built-up stress along plate boundaries', 'Changes in ocean temperature alone', 'A cause unrelated to earthquakes', 'The rotation of Earth on its axis'], 0),
    ('An electromagnet is created by ___.', ['Coiling a current-carrying wire around an iron core', 'Placing two permanent magnets next to each other with no current', 'A concept unrelated to electromagnets', 'Removing all metal from a circuit'], 0),
    ('A balanced chemical equation must show ___.', ['Equal numbers of each type of atom on both sides', 'A different number of atoms on each side of the equation', 'A concept unrelated to balancing equations', 'No atoms represented on either side'], 0),
    ('Homeostasis refers to the body’s process of ___.', ['Maintaining a stable internal environment', 'Constantly changing its internal environment with no regulation', 'A concept unrelated to homeostasis', 'Shutting down all bodily systems'], 0),
    ('Why is it useful to review earth science, physics, chemistry, and biology topics together?', ['It reinforces how these interconnected science concepts relate to one another', 'These topics have no connection to each other', 'Review is never useful in science', 'Each topic must be studied with no connection to the others'], 0)]),
H('Review: Days 51-60 Canadian History',
  'Grade 8 History strand review: this lesson revisits the Acadian Expulsion, the Rebellions of 1837-38, the Chinese Head Tax, the Komagata Maru incident, the Oka Crisis, the Korean War, and the Multiculturalism Act from recent lessons.',
  [('The Acadian Expulsion refers to the forced removal of ___.', ['French-speaking Acadians from their homes in the Maritimes', 'British settlers from Upper Canada', 'A group unrelated to the Acadian Expulsion', 'Indigenous peoples from the Prairies'], 0),
   ('A major cause of the Rebellions of 1837-38 was ___.', ['Demands for greater political representation and reform', 'A demand to expel all British colonial settlers immediately', 'A cause unrelated to the Rebellions of 1837-38', 'A dispute over territory with the United States'], 0),
   ('The Oka Crisis was primarily a dispute over ___.', ['Land rights near Oka, Quebec', 'A trade agreement with the United States', 'A dispute unrelated to the Oka Crisis', 'Federal funding for education'], 0),
   ('The Canadian Multiculturalism Act was passed in ___.', ['1988', '1867', 'A year unrelated to the Multiculturalism Act', '1950'], 0),
   ('Why is it useful to review these 19th and 20th-century Canadian history topics together?', ['It reinforces how these historical events shaped Canadian identity, rights, and policy over time', 'These topics have no connection to one another', 'A reason unrelated to social studies learning', 'Review is never useful when studying history and policy'], 0)])]),
]


def _rebalance_answer_positions(days, seed=20260802):
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
    _rebalance_answer_positions(g8_51_60)
    append_to(8, g8_51_60)
