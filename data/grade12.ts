import type { DayContent } from '@/types';

const curriculum: DayContent[] = [
{day:1, label:"Day 1 — Mon", subjects:[
  {subject:"English", title:"Literary Analysis: University-Level Essay Writing", summary:"Students develop the analytical writing skills required for first-year university — constructing complex arguments, integrating sources, and writing with precision and intellectual authority.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/c/TEDEd",
   videoUrl:"https://www.youtube.com/watch?v=UvsH5y91Eoo",
   quiz:[
     {q:"A university-level literary argument differs from a high school argument in that ___.", options:["it avoids personal interpretation","it requires longer essays","it uses more quotations","it engages with critical conversation"], answer:3},
     {q:"Intellectual authority in academic writing is established through ___.", options:["precise claims backed by strong evidence","only citing many sources","writing confidently regardless of evidence","using complex vocabulary"], answer:0},
     {q:"A counterargument in an academic essay ___.", options:["proves you are unsure of your argument","should always be avoided","weakens your position","strengthens your argument when refuted"], answer:3},
     {q:"Integrating literary criticism responsibly means ___.", options:["engaging critically with secondary sources","avoiding critics who disagree with you","only agreeing with critics","copying the critic's argument as your own"], answer:0},
     {q:"The most important difference between high school and university English is ___.", options:["university requires less reading","intellectual independence in forming your own questions","grammar is more important at university","university essays are always longer"], answer:1}
   ]},
  {subject:"AdvancedFunctions", title:"Polynomial Functions: Deep Dive into Graphs and Equations", summary:"Students investigate polynomial functions of all degrees — connecting multiplicity of zeros, end behaviour, turning points, and algebraic form to graphical behaviour.",
   resourceLabel:"Khan Academy: Polynomial Graphs", resourceUrl:"https://www.youtube.com/watch?v=1WRYEBHLLm8",
   videoUrl:"https://www.youtube.com/watch?v=5fOavu0X1Z0",
   quiz:[
     {q:"A polynomial of degree n can have at most ___ real zeros and at most ___ turning points.", options:["n zeros and n turning points","n-1 zeros and n turning points","n zeros and n-1 turning points","n+1 zeros and n turning points"], answer:2},
     {q:"A zero of multiplicity 2 means the graph ___.", options:["touches but does not cross the x-axis","crosses the x-axis at a 45° angle","has a vertical asymptote","crosses the x-axis steeply"], answer:0},
     {q:"A zero of multiplicity 3 means the graph ___.", options:["touches and bounces","creates a sharp corner","has no x-intercept there","crosses with an S-curve at that zero"], answer:3},
     {q:"For P(x) = −2(x+1)²(x−3)(x−5), the end behaviour is ___.", options:["rises left, rises right","rises left, falls right","falls both directions","falls left, rises right"], answer:2},
     {q:"The Intermediate Value Theorem guarantees ___.", options:["a polynomial is always continuous","a polynomial has exactly n roots","a zero exists if P(a), P(b) have opposite signs","the maximum value of a polynomial"], answer:2}
   ]},
  {subject:"Calculus", title:"Introduction to Limits and Continuity", summary:"Students develop an intuitive and rigorous understanding of limits — what they mean, how to evaluate them, and their role as the foundation of calculus.",
   resourceLabel:"Khan Academy: Limits Intro", resourceUrl:"https://www.youtube.com/watch?v=riXcZT2ICjA",
   videoUrl:"https://www.youtube.com/watch?v=YNstP0ESndU",
   quiz:[
     {q:"The limit of f(x) as x → a means ___.", options:["the value of f(a)","the value f(x) approaches as x nears a","the maximum of f near a","the derivative of f at a"], answer:1},
     {q:"A limit exists at x = a if and only if ___.", options:["f(a) is defined","the function is continuous at a","the left and right-hand limits are equal","the function is differentiable at a"], answer:2},
     {q:"To evaluate lim(x→2) of (x²−4)/(x−2), you ___.", options:["substitute x = 2 directly (gives 0/0)","use L'Hôpital's Rule always","factor and cancel, giving limit = 4","conclude the limit does not exist"], answer:2},
     {q:"A function f is continuous at x = a if ___.", options:["f(a) is a large number","f(a) = 0","f(a) and the limit exist and are equal","the derivative exists at a"], answer:2},
     {q:"A removable discontinuity (hole) occurs when ___.", options:["the function is not defined anywhere","the limit exists but f(a) is undefined or unequal to it","the function goes to infinity","the limit does not exist at the point"], answer:1}
   ]},
  {subject:"Physics", title:"Kinematics in 2D: Projectile Motion", summary:"Students analyse projectile motion by decomposing it into independent horizontal and vertical components, applying kinematic equations to each.",
   resourceLabel:"Crash Course Physics: Projectile Motion", resourceUrl:"https://www.youtube.com/watch?v=aY8z2qO44WA",
   videoUrl:"https://www.youtube.com/watch?v=aY8z2qO44WA",
   quiz:[
     {q:"In projectile motion, the horizontal and vertical components are independent because ___.", options:["gravity acts horizontally","horizontal velocity is always zero","air resistance eliminates horizontal motion","gravity only acts vertically"], answer:3},
     {q:"A projectile launched horizontally from height h has a time of flight determined by ___.", options:["the angle of launch","the vertical fall: t = √(2h/g)","initial horizontal speed only","only horizontal distance"], answer:1},
     {q:"The range of a projectile (launched at angle θ with speed v₀) is maximised when ___.", options:["θ = 30°","θ = 90°","θ = 60°","θ = 45°"], answer:3},
     {q:"At the peak of a projectile's trajectory, ___.", options:["both velocity components are zero","horizontal velocity is zero","the projectile stops momentarily","only vertical velocity is zero"], answer:3},
     {q:"If a ball is kicked at 20 m/s at 30° above horizontal, the initial vertical component is ___.", options:["10√3 m/s","17.3 m/s","10 m/s (20 × sin30°)","20 m/s"], answer:2}
   ]},
]},
{day:2, label:"Day 2 — Tue", subjects:[
  {subject:"English", title:"Independent Study: The Novel — Form and Meaning", summary:"Students read a major novel independently, analysing how formal choices (narration, structure, style) create meaning rather than just content.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/c/TEDEd",
   videoUrl:"https://www.youtube.com/watch?v=S928_8W7JuA",
   quiz:[
     {q:"The distinction between story (fabula) and discourse (sjuzhet) means ___.", options:["only the plot matters","discourse is less important than story","story is raw events; discourse is how they're told","they are the same in all novels"], answer:2},
     {q:"Free indirect discourse (FID) in a novel allows ___.", options:["only third-person narrators to speak","only interior monologue in first person","a narrator to render thoughts without explicit tags","only direct quotation of characters"], answer:2},
     {q:"A novel's structure (chapters, parts, epigraphs) ___.", options:["is only for practical reading purposes","is always chronological","has no relation to meaning","shapes meaning, pacing, and emphasis"], answer:3},
     {q:"Analysing a novel's prose style means ___.", options:["only counting long sentences","examining syntax, imagery, diction, and tone","only noting the vocabulary level","identifying the author's country of origin"], answer:1},
     {q:"A sophisticated novel reading at Grade 12 produces ___.", options:["a plot summary with quotations","only a character description","a thematic overview without formal analysis","an argument about the novel's formal choices"], answer:3}
   ]},
  {subject:"AdvancedFunctions", title:"Rational Functions: Analysis and Graphing", summary:"Students perform complete analysis of rational functions — identifying all asymptotes, holes, intercepts, and behaviour — and graph them without technology.",
   resourceLabel:"Khan Academy: Graphing Rational Functions", resourceUrl:"https://www.youtube.com/watch?v=5TkIe60y2GI",
   videoUrl:"https://www.youtube.com/watch?v=fy45qX8cUwQ",
   quiz:[
     {q:"To find all features of a rational function, you must ___.", options:["factor fully to find zeros, holes, and asymptotes","only find where it equals zero","only graph it with technology","only find vertical asymptotes"], answer:0},
     {q:"A slant (oblique) asymptote exists when ___.", options:["the denominator is linear only","the denominator degree exceeds the numerator","degrees are equal","the numerator degree is exactly 1 more"], answer:3},
     {q:"For f(x) = (2x² + 3x − 2)/( x − 1), the slant asymptote is found by ___.", options:["setting x → ∞ in the numerator","setting denominator = 0","cancelling x terms","dividing to get y = 2x + 5"], answer:3},
     {q:"To sketch a rational function, the correct sequence is ___.", options:["domain, asymptotes, intercepts, connect","graph first, find features after","only find asymptotes","find only the x-intercepts"], answer:0},
     {q:"The end behaviour of f(x) = (x² + 2)/(x + 1) as x → ±∞ is ___.", options:["approaches y = 1","approaches the slant asymptote y = x − 1","approaches y = x²","approaches the horizontal asymptote y = 0"], answer:1}
   ]},
  {subject:"Calculus", title:"Derivatives: Definition and Basic Rules", summary:"Students develop the concept of the derivative as a limit of difference quotients, and apply the basic differentiation rules (power, constant, sum, difference).",
   resourceLabel:"Khan Academy: Derivative Rules", resourceUrl:"https://www.youtube.com/watch?v=HEH_oKNLgUU",
   videoUrl:"https://www.youtube.com/watch?v=WsQQvHm4lSw",
   quiz:[
     {q:"The derivative f'(a) is defined as ___.", options:["f(a+1) − f(a)","lim(h→0)[f(a+h) − f(a)]/h","f(a+h) − f(a)","f(a)/h"], answer:1},
     {q:"The power rule states d/dx[xⁿ] = ___.", options:["xⁿ⁻¹","nxⁿ","nxⁿ+1","nxⁿ⁻¹"], answer:3},
     {q:"d/dx[5x³ − 2x + 7] = ___.", options:["15x³ − 2","15x² − 2","5x³ − 2","5x² − 2"], answer:1},
     {q:"The derivative of a constant is ___.", options:["undefined","1","0","the constant itself"], answer:2},
     {q:"The derivative f'(x) represents ___.", options:["the area under f(x)","the antiderivative of f(x)","the instantaneous rate of change of f(x)","f(x) squared"], answer:2}
   ]},
  {subject:"Physics", title:"Forces: Newton's Laws in 2D", summary:"Students apply Newton's three laws to two-dimensional force problems, including inclined planes, connected masses, and friction.",
   resourceLabel:"Crash Course Physics: Newtons Laws", resourceUrl:"https://www.youtube.com/watch?v=kKKM8Y-u7ds",
   videoUrl:"https://www.youtube.com/watch?v=g550H4e5FCY",
   quiz:[
     {q:"For a block on a frictionless inclined plane at angle θ, the acceleration down the incline is ___.", options:["g sinθ", "g","g tanθ","g cosθ"], answer:0},
     {q:"Normal force on an inclined plane (angle θ, mass m) is ___.", options:["mg","mg cosθ","mg tanθ","mg sinθ"], answer:1},
     {q:"Kinetic friction force equals ___.", options:["μₛN","μN always","μₖmg always","μₖN"], answer:3},
     {q:"Two masses m₁ and m₂ connected by a rope over a frictionless pulley: the acceleration is ___.", options:["g for both","only m₁g","(m₁ − m₂)g/(m₁ + m₂)","(m₂ − m₁)g/(m₁ + m₂)"], answer:2},
     {q:"Newton's Third Law states that for every action force there is ___.", options:["an equal and opposite reaction force","a smaller reaction force in the same direction","no corresponding reaction","a larger reaction force"], answer:0}
   ]},
]},
{day:3, label:"Day 3 — Wed", subjects:[
  {subject:"English", title:"Literature: The Tragic Form Across Cultures", summary:"Students compare the tragic form in different cultural traditions — Greek tragedy, Shakespearean tragedy, and contemporary tragic narratives — examining what 'tragedy' means across time and culture.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/c/TEDEd",
   videoUrl:"https://www.youtube.com/watch?v=I5KZcdAmWLw",
   quiz:[
     {q:"Greek tragedy (Sophocles, Euripides) differs from Shakespearean tragedy in ___.", options:["they are identical in form","Greek tragedy has no hero","Shakespeare's tragedies have no tragic flaws","Greek tragedy uses a chorus and unities"], answer:3},
     {q:"The concept of catharsis (Aristotle) means ___.", options:["the audience's purging of pity and fear","the villain's punishment","the protagonist's recognition of their error","the hero's physical death"], answer:0},
     {q:"Anagnorisis (recognition) in Greek tragedy is ___.", options:["a moment of terrible recognition","a minor plot device","only relevant in comedy","the moment of physical death"], answer:0},
     {q:"Contemporary tragic narratives (film, novel, theatre) typically ___.", options:["avoid tragic form entirely","adapt the tragic hero to be ordinary, not royal","only follow the Greek model","reproduce the Shakespearean model exactly"], answer:1},
     {q:"Comparing tragic forms across cultures illuminates ___.", options:["only literary technique","how cultures understand fate and justice","that tragedy is purely a Western form","only historical differences"], answer:1}
   ]},
  {subject:"AdvancedFunctions", title:"Exponential and Logarithmic Functions: Advanced Applications", summary:"Students solve complex exponential and logarithmic equations, apply change of base, and model real phenomena including logistic growth.",
   resourceLabel:"Khan Academy: Logarithm Properties", resourceUrl:"https://www.youtube.com/watch?v=TMmxKZaCqe0",
   videoUrl:"https://www.youtube.com/watch?v=oqHJ5xQYTEI",
   quiz:[
     {q:"The change of base formula log_b(x) = log(x)/log(b) allows ___.", options:["converting bases only in specific cases","evaluating logs in any base on a calculator","only base-2 conversions","converting only to base 10"], answer:1},
     {q:"Solve: log₂(x) + log₂(x − 2) = 3", options:["x = 4 or x = −2","x = 4","x = 3","x = −2"], answer:1},
     {q:"Logistic growth f(t) = L/(1 + ae^(−kt)) models populations because ___.", options:["it allows unlimited growth","it only models exponential growth","growth slows as it nears carrying capacity L","it always decreases"], answer:2},
     {q:"The natural logarithm ln(x) = log_e(x) is especially important because ___.", options:["e arises naturally in calculus","e is a round number","ln has simpler graphs","ln is easier to calculate"], answer:0},
     {q:"Solve: e^(2x) − 5e^x + 6 = 0", options:["x = ln5","x = ln2 and x = ln3","x = 0","x = 2 and x = 3"], answer:1}
   ]},
  {subject:"Calculus", title:"Derivatives: Product, Quotient, and Chain Rules", summary:"Students master the three composite differentiation rules and apply them to increasingly complex functions.",
   resourceLabel:"Khan Academy: Chain Rule", resourceUrl:"https://www.youtube.com/watch?v=0T0QrHO56qg",
   videoUrl:"https://www.youtube.com/watch?v=V0xlG8gq7uc",
   quiz:[
     {q:"The product rule for d/dx[f(x)g(x)] is ___.", options:["f'(x)g(x) + f(x)g'(x)","f(x)g'(x)","f'(x) × g'(x)","f'(x)g(x)"], answer:0},
     {q:"The quotient rule for d/dx[f(x)/g(x)] is ___.", options:["[f'(x) − g'(x)] / g(x)","[f'(x)g(x) + f(x)g'(x)] / [g(x)]²","f'(x)/g'(x)","[f'g − fg'] / g²"], answer:3},
     {q:"The chain rule for d/dx[f(g(x))] is ___.", options:["f'(g(x)) × g'(x)","f'(x) × g'(x)","f(g'(x))","f'(g(x))"], answer:0},
     {q:"d/dx[(3x² + 1)⁵] = ___.", options:["(3x² + 1)⁵ × 6x","5(6x)⁴","5(3x² + 1)⁴ × 6x","5(3x² + 1)⁴"], answer:2},
     {q:"d/dx[sin(x²)] = ___.", options:["2x cos(x²)","sin(2x)","2x cos(x)","cos(x²)"], answer:0}
   ]},
  {subject:"Physics", title:"Work, Energy, and Power: Advanced Applications", summary:"Students apply the work-energy theorem, conservation of mechanical energy, and power calculations to complex problems.",
   resourceLabel:"Crash Course Physics: Work Energy Power", resourceUrl:"https://www.youtube.com/watch?v=xNzS1OsPbFg",
   videoUrl:"https://www.youtube.com/watch?v=_MR1Dp8-F8w",
   quiz:[
     {q:"The work-energy theorem states ___.", options:["net work equals the change in kinetic energy","power equals work divided by displacement","work equals potential energy change","work equals force times velocity"], answer:0},
     {q:"Conservative forces are those for which ___.", options:["no energy is stored","friction is the best example","work done is path-independent","work depends on the path taken"], answer:2},
     {q:"Conservation of mechanical energy applies when ___.", options:["only conservative forces act, keeping KE + PE constant","only gravity acts","there is no kinetic energy","only friction acts"], answer:1},
     {q:"A 2 kg ball dropped from 5 m hits the ground with kinetic energy ___.", options:["49 J","78 J","98 J","10 J"], answer:2},
     {q:"Power is ___.", options:["energy per unit volume","force per unit area","the rate of energy transfer or work done","work times time"], answer:2}
   ]},
]},
{day:4, label:"Day 4 — Thu", subjects:[
  {subject:"English", title:"Writing: Extended Critical Analysis Essay", summary:"Students plan and write a 1000+ word critical essay on a literary text, meeting university standards for argument, evidence, and analysis.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/c/TEDEd",
   videoUrl:"https://www.youtube.com/watch?v=UvsH5y91Eoo",
   quiz:[
     {q:"University literary essays are evaluated primarily on ___.", options:["word count","the number of sources cited","correct grammar only","the quality of the analytical argument"], answer:3},
     {q:"A 1000+ word essay requires ___.", options:["only one more body paragraph","longer paragraphs with more quotations","more structural complexity and sophisticated transitions","simply more of the same as shorter essays"], answer:2},
     {q:"Evidence in a university essay should be ___.", options:["precisely chosen","replaced by paraphrase always","always a minimum of 5 lines","as long as possible"], answer:0},
     {q:"The difference between analysis and description in an extended essay is ___.", options:["they are the same at university level","description reports; analysis explains how and why","analysis only appears in conclusions","description is more academic"], answer:1},
     {q:"Concluding a long essay effectively requires ___.", options:["synthesising the argument and extending its implications","adding new evidence at the end","summarising all body paragraphs in order","repeating the thesis word for word"], answer:0}
   ]},
  {subject:"AdvancedFunctions", title:"Trigonometric Functions: Identities and Equations (Advanced)", summary:"Students prove and apply advanced trigonometric identities including compound angle, double angle, and sum-to-product formulas, and solve complex trigonometric equations.",
   resourceLabel:"Khan Academy: Trig Identities", resourceUrl:"https://www.youtube.com/watch?v=T9lt6MZKLck",
   videoUrl:"https://www.youtube.com/watch?v=iNj_loo2-W4",
   quiz:[
     {q:"To prove a trigonometric identity, you must ___.", options:["start from both sides simultaneously","cross-multiply to eliminate fractions","substitute specific values","work on one side until it equals the other"], answer:3},
     {q:"Prove: sin2x/(1 + cos2x) = tanx. Using sin2x = 2sinxcosx and cos2x = 2cos²x − 1:", options:["sin2x/(1+cos2x) simplifies to sinx/cosx = tanx","the identity is false","sin2x = tanx always","sin2x/1 + cos2x = tanx is trivially true"], answer:0},
     {q:"Sum-to-product: sinA + sinB = ___.", options:["2sin(A+B)cos(A−B)","2cos((A+B)/2)sin((A−B)/2)","sin(A+B)","2sin((A+B)/2)cos((A−B)/2)"], answer:3},
     {q:"To solve 2cos²x − cosx − 1 = 0 on [0°, 360°):", options:["x = 60° only","x = 0° and 180°","x = 0°, 120°, 240°","x = 120° only"], answer:2},
     {q:"The equation sinx = 2 has ___.", options:["infinitely many solutions","no solution (sinx ≤ 1)","one solution at x = 90°","two solutions"], answer:1}
   ]},
  {subject:"Calculus", title:"Derivatives of Trigonometric and Exponential Functions", summary:"Students differentiate sin(x), cos(x), tan(x), e^x, and ln(x), and combine these with the chain rule.",
   resourceLabel:"Khan Academy: Derivatives of Trig Functions", resourceUrl:"https://www.youtube.com/watch?v=_niP0JaOgHY",
   videoUrl:"https://www.youtube.com/watch?v=yg_497u6JnA",
   quiz:[
     {q:"d/dx[sin x] = ___.", options:["sin x","cos x","−sin x","−cos x"], answer:1},
     {q:"d/dx[cos x] = ___.", options:["−cos x","−sin x","cos x","sin x"], answer:1},
     {q:"d/dx[e^x] = ___.", options:["e^(x−1)","1/e^x","xe^(x−1)","e^x"], answer:3},
     {q:"d/dx[ln x] = ___.", options:["1/x — valid for x > 0","ln x","x/ln x","1/(x ln x)"], answer:0},
     {q:"d/dx[sin(3x²)] = ___.", options:["3x² cos(3x²)","6x cos(3x²) — chain rule: cos(3x²) × 6x","6x sin(3x²)","cos(3x²)"], answer:1}
   ]},
  {subject:"Physics", title:"Circular Motion and Gravitation", summary:"Students analyse uniform circular motion — centripetal acceleration and force — and apply Newton's law of universal gravitation.",
   resourceLabel:"Crash Course Physics: Circular Motion", resourceUrl:"https://www.youtube.com/watch?v=bpFK2VCRHUs",
   videoUrl:"https://www.youtube.com/watch?v=IawY86XveQE",
   quiz:[
     {q:"Centripetal acceleration for uniform circular motion is ___.", options:["v²/r directed toward the centre","rω","v/r","tangential acceleration"], answer:0},
     {q:"The centripetal force is ___.", options:["the outward 'centrifugal force'","a new type of force","the force of rotation","the inward force causing circular motion"], answer:3},
     {q:"Newton's law of universal gravitation: F = ___.", options:["Gm₁m₂/r²","Gm₁m₂r²","Gm₁/m₂r²","Gm₁m₂/r"], answer:0},
     {q:"Gravitational field strength g at Earth's surface is approximately 9.8 N/kg because ___.", options:["it is defined by convention","the Earth rotates","it is always constant everywhere","g = GM_E/R_E² from Newton's law"], answer:3},
     {q:"A satellite in circular orbit has ___.", options:["no gravitational force acting on it","zero speed","both thrust force and gravity","only gravity providing centripetal force"], answer:3}
   ]},
]},
{day:5, label:"Day 5 — Fri", subjects:[
  {subject:"English", title:"Media Analysis: Digital Media and Political Communication", summary:"Students analyse how digital platforms — social media, podcasts, algorithmic news — have transformed political communication and citizenship.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/c/TEDEd",
   videoUrl:"https://www.youtube.com/watch?v=NefOesTl1iQ",
   quiz:[
     {q:"Political communication via social media differs from broadcast media in ___.", options:["its interactive, many-to-many architecture","it has no political influence","it reaches fewer people","it is always more accurate"], answer:0},
     {q:"Algorithmic curation of political content can affect democracy by ___.", options:["creating filter bubbles that limit opposing views","eliminating all political bias in media","only increasing voter turnout","always improving the quality of political debate"], answer:0},
     {q:"Microtargeting in political advertising means ___.", options:["no personalisation in political ads","only using TV advertising","using personal data to target specific individuals","advertising to the largest possible audience"], answer:2},
     {q:"Disinformation campaigns in digital media are effective because ___.", options:["false information is never shared widely","digital platforms always verify content","corrections rarely spread as far as false claims","most people are incapable of critical thinking"], answer:2},
     {q:"A digitally literate citizen evaluates political content by ___.", options:["trusting verified accounts automatically","sharing immediately if it confirms their views","only reading mainstream media","checking the source, corroboration, and who benefits"], answer:3}
   ]},
  {subject:"AdvancedFunctions", title:"Combining Functions: Operations and Compositions", summary:"Students perform operations on functions (sum, difference, product, quotient) and compositions, including finding domains of combined functions.",
   resourceLabel:"Khan Academy: Composite Functions", resourceUrl:"https://www.youtube.com/watch?v=z_tEsVMKOjk",
   videoUrl:"https://www.youtube.com/watch?v=ZFPkQkURSxk",
   quiz:[
     {q:"The domain of (f + g)(x) is ___.", options:["the intersection of the domains of f and g","the domain of f only","the domain of g only","the domain of f union domain of g"], answer:0},
     {q:"The domain of f(x) = √x and g(x) = 1/(x−2): find domain of f(g(x)).", options:["x > 2","x > 0","x ≥ 2","x < 0"], answer:0},
     {q:"If f(x) = x² and g(x) = x + 1, then f(g(x)) − g(f(x)) = ___.", options:["x","0","2x−2","(x+1)² − (x²+1) = x²+2x+1 − x²−1 = 2x"], answer:3},
     {q:"The notation (f ∘ g)(x) means ___.", options:["f(x) + g(x)","f(x) × g(x)","f(g(x))","f(x)/g(x)"], answer:2},
     {q:"If f(x) = 2x − 1 and f(g(x)) = 2x + 3, then g(x) = ___.", options:["x + 2","x + 3","x + 4","2x + 3"], answer:0}
   ]},
  {subject:"Calculus", title:"Applications of Derivatives: Tangent Lines and Related Rates", summary:"Students find equations of tangent and normal lines to curves, and solve introductory related rates problems.",
   resourceLabel:"Khan Academy: Tangent Line Equations", resourceUrl:"https://www.youtube.com/watch?v=IWcPMJBTDQg",
   videoUrl:"https://www.youtube.com/watch?v=j6I3EXiKB2A",
   quiz:[
     {q:"The equation of the tangent line to y = f(x) at (a, f(a)) is ___.", options:["y = f'(a)","y = f(a)(x − a)","y = f(a)x + b","y − f(a) = f'(a)(x − a)"], answer:3},
     {q:"Find the tangent to y = x³ at x = 2.", options:["y = 12x","y = 12x − 10","y = 12x + 8","y = 3x − 2"], answer:1},
     {q:"The normal line to a curve at a point is ___.", options:["the vertical line x = a","parallel to the tangent","perpendicular to the tangent at that point","the tangent line reflected"], answer:2},
     {q:"In related rates problems, you differentiate both sides of an equation with respect to ___.", options:["time (t)","x only","both x and y","the dependent variable"], answer:0},
     {q:"A spherical balloon is inflated so V = 500 cm³/s. Find dR/dt when R = 5 cm. (V = 4/3πR³)", options:["dR/dt = 5/π ≈ 1.59 cm/s","dR/dt = V/(4πR) = 10/π","dR/dt = 500","dR/dt = 4πR²"], answer:0}
   ]},
  {subject:"Physics", title:"Waves: Transverse, Longitudinal, and Sound", summary:"Students examine wave properties (wavelength, frequency, amplitude, speed), the wave equation, and properties of sound.",
   resourceLabel:"Crash Course Physics: Waves and Sound", resourceUrl:"https://www.youtube.com/watch?v=xLbZj5qO_lI",
   videoUrl:"https://www.youtube.com/watch?v=XY0RJu4sDHk",
   quiz:[
     {q:"The wave equation v = fλ relates ___.", options:["wave speed to frequency and wavelength","velocity to force and length","amplitude to frequency","wavelength to period only"], answer:0},
     {q:"Transverse waves differ from longitudinal waves in that ___.", options:["transverse waves are only in vacuum","transverse have no amplitude","transverse waves are faster","transverse: perpendicular; longitudinal: parallel"], answer:3},
     {q:"The Doppler effect explains why ___.", options:["sound cannot travel through air","light always appears red-shifted","waves cannot be reflected","a siren's pitch changes as it approaches or recedes"], answer:3},
     {q:"Resonance occurs when ___.", options:["the driving frequency matches the object's natural frequency","all frequencies are absorbed equally","the amplitude becomes zero","only destructive interference is possible"], answer:0},
     {q:"The speed of sound in air at 20°C is approximately ___.", options:["3 × 10⁸ m/s (that is the speed of light)","about 343 m/s","150 m/s","1000 m/s"], answer:1}
   ]},
]},
{day:6, label:"Day 6 — Mon", subjects:[
  {subject:"English", title:"Literature: Poetry — The Lyric Tradition", summary:"Students study the development of the lyric poem from the Romantics through Modernism to contemporary practice, examining how lyric poetry constructs a speaking self and addresses fundamental human questions.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/c/TEDEd",
   videoUrl:"https://www.youtube.com/watch?v=eRq5PkcLqn8",
   quiz:[
     {q:"The lyric poem is distinguished by ___.", options:["personal feeling voiced by an 'I'","always being short","always rhyming","always being about nature"], answer:0},
     {q:"Romanticism's influence on lyric poetry includes ___.", options:["avoidance of personal feeling","imagination and emotional authenticity","strict adherence to rational argument","rejection of all nature imagery"], answer:1},
     {q:"Modernist lyric poetry (Eliot, Yeats, Stevens) often uses ___.", options:["only traditional forms","fragmentation and allusion","only simple language","straightforward emotional expression"], answer:1},
     {q:"Contemporary lyric poetry engages with ___.", options:["only traditional subjects like love and death","only nature as a subject","a vast range of subjects and forms","only formal experimentation"], answer:2},
     {q:"Close reading a lyric poem involves ___.", options:["only identifying the rhyme scheme","only summarising what the poem is about","attending to every word, sound, line break, and formal choice","only determining whether the speaker is happy or sad"], answer:2}
   ]},
  {subject:"AdvancedFunctions", title:"Polynomial and Rational Equations: Problem Solving", summary:"Students solve higher-degree polynomial equations and applied rational equations, applying the factor theorem, synthetic division, and rational root theorem.",
   resourceLabel:"Khan Academy: Polynomial Division", resourceUrl:"https://www.youtube.com/watch?v=FxHWoUOq2iQ",
   videoUrl:"https://www.youtube.com/watch?v=gD7A1LA4jO8",
   quiz:[
     {q:"The Rational Root Theorem states ___.", options:["a polynomial has n rational roots always","all roots of a polynomial are rational","irrational roots don't exist","p|constant term, q|leading coefficient"], answer:3},
     {q:"For P(x) = 2x³ − 3x² − 11x + 6, possible rational roots are ___.", options:["only positive integers","±1, ±2, ±3, ±6 only","±1, ±2, ±3, ±6, ±1/2, ±3/2","only ±1 and ±6"], answer:2},
     {q:"Testing P(1) = 2 − 3 − 11 + 6 = −6 ≠ 0; P(3) = 54 − 27 − 33 + 6 = 0. So ___.", options:["x = 3 only","x = 3, 1/2, −2","x = 3 and x = 0","x = 1/2 and x = −2 only"], answer:1},
     {q:"Solving a rational inequality (e.g., (x−2)/(x+1) > 0) requires ___.", options:["only testing x = 0","testing signs between critical values","multiplying both sides by (x+1)","squaring both sides"], answer:1},
     {q:"For (x − 2)/(x + 1) > 0, the solution is ___.", options:["x > 2","x < −1","x > 2 or x < −1","−1 < x < 2"], answer:2}
   ]},
  {subject:"Calculus", title:"Curve Sketching Using Derivatives", summary:"Students use the first and second derivative to identify increasing/decreasing intervals, local extrema, concavity, and inflection points.",
   resourceLabel:"Khan Academy: Curve Sketching", resourceUrl:"https://www.youtube.com/watch?v=WIDZFyfaT1I",
   videoUrl:"https://www.youtube.com/watch?v=WqRPFvZWF0k",
   quiz:[
     {q:"If f'(x) > 0 on an interval, then f ___.", options:["is concave up","is increasing on that interval","is decreasing","has a minimum"], answer:1},
     {q:"A local maximum at x = c requires ___.", options:["f'(c) > 0","f'(c) = 0 and changes sign there","f'(c) = 0 only","f'(c) < 0"], answer:1},
     {q:"The second derivative test: if f'(c) = 0 and f''(c) < 0, then ___.", options:["x = c is always a global maximum","x = c is a local maximum (concave down at c)","x = c is an inflection point","x = c is a local minimum"], answer:1},
     {q:"An inflection point occurs where ___.", options:["f'' changes sign","f' = 0","the function has a maximum","f = 0"], answer:0},
     {q:"A complete curve sketch using calculus includes ___.", options:["only zeros and asymptotes","only maxima and minima","intercepts, extrema, and concavity","only x- and y-intercepts"], answer:2}
   ]},
  {subject:"Physics", title:"Electricity: Electric Fields and Potential", summary:"Students analyse electric fields and electric potential produced by point charges and uniform fields, and relate electric potential to potential energy.",
   resourceLabel:"Crash Course Physics: Electric Fields", resourceUrl:"https://www.youtube.com/watch?v=mdulzEfQJP0",
   videoUrl:"https://www.youtube.com/watch?v=VFbyDCG_j18",
   quiz:[
     {q:"The electric field E due to a point charge Q at distance r is ___.", options:["kQ²/r²","kQr²","kQ/r², away from positive charges","kQ/r"], answer:2},
     {q:"Electric potential V at distance r from charge Q is ___.", options:["kQ/r — a scalar, no direction","kQr","kQ²/r","kQ/r² (same as field)"], answer:0},
     {q:"The relationship between electric field and electric potential is ___.", options:["E = −dV/dx (in 1D)","E = V + r","E = V/r only in uniform fields","E = V × r"], answer:0},
     {q:"A positive charge released in a uniform electric field moves ___.", options:["toward lower potential","toward higher potential","perpendicular to field lines","against the field direction"], answer:0},
     {q:"Electric field lines and equipotential surfaces are ___.", options:["parallel to each other","the same thing drawn differently","always perpendicular","only drawn around conductors"], answer:2}
   ]},
]},
{day:7, label:"Day 7 — Tue", subjects:[
  {subject:"English", title:"Drama and Theatre: Contemporary Playwriting", summary:"Students read and analyse a contemporary Canadian play, examining how playwrights structure dramatic conflict, develop character through dialogue, and use theatrical space.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/c/TEDEd",
   videoUrl:"https://www.youtube.com/watch?v=3O_ISCHsaUw",
   quiz:[
     {q:"A contemporary Canadian play is likely to engage with ___.", options:["identity, colonialism, environment","only historical events in theatrical form","only traditional dramatic forms","no Canadian themes"], answer:0},
     {q:"Dialogue in drama does more than convey information — it ___.", options:["is always realistic conversation","only advances the plot","reveals character through subtext","only establishes character mood"], answer:2},
     {q:"Non-realistic staging in contemporary theatre (abstract sets, stylised movement) ___.", options:["requires no interpretation","creates meaning by refusing the illusion of realism","is used to avoid the cost of realistic sets","is always unsuccessful with audiences"], answer:1},
     {q:"Reading a play script for performance means ___.", options:["imagining staging, rhythm, and silence","ignoring stage directions","only reading the dialogue","only finding the themes"], answer:0},
     {q:"Theatre's unique power compared to film or prose is ___.", options:["liveness: an unrepeatable shared event","better special effects","greater budget for production design","permanent record of performance"], answer:0}
   ]},
  {subject:"AdvancedFunctions", title:"Rates of Change: Introduction to Calculus Concepts", summary:"Students explore the concept of instantaneous rate of change as a limit, preparing the foundation for Grade 12 Calculus and making explicit the connection between Advanced Functions and Calculus.",
   resourceLabel:"Khan Academy: Average vs Instantaneous Rate of Change", resourceUrl:"https://www.youtube.com/watch?v=BVZNMm6GaKw",
   videoUrl:"https://www.youtube.com/watch?v=EvJah9UtqEQ",
   quiz:[
     {q:"Average rate of change of f(x) over [a, b] is ___.", options:["[f(b) − f(a)]/(b − a)","f'(a)","[f(b) − f(a)] × (b − a)","f(a)/f(b)"], answer:0},
     {q:"Instantaneous rate of change at x = a is ___.", options:["lim(h→0)[f(a+h) − f(a)]/h","f(a)/a","[f(b)−f(a)]/(b−a) for any b","f(a+1) − f(a)"], answer:0},
     {q:"If f(x) = x², the average rate of change on [2, 2+h] is ___.", options:["4 + 2h","4 + h","4h","2h"], answer:1},
     {q:"As h → 0 in the expression (4 + h), the instantaneous rate of change at x = 2 is ___.", options:["0","h","4 — confirming f'(x) = 2x, f'(2) = 4","2h"], answer:2},
     {q:"Understanding rate of change prepares you for calculus by ___.", options:["establishing the limit concept","replacing all calculus learning","making calculus unnecessary","only being relevant in physics"], answer:0}
   ]},
  {subject:"Calculus", title:"Optimisation: Maximum and Minimum Problems", summary:"Students apply derivatives to find maximum and minimum values in applied context problems — geometry, economics, and physics.",
   resourceLabel:"Khan Academy: Optimization Problems", resourceUrl:"https://www.youtube.com/watch?v=bG1v9tGTIZk",
   videoUrl:"https://www.youtube.com/watch?v=cUMvwG7wvzM",
   quiz:[
     {q:"To solve an optimisation problem with calculus, the steps are ___.", options:["define, differentiate, and solve","sketch and guess","only apply the second derivative test","differentiate directly without identifying the function"], answer:0},
     {q:"A farmer has 200 m of fencing to enclose a rectangular field against a barn (one side free). Maximise the area. If x is the side away from the barn:", options:["x = 50, width = 100, A_max = 5000 m²","x = 50 and area = 50 × 100 = 5000 m²","A = x × 200 − x","x = 100 gives maximum"], answer:0},
     {q:"The second derivative test confirms a maximum when ___.", options:["f''(c) is undefined","f''(c) = 0","f''(c) < 0 (concave down)","f''(c) > 0 (concave up — local minimum)"], answer:2},
     {q:"In an optimisation problem, endpoints of the domain must be checked because ___.", options:["extrema may occur at an endpoint","endpoints always give extrema","global extrema only occur at critical points","critical points are always the answer"], answer:0},
     {q:"Optimisation in real life includes ___.", options:["only geometric problems","only mathematical problems","no economic applications","minimising cost or maximising revenue"], answer:3}
   ]},
  {subject:"Physics", title:"Electric Circuits: Current, Resistance, and Ohm's Law", summary:"Students analyse DC electric circuits — current, voltage, resistance, Ohm's Law, series and parallel circuits, and power dissipation.",
   resourceLabel:"Crash Course Physics: Electric Circuits", resourceUrl:"https://www.youtube.com/watch?v=g-wjP1otQWI",
   videoUrl:"https://www.youtube.com/watch?v=r-SCyD7f_zI",
   quiz:[
     {q:"Ohm's Law states ___.", options:["V = IR²","V = IR","I = V + R","R = V × I"], answer:1},
     {q:"In a series circuit, ___.", options:["voltage is the same across all components","resistance decreases","current divides","current is the same through all components; total resistance = sum of individual resistances; voltage divides"], answer:0},
     {q:"In a parallel circuit, ___.", options:["total resistance is the sum of all resistances","voltage is equal across all branches","current is the same in all branches","voltage divides across branches"], answer:1},
     {q:"Power dissipated in a resistor is ___.", options:["P = IR²","P = V/I","P = IV = I²R = V²/R","P = I/R"], answer:2},
     {q:"Adding a resistor in parallel to a circuit ___.", options:["only changes the voltage","doesn't affect total resistance","decreases total resistance","increases total resistance"], answer:2}
   ]},
]},
{day:8, label:"Day 8 — Wed", subjects:[
  {subject:"English", title:"Writing: The University Application Process and Personal Writing", summary:"Students write personal statements and supplementary essays for university applications, applying their Grade 12 writing skills to genuine high-stakes contexts.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/c/TEDEd",
   videoUrl:"https://www.youtube.com/watch?v=Xz94wRwFOCI",
   quiz:[
     {q:"A university personal statement is most effective when ___.", options:["it lists every achievement in your life","it sounds like every other applicant","it reveals how you think","it focuses only on grades"], answer:2},
     {q:"Showing rather than telling in a personal statement means ___.", options:["only using achievements","describing what sparked your passion","never making claims about yourself","avoiding personal stories"], answer:1},
     {q:"Tailoring a supplementary essay to a specific university or program requires ___.", options:["copying your main personal statement","generic statements about the school","genuine research","avoiding mention of specific courses"], answer:2},
     {q:"The most common fatal flaw in university personal writing is ___.", options:["mentioning personal interests","being too generic, applying to anyone","being too specific","having too unique a perspective"], answer:1},
     {q:"Your personal statement is most valuable to you personally because ___.", options:["it impresses admission officers","only the grade matters","it guarantees admission","it requires serious self-reflection"], answer:3}
   ]},
  {subject:"AdvancedFunctions", title:"Discrete Functions: Advanced Sequences, Series, and Financial Math", summary:"Students apply geometric series formulas to financial mathematics — annuities, mortgages, and investment growth — with university-preparatory rigour.",
   resourceLabel:"Khan Academy: Geometric Series Formula", resourceUrl:"https://www.youtube.com/watch?v=RMa1QSEfzVA",
   videoUrl:"https://www.youtube.com/watch?v=Tj89FA-d0f8",
   quiz:[
     {q:"The future value of an annuity (regular payment R, interest rate i per period, n periods) is ___.", options:["FV = R × i × n","FV = R(1+i)ⁿ","FV = R[(1+i)ⁿ − 1]/i","FV = R × n"], answer:2},
     {q:"If you invest $200/month at 6%/year (0.5%/month) for 30 years, the future value is ___.", options:["$200 × (1.005)^360","200[(1.005)^360 − 1]/0.005 ≈ $200,903","200 × 360 = $72,000","200 × 0.005 × 360"], answer:1},
     {q:"The present value of an annuity formula is ___.", options:["PV = R/i","PV = R(1+i)ⁿ/i","PV = R[1 − (1+i)^(−n)]/i","PV = R × n"], answer:2},
     {q:"A mortgage is a ___.", options:["future value of an annuity problem","perpetuity","present value of an annuity problem","growing annuity"], answer:2},
     {q:"The formula for present value of a perpetuity (payment R, rate i, forever) is ___.", options:["PV = R × ∞","PV = R(1+i)/i","PV = Ri","PV = R/i"], answer:3}
   ]},
  {subject:"Calculus", title:"Integration: The Antiderivative and Indefinite Integrals", summary:"Students are introduced to integration as the reverse of differentiation, applying the power rule for integration and the constant of integration.",
   resourceLabel:"Khan Academy: Antiderivatives and Indefinite Integrals", resourceUrl:"https://www.youtube.com/watch?v=mB7DGEMb0og",
   videoUrl:"https://www.youtube.com/watch?v=xaCPDMEkbig",
   quiz:[
     {q:"The antiderivative (indefinite integral) of f(x) is ___.", options:["f(x)²/2","f'(x)","F(x) such that F'(x) = f(x)","f(x) − C"], answer:2},
     {q:"The power rule for integration: ∫xⁿ dx = ___.", options:["nxⁿ⁻¹","xⁿ/n + C","xⁿ⁺¹ + C","xⁿ⁺¹/(n+1) + C for n ≠ −1"], answer:3},
     {q:"∫(3x² − 4x + 5) dx = ___.", options:["x³ − 2x² + 5x + C","3x³ − 4x² + 5x","6x − 4","x³ + 2x² + 5x + C"], answer:0},
     {q:"The constant of integration C appears because ___.", options:["any constant's derivative is zero","C equals zero always","integration is imprecise","every integral is different"], answer:0},
     {q:"∫sin(x) dx = ___.", options:["−sin(x) + C","−cos(x) + C","sin(x) + C","cos(x) + C"], answer:1}
   ]},
  {subject:"Physics", title:"Magnetic Fields and Forces", summary:"Students examine magnetic fields produced by current-carrying conductors, and the force on a current or moving charge in a magnetic field.",
   resourceLabel:"Crash Course Physics: Magnetic Fields", resourceUrl:"https://www.youtube.com/watch?v=s94suB5uLWw",
   videoUrl:"https://www.youtube.com/watch?v=csMqfwJRjCs",
   quiz:[
     {q:"The force on a charge q moving with velocity v in a magnetic field B is ___.", options:["F = qv × B (vector cross product)","F = mv/qB","F = qvB (this is the magnitude when v ⊥ B)","F = qB/v"], answer:0},
     {q:"A charged particle moving perpendicular to a uniform magnetic field follows ___.", options:["a spiral path along B","a circular path","a parabolic path","a straight line"], answer:1},
     {q:"The force on a current-carrying wire of length L in field B (current I, angle θ) is ___.", options:["F = BIL sinθ","F = IB/L","F = IL/B","F = I/LB"], answer:0},
     {q:"Two parallel wires carrying current in the same direction ___.", options:["do not exert forces on each other","repel each other","rotate around each other","attract each other"], answer:3},
     {q:"The right-hand rule for a solenoid: point fingers in the direction of current wrap, thumb points ___.", options:["at 90° to field","toward the south pole","toward the north pole","in the direction of current flow"], answer:2}
   ]},
]},
{day:9, label:"Day 9 — Thu", subjects:[
  {subject:"English", title:"Independent Reading: Postmodern Literature", summary:"Students read a postmodern novel or short fiction collection, examining metafiction, fragmentation, unreliable narration, and postmodern challenges to stable meaning.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/c/TEDEd",
   videoUrl:"https://www.youtube.com/watch?v=7ECv-j2McbQ",
   quiz:[
     {q:"Postmodern literature challenges ___.", options:["all previous narrative techniques without exception","the concepts of stable, knowable truth and coherent identity","only the use of irony","the idea that literature can accurately represent reality"], answer:1},
     {q:"Metafiction is ___.", options:["only experimental prose poetry","fiction about real events presented as fiction","only found in postmodern novels","fiction aware of its own artifice"], answer:3},
     {q:"Intertextuality in postmodern fiction means ___.", options:["plagiarism from other works","built in dialogue with other texts","only references to classical literature","only quoting other texts directly"], answer:1},
     {q:"Pastiche differs from parody in that ___.", options:["pastiche is always comic","they are identical","pastiche has no relationship to prior works","pastiche imitates without parody's edge"], answer:3},
     {q:"Reading postmodern fiction productively requires ___.", options:["abandoning all interpretive frameworks","accepting that meaning is completely arbitrary","tolerating and enjoying ambiguity","only reading plot summaries"], answer:2}
   ]},
  {subject:"AdvancedFunctions", title:"Introduction to Vectors", summary:"Students are introduced to vectors — geometric and component representations, operations, dot product, and applications to displacement and work.",
   resourceLabel:"Khan Academy: Vectors Introduction", resourceUrl:"https://www.youtube.com/watch?v=fNk_zzaMoSs",
   videoUrl:"https://www.youtube.com/watch?v=yETvIcz1CkE",
   quiz:[
     {q:"A vector differs from a scalar in that ___.", options:["vectors have no application in physics","scalars can be negative","vectors have direction; scalars don't","vectors are always larger"], answer:2},
     {q:"Two vectors a = (a₁, a₂) and b = (b₁, b₂) are added by ___.", options:["a+b = (a₁+b₁, a₂+b₂)","multiplying components","subtracting components","taking the average of each component"], answer:0},
     {q:"The dot product a · b = ___.", options:["a × b (vector cross product)","|a| × |b| (this is only the magnitude part)","a₁b₁ + a₂b₂ = |a||b|cosθ","a₁b₂ + a₂b₁"], answer:2},
     {q:"Two vectors are perpendicular if and only if ___.", options:["their magnitudes are equal","one has zero magnitude","their dot product equals zero","they are in the same direction"], answer:2},
     {q:"The work done by force F over displacement d is ___.", options:["F × d (scalar)","W = F · d = |F||d|cosθ","F + d","|F| × |d|"], answer:1}
   ]},
  {subject:"Calculus", title:"Definite Integrals and the Fundamental Theorem of Calculus", summary:"Students compute definite integrals, apply the Fundamental Theorem of Calculus, and interpret definite integrals as areas.",
   resourceLabel:"Khan Academy: Fundamental Theorem of Calculus", resourceUrl:"https://www.youtube.com/watch?v=9vgCMNHPScU",
   videoUrl:"https://www.youtube.com/watch?v=aeB5BWY0RlE",
   quiz:[
     {q:"The Fundamental Theorem of Calculus Part 1 states ___.", options:["∫f(x)dx from a to a equals 1","integration and differentiation are unrelated","∫f(x)dx can only be approximated","if F'(x) = f(x), then ∫[a to b]f(x)dx = F(b) − F(a)"], answer:3},
     {q:"The definite integral ∫[a to b]f(x)dx represents ___.", options:["the derivative of f at the midpoint","the net signed area under the curve","the average value of f","f(b) − f(a)"], answer:1},
     {q:"∫[0 to 3](2x + 1)dx = ___.", options:["= 12","6","3 × 3 = 9","2x² + x"], answer:0},
     {q:"FTC Part 2 (Leibniz Rule): d/dx[∫[a to x]f(t)dt] = ___.", options:["f(x) − f(a)","f(x)","F(x) − F(a)","∫[a to x]f'(t)dt"], answer:1},
     {q:"The area between two curves f(x) and g(x), where f ≥ g, from a to b is ___.", options:["∫f(x)dx × ∫g(x)dx","∫[a to b][f(x) − g(x)]dx","∫f(x) × g(x)dx","[f(b)−g(b)] − [f(a)−g(a)]"], answer:1}
   ]},
  {subject:"Physics", title:"Electromagnetic Induction", summary:"Students examine Faraday's Law of electromagnetic induction, Lenz's Law, and applications including transformers and generators.",
   resourceLabel:"Crash Course Physics: Electromagnetic Induction", resourceUrl:"https://www.youtube.com/watch?v=pQp6bmJPU_0",
   videoUrl:"https://www.youtube.com/watch?v=LDOa7UdfcMQ",
   quiz:[
     {q:"Faraday's Law states that an EMF is induced in a conductor when ___.", options:["current flows through it","the magnetic flux through it changes","it is placed in a constant magnetic field","it is heated"], answer:1},
     {q:"Lenz's Law states that the induced current flows in a direction that ___.", options:["is always clockwise","has no relation to the cause","opposes the change in magnetic flux","amplifies the change causing it"], answer:2},
     {q:"An electric generator works by ___.", options:["using a battery to create magnetic flux","rotating a coil in a magnetic field","converting electrical energy to mechanical energy (that is a motor)","using nuclear fusion"], answer:1},
     {q:"A transformer steps up voltage by ___.", options:["having fewer primary turns","having more secondary turns than primary turns","using DC current (transformers require AC)","using stronger magnets"], answer:1},
     {q:"The reason high-voltage transmission lines are used to send electricity across long distances is ___.", options:["higher voltage means less power loss","high voltage is safer","high voltage doesn't need towers","only historical convention"], answer:0}
   ]},
]},
{day:10, label:"Day 10 — Fri", subjects:[
  {subject:"English", title:"Literature: Comparative Canadian and World Literature", summary:"Students compare Canadian literature with a world text, analysing how place, history, and culture shape literary form and theme.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/c/TEDEd",
   videoUrl:"https://www.youtube.com/watch?v=nJNdZGF6Xvo",
   quiz:[
     {q:"Comparative literature across cultures reveals ___.", options:["that all literature is the same beneath cultural differences","only surface-level differences","only surface-level similarities","shared themes, told in different ways"], answer:3},
     {q:"Canadian literature is shaped by ___.", options:["only the landscape","only Quebec-English tensions","geography, history, and immigration","only multiculturalism"], answer:2},
     {q:"The concept of 'writing back' (from post-colonial theory) means ___.", options:["only about rejecting Western literature","only Indigenous writing","engaging with colonial traditions","answering letters"], answer:2},
     {q:"A sophisticated comparison of two texts examines ___.", options:["only whether one is better than the other","only their plots","only their dates of publication","how each text illuminates the other"], answer:3},
     {q:"The value of global and comparative literature for Canadian students is ___.", options:["no connection to Canadian identity","only preparation for international travel","it places Canada in a global conversation","only useful for English majors"], answer:2}
   ]},
  {subject:"AdvancedFunctions", title:"Proof and Mathematical Reasoning", summary:"Students examine mathematical proof — direct proof, proof by contradiction, and mathematical induction — developing the formal reasoning skills required for university mathematics.",
   resourceLabel:"Khan Academy: Mathematical Induction", resourceUrl:"https://www.youtube.com/watch?v=wblW_M_HVQ8",
   videoUrl:"https://www.youtube.com/watch?v=SgtOzuADxK8",
   quiz:[
     {q:"A direct proof establishes a theorem by ___.", options:["deriving the theorem from known axioms","finding a counterexample","showing the opposite leads to a contradiction","testing many specific cases"], answer:0},
     {q:"Proof by contradiction assumes ___.", options:["only that algebra is valid","the theorem is sometimes false","the opposite, seeking a contradiction","the theorem is trivially true"], answer:2},
     {q:"Mathematical induction proves a statement P(n) for all n ≥ 1 by ___.", options:["only checking P(1)","proving P(n) is true for some large n","checking P(n) for n = 1 to 100","proving a base case and inductive step"], answer:3},
     {q:"Use induction to prove 1 + 2 + ... + n = n(n+1)/2. The inductive step shows: if 1+...+k = k(k+1)/2, then 1+...+k+(k+1) = ___.", options:["(k+1)(k+1)/2","k(k+1)","k(k+1)/2 + (k+1) = (k+1)(k+2)/2","k²+k/2"], answer:2},
     {q:"A single counterexample ___.", options:["strengthens a theorem by eliminating one case","has no significance in mathematics","disproves a universal statement ('for all n, P(n)')","proves a theorem in all other cases"], answer:2}
   ]},
  {subject:"Calculus", title:"Applications of Integration: Area and Volume", summary:"Students calculate areas under curves, between curves, and volumes of solids of revolution.",
   resourceLabel:"Khan Academy: Volume of Solids of Revolution", resourceUrl:"https://www.youtube.com/watch?v=R_aqSL-q6_8",
   videoUrl:"https://www.youtube.com/watch?v=xec6HTcn2M8",
   quiz:[
     {q:"The area between y = x² and y = x from 0 to 1 is ___.", options:["1/4 − 1/3 = −1/12","∫x² dx","1/2 − 1/3 = 1/6","1 − 1/3 = 2/3"], answer:2},
     {q:"The disc method for volume of revolution around the x-axis gives ___.", options:["V = 2π∫x f(x)dx","V = π∫[f(x)]² dx from a to b","V = π∫f(x)dx","V = ∫f(x)dx"], answer:1},
     {q:"The shell method for volume rotated around the y-axis gives ___.", options:["V = π∫f(x)²dx","V = 2∫f(x)dx","V = ∫f(x)dx","V = 2π∫x f(x)dx from a to b"], answer:3},
     {q:"Find the volume when y = √x from 0 to 4 is rotated around the x-axis.", options:["V = 4π","V = 16π","V = π × 4","V = 8π"], answer:3},
     {q:"Applications of integration in real life include ___.", options:["only physics problems","no applications outside mathematics","probability, work, and volume problems","only area under parabolas"], answer:2}
   ]},
  {subject:"Physics", title:"Modern Physics: Special Relativity", summary:"Students examine Einstein's special relativity — postulates, time dilation, length contraction, mass-energy equivalence, and experimental evidence.",
   resourceLabel:"Crash Course Physics: Special Relativity", resourceUrl:"https://www.youtube.com/watch?v=AInCqm5nCzw",
   videoUrl:"https://www.youtube.com/watch?v=AInCqm5nCzw",
   quiz:[
     {q:"Einstein's two postulates of special relativity are ___.", options:["only one is needed","physics and light speed are constant","matter is energy; time is space","gravity warps space; light bends around mass"], answer:1},
     {q:"Time dilation means ___.", options:["a moving clock runs slower","time passes at the same rate for all observers","clocks in motion run faster","only GPS satellites are affected"], answer:0},
     {q:"Length contraction means ___.", options:["all lengths change equally","objects appear smaller due to perspective","only length perpendicular to motion contracts","moving objects appear shorter: L = L₀/γ"], answer:3},
     {q:"E = mc² means ___.", options:["only radioactive materials have rest energy","mass is a form of energy","nuclear energy is impossible to harness","mass and energy are always the same"], answer:1},
     {q:"Evidence for special relativity includes ___.", options:["no experimental evidence exists","only thought experiments","only GPS corrections","muon lifetime observations"], answer:3}
   ]},
]},
{day:11, label:"Day 11 — Mon", subjects:[
  {subject:"English", title:"Writing: The Argumentative Essay on a Social Issue", summary:"Students write a well-researched argumentative essay on a contemporary social or political issue, integrating sources, acknowledging counterarguments, and making an original contribution.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/c/TEDEd",
   videoUrl:"https://www.youtube.com/watch?v=VZKUeEBryOk",
   quiz:[
     {q:"A strong argumentative essay on a social issue must ___.", options:["only present one side","engage the strongest opposing view","include emotional appeals only","avoid all statistics"], answer:1},
     {q:"Reliable sources for a social issues essay include ___.", options:["only news sources you agree with","any website with 'org' in the domain","only primary sources","peer-reviewed research and quality data"], answer:3},
     {q:"Correlation vs. causation in social science arguments: finding that A and B are correlated means ___.", options:["B must cause A","they are not related","they vary together, cause unclear","A always causes B"], answer:2},
     {q:"Academic integrity in a social issues essay requires ___.", options:["citing sources, distinguishing claims","never using sources","only using your own knowledge","only paraphrasing to avoid citation"], answer:0},
     {q:"The most important quality of an argumentative essay on a controversial topic is ___.", options:["an absence of counterarguments","intellectual honesty","length and number of sources","passionate expression of opinion"], answer:1}
   ]},
  {subject:"AdvancedFunctions", title:"Functions Review: Connecting All Function Families", summary:"Students synthesise the entire Advanced Functions course, connecting all function families and preparing for final assessment.",
   resourceLabel:"Khan Academy: Advanced Functions Review", resourceUrl:"https://www.youtube.com/watch?v=LkwT1GQVJP8",
   videoUrl:"https://www.youtube.com/watch?v=LNZl4GqVm58",
   quiz:[
     {q:"The fundamental difference between polynomial and rational functions is ___.", options:["number of terms","they are always different in shape","degree only","rational functions divide by a variable"], answer:3},
     {q:"Exponential and logarithmic functions are most important because ___.", options:["they are aesthetically pleasing","they model constant percentage change","they model phenomena that are only approximately linear","they are easy to calculate"], answer:1},
     {q:"Trigonometric functions are unique among function families in that ___.", options:["they have no algebraic properties","they are periodic","they only model sound","they are only defined for angles"], answer:1},
     {q:"Vector operations extend functions by ___.", options:["eliminating scalar quantities","adding magnitude and direction","adding direction to algebra","replacing all other functions"], answer:1},
     {q:"A student who has mastered Advanced Functions can ___.", options:["not extend to calculus","only work in pure mathematics","identify a function's type and features","only solve the types of problems they've seen before"], answer:2}
   ]},
  {subject:"Calculus", title:"Calculus of Exponential and Logarithmic Functions", summary:"Students differentiate and integrate e^(ax), ln(x), and related functions, and apply these to growth/decay problems.",
   resourceLabel:"Khan Academy: Derivatives of Exponential Functions", resourceUrl:"https://www.youtube.com/watch?v=MKQR_acrFOA",
   videoUrl:"https://www.youtube.com/watch?v=nqpn0SQB5ds",
   quiz:[
     {q:"d/dx[e^(ax)] = ___.", options:["e^(ax)/a","a × e^(ax) — chain rule","ae^x","e^(ax)"], answer:1},
     {q:"d/dx[ln(ax)] = ___.", options:["ln(a)/x","a × ln(x)","1/x — ln(a) is a constant","a/x"], answer:2},
     {q:"∫e^(3x) dx = ___.", options:["3e^x + C","3e^(3x) + C","e^(3x)/3 + C","e^(3x) + C"], answer:2},
     {q:"∫(1/x) dx = ___.", options:["ln|x| + C","undefined","x^(−2)/(−2) + C","−1/x² + C"], answer:0},
     {q:"A population grows at a rate proportional to its size: dP/dt = kP. The solution is ___.", options:["P(t) = P₀ + kt","P(t) = P₀(kt)","P(t) = P₀e^(kt)","P(t) = ke^(P₀t)"], answer:2}
   ]},
  {subject:"Physics", title:"Nuclear Physics and Elementary Particles", summary:"Students examine nuclear reactions (fission and fusion), binding energy, and an introduction to the Standard Model of particle physics.",
   resourceLabel:"Crash Course Physics: Nuclear Physics", resourceUrl:"https://www.youtube.com/watch?v=nRmBsxBpTjs",
   videoUrl:"https://www.youtube.com/watch?v=lUhJL7o6_cA",
   quiz:[
     {q:"Nuclear fission involves ___.", options:["radioactive beta decay","splitting a nucleus, releasing energy","combining light nuclei to form heavier ones","only gamma emission"], answer:1},
     {q:"Nuclear fusion involves ___.", options:["combining nuclei, releasing energy","splitting heavy nuclei","no energy release","only proton-electron collisions"], answer:0},
     {q:"Mass defect and binding energy: the mass of a nucleus is ___.", options:["greater than the sum of its parts","equal to the sum of its parts","slightly less than its parts' sum","impossible to measure"], answer:2},
     {q:"The Standard Model of particle physics describes ___.", options:["the particles and forces of matter","only electromagnetic forces","only the structure of atoms","only gravity and electromagnetism"], answer:0},
     {q:"The Higgs boson, discovered in 2012, is significant because ___.", options:["it is the force carrier of gravity","it was already predicted by general relativity","it creates all mass in the universe","it gives particles their mass"], answer:3}
   ]},
]},
{day:12, label:"Day 12 — Tue", subjects:[
  {subject:"English", title:"Media: Creating a Digital Portfolio", summary:"Students curate, design, and reflect on a digital portfolio of their best work across Grade 12, developing skills in curation, self-presentation, and digital literacy.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/c/TEDEd",
   videoUrl:"https://www.youtube.com/watch?v=eCmNTrgmzdk",
   quiz:[
     {q:"A digital portfolio differs from a print portfolio in that ___.", options:["it can include only digital work","it can be hyperlinked and multimedia","it is always better","it never includes reflection"], answer:1},
     {q:"Curating a portfolio requires ___.", options:["including everything you've produced","only including the most recent work","only including error-free work","selecting pieces that show your range"], answer:3},
     {q:"The reflective statement in a portfolio item ___.", options:["only explains what the piece is about","is optional and minor","describes what grade you received","explains why you chose the piece"], answer:3},
     {q:"Designing a digital portfolio involves ___.", options:["no connection to writing skills","only choosing a colour scheme","no aesthetic choices","design choices like good writing"], answer:3},
     {q:"The most important quality in a digital portfolio for university or career purposes is ___.", options:["only the most technical work","as many pieces as possible","authentic evidence of your thinking","the most elaborate visual design"], answer:2}
   ]},
  {subject:"AdvancedFunctions", title:"Exam Preparation: Comprehensive Review", summary:"Students complete comprehensive review of all Advanced Functions content in preparation for final assessment.",
   resourceLabel:"Khan Academy: Advanced Math Review", resourceUrl:"https://www.youtube.com/watch?v=jKrEFOTScwU",
   videoUrl:"https://www.youtube.com/watch?v=5NadGZg4lfI",
   quiz:[
     {q:"Find all zeros of P(x) = x⁴ − 5x² + 4.", options:["x = 1 and x = 4 only","x = ±1 and x = ±2","x = ±2 only","x = ±√5"], answer:1},
     {q:"Solve log₃(x + 2) + log₃(x) = 2.", options:["x = 3","x = 9","x = 7","x = −1+√10 ≈ 2.16 (from x²+2x−9=0)"], answer:3},
     {q:"The graph of f(x) = (x²−9)/(x−3) has ___.", options:["a zero at x=−3 and a hole at x=3","a zero at x = 3","asymptotes at x = 3 and x = −3","a vertical asymptote at x = 3"], answer:0},
     {q:"A vector a = (3, −4) has magnitude ___.", options:["5 (|a| = √(9+16) = √25 = 5)","7","√7","1"], answer:0},
     {q:"For a geometric series with t₁ = 2, r = −1/2, find S∞.", options:["4","4/3 (S∞ = t₁/(1−r))","2","1"], answer:1}
   ]},
  {subject:"Calculus", title:"Differential Equations: Separable and Initial Value Problems", summary:"Students solve separable differential equations and apply them to growth, decay, and Newton's Law of Cooling.",
   resourceLabel:"Khan Academy: Separable Differential Equations", resourceUrl:"https://www.youtube.com/watch?v=H0VEL9TFjqw",
   quiz:[
     {q:"A separable differential equation has the form ___.", options:["dy/dx = f(x)/g(x)","dy/dx = f(x)g(y)","dy/dx = f(x) + g(y)","d²y/dx² = f(y)"], answer:1},
     {q:"To solve dy/dx = 2xy, separate variables: ___.", options:["dy/dx = 2xy → dy = 2xy dx → integrate both sides","dy/y = 2x dx","dy/dx = y²","dy = y dx → y = e^x"], answer:1},
     {q:"An initial condition (e.g., y(0) = 5) determines ___.", options:["the form of the differential equation","only the domain of the solution","whether the equation is separable","only the constant of integration C in the general solution"], answer:3},
     {q:"Newton's Law of Cooling: dT/dt = k(T − T_env) models ___.", options:["only heating problems","only at absolute zero","constant temperature situations","cooling rate proportional to ΔT"], answer:3},
     {q:"The population equation dP/dt = kP(M − P)/M (logistic) is solved by ___.", options:["the power rule only","separation of variables","only numerical methods","direct integration"], answer:1}
   ]},
  {subject:"Physics", title:"Physics Year-End: Connections and Applications", summary:"Students synthesise all Grade 12 Physics — mechanics, fields, waves, modern physics — and examine how physical principles interconnect.",
   resourceLabel:"Crash Course Physics: Year Review", resourceUrl:"https://www.youtube.com/watch?v=kUDhL6C9Lao",
   quiz:[
     {q:"The four fundamental forces of nature are ___.", options:["gravity, EM, and the nuclear forces","gravity, electricity, magnetism, nuclear","friction, normal force, gravity, tension","gravity, magnetism, heat, and nuclear"], answer:0},
     {q:"Conservation laws in physics (energy, momentum, angular momentum, charge) are ___.", options:["less fundamental than Newton's Laws","only valid in isolated systems (no external forces/energy inputs)","only valid in classical physics","approximate — they can be violated in extreme conditions"], answer:1},
     {q:"The wave-particle duality in quantum mechanics, confirmed by the double-slit experiment, means ___.", options:["only light has this property","electrons are both waves and particles simultaneously","quantum objects behave like waves OR particles depending on the experimental setup — observation affects the system in a fundamental, non-classical way","quantum mechanics is incorrect"], answer:1},
     {q:"Special relativity modifies classical mechanics at ___.", options:["only for massless particles","only in gravitational fields","speeds approaching the speed of light","all speeds"], answer:2},
     {q:"The most profound insight from Grade 12 Physics is ___.", options:["physics applies only to extreme conditions","the universe operates through mathematically precise laws","only Newtonian mechanics matters","physics is only about equations"], answer:1}
   ]},
]},
{day:13, label:"Day 13 — Wed", subjects:[
  {subject:"English", title:"Independent Reading Synthesis: Personal Reading List", summary:"Students develop a personal reading list beyond the curriculum, demonstrating wide reading, independent literary judgment, and lifelong reading habits.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/c/TEDEd",
   quiz:[
     {q:"Building a personal reading list involves ___.", options:["following only the curriculum","only choosing bestsellers","reading only within one genre","exploring across genres and cultures"], answer:3},
     {q:"Keeping a reading journal develops ___.", options:["only for readers who become English teachers","no transferable skills","only a record of books completed","the habit of attending carefully to what you read"], answer:3},
     {q:"A recommendation to a peer about a book should include ___.", options:["only the genre","only the plot summary","a specific reason it's worth reading","only the theme"], answer:2},
     {q:"Reading widely beyond the curriculum benefits you by ___.", options:["replacing academic literary study","only improving your exam marks","building vocabulary and empathy","only for entertainment"], answer:2},
     {q:"The lifelong reader develops ___.", options:["a distinctive relationship to language and narrative","only factual knowledge from books","a disinterest in other media","only literary knowledge from fiction"], answer:0}
   ]},
  {subject:"AdvancedFunctions", title:"Mathematical Modelling: Choosing the Right Function", summary:"Students apply all function families to real-world data — choosing, fitting, and interpreting mathematical models.",
   resourceLabel:"Khan Academy: Mathematical Modeling", resourceUrl:"https://www.youtube.com/watch?v=A3M9Ksxrd9c",
   quiz:[
     {q:"When data shows exponential growth that eventually levels off, the best model is ___.", options:["a trigonometric function","a pure exponential function","a polynomial function","a logistic function"], answer:3},
     {q:"Data showing a repeating seasonal pattern with constant amplitude is best modelled by ___.", options:["an exponential function","a sinusoidal (trigonometric) function","a linear function","a polynomial"], answer:1},
     {q:"Data about the cooling of an object over time is best modelled by ___.", options:["a polynomial of degree 2","a linear function","a sinusoidal function","an exponential decay function"], answer:3},
     {q:"Evaluating the quality of a mathematical model requires ___.", options:["only checking the model at known points","only comparing slopes","examining residuals and the model's fit","only looking at the graph"], answer:2},
     {q:"The most important limitation of any mathematical model is ___.", options:["models are always perfect representations","it is a simplification of reality","they require too much computation","they can never be made by students"], answer:1}
   ]},
  {subject:"Calculus", title:"Applications: Calculus in Science and Engineering", summary:"Students apply differentiation and integration to physics (motion, work, fluid pressure) and examine the role of calculus in modern science.",
   resourceLabel:"Khan Academy: Calculus Applications", resourceUrl:"https://www.youtube.com/watch?v=m2MIpDrF7Es",
   quiz:[
     {q:"If s(t) is position, then v(t) = s'(t) and a(t) = v'(t) = s''(t). To find displacement from t₁ to t₂:", options:["use average velocity × time","∫[t₁ to t₂] v(t) dt = s(t₂) − s(t₁)","differentiate s(t)","use the acceleration formula"], answer:1},
     {q:"Work done by a variable force F(x) over displacement from a to b is ___.", options:["F × (b − a)","∫[a to b] F(x) dx","F(a) × (b − a)","F(b) − F(a)"], answer:1},
     {q:"The average value of a continuous function f on [a, b] is ___.", options:["[f(b)−f(a)]/(b−a)","f(a) + f(b))/2 (only for linear functions)","∫[a to b]f(x)dx","[1/(b−a)] × ∫[a to b]f(x)dx"], answer:3},
     {q:"Calculus is fundamental to ___.", options:["only physics","physics, engineering, and economics","only pure mathematics","only engineering"], answer:1},
     {q:"The most important insight calculus provides is ___.", options:["that mathematics can only describe simple systems","only how to find slopes","how to calculate derivatives and integrals","change viewed at an infinitesimal scale"], answer:3}
   ]},
  {subject:"Physics", title:"Astrophysics: Stars, Galaxies, and Cosmology", summary:"Students examine stellar evolution, galaxy structure, and the Big Bang model of the universe, connecting nuclear physics and gravity to astrophysics.",
   resourceLabel:"Crash Course Astronomy: Stars and Cosmology", resourceUrl:"https://www.youtube.com/watch?v=qGHBcRcPQeI",
   quiz:[
     {q:"A star generates energy through ___.", options:["chemical combustion","nuclear fusion","only gravitational contraction","nuclear fission of heavy elements"], answer:1},
     {q:"The Hertzsprung-Russell (H-R) diagram plots ___.", options:["speed vs. mass","distance vs. age","luminosity vs. surface temperature","temperature vs. position"], answer:2},
     {q:"A neutron star forms when ___.", options:["a massive star's core collapses","a star explodes without collapse","a star runs out of hydrogen only","any star dies"], answer:0},
     {q:"The observed redshift of distant galaxies demonstrates ___.", options:["the universe is expanding","the universe is contracting","the speed of light is increasing","only that galaxies are old"], answer:0},
     {q:"The Cosmic Microwave Background (CMB) is ___.", options:["radiation from the first stars","noise in early radio equipment","only visible with optical telescopes","leftover radiation from atoms forming"], answer:3}
   ]},
]},
{day:14, label:"Day 14 — Thu", subjects:[
  {subject:"English", title:"Grade 12 English: Culminating Preparation", summary:"Students prepare for their culminating essay and exam, reviewing the year's literary works and refining their analytical approaches.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/c/TEDEd",
   quiz:[
     {q:"The Grade 12 culminating essay should demonstrate ___.", options:["only correct grammar","your best analytical thinking","only breadth of reading","only length"], answer:1},
     {q:"Preparing for a literary exam involves ___.", options:["only re-reading all the texts","only memorising quotations","understanding each text's key themes","only reviewing the plot of each text"], answer:2},
     {q:"The most effective use of quotations in a timed essay is ___.", options:["using as many as possible","always using long quotations","only using quotations in the introduction","short quotations worth analysing"], answer:3},
     {q:"Engaging with literary criticism in a culminating essay shows ___.", options:["that critics are always right","positioning your view against scholars","that you have no original ideas","only that you have read critics"], answer:1},
     {q:"The last step before submitting a major essay is ___.", options:["only counting the words","reading the conclusion only","only checking spelling","reading it as a skeptic would"], answer:3}
   ]},
  {subject:"AdvancedFunctions", title:"Advanced Functions Final Assessment Review", summary:"Students review all major course concepts and practise exam-level problems.",
   resourceLabel:"Khan Academy: Functions Final Review", resourceUrl:"https://www.youtube.com/watch?v=nRmBsxBpTjs",
   quiz:[
     {q:"The graph of f(x) = x(x−2)²(x+1)³ has x-intercepts at ___.", options:["x = 0, 2, −1 (multiplicities 1, 2, 3)","x = 0, 4, 3","x = 0 and x = 1 only","x = 0, 2, 1"], answer:0},
     {q:"Solve: 2^(x+1) = 5^(x−1)", options:["x = 5/2","x = 4","x = ln5/ln2","x = ln10/ln(5/2)"], answer:3},
     {q:"The function f(x) = (3x²)/(x²−4) has ___.", options:["only x-intercept at x = 0","vertical asymptotes at x = ±2 only","asymptotes x=±2, y=3, intercept x=0","no asymptotes"], answer:2},
     {q:"For vectors a = (1, 3) and b = (4, −2), find a · b and determine if they are perpendicular.", options:["a · b = 0, so perpendicular","a · b = −2 ≠ 0, not perpendicular","a · b = 1 × 4 = 4","a · b = (1+4)(3+(−2)) = 5"], answer:1},
     {q:"Using induction: prove n² > 2n for all n ≥ 3. Base case n = 3: 9 > 6 ✓. Inductive step: assume k² > 2k. Then (k+1)² = ___.", options:["k² + 1","k² + 2k + 1 > 2(k+1)","k(k+1)","k² + 2"], answer:1}
   ]},
  {subject:"Calculus", title:"Calculus Final Assessment Review", summary:"Students review all major Calculus content and practise exam-level problems.",
   resourceLabel:"Khan Academy: Calculus Final Review", resourceUrl:"https://www.youtube.com/watch?v=6HkBGVPWIXA",
   quiz:[
     {q:"Evaluate: lim(x→0) of (sin x)/x.", options:["lim(x→0) sin(x)/x = 1","−1","∞","0"], answer:0},
     {q:"Find the equation of the tangent to f(x) = e^x at x = 0.", options:["y = 2x","y = x + 1","y = x","y = e^x"], answer:1},
     {q:"∫[0 to π]sin(x)dx = ___.", options:["= 2","π","−1","0"], answer:0},
     {q:"The maximum of f(x) = x³ − 3x on [−2, 2] occurs at ___.", options:["x = 1","x = −2","x = −1 and x = 2 (both give f(x) = 2)","x = 0"], answer:2},
     {q:"Solve the IVP: dy/dx = y, y(0) = 3.", options:["y = e^(3x)","y = 3x","y = e^x + 3","y = 3e^x"], answer:3}
   ]},
  {subject:"Physics", title:"Physics Final Assessment Review", summary:"Students review all Grade 12 Physics content and practise exam-level problems.",
   resourceLabel:"Crash Course Physics: Final Review", resourceUrl:"https://www.youtube.com/watch?v=pGj9isFr21U",
   quiz:[
     {q:"A ball on a string of radius 0.5 m completes one revolution in 2 s. Find centripetal acceleration.", options:["ac ≈ 4.93 m/s² (4π²r/T²)","ac = 2π m/s²","ac = 10 m/s²","ac = 5 m/s²"], answer:0},
     {q:"Using Faraday's Law: a coil of 50 turns has its flux change from 0.02 Wb to 0.08 Wb in 0.1 s. The induced EMF is ___.", options:["300 V","30 mV","EMF = 30 V (NΔΦ/Δt)","0.6 V"], answer:2},
     {q:"An object at rest has rest energy E₀ = mc². For m = 1 kg, E₀ = ___.", options:["1 J","9 × 10¹⁶ J (E₀ = mc² = 1 × (3×10⁸)²)","c J","3 × 10⁸ J"], answer:1},
     {q:"A circuit has a 12 V battery, 4Ω and 2Ω resistors in series. Current = ___.", options:["I = 12 A","I = V/R_total = 12/6 = 2 A","I = 3 A","I = 6 A"], answer:1},
     {q:"Time dilation: a muon travels at 0.98c. Its proper lifetime is 2.2 μs. Time measured in lab frame = ___.", options:["t ≈ 11 μs (γt₀)","2.2 μs unchanged","0.44 μs","22 μs"], answer:0}
   ]},
]},
{day:15, label:"Day 15 — Fri", subjects:[
  {subject:"English", title:"Grade 12 English: Exam and Celebration", summary:"A final celebration of Grade 12 English — reflecting on the year's literary journey and looking ahead to university and lifelong reading.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/c/TEDEd",
   quiz:[
     {q:"Grade 12 English culminates in ___.", options:["the end of reading and writing as serious pursuits","only exam preparation","completed study of English","a genuine transformation"], answer:3},
     {q:"The connection between literature and university study is ___.", options:["literary study skills transfer broadly","literature is only relevant in humanities programs","literature is not studied at university","no connection"], answer:0},
     {q:"Reading literature throughout your adult life ___.", options:["is only for people who study English","is largely irrelevant after graduation","sustains growth, meaning, and skill","has no connection to professional success"], answer:2},
     {q:"The writers you have studied in Grade 12 ___.", options:["have given you intellectual companions","are only relevant in academic contexts","have taught you only literary technique","are now no longer relevant"], answer:0},
     {q:"English, as a discipline and a practice, is ___.", options:["only about grammar and spelling","a set of skills you've now mastered and completed","only about fiction and poetry","a lifelong pursuit"], answer:3}
   ]},
  {subject:"AdvancedFunctions", title:"Looking Back, Looking Forward", summary:"Students reflect on their mathematical development across MHF4U and its connection to university mathematics.",
   resourceLabel:"Khan Academy: Looking Ahead to Calculus", resourceUrl:"https://www.youtube.com/watch?v=riXcZT2ICjA",
   quiz:[
     {q:"Advanced Functions has prepared you for university mathematics by ___.", options:["only for students in STEM programs","teaching you all the mathematics you will ever need","developing fluency in function analysis","being equivalent to first-year university calculus"], answer:2},
     {q:"The most transferable mathematical skill from Grade 12 is ___.", options:["reasoning and rigorous argument","memorising all formulas","only knowing specific function types","computing derivatives (which you haven't done in this course)"], answer:0},
     {q:"Mathematics at university is ___.", options:["only about computation","more abstract and proof-based","identical to high school mathematics","easier than high school"], answer:1},
     {q:"The mathematicians whose work you have implicitly used in this course — Euler, Gauss, Newton — ___.", options:["were only interested in pure theory","had no connection to the mathematics you studied","are only important to professional mathematicians","built modern science's framework"], answer:3},
     {q:"Finishing Advanced Functions means ___.", options:["ready for most university programs","you are done with mathematics","you need no further mathematical study","only that you passed the course"], answer:0}
   ]},
  {subject:"Calculus", title:"Calculus: Looking Back and Forward", summary:"Students reflect on the year's learning in calculus and its connections to the mathematical sciences.",
   resourceLabel:"Khan Academy: Calculus Bridge to University", resourceUrl:"https://www.youtube.com/watch?v=WUvTyaaNkzM",
   quiz:[
     {q:"The Fundamental Theorem of Calculus is profound because ___.", options:["it is the most complex theorem in mathematics","it reveals that differentiation and integration","it makes integration easier to compute","only because it involves two operations"], answer:1},
     {q:"Calculus was developed independently by ___.", options:["Descartes and Fermat","Gauss and Euler","Newton and Leibniz in the 17th century","Euclid and Archimedes"], answer:2},
     {q:"The most important application of calculus in the 21st century is ___.", options:["only in physics","only bridge design","arguably machine learning","only in engineering"], answer:2},
     {q:"Differential equations (which you've begun) are ___.", options:["the language in which most of science is written","a minor extension of introductory calculus","only for engineers","less important than algebra"], answer:0},
     {q:"Completing Grade 12 Calculus means ___.", options:["you have mastered all of calculus","ready for university-level calculus","university calculus will be completely familiar","calculus is now closed to you"], answer:1}
   ]},
  {subject:"Physics", title:"Physics: A Final Reflection", summary:"Students reflect on their learning in Grade 12 Physics and the role of physics in understanding the universe.",
   resourceLabel:"Crash Course Physics: Reflecting on Physics", resourceUrl:"https://www.youtube.com/watch?v=kKKM8Y-u7ds",
   quiz:[
     {q:"Physics is the most fundamental science because ___.", options:["it underlies all other sciences","it is the oldest science","it is the most difficult","only physicists understand it"], answer:0},
     {q:"The history of physics shows ___.", options:["a series of revolutionary conceptual shifts","major changes in understanding are no longer possible","only a gradual accumulation of facts","physics is a complete and finished discipline"], answer:0},
     {q:"Quantum mechanics and general relativity, the two great theories of 20th century physics, ___.", options:["are in perfect agreement","have been completely unified","are both confirmed but inconsistent","have no experimental support"], answer:2},
     {q:"Physics shapes your daily life through ___.", options:["only large-scale technologies","only electrical devices","phones, GPS, and medical imaging","no practical applications in everyday life"], answer:2},
     {q:"The greatest gift of physics education is ___.", options:["the habit of confidently asking 'why?'","passing the exam","knowing all the formulas","only useful if you study physics at university"], answer:0}
   ]},
]},
{day:16, label:"Day 16 — Mon", subjects:[
  {subject:"English", title:"Postcolonial Literature: Writing Back to Empire", summary:"Students examine postcolonial theory and its application to literary texts — how writers from formerly colonised nations rewrite colonial narratives.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/watch?v=G15p7uOc-aA",
   videoUrl:"https://www.youtube.com/watch?v=wgIp1wjkEA8",
   quiz:[
     {q:"The term 'writing back' (Ashcroft et al.) refers to ___.", options:["only protest poetry","authors responding to publisher rejections","rewriting colonial canonical texts","only African literature"], answer:2},
     {q:"Chinua Achebe's critique of Conrad's Heart of Darkness argues ___.", options:["Conrad makes Africa a mere backdrop","the novel is flawless","the novel is primarily about navigation","Conrad was not a racist"], answer:0},
     {q:"The use of the coloniser's language by postcolonial writers is ___.", options:["a complex negotiation","a sign of cultural defeat","unproblematic and straightforward","never chosen freely"], answer:0},
     {q:"Hybridity (Homi Bhabha) in postcolonial literature refers to ___.", options:["mixing languages only","cultural mixing produced by colonialism","cultural purity in new nations","a purely biological concept"], answer:1},
     {q:"Applying postcolonial theory to a Canadian text requires ___.", options:["acknowledging Canada's specific colonial history","recognising Canada has no colonial history","treating all colonial experiences as identical","only examining French-English relations"], answer:0}
   ]},
  {subject:"AdvancedFunctions", title:"Vectors in Three Dimensions", summary:"Students extend 2D vector concepts to 3D — Cartesian coordinates, vector operations, magnitude, dot product, and angle between vectors.",
   resourceLabel:"Khan Academy", resourceUrl:"https://www.youtube.com/watch?v=k7RM-ot2NWY",
   quiz:[
     {q:"A vector in 3D is written as ___.", options:["a = (a₁, a₂, a₃) or a₁i + a₂j + a₃k","x + y + z","[x:y:z]","(x, y)"], answer:0},
     {q:"The magnitude of a = (2, −1, 3) is ___.", options:["√(2+1+3) = √6","2 + 1 + 3 = 6","√(4+1+9) = √14","6"], answer:2},
     {q:"The dot product a · b for a=(1,2,3) and b=(4,−1,2) is ___.", options:["4−1+6 = 9... wait: 1×4 + 2×(−1) + 3×2 = 4 − 2 + 6 = 8","4 + 2 + 6 = 12","1×4 − 2×1 + 3×2 = 8","(4,−2,6)"], answer:2},
     {q:"The angle θ between vectors a and b satisfies ___.", options:["cosθ = |a|/|b|","tanθ = a·b","sinθ = a·b/(|a||b|)","cosθ = a·b/(|a||b|)"], answer:3},
     {q:"Two vectors in 3D are perpendicular when ___.", options:["their components are proportional","|a| = |b| = 1","their dot product equals zero","they have equal magnitudes"], answer:2}
   ]},
  {subject:"Calculus", title:"Related Rates: Advanced Applications", summary:"Students solve multi-step related rates problems in geometry, physics, and engineering contexts.",
   resourceLabel:"Khan Academy Calculus", resourceUrl:"https://www.youtube.com/watch?v=I9mVUo-bhM8",
   quiz:[
     {q:"The key step in any related rates problem is ___.", options:["only to identify the unknown","to find the maximum value","to differentiate the known quantity","relate quantities, then differentiate"], answer:3},
     {q:"A ladder 5 m long leans against a wall. The base slides out at 0.5 m/s. When base is 3 m from wall: find how fast the top slides down.", options:["dy/dt = 0.375 m/s down","dy/dt = 0.25 m/s","dy/dt = 0.5 m/s","dy/dt = 1 m/s"], answer:0},
     {q:"Water pours into a conical tank (radius r, height h, r/h = 1/2) at 5 m³/min. Find dh/dt when h = 3 m.", options:["dh/dt = 20/(9π) m/min","dh/dt = 5 m/min","dh/dt = 5/(3π) m/min","dh/dt = 20/(3π) m/min"], answer:0},
     {q:"Two cars leave an intersection at right angles: A at 60 km/h north, B at 80 km/h east. Find rate of distance increase after 1 hour.", options:["140 km/h","72 km/h","50 km/h","100 km/h"], answer:3},
     {q:"What distinguishes a related rates problem from a standard derivative problem?", options:["related rates use only one variable","related rates never require the chain rule","related rates only involve geometry","quantities change together over time"], answer:3}
   ]},
  {subject:"Physics", title:"Momentum and Impulse", summary:"Students analyse linear momentum, impulse, and the impulse-momentum theorem in collision contexts.",
   resourceLabel:"Crash Course Physics", resourceUrl:"https://www.youtube.com/watch?v=nPnPqH-R_Y4",
   quiz:[
     {q:"Linear momentum is defined as ___.", options:["p = Ft","p = mv² (kinetic energy, not momentum)","p = ma","p = mv, a vector quantity"], answer:3},
     {q:"The impulse-momentum theorem states ___.", options:["J = mv only","J = ma × t","J = Ft² ","J = FΔt = Δp"], answer:3},
     {q:"Conservation of linear momentum applies when ___.", options:["friction is absent","all forces are equal","no net external force acts on the system","the system is in free fall"], answer:2},
     {q:"In a perfectly inelastic collision ___.", options:["kinetic energy is conserved","both objects pass through each other","the objects bounce elastically","the objects stick together"], answer:3},
     {q:"A 0.5 kg ball at 10 m/s east collides and sticks to a 1.5 kg ball at rest. Final velocity:", options:["v = 2.5 m/s east","v = 5 m/s","v = 3.3 m/s","v = 10 m/s"], answer:0}
   ]},
]},
{day:17, label:"Day 17 — Tue", subjects:[
  {subject:"English", title:"Comparative Essay: World Literature", summary:"Students write a formal comparative essay on two world literature texts, applying university-level analytical standards.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/watch?v=MSYw502dJNY",
   quiz:[
     {q:"A comparative essay thesis must ___.", options:["describe similarities only","only list the works to be compared","treat works as entirely separate","make a claim about what the comparison reveals"], answer:3},
     {q:"Integrating two texts in a comparative essay is best done by ___.", options:["never mixing the texts","only using plot summaries","using a point-by-point structure for analytical comparison","discussing one text fully, then the other (block method always)"], answer:2},
     {q:"When comparing texts from different cultural contexts, a student must ___.", options:["treat one culture as the norm and the other as exotic","acknowledge the cultural and historical specificity of each text","assume all cultures value the same things","only focus on form, not context"], answer:1},
     {q:"The most sophisticated comparative essays ___.", options:["only describe similarities","find a productive tension","treat texts independently and in parallel only","only note obvious differences"], answer:1},
     {q:"Works from different languages in translation present ___.", options:["opportunities to compare style directly","a specific interpretive challenge","no issues since translation is neutral","no analytical interest"], answer:1}
   ]},
  {subject:"AdvancedFunctions", title:"Lines and Planes in Three Dimensions", summary:"Students write vector and parametric equations of lines in 3D, and scalar and vector equations of planes.",
   resourceLabel:"Khan Academy", resourceUrl:"https://www.youtube.com/watch?v=1DfkHs6MFJk",
   quiz:[
     {q:"The vector equation of a line through point P₀=(x₀,y₀,z₀) with direction d=(a,b,c) is ___.", options:["r = (x₀,y₀,z₀) + t(a,b,c)","r = d × P₀","r = P₀ + t (the direction is missing)","r = (x₀+a, y₀+b, z₀+c)"], answer:0},
     {q:"The parametric equations of the same line are ___.", options:["x=x₀+at, y=y₀+bt, z=z₀+ct","only x = x₀ + at","x=at, y=bt, z=ct only","x=x₀t, y=y₀t, z=z₀t"], answer:0},
     {q:"The scalar (Cartesian) equation of a plane with normal n=(A,B,C) through (x₀,y₀,z₀) is ___.", options:["A(x+x₀)+B(y+y₀)+C(z+z₀)=0","A(x−x₀)+B(y−y₀)+C(z−z₀)=0","A+B+C=D","Ax + By + Cz = 0 (only if through origin)"], answer:1},
     {q:"Two planes are parallel if and only if ___.", options:["their equations differ only by a constant","they have the same x-intercept","their normal vectors are parallel","they are both horizontal"], answer:2},
     {q:"A line is perpendicular to a plane when ___.", options:["the line passes through the origin","its direction matches the normal vector","the line has slope 1","the line's direction vector is horizontal"], answer:1}
   ]},
  {subject:"Calculus", title:"L'Hôpital's Rule and Indeterminate Forms", summary:"Students apply L'Hôpital's Rule to evaluate limits of indeterminate forms (0/0, ∞/∞, ∞−∞, 0·∞).",
   resourceLabel:"Khan Academy Calculus", resourceUrl:"https://www.youtube.com/watch?v=_2aCDXyFZC8",
   quiz:[
     {q:"L'Hôpital's Rule states that if lim f/g = 0/0 or ∞/∞, then ___.", options:["lim f(x)/g(x) = lim f'(x)/g'(x)","lim f/g = f/g evaluated at the limit point","lim f/g = lim (f+g)","lim f/g = lim (f−g)/(g)"], answer:0},
     {q:"Evaluate lim(x→0) sin(x)/x.", options:["Apply L'Hôpital: lim cos(x)/cos(x) = 1","Apply L'Hôpital: lim cos(x)/1 = 1","This is not 0/0 form; the limit is 0","Apply L'Hôpital: lim −sin(x)/0 = undefined"], answer:1},
     {q:"Evaluate lim(x→∞) x/eˣ.", options:["The limit is ∞","L'Hôpital (∞/∞): lim 1/eˣ = 0","The limit is 1","L'Hôpital: lim 1/xeˣ"], answer:1},
     {q:"The form 0·∞ is handled by ___.", options:["directly multiplying the limits","rewriting as 0/0 or ∞/∞, then L'Hôpital","taking the square root","no special technique needed"], answer:1},
     {q:"Evaluate lim(x→0⁺) x·ln(x).", options:["−1","∞","1","0 (rewrite as ∞/∞, apply L'Hôpital)"], answer:3}
   ]},
  {subject:"Physics", title:"Conservation of Momentum: Collisions in 2D", summary:"Students apply conservation of momentum to two-dimensional collisions, resolving vectors into components.",
   resourceLabel:"Crash Course Physics", resourceUrl:"https://www.youtube.com/watch?v=3sGOCBfpmbY",
   quiz:[
     {q:"For a 2D collision, conservation of momentum applies ___.", options:["independently to x and y components","only in the horizontal direction","only for elastic collisions","only if no friction acts"], answer:0},
     {q:"In a 2D elastic collision, both ___ and ___ are conserved.", options:["force and time","momentum and kinetic energy","mass and velocity","mass and charge"], answer:1},
     {q:"A 2 kg ball moving at 5 m/s east hits a 2 kg ball at rest. After collision ball 1 moves north. By symmetry (equal masses, elastic):", options:["ball 2 moves east at 5 m/s, ball 1 stops","ball 1 bounces back west","both stop","both balls move east at 2.5 m/s"], answer:0},
     {q:"The coefficient of restitution e = ___.", options:["e = v₁_initial/v₂_final","e = m₁/m₂","e = final momentum/initial momentum","e = speed after/speed before"], answer:3},
     {q:"An explosion (reverse collision) starting from rest: total momentum after = ___.", options:["equal to the initial kinetic energy","zero — momentum stays conserved at zero","equal to the mass times the speed of the larger piece","equal to the net external force"], answer:1}
   ]},
]},
{day:18, label:"Day 18 — Wed", subjects:[
  {subject:"English", title:"Literary Theory: Reading Through a Lens", summary:"Students apply feminist, Marxist, and psychoanalytic critical lenses to literary texts, understanding how theory shapes interpretation.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/watch?v=qGHBcRcPQeI",
   quiz:[
     {q:"Applying a critical lens to a text means ___.", options:["finding the one correct interpretation","using a theoretical framework to ask specific questions of the text","proving the author had specific intentions","only citing theory in a bibliography"], answer:1},
     {q:"Feminist literary criticism examines ___.", options:["how texts shape or subvert gender roles","only gender in isolation from other factors","only texts with female protagonists","only texts by women"], answer:0},
     {q:"Marxist literary criticism examines ___.", options:["only communist literature","how texts reflect the economic base","only class conflict in plot","only economic statistics in fiction"], answer:1},
     {q:"Psychoanalytic literary criticism (Freud, Lacan) examines ___.", options:["the unconscious dimensions of texts","only mentally ill characters","only the author's biography","only obvious symbolism"], answer:0},
     {q:"The danger of applying theory mechanically is ___.", options:["the theory becomes irrelevant","theory always improves a reading","the text is reduced to an illustration of the theory","no danger exists in using theory"], answer:2}
   ]},
  {subject:"AdvancedFunctions", title:"The Cross Product in 3D", summary:"Students compute cross products of 3D vectors and apply them to find normals to planes, areas of parallelograms, and equations of planes.",
   resourceLabel:"Khan Academy", resourceUrl:"https://www.youtube.com/watch?v=pJzmiywagfY",
   quiz:[
     {q:"The cross product a × b produces ___.", options:["a vector perpendicular to both a and b","a scalar equal to |a||b|cosθ","the component-wise product of two vectors","the dot product of two vectors"], answer:0},
     {q:"For a=(1,0,0) and b=(0,1,0), a × b = ___.", options:["(−1,0,0)","(1,1,0)","(0,0,0)","(0,0,1) = k"], answer:3},
     {q:"The area of a parallelogram with sides a and b is ___.", options:["|a × b|","|a| × |b|","a · b","|a|² + |b|²"], answer:0},
     {q:"To find the equation of a plane through three points P₁, P₂, P₃, find ___.", options:["only the distance between the points","the sum of all coordinates","the cross product of P₁P₂ and P₁P₃","the midpoint of the three points"], answer:2},
     {q:"a × b = −(b × a) means ___.", options:["cross product is commutative","cross product is anti-commutative","cross product always gives zero","a × b and b × a are equal"], answer:1}
   ]},
  {subject:"Calculus", title:"Implicit Differentiation and Inverse Functions", summary:"Students apply implicit differentiation to curves defined implicitly, and differentiate inverse trigonometric and general inverse functions.",
   resourceLabel:"Khan Academy Calculus", resourceUrl:"https://www.youtube.com/watch?v=mSVrqKZDRF4",
   quiz:[
     {q:"Implicit differentiation is needed when ___.", options:["y cannot easily be isolated","the function is a polynomial","the function has no y variable","y is explicitly solved in terms of x"], answer:0},
     {q:"Differentiate x² + y² = 25 implicitly. dy/dx = ___.", options:["x/y","2x + 2y","−y/x","−x/y"], answer:3},
     {q:"d/dx[arcsin(x)] = ___.", options:["−1/√(1−x²)","1/√(1−x²)","1/cos(x)","cos(arcsin x)"], answer:1},
     {q:"d/dx[arctan(x)] = ___.", options:["1/cos²(x)","1/(1+x²)","−1/(1+x²)","sec²(x)"], answer:1},
     {q:"The general inverse function derivative rule: if g = f⁻¹, then g'(x) = ___.", options:["g(f'(x))","1/f'(g(x))","1/f(x)","f'(g(x))"], answer:1}
   ]},
  {subject:"Physics", title:"Simple Harmonic Motion", summary:"Students analyse SHM — period, frequency, amplitude, restoring force — and apply to springs and pendulums.",
   resourceLabel:"Crash Course Physics", resourceUrl:"https://www.youtube.com/watch?v=ZkLXIZoCo-o",
   quiz:[
     {q:"Simple harmonic motion occurs when ___.", options:["speed is constant","restoring force ∝ −displacement","the amplitude increases over time","the restoring force is constant"], answer:1},
     {q:"For a spring-mass system, the period is ___.", options:["T = 2π√(k/m)","T = 2π√(m/k)","T = 2π√k","T = 2πm/k"], answer:1},
     {q:"For a simple pendulum of length L, T = ___.", options:["T = 2πL/g","T = 2πg/L","T = 2π√(L/g)","T = 2π√(g/L)"], answer:2},
     {q:"The total mechanical energy in SHM is ___.", options:["constant: E = ½kA² (where A is amplitude)","only potential energy","only kinetic energy","zero at the equilibrium position"], answer:0},
     {q:"At maximum displacement (amplitude) in SHM, the velocity is ___ and acceleration is ___.  ", options:["maximum and zero","zero and zero","maximum and maximum","zero and maximum"], answer:3}
   ]},
]},
{day:19, label:"Day 19 — Thu", subjects:[
  {subject:"English", title:"Satire: Social Critique Through Comedy", summary:"Students analyse satire as a literary mode — examining targets, techniques (irony, parody, exaggeration), and the ethics and limits of satirical writing.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/watch?v=d1bE7LfNqlU",
   quiz:[
     {q:"Satire differs from simple comedy in that ___.", options:["satire is never funny","satire is always gentler than direct critique","satire uses humour to expose folly","satire has no political dimension"], answer:2},
     {q:"Horatian satire (after Horace) is characterised by ___.", options:["bitter, savage attack","no use of irony","no political targets","gentle, urbane wit"], answer:3},
     {q:"Juvenalian satire (after Juvenal) is characterised by ___.", options:["bitter, contemptuous indignation","praise of the satirical target","gentle humour","no exaggeration"], answer:0},
     {q:"Jonathan Swift's 'A Modest Proposal' uses ___.", options:["sustained irony","straightforward rhetorical argument","pure comedy without bite","direct emotional appeal"], answer:0},
     {q:"The ethics of satire involve ___.", options:["no ethical considerations","that any target is fair game","punching down vs. challenging power","only attacking powerful institutions"], answer:2}
   ]},
  {subject:"AdvancedFunctions", title:"Equations of Lines and Planes: Intersections and Distances", summary:"Students find intersections of lines and planes in 3D and calculate distances from points to lines and planes.",
   resourceLabel:"Khan Academy", resourceUrl:"https://www.youtube.com/watch?v=5AWob_z74Ks",
   quiz:[
     {q:"To find where a line intersects a plane, substitute the ___ into the plane equation.", options:["normal vector of the plane","coordinates of any point on the plane","direction vector of the line","parametric equations, solve for t"], answer:3},
     {q:"The distance from point P=(x₁,y₁,z₁) to plane Ax+By+Cz=D is ___.", options:["|Ax₁+By₁+Cz₁|","√(A²+B²+C²)","|AP₁|","|Ax₁+By₁+Cz₁−D|/√(A²+B²+C²)"], answer:3},
     {q:"Two lines in 3D can be ___.", options:["parallel, intersecting, or skew","always intersecting","always coplanar","only parallel or intersecting"], answer:0},
     {q:"To determine if two lines in 3D intersect, you ___.", options:["set parametric equations equal in all three coordinates and check if a consistent solution (value of both parameters) exists","set their position vectors equal and check for consistency","check if their direction vectors are equal","only check if they are parallel"], answer:1},
     {q:"The angle between two planes equals ___.", options:["the angle between a line and the plane","the angle between their normal vectors","90° always","the angle between their x-intercepts"], answer:1}
   ]},
  {subject:"Calculus", title:"Mean Value Theorem and Monotonicity", summary:"Students state and apply the Mean Value Theorem, Rolle's Theorem, and use them to analyse function behaviour.",
   resourceLabel:"Khan Academy Calculus", resourceUrl:"https://www.youtube.com/watch?v=mAul5vTAJSA",
   quiz:[
     {q:"Rolle's Theorem states: if f is continuous on [a,b], differentiable on (a,b), and f(a)=f(b), then ___.", options:["there exists c in (a,b) such that f'(c) = 1","f is constant on [a,b]","f has no local extrema","there exists c in (a,b) such that f'(c) = 0"], answer:3},
     {q:"The Mean Value Theorem states: if f is continuous on [a,b] and differentiable on (a,b), then ___.", options:["f'(c) = [f(b)−f(a)]/(b−a) for some c","f(a) = f(b) always","f achieves its maximum at a or b","f'(x) = 0 for some x"], answer:0},
     {q:"A geometric interpretation of the MVT: ___.", options:["the tangent at c parallels the secant","the function achieves both max and min","the function always has a zero","the tangent and secant are always perpendicular"], answer:0},
     {q:"If f'(x) > 0 for all x in (a,b), then the MVT implies ___.", options:["f(a) = f(b)","f has no extrema only","f is strictly increasing on (a,b)","f is constant"], answer:2},
     {q:"If f'(x) = g'(x) for all x, then ___.", options:["f(x) = g(x)","f(x) = g(x) + C for some constant C","f and g are both zero","no relationship can be inferred"], answer:1}
   ]},
  {subject:"Physics", title:"Wave Superposition and Interference", summary:"Students analyse the superposition of waves — constructive and destructive interference, standing waves, and resonance in strings and air columns.",
   resourceLabel:"Crash Course Physics", resourceUrl:"https://www.youtube.com/watch?v=7cDAYFTXq3E",
   quiz:[
     {q:"The principle of superposition states ___.", options:["only two waves can interfere","louder waves always dominate","waves cannot occupy the same space","overlapping waves sum displacements"], answer:3},
     {q:"Constructive interference occurs when ___.", options:["waves have different frequencies","waves are perpendicular","the path difference is a half-integer multiple of λ","waves arrive in phase (path difference = nλ for integer n)"], answer:3},
     {q:"Destructive interference occurs when ___.", options:["waves have equal amplitudes only","waves arrive out of phase (path difference = (n+½)λ)","waves travel in opposite directions","path difference = nλ"], answer:1},
     {q:"A standing wave on a string fixed at both ends has nodes at ___.", options:["antinodes only","only at the centre","the fixed endpoints","random positions along the string"], answer:2},
     {q:"The fundamental frequency of a string of length L, tension T, mass/length μ is ___.", options:["f₁ = L/(2√(T/μ))","f₁ = 2L√(μ/T)","f₁ = 1/(2L) × √(T/μ)","f₁ = √(TL/μ)"], answer:2}
   ]},
]},
{day:20, label:"Day 20 — Fri", subjects:[
  {subject:"English", title:"The Research Essay: Argument and Evidence at University Level", summary:"Students write and revise a fully documented research essay integrating primary texts, secondary criticism, and their own analysis.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/watch?v=vtIzMaLkCaM",
   quiz:[
     {q:"A literary research essay differs from a personal response in that ___.", options:["it is longer only","personal response is always better","it joins the critical conversation","it does not use primary texts"], answer:2},
     {q:"Selecting secondary sources for a literary research essay requires ___.", options:["only using Wikipedia and study guides","only the most recent criticism","peer-reviewed scholarly articles and books","any online source about the author"], answer:2},
     {q:"Synthesising sources in a research essay means ___.", options:["never agreeing with any source","weaving perspectives into your argument","quoting each source in order","only summarising each source separately"], answer:1},
     {q:"MLA citation requires ___.", options:["only in-text page numbers for everything","citations and a Works Cited page","only footnotes, no bibliography","only a bibliography, no in-text citation"], answer:1},
     {q:"Academic integrity in a research essay means ___.", options:["only quoting correctly","citing sources and original synthesis","only avoiding copy-paste","only citing sources you agree with"], answer:1}
   ]},
  {subject:"AdvancedFunctions", title:"Geometric Vectors: Applications to Physics and Engineering", summary:"Students apply 3D vector concepts to displacement, velocity, force equilibrium, and work problems.",
   resourceLabel:"Khan Academy", resourceUrl:"https://www.youtube.com/watch?v=ozwodzD5bte",
   quiz:[
     {q:"Resolving a force into components in 3D uses ___.", options:["trigonometry only","F = Fₓi + F_yj + F_zk","only the magnitude of the force","the dot product alone"], answer:1},
     {q:"For three forces to be in equilibrium, their vector sum must be ___.", options:["zero: F₁ + F₂ + F₃ = 0","equal to the largest force","non-zero","pointing downward"], answer:0},
     {q:"The scalar projection of a onto b is ___.", options:["a×b","|a||b|","a·b (the full dot product)","a·b̂ = a·b/|b|"], answer:3},
     {q:"The vector projection of a onto b is ___.", options:["a × b","(a·b̂)b̂ = (a·b/|b|²)b","a·b/|b|²","|a|cosθ"], answer:1},
     {q:"Work done by a force F over displacement d is ___.", options:["F + d","|F||d|","W = F · d = |F||d|cosθ","F × d (cross product — this gives a vector, not work)"], answer:2}
   ]},
  {subject:"Calculus", title:"Integration by Substitution", summary:"Students apply the substitution rule (u-substitution) to evaluate indefinite and definite integrals of composite functions.",
   resourceLabel:"Khan Academy Calculus", resourceUrl:"https://www.youtube.com/watch?v=-9M9P7xNDH4",
   quiz:[
     {q:"The substitution rule reverses ___.", options:["the quotient rule","the chain rule","the power rule","the product rule"], answer:1},
     {q:"∫2x(x²+1)⁵ dx: let u = x²+1, du = 2x dx. The integral becomes ___.", options:["∫u⁵ 2x dx","∫2xu⁵ du","∫(x²+1)⁵ du","∫u⁵ du = u⁶/6 + C = (x²+1)⁶/6 + C"], answer:3},
     {q:"∫sin(3x) dx: let u = 3x, du = 3 dx. The integral = ___.", options:["−cos(3x)/3 + C","−cos(3x) + C","cos(3x)/3 + C","−3cos(3x) + C"], answer:0},
     {q:"For a definite integral with substitution, you must ___.", options:["change limits to u-values","never use substitution in definite integrals","keep the same limits of integration","always change back to x before evaluating"], answer:0},
     {q:"∫[0 to 1] x·e^(x²) dx: let u = x², du = 2x dx. Limits: u(0)=0, u(1)=1. Result:", options:["e/2","e−1","(e−1)","∫[0 to 1] e^u du/2 = [e^u/2]₀¹ = (e−1)/2"], answer:3}
   ]},
  {subject:"Physics", title:"Optics: Reflection and Refraction", summary:"Students apply the law of reflection and Snell's Law to mirrors, lenses, and fibre optics; analyse total internal reflection.",
   resourceLabel:"Crash Course Physics", resourceUrl:"https://www.youtube.com/watch?v=_dBmNF_XBTU",
   quiz:[
     {q:"The law of reflection states ___.", options:["the angle of incidence and refraction are equal","light always reflects at 45°","reflected rays are always horizontal","incidence angle equals reflection angle"], answer:3},
     {q:"Snell's Law of refraction is ___.", options:["n₁sinθ₁ = n₂sinθ₂","n₁θ₁ = n₂θ₂","n₁cosθ₁ = n₂cosθ₂","n₁/sinθ₁ = n₂/sinθ₂"], answer:0},
     {q:"Total internal reflection occurs when ___.", options:["any light passes from air to glass","light passes from glass to air at any angle","n₁ < n₂","refraction hits 90°, the critical angle"], answer:3},
     {q:"A converging (convex) lens ___.", options:["converges rays to a focal point","only works for objects at infinity","diverges parallel rays","creates only virtual images"], answer:0},
     {q:"Optical fibre works by ___.", options:["total internal reflection","total reflection from metal coatings","only working in vacuum","absorption of light"], answer:0}
   ]},
]},
{day:21, label:"Day 21 — Mon", subjects:[
  {subject:"English", title:"The Novel as Social Document: Realism and Its Discontents", summary:"Students examine realist novels and their sociological dimension — how fiction can document social reality while remaining art.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/watch?v=qGHBcRcPQeI",
   quiz:[
     {q:"Nineteenth-century realism in the novel aimed to ___.", options:["represent society as it actually is","create pure fantasy worlds","avoid representing working-class life","focus only on aristocratic characters"], answer:0},
     {q:"The sociological reading of a novel examines ___.", options:["only the author's biography","only plot and character","how the novel reflects its social era","only style and form"], answer:2},
     {q:"A 'condition of England' novel (like those by Dickens or Gaskell) characteristically ___.", options:["only follows middle-class characters","dramatises a contemporary social problem","avoids contemporary social problems","romanticises the past"], answer:1},
     {q:"The danger of reading a novel only as a social document is ___.", options:["it always misidentifies the social context","it is the correct approach","reducing it to data, ignoring artistry","it makes the novel more interesting"], answer:2},
     {q:"Contemporary fiction as social document includes ___.", options:["only 'issues novels' without literary merit","no claim to documentary accuracy","only literary fiction set in the past","novels on climate and social justice"], answer:3}
   ]},
  {subject:"AdvancedFunctions", title:"Vectors: Applications to Navigation and Problem Solving", summary:"Students apply 3D vector techniques to navigation, structural problems, and multi-step applied problems.",
   resourceLabel:"Khan Academy", resourceUrl:"https://www.youtube.com/watch?v=ml4NSzCQobk",
   quiz:[
     {q:"A boat travels at 20 km/h in a river with current 5 km/h perpendicular. Its actual speed is ___.", options:["15 km/h","√(20² + 5²) = √425 ≈ 20.6 km/h","25 km/h","10 km/h"], answer:1},
     {q:"A plane heads north at 800 km/h; wind blows east at 100 km/h. The resultant speed is ___.", options:["700 km/h","900 km/h","800 + 100 = 900 km/h (this adds speeds, not vectors)","√(800² + 100²) = √650000 ≈ 806 km/h"], answer:3},
     {q:"Forces of 30 N north and 40 N east act on an object. The resultant force is ___.", options:["50 N due northeast","50 N at arctan(40/30) N of E","70 N","10 N"], answer:1},
     {q:"To find the angle between two 3D vectors a = (1,2,2) and b = (2,1,−2):", options:["θ = 30°","θ = 60°","θ = 45°","θ = 90° (perpendicular)"], answer:3},
     {q:"A force of (3, 4, 0) N acts over displacement (1, 1, 5) m. Work done = ___.", options:["3+4+1+1+5 = 14 J","(3+4+0)(1+1+5) = 49 J","√(3²+4²+0²) J","3·1 + 4·1 + 0·5 = 7 J"], answer:3}
   ]},
  {subject:"Calculus", title:"Integration by Parts", summary:"Students apply the integration by parts formula to products of functions, including repeated application and tabular method.",
   resourceLabel:"Khan Academy Calculus", resourceUrl:"https://www.youtube.com/watch?v=2I-_SV8cwsw",
   quiz:[
     {q:"Integration by parts: ∫u dv = ___.", options:["uv − ∫u dv","∫u dx + ∫dv","uv − ∫v du","u dv − v du"], answer:2},
     {q:"To integrate ∫x·eˣ dx, choose u = x, dv = eˣ dx. Then du = dx, v = eˣ. Result:", options:["x·eˣ − eˣ + C = eˣ(x−1) + C","eˣ(x+1) + C","x·eˣ + eˣ + C","x·eˣ + C"], answer:0},
     {q:"For ∫ln(x) dx, choose u = ln(x), dv = dx. Then du = 1/x dx, v = x. Result:", options:["x·ln(x) − x + C","ln(x)/x + C","ln(x) + C","x/ln(x) + C"], answer:0},
     {q:"∫x²·sin(x) dx requires ___.", options:["no special technique","two rounds of integration by parts","one application of parts","u-substitution only"], answer:1},
     {q:"The mnemonic LIATE suggests choosing u as ___.", options:["the first in LIATE order","the last function in the product","the exponential always","the function that differentiates to zero"], answer:0}
   ]},
  {subject:"Physics", title:"The Photoelectric Effect and Wave-Particle Duality", summary:"Students examine the photoelectric effect, photon model of light, and the evidence for wave-particle duality.",
   resourceLabel:"Crash Course Physics", resourceUrl:"https://www.youtube.com/watch?v=kcSYV8bZhjc",
   quiz:[
     {q:"The photoelectric effect is the emission of electrons from a metal surface when ___.", options:["a current is applied to the metal","the metal is heated sufficiently","the metal is cooled to absolute zero","light of sufficient frequency illuminates the metal"], answer:3},
     {q:"Classical wave theory failed to explain the photoelectric effect because ___.", options:["it correctly predicted everything","any frequency could eject electrons","it predicted no electrons would be emitted","it predicted only red light would work"], answer:1},
     {q:"Einstein's explanation of the photoelectric effect (1905) proposed ___.", options:["light is purely a particle with no wave properties","the metal surface is the key factor","light energy comes in discrete packets (photons) of energy E = hf","the current from the battery ejects electrons"], answer:2},
     {q:"De Broglie's hypothesis proposed that matter also has wave properties: λ = ___.", options:["h × mv","h/(mv) = h/p","h/f","mv/h"], answer:1},
     {q:"Wave-particle duality means ___.", options:["only light can be a wave","quantum objects are neither waves nor particles","only electrons can be particles","objects act as waves or particles"], answer:3}
   ]},
]},
{day:22, label:"Day 22 — Tue", subjects:[
  {subject:"English", title:"Short Fiction Masterworks: Structure, Voice, and Compression", summary:"Students study canonical short stories, examining how compressed form demands particular mastery of voice, structure, epiphany, and economy of language.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/watch?v=dtRCMONW8bQ",
   quiz:[
     {q:"The short story differs from the novel in that ___.", options:["it demands absolute economy","it is always easier to write","it can never achieve the depth of a novel","it has no character development"], answer:0},
     {q:"The 'epiphany' in Joyce's short fiction (from 'Dubliners') refers to ___.", options:["a moment of sudden insight or revelation","a surprise plot twist","a religious experience only","the story's happy ending"], answer:0},
     {q:"Point of view in a short story is especially important because ___.", options:["point of view has no relation to meaning","third person is always better","first person is always best","limited space makes voice vital"], answer:3},
     {q:"Chekhov's famous 'gun' principle states ___.", options:["every story needs violence","stories should be realistic only","a gun shown early must be fired later","guns are important in Russian fiction"], answer:2},
     {q:"Compression in short fiction achieves ___.", options:["only brevity without depth","less than the novel in all respects","nothing that a longer story could not do better","a different kind of intensity"], answer:3}
   ]},
  {subject:"AdvancedFunctions", title:"Counting Principles and Permutations", summary:"Students apply the fundamental counting principle, permutations (with and without repetition), and circular permutations to combinatorics problems.",
   resourceLabel:"Khan Academy", resourceUrl:"https://www.youtube.com/watch?v=XqQTXW7XfYA",
   quiz:[
     {q:"The fundamental counting principle: if event A can occur in m ways and event B in n ways, then A then B can occur in ___.", options:["m × n ways (multiplication principle)","m − n ways","m! ways","m + n ways (addition applies when events are mutually exclusive alternatives)"], answer:0},
     {q:"The number of permutations of n distinct objects taken r at a time is ___.", options:["n!","nCr = n!/(r!(n−r)!)","n!/r!","n!/(n−r)!... = nPr"], answer:3},
     {q:"How many 4-digit PINs have no repeated digits?", options:["4! = 24","10 × 9 × 8 × 7 = 5040 (=10P4)","10 × 9 × 8 = 720","10⁴ = 10000"], answer:1},
     {q:"In how many ways can 5 people sit at a round table?", options:["5! = 120","5","(5−1)! = 4! = 24","5!/5 = 24"], answer:2},
     {q:"If 3 of 8 books must always be together, the number of arrangements on a shelf is ___.", options:["3! × 6!","8! arrangements","3! × 8!","6! only"], answer:0}
   ]},
  {subject:"Calculus", title:"Volumes of Solids of Revolution: Advanced", summary:"Students compute volumes using disc/washer and shell methods, and apply the methods to multi-region problems.",
   resourceLabel:"Khan Academy Calculus", resourceUrl:"https://www.youtube.com/watch?v=EFkEnCYdVAU",
   quiz:[
     {q:"The washer method for a solid between y=f(x) and y=g(x) (f≥g) rotated about x-axis gives ___.", options:["V = π∫{[f(x)]² − [g(x)]²} dx","V = 2π∫x[f(x)−g(x)] dx","V = π∫[f(x)+g(x)] dx","V = π∫[f(x)−g(x)]² dx"], answer:0},
     {q:"Find the volume when the region between y=x and y=x² (0≤x≤1) is rotated about the x-axis.", options:["V = π/6","V = π/15","V = 2π/15","V = π/3"], answer:2},
     {q:"The shell method integrates ___ when rotating about the y-axis.", options:["horizontal strips of width dy","circular discs perpendicular to y","the radius squared","vertical shells: V = 2π∫x·f(x) dx from a to b"], answer:3},
     {q:"Choosing between disc/washer and shell methods: prefer shells when ___.", options:["solving for x in terms of y would be difficult","only for linear functions","always preferring shells","the function has no closed form"], answer:0},
     {q:"The volume of a sphere of radius r by discs: V = π∫[-r to r](r²−x²) dx = ___.", options:["4πr³/3","2πr³","πr³","4πr²/3"], answer:0}
   ]},
  {subject:"Physics", title:"Atomic Structure and Quantum Numbers", summary:"Students examine the Bohr model, quantum mechanical model, and electron configurations using quantum numbers.",
   resourceLabel:"Crash Course Physics", resourceUrl:"https://www.youtube.com/watch?v=Ewf6RuLlSvc",
   quiz:[
     {q:"The Bohr model of the hydrogen atom correctly predicted ___.", options:["the Zeeman effect","the spectra of all elements","the 3D shape of orbitals","hydrogen's discrete emission spectrum"], answer:3},
     {q:"The principal quantum number n determines ___.", options:["the energy level and size of the orbital","the shape of the orbital","the magnetic orientation of the orbital","the spin of the electron"], answer:0},
     {q:"The four quantum numbers (n, l, mₗ, mₛ) together specify ___.", options:["a unique quantum state per electron","only the energy of the electron","only the spin orientation","only the orbital shape"], answer:0},
     {q:"The Heisenberg Uncertainty Principle states ___.", options:["measurement has no effect on quantum systems","electrons move in defined circular orbits","Δx × Δp ≥ ℏ/2","quantum mechanics is only approximate"], answer:2},
     {q:"Electron configuration of carbon (Z=6) following Aufbau principle is ___.", options:["1s²2p⁴","1s²2s¹2p³","1s²2s²2p²","1s¹2s²2p³"], answer:2}
   ]},
]},
{day:23, label:"Day 23 — Wed", subjects:[
  {subject:"English", title:"Documentary and Non-Fiction: Truth, Form, and Ethics", summary:"Students examine documentary film and literary non-fiction (creative non-fiction, journalism) — exploring how non-fiction makes arguments and ethical obligations to truth.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/watch?v=2HqT7QbVCnc",
   quiz:[
     {q:"Documentary film differs from fiction film in that ___.", options:["documentary has no narrative structure","documentary is always objective","documentary claims a relationship to actual events and people","documentary uses no cinematic technique"], answer:2},
     {q:"Rhetorical strategies in documentary include ___.", options:["only verbal argument","footage order, music, and narration","only factual presentation","no rhetorical strategies"], answer:1},
     {q:"Creative non-fiction (e.g., literary journalism, memoir, personal essay) ___.", options:["should avoid literary techniques","has no responsibility to truth","is always more subjective than journalism","uses fiction techniques for facts"], answer:3},
     {q:"The ethics of documentary representation include ___.", options:["no issue if filming in public spaces","no ethical obligations since subjects consented","only legal considerations","obligations of consent and fairness"], answer:3},
     {q:"Analysing a documentary as a text means ___.", options:["only checking factual accuracy","only watching without analysis","examining its rhetoric and evidence","accepting it as a neutral truth document"], answer:2}
   ]},
  {subject:"AdvancedFunctions", title:"Combinations and the Binomial Theorem", summary:"Students calculate combinations, apply Pascal's triangle, and expand binomials using the Binomial Theorem.",
   resourceLabel:"Khan Academy", resourceUrl:"https://www.youtube.com/watch?v=Eu2oYKiPxu0",
   quiz:[
     {q:"The number of combinations of n objects taken r at a time is ___.", options:["n!/(n−r)!","n!/r!","n!","C(n,r) = n!/(r!(n−r)!)"], answer:3},
     {q:"How many ways can a committee of 3 be chosen from 10 people?", options:["10!/3! = 604800","10P3 = 720","10 × 3 = 30","C(10,3) = 10!/(3!7!) = 120"], answer:3},
     {q:"The Binomial Theorem states (a+b)ⁿ = ___.", options:["∑[k=0 to n] C(n,k) aⁿ⁻ᵏ bᵏ","aⁿ + bⁿ only","∑ C(n,k) aᵏbⁿ⁻ᵏ","n·aⁿ⁻¹b + aⁿ"], answer:0},
     {q:"The term with b³ in (2x + 3)⁵ is ___.", options:["C(5,3)(2x)²(3)³ = 1080x²","C(5,3)(2x)³(3)²","C(5,3)(2x)²(3)³ = 10 × 4x² × 27 = 1080x²","C(5,2)(2x)³(3)²"], answer:2},
     {q:"Pascal's triangle has the property that ___.", options:["C(n,r) = C(n−1,r)","C(n,r) = C(n,r−1) + C(n,r+1)","each entry is the sum of all entries above","C(n,r) = C(n−1,r−1) + C(n−1,r)"], answer:3}
   ]},
  {subject:"Calculus", title:"Numerical Integration: Riemann Sums and the Trapezoid Rule", summary:"Students approximate definite integrals using Riemann sums, the Trapezoid Rule, and Simpson's Rule.",
   resourceLabel:"Khan Academy Calculus", resourceUrl:"https://www.youtube.com/watch?v=YTKQswb60Pw",
   quiz:[
     {q:"A Riemann sum approximates a definite integral by ___.", options:["differentiating at sample points","only using the left endpoint always","summing the areas of rectangles","using the antiderivative"], answer:2},
     {q:"The Trapezoid Rule approximates ∫f dx using ___.", options:["only left-endpoint rectangles","the average of f(a) and f(b) only","only the area of one trapezoid","trapezoids instead of rectangles"], answer:3},
     {q:"Simpson's Rule (n even) is ___.", options:["the same as the trapezoid rule","only used for linear functions","(h/3)[f(x₀)+4f(x₁)+2f(x₂)+...+f(xₙ)]","only the midpoint rule"], answer:2},
     {q:"Numerical integration is necessary when ___.", options:["there's no closed-form antiderivative","only for physics problems","the function is always integrable","you cannot use the FTC"], answer:0},
     {q:"As the number of subintervals n → ∞, all Riemann sum approximations ___.", options:["converge to the exact integral value","approach different limits","remain the same","diverge"], answer:0}
   ]},
  {subject:"Physics", title:"Nuclear Reactions: Fission, Fusion, and Radioactive Decay", summary:"Students analyse nuclear reactions, calculate binding energy per nucleon, and apply decay equations.",
   resourceLabel:"Crash Course Physics", resourceUrl:"https://www.youtube.com/watch?v=nRmBsxBpTjs",
   quiz:[
     {q:"Radioactive decay follows ___.", options:["a linear decrease in activity","constant activity indefinitely","an exponential law: N(t) = N₀e^(−λt)","a quadratic decay law"], answer:2},
     {q:"Half-life T½ is related to decay constant λ by ___.", options:["T½ = λ","T½ = ln2/λ = 0.693/λ","T½ = 1/λ","T½ = e^λ"], answer:1},
     {q:"Binding energy per nucleon peaks at ___.", options:["hydrogen-1 (lightest)","iron-56, where fusion meets fission","uranium-238 (heaviest stable nucleus)","carbon-12 (organic life basis)"], answer:1},
     {q:"Carbon-14 dating works because ___.", options:["C-14 is created only in labs","C-14 is the most common carbon isotope","C-14 decays at a known rate, T½≈5730yr","C-14 is stable indefinitely"], answer:2},
     {q:"The Q-value of a nuclear reaction is ___.", options:["the quality of the nuclear fuel","the charge of the nucleus","the quantity of material used","the energy released: Q = Δmass × c²"], answer:3}
   ]},
]},
{day:24, label:"Day 24 — Thu", subjects:[
  {subject:"English", title:"Contemporary Drama: Stagecraft and Text", summary:"Students examine a contemporary play, analysing the relationship between the written text and its realisation in performance.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/watch?v=W3MJj5AjAMc",
   quiz:[
     {q:"A play script is ___.", options:["always the same in any production","less important than the director's vision","the complete work of art in itself","a blueprint for performance"], answer:3},
     {q:"Stage directions in a contemporary play ___.", options:["are always followed literally","may be poetic, ambiguous, or minimal","tell audiences what to think","are always ignored by directors"], answer:1},
     {q:"Theatre's relationship to contemporary politics includes ___.", options:["avoidance of political content","documentary theatre only","only historical political subjects","verbatim, protest, and other forms"], answer:3},
     {q:"Analysing a contemporary play without seeing it in production requires ___.", options:["imagining a specific production as if it were the only one","admitting analysis is impossible without performance","only reading the dialogue as prose","imaginative performance reading"], answer:3},
     {q:"The most important question when analysing a scene in a contemporary play is ___.", options:["what happens in the plot","what each character wants in the scene","how many characters appear","what time period is the play set in"], answer:1}
   ]},
  {subject:"AdvancedFunctions", title:"Probability Distributions: Binomial and Geometric", summary:"Students work with discrete probability distributions — binomial and geometric — applying formulas and interpreting results.",
   resourceLabel:"Khan Academy", resourceUrl:"https://www.youtube.com/watch?v=J8jNoF-K8Z8",
   quiz:[
     {q:"The binomial distribution applies when ___.", options:["only one trial is performed","probability changes each trial","n trials, constant probability p","trials have more than two outcomes"], answer:2},
     {q:"P(X=k) for a binomial distribution is ___.", options:["C(n,k) × pᵏ × (1−p)^n","C(n,k) × pᵏ × (1−p)^(n−k)","p^k × (1-p)^(n-k)","n × p × k"], answer:1},
     {q:"For a binomial random variable X ~ B(n,p), E(X) = ___.", options:["np(1−p)","n/p","np (expected successes in n trials)","p/n"], answer:2},
     {q:"The geometric distribution models ___.", options:["trials until the first success","the number of successes in n trials","the probability of exactly one success","only continuous random variables"], answer:0},
     {q:"A quality control check has 5% defective rate. Find P(exactly 2 defective in 20 items).", options:["C(20,2)(0.05)²","(0.05)² × 20","2/20 = 0.10","C(20,2)(0.05)²(0.95)¹⁸ ≈ 0.189"], answer:3}
   ]},
  {subject:"Calculus", title:"Differential Equations: Growth, Decay, and Newton's Law", summary:"Students solve separable ODEs applied to exponential growth, radioactive decay, and Newton's Law of Cooling.",
   resourceLabel:"Khan Academy Calculus", resourceUrl:"https://www.youtube.com/watch?v=H0VEL9TFjqw",
   quiz:[
     {q:"The general solution of dP/dt = kP is ___.", options:["P(t) = ke^(P₀t)","P(t) = P₀ + kt","P(t) = P₀e^(kt)","P(t) = P₀kt"], answer:2},
     {q:"A culture of 1000 bacteria doubles in 3 hours. After 9 hours:", options:["6000","2000","3000","8000 (doubles 3 times)"], answer:3},
     {q:"Radioactive decay: dN/dt = −λN. Given N₀ = 400 and T½ = 5 years, after 10 years N = ___.", options:["400e^(−10)","400 − 2λ","200","400 × (1/2)² = 100 (two half-lives)"], answer:3},
     {q:"Newton's Law of Cooling: T(t) = T_env + (T₀ − T_env)e^(−kt). A 90°C coffee in a 20°C room cools to 70°C in 10 min. After 30 more minutes T ≈ ___.", options:["≈ 38°C","50°C","60°C","45°C"], answer:0},
     {q:"A differential equation is separable if ___.", options:["its solution is always exponential","it can be written as dy/g(y) = f(x) dx","it has constant coefficients","it involves only one variable"], answer:1}
   ]},
  {subject:"Physics", title:"Modern Physics: Quantum Mechanics and the Standard Model", summary:"Students examine the probabilistic nature of quantum mechanics, wave functions, and an overview of the Standard Model.",
   resourceLabel:"Crash Course Physics", resourceUrl:"https://www.youtube.com/watch?v=p7bzE1E5PMY",
   quiz:[
     {q:"The wave function ψ(x,t) in quantum mechanics gives ___.", options:["the exact position of the particle","the energy of the particle directly","the probability amplitude","the actual path of the particle"], answer:2},
     {q:"The Schrödinger equation is ___.", options:["the fundamental equation of quantum mechanics","only applicable to classical waves","a statement of conservation of energy","only for relativistic particles"], answer:0},
     {q:"Quantum tunnelling allows ___.", options:["particles to cross forbidden barriers","only photons to pass through barriers","energy conservation to be violated","particles to exceed the speed of light"], answer:0},
     {q:"The Standard Model classifies matter as composed of ___.", options:["photons and electrons only","protons and neutrons only","atoms and molecules only","quarks and leptons"], answer:3},
     {q:"The unresolved problems in the Standard Model include ___.", options:["no unresolved problems","only cosmological questions","only mathematical issues","gaps in gravity and dark matter theory"], answer:3}
   ]},
]},
{day:25, label:"Day 25 — Fri", subjects:[
  {subject:"English", title:"Research Essay Workshop: Drafting and Peer Review", summary:"Students workshop research essay drafts in a peer-review setting, applying structured feedback protocols and revising for argument, evidence, and style.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/watch?v=8eB7SSNC5ys",
   quiz:[
     {q:"Peer review is most valuable when ___.", options:["reviewers respond as genuine readers","reviewers focus only on grammar","reviewers are lenient to encourage the writer","reviewers only praise the essay"], answer:0},
     {q:"The most important question to ask about a research essay draft is ___.", options:["does the evidence support each claim?","are there enough quotations?","is the essay long enough?","is the Works Cited formatted correctly?"], answer:0},
     {q:"Revising an essay is different from editing in that ___.", options:["editing is more important","revising is only fixing grammar","they are the same process","revising rethinks the argument itself"], answer:3},
     {q:"When evidence does not support your claim, the correct response is ___.", options:["ignore the problem","delete the evidence","misrepresent the evidence to fit","revise the claim or the evidence"], answer:3},
     {q:"Academic voice in a research essay is characterised by ___.", options:["only long, complex sentences","avoiding the first person always","only formal vocabulary","precision, economy, and analytical clarity"], answer:3}
   ]},
  {subject:"AdvancedFunctions", title:"Probability: Conditional Probability and Independence", summary:"Students apply conditional probability, Bayes' Theorem, and independence to complex probability problems.",
   resourceLabel:"Khan Academy", resourceUrl:"https://www.youtube.com/watch?v=H02B3aMNKzE",
   quiz:[
     {q:"Conditional probability P(A|B) = ___.", options:["P(A) + P(B)","P(A∩B)/P(B)","P(A) × P(B)","P(A)/P(B)"], answer:1},
     {q:"Events A and B are independent if and only if ___.", options:["P(A|B) = P(A)","P(A∩B) = 0","P(A) = P(B)","P(A) + P(B) = 1"], answer:0},
     {q:"Bayes' Theorem: P(A|B) = ___.", options:["P(B|A)×P(A)×P(B)","P(B|A)/P(A)","P(A|B) = P(A)P(B)","P(B|A)×P(A) / P(B)"], answer:3},
     {q:"A medical test has 99% sensitivity (P(+|disease)) and 95% specificity (P(−|no disease)). Prevalence = 1%. P(disease | positive test) ≈ ___.", options:["≈ 16.7% (via Bayes' theorem)","≈ 99%","≈ 50%","≈ 5%"], answer:0},
     {q:"The multiplication rule for conditional probability: P(A∩B) = ___.", options:["P(A)×P(B) always","P(A)×P(B|A) = P(B)×P(A|B)","P(A|B) − P(B)","P(A) + P(B) − P(A∪B)"], answer:1}
   ]},
  {subject:"Calculus", title:"Arc Length and Surface Area", summary:"Students calculate arc lengths of curves and surface areas of solids of revolution using integration.",
   resourceLabel:"Khan Academy Calculus", resourceUrl:"https://www.youtube.com/watch?v=PwmqebSqc_s",
   quiz:[
     {q:"The arc length of y = f(x) from a to b is ___.", options:["∫[a to b]√(1+[f(x)]²) dx","∫[a to b]f(x) dx","∫[a to b]√(1+[f'(x)]²) dx","∫[a to b](1+f(x)) dx"], answer:2},
     {q:"Find the arc length of y = x³/² from x=0 to x=4.", options:["∫√(1+x³) dx","4³/² = 8","∫[0,4]√(1+9x/4) dx","4 × √(1+9) = 4√10"], answer:2},
     {q:"Surface area of y=f(x) rotated about x-axis from a to b is ___.", options:["π∫[f(x)]² dx (this is volume by discs)","2π∫f(x)√(1+[f'(x)]²) dx","2π∫f(x) dx","π∫f(x)√(1+[f'(x)]²) dx"], answer:1},
     {q:"These formulas require that f(x) is ___.", options:["continuously differentiable on [a,b]","only continuous","only integrable","always positive"], answer:0},
     {q:"For a circle of radius r (parametrically x=rcosθ, y=rsinθ), the arc length (circumference) formula gives ___.", options:["2πr² (this is area)","πr","πr²","2πr"], answer:3}
   ]},
  {subject:"Physics", title:"Medical and Applied Physics", summary:"Students see how physics principles apply to medicine — X-rays, MRI, PET scans, ultrasound, and radiation therapy.",
   resourceLabel:"Crash Course Physics", resourceUrl:"https://www.youtube.com/watch?v=cMJpFjmJZ9s",
   quiz:[
     {q:"X-rays penetrate soft tissue but are absorbed by bone because ___.", options:["X-rays cannot travel through any material","X-rays are repelled by calcium","bone is harder than soft tissue","bone is denser and absorbs X-rays more"], answer:3},
     {q:"MRI (Magnetic Resonance Imaging) uses ___.", options:["radioactive tracers","X-rays with computer processing","the magnetism of hydrogen protons","ultrasound at very high frequencies"], answer:2},
     {q:"PET (Positron Emission Tomography) works by ___.", options:["measuring sound waves inside the body","using a magnetic field to image organs","detecting gamma rays from positron-electron annihilation","using external X-ray sources"], answer:2},
     {q:"Ultrasound imaging uses ___.", options:["gamma radiation","visible light","high-frequency sound waves (1–20 MHz)","infrared radiation"], answer:2},
     {q:"Radiation therapy targets cancer because ___.", options:["normal cells cannot be harmed by radiation","radiation has no side effects","radiation damages DNA in dividing cells","only cancer cells absorb radiation"], answer:2}
   ]},
]},
{day:26, label:"Day 26 — Mon", subjects:[
  {subject:"English", title:"Oral Communication: Seminar and Academic Discussion", summary:"Students prepare for and participate in a formal Socratic seminar, developing skills in academic discussion, active listening, and building on others' ideas.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/watch?v=bPkHcTk55Vc",
   quiz:[
     {q:"A Socratic seminar is characterised by ___.", options:["competitive debate with winners","open, collaborative inquiry","the teacher asking all the questions","only one student speaking at a time"], answer:1},
     {q:"Effective academic discussion requires ___.", options:["never asking questions during someone's turn","active listening","talking as much as possible","always agreeing with the previous speaker"], answer:1},
     {q:"To advance a seminar discussion, a student should ___.", options:["only repeat what they prepared","introduce a new topic unrelated to the discussion","build on, extend, or challenge ideas","ask for more clarification"], answer:2},
     {q:"The purpose of requiring textual evidence in a seminar is ___.", options:["to penalise students who didn't prepare","to ground claims in specific textual detail","to fill time in the discussion","to show you did the reading"], answer:1},
     {q:"The highest level of seminar participation involves ___.", options:["asking a question opening new thinking","speaking longest","making the most points","never asking questions"], answer:0}
   ]},
  {subject:"AdvancedFunctions", title:"Advanced Functions: Comprehensive Review", summary:"Students review the full MHF4U course with examination-level practice problems spanning all strands.",
   resourceLabel:"Khan Academy", resourceUrl:"https://www.youtube.com/watch?v=MKQR_acrFOA",
   quiz:[
     {q:"A function f has an inverse f⁻¹ if and only if ___.", options:["f is continuous","f is differentiable","f is defined for all x","f is one-to-one"], answer:3},
     {q:"Solve: log₂(x+1) − log₂(x−1) = 3.", options:["x = 9","x = 9/7","x = 3","x = 7"], answer:1},
     {q:"The dot product of a = (1,−2,3) and b = (4,1,−2) is ___.", options:["4 + 2 − 6 = 0","1×4−2×1+3×2 = 8","4−2+6 = 8... no: 1×4+(−2)×1+3×(−2) = 4−2−6 = −4","−4 (1×4 + (−2)×1 + 3×(−2) = 4−2−6 = −4)"], answer:3},
     {q:"The general term of the expansion (3x−2)⁶ containing x⁴ is ___.", options:["C(6,4)(3x)⁴(−2)²","C(6,2)(3x)⁴(−2)² = 15 × 81x⁴ × 4 = 4860x⁴","C(6,4)(3x)⁴(−2)² = 15 × 81x⁴ × 4 = 4860x⁴","C(6,2)(3x)⁴(2)² = 4860x⁴"], answer:0},
     {q:"In how many ways can the letters of MISSISSIPPI be arranged?", options:["11!/4!","11!","11!/4!4!","11!/4!4!2! = 34650"], answer:3}
   ]},
  {subject:"Calculus", title:"Calculus: Comprehensive Review", summary:"Students review the full calculus course with examination-level problems on limits, derivatives, and integrals.",
   resourceLabel:"Khan Academy Calculus", resourceUrl:"https://www.youtube.com/watch?v=HEH_oKNLgUU",
   quiz:[
     {q:"Find the derivative of f(x) = x²·sin(3x).", options:["f'(x) = x²·3cos(3x)","f'(x) = 2x sin(3x) + 3x²cos(3x)","f'(x) = 2x·sin(3x) + x²·cos(3x)","f'(x) = 2x·cos(3x)"], answer:1},
     {q:"A box with square base (side x) and no top has surface area 108 cm². Maximise volume. V = x²h, 4xh+x² = 108 → h = (108−x²)/(4x). V(x) = ___.", options:["V_max = 108 cm³ at x = 6","V = x³/4","V = 108x","V = 27x²"], answer:0},
     {q:"∫[1 to e] (ln x)/x dx = ___.", options:["e","1","ln(e)/e = 1/e","= 1/2 (via u=ln x substitution)"], answer:3},
     {q:"The area enclosed by y = x² and y = 2x is ___.", options:["8/3","2/3","4/3","∫[0 to 2](2x−x²) dx = [x²−x³/3]₀² = 4−8/3 = 4/3"], answer:2},
     {q:"Solve: dy/dx = x/y; y(0) = 2.", options:["y = xe^x + 2","y = √(x²+4)","y = 2e^(x²/2)","y = x²/2 + 2"], answer:1}
   ]},
  {subject:"Physics", title:"Physics: Comprehensive Review", summary:"Students review the full SPH4U course with examination-level multi-concept problems.",
   resourceLabel:"Crash Course Physics", resourceUrl:"https://www.youtube.com/watch?v=pGj9isFr21U",
   quiz:[
     {q:"A 1500 kg car accelerates from 0 to 25 m/s in 10 s up a 10° incline (μₖ = 0.1). Net force required:", options:["F_net ≈ 7754 N","F = mg sinθ only","F = 1500 × 2.5 = 3750 N","F = ma only"], answer:0},
     {q:"A spring (k=400 N/m) is compressed 0.2 m and launches a 0.1 kg ball. Speed at launch:", options:["v = 0.2 m/s","v = √(kx) = √80 ≈ 8.9 m/s","v = kx/m = 0.2×400/0.1 = 800 m/s","v ≈ 12.6 m/s (energy conservation)"], answer:3},
     {q:"A charge q₁ = +2μC is 0.3 m from q₂ = −3μC. The electrostatic force magnitude:", options:["F = 0.06 N","F = 0.006 N","F = 0.6 N (attractive)","F = 6 N"], answer:2},
     {q:"A proton (m=1.67×10⁻²⁷ kg, q=1.6×10⁻¹⁹ C) enters a 0.5 T field at 10⁶ m/s perpendicular. Radius of circular path:", options:["r = 1 m","r = 0.1 m","r ≈ 2.1 cm","r = mv/q = 10.4 m"], answer:2},
     {q:"Muons created in upper atmosphere have T½ = 2.2 μs. Moving at 0.98c, the lab-frame half-life is ___.", options:["4.4 μs","1.1 μs","lab T½ ≈ 11 μs (γ≈5)","2.2 μs unchanged"], answer:2}
   ]},
]},
{day:27, label:"Day 27 — Tue", subjects:[
  {subject:"English", title:"Writing Workshop: Style, Voice, and the Sentence", summary:"Students examine prose style at the level of the sentence — rhythm, syntax, diction — and revise their own writing for greater clarity, precision, and voice.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/watch?v=kLJE8IYIQEM",
   quiz:[
     {q:"Prose style at the sentence level includes ___.", options:["only grammar and spelling","only sentence length","only vocabulary choice","rhythm, syntax, and diction together"], answer:3},
     {q:"Varying sentence length in academic prose ___.", options:["shows inconsistent style","has no effect on the reader","should be avoided in formal writing","creates rhythm and emphasis"], answer:3},
     {q:"Nominalisations (turning verbs/adjectives into nouns) in academic writing ___.", options:["always improve clarity","are mandatory in formal academic style","should be avoided always","can obscure agency and add density"], answer:3},
     {q:"The difference between a precise word and an approximate one is ___.", options:["only important in poetry","only a matter of style","enormous in academic writing","unimportant if the meaning is roughly correct"], answer:2},
     {q:"Revision at the sentence level should happen ___.", options:["never — first drafts are always good enough","after revising argument and structure","before revising the argument structure","only for the introduction"], answer:1}
   ]},
  {subject:"AdvancedFunctions", title:"Advanced Functions: Final Exam Preparation", summary:"Rigorous examination-level practice with full worked solutions for all Advanced Functions topics.",
   resourceLabel:"Khan Academy", resourceUrl:"https://www.youtube.com/watch?v=LkwT1GQVJP8",
   quiz:[
     {q:"Determine all values of k for which x³ + 5x² + kx + 2 has (x+2) as a factor.", options:["k = 3","k = 5","P(−2) = 0: −8+20−2k+2=0 → 14−2k=0 → k=7","k = −7"], answer:2},
     {q:"Find the scalar equation of the plane through P(1,2,3), Q(2,−1,0), R(4,1,2).", options:["3x+4y+4z = 6","3x−4y+4z = 0","x+y+z = 6","3x+4y−4z = −1"], answer:3},
     {q:"A geometric series has t₃ = 12 and t₆ = 96. Find t₁ and r.", options:["r=4, t₁=0.75","r=2, t₁=6","r=2, t₁=3","t₃=t₁r²=12; t₆=t₁r⁵=96; dividing: r³=8 → r=2; t₁=12/4=3"], answer:2},
     {q:"P(at least one 6 in 4 rolls of a fair die) = ___.", options:["(1/6)⁴","4/6","≈ 0.518 (via 1 − P(no sixes))","4 × 1/6 = 2/3"], answer:2},
     {q:"The maximum value of f(x) = sin(2x) + cos(2x) is ___.", options:["1","√3","2","√2 (amplitude R=√2)"], answer:3}
   ]},
  {subject:"Calculus", title:"Calculus: Final Exam Preparation", summary:"Rigorous examination-level problems for Calculus and Vectors.",
   resourceLabel:"Khan Academy Calculus", resourceUrl:"https://www.youtube.com/watch?v=6HkBGVPWIXA",
   quiz:[
     {q:"Find the area between y=e^x, y=x, x=0, x=1.", options:["e − 1","e − 3/2 ≈ 1.218","1/2","e"], answer:1},
     {q:"A particle has velocity v(t) = 3t² − 6t. Find the displacement from t=0 to t=3.", options:["3","0 (returns to start)","−9","9"], answer:1},
     {q:"Evaluate ∫ x·ln(x) dx.", options:["x²ln(x)/2 − x²/4 + C","x ln(x) − x + C","ln(x²)/2 + C","x²ln(x)/2 + C"], answer:0},
     {q:"The line tangent to the curve x²y + y³ = 10 at (1,2):", options:["y = −4/13 x + 30/13","y−2 = 4/13(x−1)","y−2 = −4/13(x−1)","y = −x + 3"], answer:2},
     {q:"A box is formed by cutting squares of side x from corners of a 30×20 cm sheet. Maximise volume.", options:["x = 5 cm","x = 10 cm","x ≈ 3.9 cm","x = 3 cm"], answer:2}
   ]},
  {subject:"Physics", title:"Physics: Final Exam Preparation", summary:"Comprehensive examination-level physics problems spanning all SPH4U topics.",
   resourceLabel:"Crash Course Physics", resourceUrl:"https://www.youtube.com/watch?v=kKKM8Y-u7ds",
   quiz:[
     {q:"A 0.5 kg ball on a 1 m string moves in a horizontal circle at 3 m/s. Tension in string (ignore gravity):", options:["T = mv²/r = 0.5×9/1 = 4.5 N","T = 1.5/1 = 1.5 N","T = 5 N","T = 0.5 × 3 = 1.5 N"], answer:0},
     {q:"Two parallel plates 0.01 m apart with potential difference 100 V. Electric field between plates:", options:["E = 1000 V/m","E = 100 V/m","E = 10 V/m","E = V/d = 100/0.01 = 10,000 V/m"], answer:3},
     {q:"An 8 kg mass oscillates on a spring (k = 200 N/m). Period:", options:["T = 2π s","T ≈ 1.26 s","T = 0.2 s","T = 2π√(200/8) ≈ 15.7 s"], answer:1},
     {q:"A generator coil (N=100 turns, area 0.05 m², B=0.8 T) rotates at 60 Hz. Peak EMF:", options:["EMF = 60 V","EMF = 100×60 = 6000 V","EMF = NBAB = 4 V","EMF_max ≈ 1508 V"], answer:3},
     {q:"An electron (m=9.11×10⁻³¹ kg) is accelerated through 500 V. Final kinetic energy and speed:", options:["v = 500 m/s","v = c = 3×10⁸ m/s","v = 3×10⁵ m/s","v ≈ 1.33×10⁷ m/s"], answer:3}
   ]},
]},
{day:28, label:"Day 28 — Wed", subjects:[
  {subject:"English", title:"Culminating Essay: Writing Under Examination Conditions", summary:"Students practise writing a full analytical essay under timed conditions, applying all skills developed throughout the year.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/watch?v=kLJE8IYIQEM",
   quiz:[
     {q:"The most important 5 minutes of a timed literary essay are ___.", options:["the first 5 minutes of planning","the conclusion","the middle of the essay","the last 5 minutes of writing"], answer:0},
     {q:"In a timed essay, the most common weakness is ___.", options:["insufficient analytical development","writing too slowly","knowing the text too well","writing in too formal a register"], answer:0},
     {q:"Choosing a quotation under time pressure: prefer ___.", options:["only quotations you've memorised exactly","the longest quotation you can recall","a short, specific phrase that is analytically productive","any passage you remember"], answer:2},
     {q:"Ending a timed essay effectively: the conclusion should ___.", options:["repeat the introduction word for word","introduce new evidence","only name the texts again","synthesise the essay's argument in 3-5 sentences"], answer:3},
     {q:"A student who has genuinely mastered Grade 12 English will find timed writing ___.", options:["only useful for English exams","impossible without notes","irrelevant to real university skill","challenging but empowering"], answer:3}
   ]},
  {subject:"AdvancedFunctions", title:"Advanced Functions: Culminating Task", summary:"Students complete a culminating task integrating multiple strands of the MHF4U course.",
   resourceLabel:"Khan Academy", resourceUrl:"https://www.youtube.com/watch?v=jKrEFOTScwU",
   quiz:[
     {q:"Part 1: Identify all features of f(x) = (x²−4)/(x²−x−2) and sketch.", options:["VA at x=2 and x=1 only","x-int at x = ±2 with no hole","Hole x=2; VA x=−1; HA y=1; x-int −2","HA at y = 0"], answer:2},
     {q:"Part 2: Solve 2^(x+1) = 3^(x−1) algebraically.", options:["x = ln6/(ln3−ln2) ≈ 3.82","x = 1","x = 2","x = ln(3/2)"], answer:0},
     {q:"Part 3: The position vectors of points A and B are a=(3,1,−2) and b=(1,−1,4). Find the midpoint M and |AB|.", options:["M = (1,1,1); |AB| = √44","M = (2,0,1); |AB| = √40","M=(2,0,1); |AB|=√44=2√11","M = (4,0,2); |AB| = 8"], answer:2},
     {q:"Part 4: A fair coin is tossed 8 times. Find P(at least 6 heads).", options:["1/4","37/64","37/256","P(X≥6) = P(6)+P(7)+P(8) = [C(8,6)+C(8,7)+C(8,8)]/2⁸ = (28+8+1)/256 = 37/256 ≈ 0.145"], answer:2},
     {q:"Part 5: Prove by induction that ∑(k=1 to n) k³ = [n(n+1)/2]².", options:["Requires calculus, not induction","Formula is incorrect","True for n=1; induction confirms it","Not provable by induction"], answer:2}
   ]},
  {subject:"Calculus", title:"Calculus: Culminating Task", summary:"Students complete a culminating task integrating limits, derivatives, and integrals.",
   resourceLabel:"Khan Academy Calculus", resourceUrl:"https://www.youtube.com/watch?v=9vgCMNHPScU",
   quiz:[
     {q:"Part 1: lim(x→0) (e^x − 1 − x)/x².", options:["the limit is 0","L'Hôpital once: e^x − 1","the limit is 1","L'Hôpital twice: limit = 1/2"], answer:3},
     {q:"Part 2: Differentiate f(x) = arctan(√x) and find f'(1).", options:["f'(1) = 1/4 via chain rule","f'(x) = 1/(1+x) × 1/(2√x) = 1/(2√x(1+x)); f'(1) = 1/(2×1×2) = 1/4","f'(x) = 1/(2√x)","f'(1) = 1/2"], answer:0},
     {q:"Part 3: ∫₀^(π/2) sin²(x) dx.", options:["π/4","use identity sin²x = (1−cos2x)/2; ∫₀^(π/2)(1−cos2x)/2 dx = [x/2−sin(2x)/4]₀^(π/2) = π/4","1/2","π/2"], answer:0},
     {q:"Part 4: Find the point on y = x² closest to (0, 3).", options:["(0,0)","(1,1)","(√11/2, 11/4), from minimising D²","(√3, 3)"], answer:2},
     {q:"Part 5: Solve dy/dx = xy with y(0) = 1.", options:["y = x²/2 + 1","y = xe^x + 1","y = e^(x²/2) (separable ODE)","y = e^x"], answer:2}
   ]},
  {subject:"Physics", title:"Physics: Culminating Task", summary:"Students complete a multi-concept physics culminating task.",
   resourceLabel:"Crash Course Physics", resourceUrl:"https://www.youtube.com/watch?v=aY8z2qO44WA",
   quiz:[
     {q:"A projectile is launched at 50 m/s at 37° above horizontal. Find max height and range.", options:["H=50 m; R=200 m","H=40 m; R=250 m","H=30 m; R=300 m","H≈45.9 m, R≈245 m (v₀y=30, v₀x=40)"], answer:3},
     {q:"A 2 kg block slides down a 30° ramp (μₖ=0.2) of length 5 m from rest. Speed at bottom:", options:["v≈5.66 m/s (a=3.2 m/s² down the ramp)","v = 5 m/s","v = 10 m/s","v = √(2gh) = √(2×9.8×2.5) ≈ 7 m/s"], answer:0},
     {q:"A transformer: 120 V primary, 2400 V secondary, 0.5 A secondary current. Primary current:", options:["I_p = 0.025 A","I_p = 0.5 A","I_p = 2.5 A","I_p = 2400×0.5/120 = 10 A"], answer:3},
     {q:"Radioactive source: activity at t=0 is 8000 Bq; after 12 hours = 1000 Bq. Find T½.", options:["T½ = 2 hours","T½ = 3 hours","T½ = 6 hours","T½=4 hours, since 12h = 3 half-lives"], answer:3},
     {q:"Calculate the de Broglie wavelength of an electron (m=9.11×10⁻³¹ kg) moving at 10⁶ m/s.", options:["λ = 10⁻⁶ m","λ = 1 nm","λ = 10⁻³⁴ m","λ = h/(mv) ≈ 7.28×10⁻¹⁰ m = 0.728 nm"], answer:3}
   ]},
]},
{day:29, label:"Day 29 — Thu", subjects:[
  {subject:"English", title:"Grade 12 English: Oral Culminating and Reflection", summary:"Students deliver oral culminating presentations and reflect on their growth as readers, writers, and thinkers across Grade 12.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/watch?v=MSYw502dJNY",
   quiz:[
     {q:"An oral culminating in Grade 12 English demonstrates ___.", options:["only knowledge of plot","integrating all your analytical skills","only public speaking skill","only the ability to memorise"], answer:1},
     {q:"Reflecting on your development as a reader across Grade 12 means ___.", options:["only counting books read","articulating what has changed in how you read","only recognising what you found difficult","only identifying your favourite text"], answer:1},
     {q:"The skills developed in Grade 12 English that transfer most directly to university are ___.", options:["only knowledge of canonical literature","critical reading and analytical writing","only reading speed","only essay formatting"], answer:1},
     {q:"The most significant intellectual growth in Grade 12 English occurs when ___.", options:["you finish all the assessments","you get the highest mark","you form your own original arguments","you have memorised the most quotations"], answer:2},
     {q:"Grade 12 English is fundamentally about ___.", options:["preparing for English at university","memorising literary terms","thinking and communicating precisely","learning to write five-paragraph essays"], answer:2}
   ]},
  {subject:"AdvancedFunctions", title:"Advanced Functions: Final Reflection and Looking Forward", summary:"Students reflect on the year's learning in Advanced Functions and its significance for future study.",
   resourceLabel:"Khan Academy", resourceUrl:"https://www.youtube.com/watch?v=nRmBsxBpTjs",
   quiz:[
     {q:"The central organising concept of Advanced Functions is ___.", options:["the function as a general math object","only polynomial equations","the derivative of a function","only trigonometric functions"], answer:0},
     {q:"A student who has mastered Advanced Functions can ___.", options:["only work in Ontario high schools","only solve textbook problems","never need mathematics again","analyse a function's type and features"], answer:3},
     {q:"The connection between Advanced Functions and Calculus is ___.", options:["calculus is harder but unrelated","direct — calculus builds on functions","Advanced Functions is only for non-calculus students","calculus uses completely different functions"], answer:1},
     {q:"The proof and reasoning strand in Advanced Functions ___.", options:["is unrelated to the function content","introduces formal math reasoning","is only for future mathematics students","is only about mathematical induction"], answer:1},
     {q:"Looking back on Grade 12 mathematics, the most valuable habit of mind developed is ___.", options:["test-taking strategy","speed at calculation","mathematical curiosity","memorisation of formulas"], answer:2}
   ]},
  {subject:"Calculus", title:"Calculus: Final Reflection and University Preparation", summary:"Students reflect on Calculus learning and prepare for university calculus courses.",
   resourceLabel:"Khan Academy Calculus", resourceUrl:"https://www.youtube.com/watch?v=riXcZT2ICjA",
   quiz:[
     {q:"The two most important ideas in Calculus are ___.", options:["the product rule and chain rule","derivatives and integrals as separate topics","the derivative and integral (inverses)","limits and power rule"], answer:2},
     {q:"University calculus (Calculus I, II) will build on your Grade 12 learning by ___.", options:["not requiring any Grade 12 preparation","being much easier","adding multivariable calc and series","starting completely from scratch"], answer:2},
     {q:"The most important skill for university calculus is ___.", options:["memorising all derivative rules","algebraic fluency","only understanding limits","only understanding integration"], answer:1},
     {q:"Calculus is the mathematics of ___.", options:["only curves and slopes","only areas and volumes","only physics","change: motion, growth, decay, and flow"], answer:3},
     {q:"The experience of Grade 12 Calculus ___.", options:["shows mathematics is only about computation","shows that advanced mathematics is inaccessible to most people","is sufficient for all future mathematics needs","shows persistence unlocks deep ideas"], answer:3}
   ]},
  {subject:"Physics", title:"Physics: Final Reflection and Looking to University", summary:"Students reflect on their Grade 12 Physics learning and its connections to university physics and modern life.",
   resourceLabel:"Crash Course Physics", resourceUrl:"https://www.youtube.com/watch?v=aY8z2qO44WA",
   quiz:[
     {q:"The most important conceptual development in Grade 12 Physics is ___.", options:["understanding the SI unit system","moving from Newtonian to quantum ideas","learning to use complex formulas","knowing all fundamental constants"], answer:1},
     {q:"University physics (mechanics, E&M, waves/optics, modern physics) builds on Grade 12 by ___.", options:["deepening and mathematising every concept","repeating the same material","being completely different in content","being much easier"], answer:0},
     {q:"Physics problem-solving skill transfers to ___.", options:["only engineering problems","only science","only physics problems","any domain needing structured analysis"], answer:3},
     {q:"The most significant open problems in physics today are ___.", options:["quantum gravity and dark matter/energy","already solved in principle","only relevant to theorists","only mathematical"], answer:0},
     {q:"Grade 12 Physics has shown you that ___.", options:["physics is a closed discipline with all answers known","the universe operates according to mathematical laws of astonishing elegance and power","equations are more important than concepts","physics is only for those who plan to study it at university"], answer:1}
   ]},
]},
{day:30, label:"Day 30 — Fri", subjects:[
  {subject:"English", title:"Grade 12 Celebration: A Year of Growth", summary:"A final day celebrating the intellectual journey of Grade 12 — reflecting on growth, looking ahead to university and life, and recognising what has been accomplished.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/watch?v=jTDkTt1UTXM",
   quiz:[
     {q:"The most important thing accomplished in Grade 12 is ___.", options:["only university preparation","only skill development","genuine intellectual growth","a high grade average"], answer:2},
     {q:"University marks a transition from ___.", options:["high school content to harder content","guided learning to independent intellectual life","being assessed to never being assessed again","one set of rules to another set of rules"], answer:1},
     {q:"The reading and writing skills developed in Grade 12 ___.", options:["are only for English programs","will be forgotten quickly after exams","are vital in any analytical field","have no relevance outside school"], answer:2},
     {q:"Looking back on all of Grade 12, the subject that will most surprise you at university is ___.", options:["the one that opens up into a vast new world","the one that gave you the worst grade","the one you studied least","the one that was easiest in high school"], answer:0},
     {q:"The best preparation for university and adult life that Grade 12 has provided is ___.", options:["achieving the highest possible marks","only having specific skills","knowing all the curriculum content","the experience of sustained intellectual effort"], answer:3}
   ]},
  {subject:"AdvancedFunctions", title:"Grade 12 Mathematics: Final Day Celebration", summary:"Students celebrate completing two of Ontario's most rigorous mathematics courses and look ahead with confidence.",
   resourceLabel:"Khan Academy: Encouragement for Math Students", resourceUrl:"https://www.youtube.com/watch?v=riXcZT2ICjA",
   quiz:[
     {q:"Completing both Advanced Functions and Calculus in Grade 12 demonstrates ___.", options:["nothing about future capabilities","genuine mathematical maturity","only good test-taking strategy","only that you like mathematics"], answer:1},
     {q:"The discipline of solving a difficult mathematics problem translates to ___.", options:["nothing outside mathematics","only to science and engineering","any field needing persistence and rigor","only future mathematics problems"], answer:2},
     {q:"The most important mathematical truth you have encountered in Grade 12 is ___.", options:["the quadratic formula","the formula for the area of a circle","that calculus links two core operations","only the power rule"], answer:2},
     {q:"A student who has done well in Grade 12 mathematics should feel ___.", options:["that they have developed genuine mathematical power","that they have exhausted mathematics","that mathematics is now fully mastered","that mathematics is only useful for specialists"], answer:0},
     {q:"Looking ahead, Grade 12 mathematics graduates who pursue further study will discover ___.", options:["that all mathematics has now been discovered","that first-year university mathematics is the same as Grade 12","that mathematics is a vast, living field of inquiry","that mathematics becomes less interesting at university"], answer:2}
   ]},
  {subject:"Physics", title:"Grade 12 Physics: Final Day", summary:"Students celebrate completing Grade 12 Physics and look ahead to university and the world of physics.",
   resourceLabel:"Crash Course Physics: Celebration", resourceUrl:"https://www.youtube.com/watch?v=pGj9isFr21U",
   quiz:[
     {q:"Grade 12 Physics has given you ___.", options:["only a foundation for university physics","a way of seeing the world","only laboratory skills","only a set of formulas to memorise"], answer:1},
     {q:"The greatest physicists (Newton, Faraday, Maxwell, Einstein, Bohr, Feynman) were unified by ___.", options:["only mathematical genius","deep curiosity about how the world works","only experimental skill","only theoretical creativity"], answer:1},
     {q:"Climate change, renewable energy, quantum computing, and medical imaging are all ___.", options:["applications of physical principles","only political issues","unrelated to physics","only engineering problems"], answer:0},
     {q:"The challenges that await the next generation of physicists and engineers include ___.", options:["problems that have already been solved","only problems in pure mathematics","fusion energy and quantum computing","only incremental improvements to existing technology"], answer:2},
     {q:"The final lesson of Grade 12 Physics is ___.", options:["only specialists need to understand physics","physics content is fully memorised and complete","curiosity is the essential scientific virtue","physics is too difficult for most people"], answer:2}
   ]},
]},
];

export default curriculum;