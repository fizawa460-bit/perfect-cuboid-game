# M3-T11-128 — Exact real evaluation image versus the universal norm witness

STATUS=PROVED_EXACT_REAL_SIGNATURE / WITHIN_SESSION_ADVERSARIAL_AUDIT_PASS / GLOBAL_COUNTING_CREDIT0
TYPE=GENUINE_NON_NORM_LOCAL_COMPATIBILITY / NORMALIZATION_AND_SCALAR_QUOTIENT_FIREWALL
POPULATION=Audited123 irreducible-S4 rational-u complement of retained nondegenerate fixed-packet physical endpoints, one endpoint one count.
HEIGHT=Exact physical R<=B retained; no auxiliary-box replacement. Algebraic assertions hold for every reduced u=a/b, a!=0,b>0, regardless of Galois group.
DEPENDS_ON=105 necessary negative-square quartic;106 actual z=S/2;109 S4 complement;123 integral packet and universal gamma. No extra charge of105–107 local selectors.
ALIASES=S4OrderedRealEvaluationSignature; S4UniversalGammaRealExclusion; S4RealSignatureKernelAdapter.
DUPLICATE_OF=NONE. Targeted canonical ledger/route search found123 retains archimedean signs but does not compute their evaluation image or gamma obstruction.
SUPERSEDES=No theorem. Refines123's explicit warning that its coarse norm fiber is not a locally compatible descent set.

## 1. Exact coordinates and the curve being tested
Use123's N=a²+b², D0=2b²-25a²,
F(X)=N X⁴-8abX³+(11a²-b²)X²+6abX-a²,
theta_root=theta, alpha=Ntheta,
G(X)=N³F(X/N), beta=Nm-nalpha, gamma=alpha(aN-balpha), xi=beta/gamma.
The ACTUAL physical z=S/2=m/n is reduced with n>0. Restore
[z-theta]=[Nn beta]=[Nn gamma xi].
Nn is positive at infinity. Thus beta and the original evaluation have identical real signs; beta cannot be confused with the original class at finite places.

The necessary residual curve is C_u: w²=-F(z)/N, with w!=0. This squarefree quartic defines a genus1 curve after smooth completion, not the full genus2 physical cover. Physical points project to it by105. We compute only its non-root affine real evaluation image and the induced necessary physical condition; we neither identify its fake Selmer set with the full physical cover nor prove a lifting converse.

## 2. Exact root ordering, without numerical precision assumptions
disc(F)=16a²N²D0³, F(0)=-a²<0, F(a/b)=a²(a²+2b²)²/b⁴>0. D0 cannot vanish for nonzero rational u.
F has at least two real roots since its leading coefficient is positive and F(0)<0. A separable real quartic with positive discriminant has zero or four real roots, and one with negative discriminant has two. Consequently:
D0>0: four real embeddings; D0<0: two real embeddings and one complex pair.

For a>0, Descartes applied to F(-X) gives exactly one negative root: its coefficient signs are +,+,(either sign),-,-, with one variation. In the four-real case the other three roots are positive. Write r1<r2<r3<r4. Since F(0)<0 and F(u)>0, either r2<u<r3 or r4<u. The second possibility contradicts Vieta:
sum r_i=8u/(1+u²)>3u, whereas r1<0 and the other three roots<u would give sum r_i<3u. Here D0>0 implies u²<2/25, so the strict inequality holds. Hence
a>0,D0>0: r1<0<r2<u<r3<r4.
a>0,D0<0: r1<0<r2<u.
For a<0 use F_{-a,b}(X)=F_{a,b}(-X) and reflect the ordered roots:
a<0,D0>0: r1<r2<u<r3<0<r4.
a<0,D0<0: u<r1<0<r2.
The roots of G are N*r_i, so their order agrees. Neither 0 nor u is a root.

## 3. The real evaluation image and gamma's mismatch
In increasing root order, beta_i=Nn(z-r_i). For real non-root points on C_u, F(z)<0. Thus its exact sign image is
four real roots: E_inf={+---, +++-}, from z in(r1,r2) or(r3,r4);
two real roots: E_inf={+-}, from z in(r1,r2).
Every displayed vector is realized on the residual REAL curve; omitted physical packet/pole constraints can make the actual physical image smaller. These are not rational-point existence assertions.

gamma_i=N²*r_i*(a-b*r_i). It is positive precisely for roots strictly between0 andu. Therefore:

| Regime | sign(gamma) | necessary sign(xi) |
| --- | --- | --- |
| D0>0,a>0 | -+-- | {--++, -+-+} |
| D0>0,a<0 | --+- | {--++, -+-+} |
| D0<0,a>0 | -+ | {--} |
| D0<0,a<0 | +- | {++} |

In the four-real regime, BOTH gamma and -gamma miss E_inf. Thus123's universal supported norm[-1] class fails even the residual real evaluation condition, including after quotienting by rational scalars. In particular xi cannot be the identity squareclass for a physical point there. This is a genuine distinction beyond the norm condition: gamma is still a valid member of the coarse norm fiber, with Norm(gamma)=-(a²N³(a²+2b²))².

In the two-real regime, gamma fails the normalized image for a>0 but -gamma passes its REAL sign test. For a<0 gamma itself passes. Hence gamma is NOT excluded in the rational-scalar quotient in this regime. Never extend the four-real exclusion to all u or confuse failure of a representative with failure of its projective descent class. Passing this real test establishes no finite local/global compatibility.

## 4. Exact finite-packet signature adapter, retaining class groups
Let V_u be123's supported norm kernel and sigma_inf:V_u -> E_r the sign homomorphism, where E_r consists of vectors with product+1 in the r real embeddings. Complex norms are positive. Put W_u=ker(sigma_inf), and let T_u be the xi set in the table. Define ONLY the necessary real-compatible normalized packet
H_u^{-,inf}={gamma*xi:xi in V_u, sigma_inf(xi) in T_u}.
Then exactly
|H_u^{-,inf}|=|T_u intersect sigma_inf(V_u)|*|W_u|.
In particular it is at most2|W_u| for four real roots and at most|W_u| for two real roots. The set can be empty; no signature surjectivity or nonemptiness is assumed. The universal gamma construction does NOT prove this smaller packet is nonempty in the four-real regime.

For four real embeddings the ambient norm[-1] real sign set has8 vectors and E_inf has2; after quotienting by simultaneous sign reversal there are4 ambient classes and2 evaluation classes. These ambient ratios are NOT probabilities on the global packet or physical measure. sigma_inf(V_u) may be a proper subgroup; its intersection with T_u must be calculated, not replaced by a1/4 factor.
Retain123's bound
|V_u|<=2^(4+4omega(|2aND0|))*|Cl(K_u)[2]|.
No class group, actual signature image, full Selmer set or moving-u distribution is computed here. This adapter filters labels per u; it does not bound the number of occupied u. It yields NO independent counting credit or fixed power saving.

## 5. Verification and method source
Independent standard-library replay uses exact rational Sturm sequences to count all real roots and roots below0 andu for718 primitive signed packets with1<=|a|,b<=24:100 four-real,618 two-real. Complete finite sign enumeration checks gamma, E_inf, T_u, scalar-quotient inclusion/exclusion and ambient cardinalities. No floating-root arithmetic, Galois-group/class-group computation or physical endpoint enumeration is used. These separable algebraic samples support the proof; they are not claimed allS4 or physical.
Wolfram exact expansion independently returns disc(F), F(u), F'(u)=2a(2a⁴+a²b²+2b⁴)/b³ and reflection residual0. All multiplications are explicit in the retained replay; an initial unretained input token abx was corrected before using the symbolic output.
Primary method context: Bruin–Stoll, Two-cover descent on hyperelliptic curves, arXiv:0803.2052v2, Section5 (ordered real evaluation signs and scalar quotient) and Section6 (local-compatible intersection distinct from supported packets). Our increasing ordering, negative-leading residual curve and positive normalization are derived here.
https://arxiv.org/html/0803.2052v2

## 6. Continuation and firewalls
NEXT_RESEARCH_CARD_ID=M3-T11-129
CURRENT_ATTACK=S4GlobalSignatureImageAndBadPrimeCompatibility
NEXT_LEGAL_ACTION=On retained irreducible-S4 u, determine whether sigma_inf(V_u) intersects the explicit T_u and combine with genuine bad-prime evaluation conditions on original[Nn gamma xi]. Seek an exact algebraic certificate or same-R<=B moving-u obstruction, not ambient sign ratios. A full Selmer computation requires its precise curve/cover and scalar quotient. Retain Cl(K_u)[2], actual n, pole/root exclusions,105–107 no-double-charge and fixed-u036 multiplicity. Do not claim moving-u contraction from merely excluding gamma. TI remains parked; theta127 full original-r realization stays open but inactive.
DO_NOT_REPEAT=No universal norm witness=>locally compatible class; no sign parity=>ordered evaluation; no two-real normalized representative failure=>projective exclusion; no constant sign fraction=>power saving; no real point=>rational/physical point; no uncomputed signature surjectivity or class-group deletion.
REOPEN_CONDITION=New exact global signature/bad-prime image calculation or a same-physical-measure cross-u realization theorem.
AUDIT_MODE=Within-session adversarial rederivation, not external audit.
GLOBAL_COUNTING_CREDIT=0
GLOBAL_FIXED_POWER_SAVING=false
PRIMARY_GATE_CLOSED=false
M3_T11_PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false
