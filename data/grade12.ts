import type { DayContent } from '@/types';

const curriculum: DayContent[] = [
{day:1, label:"Day 1 — Mon", subjects:[
  {subject:"English", title:"Literary Analysis: University-Level Essay Writing", summary:"Students develop the analytical writing skills required for first-year university — constructing complex arguments, integrating sources, and writing with precision and intellectual authority.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/c/TEDEd",
   quiz:[
     {q:"A university-level literary argument differs from a high school argument in that ___.", options:["it requires longer essays","it avoids personal interpretation","it uses more quotations","it engages with the critical conversation around a text — acknowledging existing interpretations and positioning your own reading in relation to them, not just stating your view in isolation"], answer:3},
     {q:"Intellectual authority in academic writing is established through ___.", options:["using complex vocabulary","only citing many sources","writing confidently regardless of evidence","precise, specific claims supported by carefully selected and analysed evidence — authority comes from the quality of your reasoning, not the confidence of your assertions"], answer:3},
     {q:"A counterargument in an academic essay ___.", options:["weakens your position","should always be avoided","proves you are unsure of your argument","strengthens your argument when addressed and refuted — demonstrating that you have considered alternative interpretations and can explain why your reading is more persuasive"], answer:3},
     {q:"Integrating literary criticism responsibly means ___.", options:["copying the critic's argument as your own","only agreeing with critics","avoiding critics who disagree with you","engaging critically with secondary sources — using them to inform, enrich, or challenge your reading, while maintaining your own analytical voice and making your own contribution"], answer:3},
     {q:"The most important difference between high school and university English is ___.", options:["university requires less reading","university essays are always longer","grammar is more important at university","intellectual independence: university expects you to formulate genuine, original questions about texts and pursue them with rigour, not just respond to provided prompts"], answer:3}
   ]},
  {subject:"Advanced Functions", title:"Polynomial Functions: Deep Dive into Graphs and Equations", summary:"Students investigate polynomial functions of all degrees — connecting multiplicity of zeros, end behaviour, turning points, and algebraic form to graphical behaviour.",
   resourceLabel:"Khan Academy: Polynomial Graphs", resourceUrl:"https://www.youtube.com/watch?v=1WRYEBHLLm8",
   quiz:[
     {q:"A polynomial of degree n can have at most ___ real zeros and at most ___ turning points.", options:["n zeros and n turning points","n-1 zeros and n turning points","n zeros and n-1 turning points (a degree-n polynomial has at most n zeros and at most n-1 local maxima/minima)","n+1 zeros and n turning points"], answer:2},
     {q:"A zero of multiplicity 2 means the graph ___.", options:["crosses the x-axis steeply","has a vertical asymptote","crosses the x-axis at a 45° angle","touches but does not cross the x-axis — the graph is tangent to the x-axis at that zero"], answer:3},
     {q:"A zero of multiplicity 3 means the graph ___.", options:["touches and bounces","has no x-intercept there","crosses with an S-curve (point of inflection) at that zero — flattening as it crosses","creates a sharp corner"], answer:2},
     {q:"For P(x) = −2(x+1)²(x−3)(x−5), the end behaviour is ___.", options:["rises left, rises right","falls left, rises right","rises left, falls right","falls both directions — leading term is −2x⁴ (even degree, negative coefficient)"], answer:3},
     {q:"The Intermediate Value Theorem guarantees ___.", options:["a polynomial has exactly n roots","the maximum value of a polynomial","a zero exists between a and b if P(a) and P(b) have opposite signs — at least one zero must exist where the graph crosses zero","a polynomial is always continuous"], answer:2}
   ]},
  {subject:"Calculus", title:"Introduction to Limits and Continuity", summary:"Students develop an intuitive and rigorous understanding of limits — what they mean, how to evaluate them, and their role as the foundation of calculus.",
   resourceLabel:"Khan Academy: Limits Intro", resourceUrl:"https://www.youtube.com/watch?v=riXcZT2ICjA",
   quiz:[
     {q:"The limit of f(x) as x → a means ___.", options:["the value of f(a)","the maximum of f near a","the derivative of f at a","the value that f(x) approaches as x gets arbitrarily close to a — regardless of (and independent of) f(a) itself"], answer:3},
     {q:"A limit exists at x = a if and only if ___.", options:["f(a) is defined","the left-hand and right-hand limits both exist and are equal to each other","the function is differentiable at a","the function is continuous at a"], answer:1},
     {q:"To evaluate lim(x→2) of (x²−4)/(x−2), you ___.", options:["substitute x = 2 directly (gives 0/0)","conclude the limit does not exist","use L'Hôpital's Rule always","factor: (x−2)(x+2)/(x−2) = x+2 for x≠2, so the limit = 4"], answer:3},
     {q:"A function f is continuous at x = a if ___.", options:["f(a) is a large number","f(a) = 0","the derivative exists at a","three conditions hold: f(a) is defined, lim(x→a)f(x) exists, and lim(x→a)f(x) = f(a)"], answer:3},
     {q:"A removable discontinuity (hole) occurs when ___.", options:["the limit does not exist at the point","the function goes to infinity","the function is not defined anywhere","the limit exists at x = a but either f(a) is undefined or f(a) ≠ the limit — the discontinuity can be "fixed" by redefining f(a)"], answer:3}
   ]},
  {subject:"Physics", title:"Kinematics in 2D: Projectile Motion", summary:"Students analyse projectile motion by decomposing it into independent horizontal and vertical components, applying kinematic equations to each.",
   resourceLabel:"Crash Course Physics: Projectile Motion", resourceUrl:"https://www.youtube.com/watch?v=aY8z2qO44WA",
   quiz:[
     {q:"In projectile motion, the horizontal and vertical components are independent because ___.", options:["gravity acts horizontally","air resistance eliminates horizontal motion","horizontal velocity is always zero","gravity only acts vertically — horizontal velocity remains constant (no acceleration), while vertical motion has constant downward acceleration g = 9.8 m/s²"], answer:3},
     {q:"A projectile launched horizontally from height h has a time of flight determined by ___.", options:["initial horizontal speed only","only horizontal distance","the angle of launch","the vertical fall: h = ½gt², so t = √(2h/g) — same as a dropped object from the same height"], answer:3},
     {q:"The range of a projectile (launched at angle θ with speed v₀) is maximised when ___.", options:["θ = 90°","θ = 30°","θ = 60°","θ = 45° — for a level surface, R = v₀²sin(2θ)/g, maximised when sin(2θ) = 1, i.e., 2θ = 90°"], answer:3},
     {q:"At the peak of a projectile's trajectory, ___.", options:["both velocity components are zero","horizontal velocity is zero","the projectile stops momentarily","only the vertical component of velocity is zero — horizontal velocity is unchanged throughout"], answer:3},
     {q:"If a ball is kicked at 20 m/s at 30° above horizontal, the initial vertical component is ___.", options:["20 m/s","10 m/s (v₀y = 20sin30° = 20 × 0.5 = 10 m/s)","17.3 m/s","10√3 m/s"], answer:1}
   ]},
]},
{day:2, label:"Day 2 — Tue", subjects:[
  {subject:"English", title:"Independent Study: The Novel — Form and Meaning", summary:"Students read a major novel independently, analysing how formal choices (narration, structure, style) create meaning rather than just content.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/c/TEDEd",
   quiz:[
     {q:"The distinction between story (fabula) and discourse (sjuzhet) means ___.", options:["they are the same in all novels","only the plot matters","discourse is less important than story","story is the raw chronological events; discourse is how those events are arranged and told — great novelists manipulate discourse to shape meaning, pace, and perspective"], answer:3},
     {q:"Free indirect discourse (FID) in a novel allows ___.", options:["only third-person narrators to speak","only direct quotation of characters","only interior monologue in first person","a third-person narrator to render a character's thoughts and speech without explicit tags — blurring the boundary between narrator and character, creating empathy and irony simultaneously"], answer:3},
     {q:"A novel's structure (chapters, parts, epigraphs) ___.", options:["is only for practical reading purposes","has no relation to meaning","is always chronological","creates meaning: fragmented structure can mirror a fragmented self; circular structure can suggest entrapment; the placement of chapter breaks shapes pacing and emphasis"], answer:3},
     {q:"Analysing a novel's prose style means ___.", options:["only counting long sentences","identifying the author's country of origin","only noting the vocabulary level","examining sentence length and rhythm, syntax, imagery, diction, tone, and the relationship between these choices and the novel's themes and effects"], answer:3},
     {q:"A sophisticated novel reading at Grade 12 produces ___.", options:["a plot summary with quotations","only a character description","a thematic overview without formal analysis","an argument about how the novel's formal choices create and enrich its meaning — form and content are inseparable"], answer:3}
   ]},
  {subject:"Advanced Functions", title:"Rational Functions: Analysis and Graphing", summary:"Students perform complete analysis of rational functions — identifying all asymptotes, holes, intercepts, and behaviour — and graph them without technology.",
   resourceLabel:"Khan Academy: Graphing Rational Functions", resourceUrl:"https://www.youtube.com/watch?v=5TkIe60y2GI",
   quiz:[
     {q:"To find all features of a rational function, you must ___.", options:["only find where it equals zero","only find vertical asymptotes","only graph it with technology","factor both numerator and denominator completely to identify zeros, holes, vertical asymptotes, and simplify for horizontal/oblique asymptotes"], answer:3},
     {q:"A slant (oblique) asymptote exists when ___.", options:["the denominator degree exceeds the numerator","degrees are equal","the denominator is linear only","the numerator degree is exactly 1 more than the denominator — found by polynomial long division"], answer:3},
     {q:"For f(x) = (2x² + 3x − 2)/( x − 1), the slant asymptote is found by ___.", options:["setting x → ∞ in the numerator","dividing 2x² + 3x − 2 by x − 1: 2x + 5 remainder 3, so slant asymptote y = 2x + 5","setting denominator = 0","cancelling x terms"], answer:1},
     {q:"To sketch a rational function, the correct sequence is ___.", options:["graph first, find features after","find only the x-intercepts","only find asymptotes","domain → vertical asymptotes/holes → horizontal/oblique asymptote → x-intercepts → y-intercept → behaviour near asymptotes → connect carefully"], answer:3},
     {q:"The end behaviour of f(x) = (x² + 2)/(x + 1) as x → ±∞ is ___.", options:["approaches y = x²","approaches y = 1","approaches the horizontal asymptote y = 0","approaches the slant asymptote y = x − 1 (since x² + 2 ÷ (x+1) = x − 1 remainder 3)"], answer:3}
   ]},
  {subject:"Calculus", title:"Derivatives: Definition and Basic Rules", summary:"Students develop the concept of the derivative as a limit of difference quotients, and apply the basic differentiation rules (power, constant, sum, difference).",
   resourceLabel:"Khan Academy: Derivative Rules", resourceUrl:"https://www.youtube.com/watch?v=HEH_oKNLgUU",
   quiz:[
     {q:"The derivative f'(a) is defined as ___.", options:["f(a+h) − f(a)","f(a)/h","lim(h→0)[f(a+h) − f(a)]/h — the slope of the tangent line at x = a","f(a+1) − f(a)"], answer:2},
     {q:"The power rule states d/dx[xⁿ] = ___.", options:["xⁿ⁻¹","nxⁿ","nxⁿ+1","nxⁿ⁻¹ — bring down the exponent and reduce it by 1"], answer:3},
     {q:"d/dx[5x³ − 2x + 7] = ___.", options:["5x² − 2","15x³ − 2","5x³ − 2","15x² − 2 (power rule on each term; constant 7 disappears)"], answer:3},
     {q:"The derivative of a constant is ___.", options:["the constant itself","1","undefined","0 — constants have no rate of change"], answer:3},
     {q:"The derivative f'(x) represents ___.", options:["the area under f(x)","f(x) squared","the antiderivative of f(x)","the instantaneous rate of change of f(x) — the slope of the tangent line to the graph of f at any point x"], answer:3}
   ]},
  {subject:"Physics", title:"Forces: Newton's Laws in 2D", summary:"Students apply Newton's three laws to two-dimensional force problems, including inclined planes, connected masses, and friction.",
   resourceLabel:"Crash Course Physics: Newtons Laws", resourceUrl:"https://www.youtube.com/watch?v=kKKM8Y-u7ds",
   quiz:[
     {q:"For a block on a frictionless inclined plane at angle θ, the acceleration down the incline is ___.", options:["g","g cosθ","g tanθ","g sinθ — only the component of gravity along the incline acts (mg sinθ = ma, so a = g sinθ)"], answer:3},
     {q:"Normal force on an inclined plane (angle θ, mass m) is ___.", options:["mg","mg sinθ","mg tanθ","mg cosθ — perpendicular to the incline surface"], answer:3},
     {q:"Kinetic friction force equals ___.", options:["μₛN","μN always","μₖmg always","μₖN — kinetic friction coefficient times normal force, opposing motion"], answer:3},
     {q:"Two masses m₁ and m₂ connected by a rope over a frictionless pulley: the acceleration is ___.", options:["(m₁ − m₂)g/(m₁ + m₂)... wait — depends on orientation","g for both","only m₁g","a = (m₁ − m₂)g/(m₁ + m₂) for an Atwood machine — net force divided by total mass"], answer:0},
     {q:"Newton's Third Law states that for every action force there is ___.", options:["a larger reaction force","no corresponding reaction","a smaller reaction force in the same direction","an equal and opposite reaction force — acting on a DIFFERENT object than the action force"], answer:3}
   ]},
]},
{day:3, label:"Day 3 — Wed", subjects:[
  {subject:"English", title:"Literature: The Tragic Form Across Cultures", summary:"Students compare the tragic form in different cultural traditions — Greek tragedy, Shakespearean tragedy, and contemporary tragic narratives — examining what "tragedy" means across time and culture.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/c/TEDEd",
   quiz:[
     {q:"Greek tragedy (Sophocles, Euripides) differs from Shakespearean tragedy in ___.", options:["Greek tragedy has no hero","Shakespeare's tragedies have no tragic flaws","they are identical in form","Greek tragedy uses a chorus, observes the three unities (time, place, action), explores fate vs. free will through divine will; Shakespeare focuses on individual psychological complexity in a Christian moral framework"], answer:3},
     {q:"The concept of catharsis (Aristotle) means ___.", options:["the hero's physical death","the villain's punishment","the audience's purging or clarification of emotions — pity and fear experienced through tragedy serve a therapeutic or enlightening function for the audience","the protagonist's recognition of their error"], answer:3},
     {q:"Anagnorisis (recognition) in Greek tragedy is ___.", options:["the moment of physical death","only relevant in comedy","a minor plot device","the protagonist's moment of terrible recognition — realising the truth of their situation, often connected to hamartia — which may precede but cannot prevent their downfall"], answer:3},
     {q:"Contemporary tragic narratives (film, novel, theatre) typically ___.", options:["avoid tragic form entirely","only follow the Greek model","reproduce the Shakespearean model exactly","adapt the tragic form to modern concerns: the tragic hero may be ordinary rather than royal, the forces of doom may be social and psychological rather than divine, and catharsis may be replaced by critique"], answer:3},
     {q:"Comparing tragic forms across cultures illuminates ___.", options:["only historical differences","only literary technique","that tragedy is purely a Western form","how different cultures understand fate, justice, individual agency, and what makes human suffering meaningful — tragedy is a cross-cultural form, but its specific expression reflects distinct world views"], answer:3}
   ]},
  {subject:"Advanced Functions", title:"Exponential and Logarithmic Functions: Advanced Applications", summary:"Students solve complex exponential and logarithmic equations, apply change of base, and model real phenomena including logistic growth.",
   resourceLabel:"Khan Academy: Logarithm Properties", resourceUrl:"https://www.youtube.com/watch?v=TMmxKZaCqe0",
   quiz:[
     {q:"The change of base formula log_b(x) = log(x)/log(b) allows ___.", options:["converting bases only in specific cases","converting only to base 10","only base-2 conversions","evaluating logarithms in any base using a calculator (which typically has only base-10 or base-e), and simplifying logarithmic expressions"], answer:3},
     {q:"Solve: log₂(x) + log₂(x − 2) = 3", options:["x = 3 (only valid solution: log₂(x(x−2)) = 3 → x(x−2) = 8 → x²−2x−8 = 0 → (x−4)(x+2) = 0 → x = 4 or x = −2; x = −2 rejected since log is undefined there)","x = 4 — check: log₂(4) + log₂(2) = 2 + 1 = 3 ✓","x = −2","x = 4 or x = −2"], answer:1},
     {q:"Logistic growth f(t) = L/(1 + ae^(−kt)) models populations because ___.", options:["it only models exponential growth","it allows unlimited growth","it always decreases","it shows rapid initial growth that slows as the population approaches the carrying capacity L — more realistic than pure exponential growth"], answer:3},
     {q:"The natural logarithm ln(x) = log_e(x) is especially important because ___.", options:["e is a round number","ln is easier to calculate","ln has simpler graphs","the number e ≈ 2.718 arises naturally in calculus (as the base of the derivative of exponential functions) — ln is the inverse of e^x, the most important exponential function"], answer:3},
     {q:"Solve: e^(2x) − 5e^x + 6 = 0", options:["x = ln2 and x = ln3 (let u = e^x: u² − 5u + 6 = (u−2)(u−3) = 0; u = 2 or 3; e^x = 2 → x = ln2; e^x = 3 → x = ln3)","x = 2 and x = 3","x = ln5","x = 0"], answer:0}
   ]},
  {subject:"Calculus", title:"Derivatives: Product, Quotient, and Chain Rules", summary:"Students master the three composite differentiation rules and apply them to increasingly complex functions.",
   resourceLabel:"Khan Academy: Chain Rule", resourceUrl:"https://www.youtube.com/watch?v=0T0QrHO56qg",
   quiz:[
     {q:"The product rule for d/dx[f(x)g(x)] is ___.", options:["f'(x) × g'(x)","f'(x)g(x)","f(x)g'(x)","f'(x)g(x) + f(x)g'(x) — differentiate each factor and apply"], answer:3},
     {q:"The quotient rule for d/dx[f(x)/g(x)] is ___.", options:["f'(x)/g'(x)","[f'(x)g(x) + f(x)g'(x)] / [g(x)]²","[f'g − fg'] / g²  (low d-high minus high d-low, over low squared)","[f'(x) − g'(x)] / g(x)"], answer:2},
     {q:"The chain rule for d/dx[f(g(x))] is ___.", options:["f'(x) × g'(x)","f'(g(x))","f(g'(x))","f'(g(x)) × g'(x) — differentiate the outer function at the inner, times the derivative of the inner"], answer:3},
     {q:"d/dx[(3x² + 1)⁵] = ___.", options:["5(3x² + 1)⁴","5(6x)⁴","5(3x² + 1)⁴ × 6x (chain rule: outer × derivative of inner)","(3x² + 1)⁵ × 6x"], answer:2},
     {q:"d/dx[sin(x²)] = ___.", options:["cos(x²)","sin(2x)","2x cos(x)","2x cos(x²) — chain rule: cos(x²) × 2x"], answer:3}
   ]},
  {subject:"Physics", title:"Work, Energy, and Power: Advanced Applications", summary:"Students apply the work-energy theorem, conservation of mechanical energy, and power calculations to complex problems.",
   resourceLabel:"Crash Course Physics: Work Energy Power", resourceUrl:"https://www.youtube.com/watch?v=xNzS1OsPbFg",
   quiz:[
     {q:"The work-energy theorem states ___.", options:["work equals force times velocity","work equals potential energy change","net work done on an object equals its change in kinetic energy (W_net = ΔKE)","power equals work divided by displacement"], answer:2},
     {q:"Conservative forces are those for which ___.", options:["work depends on the path taken","no energy is stored","friction is the best example","work done is path-independent — only the endpoints matter; mechanical energy is conserved in systems with only conservative forces"], answer:3},
     {q:"Conservation of mechanical energy applies when ___.", options:["there is no kinetic energy","only gravity acts","only friction acts","only conservative forces act — total mechanical energy (KE + PE) remains constant"], answer:1},
     {q:"A 2 kg ball dropped from 5 m hits the ground with kinetic energy ___.", options:["98 J (KE = mgh = 2 × 9.8 × 5 = 98 J, by conservation of energy)","49 J","10 J","2 × 9.8 × 5 J = 98 J (confirm both methods agree)"], answer:0},
     {q:"Power is ___.", options:["force per unit area","energy per unit volume","work times time","the rate of energy transfer or work done: P = W/t = Fv (for constant force parallel to velocity)"], answer:3}
   ]},
]},
{day:4, label:"Day 4 — Thu", subjects:[
  {subject:"English", title:"Writing: Extended Critical Analysis Essay", summary:"Students plan and write a 1000+ word critical essay on a literary text, meeting university standards for argument, evidence, and analysis.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/c/TEDEd",
   quiz:[
     {q:"University literary essays are evaluated primarily on ___.", options:["the number of sources cited","word count","correct grammar only","the quality of the analytical argument — how specific, arguable, well-supported, and intellectually interesting the thesis is, and how precisely and rigorously it is developed"], answer:3},
     {q:"A 1000+ word essay requires ___.", options:["longer paragraphs with more quotations","simply more of the same as shorter essays","only one more body paragraph","more structural complexity: multiple interrelated lines of argument, developed through the essay, requiring careful paragraph sequencing and more sophisticated transitions"], answer:3},
     {q:"Evidence in a university essay should be ___.", options:["as long as possible","replaced by paraphrase always","always a minimum of 5 lines","precisely chosen — the smallest portion of text that demonstrates the specific point you are making, embedded grammatically, and always followed by analysis that earns the quotation"], answer:3},
     {q:"The difference between analysis and description in an extended essay is ___.", options:["they are the same at university level","description is more academic","analysis only appears in conclusions","description reports what the text does; analysis explains how and why specific choices create specific effects — every paragraph must be driven by analysis, not description"], answer:3},
     {q:"Concluding a long essay effectively requires ___.", options:["summarising all body paragraphs in order","repeating the thesis word for word","adding new evidence at the end","synthesising the essay's argument, extending the thesis to its larger implications, and leaving the reader with a new perspective or unresolved question — not just restating what has been said"], answer:3}
   ]},
  {subject:"Advanced Functions", title:"Trigonometric Functions: Identities and Equations (Advanced)", summary:"Students prove and apply advanced trigonometric identities including compound angle, double angle, and sum-to-product formulas, and solve complex trigonometric equations.",
   resourceLabel:"Khan Academy: Trig Identities", resourceUrl:"https://www.youtube.com/watch?v=T9lt6MZKLck",
   quiz:[
     {q:"To prove a trigonometric identity, you must ___.", options:["substitute specific values","start from both sides simultaneously","cross-multiply to eliminate fractions","work on one side only, transforming it to equal the other, using only known identities and algebraic operations — never treating it like an equation to solve"], answer:3},
     {q:"Prove: sin2x/(1 + cos2x) = tanx. Using sin2x = 2sinxcosx and cos2x = 2cos²x − 1:", options:["1 + cos2x = 2cos²x; so sin2x/(1+cos2x) = 2sinxcosx/2cos²x = sinx/cosx = tanx ✓","the identity is false","sin2x/1 + cos2x = tanx is trivially true","sin2x = tanx always"], answer:0},
     {q:"Sum-to-product: sinA + sinB = ___.", options:["2sin(A+B)cos(A−B)","sin(A+B)","2cos((A+B)/2)sin((A−B)/2)","2sin((A+B)/2)cos((A−B)/2) — a useful formula for adding sine functions"], answer:3},
     {q:"To solve 2cos²x − cosx − 1 = 0 on [0°, 360°):", options:["let u = cosx: (2u + 1)(u − 1) = 0; cosx = −1/2 → x = 120°, 240°; cosx = 1 → x = 0°","x = 60° only","x = 0° and 180°","x = 120° only"], answer:0},
     {q:"The equation sinx = 2 has ___.", options:["two solutions","infinitely many solutions","no solution — sinx is bounded between −1 and 1 for all real x","one solution at x = 90°"], answer:2}
   ]},
  {subject:"Calculus", title:"Derivatives of Trigonometric and Exponential Functions", summary:"Students differentiate sin(x), cos(x), tan(x), e^x, and ln(x), and combine these with the chain rule.",
   resourceLabel:"Khan Academy: Derivatives of Trig Functions", resourceUrl:"https://www.youtube.com/watch?v=_niP0JaOgHY",
   quiz:[
     {q:"d/dx[sin x] = ___.", options:["−sin x","sin x","−cos x","cos x"], answer:3},
     {q:"d/dx[cos x] = ___.", options:["sin x","cos x","−sin x","−cos x — this is negative, unlike the derivative of sine"], answer:3},
     {q:"d/dx[e^x] = ___.", options:["e^(x−1)","xe^(x−1)","1/e^x","e^x — the exponential function e^x is the unique function equal to its own derivative"], answer:3},
     {q:"d/dx[ln x] = ___.", options:["ln x","x/ln x","1/x — valid for x > 0","1/(x ln x)"], answer:2},
     {q:"d/dx[sin(3x²)] = ___.", options:["cos(3x²)","6x sin(3x²)","3x² cos(3x²)","6x cos(3x²) — chain rule: cos(3x²) × 6x"], answer:3}
   ]},
  {subject:"Physics", title:"Circular Motion and Gravitation", summary:"Students analyse uniform circular motion — centripetal acceleration and force — and apply Newton's law of universal gravitation.",
   resourceLabel:"Crash Course Physics: Circular Motion", resourceUrl:"https://www.youtube.com/watch?v=bpFK2VCRHUs",
   quiz:[
     {q:"Centripetal acceleration for uniform circular motion is ___.", options:["tangential acceleration","v/r","rω","v²/r directed toward the centre — it is the acceleration required to continually change the direction of velocity"], answer:3},
     {q:"The centripetal force is ___.", options:["a new type of force","the force of rotation","the outward "centrifugal force"","the net inward force that causes circular motion: F_c = mv²/r — it is provided by real forces such as gravity, tension, or normal force"], answer:3},
     {q:"Newton's law of universal gravitation: F = ___.", options:["Gm₁m₂/r","Gm₁m₂r²","Gm₁/m₂r²","Gm₁m₂/r² — gravitational force between two masses, inversely proportional to the square of the distance between them"], answer:3},
     {q:"Gravitational field strength g at Earth's surface is approximately 9.8 N/kg because ___.", options:["it is defined by convention","the Earth rotates","g = GM_E/R_E² — the gravitational field strength is Newton's Law applied to one mass at the Earth's surface","it is always constant everywhere"], answer:2},
     {q:"A satellite in circular orbit has ___.", options:["no gravitational force acting on it","zero speed","both thrust force and gravity","only gravity acting, providing the centripetal force: GM_E m/r² = mv²/r, giving orbital speed v = √(GM_E/r)"], answer:3}
   ]},
]},
{day:5, label:"Day 5 — Fri", subjects:[
  {subject:"English", title:"Media Analysis: Digital Media and Political Communication", summary:"Students analyse how digital platforms — social media, podcasts, algorithmic news — have transformed political communication and citizenship.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/c/TEDEd",
   quiz:[
     {q:"Political communication via social media differs from broadcast media in ___.", options:["it reaches fewer people","it is always more accurate","it has no political influence","its interactive, many-to-many architecture — anyone can broadcast to thousands; algorithms determine reach; misinformation can spread as fast as truth; echo chambers form algorithmically"], answer:3},
     {q:"Algorithmic curation of political content can affect democracy by ___.", options:["only increasing voter turnout","always improving the quality of political debate","eliminating all political bias in media","creating filter bubbles where citizens see primarily content that confirms their existing beliefs, potentially reducing exposure to legitimate opposing perspectives"], answer:3},
     {q:"Microtargeting in political advertising means ___.", options:["advertising to the largest possible audience","only using TV advertising","no personalisation in political ads","using detailed personal data (demographics, browsing history, location) to target specific political messages to specific individuals — much more precise than traditional broadcast advertising"], answer:3},
     {q:"Disinformation campaigns in digital media are effective because ___.", options:["false information is never shared widely","digital platforms always verify content","most people are incapable of critical thinking","corrections rarely spread as far as the original false claim; outrage drives engagement (and algorithmic amplification); and false information may be deliberately designed to be emotionally compelling and hard to disprove quickly"], answer:3},
     {q:"A digitally literate citizen evaluates political content by ___.", options:["sharing immediately if it confirms their views","trusting verified accounts automatically","only reading mainstream media","checking the source, looking for corroboration from multiple independent credible sources, examining who benefits from the claim, and being especially skeptical of content that produces strong emotional reactions"], answer:3}
   ]},
  {subject:"Advanced Functions", title:"Combining Functions: Operations and Compositions", summary:"Students perform operations on functions (sum, difference, product, quotient) and compositions, including finding domains of combined functions.",
   resourceLabel:"Khan Academy: Composite Functions", resourceUrl:"https://www.youtube.com/watch?v=z_tEsVMKOjk",
   quiz:[
     {q:"The domain of (f + g)(x) is ___.", options:["the domain of f only","the domain of g only","the domain of f union domain of g","the intersection of the domains of f and g — both must be defined"], answer:3},
     {q:"The domain of f(x) = √x and g(x) = 1/(x−2): find domain of f(g(x)).", options:["x > 0","x ≥ 2","x < 0","g(x) must be ≥ 0 for √g(x) to exist, so 1/(x−2) ≥ 0, meaning x > 2 (and x ≠ 2) — domain is x > 2"], answer:3},
     {q:"If f(x) = x² and g(x) = x + 1, then f(g(x)) − g(f(x)) = ___.", options:["0","x","(x+1)² − (x²+1) = x²+2x+1 − x²−1 = 2x","2x−2"], answer:2},
     {q:"The notation (f ∘ g)(x) means ___.", options:["f(x) × g(x)","f(x) + g(x)","f(x)/g(x)","f(g(x)) — apply g first, then f — the order matters and is read right to left in the composition notation"], answer:3},
     {q:"If f(x) = 2x − 1 and f(g(x)) = 2x + 3, then g(x) = ___.", options:["2x + 3","x + 3","x + 2 (since 2g(x) − 1 = 2x + 3 → 2g(x) = 2x + 4 → g(x) = x + 2)","x + 4"], answer:2}
   ]},
  {subject:"Calculus", title:"Applications of Derivatives: Tangent Lines and Related Rates", summary:"Students find equations of tangent and normal lines to curves, and solve introductory related rates problems.",
   resourceLabel:"Khan Academy: Tangent Line Equations", resourceUrl:"https://www.youtube.com/watch?v=IWcPMJBTDQg",
   quiz:[
     {q:"The equation of the tangent line to y = f(x) at (a, f(a)) is ___.", options:["y = f'(a)","y = f(a)(x − a)","y = f(a)x + b","y − f(a) = f'(a)(x − a) — point-slope form using the slope from the derivative"], answer:3},
     {q:"Find the tangent to y = x³ at x = 2.", options:["y = 3x − 2","y = 12x − 10 (slope = f'(2) = 3(4) = 12; point = (2, 8); y − 8 = 12(x − 2))","y = 12x + 8","y = 12x"], answer:1},
     {q:"The normal line to a curve at a point is ___.", options:["perpendicular to the curve at that point (slope = −1/f'(a))","parallel to the tangent","the tangent line reflected","the vertical line x = a"], answer:0},
     {q:"In related rates problems, you differentiate both sides of an equation with respect to ___.", options:["x only","both x and y","the dependent variable","time (t), using the chain rule to connect rates of change of related quantities"], answer:3},
     {q:"A spherical balloon is inflated so V = 500 cm³/s. Find dR/dt when R = 5 cm. (V = 4/3πR³)", options:["dR/dt = 500/(4πR²) = 500/(4π×25) = 5/π ≈ 1.59 cm/s","dR/dt = 500","dR/dt = 4πR²","dR/dt = V/(4πR) = 10/π"], answer:0}
   ]},
  {subject:"Physics", title:"Waves: Transverse, Longitudinal, and Sound", summary:"Students examine wave properties (wavelength, frequency, amplitude, speed), the wave equation, and properties of sound.",
   resourceLabel:"Crash Course Physics: Waves and Sound", resourceUrl:"https://www.youtube.com/watch?v=xLbZj5qO_lI",
   quiz:[
     {q:"The wave equation v = fλ relates ___.", options:["velocity to force and length","amplitude to frequency","wavelength to period only","wave speed to frequency and wavelength — doubling the frequency halves the wavelength for the same medium"], answer:3},
     {q:"Transverse waves differ from longitudinal waves in that ___.", options:["transverse waves are faster","transverse have no amplitude","transverse waves are only in vacuum","in transverse waves, particles vibrate perpendicular to the wave direction (e.g., light, water waves); in longitudinal waves, particles vibrate parallel to the direction of propagation (e.g., sound)"], answer:3},
     {q:"The Doppler effect explains why ___.", options:["sound cannot travel through air","waves cannot be reflected","the pitch of a police siren seems to change as it approaches and recedes — the source moves relative to the observer, compressing or stretching the wavelengths","light always appears red-shifted"], answer:2},
     {q:"Resonance occurs when ___.", options:["only destructive interference is possible","the driving frequency matches the object's natural frequency — producing maximum amplitude oscillations that can be very large (e.g., a singer breaking a glass, a bridge vibrating in wind)","all frequencies are absorbed equally","the amplitude becomes zero"], answer:1},
     {q:"The speed of sound in air at 20°C is approximately ___.", options:["3 × 10⁸ m/s (that is the speed of light)","150 m/s","1000 m/s","343 m/s — varies with temperature and medium (faster in warmer air and in liquids/solids than in air)"], answer:3}
   ]},
]},
{day:6, label:"Day 6 — Mon", subjects:[
  {subject:"English", title:"Literature: Poetry — The Lyric Tradition", summary:"Students study the development of the lyric poem from the Romantics through Modernism to contemporary practice, examining how lyric poetry constructs a speaking self and addresses fundamental human questions.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/c/TEDEd",
   quiz:[
     {q:"The lyric poem is distinguished by ___.", options:["always rhyming","always being about nature","always being short","its expression of personal feeling or thought through a speaking "I" — the lyric creates a sense of intimacy and presence, as if a thinking, feeling consciousness is directly addressed to us"], answer:3},
     {q:"Romanticism's influence on lyric poetry includes ___.", options:["rejection of all nature imagery","strict adherence to rational argument","avoidance of personal feeling","emphasis on individual imagination, emotional authenticity, the sublimity of nature, and the power of poetry to access truths unavailable to rational analysis"], answer:3},
     {q:"Modernist lyric poetry (Eliot, Yeats, Stevens) often uses ___.", options:["straightforward emotional expression","only traditional forms","only simple language","fragmentation, allusion, difficulty, and impersonality — the "persona" of the poem is often distanced or deliberately constructed, rejecting Romantic expressivism for a more ironic, cerebral stance"], answer:3},
     {q:"Contemporary lyric poetry engages with ___.", options:["only traditional subjects like love and death","only formal experimentation","only nature as a subject","a vast range of subjects and forms — from personal trauma and identity politics to ecological crisis and digital culture — often in hybrid forms mixing prose and verse"], answer:3},
     {q:"Close reading a lyric poem involves ___.", options:["only identifying the rhyme scheme","only determining whether the speaker is happy or sad","only summarising what the poem is about","attending to every word, sound, line break, and formal choice — lyric poetry is maximally compressed, so nothing is accidental"], answer:3}
   ]},
  {subject:"Advanced Functions", title:"Polynomial and Rational Equations: Problem Solving", summary:"Students solve higher-degree polynomial equations and applied rational equations, applying the factor theorem, synthetic division, and rational root theorem.",
   resourceLabel:"Khan Academy: Polynomial Division", resourceUrl:"https://www.youtube.com/watch?v=FxHWoUOq2iQ",
   quiz:[
     {q:"The Rational Root Theorem states ___.", options:["all roots of a polynomial are rational","irrational roots don't exist","a polynomial has n rational roots always","if P(x) has integer coefficients, any rational root p/q (in lowest terms) must have p dividing the constant term and q dividing the leading coefficient"], answer:3},
     {q:"For P(x) = 2x³ − 3x² − 11x + 6, possible rational roots are ___.", options:["±1, ±2, ±3, ±6 only","±1, ±2, ±3, ±6, ±1/2, ±3/2 (factors of 6 over factors of 2)","only positive integers","only ±1 and ±6"], answer:1},
     {q:"Testing P(1) = 2 − 3 − 11 + 6 = −6 ≠ 0; P(3) = 54 − 27 − 33 + 6 = 0. So ___.", options:["x = 3 is a root; divide to get 2x² + 3x − 2 = (2x−1)(x+2); all roots: x = 3, 1/2, −2","x = 3 only","x = 3 and x = 0","x = 1/2 and x = −2 only"], answer:0},
     {q:"Solving a rational inequality (e.g., (x−2)/(x+1) > 0) requires ___.", options:["multiplying both sides by (x+1)","squaring both sides","only testing x = 0","finding critical values (zeros and undefined points), then testing sign in each interval on a number line"], answer:3},
     {q:"For (x − 2)/(x + 1) > 0, the solution is ___.", options:["x > 2","x > 2 or x < −1 (positive/positive or negative/negative gives positive ratio)","−1 < x < 2","x < −1"], answer:1}
   ]},
  {subject:"Calculus", title:"Curve Sketching Using Derivatives", summary:"Students use the first and second derivative to identify increasing/decreasing intervals, local extrema, concavity, and inflection points.",
   resourceLabel:"Khan Academy: Curve Sketching", resourceUrl:"https://www.youtube.com/watch?v=WIDZFyfaT1I",
   quiz:[
     {q:"If f'(x) > 0 on an interval, then f ___.", options:["is concave up","has a minimum","is decreasing","is increasing on that interval"], answer:3},
     {q:"A local maximum at x = c requires ___.", options:["f'(c) > 0","f'(c) < 0","f'(c) = 0 only","f'(c) = 0 (or f'(c) undefined) AND f'changes from positive to negative — the first derivative test"], answer:3},
     {q:"The second derivative test: if f'(c) = 0 and f''(c) < 0, then ___.", options:["x = c is an inflection point","x = c is a local minimum","x = c is always a global maximum","x = c is a local maximum (concave down at c)"], answer:3},
     {q:"An inflection point occurs where ___.", options:["f = 0","f' = 0","the function has a maximum","f'' changes sign — concavity changes from up to down or down to up; the curve "bends the other way""], answer:3},
     {q:"A complete curve sketch using calculus includes ___.", options:["only zeros and asymptotes","only maxima and minima","domain, intercepts, asymptotes, increasing/decreasing intervals, local extrema, concavity, and inflection points — all derived algebraically before sketching"], answer:3}
   ]},
  {subject:"Physics", title:"Electricity: Electric Fields and Potential", summary:"Students analyse electric fields and electric potential produced by point charges and uniform fields, and relate electric potential to potential energy.",
   resourceLabel:"Crash Course Physics: Electric Fields", resourceUrl:"https://www.youtube.com/watch?v=mdulzEfQJP0",
   quiz:[
     {q:"The electric field E due to a point charge Q at distance r is ___.", options:["kQ/r","kQ²/r²","kQr²","kQ/r² directed away from positive charges (Coulomb's Law for field strength, by convention field points in the direction of force on a positive test charge)"], answer:3},
     {q:"Electric potential V at distance r from charge Q is ___.", options:["kQ/r² (same as field)","kQr","kQ²/r","kQ/r — a scalar (no direction), with potential energy U = qV for a charge q in the field"], answer:3},
     {q:"The relationship between electric field and electric potential is ___.", options:["E = V × r","E = V + r","E = V/r only in uniform fields","E = −dV/dx (in 1D) — the field is the negative gradient of the potential; field points from high to low potential"], answer:3},
     {q:"A positive charge released in a uniform electric field moves ___.", options:["toward lower potential (in the direction of E, which points from high to low potential)","toward higher potential","perpendicular to field lines","against the field direction"], answer:0},
     {q:"Electric field lines and equipotential surfaces are ___.", options:["parallel to each other","only drawn around conductors","the same thing drawn differently","always perpendicular — field lines show the direction of force on a positive charge; equipotential surfaces connect points of equal potential"], answer:3}
   ]},
]},
{day:7, label:"Day 7 — Tue", subjects:[
  {subject:"English", title:"Drama and Theatre: Contemporary Playwriting", summary:"Students read and analyse a contemporary Canadian play, examining how playwrights structure dramatic conflict, develop character through dialogue, and use theatrical space.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/c/TEDEd",
   quiz:[
     {q:"A contemporary Canadian play is likely to engage with ___.", options:["no Canadian themes","only historical events in theatrical form","only traditional dramatic forms","one or more of: Indigenous land rights and colonialism, immigration and multicultural identity, regional politics, environmental crisis, or LGBTQ+ experience — reflecting Canada's contemporary social landscape"], answer:3},
     {q:"Dialogue in drama does more than convey information — it ___.", options:["is always realistic conversation","only advances the plot","only establishes character mood","reveals character through what is said, what is NOT said, and HOW it is said; subtext (the meaning beneath the surface) is often more important than the words themselves"], answer:3},
     {q:"Non-realistic staging in contemporary theatre (abstract sets, stylised movement) ___.", options:["is always unsuccessful with audiences","requires no interpretation","is used to avoid the cost of realistic sets","creates meaning by refusing the illusion of realism — drawing attention to theatricality itself and inviting audiences to engage imaginatively rather than passively accept an illusion"], answer:3},
     {q:"Reading a play script for performance means ___.", options:["only reading the dialogue","only finding the themes","ignoring stage directions","imagining all dimensions: the spatial relationships, physicality, rhythm of speech, silences, and theatrical choices that a director, designer, and actors would bring to the text"], answer:3},
     {q:"Theatre's unique power compared to film or prose is ___.", options:["better special effects","permanent record of performance","greater budget for production design","liveness — the co-presence of performer and audience creates an unrepeatable event, a shared experience of risk and immediacy that no recording can replicate"], answer:3}
   ]},
  {subject:"Advanced Functions", title:"Rates of Change: Introduction to Calculus Concepts", summary:"Students explore the concept of instantaneous rate of change as a limit, preparing the foundation for Grade 12 Calculus and making explicit the connection between Advanced Functions and Calculus.",
   resourceLabel:"Khan Academy: Average vs Instantaneous Rate of Change", resourceUrl:"https://www.youtube.com/watch?v=BVZNMm6GaKw",
   quiz:[
     {q:"Average rate of change of f(x) over [a, b] is ___.", options:["f'(a)","f(a)/f(b)","[f(b) − f(a)] × (b − a)","[f(b) − f(a)]/(b − a) — the slope of the secant line through (a, f(a)) and (b, f(b))"], answer:3},
     {q:"Instantaneous rate of change at x = a is ___.", options:["[f(b)−f(a)]/(b−a) for any b","f(a)/a","f(a+1) − f(a)","lim(h→0)[f(a+h) − f(a)]/h — the slope of the tangent line at a, i.e., the derivative f'(a)"], answer:3},
     {q:"If f(x) = x², the average rate of change on [2, 2+h] is ___.", options:["4 + h (= [f(2+h) − f(2)]/h = [(2+h)² − 4]/h = [4+4h+h²−4]/h = 4+h)","2h","4h","4 + 2h"], answer:0},
     {q:"As h → 0 in the expression (4 + h), the instantaneous rate of change at x = 2 is ___.", options:["4 — confirming f'(x) = 2x, f'(2) = 4","2h","h","0"], answer:0},
     {q:"Understanding rate of change prepares you for calculus by ___.", options:["replacing all calculus learning","making calculus unnecessary","only being relevant in physics","establishing the limit concept — derivatives are defined as limits of difference quotients, so deep understanding of rates of change makes the formal definition of derivative intuitive rather than arbitrary"], answer:3}
   ]},
  {subject:"Calculus", title:"Optimisation: Maximum and Minimum Problems", summary:"Students apply derivatives to find maximum and minimum values in applied context problems — geometry, economics, and physics.",
   resourceLabel:"Khan Academy: Optimization Problems", resourceUrl:"https://www.youtube.com/watch?v=bG1v9tGTIZk",
   quiz:[
     {q:"To solve an optimisation problem with calculus, the steps are ___.", options:["sketch and guess","differentiate directly without identifying the function","only apply the second derivative test","define variables and constraints, write the objective function (what to optimise), reduce to one variable using constraints, differentiate, set to zero, find candidates, verify global extremum"], answer:3},
     {q:"A farmer has 200 m of fencing to enclose a rectangular field against a barn (one side free). Maximise the area. If x is the side away from the barn:", options:["A = 200x − 2x², A'= 200 − 4x = 0, x = 50, width = 100, A_max = 5000 m²","A = x × 200 − x","x = 100 gives maximum","x = 50 and area = 50 × 100 = 5000 m²"], answer:0},
     {q:"The second derivative test confirms a maximum when ___.", options:["f''(c) = 0","f''(c) is undefined","f''(c) > 0 (concave up — local minimum)","f''(c) < 0 (concave down at the critical point — local maximum)"], answer:3},
     {q:"In an optimisation problem, endpoints of the domain must be checked because ___.", options:["endpoints always give extrema","critical points are always the answer","global extrema only occur at critical points","the global maximum or minimum may occur at an endpoint of the feasible domain, not at an interior critical point"], answer:3},
     {q:"Optimisation in real life includes ___.", options:["only mathematical problems","no economic applications","only geometric problems","minimising cost, maximising revenue, finding the most efficient shape for a container, minimising material use, maximising the strength of a structure — calculus is the tool of choice"], answer:3}
   ]},
  {subject:"Physics", title:"Electric Circuits: Current, Resistance, and Ohm's Law", summary:"Students analyse DC electric circuits — current, voltage, resistance, Ohm's Law, series and parallel circuits, and power dissipation.",
   resourceLabel:"Crash Course Physics: Electric Circuits", resourceUrl:"https://www.youtube.com/watch?v=g-wjP1otQWI",
   quiz:[
     {q:"Ohm's Law states ___.", options:["V = IR²","R = V × I","I = V + R","V = IR — voltage equals current times resistance; a linear relationship for ohmic conductors"], answer:3},
     {q:"In a series circuit, ___.", options:["voltage is the same across all components","resistance decreases","current divides","current is the same through all components; total resistance = sum of individual resistances; voltage divides"], answer:0},
     {q:"In a parallel circuit, ___.", options:["voltage divides across branches","current is the same in all branches","total resistance is the sum of all resistances","voltage is the same across all branches; current divides; 1/R_total = 1/R₁ + 1/R₂ + ..."], answer:3},
     {q:"Power dissipated in a resistor is ___.", options:["P = I/R","P = IR²","P = V/I","P = IV = I²R = V²/R — three equivalent expressions, all valid for any resistor obeying Ohm's Law"], answer:3},
     {q:"Adding a resistor in parallel to a circuit ___.", options:["increases total resistance","doesn't affect total resistance","only changes the voltage","decreases total resistance — 1/R_total = 1/R₁ + 1/R₂ means R_total is always less than either individual resistance"], answer:3}
   ]},
]},
{day:8, label:"Day 8 — Wed", subjects:[
  {subject:"English", title:"Writing: The University Application Process and Personal Writing", summary:"Students write personal statements and supplementary essays for university applications, applying their Grade 12 writing skills to genuine high-stakes contexts.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/c/TEDEd",
   quiz:[
     {q:"A university personal statement is most effective when ___.", options:["it lists every achievement in your life","it sounds like every other applicant","it focuses only on grades","it reveals how you think — through a specific story or question that shows your intellectual curiosity, growth, and genuine engagement with ideas"], answer:3},
     {q:"Showing rather than telling in a personal statement means ___.", options:["never making claims about yourself","avoiding personal stories","only using achievements","instead of saying "I am passionate about biology," describing the specific moment, question, or observation that sparked that passion — concrete specificity is more persuasive than self-description"], answer:3},
     {q:"Tailoring a supplementary essay to a specific university or program requires ___.", options:["copying your main personal statement","generic statements about the school","avoiding mention of specific courses","genuine research — knowing specific programs, professors, courses, or approaches at that institution and explaining how they connect to your specific intellectual interests"], answer:3},
     {q:"The most common fatal flaw in university personal writing is ___.", options:["being too specific","mentioning personal interests","having too unique a perspective","being generic — writing could apply to any student, at any school, in any program — producing no sense of who this specific person is or why this specific school is right for them"], answer:3},
     {q:"Your personal statement is most valuable to you personally because ___.", options:["it guarantees admission","it impresses admission officers","only the grade matters","it requires you to reflect seriously on who you are, what you care about, and where you want to go — the act of writing it is itself valuable, not just the finished product"], answer:3}
   ]},
  {subject:"Advanced Functions", title:"Discrete Functions: Advanced Sequences, Series, and Financial Math", summary:"Students apply geometric series formulas to financial mathematics — annuities, mortgages, and investment growth — with university-preparatory rigour.",
   resourceLabel:"Khan Academy: Geometric Series Formula", resourceUrl:"https://www.youtube.com/watch?v=RMa1QSEfzVA",
   quiz:[
     {q:"The future value of an annuity (regular payment R, interest rate i per period, n periods) is ___.", options:["FV = R × n","FV = R(1+i)ⁿ","FV = R × i × n","FV = R[(1+i)ⁿ − 1]/i — a geometric series: each payment earns compound interest for a different number of periods"], answer:3},
     {q:"If you invest $200/month at 6%/year (0.5%/month) for 30 years, the future value is ___.", options:["200 × 360 = $72,000","$200 × (1.005)^360","200[(1.005)^360 − 1]/0.005 ≈ $200,903 — compound interest dramatically amplifies regular saving","200 × 0.005 × 360"], answer:2},
     {q:"The present value of an annuity formula is ___.", options:["PV = R × n","PV = R/i","PV = R(1+i)ⁿ/i","PV = R[1 − (1+i)^(−n)]/i — how much a series of future payments is worth today"], answer:3},
     {q:"A mortgage is a ___.", options:["future value of an annuity problem","growing annuity","perpetuity","present value of an annuity problem — the loan amount is the PV; monthly payments are R; solving for R gives the payment size"], answer:3},
     {q:"The formula for present value of a perpetuity (payment R, rate i, forever) is ___.", options:["PV = Ri","PV = R × ∞","PV = R/i — as n → ∞ in the annuity formula, (1+i)^(−n) → 0","PV = R(1+i)/i"], answer:2}
   ]},
  {subject:"Calculus", title:"Integration: The Antiderivative and Indefinite Integrals", summary:"Students are introduced to integration as the reverse of differentiation, applying the power rule for integration and the constant of integration.",
   resourceLabel:"Khan Academy: Antiderivatives and Indefinite Integrals", resourceUrl:"https://www.youtube.com/watch?v=mB7DGEMb0og",
   quiz:[
     {q:"The antiderivative (indefinite integral) of f(x) is ___.", options:["f'(x)","f(x) − C","f(x)²/2","F(x) such that F'(x) = f(x); written ∫f(x)dx = F(x) + C where C is the constant of integration"], answer:3},
     {q:"The power rule for integration: ∫xⁿ dx = ___.", options:["xⁿ/n + C","nxⁿ⁻¹","xⁿ⁺¹ + C","xⁿ⁺¹/(n+1) + C for n ≠ −1"], answer:3},
     {q:"∫(3x² − 4x + 5) dx = ___.", options:["6x − 4","3x³ − 4x² + 5x","x³ − 2x² + 5x + C","x³ − 2x² + 5x + C — integrate term by term using the power rule"], answer:3},
     {q:"The constant of integration C appears because ___.", options:["integration is imprecise","every integral is different","C equals zero always","any constant differentiates to zero, so infinitely many functions have the same derivative — C represents the "lost" information about the original function's vertical shift"], answer:3},
     {q:"∫sin(x) dx = ___.", options:["cos(x) + C","−cos(x) + C — since d/dx[−cos(x)] = sin(x)","sin(x) + C","−sin(x) + C"], answer:1}
   ]},
  {subject:"Physics", title:"Magnetic Fields and Forces", summary:"Students examine magnetic fields produced by current-carrying conductors, and the force on a current or moving charge in a magnetic field.",
   resourceLabel:"Crash Course Physics: Magnetic Fields", resourceUrl:"https://www.youtube.com/watch?v=s94suB5uLWw",
   quiz:[
     {q:"The force on a charge q moving with velocity v in a magnetic field B is ___.", options:["F = qvB (this is the magnitude when v ⊥ B)","F = qB/v","F = mv/qB","F = qv × B (vector cross product) — magnitude F = qvB sinθ, direction given by the right-hand rule"], answer:3},
     {q:"A charged particle moving perpendicular to a uniform magnetic field follows ___.", options:["a straight line","a parabolic path","a spiral path along B","a circular path — the magnetic force is always perpendicular to velocity, providing centripetal force without doing work"], answer:3},
     {q:"The force on a current-carrying wire of length L in field B (current I, angle θ) is ___.", options:["F = IL/B","F = IB/L","F = I/LB","F = BIL sinθ — the force on a current equals the force on the moving charges per unit length times the length"], answer:3},
     {q:"Two parallel wires carrying current in the same direction ___.", options:["repel each other","do not exert forces on each other","rotate around each other","attract each other — the magnetic field of each wire exerts an attractive force on the current in the other"], answer:3},
     {q:"The right-hand rule for a solenoid: point fingers in the direction of current wrap, thumb points ___.", options:["in the direction of current flow","toward the south pole","at 90° to field","toward the north pole — the solenoid's magnetic field inside points in the direction of the thumb"], answer:3}
   ]},
]},
{day:9, label:"Day 9 — Thu", subjects:[
  {subject:"English", title:"Independent Reading: Postmodern Literature", summary:"Students read a postmodern novel or short fiction collection, examining metafiction, fragmentation, unreliable narration, and postmodern challenges to stable meaning.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/c/TEDEd",
   quiz:[
     {q:"Postmodern literature challenges ___.", options:["all previous narrative techniques without exception","only the use of irony","the idea that literature can accurately represent reality","the concepts of stable, knowable truth and coherent identity — postmodern texts often question the authority of the narrator, the reliability of language, and the very possibility of authentic selfhood"], answer:3},
     {q:"Metafiction is ___.", options:["fiction about real events presented as fiction","only experimental prose poetry","only found in postmodern novels","fiction that self-consciously draws attention to its own artifice — reminding readers they are reading a constructed text, often by having narrators comment on the act of storytelling"], answer:3},
     {q:"Intertextuality in postmodern fiction means ___.", options:["plagiarism from other works","only references to classical literature","only quoting other texts directly","the way a text is built from and in dialogue with other texts — quotations, allusions, parody, pastiche — blurring the boundaries between "original" and "borrowed" material"], answer:3},
     {q:"Pastiche differs from parody in that ___.", options:["pastiche has no relationship to prior works","pastiche is always comic","they are identical","pastiche imitates a style without the critical distance of parody — it celebrates or mourns a style rather than mocking it; Fredric Jameson saw pastiche as the dominant mode of postmodern culture"], answer:3},
     {q:"Reading postmodern fiction productively requires ___.", options:["abandoning all interpretive frameworks","accepting that meaning is completely arbitrary","only reading plot summaries","tolerating and enjoying ambiguity — learning to read with pleasure the way meaning is deferred, multiplied, and complicated rather than seeking a definitive single meaning"], answer:3}
   ]},
  {subject:"Advanced Functions", title:"Introduction to Vectors", summary:"Students are introduced to vectors — geometric and component representations, operations, dot product, and applications to displacement and work.",
   resourceLabel:"Khan Academy: Vectors Introduction", resourceUrl:"https://www.youtube.com/watch?v=fNk_zzaMoSs",
   quiz:[
     {q:"A vector differs from a scalar in that ___.", options:["vectors are always larger","vectors have no application in physics","scalars can be negative","a vector has both magnitude and direction (e.g., displacement, velocity, force); a scalar has only magnitude (e.g., distance, speed, mass)"], answer:3},
     {q:"Two vectors a = (a₁, a₂) and b = (b₁, b₂) are added by ___.", options:["multiplying components","taking the average of each component","subtracting components","adding corresponding components: a + b = (a₁+b₁, a₂+b₂) — equivalent to the geometric tip-to-tail rule"], answer:3},
     {q:"The dot product a · b = ___.", options:["|a| × |b| (this is only the magnitude part)","a₁b₂ + a₂b₁","a × b (vector cross product)","a₁b₁ + a₂b₂ = |a||b|cosθ — a scalar that captures the "same-direction" component of two vectors"], answer:3},
     {q:"Two vectors are perpendicular if and only if ___.", options:["their magnitudes are equal","one has zero magnitude","they are in the same direction","their dot product equals zero — cosθ = 0 when θ = 90°"], answer:3},
     {q:"The work done by force F over displacement d is ___.", options:["F × d (scalar)","F + d","|F| × |d|","W = F · d = |F||d|cosθ — work is the dot product; only the component of force in the direction of displacement does work"], answer:3}
   ]},
  {subject:"Calculus", title:"Definite Integrals and the Fundamental Theorem of Calculus", summary:"Students compute definite integrals, apply the Fundamental Theorem of Calculus, and interpret definite integrals as areas.",
   resourceLabel:"Khan Academy: Fundamental Theorem of Calculus", resourceUrl:"https://www.youtube.com/watch?v=9vgCMNHPScU",
   quiz:[
     {q:"The Fundamental Theorem of Calculus Part 1 states ___.", options:["integration and differentiation are unrelated","∫f(x)dx can only be approximated","∫f(x)dx from a to a equals 1","if F'(x) = f(x), then ∫[a to b]f(x)dx = F(b) − F(a) — connecting the antiderivative to the area under the curve"], answer:3},
     {q:"The definite integral ∫[a to b]f(x)dx represents ___.", options:["f(b) − f(a)","the derivative of f at the midpoint","the net signed area between the curve y = f(x) and the x-axis from x = a to x = b (negative where f is below the x-axis)","the average value of f"], answer:2},
     {q:"∫[0 to 3](2x + 1)dx = ___.", options:["[x² + x] from 0 to 3 = (9+3) − (0+0) = 12","2x² + x","3 × 3 = 9","6"], answer:0},
     {q:"FTC Part 2 (Leibniz Rule): d/dx[∫[a to x]f(t)dt] = ___.", options:["∫[a to x]f'(t)dt","F(x) − F(a)","f(x) − f(a)","f(x) — differentiating the area function recovers the original integrand"], answer:3},
     {q:"The area between two curves f(x) and g(x), where f ≥ g, from a to b is ___.", options:["∫[a to b]f(x)dx − ∫[a to b]g(x)dx = ∫[a to b][f(x) − g(x)]dx","∫f(x) × g(x)dx","∫f(x)dx × ∫g(x)dx","[f(b)−g(b)] − [f(a)−g(a)]"], answer:0}
   ]},
  {subject:"Physics", title:"Electromagnetic Induction", summary:"Students examine Faraday's Law of electromagnetic induction, Lenz's Law, and applications including transformers and generators.",
   resourceLabel:"Crash Course Physics: Electromagnetic Induction", resourceUrl:"https://www.youtube.com/watch?v=pQp6bmJPU_0",
   quiz:[
     {q:"Faraday's Law states that an EMF is induced in a conductor when ___.", options:["current flows through it","it is heated","it is placed in a constant magnetic field","the magnetic flux through it changes — the induced EMF equals the rate of change of flux: EMF = −dΦ/dt"], answer:3},
     {q:"Lenz's Law states that the induced current flows in a direction that ___.", options:["amplifies the change causing it","has no relation to the cause","is always clockwise","opposes the change in magnetic flux — a consequence of energy conservation: the induced current always acts to maintain the existing flux"], answer:3},
     {q:"An electric generator works by ___.", options:["converting electrical energy to mechanical energy (that is a motor)","using a battery to create magnetic flux","using nuclear fusion","rotating a coil in a magnetic field — changing magnetic flux induces an EMF, converting mechanical energy to electrical energy"], answer:3},
     {q:"A transformer steps up voltage by ___.", options:["using stronger magnets","using DC current (transformers require AC)","having fewer primary turns","having more secondary turns than primary turns — V_s/V_p = N_s/N_p; stepping up voltage steps down current (power conservation: V_p I_p = V_s I_s)"], answer:3},
     {q:"The reason high-voltage transmission lines are used to send electricity across long distances is ___.", options:["high voltage is safer","high voltage doesn't need towers","only historical convention","at high voltage, the current is lower (P = IV), so power loss (P_loss = I²R) in the wires is minimised — transformers make this practical with AC"], answer:3}
   ]},
]},
{day:10, label:"Day 10 — Fri", subjects:[
  {subject:"English", title:"Literature: Comparative Canadian and World Literature", summary:"Students compare Canadian literature with a world text, analysing how place, history, and culture shape literary form and theme.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/c/TEDEd",
   quiz:[
     {q:"Comparative literature across cultures reveals ___.", options:["only surface-level differences","only surface-level similarities","that all literature is the same beneath cultural differences","both universal human concerns (love, death, justice, belonging) and radically different ways of understanding and representing those concerns — the comparison enriches both texts"], answer:3},
     {q:"Canadian literature is shaped by ___.", options:["only multiculturalism","only Quebec-English tensions","only the landscape","a unique combination of colonial history, vast geography, proximity to the US, two official languages, Indigenous presence, and ongoing waves of immigration — producing a literature of settlement, survival, and identity"], answer:3},
     {q:"The concept of "writing back" (from post-colonial theory) means ___.", options:["only Indigenous writing","answering letters","only about rejecting Western literature","texts from formerly colonised cultures engaging with, subverting, or transforming the literary traditions of the colonising culture — rewriting familiar narratives from marginalised perspectives"], answer:3},
     {q:"A sophisticated comparison of two texts examines ___.", options:["only their plots","only their dates of publication","only whether one is better than the other","how each text's formal choices, cultural context, and thematic concerns illuminate the other — finding meaningful connections and tensions that reveal something about both"], answer:3},
     {q:"The value of global and comparative literature for Canadian students is ___.", options:["only preparation for international travel","only useful for English majors","no connection to Canadian identity","it places Canada in a global conversation — students discover both what is distinctive about Canadian literature and what connects it to the broader human story"], answer:3}
   ]},
  {subject:"Advanced Functions", title:"Proof and Mathematical Reasoning", summary:"Students examine mathematical proof — direct proof, proof by contradiction, and mathematical induction — developing the formal reasoning skills required for university mathematics.",
   resourceLabel:"Khan Academy: Mathematical Induction", resourceUrl:"https://www.youtube.com/watch?v=wblW_M_HVQ8",
   quiz:[
     {q:"A direct proof establishes a theorem by ___.", options:["testing many specific cases","showing the opposite leads to a contradiction","finding a counterexample","starting from known axioms and definitions, and deriving the theorem through valid logical steps"], answer:3},
     {q:"Proof by contradiction assumes ___.", options:["the theorem is trivially true","the opposite of the theorem, then derives a logical impossibility — proving the original theorem must be true","only that algebra is valid","the theorem is sometimes false"], answer:1},
     {q:"Mathematical induction proves a statement P(n) for all n ≥ 1 by ___.", options:["checking P(n) for n = 1 to 100","proving P(n) is true for some large n","only checking P(1)","proving P(1) (base case) and proving that if P(k) is true, then P(k+1) is also true (inductive step) — together, these imply P(n) is true for all n"], answer:3},
     {q:"Use induction to prove 1 + 2 + ... + n = n(n+1)/2. The inductive step shows: if 1+...+k = k(k+1)/2, then 1+...+k+(k+1) = ___.", options:["k(k+1)/2 + (k+1) = (k+1)(k+2)/2 — which is the formula for n = k+1 ✓","k²+k/2","k(k+1)","(k+1)(k+1)/2"], answer:0},
     {q:"A single counterexample ___.", options:["proves a theorem in all other cases","has no significance in mathematics","strengthens a theorem by eliminating one case","disproves a universal statement ("for all n, P(n)") — you only need one example where the statement fails to prove it is not universally true"], answer:3}
   ]},
  {subject:"Calculus", title:"Applications of Integration: Area and Volume", summary:"Students calculate areas under curves, between curves, and volumes of solids of revolution.",
   resourceLabel:"Khan Academy: Volume of Solids of Revolution", resourceUrl:"https://www.youtube.com/watch?v=R_aqSL-q6_8",
   quiz:[
     {q:"The area between y = x² and y = x from 0 to 1 is ___.", options:["∫[0 to 1](x − x²)dx = [x²/2 − x³/3] from 0 to 1 = 1/2 − 1/3 = 1/6","∫x² dx","1/4 − 1/3 = −1/12","1 − 1/3 = 2/3"], answer:0},
     {q:"The disc method for volume of revolution around the x-axis gives ___.", options:["V = 2π∫x f(x)dx","V = π∫[f(x)]² dx from a to b — summing circular cross-sections of radius f(x)","V = ∫f(x)dx","V = π∫f(x)dx"], answer:1},
     {q:"The shell method for volume rotated around the y-axis gives ___.", options:["V = π∫f(x)²dx","V = ∫f(x)dx","V = 2π∫x f(x)dx from a to b — summing cylindrical shell volumes","V = 2∫f(x)dx"], answer:2},
     {q:"Find the volume when y = √x from 0 to 4 is rotated around the x-axis.", options:["V = π∫[0 to 4](√x)² dx = π∫[0 to 4]x dx = π[x²/2] from 0 to 4 = 8π","V = π × 4","V = 4π","V = 16π"], answer:0},
     {q:"Applications of integration in real life include ___.", options:["no applications outside mathematics","only physics problems","only area under parabolas","probability distributions, finding work done by variable forces, computing areas of irregular shapes, and calculating volumes of any solid with known cross-sections"], answer:3}
   ]},
  {subject:"Physics", title:"Modern Physics: Special Relativity", summary:"Students examine Einstein's special relativity — postulates, time dilation, length contraction, mass-energy equivalence, and experimental evidence.",
   resourceLabel:"Crash Course Physics: Special Relativity", resourceUrl:"https://www.youtube.com/watch?v=AInCqm5nCzw",
   quiz:[
     {q:"Einstein's two postulates of special relativity are ___.", options:["matter is energy; time is space","gravity warps space; light bends around mass","only one is needed","(1) the laws of physics are identical in all inertial frames; (2) the speed of light c is constant in all inertial frames regardless of source or observer motion"], answer:3},
     {q:"Time dilation means ___.", options:["clocks in motion run faster","time passes at the same rate for all observers","only GPS satellites are affected","a clock in motion relative to an observer runs slower than one at rest — the moving clock measures less elapsed time: Δt' = γΔt₀ where γ = 1/√(1 − v²/c²)"], answer:3},
     {q:"Length contraction means ___.", options:["objects appear smaller due to perspective","only length perpendicular to motion contracts","all lengths change equally","objects moving at speed v appear shorter along the direction of motion: L = L₀/γ — at relativistic speeds objects are compressed in the direction of travel"], answer:3},
     {q:"E = mc² means ___.", options:["mass and energy are always the same","only radioactive materials have rest energy","nuclear energy is impossible to harness","mass is a form of energy — a tiny mass corresponds to enormous energy (c² ≈ 9 × 10¹⁶ J/kg); this equivalence explains nuclear energy and pair production"], answer:3},
     {q:"Evidence for special relativity includes ___.", options:["no experimental evidence exists","only thought experiments","only GPS corrections","muon lifetime: muons created in upper atmosphere have insufficient lifetime to reach Earth at c — but time dilation means they age slowly relative to us, and we observe them at sea level"], answer:3}
   ]},
]},
{day:11, label:"Day 11 — Mon", subjects:[
  {subject:"English", title:"Writing: The Argumentative Essay on a Social Issue", summary:"Students write a well-researched argumentative essay on a contemporary social or political issue, integrating sources, acknowledging counterarguments, and making an original contribution.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/c/TEDEd",
   quiz:[
     {q:"A strong argumentative essay on a social issue must ___.", options:["avoid all statistics","only present one side","include emotional appeals only","engage with the strongest version of the opposing view (steelmanning), not a weak caricature — and explain why your position is more defensible despite the counterargument"], answer:3},
     {q:"Reliable sources for a social issues essay include ___.", options:["only news sources you agree with","any website with "org" in the domain","only primary sources","peer-reviewed research, government data, established journalism organisations, expert commentary, and primary sources — evaluated for methodology, transparency, and independence"], answer:3},
     {q:"Correlation vs. causation in social science arguments: finding that A and B are correlated means ___.", options:["A always causes B","B must cause A","they are not related","A and B vary together, but this could be because A causes B, B causes A, a third factor causes both, or the correlation is coincidental — more evidence is needed to establish causation"], answer:3},
     {q:"Academic integrity in a social issues essay requires ___.", options:["only using your own knowledge","only paraphrasing to avoid citation","never using sources","citing all sources of information, ideas, and argument (whether quoted or paraphrased), distinguishing your own claims from sourced claims, and being transparent about the evidential basis of all arguments"], answer:3},
     {q:"The most important quality of an argumentative essay on a controversial topic is ___.", options:["passionate expression of opinion","length and number of sources","an absence of counterarguments","intellectual honesty — acknowledging uncertainty where it exists, representing opposing views fairly, and grounding your argument in evidence rather than only in conviction"], answer:3}
   ]},
  {subject:"Advanced Functions", title:"Functions Review: Connecting All Function Families", summary:"Students synthesise the entire Advanced Functions course, connecting all function families and preparing for final assessment.",
   resourceLabel:"Khan Academy: Advanced Functions Review", resourceUrl:"https://www.youtube.com/watch?v=LkwT1GQVJP8",
   quiz:[
     {q:"The fundamental difference between polynomial and rational functions is ___.", options:["degree only","number of terms","they are always different in shape","rational functions involve division by a variable expression, creating domain restrictions (vertical asymptotes or holes) absent in polynomials"], answer:3},
     {q:"Exponential and logarithmic functions are most important because ___.", options:["they are easy to calculate","they are aesthetically pleasing","they model phenomena that are only approximately linear","they model phenomena where a constant percentage change occurs per unit time — population growth, radioactive decay, compound interest, pH, the Richter scale"], answer:3},
     {q:"Trigonometric functions are unique among function families in that ___.", options:["they only model sound","they have no algebraic properties","they are only defined for angles","they are periodic — they repeat their values at regular intervals, making them essential for modelling oscillatory and cyclical phenomena throughout physics and engineering"], answer:3},
     {q:"Vector operations extend functions by ___.", options:["adding direction to algebra","eliminating scalar quantities","replacing all other functions","allowing mathematical description of quantities that have both magnitude and direction — force, displacement, velocity — enabling 2D and 3D physics and geometry"], answer:3},
     {q:"A student who has mastered Advanced Functions can ___.", options:["only solve the types of problems they've seen before","not extend to calculus","only work in pure mathematics","see a mathematical relationship and immediately identify: what type of function? What are its key features? What algebraic technique applies? What does its graph look like? — fluent pattern recognition across all function families"], answer:3}
   ]},
  {subject:"Calculus", title:"Calculus of Exponential and Logarithmic Functions", summary:"Students differentiate and integrate e^(ax), ln(x), and related functions, and apply these to growth/decay problems.",
   resourceLabel:"Khan Academy: Derivatives of Exponential Functions", resourceUrl:"https://www.youtube.com/watch?v=MKQR_acrFOA",
   quiz:[
     {q:"d/dx[e^(ax)] = ___.", options:["ae^x","e^(ax)","a × e^(ax) — chain rule: derivative of outer (e^u) times derivative of inner (a)","e^(ax)/a"], answer:2},
     {q:"d/dx[ln(ax)] = ___.", options:["a/x","ln(a)/x","a × ln(x)","1/x — since ln(ax) = ln(a) + ln(x), and ln(a) is a constant with derivative 0"], answer:3},
     {q:"∫e^(3x) dx = ___.", options:["3e^(3x) + C","e^(3x)/3 + C — anti-chain-rule: divide by the inner derivative","e^(3x) + C","3e^x + C"], answer:1},
     {q:"∫(1/x) dx = ___.", options:["x^(−2)/(−2) + C","undefined","−1/x² + C","ln|x| + C — the integral of 1/x is the natural log (valid for x > 0; the absolute value handles x < 0)"], answer:3},
     {q:"A population grows at a rate proportional to its size: dP/dt = kP. The solution is ___.", options:["P(t) = P₀ + kt","P(t) = P₀e^(kt) — solving the separable differential equation dP/P = k dt → ln P = kt + C → P = P₀e^(kt)","P(t) = P₀(kt)","P(t) = ke^(P₀t)"], answer:1}
   ]},
  {subject:"Physics", title:"Nuclear Physics and Elementary Particles", summary:"Students examine nuclear reactions (fission and fusion), binding energy, and an introduction to the Standard Model of particle physics.",
   resourceLabel:"Crash Course Physics: Nuclear Physics", resourceUrl:"https://www.youtube.com/watch?v=nRmBsxBpTjs",
   quiz:[
     {q:"Nuclear fission involves ___.", options:["combining light nuclei to form heavier ones","radioactive beta decay","only gamma emission","splitting a heavy nucleus (e.g., U-235) into two smaller nuclei, releasing neutrons and a large amount of energy — exploited in nuclear reactors and weapons"], answer:3},
     {q:"Nuclear fusion involves ___.", options:["splitting heavy nuclei","only proton-electron collisions","no energy release","combining light nuclei (e.g., hydrogen isotopes) to form a heavier nucleus, releasing enormous energy — the process powering stars and pursued for clean energy on Earth"], answer:3},
     {q:"Mass defect and binding energy: the mass of a nucleus is ___.", options:["equal to the sum of its parts","greater than the sum of its parts","impossible to measure","slightly less than the sum of its constituent protons and neutrons — the "missing" mass is the binding energy (E = mc²): this is the energy released when the nucleus forms"], answer:3},
     {q:"The Standard Model of particle physics describes ___.", options:["only the structure of atoms","only electromagnetic forces","only gravity and electromagnetism","the fundamental particles (quarks, leptons) and forces (electromagnetic, strong nuclear, weak nuclear) that make up all matter — gravity is not yet unified in the Standard Model"], answer:3},
     {q:"The Higgs boson, discovered in 2012, is significant because ___.", options:["it creates all mass in the universe","it is the force carrier of gravity","it was already predicted by general relativity","it is the field particle associated with the Higgs field, which gives fundamental particles their mass — confirming the Standard Model's prediction after 50 years of searching"], answer:3}
   ]},
]},
{day:12, label:"Day 12 — Tue", subjects:[
  {subject:"English", title:"Media: Creating a Digital Portfolio", summary:"Students curate, design, and reflect on a digital portfolio of their best work across Grade 12, developing skills in curation, self-presentation, and digital literacy.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/c/TEDEd",
   quiz:[
     {q:"A digital portfolio differs from a print portfolio in that ___.", options:["it is always better","it can include only digital work","it never includes reflection","it can be hyperlinked, multimedia, and publicly accessible — connecting written work to visual, audio, and video media in ways a print portfolio cannot"], answer:3},
     {q:"Curating a portfolio requires ___.", options:["including everything you've produced","only including error-free work","only including the most recent work","deliberate selection based on criteria: which pieces best demonstrate your range, growth, and strongest capabilities — curation is itself a creative and analytical act"], answer:3},
     {q:"The reflective statement in a portfolio item ___.", options:["describes what grade you received","only explains what the piece is about","is optional and minor","explains why you selected this piece, what it demonstrates about your thinking and skills, and what you would do differently — metacognition applied to writing"], answer:3},
     {q:"Designing a digital portfolio involves ___.", options:["only choosing a colour scheme","no aesthetic choices","no connection to writing skills","decisions about organisation, hierarchy, visual design, and navigation that reflect the same principles as good writing: clarity, purpose, coherence, and attention to audience"], answer:3},
     {q:"The most important quality in a digital portfolio for university or career purposes is ___.", options:["the most elaborate visual design","only the most technical work","as many pieces as possible","authentic evidence of your thinking — not just correct answers but genuine intellectual engagement, growth, and the distinctive qualities of your mind"], answer:3}
   ]},
  {subject:"Advanced Functions", title:"Exam Preparation: Comprehensive Review", summary:"Students complete comprehensive review of all Advanced Functions content in preparation for final assessment.",
   resourceLabel:"Khan Academy: Advanced Math Review", resourceUrl:"https://www.youtube.com/watch?v=jKrEFOTScwU",
   quiz:[
     {q:"Find all zeros of P(x) = x⁴ − 5x² + 4.", options:["x = ±1 and x = ±2 (factor as (x²−1)(x²−4) = (x−1)(x+1)(x−2)(x+2))","x = 1 and x = 4 only","x = ±2 only","x = ±√5"], answer:0},
     {q:"Solve log₃(x + 2) + log₃(x) = 2.", options:["x = 1 (log₃(x(x+2)) = 2 → x²+2x = 9 → x²+2x−9 = 0... wait: x²+2x = 9 → x = (−2+√40)/2 ≈ 1.16; let me use exact: x²+2x−9=0 → x = (−2+√40)/2)","x = 3","x = 9","x = 7"], answer:0},
     {q:"The graph of f(x) = (x²−9)/(x−3) has ___.", options:["a vertical asymptote at x = 3","a zero at x = −3 and a hole at x = 3 (since (x²−9) = (x−3)(x+3), the (x−3) cancels leaving x+3 with a hole at x=3)","a zero at x = 3","asymptotes at x = 3 and x = −3"], answer:1},
     {q:"A vector a = (3, −4) has magnitude ___.", options:["7","1","√7","5 (|a| = √(9+16) = √25 = 5)"], answer:3},
     {q:"For a geometric series with t₁ = 2, r = −1/2, find S∞.", options:["4/3 (S∞ = t₁/(1−r) = 2/(1+1/2) = 2/(3/2) = 4/3)","2","4","1"], answer:0}
   ]},
  {subject:"Calculus", title:"Differential Equations: Separable and Initial Value Problems", summary:"Students solve separable differential equations and apply them to growth, decay, and Newton's Law of Cooling.",
   resourceLabel:"Khan Academy: Separable Differential Equations", resourceUrl:"https://www.youtube.com/watch?v=H0VEL9TFjqw",
   quiz:[
     {q:"A separable differential equation has the form ___.", options:["dy/dx = f(x) + g(y)","d²y/dx² = f(y)","dy/dx = f(x)g(y) — the variables can be separated: dy/g(y) = f(x)dx","dy/dx = f(x)/g(x)"], answer:2},
     {q:"To solve dy/dx = 2xy, separate variables: ___.", options:["dy/dx = 2xy → dy = 2xy dx → integrate both sides","dy/y = 2x dx → ∫dy/y = ∫2x dx → ln|y| = x² + C → y = Ae^(x²)","dy = y dx → y = e^x","dy/dx = y²"], answer:1},
     {q:"An initial condition (e.g., y(0) = 5) determines ___.", options:["the form of the differential equation","only the constant of integration C in the general solution — giving a particular solution","whether the equation is separable","only the domain of the solution"], answer:1},
     {q:"Newton's Law of Cooling: dT/dt = k(T − T_env) models ___.", options:["only heating problems","only at absolute zero","constant temperature situations","how an object's temperature T changes at a rate proportional to the difference between T and the surrounding temperature — exponential decay to equilibrium"], answer:3},
     {q:"The population equation dP/dt = kP(M − P)/M (logistic) is solved by ___.", options:["separation of variables (requires partial fractions)","the power rule only","direct integration","only numerical methods"], answer:0}
   ]},
  {subject:"Physics", title:"Physics Year-End: Connections and Applications", summary:"Students synthesise all Grade 12 Physics — mechanics, fields, waves, modern physics — and examine how physical principles interconnect.",
   resourceLabel:"Crash Course Physics: Year Review", resourceUrl:"https://www.youtube.com/watch?v=kUDhL6C9Lao",
   quiz:[
     {q:"The four fundamental forces of nature are ___.", options:["gravity, magnetism, heat, and nuclear","gravity, electricity, magnetism, nuclear","gravity, electromagnetism, the strong nuclear force, and the weak nuclear force — all other forces are manifestations of these four","friction, normal force, gravity, tension"], answer:2},
     {q:"Conservation laws in physics (energy, momentum, angular momentum, charge) are ___.", options:["approximate — they can be violated in extreme conditions","only valid in classical physics","only valid in isolated systems (no external forces/energy inputs) — and are among the most powerful and far-reaching principles in all of physics","less fundamental than Newton's Laws"], answer:2},
     {q:"The wave-particle duality in quantum mechanics, confirmed by the double-slit experiment, means ___.", options:["only light has this property","electrons are both waves and particles simultaneously","quantum mechanics is incorrect","quantum objects behave like waves OR particles depending on the experimental setup — observation affects the system in a fundamental, non-classical way"], answer:1},
     {q:"Special relativity modifies classical mechanics at ___.", options:["all speeds","only for massless particles","only in gravitational fields","speeds approaching the speed of light — at everyday speeds, relativistic corrections are negligible, and classical mechanics is an excellent approximation"], answer:3},
     {q:"The most profound insight from Grade 12 Physics is ___.", options:["only Newtonian mechanics matters","physics is only about equations","physics applies only to extreme conditions","the universe operates through mathematically precise laws — and that our human-scale intuitions, while useful approximations, break down at extreme speeds, scales, and energies in ways that reveal deeper truths about reality"], answer:3}
   ]},
]},
{day:13, label:"Day 13 — Wed", subjects:[
  {subject:"English", title:"Independent Reading Synthesis: Personal Reading List", summary:"Students develop a personal reading list beyond the curriculum, demonstrating wide reading, independent literary judgment, and lifelong reading habits.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/c/TEDEd",
   quiz:[
     {q:"Building a personal reading list involves ___.", options:["only choosing bestsellers","following only the curriculum","reading only within one genre","deliberate exploration across genres, periods, cultures, and forms — allowing recommendations, curiosity, and connections between books to guide you into territory you would not otherwise encounter"], answer:3},
     {q:"Keeping a reading journal develops ___.", options:["only a record of books completed","no transferable skills","only for readers who become English teachers","the habit of attending carefully to what you read — noting questions, images, passages, and ideas that matter to you, building a personal archive of reading that enriches all future reading and writing"], answer:3},
     {q:"A recommendation to a peer about a book should include ___.", options:["only the plot summary","only the theme","only the genre","a specific reason this book is worth reading: what is distinctive about its prose, its ideas, its emotional impact, or its formal innovation — not just what it's about, but why it matters"], answer:3},
     {q:"Reading widely beyond the curriculum benefits you by ___.", options:["only improving your exam marks","replacing academic literary study","only for entertainment","building vocabulary, background knowledge, cultural awareness, empathy, narrative intelligence, and the capacity for sustained attention — all of which transfer to academic and professional life"], answer:3},
     {q:"The lifelong reader develops ___.", options:["only factual knowledge from books","only literary knowledge from fiction","a disinterest in other media","a distinctive relationship to language and narrative — a richer inner life, a wider frame of reference, and a deeper capacity for understanding perspectives and experiences beyond their own"], answer:3}
   ]},
  {subject:"Advanced Functions", title:"Mathematical Modelling: Choosing the Right Function", summary:"Students apply all function families to real-world data — choosing, fitting, and interpreting mathematical models.",
   resourceLabel:"Khan Academy: Mathematical Modeling", resourceUrl:"https://www.youtube.com/watch?v=A3M9Ksxrd9c",
   quiz:[
     {q:"When data shows exponential growth that eventually levels off, the best model is ___.", options:["a polynomial function","a trigonometric function","a pure exponential function","a logistic function — capturing rapid initial growth that slows as the population approaches carrying capacity"], answer:3},
     {q:"Data showing a repeating seasonal pattern with constant amplitude is best modelled by ___.", options:["an exponential function","a polynomial","a linear function","a sinusoidal (trigonometric) function — periodic data requires a periodic model"], answer:3},
     {q:"Data about the cooling of an object over time is best modelled by ___.", options:["a linear function","a polynomial of degree 2","a sinusoidal function","an exponential decay function — Newton's Law of Cooling produces exponential temperature change"], answer:3},
     {q:"Evaluating the quality of a mathematical model requires ___.", options:["only looking at the graph","only comparing slopes","only checking the model at known points","examining residuals (differences between predicted and observed values), assessing whether the model captures the pattern, and considering whether the model makes sense outside the data range"], answer:3},
     {q:"The most important limitation of any mathematical model is ___.", options:["they can never be made by students","models are always perfect representations","they require too much computation","it is a simplification of reality — it captures some aspects of the phenomenon and misses others; the skill is knowing which simplifications are acceptable for the purpose at hand"], answer:3}
   ]},
  {subject:"Calculus", title:"Applications: Calculus in Science and Engineering", summary:"Students apply differentiation and integration to physics (motion, work, fluid pressure) and examine the role of calculus in modern science.",
   resourceLabel:"Khan Academy: Calculus Applications", resourceUrl:"https://www.youtube.com/watch?v=m2MIpDrF7Es",
   quiz:[
     {q:"If s(t) is position, then v(t) = s'(t) and a(t) = v'(t) = s''(t). To find displacement from t₁ to t₂:", options:["use the acceleration formula","differentiate s(t)","use average velocity × time","∫[t₁ to t₂] v(t) dt = s(t₂) − s(t₁)"], answer:3},
     {q:"Work done by a variable force F(x) over displacement from a to b is ___.", options:["F × (b − a)","F(b) − F(a)","∫[a to b] F(x) dx — summing infinitesimal work elements, which requires integration when F varies","F(a) × (b − a)"], answer:2},
     {q:"The average value of a continuous function f on [a, b] is ___.", options:["f(a) + f(b))/2 (only for linear functions)","∫[a to b]f(x)dx","[f(b)−f(a)]/(b−a)","[1/(b−a)] × ∫[a to b]f(x)dx — the integral divided by the interval length"], answer:3},
     {q:"Calculus is fundamental to ___.", options:["only pure mathematics","only physics","only engineering","physics (motion, fields, thermodynamics), engineering (design, control systems), economics (marginal analysis), biology (population models), and statistics (probability distributions) — it is the mathematical language of change"], answer:3},
     {q:"The most important insight calculus provides is ___.", options:["how to calculate derivatives and integrals","only how to find slopes","that mathematics can only describe simple systems","that continuous change can be understood by examining it at an infinitesimal scale — and that the process of accumulation (integration) and the process of change (differentiation) are inverse operations"], answer:3}
   ]},
  {subject:"Physics", title:"Astrophysics: Stars, Galaxies, and Cosmology", summary:"Students examine stellar evolution, galaxy structure, and the Big Bang model of the universe, connecting nuclear physics and gravity to astrophysics.",
   resourceLabel:"Crash Course Astronomy: Stars and Cosmology", resourceUrl:"https://www.youtube.com/watch?v=qGHBcRcPQeI",
   quiz:[
     {q:"A star generates energy through ___.", options:["nuclear fission of heavy elements","chemical combustion","only gravitational contraction","nuclear fusion — hydrogen nuclei fuse to form helium in the stellar core, releasing energy from the mass defect"], answer:3},
     {q:"The Hertzsprung-Russell (H-R) diagram plots ___.", options:["speed vs. mass","distance vs. age","temperature vs. position","luminosity vs. surface temperature — revealing that most stars (on the "main sequence") have a predictable relationship between these quantities"], answer:3},
     {q:"A neutron star forms when ___.", options:["a star runs out of hydrogen only","any star dies","a star explodes without collapse","a massive star undergoes a supernova and its core collapses — protons and electrons combine to form neutrons, producing an incredibly dense object roughly the size of a city"], answer:3},
     {q:"The observed redshift of distant galaxies demonstrates ___.", options:["the universe is contracting","only that galaxies are old","the speed of light is increasing","the universe is expanding — light from distant galaxies is shifted toward longer (red) wavelengths, consistent with recessional velocity increasing with distance (Hubble's Law)"], answer:3},
     {q:"The Cosmic Microwave Background (CMB) is ___.", options:["radiation from the first stars","only visible with optical telescopes","noise in early radio equipment","thermal radiation left over from when the universe cooled enough for atoms to form (~380,000 years after the Big Bang) — the strongest evidence for the Big Bang model"], answer:3}
   ]},
]},
{day:14, label:"Day 14 — Thu", subjects:[
  {subject:"English", title:"Grade 12 English: Culminating Preparation", summary:"Students prepare for their culminating essay and exam, reviewing the year's literary works and refining their analytical approaches.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/c/TEDEd",
   quiz:[
     {q:"The Grade 12 culminating essay should demonstrate ___.", options:["only breadth of reading","only length","only correct grammar","the highest level of analytical thinking you are capable of: a specific, arguable, complex thesis; precise, well-chosen evidence; sophisticated analysis; and a coherent, well-structured argument"], answer:3},
     {q:"Preparing for a literary exam involves ___.", options:["only memorising quotations","only re-reading all the texts","only reviewing the plot of each text","understanding each text's formal choices, key thematic concerns, and the arguments you could make about it — having 2-3 developed analytical positions for each major text"], answer:3},
     {q:"The most effective use of quotations in a timed essay is ___.", options:["always using long quotations","using as many as possible","only using quotations in the introduction","shorter, precisely targeted quotations that require and reward analysis — a brief, telling phrase you can unpack analytically is better than a long passage you merely describe"], answer:3},
     {q:"Engaging with literary criticism in a culminating essay shows ___.", options:["only that you have read critics","that you have no original ideas","that critics are always right","that you can position your own reading in relation to existing scholarly perspectives — agreeing, disagreeing, extending, or qualifying a critical position with textual evidence"], answer:3},
     {q:"The last step before submitting a major essay is ___.", options:["only checking spelling","reading the conclusion only","only counting the words","reading the complete essay as a skeptical stranger would: does the argument actually hold? Is each claim supported? Does the conclusion follow from the evidence? Is the voice consistent and clear?"], answer:3}
   ]},
  {subject:"Advanced Functions", title:"Advanced Functions Final Assessment Review", summary:"Students review all major course concepts and practise exam-level problems.",
   resourceLabel:"Khan Academy: Functions Final Review", resourceUrl:"https://www.youtube.com/watch?v=nRmBsxBpTjs",
   quiz:[
     {q:"The graph of f(x) = x(x−2)²(x+1)³ has x-intercepts at ___.", options:["x = 0, 2, −1 with multiplicities 1, 2, 3 respectively — crosses at 0 and −1, touches at 2","x = 0, 4, 3","x = 0, 2, 1","x = 0 and x = 1 only"], answer:0},
     {q:"Solve: 2^(x+1) = 5^(x−1)", options:["(x+1)ln2 = (x−1)ln5 → x(ln2−ln5) = −ln5 − ln2 → x = (ln5+ln2)/(ln5−ln2) = ln10/ln(5/2)","x = ln5/ln2","x = 5/2","x = 4"], answer:0},
     {q:"The function f(x) = (3x²)/(x²−4) has ___.", options:["no asymptotes","vertical asymptotes at x = ±2, horizontal asymptote y = 3 (ratio of leading coefficients), x-intercept at x = 0","only x-intercept at x = 0","vertical asymptotes at x = ±2 only"], answer:1},
     {q:"For vectors a = (1, 3) and b = (4, −2), find a · b and determine if they are perpendicular.", options:["a · b = 4 + (−6) = −2 ≠ 0, so not perpendicular","a · b = 0, so perpendicular","a · b = 1 × 4 = 4","a · b = (1+4)(3+(−2)) = 5"], answer:0},
     {q:"Using induction: prove n² > 2n for all n ≥ 3. Base case n = 3: 9 > 6 ✓. Inductive step: assume k² > 2k. Then (k+1)² = ___.", options:["k² + 2k + 1 > 2k + 2k + 1 > 2(k+1) ✓ (using k ≥ 3 so 2k > 2)","k² + 1","k² + 2","k(k+1)"], answer:0}
   ]},
  {subject:"Calculus", title:"Calculus Final Assessment Review", summary:"Students review all major Calculus content and practise exam-level problems.",
   resourceLabel:"Khan Academy: Calculus Final Review", resourceUrl:"https://www.youtube.com/watch?v=6HkBGVPWIXA",
   quiz:[
     {q:"Evaluate: lim(x→0) of (sin x)/x.", options:["0","∞","lim(x→0) sin(x)/x = 1 (a fundamental limit in calculus — proved by the squeeze theorem or L'Hôpital's Rule)","−1"], answer:2},
     {q:"Find the equation of the tangent to f(x) = e^x at x = 0.", options:["y = e^x","y = x","y = x + 1 (f(0) = 1, f'(x) = e^x, f'(0) = 1, tangent: y − 1 = 1(x − 0))","y = 2x"], answer:2},
     {q:"∫[0 to π]sin(x)dx = ___.", options:["−1","0","π","[−cos(x)] from 0 to π = −cos(π) − (−cos(0)) = 1 + 1 = 2"], answer:3},
     {q:"The maximum of f(x) = x³ − 3x on [−2, 2] occurs at ___.", options:["x = 2: f(2) = 2 (f'(x) = 3x²−3 = 0 → x = ±1; f(1) = −2 (local min), f(−1) = 2 (local max); endpoints: f(−2) = −2, f(2) = 2; global max = 2 at x = −1 and x = 2)","x = 1","x = 0","x = −2"], answer:0},
     {q:"Solve the IVP: dy/dx = y, y(0) = 3.", options:["y = 3e^x (general solution y = Ce^x; C = 3 from initial condition)","y = e^(3x)","y = 3x","y = e^x + 3"], answer:0}
   ]},
  {subject:"Physics", title:"Physics Final Assessment Review", summary:"Students review all Grade 12 Physics content and practise exam-level problems.",
   resourceLabel:"Crash Course Physics: Final Review", resourceUrl:"https://www.youtube.com/watch?v=pGj9isFr21U",
   quiz:[
     {q:"A ball on a string of radius 0.5 m completes one revolution in 2 s. Find centripetal acceleration.", options:["ac = v²/r = (2πr/T)²/r = 4π²r/T² = 4π²(0.5)/4 = π²/2 ≈ 4.93 m/s²","ac = 10 m/s²","ac = 2π m/s²","ac = 5 m/s²"], answer:0},
     {q:"Using Faraday's Law: a coil of 50 turns has its flux change from 0.02 Wb to 0.08 Wb in 0.1 s. The induced EMF is ___.", options:["EMF = −NΔΦ/Δt = −50(0.06)/0.1 = −30 V (magnitude 30 V)","30 mV","0.6 V","300 V"], answer:0},
     {q:"An object at rest has rest energy E₀ = mc². For m = 1 kg, E₀ = ___.", options:["9 × 10¹⁶ J (E₀ = mc² = 1 × (3×10⁸)²)","3 × 10⁸ J","1 J","c J"], answer:0},
     {q:"A circuit has a 12 V battery, 4Ω and 2Ω resistors in series. Current = ___.", options:["I = V/R_total = 12/6 = 2 A","I = 3 A","I = 6 A","I = 12 A"], answer:0},
     {q:"Time dilation: a muon travels at 0.98c. Its proper lifetime is 2.2 μs. Time measured in lab frame = ___.", options:["t = γt₀ = 2.2/√(1−0.98²) μs ≈ 2.2/0.199 ≈ 11 μs","2.2 μs unchanged","0.44 μs","22 μs"], answer:0}
   ]},
]},
{day:15, label:"Day 15 — Fri", subjects:[
  {subject:"English", title:"Grade 12 English: Exam and Celebration", summary:"A final celebration of Grade 12 English — reflecting on the year's literary journey and looking ahead to university and lifelong reading.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/c/TEDEd",
   quiz:[
     {q:"Grade 12 English culminates in ___.", options:["completed study of English","the end of reading and writing as serious pursuits","only exam preparation","a genuine transformation — students who engage deeply emerge as fundamentally different readers and thinkers, with analytical skills, literary knowledge, and communicative power that will serve them throughout their lives"], answer:3},
     {q:"The connection between literature and university study is ___.", options:["literature is only relevant in humanities programs","literature is not studied at university","no connection","the analytical, argumentative, and communicative skills developed in literary study are fundamental to success in virtually any university discipline — history, law, political science, philosophy, psychology, and increasingly science communication"], answer:3},
     {q:"Reading literature throughout your adult life ___.", options:["is only for people who study English","has no connection to professional success","is largely irrelevant after graduation","sustains intellectual and empathetic development, provides pleasure and meaning, connects you to the fullest range of human experience, and maintains the reading skills that atrophy without practice"], answer:3},
     {q:"The writers you have studied in Grade 12 ___.", options:["are now no longer relevant","are only relevant in academic contexts","have taught you only literary technique","have given you intellectual companions — voices you can return to throughout your life, finding new meaning as your own experience grows"], answer:3},
     {q:"English, as a discipline and a practice, is ___.", options:["a set of skills you've now mastered and completed","only about grammar and spelling","only about fiction and poetry","a lifelong pursuit — language and literature are not finished, not mastered, not set aside after graduation but lived with, returned to, and deepened throughout a human life"], answer:3}
   ]},
  {subject:"Advanced Functions", title:"Looking Back, Looking Forward", summary:"Students reflect on their mathematical development across MHF4U and its connection to university mathematics.",
   resourceLabel:"Khan Academy: Looking Ahead to Calculus", resourceUrl:"https://www.youtube.com/watch?v=riXcZT2ICjA",
   quiz:[
     {q:"Advanced Functions has prepared you for university mathematics by ___.", options:["teaching you all the mathematics you will ever need","only for students in STEM programs","being equivalent to first-year university calculus","developing fluency in function analysis — the foundation for calculus, linear algebra, statistics, and all quantitative reasoning at university level"], answer:3},
     {q:"The most transferable mathematical skill from Grade 12 is ___.", options:["memorising all formulas","only knowing specific function types","computing derivatives (which you haven't done in this course)","mathematical reasoning: forming conjectures, testing them systematically, constructing rigorous arguments, and knowing when a result is proven vs. merely plausible"], answer:3},
     {q:"Mathematics at university is ___.", options:["identical to high school mathematics","easier than high school","only about computation","more abstract and proof-based — shifting from applying formulas to understanding why they work and extending them to new situations; Grade 12 Advanced Functions is the foundation for this shift"], answer:3},
     {q:"The mathematicians whose work you have implicitly used in this course — Euler, Gauss, Newton — ___.", options:["were only interested in pure theory","had no connection to the mathematics you studied","are only important to professional mathematicians","built the framework that makes modern science, engineering, finance, and computing possible — Grade 12 mathematics is not just school content but access to centuries of human intellectual achievement"], answer:3},
     {q:"Finishing Advanced Functions means ___.", options:["you are done with mathematics","you need no further mathematical study","only that you passed the course","you have the mathematical tools to pursue virtually any university program — and more importantly, you have experienced mathematical thinking at a level that trains the mind for rigorous reasoning in any field"], answer:3}
   ]},
  {subject:"Calculus", title:"Calculus: Looking Back and Forward", summary:"Students reflect on the year's learning in calculus and its connections to the mathematical sciences.",
   resourceLabel:"Khan Academy: Calculus Bridge to University", resourceUrl:"https://www.youtube.com/watch?v=WUvTyaaNkzM",
   quiz:[
     {q:"The Fundamental Theorem of Calculus is profound because ___.", options:["it makes integration easier to compute","only because it involves two operations","it is the most complex theorem in mathematics","it reveals that differentiation and integration — apparently unrelated operations — are inverse operations, unifying two major streams of mathematical thinking into a single theory"], answer:3},
     {q:"Calculus was developed independently by ___.", options:["Euclid and Archimedes","Gauss and Euler","Descartes and Fermat","Newton and Leibniz in the 17th century — a famous priority dispute, but their discoveries were genuinely independent and used different notation (we use Leibniz's)"], answer:3},
     {q:"The most important application of calculus in the 21st century is ___.", options:["only in physics","only in engineering","only bridge design","arguably machine learning — the training of neural networks relies on gradient descent (an application of multivariable calculus) to optimise complex functions with millions of parameters"], answer:3},
     {q:"Differential equations (which you've begun) are ___.", options:["a minor extension of introductory calculus","less important than algebra","only for engineers","the language in which most of science is written — from Newton's laws to quantum mechanics to epidemiology to population ecology, the universe is described by equations relating rates of change"], answer:3},
     {q:"Completing Grade 12 Calculus means ___.", options:["you have mastered all of calculus","university calculus will be completely familiar","calculus is now closed to you","you have the foundation to study multivariable calculus, differential equations, and real analysis at university — the door to the mathematical sciences is open"], answer:3}
   ]},
  {subject:"Physics", title:"Physics: A Final Reflection", summary:"Students reflect on their learning in Grade 12 Physics and the role of physics in understanding the universe.",
   resourceLabel:"Crash Course Physics: Reflecting on Physics", resourceUrl:"https://www.youtube.com/watch?v=kKKM8Y-u7ds",
   quiz:[
     {q:"Physics is the most fundamental science because ___.", options:["it is the oldest science","it is the most difficult","only physicists understand it","its principles underlie chemistry, biology, and engineering — chemistry is physics applied to electrons, biology applies chemical and physical principles to living systems, and all technology exploits physical laws"], answer:3},
     {q:"The history of physics shows ___.", options:["physics is a complete and finished discipline","major changes in understanding are no longer possible","only a gradual accumulation of facts","a series of revolutionary conceptual shifts — from Aristotle to Newton, from Newton to Einstein, from classical to quantum — each overturning apparently solid knowledge and revealing something deeper"], answer:3},
     {q:"Quantum mechanics and general relativity, the two great theories of 20th century physics, ___.", options:["are in perfect agreement","have been completely unified","have no experimental support","are both spectacularly confirmed but mutually inconsistent — their reconciliation (quantum gravity) is one of the greatest unsolved problems in all of science"], answer:3},
     {q:"Physics shapes your daily life through ___.", options:["no practical applications in everyday life","only large-scale technologies","only electrical devices","everything: the transistors in your phone, the GPS that locates you, the medical imaging that diagnoses disease, the lasers that read discs, the superconductors in MRI machines — all rest on 20th century physics"], answer:3},
     {q:"The greatest gift of physics education is ___.", options:["knowing all the formulas","passing the exam","only useful if you study physics at university","the habit of asking "why does this happen?" and having confidence that patient, systematic inquiry can reveal the answer — the physicist's mindset: curiosity, rigour, and belief in the comprehensibility of nature"], answer:3}
   ]},
]},
];
{day:16, label:"Day 16 — Mon", subjects:[
  {subject:"English", title:"Postcolonial Literature: Writing Back to Empire", summary:"Students examine postcolonial theory and its application to literary texts — how writers from formerly colonised nations rewrite colonial narratives.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/watch?v=G15p7uOc-aA",
   quiz:[
     {q:"The term "writing back" (Ashcroft et al.) refers to ___.", options:["authors responding to publisher rejections","only African literature","only protest poetry","postcolonial writers engaging with, subverting, and rewriting the canonical texts of the colonising culture — reclaiming language and narrative for suppressed perspectives"], answer:3},
     {q:"Chinua Achebe's critique of Conrad's Heart of Darkness argues ___.", options:["the novel is flawless","Conrad was not a racist","the novel is primarily about navigation","Conrad dehumanises Africans by making Africa merely a backdrop for a European psychological journey — denying African people interiority, agency, and humanity"], answer:3},
     {q:"The use of the coloniser's language by postcolonial writers is ___.", options:["a sign of cultural defeat","never chosen freely","unproblematic and straightforward","a complex negotiation — some see it as accommodation, others as strategic subversion; many writers (Achebe, Ngugi, Rushdie) have debated this directly in essays and in their fiction"], answer:3},
     {q:"Hybridity (Homi Bhabha) in postcolonial literature refers to ___.", options:["mixing languages only","a purely biological concept","cultural purity in new nations","the complex cultural mixing produced by colonialism — neither purely coloniser nor colonised, but a "third space" of negotiated identity"], answer:3},
     {q:"Applying postcolonial theory to a Canadian text requires ___.", options:["recognising Canada has no colonial history","only examining French-English relations","treating all colonial experiences as identical","acknowledging Canada's specific colonial history — both as a British colony and as a settler-colonial state with ongoing impacts on Indigenous peoples — a complex dual position"], answer:3}
   ]},
  {subject:"Advanced Functions", title:"Vectors in Three Dimensions", summary:"Students extend 2D vector concepts to 3D — Cartesian coordinates, vector operations, magnitude, dot product, and angle between vectors.",
   resourceLabel:"Khan Academy", resourceUrl:"https://www.youtube.com/watch?v=k7RM-ot2NWY",
   quiz:[
     {q:"A vector in 3D is written as ___.", options:["(x, y)","[x:y:z]","x + y + z","a = (a₁, a₂, a₃) or a₁i + a₂j + a₃k — three components corresponding to x, y, z directions"], answer:3},
     {q:"The magnitude of a = (2, −1, 3) is ___.", options:["6","2 + 1 + 3 = 6","√(4+1+9) = √14","√(2+1+3) = √6"], answer:2},
     {q:"The dot product a · b for a=(1,2,3) and b=(4,−1,2) is ___.", options:["(4,−2,6)","4−1+6 = 9... wait: 1×4 + 2×(−1) + 3×2 = 4 − 2 + 6 = 8","4 + 2 + 6 = 12","1×4 − 2×1 + 3×2 = 8"], answer:3},
     {q:"The angle θ between vectors a and b satisfies ___.", options:["sinθ = a·b/(|a||b|)","cosθ = |a|/|b|","tanθ = a·b","cosθ = a·b/(|a||b|) — rearranging the dot product formula: a·b = |a||b|cosθ"], answer:3},
     {q:"Two vectors in 3D are perpendicular when ___.", options:["they have equal magnitudes","their components are proportional","|a| = |b| = 1","their dot product equals zero: a·b = a₁b₁ + a₂b₂ + a₃b₃ = 0"], answer:3}
   ]},
  {subject:"Calculus", title:"Related Rates: Advanced Applications", summary:"Students solve multi-step related rates problems in geometry, physics, and engineering contexts.",
   resourceLabel:"Khan Academy Calculus", resourceUrl:"https://www.youtube.com/watch?v=I9mVUo-bhM8",
   quiz:[
     {q:"The key step in any related rates problem is ___.", options:["to differentiate the known quantity","to find the maximum value","only to identify the unknown","to write an equation relating the quantities that are changing, then differentiate both sides with respect to time using the chain rule"], answer:3},
     {q:"A ladder 5 m long leans against a wall. The base slides out at 0.5 m/s. When base is 3 m from wall: find how fast the top slides down.", options:["dy/dt = 0.375 m/s down (x²+y²=25; 2x dx/dt+2y dy/dt=0; y=4; dy/dt = −x/y × dx/dt = −3/4 × 0.5 = −0.375 m/s)","dy/dt = 0.5 m/s","dy/dt = 1 m/s","dy/dt = 0.25 m/s"], answer:0},
     {q:"Water pours into a conical tank (radius r, height h, r/h = 1/2) at 5 m³/min. Find dh/dt when h = 3 m.", options:["dh/dt = 5/(9π/4) = 20/(9π) m/min (V=1/3πr²h=πh³/12; dV/dt=πh²/4 × dh/dt; 5=π(9)/4 × dh/dt)","dh/dt = 5 m/min","dh/dt = 5/(3π) m/min","dh/dt = 20/(3π) m/min"], answer:0},
     {q:"Two cars leave an intersection at right angles: A at 60 km/h north, B at 80 km/h east. Find rate of distance increase after 1 hour.", options:["100 km/h (z²=x²+y²; 2z dz/dt=2x dx/dt+2y dy/dt; at t=1: x=80, y=60, z=100; dz/dt=(80×80+60×60)/100=100)","140 km/h","50 km/h","72 km/h"], answer:0},
     {q:"What distinguishes a related rates problem from a standard derivative problem?", options:["related rates use only one variable","related rates never require the chain rule","related rates only involve geometry","in related rates, multiple quantities change with time, and we use implicit differentiation with respect to time to relate their rates — the chain rule appears on every term"], answer:3}
   ]},
  {subject:"Physics", title:"Momentum and Impulse", summary:"Students analyse linear momentum, impulse, and the impulse-momentum theorem in collision contexts.",
   resourceLabel:"Crash Course Physics", resourceUrl:"https://www.youtube.com/watch?v=nPnPqH-R_Y4",
   quiz:[
     {q:"Linear momentum is defined as ___.", options:["p = mv² (kinetic energy, not momentum)","p = ma","p = Ft","p = mv — a vector quantity; its direction is the same as velocity"], answer:3},
     {q:"The impulse-momentum theorem states ___.", options:["J = mv only","J = Ft² ","J = ma × t","J = FΔt = Δp — the impulse (force × time) equals the change in momentum; this connects force, time, and motion change"], answer:3},
     {q:"Conservation of linear momentum applies when ___.", options:["all forces are equal","friction is absent","the system is in free fall","no net external force acts on the system — the total momentum before equals total momentum after, regardless of what happens internally"], answer:3},
     {q:"In a perfectly inelastic collision ___.", options:["both objects pass through each other","kinetic energy is conserved","the objects bounce elastically","the objects stick together — momentum is conserved but kinetic energy is not; some KE converts to heat, sound, or deformation"], answer:3},
     {q:"A 0.5 kg ball at 10 m/s east collides and sticks to a 1.5 kg ball at rest. Final velocity:", options:["v = 0.5×10/(0.5+1.5) = 5/2 = 2.5 m/s east","v = 5 m/s","v = 3.3 m/s","v = 10 m/s"], answer:0}
   ]},
]},
{day:17, label:"Day 17 — Tue", subjects:[
  {subject:"English", title:"Comparative Essay: World Literature", summary:"Students write a formal comparative essay on two world literature texts, applying university-level analytical standards.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/watch?v=MSYw502dJNY",
   quiz:[
     {q:"A comparative essay thesis must ___.", options:["only list the works to be compared","treat works as entirely separate","describe similarities only","make a claim about what the comparison reveals — not just "A and B are similar/different" but "this specific similarity/difference illuminates X about both texts""], answer:3},
     {q:"Integrating two texts in a comparative essay is best done by ___.", options:["discussing one text fully, then the other (block method always)","never mixing the texts","only using plot summaries","using a point-by-point structure for analytical comparison — each paragraph focuses on a specific comparative point, weaving both texts together to support the analytical claim"], answer:3},
     {q:"When comparing texts from different cultural contexts, a student must ___.", options:["assume all cultures value the same things","treat one culture as the norm and the other as exotic","only focus on form, not context","acknowledge the cultural and historical specificity of each text — avoid imposing one cultural framework on the other, and use both contexts to enrich the comparison"], answer:3},
     {q:"The most sophisticated comparative essays ___.", options:["only describe similarities","only note obvious differences","treat texts independently and in parallel only","find a productive tension — a similarity that conceals difference, or a difference that reveals a shared concern — and use this to generate genuine analytical insight"], answer:3},
     {q:"Works from different languages in translation present ___.", options:["no issues since translation is neutral","opportunities to compare style directly","no analytical interest","a specific interpretive challenge — you are reading the translator's choices as well as the author's, and you should acknowledge this while still engaging meaningfully with the available text"], answer:3}
   ]},
  {subject:"Advanced Functions", title:"Lines and Planes in Three Dimensions", summary:"Students write vector and parametric equations of lines in 3D, and scalar and vector equations of planes.",
   resourceLabel:"Khan Academy", resourceUrl:"https://www.youtube.com/watch?v=1DfkHs6MFJk",
   quiz:[
     {q:"The vector equation of a line through point P₀=(x₀,y₀,z₀) with direction d=(a,b,c) is ___.", options:["r = (x₀+a, y₀+b, z₀+c)","r = d × P₀","r = P₀ + t (the direction is missing)","r = (x₀,y₀,z₀) + t(a,b,c) — a point plus a scalar multiple of the direction vector"], answer:3},
     {q:"The parametric equations of the same line are ___.", options:["only x = x₀ + at","x=x₀+at, y=y₀+bt, z=z₀+ct — one equation per dimension, each parameterised by t","x=at, y=bt, z=ct only","x=x₀t, y=y₀t, z=z₀t"], answer:1},
     {q:"The scalar (Cartesian) equation of a plane with normal n=(A,B,C) through (x₀,y₀,z₀) is ___.", options:["A+B+C=D","Ax + By + Cz = 0 (only if through origin)","A(x+x₀)+B(y+y₀)+C(z+z₀)=0","A(x−x₀)+B(y−y₀)+C(z−z₀)=0 — or equivalently Ax+By+Cz=D where D=Ax₀+By₀+Cz₀"], answer:3},
     {q:"Two planes are parallel if and only if ___.", options:["they have the same x-intercept","their equations differ only by a constant","they are both horizontal","their normal vectors are parallel (one is a scalar multiple of the other)"], answer:3},
     {q:"A line is perpendicular to a plane when ___.", options:["the line's direction vector is horizontal","the line passes through the origin","the line has slope 1","the line's direction vector is parallel to the plane's normal vector — the line points in the same direction as the normal"], answer:3}
   ]},
  {subject:"Calculus", title:"L'Hôpital's Rule and Indeterminate Forms", summary:"Students apply L'Hôpital's Rule to evaluate limits of indeterminate forms (0/0, ∞/∞, ∞−∞, 0·∞).",
   resourceLabel:"Khan Academy Calculus", resourceUrl:"https://www.youtube.com/watch?v=_2aCDXyFZC8",
   quiz:[
     {q:"L'Hôpital's Rule states that if lim f/g = 0/0 or ∞/∞, then ___.", options:["lim f/g = lim (f+g)","lim f/g = lim (f−g)/(g)","lim f/g = f/g evaluated at the limit point","lim f(x)/g(x) = lim f'(x)/g'(x) — provided the latter limit exists; differentiate numerator and denominator separately (not the quotient rule)"], answer:3},
     {q:"Evaluate lim(x→0) sin(x)/x.", options:["Apply L'Hôpital: lim cos(x)/1 = 1","Apply L'Hôpital: lim −sin(x)/0 = undefined","Apply L'Hôpital: lim cos(x)/cos(x) = 1","This is not 0/0 form; the limit is 0"], answer:0},
     {q:"Evaluate lim(x→∞) x/eˣ.", options:["L'Hôpital (∞/∞): lim 1/eˣ = 0 — exponentials grow faster than polynomials","L'Hôpital: lim 1/xeˣ","The limit is ∞","The limit is 1"], answer:0},
     {q:"The form 0·∞ is handled by ___.", options:["directly multiplying the limits","taking the square root","no special technique needed","rewriting as 0/(1/∞) = 0/0 or ∞/(1/0) = ∞/∞, then applying L'Hôpital"], answer:3},
     {q:"Evaluate lim(x→0⁺) x·ln(x).", options:["0 (rewrite as ln(x)/(1/x) = ∞/∞; L'Hôpital: (1/x)/(−1/x²) = −x → 0)","∞","1","−1"], answer:0}
   ]},
  {subject:"Physics", title:"Conservation of Momentum: Collisions in 2D", summary:"Students apply conservation of momentum to two-dimensional collisions, resolving vectors into components.",
   resourceLabel:"Crash Course Physics", resourceUrl:"https://www.youtube.com/watch?v=3sGOCBfpmbY",
   quiz:[
     {q:"For a 2D collision, conservation of momentum applies ___.", options:["only in the horizontal direction","only for elastic collisions","only if no friction acts","independently to both x and y components simultaneously — momentum is a vector, so each component is separately conserved"], answer:3},
     {q:"In a 2D elastic collision, both ___ and ___ are conserved.", options:["mass and velocity","force and time","mass and charge","momentum (vector) and kinetic energy (scalar) — both are conserved simultaneously"], answer:3},
     {q:"A 2 kg ball moving at 5 m/s east hits a 2 kg ball at rest. After collision ball 1 moves north. By symmetry (equal masses, elastic):", options:["both balls move east at 2.5 m/s","ball 2 moves east at 5 m/s, ball 1 stops — total KE and momentum conserved (for equal mass elastic head-on collision)... but this is 2D so ball 1 moves north — ball 2 moves east at 5 m/s","both stop","ball 1 bounces back west"], answer:1},
     {q:"The coefficient of restitution e = ___.", options:["e = m₁/m₂","e = v₁_initial/v₂_final","e = final momentum/initial momentum","e = relative speed after/relative speed before — 0 for perfectly inelastic, 1 for perfectly elastic"], answer:3},
     {q:"An explosion (reverse collision) starting from rest: total momentum after = ___.", options:["equal to the initial kinetic energy","equal to the mass times the speed of the larger piece","equal to the net external force","zero — momentum is conserved; since initial momentum was zero, all fragments' momenta sum to zero"], answer:3}
   ]},
]},
{day:18, label:"Day 18 — Wed", subjects:[
  {subject:"English", title:"Literary Theory: Reading Through a Lens", summary:"Students apply feminist, Marxist, and psychoanalytic critical lenses to literary texts, understanding how theory shapes interpretation.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/watch?v=qGHBcRcPQeI",
   quiz:[
     {q:"Applying a critical lens to a text means ___.", options:["finding the one correct interpretation","proving the author had specific intentions","only citing theory in a bibliography","using a theoretical framework to ask specific questions of the text — the lens determines what you notice, what questions you ask, and how you interpret what you find"], answer:3},
     {q:"Feminist literary criticism examines ___.", options:["only texts by women","only texts with female protagonists","only gender in isolation from other factors","how texts construct, reinforce, challenge, or subvert gender roles and the social, political, and economic structures that subordinate women — applied to texts by any author"], answer:3},
     {q:"Marxist literary criticism examines ___.", options:["only communist literature","only economic statistics in fiction","only class conflict in plot","how texts reflect, reinforce, or critique the economic base and ideological superstructure of society — including class, labour, power, and commodity relations"], answer:3},
     {q:"Psychoanalytic literary criticism (Freud, Lacan) examines ___.", options:["only mentally ill characters","only the author's biography","only obvious symbolism","the unconscious dimensions of texts — repression, desire, the uncanny, dream logic, the dynamics of id/ego/superego or Lacanian registers (Symbolic, Imaginary, Real)"], answer:3},
     {q:"The danger of applying theory mechanically is ___.", options:["the theory becomes irrelevant","theory always improves a reading","no danger exists in using theory","the text is reduced to an illustration of the theory — sophisticated critical work uses theory as a lens to illuminate specific textual details, not as a formula that produces predetermined readings"], answer:3}
   ]},
  {subject:"Advanced Functions", title:"The Cross Product in 3D", summary:"Students compute cross products of 3D vectors and apply them to find normals to planes, areas of parallelograms, and equations of planes.",
   resourceLabel:"Khan Academy", resourceUrl:"https://www.youtube.com/watch?v=pJzmiywagfY",
   quiz:[
     {q:"The cross product a × b produces ___.", options:["a scalar equal to |a||b|cosθ","the component-wise product of two vectors","the dot product of two vectors","a vector perpendicular to both a and b — with magnitude |a||b|sinθ"], answer:3},
     {q:"For a=(1,0,0) and b=(0,1,0), a × b = ___.", options:["(0,0,0)","(1,1,0)","(−1,0,0)","(0,0,1) = k — the z-unit vector; confirms right-hand rule"], answer:3},
     {q:"The area of a parallelogram with sides a and b is ___.", options:["a · b","|a| × |b|","|a|² + |b|²","|a × b| — the magnitude of the cross product equals the area of the parallelogram spanned by the two vectors"], answer:3},
     {q:"To find the equation of a plane through three points P₁, P₂, P₃, find ___.", options:["the midpoint of the three points","only the distance between the points","the sum of all coordinates","vectors P₁P₂ and P₁P₃, then compute their cross product to get the normal n, then write the plane equation using n and any of the three points"], answer:3},
     {q:"a × b = −(b × a) means ___.", options:["cross product is commutative","cross product always gives zero","a × b and b × a are equal","cross product is anti-commutative — reversing the order reverses the direction of the resulting vector; the magnitude is the same"], answer:3}
   ]},
  {subject:"Calculus", title:"Implicit Differentiation and Inverse Functions", summary:"Students apply implicit differentiation to curves defined implicitly, and differentiate inverse trigonometric and general inverse functions.",
   resourceLabel:"Khan Academy Calculus", resourceUrl:"https://www.youtube.com/watch?v=mSVrqKZDRF4",
   quiz:[
     {q:"Implicit differentiation is needed when ___.", options:["the function is a polynomial","the function has no y variable","y is explicitly solved in terms of x","y cannot easily be isolated — you differentiate both sides with respect to x, treating y as a function of x and applying the chain rule whenever y appears"], answer:3},
     {q:"Differentiate x² + y² = 25 implicitly. dy/dx = ___.", options:["2x + 2y","−x/y (differentiating: 2x + 2y·dy/dx = 0 → dy/dx = −x/y)","x/y","−y/x"], answer:1},
     {q:"d/dx[arcsin(x)] = ___.", options:["cos(arcsin x)","1/cos(x)","−1/√(1−x²)","1/√(1−x²) — derived via implicit differentiation of y = arcsin(x) → sin(y) = x → cos(y)·dy/dx = 1 → dy/dx = 1/cos(y) = 1/√(1−x²)"], answer:3},
     {q:"d/dx[arctan(x)] = ___.", options:["sec²(x)","1/(1+x²) — derived: tan(y) = x → sec²(y)·dy/dx = 1 → dy/dx = cos²(y) = 1/(1+x²)","1/cos²(x)","−1/(1+x²)"], answer:1},
     {q:"The general inverse function derivative rule: if g = f⁻¹, then g'(x) = ___.", options:["1/f(x)","f'(g(x))","g(f'(x))","1/f'(g(x)) — the slope of the inverse at x is the reciprocal of the slope of f at the corresponding point"], answer:3}
   ]},
  {subject:"Physics", title:"Simple Harmonic Motion", summary:"Students analyse SHM — period, frequency, amplitude, restoring force — and apply to springs and pendulums.",
   resourceLabel:"Crash Course Physics", resourceUrl:"https://www.youtube.com/watch?v=ZkLXIZoCo-o",
   quiz:[
     {q:"Simple harmonic motion occurs when ___.", options:["speed is constant","the restoring force is constant","the amplitude increases over time","the restoring force is proportional to and opposite to the displacement: F = −kx — this produces sinusoidal oscillation"], answer:3},
     {q:"For a spring-mass system, the period is ___.", options:["T = 2π√(k/m)","T = 2πm/k","T = 2π√(m/k) — independent of amplitude; depends only on mass and spring constant","T = 2π√k"], answer:2},
     {q:"For a simple pendulum of length L, T = ___.", options:["T = 2π√(g/L)","T = 2πL/g","T = 2π√(L/g) — valid for small angles only; independent of mass and (approximately) amplitude","T = 2πg/L"], answer:2},
     {q:"The total mechanical energy in SHM is ___.", options:["only kinetic energy","only potential energy","zero at the equilibrium position","constant: E = ½kA² (where A is amplitude) — KE and PE convert to each other, but their sum is always ½kA²"], answer:3},
     {q:"At maximum displacement (amplitude) in SHM, the velocity is ___ and acceleration is ___.  ", options:["maximum and maximum","zero and zero","maximum and zero","zero and maximum — at the endpoints, the object momentarily stops (v=0) and the restoring force (and thus acceleration) is greatest"], answer:3}
   ]},
]},
{day:19, label:"Day 19 — Thu", subjects:[
  {subject:"English", title:"Satire: Social Critique Through Comedy", summary:"Students analyse satire as a literary mode — examining targets, techniques (irony, parody, exaggeration), and the ethics and limits of satirical writing.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/watch?v=d1bE7LfNqlU",
   quiz:[
     {q:"Satire differs from simple comedy in that ___.", options:["satire is never funny","satire is always gentler than direct critique","satire has no political dimension","satire uses humour to expose, criticise, and potentially reform human folly, vice, or social institutions — comedy is an end in itself; satirical comedy is a means to a critical end"], answer:3},
     {q:"Horatian satire (after Horace) is characterised by ___.", options:["bitter, savage attack","no use of irony","no political targets","gentle, urbane wit — the satirist laughs with the audience at human folly, gently nudging toward reform rather than condemning"], answer:3},
     {q:"Juvenalian satire (after Juvenal) is characterised by ___.", options:["gentle humour","no exaggeration","praise of the satirical target","bitter, contemptuous indignation — the satirist condemns and attacks; the tone is harsh, the critique unsparing"], answer:3},
     {q:"Jonathan Swift's "A Modest Proposal" uses ___.", options:["straightforward rhetorical argument","direct emotional appeal","pure comedy without bite","sustained irony — the narrator's reasonable tone and logical precision make the monstrous proposal (eating Irish babies) more horrifying, not less; the gap between manner and content is the satirical engine"], answer:3},
     {q:"The ethics of satire involve ___.", options:["no ethical considerations","only attacking powerful institutions","that any target is fair game","difficult questions about power: satire that "punches down" (mocks the vulnerable) is ethically different from satire that challenges power — and the line is not always clear"], answer:3}
   ]},
  {subject:"Advanced Functions", title:"Equations of Lines and Planes: Intersections and Distances", summary:"Students find intersections of lines and planes in 3D and calculate distances from points to lines and planes.",
   resourceLabel:"Khan Academy", resourceUrl:"https://www.youtube.com/watch?v=5AWob_z74Ks",
   quiz:[
     {q:"To find where a line intersects a plane, substitute the ___ into the plane equation.", options:["normal vector of the plane","coordinates of any point on the plane","parametric equations of the line (in terms of t) and solve for t","direction vector of the line"], answer:2},
     {q:"The distance from point P=(x₁,y₁,z₁) to plane Ax+By+Cz=D is ___.", options:["|AP₁|","√(A²+B²+C²)","|Ax₁+By₁+Cz₁|","|Ax₁+By₁+Cz₁−D|/√(A²+B²+C²) — a formula analogous to the 2D point-to-line distance"], answer:3},
     {q:"Two lines in 3D can be ___.", options:["only parallel or intersecting","always coplanar","always intersecting","parallel, intersecting, or skew (non-parallel, non-intersecting lines that do not lie in the same plane)"], answer:3},
     {q:"To determine if two lines in 3D intersect, you ___.", options:["check if their direction vectors are equal","set their position vectors equal and check for consistency","only check if they are parallel","set parametric equations equal in all three coordinates and check if a consistent solution (value of both parameters) exists"], answer:1},
     {q:"The angle between two planes equals ___.", options:["the angle between their x-intercepts","90° always","the angle between a line and the plane","the angle between their normal vectors (or its supplement, taking the acute angle)"], answer:3}
   ]},
  {subject:"Calculus", title:"Mean Value Theorem and Monotonicity", summary:"Students state and apply the Mean Value Theorem, Rolle's Theorem, and use them to analyse function behaviour.",
   resourceLabel:"Khan Academy Calculus", resourceUrl:"https://www.youtube.com/watch?v=mAul5vTAJSA",
   quiz:[
     {q:"Rolle's Theorem states: if f is continuous on [a,b], differentiable on (a,b), and f(a)=f(b), then ___.", options:["f is constant on [a,b]","f has no local extrema","there exists c in (a,b) such that f'(c) = 1","there exists c in (a,b) such that f'(c) = 0 — at least one point where the tangent is horizontal"], answer:3},
     {q:"The Mean Value Theorem states: if f is continuous on [a,b] and differentiable on (a,b), then ___.", options:["f achieves its maximum at a or b","f(a) = f(b) always","f'(x) = 0 for some x","there exists c in (a,b) such that f'(c) = [f(b)−f(a)]/(b−a) — the instantaneous rate equals the average rate at some interior point"], answer:3},
     {q:"A geometric interpretation of the MVT: ___.", options:["the tangent and secant are always perpendicular","the function always has a zero","the function achieves both max and min","the tangent line at some interior point c is parallel to the secant line through (a,f(a)) and (b,f(b))"], answer:3},
     {q:"If f'(x) > 0 for all x in (a,b), then the MVT implies ___.", options:["f is constant","f has no extrema only","f(a) = f(b)","f is strictly increasing on (a,b) — a corollary: a positive derivative implies increasing function"], answer:3},
     {q:"If f'(x) = g'(x) for all x, then ___.", options:["f(x) = g(x)","f and g are both zero","no relationship can be inferred","f(x) = g(x) + C for some constant C — their derivatives being equal means they can only differ by a constant (a direct corollary of the MVT)"], answer:3}
   ]},
  {subject:"Physics", title:"Wave Superposition and Interference", summary:"Students analyse the superposition of waves — constructive and destructive interference, standing waves, and resonance in strings and air columns.",
   resourceLabel:"Crash Course Physics", resourceUrl:"https://www.youtube.com/watch?v=7cDAYFTXq3E",
   quiz:[
     {q:"The principle of superposition states ___.", options:["waves cannot occupy the same space","only two waves can interfere","louder waves always dominate","when two or more waves overlap, the resultant displacement is the algebraic sum of the individual displacements — waves pass through each other unchanged"], answer:3},
     {q:"Constructive interference occurs when ___.", options:["waves have different frequencies","waves are perpendicular","the path difference is a half-integer multiple of λ","waves arrive in phase (path difference = nλ for integer n) — crests coincide, producing maximum amplitude"], answer:3},
     {q:"Destructive interference occurs when ___.", options:["waves have equal amplitudes only","waves travel in opposite directions","path difference = nλ","waves arrive out of phase (path difference = (n+½)λ) — crest meets trough, producing minimum or zero amplitude"], answer:3},
     {q:"A standing wave on a string fixed at both ends has nodes at ___.", options:["antinodes only","only at the centre","random positions along the string","the fixed endpoints — and additional nodes at intervals of λ/2; antinodes are halfway between nodes"], answer:3},
     {q:"The fundamental frequency of a string of length L, tension T, mass/length μ is ___.", options:["f₁ = L/(2√(T/μ))","f₁ = 2L√(μ/T)","f₁ = 1/(2L) × √(T/μ) — the lowest resonant frequency; harmonics are multiples of f₁","f₁ = √(TL/μ)"], answer:2}
   ]},
]},
{day:20, label:"Day 20 — Fri", subjects:[
  {subject:"English", title:"The Research Essay: Argument and Evidence at University Level", summary:"Students write and revise a fully documented research essay integrating primary texts, secondary criticism, and their own analysis.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/watch?v=vtIzMaLkCaM",
   quiz:[
     {q:"A literary research essay differs from a personal response in that ___.", options:["it does not use primary texts","it is longer only","personal response is always better","it situates your argument within the existing critical conversation — using secondary sources to identify what critics have argued and positioning your own reading in relation to that conversation"], answer:3},
     {q:"Selecting secondary sources for a literary research essay requires ___.", options:["only using Wikipedia and study guides","any online source about the author","only the most recent criticism","peer-reviewed scholarly articles and books — sources that have been evaluated by experts in the field and make rigorous, evidence-based arguments about the text"], answer:3},
     {q:"Synthesising sources in a research essay means ___.", options:["quoting each source in order","only summarising each source separately","never agreeing with any source","weaving together multiple perspectives to illuminate your own argument — sources speak to each other and to your thesis, not just in sequence"], answer:3},
     {q:"MLA citation requires ___.", options:["only in-text page numbers for everything","only a bibliography, no in-text citation","only footnotes, no bibliography","in-text citations (author page#) and a corresponding Works Cited page — for online sources, include URL or DOI and access date as applicable"], answer:3},
     {q:"Academic integrity in a research essay means ___.", options:["only quoting correctly","only avoiding copy-paste","only citing sources you agree with","citing every source of ideas, information, and argument (whether quoted, paraphrased, or summarised) and presenting your own original synthesis and argument — not reproducing others' analysis as your own"], answer:3}
   ]},
  {subject:"Advanced Functions", title:"Geometric Vectors: Applications to Physics and Engineering", summary:"Students apply 3D vector concepts to displacement, velocity, force equilibrium, and work problems.",
   resourceLabel:"Khan Academy", resourceUrl:"https://www.youtube.com/watch?v=ozwodzD5bte",
   quiz:[
     {q:"Resolving a force into components in 3D uses ___.", options:["trigonometry only","the dot product alone","only the magnitude of the force","F = Fₓi + F_yj + F_zk — decomposing the force vector into x, y, z components using direction cosines or given angles"], answer:3},
     {q:"For three forces to be in equilibrium, their vector sum must be ___.", options:["equal to the largest force","non-zero","pointing downward","zero: F₁ + F₂ + F₃ = 0 — equilibrium means no net force, so all components sum to zero"], answer:3},
     {q:"The scalar projection of a onto b is ___.", options:["|a||b|","a·b (the full dot product)","a×b","a·b̂ = a·b/|b| — the signed magnitude of a's component in the direction of b"], answer:3},
     {q:"The vector projection of a onto b is ___.", options:["a·b/|b|²","(a·b̂)b̂ = (a·b/|b|²)b — the component of a in the direction of b, as a vector","|a|cosθ","a × b"], answer:1},
     {q:"Work done by a force F over displacement d is ___.", options:["|F||d|","F × d (cross product — this gives a vector, not work)","F + d","W = F · d = |F||d|cosθ — only the component of force in the direction of displacement does work"], answer:3}
   ]},
  {subject:"Calculus", title:"Integration by Substitution", summary:"Students apply the substitution rule (u-substitution) to evaluate indefinite and definite integrals of composite functions.",
   resourceLabel:"Khan Academy Calculus", resourceUrl:"https://www.youtube.com/watch?v=-9M9P7xNDH4",
   quiz:[
     {q:"The substitution rule reverses ___.", options:["the product rule","the quotient rule","the power rule","the chain rule — if the integrand is of the form f(g(x))g'(x), let u = g(x), du = g'(x)dx, and integrate f(u)du"], answer:3},
     {q:"∫2x(x²+1)⁵ dx: let u = x²+1, du = 2x dx. The integral becomes ___.", options:["∫u⁵ du = u⁶/6 + C = (x²+1)⁶/6 + C","∫2xu⁵ du","∫u⁵ 2x dx","∫(x²+1)⁵ du"], answer:0},
     {q:"∫sin(3x) dx: let u = 3x, du = 3 dx. The integral = ___.", options:["−cos(3x)/3 + C (= ∫sin(u) du/3 = −cos(u)/3 + C)","−cos(3x) + C","cos(3x)/3 + C","−3cos(3x) + C"], answer:0},
     {q:"For a definite integral with substitution, you must ___.", options:["always change back to x before evaluating","never use substitution in definite integrals","keep the same limits of integration","either change the limits of integration to u-values, or substitute back to x before evaluating at original limits"], answer:3},
     {q:"∫[0 to 1] x·e^(x²) dx: let u = x², du = 2x dx. Limits: u(0)=0, u(1)=1. Result:", options:["∫[0 to 1] e^u du/2 = [e^u/2]₀¹ = (e−1)/2","e/2","(e−1)","e−1"], answer:0}
   ]},
  {subject:"Physics", title:"Optics: Reflection and Refraction", summary:"Students apply the law of reflection and Snell's Law to mirrors, lenses, and fibre optics; analyse total internal reflection.",
   resourceLabel:"Crash Course Physics", resourceUrl:"https://www.youtube.com/watch?v=_dBmNF_XBTU",
   quiz:[
     {q:"The law of reflection states ___.", options:["the angle of incidence and refraction are equal","light always reflects at 45°","reflected rays are always horizontal","the angle of incidence equals the angle of reflection, both measured from the normal to the surface"], answer:3},
     {q:"Snell's Law of refraction is ___.", options:["n₁cosθ₁ = n₂cosθ₂","n₁θ₁ = n₂θ₂","n₁/sinθ₁ = n₂/sinθ₂","n₁sinθ₁ = n₂sinθ₂ — where n is the index of refraction; light bends toward the normal when entering a denser medium"], answer:3},
     {q:"Total internal reflection occurs when ___.", options:["any light passes from air to glass","n₁ < n₂","the angle of refraction reaches 90° (critical angle sinθ_c = n₂/n₁) and beyond — light is entirely reflected back into the denser medium","light passes from glass to air at any angle"], answer:2},
     {q:"A converging (convex) lens ___.", options:["creates only virtual images","only works for objects at infinity","diverges parallel rays","converges parallel rays to a focal point; the thin lens equation 1/f = 1/dₒ + 1/dᵢ relates focal length, object distance, and image distance"], answer:3},
     {q:"Optical fibre works by ___.", options:["total reflection from metal coatings","only working in vacuum","absorption of light","total internal reflection — light is repeatedly totally internally reflected along the fibre, allowing lossless transmission of data over long distances"], answer:3}
   ]},
]},
{day:21, label:"Day 21 — Mon", subjects:[
  {subject:"English", title:"The Novel as Social Document: Realism and Its Discontents", summary:"Students examine realist novels and their sociological dimension — how fiction can document social reality while remaining art.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/watch?v=qGHBcRcPQeI",
   quiz:[
     {q:"Nineteenth-century realism in the novel aimed to ___.", options:["create pure fantasy worlds","avoid representing working-class life","focus only on aristocratic characters","represent society as it actually is — with documentary precision, attention to social class, economic conditions, and the quotidian lives of ordinary people, not just heroes and aristocrats"], answer:3},
     {q:"The sociological reading of a novel examines ___.", options:["only the author's biography","only plot and character","only style and form","how the novel reflects and critiques the social structures, ideologies, and class relations of its historical moment — what it can tell us about the world that produced it"], answer:3},
     {q:"A "condition of England" novel (like those by Dickens or Gaskell) characteristically ___.", options:["romanticises the past","avoids contemporary social problems","only follows middle-class characters","dramatises a contemporary social problem — poverty, industrialisation, factory conditions, child labour — as a way of drawing public attention to injustice"], answer:3},
     {q:"The danger of reading a novel only as a social document is ___.", options:["it always misidentifies the social context","it makes the novel more interesting","it is the correct approach","reducing the novel to a source of sociological information while ignoring its formal complexity, aesthetic achievements, and the ways form and content are inseparable"], answer:3},
     {q:"Contemporary fiction as social document includes ___.", options:["no claim to documentary accuracy","only "issues novels" without literary merit","only literary fiction set in the past","novels that address climate change, algorithmic culture, economic precarity, migration, and racial justice — fiction as a mode of social imagination that can reveal what statistics and journalism cannot"], answer:3}
   ]},
  {subject:"Advanced Functions", title:"Vectors: Applications to Navigation and Problem Solving", summary:"Students apply 3D vector techniques to navigation, structural problems, and multi-step applied problems.",
   resourceLabel:"Khan Academy", resourceUrl:"https://www.youtube.com/watch?v=ml4NSzCQobk",
   quiz:[
     {q:"A boat travels at 20 km/h in a river with current 5 km/h perpendicular. Its actual speed is ___.", options:["25 km/h","15 km/h","10 km/h","√(20² + 5²) = √425 ≈ 20.6 km/h — vector addition of boat velocity and current velocity"], answer:3},
     {q:"A plane heads north at 800 km/h; wind blows east at 100 km/h. The resultant speed is ___.", options:["900 km/h","√(800² + 100²) = √650000 ≈ 806 km/h","700 km/h","800 + 100 = 900 km/h (this adds speeds, not vectors)"], answer:1},
     {q:"Forces of 30 N north and 40 N east act on an object. The resultant force is ___.", options:["70 N","50 N at arctan(40/30) N of E — √(30²+40²) = 50 N; direction = arctan(E/N) from north","10 N","50 N due northeast"], answer:1},
     {q:"To find the angle between two 3D vectors a = (1,2,2) and b = (2,1,−2):", options:["cosθ = (2+2−4)/(3×3) = 0/9 = 0, so θ = 90° (perpendicular)","θ = 45°","θ = 60°","θ = 30°"], answer:0},
     {q:"A force of (3, 4, 0) N acts over displacement (1, 1, 5) m. Work done = ___.", options:["(3+4+0)(1+1+5) = 49 J","√(3²+4²+0²) J","3·1 + 4·1 + 0·5 = 7 J — dot product gives scalar work","3+4+1+1+5 = 14 J"], answer:2}
   ]},
  {subject:"Calculus", title:"Integration by Parts", summary:"Students apply the integration by parts formula to products of functions, including repeated application and tabular method.",
   resourceLabel:"Khan Academy Calculus", resourceUrl:"https://www.youtube.com/watch?v=2I-_SV8cwsw",
   quiz:[
     {q:"Integration by parts: ∫u dv = ___.", options:["uv − ∫u dv","u dv − v du","∫u dx + ∫dv","uv − ∫v du — derived from the product rule for differentiation"], answer:3},
     {q:"To integrate ∫x·eˣ dx, choose u = x, dv = eˣ dx. Then du = dx, v = eˣ. Result:", options:["x·eˣ − eˣ + C = eˣ(x−1) + C","x·eˣ + eˣ + C","x·eˣ + C","eˣ(x+1) + C"], answer:0},
     {q:"For ∫ln(x) dx, choose u = ln(x), dv = dx. Then du = 1/x dx, v = x. Result:", options:["x·ln(x) − x + C (= x ln(x) − ∫x · 1/x dx = x ln(x) − ∫1 dx)","ln(x)/x + C","x/ln(x) + C","ln(x) + C"], answer:0},
     {q:"∫x²·sin(x) dx requires ___.", options:["one application of parts","u-substitution only","no special technique","two applications of integration by parts (or the tabular method) — the power of x reduces each time until only sin(x) remains"], answer:3},
     {q:"The mnemonic LIATE suggests choosing u as ___.", options:["the function that differentiates to zero","the last function in the product","the exponential always","the function that comes first in: Logarithm, Inverse trig, Algebraic, Trig, Exponential — generally the "earlier" choice makes du simpler"], answer:3}
   ]},
  {subject:"Physics", title:"The Photoelectric Effect and Wave-Particle Duality", summary:"Students examine the photoelectric effect, photon model of light, and the evidence for wave-particle duality.",
   resourceLabel:"Crash Course Physics", resourceUrl:"https://www.youtube.com/watch?v=kcSYV8bZhjc",
   quiz:[
     {q:"The photoelectric effect is the emission of electrons from a metal surface when ___.", options:["a current is applied to the metal","the metal is heated sufficiently","the metal is cooled to absolute zero","light of sufficient frequency illuminates the metal — demonstrating that light transfers energy in discrete quanta (photons)"], answer:3},
     {q:"Classical wave theory failed to explain the photoelectric effect because ___.", options:["it predicted no electrons would be emitted","it correctly predicted everything","it predicted only red light would work","it predicted that any frequency of light would eject electrons given enough intensity — but experiment showed frequency, not intensity, determines if electrons are ejected"], answer:3},
     {q:"Einstein's explanation of the photoelectric effect (1905) proposed ___.", options:["light is purely a particle with no wave properties","the metal surface is the key factor","the current from the battery ejects electrons","light energy comes in discrete packets (photons) of energy E = hf — below the threshold frequency, no single photon has enough energy to eject an electron regardless of intensity"], answer:3},
     {q:"De Broglie's hypothesis proposed that matter also has wave properties: λ = ___.", options:["h/(mv) = h/p — the de Broglie wavelength of a particle with momentum p; confirmed experimentally by electron diffraction","h/f","h × mv","mv/h"], answer:0},
     {q:"Wave-particle duality means ___.", options:["only light can be a wave","only electrons can be particles","quantum objects are neither waves nor particles","quantum objects exhibit wave behaviour (interference, diffraction) in some experiments and particle behaviour (discrete energy, localised detection) in others — the nature of the observation determines which aspect is revealed"], answer:3}
   ]},
]},
{day:22, label:"Day 22 — Tue", subjects:[
  {subject:"English", title:"Short Fiction Masterworks: Structure, Voice, and Compression", summary:"Students study canonical short stories, examining how compressed form demands particular mastery of voice, structure, epiphany, and economy of language.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/watch?v=dtRCMONW8bQ",
   quiz:[
     {q:"The short story differs from the novel in that ___.", options:["it is always easier to write","it has no character development","it can never achieve the depth of a novel","it demands absolute economy — every word must work; there is no space for subplots, extended development, or leisurely description — the form itself creates pressure"], answer:3},
     {q:"The "epiphany" in Joyce's short fiction (from "Dubliners") refers to ___.", options:["a religious experience only","a surprise plot twist","the story's happy ending","a moment of sudden insight or revelation — often quiet and internal — when a character perceives something essential about themselves or their situation"], answer:3},
     {q:"Point of view in a short story is especially important because ___.", options:["first person is always best","third person is always better","point of view has no relation to meaning","the limited space means the narrative voice is almost everything — the angle from which the story is told determines what is knowable, what is visible, and what the reader can understand"], answer:3},
     {q:"Chekhov's famous "gun" principle states ___.", options:["every story needs violence","guns are important in Russian fiction","stories should be realistic only","if a gun is shown in the first act, it must be fired by the third — dramatic economy requires that every element introduced must be relevant; details are significant precisely because they are selected"], answer:3},
     {q:"Compression in short fiction achieves ___.", options:["nothing that a longer story could not do better","less than the novel in all respects","only brevity without depth","a different kind of intensity — the reader carries more weight; implication, suggestion, and what is left unsaid become as important as what is stated, creating resonant ambiguity"], answer:3}
   ]},
  {subject:"Advanced Functions", title:"Counting Principles and Permutations", summary:"Students apply the fundamental counting principle, permutations (with and without repetition), and circular permutations to combinatorics problems.",
   resourceLabel:"Khan Academy", resourceUrl:"https://www.youtube.com/watch?v=XqQTXW7XfYA",
   quiz:[
     {q:"The fundamental counting principle: if event A can occur in m ways and event B in n ways, then A then B can occur in ___.", options:["m + n ways (addition applies when events are mutually exclusive alternatives)","m × n ways — the multiplication principle: each choice for A pairs with each choice for B","m! ways","m − n ways"], answer:1},
     {q:"The number of permutations of n distinct objects taken r at a time is ___.", options:["n!/(n−r)!... = nPr","n!/r!","nCr = n!/(r!(n−r)!)","n!"], answer:0},
     {q:"How many 4-digit PINs have no repeated digits?", options:["10 × 9 × 8 × 7 = 5040 (=10P4)","10⁴ = 10000","10 × 9 × 8 = 720","4! = 24"], answer:0},
     {q:"In how many ways can 5 people sit at a round table?", options:["5! = 120","(5−1)! = 4! = 24 — circular permutations fix one position to account for rotational equivalence","5!/5 = 24","5"], answer:1},
     {q:"If 3 of 8 books must always be together, the number of arrangements on a shelf is ___.", options:["8! arrangements","3! × 6! (treat the 3 as a block: 6! arrangements of 6 items × 3! internal arrangements of the block)","6! only","3! × 8!"], answer:1}
   ]},
  {subject:"Calculus", title:"Volumes of Solids of Revolution: Advanced", summary:"Students compute volumes using disc/washer and shell methods, and apply the methods to multi-region problems.",
   resourceLabel:"Khan Academy Calculus", resourceUrl:"https://www.youtube.com/watch?v=EFkEnCYdVAU",
   quiz:[
     {q:"The washer method for a solid between y=f(x) and y=g(x) (f≥g) rotated about x-axis gives ___.", options:["V = π∫[f(x)−g(x)]² dx","V = π∫[f(x)+g(x)] dx","V = 2π∫x[f(x)−g(x)] dx","V = π∫{[f(x)]² − [g(x)]²} dx — subtract the inner circle (g) from the outer circle (f)"], answer:3},
     {q:"Find the volume when the region between y=x and y=x² (0≤x≤1) is rotated about the x-axis.", options:["V = π∫₀¹(x² − x⁴)dx = π[x³/3 − x⁵/5]₀¹ = π(1/3−1/5) = 2π/15","V = π/6","V = π/3","V = π/15"], answer:0},
     {q:"The shell method integrates ___ when rotating about the y-axis.", options:["horizontal strips of width dy","the radius squared","circular discs perpendicular to y","vertical shells: V = 2π∫x·f(x) dx from a to b — shell radius = x, shell height = f(x)"], answer:3},
     {q:"Choosing between disc/washer and shell methods: prefer shells when ___.", options:["always preferring shells","the function has no closed form","only for linear functions","solving for x in terms of y would be difficult — shells allow integration in x even when rotating about y"], answer:3},
     {q:"The volume of a sphere of radius r by discs: V = π∫[-r to r](r²−x²) dx = ___.", options:["4πr²/3","πr³","4πr³/3 ✓ — [π(r²x − x³/3)] from −r to r = π(r³−r³/3) − π(−r³+r³/3) = 4πr³/3","2πr³"], answer:2}
   ]},
  {subject:"Physics", title:"Atomic Structure and Quantum Numbers", summary:"Students examine the Bohr model, quantum mechanical model, and electron configurations using quantum numbers.",
   resourceLabel:"Crash Course Physics", resourceUrl:"https://www.youtube.com/watch?v=Ewf6RuLlSvc",
   quiz:[
     {q:"The Bohr model of the hydrogen atom correctly predicted ___.", options:["the spectra of all elements","the 3D shape of orbitals","the Zeeman effect","the discrete emission spectrum of hydrogen — electrons occupy fixed energy levels, and photon emission corresponds to electron transitions between levels: ΔE = hf"], answer:3},
     {q:"The principal quantum number n determines ___.", options:["the spin of the electron","the magnetic orientation of the orbital","the shape of the orbital","the energy level and size of the orbital — n = 1, 2, 3, ... with higher n meaning higher energy and larger radius"], answer:3},
     {q:"The four quantum numbers (n, l, mₗ, mₛ) together specify ___.", options:["only the energy of the electron","only the orbital shape","only the spin orientation","a unique quantum state for each electron in an atom — the Pauli Exclusion Principle states no two electrons can share the same set of four quantum numbers"], answer:3},
     {q:"The Heisenberg Uncertainty Principle states ___.", options:["measurement has no effect on quantum systems","electrons move in defined circular orbits","quantum mechanics is only approximate","Δx × Δp ≥ ℏ/2 — the more precisely we know a particle's position, the less precisely we can know its momentum, and vice versa; this is a fundamental feature of nature, not a limitation of our instruments"], answer:3},
     {q:"Electron configuration of carbon (Z=6) following Aufbau principle is ___.", options:["1s¹2s²2p³","1s²2s²2p² — 2 electrons in 1s, 2 in 2s, 2 in 2p (Hund's rule: they enter different 2p orbitals with parallel spins)","1s²2s¹2p³","1s²2p⁴"], answer:1}
   ]},
]},
{day:23, label:"Day 23 — Wed", subjects:[
  {subject:"English", title:"Documentary and Non-Fiction: Truth, Form, and Ethics", summary:"Students examine documentary film and literary non-fiction (creative non-fiction, journalism) — exploring how non-fiction makes arguments and ethical obligations to truth.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/watch?v=2HqT7QbVCnc",
   quiz:[
     {q:"Documentary film differs from fiction film in that ___.", options:["documentary has no narrative structure","documentary is always objective","documentary uses no cinematic technique","documentary claims a relationship to actual events and people — but this claim does not mean documentary is neutral or unmediated; every documentary makes choices that shape the audience's understanding"], answer:3},
     {q:"Rhetorical strategies in documentary include ___.", options:["no rhetorical strategies","only factual presentation","only verbal argument","interview selection, ordering of footage, music and sound, narration, juxtaposition — all of which guide the viewer toward a particular interpretation while appearing merely to present facts"], answer:3},
     {q:"Creative non-fiction (e.g., literary journalism, memoir, personal essay) ___.", options:["has no responsibility to truth","is always more subjective than journalism","should avoid literary techniques","uses the techniques of fiction (scene, character, voice, imagery, structure) in the service of factual content — but maintains an ethical obligation to truth that fiction does not"], answer:3},
     {q:"The ethics of documentary representation include ___.", options:["no ethical obligations since subjects consented","only legal considerations","no issue if filming in public spaces","obligations around consent, fair representation, potential harm to subjects, and the power differential between filmmaker and subject — particularly when filming vulnerable communities"], answer:3},
     {q:"Analysing a documentary as a text means ___.", options:["accepting it as a neutral truth document","only checking factual accuracy","only watching without analysis","examining its rhetorical strategies, cinematic choices, ideological assumptions, and the relationship between its claims and the evidence it presents — treating it as an argument, not just a record"], answer:3}
   ]},
  {subject:"Advanced Functions", title:"Combinations and the Binomial Theorem", summary:"Students calculate combinations, apply Pascal's triangle, and expand binomials using the Binomial Theorem.",
   resourceLabel:"Khan Academy", resourceUrl:"https://www.youtube.com/watch?v=Eu2oYKiPxu0",
   quiz:[
     {q:"The number of combinations of n objects taken r at a time is ___.", options:["n!/r!","n!/(n−r)!","n!","C(n,r) = n!/(r!(n−r)!) — order does not matter in combinations; fewer than permutations by a factor of r!"], answer:3},
     {q:"How many ways can a committee of 3 be chosen from 10 people?", options:["10!/3! = 604800","10P3 = 720","C(10,3) = 10!/(3!7!) = 120","10 × 3 = 30"], answer:2},
     {q:"The Binomial Theorem states (a+b)ⁿ = ___.", options:["aⁿ + bⁿ only","n·aⁿ⁻¹b + aⁿ","∑ C(n,k) aᵏbⁿ⁻ᵏ","∑[k=0 to n] C(n,k) aⁿ⁻ᵏ bᵏ — a sum of n+1 terms with binomial coefficients from Pascal's triangle"], answer:3},
     {q:"The term with b³ in (2x + 3)⁵ is ___.", options:["C(5,3)(2x)²(3)³ = 10 × 4x² × 27 = 1080x²","C(5,2)(2x)³(3)²","C(5,3)(2x)³(3)²","C(5,3)(2x)²(3)³ = 1080x²"], answer:0},
     {q:"Pascal's triangle has the property that ___.", options:["C(n,r) = C(n,r−1) + C(n,r+1)","C(n,r) = C(n−1,r)","each entry is the sum of all entries above","C(n,r) = C(n−1,r−1) + C(n−1,r) — each entry is the sum of the two entries above it"], answer:3}
   ]},
  {subject:"Calculus", title:"Numerical Integration: Riemann Sums and the Trapezoid Rule", summary:"Students approximate definite integrals using Riemann sums, the Trapezoid Rule, and Simpson's Rule.",
   resourceLabel:"Khan Academy Calculus", resourceUrl:"https://www.youtube.com/watch?v=YTKQswb60Pw",
   quiz:[
     {q:"A Riemann sum approximates a definite integral by ___.", options:["using the antiderivative","differentiating at sample points","only using the left endpoint always","summing the areas of rectangles; left, right, and midpoint Riemann sums use different sample points within each subinterval"], answer:3},
     {q:"The Trapezoid Rule approximates ∫f dx using ___.", options:["only left-endpoint rectangles","the average of f(a) and f(b) only","only the area of one trapezoid","trapezoids instead of rectangles: T = (h/2)[f(x₀)+2f(x₁)+...+2f(xₙ₋₁)+f(xₙ)] where h = (b−a)/n"], answer:3},
     {q:"Simpson's Rule (n even) is ___.", options:["only the midpoint rule","the same as the trapezoid rule","only used for linear functions","(h/3)[f(x₀)+4f(x₁)+2f(x₂)+4f(x₃)+...+4f(xₙ₋₁)+f(xₙ)] — alternating coefficients 4 and 2; generally more accurate than trapezoid"], answer:3},
     {q:"Numerical integration is necessary when ___.", options:["the function is always integrable","only for physics problems","you cannot use the FTC","the antiderivative cannot be expressed in closed form — many real-world functions (e.g., e^(−x²), √(1+x³)) have no elementary antiderivative"], answer:3},
     {q:"As the number of subintervals n → ∞, all Riemann sum approximations ___.", options:["diverge","approach different limits","remain the same","converge to the exact value of the definite integral — this is precisely the definition of the Riemann integral"], answer:3}
   ]},
  {subject:"Physics", title:"Nuclear Reactions: Fission, Fusion, and Radioactive Decay", summary:"Students analyse nuclear reactions, calculate binding energy per nucleon, and apply decay equations.",
   resourceLabel:"Crash Course Physics", resourceUrl:"https://www.youtube.com/watch?v=nRmBsxBpTjs",
   quiz:[
     {q:"Radioactive decay follows ___.", options:["a linear decrease in activity","a quadratic decay law","constant activity indefinitely","an exponential law: N(t) = N₀e^(−λt), where λ is the decay constant; after each half-life, half the remaining nuclei have decayed"], answer:3},
     {q:"Half-life T½ is related to decay constant λ by ___.", options:["T½ = λ","T½ = 1/λ","T½ = e^λ","T½ = ln2/λ = 0.693/λ — solving N₀/2 = N₀e^(−λT½)"], answer:3},
     {q:"Binding energy per nucleon peaks at ___.", options:["uranium-238 (heaviest stable nucleus)","hydrogen-1 (lightest)","carbon-12 (organic life basis)","iron-56 — nuclei lighter than iron release energy by fusion; nuclei heavier than iron release energy by fission; this is why both processes release energy"], answer:3},
     {q:"Carbon-14 dating works because ___.", options:["C-14 is created only in labs","C-14 is stable indefinitely","C-14 is the most common carbon isotope","C-14 is produced at a constant rate in the atmosphere by cosmic rays and incorporated into living organisms; after death, C-14 decays with T½ ≈ 5730 years, allowing age determination"], answer:3},
     {q:"The Q-value of a nuclear reaction is ___.", options:["the quantity of material used","the quality of the nuclear fuel","the charge of the nucleus","the energy released: Q = (mass of reactants − mass of products) × c²; positive Q means energy is released (exothermic)"], answer:3}
   ]},
]},
{day:24, label:"Day 24 — Thu", subjects:[
  {subject:"English", title:"Contemporary Drama: Stagecraft and Text", summary:"Students examine a contemporary play, analysing the relationship between the written text and its realisation in performance.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/watch?v=W3MJj5AjAMc",
   quiz:[
     {q:"A play script is ___.", options:["the complete work of art in itself","less important than the director's vision","always the same in any production","a blueprint for performance — the text is indeterminate until realised; staging choices, casting, design, and acting all complete the work the playwright began"], answer:3},
     {q:"Stage directions in a contemporary play ___.", options:["are always followed literally","are always ignored by directors","tell audiences what to think","may be poetic, ambiguous, or minimal — some playwrights (Beckett, Pinter) make stage directions part of the artistic text; others leave maximum freedom to the director and designer"], answer:3},
     {q:"Theatre's relationship to contemporary politics includes ___.", options:["avoidance of political content","only historical political subjects","documentary theatre only","verbatim theatre (using real testimony), protest theatre, community-based theatre, and mainstream drama that addresses current social and political questions"], answer:3},
     {q:"Analysing a contemporary play without seeing it in production requires ___.", options:["imagining a specific production as if it were the only one","admitting analysis is impossible without performance","only reading the dialogue as prose","imaginative performance reading — envisioning how the text could be staged, what choices are available, and how different productions might emphasise different aspects of the text"], answer:3},
     {q:"The most important question when analysing a scene in a contemporary play is ___.", options:["what happens in the plot","what time period is the play set in","how many characters appear","what does each character want in this scene, and what theatrical means are used to create or frustrate that desire — dramatic action is always about want and obstacle"], answer:3}
   ]},
  {subject:"Advanced Functions", title:"Probability Distributions: Binomial and Geometric", summary:"Students work with discrete probability distributions — binomial and geometric — applying formulas and interpreting results.",
   resourceLabel:"Khan Academy", resourceUrl:"https://www.youtube.com/watch?v=J8jNoF-K8Z8",
   quiz:[
     {q:"The binomial distribution applies when ___.", options:["trials have more than two outcomes","probability changes each trial","only one trial is performed","there are n independent identical trials, each with two outcomes (success/failure), and probability of success p is constant — counting the number of successes X"], answer:3},
     {q:"P(X=k) for a binomial distribution is ___.", options:["C(n,k) × pᵏ × (1−p)^n","p^k × (1-p)^(n-k)","C(n,k) × pᵏ × (1−p)^(n−k) — choosing which k trials succeed times the probability of that pattern","n × p × k"], answer:2},
     {q:"For a binomial random variable X ~ B(n,p), E(X) = ___.", options:["np(1−p)","n/p","p/n","np — the expected number of successes in n trials; variance is np(1−p)"], answer:3},
     {q:"The geometric distribution models ___.", options:["the number of successes in n trials","only continuous random variables","the probability of exactly one success","the number of trials until the first success: P(X=k) = (1−p)^(k−1) × p; E(X) = 1/p"], answer:3},
     {q:"A quality control check has 5% defective rate. Find P(exactly 2 defective in 20 items).", options:["C(20,2)(0.05)²(0.95)¹⁸ ≈ 0.189","(0.05)² × 20","C(20,2)(0.05)²","2/20 = 0.10"], answer:0}
   ]},
  {subject:"Calculus", title:"Differential Equations: Growth, Decay, and Newton's Law", summary:"Students solve separable ODEs applied to exponential growth, radioactive decay, and Newton's Law of Cooling.",
   resourceLabel:"Khan Academy Calculus", resourceUrl:"https://www.youtube.com/watch?v=H0VEL9TFjqw",
   quiz:[
     {q:"The general solution of dP/dt = kP is ___.", options:["P(t) = P₀ + kt","P(t) = ke^(P₀t)","P(t) = P₀kt","P(t) = P₀e^(kt) — separate, integrate both sides: ∫dP/P = ∫k dt → ln P = kt + C → P = Ae^(kt)"], answer:3},
     {q:"A culture of 1000 bacteria doubles in 3 hours. After 9 hours:", options:["8000 (doubles 3 times: ×2×2×2 = 8; 1000 × 8 = 8000)","6000","3000","2000"], answer:0},
     {q:"Radioactive decay: dN/dt = −λN. Given N₀ = 400 and T½ = 5 years, after 10 years N = ___.", options:["400 × (1/2)² = 100 (two half-lives)","200","400 − 2λ","400e^(−10)"], answer:0},
     {q:"Newton's Law of Cooling: T(t) = T_env + (T₀ − T_env)e^(−kt). A 90°C coffee in a 20°C room cools to 70°C in 10 min. After 30 more minutes T ≈ ___.", options:["solve: 70=20+(90−20)e^(−10k) → e^(−10k)=5/7; T(40)=20+70e^(−40k)=20+70(5/7)⁴ ≈ 20+70×0.26=38°C","50°C","60°C","45°C"], answer:0},
     {q:"A differential equation is separable if ___.", options:["it involves only one variable","its solution is always exponential","it has constant coefficients","it can be written as dy/g(y) = f(x) dx — the variables can be completely separated to opposite sides before integrating"], answer:3}
   ]},
  {subject:"Physics", title:"Modern Physics: Quantum Mechanics and the Standard Model", summary:"Students examine the probabilistic nature of quantum mechanics, wave functions, and an overview of the Standard Model.",
   resourceLabel:"Crash Course Physics", resourceUrl:"https://www.youtube.com/watch?v=p7bzE1E5PMY",
   quiz:[
     {q:"The wave function ψ(x,t) in quantum mechanics gives ___.", options:["the exact position of the particle","the energy of the particle directly","the actual path of the particle","the probability amplitude — |ψ|² gives the probability density of finding the particle at position x at time t"], answer:3},
     {q:"The Schrödinger equation is ___.", options:["a statement of conservation of energy","only applicable to classical waves","only for relativistic particles","the fundamental equation of quantum mechanics — describing how the wave function evolves in time; solving it gives the allowed quantum states and their energies"], answer:3},
     {q:"Quantum tunnelling allows ___.", options:["particles to exceed the speed of light","energy conservation to be violated","only photons to pass through barriers","particles to pass through potential barriers that classical mechanics would prohibit — explained by the non-zero probability amplitude on the far side of the barrier; crucial in nuclear fusion and semiconductor devices"], answer:3},
     {q:"The Standard Model classifies matter as composed of ___.", options:["atoms and molecules only","protons and neutrons only","photons and electrons only","quarks (making up protons, neutrons) and leptons (electrons, neutrinos) — interacting via bosons: photons (EM), W/Z bosons (weak), gluons (strong)"], answer:3},
     {q:"The unresolved problems in the Standard Model include ___.", options:["no unresolved problems","only cosmological questions","only mathematical issues","no quantum description of gravity, no explanation of dark matter or dark energy, and no explanation of the matter-antimatter asymmetry in the universe"], answer:3}
   ]},
]},
{day:25, label:"Day 25 — Fri", subjects:[
  {subject:"English", title:"Research Essay Workshop: Drafting and Peer Review", summary:"Students workshop research essay drafts in a peer-review setting, applying structured feedback protocols and revising for argument, evidence, and style.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/watch?v=8eB7SSNC5ys",
   quiz:[
     {q:"Peer review is most valuable when ___.", options:["reviewers focus only on grammar","reviewers are lenient to encourage the writer","reviewers only praise the essay","reviewers respond as genuine readers — identifying where the argument is unclear, where evidence is unconvincing, where the analysis is superficial — providing the response a real academic reader would give"], answer:3},
     {q:"The most important question to ask about a research essay draft is ___.", options:["is the Works Cited formatted correctly?","is the essay long enough?","are there enough quotations?","does each paragraph contribute to a single unified argument, and does the evidence actually support the specific claim made in each paragraph?"], answer:3},
     {q:"Revising an essay is different from editing in that ___.", options:["editing is more important","they are the same process","revising is only fixing grammar","revising involves reconsidering the argument, structure, and evidence — making major changes to content and organisation; editing addresses sentence-level clarity and correctness"], answer:3},
     {q:"When evidence does not support your claim, the correct response is ___.", options:["delete the evidence","misrepresent the evidence to fit","ignore the problem","revise either the claim to match the evidence, or find better evidence for the existing claim — intellectual honesty requires alignment between claim and evidence"], answer:3},
     {q:"Academic voice in a research essay is characterised by ___.", options:["only long, complex sentences","avoiding the first person always","only formal vocabulary","precision, economy, and analytical clarity — making specific, defensible claims; avoiding vague assertions; using evidence not to decorate but to prove; maintaining a consistently critical and engaged voice"], answer:3}
   ]},
  {subject:"Advanced Functions", title:"Probability: Conditional Probability and Independence", summary:"Students apply conditional probability, Bayes' Theorem, and independence to complex probability problems.",
   resourceLabel:"Khan Academy", resourceUrl:"https://www.youtube.com/watch?v=H02B3aMNKzE",
   quiz:[
     {q:"Conditional probability P(A|B) = ___.", options:["P(A) + P(B)","P(A) × P(B)","P(A)/P(B)","P(A∩B)/P(B) — the probability of A given that B has occurred; restricts the sample space to outcomes in B"], answer:3},
     {q:"Events A and B are independent if and only if ___.", options:["P(A) = P(B)","P(A∩B) = 0","P(A) + P(B) = 1","P(A|B) = P(A), equivalently P(A∩B) = P(A)P(B) — knowing B occurred gives no information about A"], answer:3},
     {q:"Bayes' Theorem: P(A|B) = ___.", options:["P(B|A)/P(A)","P(A|B) = P(A)P(B)","P(B|A)×P(A)×P(B)","P(B|A)×P(A) / P(B) — allows updating probability of A given new evidence B"], answer:3},
     {q:"A medical test has 99% sensitivity (P(+|disease)) and 95% specificity (P(−|no disease)). Prevalence = 1%. P(disease | positive test) ≈ ___.", options:["≈ 16.7% (Bayes: P(D|+) = 0.99×0.01/(0.99×0.01+0.05×0.99) ≈ 0.0099/0.059 ≈ 0.167)","≈ 99%","≈ 50%","≈ 5%"], answer:0},
     {q:"The multiplication rule for conditional probability: P(A∩B) = ___.", options:["P(A) + P(B) − P(A∪B)","P(A)×P(B) always","P(A|B) − P(B)","P(A)×P(B|A) = P(B)×P(A|B) — either form works; the second factor is the conditional probability of the second event given the first"], answer:3}
   ]},
  {subject:"Calculus", title:"Arc Length and Surface Area", summary:"Students calculate arc lengths of curves and surface areas of solids of revolution using integration.",
   resourceLabel:"Khan Academy Calculus", resourceUrl:"https://www.youtube.com/watch?v=PwmqebSqc_s",
   quiz:[
     {q:"The arc length of y = f(x) from a to b is ___.", options:["∫[a to b]√(1+[f(x)]²) dx","∫[a to b]f(x) dx","∫[a to b](1+f(x)) dx","∫[a to b]√(1+[f'(x)]²) dx — derived from approximating the curve by infinitesimal line segments ds = √(dx²+dy²)"], answer:3},
     {q:"Find the arc length of y = x³/² from x=0 to x=4.", options:["∫[0 to 4]√(1+(3x^(1/2)/2)²) dx = ∫√(1+9x/4) dx — solved by substitution; ≈ 9.07","∫√(1+x³) dx","4³/² = 8","4 × √(1+9) = 4√10"], answer:0},
     {q:"Surface area of y=f(x) rotated about x-axis from a to b is ___.", options:["2π∫f(x) dx","π∫[f(x)]² dx (this is volume by discs)","π∫f(x)√(1+[f'(x)]²) dx","2π∫f(x)√(1+[f'(x)]²) dx — sum of infinitesimal bands of circumference 2πf(x) and slant height ds"], answer:3},
     {q:"These formulas require that f(x) is ___.", options:["only integrable","only continuous","always positive","continuously differentiable (f' continuous) on [a,b] — so that ds = √(1+[f'(x)]²)dx is well-defined"], answer:3},
     {q:"For a circle of radius r (parametrically x=rcosθ, y=rsinθ), the arc length (circumference) formula gives ___.", options:["2πr² (this is area)","πr²","πr","2πr — ∫[0 to 2π]√((−rsinθ)²+(rcosθ)²) dθ = ∫[0 to 2π]r dθ = 2πr ✓"], answer:3}
   ]},
  {subject:"Physics", title:"Medical and Applied Physics", summary:"Students see how physics principles apply to medicine — X-rays, MRI, PET scans, ultrasound, and radiation therapy.",
   resourceLabel:"Crash Course Physics", resourceUrl:"https://www.youtube.com/watch?v=cMJpFjmJZ9s",
   quiz:[
     {q:"X-rays penetrate soft tissue but are absorbed by bone because ___.", options:["X-rays are repelled by calcium","bone is harder than soft tissue","bone is denser and contains calcium which absorbs X-rays more strongly — the differential absorption creates the radiographic image","X-rays cannot travel through any material"], answer:2},
     {q:"MRI (Magnetic Resonance Imaging) uses ___.", options:["X-rays with computer processing","radioactive tracers","ultrasound at very high frequencies","the magnetic properties of hydrogen nuclei (protons) — a strong magnetic field aligns them, then radiofrequency pulses disturb the alignment; detecting the return to equilibrium creates images of soft tissue"], answer:3},
     {q:"PET (Positron Emission Tomography) works by ___.", options:["using external X-ray sources","using a magnetic field to image organs","measuring sound waves inside the body","detecting gamma rays from positron-electron annihilation — a positron-emitting tracer is injected, and annihilation events (producing paired gamma rays) reveal metabolic activity"], answer:3},
     {q:"Ultrasound imaging uses ___.", options:["gamma radiation","visible light","infrared radiation","high-frequency sound waves (1–20 MHz) — reflected differently by tissues of different density; safe for foetal imaging because it uses no ionising radiation"], answer:3},
     {q:"Radiation therapy targets cancer because ___.", options:["only cancer cells absorb radiation","radiation has no side effects","normal cells cannot be harmed by radiation","ionising radiation damages DNA, killing rapidly dividing cells (cancer cells divide faster than most normal cells) — but normal tissue damage is a significant side effect requiring careful dosing and targeting"], answer:3}
   ]},
]},
{day:26, label:"Day 26 — Mon", subjects:[
  {subject:"English", title:"Oral Communication: Seminar and Academic Discussion", summary:"Students prepare for and participate in a formal Socratic seminar, developing skills in academic discussion, active listening, and building on others' ideas.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/watch?v=bPkHcTk55Vc",
   quiz:[
     {q:"A Socratic seminar is characterised by ___.", options:["the teacher asking all the questions","competitive debate with winners","only one student speaking at a time","open-ended discussion in which students build on each other's ideas, ask genuine questions, and arrive at deeper understanding through collaborative inquiry"], answer:3},
     {q:"Effective academic discussion requires ___.", options:["talking as much as possible","always agreeing with the previous speaker","never asking questions during someone's turn","active listening — being able to summarise what the previous speaker said before responding, engaging with their actual argument rather than changing the subject"], answer:3},
     {q:"To advance a seminar discussion, a student should ___.", options:["only repeat what they prepared","introduce a new topic unrelated to the discussion","ask for more clarification","build on a previous contribution, extend an idea, respectfully challenge an assertion with evidence, or introduce a complicating example that tests the group's emerging understanding"], answer:3},
     {q:"The purpose of requiring textual evidence in a seminar is ___.", options:["to show you did the reading","to fill time in the discussion","to penalise students who didn't prepare","to ground claims in specific textual detail — preventing discussion from floating into vague assertion, and ensuring claims about texts are based on what texts actually say and do"], answer:3},
     {q:"The highest level of seminar participation involves ___.", options:["speaking longest","making the most points","never asking questions","asking a question that genuinely opens up new thinking for the group — the best seminar contributions change the direction of the discussion productively"], answer:3}
   ]},
  {subject:"Advanced Functions", title:"Advanced Functions: Comprehensive Review", summary:"Students review the full MHF4U course with examination-level practice problems spanning all strands.",
   resourceLabel:"Khan Academy", resourceUrl:"https://www.youtube.com/watch?v=MKQR_acrFOA",
   quiz:[
     {q:"A function f has an inverse f⁻¹ if and only if ___.", options:["f is continuous","f is differentiable","f is defined for all x","f is one-to-one (passes the horizontal line test) — a bijection from its domain to its range, so the inverse is also a function"], answer:3},
     {q:"Solve: log₂(x+1) − log₂(x−1) = 3.", options:["x = 9/7: log₂((x+1)/(x−1)) = 3 → (x+1)/(x−1) = 8 → x+1 = 8x−8 → 9 = 7x → x = 9/7... check: x−1 = 2/7 > 0 ✓","x = 3","x = 7","x = 9"], answer:0},
     {q:"The dot product of a = (1,−2,3) and b = (4,1,−2) is ___.", options:["4−2+6 = 8... no: 1×4+(−2)×1+3×(−2) = 4−2−6 = −4","4 + 2 − 6 = 0","1×4−2×1+3×2 = 8","−4 (1×4 + (−2)×1 + 3×(−2) = 4−2−6 = −4)"], answer:3},
     {q:"The general term of the expansion (3x−2)⁶ containing x⁴ is ___.", options:["C(6,2)(3x)⁴(−2)² = 15 × 81x⁴ × 4 = 4860x⁴","C(6,4)(3x)⁴(−2)² = 15 × 81x⁴ × 4 = 4860x⁴","C(6,2)(3x)⁴(2)² = 4860x⁴","C(6,4)(3x)⁴(−2)² — note: term with x⁴ has k=4 in (3x)^(6−k)(−2)^k: k=2 → C(6,2)(3x)⁴(−2)² = 15×81×4 x⁴ = 4860x⁴"], answer:3},
     {q:"In how many ways can the letters of MISSISSIPPI be arranged?", options:["11!/4!4!2! = 34650 (11 letters: 1M, 4I, 4S, 2P)","11!","11!/4!4!","11!/4!"], answer:0}
   ]},
  {subject:"Calculus", title:"Calculus: Comprehensive Review", summary:"Students review the full calculus course with examination-level problems on limits, derivatives, and integrals.",
   resourceLabel:"Khan Academy Calculus", resourceUrl:"https://www.youtube.com/watch?v=HEH_oKNLgUU",
   quiz:[
     {q:"Find the derivative of f(x) = x²·sin(3x).", options:["f'(x) = 2x·sin(3x) + x²·3cos(3x) = 2x sin(3x) + 3x²cos(3x) (product rule)","f'(x) = 2x·cos(3x)","f'(x) = x²·3cos(3x)","f'(x) = 2x·sin(3x) + x²·cos(3x)"], answer:0},
     {q:"A box with square base (side x) and no top has surface area 108 cm². Maximise volume. V = x²h, 4xh+x² = 108 → h = (108−x²)/(4x). V(x) = ___.", options:["V = x²(108−x²)/(4x) = x(108−x²)/4 = 27x − x³/4; V'= 27−3x²/4 = 0 → x² = 36 → x = 6; V_max = 6×(108−36)/24 = 6×3 = 108 cm³","V = 108x","V = x³/4","V = 27x²"], answer:0},
     {q:"∫[1 to e] (ln x)/x dx = ___.", options:["[let u=ln x, du=1/x dx: ∫₀¹ u du = u²/2|₀¹ = 1/2]","ln(e)/e = 1/e","1","e"], answer:0},
     {q:"The area enclosed by y = x² and y = 2x is ___.", options:["∫[0 to 2](2x−x²) dx = [x²−x³/3]₀² = 4−8/3 = 4/3","2/3","8/3","4/3"], answer:3},
     {q:"Solve: dy/dx = x/y; y(0) = 2.", options:["y dy = x dx; ∫y dy = ∫x dx; y²/2 = x²/2 + C; at (0,2): C = 2; y² = x² + 4; y = √(x²+4)","y = x²/2 + 2","y = xe^x + 2","y = 2e^(x²/2)"], answer:0}
   ]},
  {subject:"Physics", title:"Physics: Comprehensive Review", summary:"Students review the full SPH4U course with examination-level multi-concept problems.",
   resourceLabel:"Crash Course Physics", resourceUrl:"https://www.youtube.com/watch?v=pGj9isFr21U",
   quiz:[
     {q:"A 1500 kg car accelerates from 0 to 25 m/s in 10 s up a 10° incline (μₖ = 0.1). Net force required:", options:["F_net = ma + mg sinθ + μₖmg cosθ = 1500(2.5) + 1500(9.8)(0.174) + 0.1×1500×9.8×0.985 ≈ 3750+2557+1447 ≈ 7754 N","F = 1500 × 2.5 = 3750 N","F = mg sinθ only","F = ma only"], answer:0},
     {q:"A spring (k=400 N/m) is compressed 0.2 m and launches a 0.1 kg ball. Speed at launch:", options:["½kx² = ½mv²; v = x√(k/m) = 0.2√4000 ≈ 12.6 m/s","v = kx/m = 0.2×400/0.1 = 800 m/s","v = 0.2 m/s","v = √(kx) = √80 ≈ 8.9 m/s"], answer:0},
     {q:"A charge q₁ = +2μC is 0.3 m from q₂ = −3μC. The electrostatic force magnitude:", options:["F = kq₁q₂/r² = 9×10⁹ × 2×10⁻⁶ × 3×10⁻⁶ / 0.09 = 0.6 N (attractive)","F = 0.06 N","F = 6 N","F = 0.006 N"], answer:0},
     {q:"A proton (m=1.67×10⁻²⁷ kg, q=1.6×10⁻¹⁹ C) enters a 0.5 T field at 10⁶ m/s perpendicular. Radius of circular path:", options:["r = mv/(qB) = 1.67×10⁻²⁷×10⁶/(1.6×10⁻¹⁹×0.5) ≈ 0.0209 m ≈ 2.1 cm","r = 1 m","r = 0.1 m","r = mv/q = 10.4 m"], answer:0},
     {q:"Muons created in upper atmosphere have T½ = 2.2 μs. Moving at 0.98c, the lab-frame half-life is ___.", options:["γ × 2.2 μs where γ = 1/√(1−0.96) ≈ 5; lab T½ ≈ 11 μs","2.2 μs unchanged","4.4 μs","1.1 μs"], answer:0}
   ]},
]},
{day:27, label:"Day 27 — Tue", subjects:[
  {subject:"English", title:"Writing Workshop: Style, Voice, and the Sentence", summary:"Students examine prose style at the level of the sentence — rhythm, syntax, diction — and revise their own writing for greater clarity, precision, and voice.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/watch?v=kLJE8IYIQEM",
   quiz:[
     {q:"Prose style at the sentence level includes ___.", options:["only grammar and spelling","only vocabulary choice","only sentence length","rhythm (patterns of stress, sentence length variation), syntax (clause structure, subordination), and diction (word choice, register, tone) — all working together to create a distinctive voice"], answer:3},
     {q:"Varying sentence length in academic prose ___.", options:["has no effect on the reader","should be avoided in formal writing","shows inconsistent style","creates rhythm and emphasis — a short sentence after several long ones lands with particular force; uniform sentence length produces monotony regardless of the quality of the ideas"], answer:3},
     {q:"Nominalisations (turning verbs/adjectives into nouns) in academic writing ___.", options:["always improve clarity","should be avoided always","are mandatory in formal academic style","can obscure agency and make prose unnecessarily dense — "the improvement of student performance" is weaker than "students improved"; nominalisation is sometimes appropriate but often inflates and obscures"], answer:3},
     {q:"The difference between a precise word and an approximate one is ___.", options:["only a matter of style","unimportant if the meaning is roughly correct","only important in poetry","enormous in academic writing — "the passage suggests ambivalence" is analytically precise; "the passage shows something complicated" is not; precision in diction is precision in thinking"], answer:3},
     {q:"Revision at the sentence level should happen ___.", options:["before revising the argument structure","only for the introduction","never — first drafts are always good enough","after the larger revision (argument, structure, evidence) is complete — it is inefficient to perfect sentences in a paragraph that may be restructured or deleted"], answer:3}
   ]},
  {subject:"Advanced Functions", title:"Advanced Functions: Final Exam Preparation", summary:"Rigorous examination-level practice with full worked solutions for all Advanced Functions topics.",
   resourceLabel:"Khan Academy", resourceUrl:"https://www.youtube.com/watch?v=LkwT1GQVJP8",
   quiz:[
     {q:"Determine all values of k for which x³ + 5x² + kx + 2 has (x+2) as a factor.", options:["P(−2) = 0: −8+20−2k+2=0 → 14−2k=0 → k=7","k = 3","k = −7","k = 5"], answer:0},
     {q:"Find the scalar equation of the plane through P(1,2,3), Q(2,−1,0), R(4,1,2).", options:["PQ=(1,−3,−3), PR=(3,−1,−1); n = PQ×PR = (3×(−1)−(−3)×(−1), (−3)×3−1×(−1), 1×(−1)−(−3)×3) = (−3−3, −9+1, −1+9) = (−6,−8,8); simplify: (3,4,−4); eq: 3(x−1)+4(y−2)−4(z−3) = 0 → 3x+4y−4z = −1","x+y+z = 6","3x+4y+4z = 6","3x−4y+4z = 0"], answer:0},
     {q:"A geometric series has t₃ = 12 and t₆ = 96. Find t₁ and r.", options:["t₃=t₁r²=12; t₆=t₁r⁵=96; dividing: r³=8 → r=2; t₁=12/4=3","r=2, t₁=3","r=4, t₁=0.75","r=2, t₁=6"], answer:1},
     {q:"P(at least one 6 in 4 rolls of a fair die) = ___.", options:["4/6","1 − P(no sixes) = 1 − (5/6)⁴ = 1 − 625/1296 = 671/1296 ≈ 0.518","4 × 1/6 = 2/3","(1/6)⁴"], answer:1},
     {q:"The maximum value of f(x) = sin(2x) + cos(2x) is ___.", options:["2","1","√2 (write as R·sin(2x+φ) where R=√(1²+1²)=√2)","√3"], answer:2}
   ]},
  {subject:"Calculus", title:"Calculus: Final Exam Preparation", summary:"Rigorous examination-level problems for Calculus and Vectors.",
   resourceLabel:"Khan Academy Calculus", resourceUrl:"https://www.youtube.com/watch?v=6HkBGVPWIXA",
   quiz:[
     {q:"Find the area between y=e^x, y=x, x=0, x=1.", options:["∫₀¹(e^x − x)dx = [e^x − x²/2]₀¹ = (e−1/2) − (1−0) = e − 3/2 ≈ 1.218","e − 1","1/2","e"], answer:0},
     {q:"A particle has velocity v(t) = 3t² − 6t. Find the displacement from t=0 to t=3.", options:["∫₀³(3t²−6t)dt = [t³−3t²]₀³ = 27−27 = 0 (returns to start)","9","−9","3"], answer:0},
     {q:"Evaluate ∫ x·ln(x) dx.", options:["use parts: u=ln(x), dv=x dx → v=x²/2; x²ln(x)/2 − ∫x²/2 × 1/x dx = x²ln(x)/2 − x²/4 + C","x²ln(x)/2 + C","ln(x²)/2 + C","x ln(x) − x + C"], answer:0},
     {q:"The line tangent to the curve x²y + y³ = 10 at (1,2):", options:["implicit diff: 2xy + x²y' + 3y²y' = 0; y'(x²+3y²) = −2xy; y'(1,2) = −4/13; tangent: y−2 = −4/13(x−1)","y = −x + 3","y = −4/13 x + 30/13","y−2 = 4/13(x−1)"], answer:0},
     {q:"A box is formed by cutting squares of side x from corners of a 30×20 cm sheet. Maximise volume.", options:["V = x(30−2x)(20−2x); V'= 0 gives 12x²−200x+600=0 → 3x²−50x+150=0; x=(50±√(2500−1800))/6=(50±√700)/6; x≈(50−26.5)/6≈3.9 cm","x = 5 cm","x = 3 cm","x = 10 cm"], answer:0}
   ]},
  {subject:"Physics", title:"Physics: Final Exam Preparation", summary:"Comprehensive examination-level physics problems spanning all SPH4U topics.",
   resourceLabel:"Crash Course Physics", resourceUrl:"https://www.youtube.com/watch?v=kKKM8Y-u7ds",
   quiz:[
     {q:"A 0.5 kg ball on a 1 m string moves in a horizontal circle at 3 m/s. Tension in string (ignore gravity):", options:["T = mv²/r = 0.5×9/1 = 4.5 N","T = 0.5 × 3 = 1.5 N","T = 1.5/1 = 1.5 N","T = 5 N"], answer:0},
     {q:"Two parallel plates 0.01 m apart with potential difference 100 V. Electric field between plates:", options:["E = V/d = 100/0.01 = 10,000 V/m","E = 100 V/m","E = 10 V/m","E = 1000 V/m"], answer:0},
     {q:"An 8 kg mass oscillates on a spring (k = 200 N/m). Period:", options:["T = 2π√(m/k) = 2π√(8/200) = 2π√(0.04) = 2π × 0.2 ≈ 1.26 s","T = 2π√(200/8) ≈ 15.7 s","T = 0.2 s","T = 2π s"], answer:0},
     {q:"A generator coil (N=100 turns, area 0.05 m², B=0.8 T) rotates at 60 Hz. Peak EMF:", options:["EMF_max = NBAω = 100×0.8×0.05×(2π×60) ≈ 1508 V","EMF = NBAB = 4 V","EMF = 100×60 = 6000 V","EMF = 60 V"], answer:0},
     {q:"An electron (m=9.11×10⁻³¹ kg) is accelerated through 500 V. Final kinetic energy and speed:", options:["KE = qV = 1.6×10⁻¹⁹×500 = 8×10⁻¹⁷ J; v = √(2KE/m) = √(1.6×10⁻¹⁶/9.11×10⁻³¹) ≈ 1.33×10⁷ m/s","v = 500 m/s","v = c = 3×10⁸ m/s","v = 3×10⁵ m/s"], answer:0}
   ]},
]},
{day:28, label:"Day 28 — Wed", subjects:[
  {subject:"English", title:"Culminating Essay: Writing Under Examination Conditions", summary:"Students practise writing a full analytical essay under timed conditions, applying all skills developed throughout the year.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/watch?v=kLJE8IYIQEM",
   quiz:[
     {q:"The most important 5 minutes of a timed literary essay are ___.", options:["the last 5 minutes of writing","the middle of the essay","the conclusion","the first 5 minutes of planning — a clear, specific thesis and a logical outline before writing saves time and produces a more coherent essay than beginning immediately"], answer:3},
     {q:"In a timed essay, the most common weakness is ___.", options:["writing too slowly","knowing the text too well","writing in too formal a register","insufficient analytical development — students describe textual events or state themes without explaining how specific textual choices create meaning; analysis takes time and cannot be rushed"], answer:3},
     {q:"Choosing a quotation under time pressure: prefer ___.", options:["the longest quotation you can recall","any passage you remember","only quotations you've memorised exactly","a short, specific phrase that is analytically productive — better to have two precise words you can analyse fully than two sentences you can only describe"], answer:3},
     {q:"Ending a timed essay effectively: the conclusion should ___.", options:["repeat the introduction word for word","only name the texts again","introduce new evidence","synthesise the essay's argument in 3-5 sentences — showing how the evidence collectively demonstrates the thesis, and opening one genuinely new perspective or question without introducing new evidence"], answer:3},
     {q:"A student who has genuinely mastered Grade 12 English will find timed writing ___.", options:["impossible without notes","irrelevant to real university skill","only useful for English exams","challenging but empowering — demonstrating that analytical thinking and articulate expression under pressure are real intellectual capacities, not just performances"], answer:3}
   ]},
  {subject:"Advanced Functions", title:"Advanced Functions: Culminating Task", summary:"Students complete a culminating task integrating multiple strands of the MHF4U course.",
   resourceLabel:"Khan Academy", resourceUrl:"https://www.youtube.com/watch?v=jKrEFOTScwU",
   quiz:[
     {q:"Part 1: Identify all features of f(x) = (x²−4)/(x²−x−2) and sketch.", options:["Factor: (x−2)(x+2)/((x−2)(x+1)); hole at x=2; VA at x=−1; HA y=1 (equal degrees); x-int at x=−2; y-int at f(0)=4/−2=−2; hole at (2, 4/3)","VA at x=2 and x=1 only","HA at y = 0","x-int at x = ±2 with no hole"], answer:0},
     {q:"Part 2: Solve 2^(x+1) = 3^(x−1) algebraically.", options:["(x+1)ln2 = (x−1)ln3; x(ln2−ln3) = −ln3−ln2 = −ln6; x = ln6/(ln3−ln2) ≈ 3.82","x = ln(3/2)","x = 1","x = 2"], answer:0},
     {q:"Part 3: The position vectors of points A and B are a=(3,1,−2) and b=(1,−1,4). Find the midpoint M and |AB|.", options:["M = ((3+1)/2, (1−1)/2, (−2+4)/2) = (2,0,1); |AB| = √((−2)²+(−2)²+6²) = √44 = 2√11","M = (4,0,2); |AB| = 8","M = (2,0,1); |AB| = √40","M = (1,1,1); |AB| = √44"], answer:0},
     {q:"Part 4: A fair coin is tossed 8 times. Find P(at least 6 heads).", options:["P(X≥6) = P(6)+P(7)+P(8) = [C(8,6)+C(8,7)+C(8,8)]/2⁸ = (28+8+1)/256 = 37/256 ≈ 0.145","37/256","1/4","37/64"], answer:1},
     {q:"Part 5: Prove by induction that ∑(k=1 to n) k³ = [n(n+1)/2]².", options:["Base: n=1: 1 = (1×2/2)² = 1 ✓. Inductive step: assume ∑k³ = [k(k+1)/2]²; add (k+1)³: [k(k+1)/2]²+(k+1)³ = (k+1)²[k²/4+(k+1)] = (k+1)²(k²+4k+4)/4 = [(k+1)(k+2)/2]² ✓","Not provable by induction","Formula is incorrect","Requires calculus, not induction"], answer:0}
   ]},
  {subject:"Calculus", title:"Calculus: Culminating Task", summary:"Students complete a culminating task integrating limits, derivatives, and integrals.",
   resourceLabel:"Khan Academy Calculus", resourceUrl:"https://www.youtube.com/watch?v=9vgCMNHPScU",
   quiz:[
     {q:"Part 1: lim(x→0) (e^x − 1 − x)/x².", options:["L'Hôpital twice: (e^x−1)/(2x) → e^x/2 → 1/2","L'Hôpital once: e^x − 1","the limit is 0","the limit is 1"], answer:0},
     {q:"Part 2: Differentiate f(x) = arctan(√x) and find f'(1).", options:["f'(x) = 1/(1+x) × 1/(2√x) = 1/(2√x(1+x)); f'(1) = 1/(2×1×2) = 1/4","f'(1) = 1/2","f'(1) = 1/4 using chain rule on arctan(x^(1/2)): 1/(1+x) × 1/(2√x)","f'(x) = 1/(2√x)"], answer:2},
     {q:"Part 3: ∫₀^(π/2) sin²(x) dx.", options:["use identity sin²x = (1−cos2x)/2; ∫₀^(π/2)(1−cos2x)/2 dx = [x/2−sin(2x)/4]₀^(π/2) = π/4","π/2","π/4","1/2"], answer:2},
     {q:"Part 4: Find the point on y = x² closest to (0, 3).", options:["Minimise D² = x² + (x²−3)²; d(D²)/dx = 2x+2(x²−3)(2x) = 2x(1+4x²−12) = 2x(4x²−11) = 0; x=0 (local max of distance) or x²=11/4; point: (√(11)/2, 11/4)","(0,0)","(1,1)","(√3, 3)"], answer:0},
     {q:"Part 5: Solve dy/dx = xy with y(0) = 1.", options:["separate: dy/y = x dx; ln|y| = x²/2 + C; y(0)=1 → C=0; y = e^(x²/2)","y = e^x","y = x²/2 + 1","y = xe^x + 1"], answer:0}
   ]},
  {subject:"Physics", title:"Physics: Culminating Task", summary:"Students complete a multi-concept physics culminating task.",
   resourceLabel:"Crash Course Physics", resourceUrl:"https://www.youtube.com/watch?v=aY8z2qO44WA",
   quiz:[
     {q:"A projectile is launched at 50 m/s at 37° above horizontal. Find max height and range.", options:["v₀y=50sin37°=30 m/s; v₀x=50cos37°=40 m/s; max H=v₀y²/(2g)=900/19.6≈45.9 m; T=2×30/9.8≈6.1 s; R=40×6.1≈245 m","H=50 m; R=200 m","H=30 m; R=300 m","H=40 m; R=250 m"], answer:0},
     {q:"A 2 kg block slides down a 30° ramp (μₖ=0.2) of length 5 m from rest. Speed at bottom:", options:["a = g(sin30°−μₖcos30°) = 9.8(0.5−0.2×0.866) = 9.8×0.327 = 3.2 m/s²; v²=2×3.2×5=32; v≈5.66 m/s","v = √(2gh) = √(2×9.8×2.5) ≈ 7 m/s","v = 5 m/s","v = 10 m/s"], answer:0},
     {q:"A transformer: 120 V primary, 2400 V secondary, 0.5 A secondary current. Primary current:", options:["V_p I_p = V_s I_s; I_p = 2400×0.5/120 = 10 A","I_p = 0.5 A","I_p = 2.5 A","I_p = 0.025 A"], answer:0},
     {q:"Radioactive source: activity at t=0 is 8000 Bq; after 12 hours = 1000 Bq. Find T½.", options:["8000×(1/2)^(12/T½) = 1000; (1/2)^(12/T½)=1/8=(1/2)³; 12/T½=3; T½=4 hours","T½ = 3 hours","T½ = 6 hours","T½ = 2 hours"], answer:0},
     {q:"Calculate the de Broglie wavelength of an electron (m=9.11×10⁻³¹ kg) moving at 10⁶ m/s.", options:["λ = h/(mv) = 6.63×10⁻³⁴/(9.11×10⁻³¹×10⁶) ≈ 7.28×10⁻¹⁰ m = 0.728 nm","λ = 10⁻³⁴ m","λ = 10⁻⁶ m","λ = 1 nm"], answer:0}
   ]},
]},
{day:29, label:"Day 29 — Thu", subjects:[
  {subject:"English", title:"Grade 12 English: Oral Culminating and Reflection", summary:"Students deliver oral culminating presentations and reflect on their growth as readers, writers, and thinkers across Grade 12.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/watch?v=MSYw502dJNY",
   quiz:[
     {q:"An oral culminating in Grade 12 English demonstrates ___.", options:["only public speaking skill","only the ability to memorise","only knowledge of plot","the integration of all your analytical learning: the ability to think aloud, respond to texts in real time, construct an argument under pressure, and communicate sophisticated ideas to an audience"], answer:3},
     {q:"Reflecting on your development as a reader across Grade 12 means ___.", options:["only counting books read","only identifying your favourite text","only recognising what you found difficult","articulating what has changed in how you read — what you now notice, ask, and value that you did not before — making your intellectual growth conscious and available for further development"], answer:3},
     {q:"The skills developed in Grade 12 English that transfer most directly to university are ___.", options:["only essay formatting","only reading speed","only knowledge of canonical literature","critical reading, analytical argument, evidence-based reasoning, and clear written communication — the core intellectual skills of university education in any discipline"], answer:3},
     {q:"The most significant intellectual growth in Grade 12 English occurs when ___.", options:["you finish all the assessments","you get the highest mark","you have memorised the most quotations","you move from seeking the "right answer" to generating your own well-supported, genuinely original interpretive arguments — from passive consumer to active maker of meaning"], answer:3},
     {q:"Grade 12 English is fundamentally about ___.", options:["learning to write five-paragraph essays","memorising literary terms","preparing for English at university","developing your capacity to think carefully, feel deeply, and communicate precisely — using literature as the site and language as the tool of that development"], answer:3}
   ]},
  {subject:"Advanced Functions", title:"Advanced Functions: Final Reflection and Looking Forward", summary:"Students reflect on the year's learning in Advanced Functions and its significance for future study.",
   resourceLabel:"Khan Academy", resourceUrl:"https://www.youtube.com/watch?v=nRmBsxBpTjs",
   quiz:[
     {q:"The central organising concept of Advanced Functions is ___.", options:["the derivative of a function","only polynomial equations","only trigonometric functions","the function — as a general mathematical object with domain, range, graph, and multiple representations; all topics in the course are about different families of functions and their properties"], answer:3},
     {q:"A student who has mastered Advanced Functions can ___.", options:["only solve textbook problems","only work in Ontario high schools","never need mathematics again","see a mathematical relationship and ask: What type of function models this? What are its key features? How does it transform? This is mathematical fluency that transfers to any quantitative field"], answer:3},
     {q:"The connection between Advanced Functions and Calculus is ___.", options:["calculus is harder but unrelated","calculus uses completely different functions","Advanced Functions is only for non-calculus students","direct: calculus studies how functions change (differentiation) and accumulate (integration); you need deep knowledge of all function families to do calculus effectively"], answer:3},
     {q:"The proof and reasoning strand in Advanced Functions ___.", options:["is only for future mathematics students","is unrelated to the function content","is only about mathematical induction","introduces the formal mathematical reasoning that is the foundation of university mathematics — learning to construct and verify proofs, not just apply algorithms"], answer:3},
     {q:"Looking back on Grade 12 mathematics, the most valuable habit of mind developed is ___.", options:["memorisation of formulas","speed at calculation","test-taking strategy","mathematical curiosity — the willingness to ask "why does this work?" and "what would happen if...?" and to pursue those questions rigorously to a satisfying answer"], answer:3}
   ]},
  {subject:"Calculus", title:"Calculus: Final Reflection and University Preparation", summary:"Students reflect on Calculus learning and prepare for university calculus courses.",
   resourceLabel:"Khan Academy Calculus", resourceUrl:"https://www.youtube.com/watch?v=riXcZT2ICjA",
   quiz:[
     {q:"The two most important ideas in Calculus are ___.", options:["the product rule and chain rule","limits and power rule","derivatives and integrals as separate topics","the derivative (instantaneous rate of change as a limit) and the integral (accumulated change); and that they are inverse operations — the Fundamental Theorem connecting them"], answer:3},
     {q:"University calculus (Calculus I, II) will build on your Grade 12 learning by ___.", options:["starting completely from scratch","being much easier","not requiring any Grade 12 preparation","introducing multivariable calculus, series, improper integrals, and applications in physics, engineering, and economics — Grade 12 calculus is the essential foundation"], answer:3},
     {q:"The most important skill for university calculus is ___.", options:["algebraic fluency — limits and derivatives require confident algebra; students who struggle with algebra in Grade 12 will find university calculus very difficult","memorising all derivative rules","only understanding limits","only understanding integration"], answer:0},
     {q:"Calculus is the mathematics of ___.", options:["only curves and slopes","only physics","only areas and volumes","change — and thus of the continuous aspects of the real world: motion, growth, decay, oscillation, flow, and optimisation; it is the most widely applied branch of mathematics"], answer:3},
     {q:"The experience of Grade 12 Calculus ___.", options:["is sufficient for all future mathematics needs","shows mathematics is only about computation","shows that advanced mathematics is inaccessible to most people","demonstrates that with persistence and conceptual understanding, genuinely deep mathematical ideas are accessible — and that the intellectual reward of understanding such ideas is considerable"], answer:3}
   ]},
  {subject:"Physics", title:"Physics: Final Reflection and Looking to University", summary:"Students reflect on their Grade 12 Physics learning and its connections to university physics and modern life.",
   resourceLabel:"Crash Course Physics", resourceUrl:"https://www.youtube.com/watch?v=aY8z2qO44WA",
   quiz:[
     {q:"The most important conceptual development in Grade 12 Physics is ___.", options:["learning to use complex formulas","understanding the SI unit system","knowing all fundamental constants","moving from the intuitive Newtonian world to the deeply counter-intuitive worlds of quantum mechanics and relativity — where human intuition, while useful at everyday scales, fundamentally misleads"], answer:3},
     {q:"University physics (mechanics, E&M, waves/optics, modern physics) builds on Grade 12 by ___.", options:["being completely different in content","being much easier","repeating the same material","deepening and mathematising every concept — using multivariable calculus, differential equations, and linear algebra as the primary tools; Grade 12 physics is the conceptual foundation"], answer:3},
     {q:"Physics problem-solving skill transfers to ___.", options:["only physics problems","only engineering problems","only science","any domain requiring structured analytical reasoning: identifying what is given and unknown, selecting appropriate principles, working systematically, checking answers dimensionally and intuitively"], answer:3},
     {q:"The most significant open problems in physics today are ___.", options:["already solved in principle","only mathematical","only relevant to theorists","quantum gravity, dark matter, dark energy, matter-antimatter asymmetry, and a unified theory of all forces — each of which may require conceptual revolutions as profound as Einstein's or Planck's"], answer:3},
     {q:"Grade 12 Physics has shown you that ___.", options:["physics is a closed discipline with all answers known","physics is only for those who plan to study it at university","equations are more important than concepts","the universe operates according to mathematical laws of astonishing elegance and power — and that patient, systematic, mathematically guided inquiry is the most reliable path to understanding it"], answer:3}
   ]},
]},
{day:30, label:"Day 30 — Fri", subjects:[
  {subject:"English", title:"Grade 12 Celebration: A Year of Growth", summary:"A final day celebrating the intellectual journey of Grade 12 — reflecting on growth, looking ahead to university and life, and recognising what has been accomplished.",
   resourceLabel:"TED-Ed: Literature", resourceUrl:"https://www.youtube.com/watch?v=jTDkTt1UTXM",
   quiz:[
     {q:"The most important thing accomplished in Grade 12 is ___.", options:["a high grade average","only university preparation","only skill development","genuine intellectual growth — deeper, more independent thinking; the ability to sustain a complex argument; wider reading and a more developed aesthetic and critical sensibility"], answer:3},
     {q:"University marks a transition from ___.", options:["one set of rules to another set of rules","high school content to harder content","being assessed to never being assessed again","guided learning to independent intellectual life — you choose your own questions, pursue your own research, and take responsibility for your own intellectual development to a degree impossible in high school"], answer:3},
     {q:"The reading and writing skills developed in Grade 12 ___.", options:["are only for English programs","will be forgotten quickly after exams","have no relevance outside school","are fundamental to success in any field requiring communication, analysis, or sustained thinking — virtually every university program and professional career"], answer:3},
     {q:"Looking back on all of Grade 12, the subject that will most surprise you at university is ___.", options:["the one that gave you the worst grade","the one that was easiest in high school","the one you studied least","the one that opens up into a vast new world — where high school content was the surface of an ocean; at university you begin to dive"], answer:3},
     {q:"The best preparation for university and adult life that Grade 12 has provided is ___.", options:["knowing all the curriculum content","achieving the highest possible marks","only having specific skills","the experience of sustained intellectual effort — wrestling with difficulty, revising your thinking, producing work you genuinely stand behind, and discovering what you are actually capable of"], answer:3}
   ]},
  {subject:"Advanced Functions and Calculus", title:"Grade 12 Mathematics: Final Day Celebration", summary:"Students celebrate completing two of Ontario's most rigorous mathematics courses and look ahead with confidence.",
   resourceLabel:"Khan Academy: Encouragement for Math Students", resourceUrl:"https://www.youtube.com/watch?v=riXcZT2ICjA",
   quiz:[
     {q:"Completing both Advanced Functions and Calculus in Grade 12 demonstrates ___.", options:["only that you like mathematics","only good test-taking strategy","nothing about future capabilities","genuine mathematical maturity — you have engaged with the deepest mathematical ideas taught in Ontario secondary school, and you have the foundation for any quantitatively demanding university program"], answer:3},
     {q:"The discipline of solving a difficult mathematics problem translates to ___.", options:["only future mathematics problems","only to science and engineering","nothing outside mathematics","any domain requiring persistence, systematic analysis, and comfort with complexity — the problem-solving mindset is not subject-specific"], answer:3},
     {q:"The most important mathematical truth you have encountered in Grade 12 is ___.", options:["the formula for the area of a circle","the quadratic formula","only the power rule","that calculus connects the two most fundamental mathematical operations — differentiation and integration — in a single elegant theorem; and that this connection, discovered 350 years ago, underlies virtually all of modern science and technology"], answer:3},
     {q:"A student who has done well in Grade 12 mathematics should feel ___.", options:["that they have exhausted mathematics","that mathematics is now fully mastered","that mathematics is only useful for specialists","that they have developed genuine mathematical power — the ability to reason precisely, handle abstraction, and apply formal thinking to real problems — a portable, durable, and extremely valuable intellectual asset"], answer:3},
     {q:"Looking ahead, Grade 12 mathematics graduates who pursue further study will discover ___.", options:["that first-year university mathematics is the same as Grade 12","that mathematics becomes less interesting at university","that all mathematics has now been discovered","that mathematics is a vast, living field of inquiry — Grade 12 covered two centuries of mathematical development; several more centuries (and open research problems) await"], answer:3}
   ]},
  {subject:"Physics", title:"Grade 12 Physics: Final Day", summary:"Students celebrate completing Grade 12 Physics and look ahead to university and the world of physics.",
   resourceLabel:"Crash Course Physics: Celebration", resourceUrl:"https://www.youtube.com/watch?v=pGj9isFr21U",
   quiz:[
     {q:"Grade 12 Physics has given you ___.", options:["only a set of formulas to memorise","only laboratory skills","only a foundation for university physics","a way of seeing the world — every natural phenomenon from the motion of planets to the behaviour of electrons is in principle understandable through the application of a small number of elegant physical laws"], answer:3},
     {q:"The greatest physicists (Newton, Faraday, Maxwell, Einstein, Bohr, Feynman) were unified by ___.", options:["only mathematical genius","only experimental skill","only theoretical creativity","deep curiosity about how the world works — combined with the discipline to pursue that curiosity systematically, the mathematical tools to express what they found, and the imagination to conceive what had never been conceived before"], answer:3},
     {q:"Climate change, renewable energy, quantum computing, and medical imaging are all ___.", options:["unrelated to physics","only political issues","only engineering problems","direct applications of physical principles — Grade 12 Physics is not abstract knowledge but the foundation of the most pressing technological challenges facing humanity"], answer:3},
     {q:"The challenges that await the next generation of physicists and engineers include ___.", options:["only incremental improvements to existing technology","problems that have already been solved","only problems in pure mathematics","fusion energy, quantum computers, materials science for sustainability, space exploration, and the ultimate questions of quantum gravity and the nature of dark matter — genuinely open, important, and difficult"], answer:3},
     {q:"The final lesson of Grade 12 Physics is ___.", options:["physics is too difficult for most people","only specialists need to understand physics","physics content is fully memorised and complete","curiosity is the essential scientific virtue — the questions "why?" and "what if?" and "how do we know?" asked persistently, rigorously, and with mathematical precision, are what the entire edifice of physics is built on"], answer:3}
   ]},
]},
];

export default curriculum;