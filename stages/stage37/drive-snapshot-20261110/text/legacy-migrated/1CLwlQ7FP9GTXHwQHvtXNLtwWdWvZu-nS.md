# M3-T11-127 — Global E_theta point impostors with fresh quarter components
DATE=2026-09-30
STATUS=PROVED_COARSE_GLOBAL_POINT_EXISTENCE_OBSTRUCTION / WITHIN_SESSION_ADVERSARIAL_AUDIT_PASS / GLOBAL_COUNTING_CREDIT0
PRIMARY_GATE=M3-T11-GATE-001 OPEN
AUDIT_MODE=Within-session adversarial rederivation, not external or independent-agent audit.
CURRENT_AUTHORITY=Drive MAIN/INDEX/RESULT-LEDGER/active ROUTE126.
DEPENDENCIES=093/094 theta/cofactor;095 physical Z/old-w relation;096 translated curve;124 gcd;125 denominator consequence;126 reduction/component packet.
POPULATION_BOUNDARY=The constructed family below is a RELAXED arithmetic family, NOT asserted Stage37 physical endpoints, not all fixed-packet compatibility, and not an exact-R<=B family. The task's physical measure is never replaced by it. It proves only that a specified standalone coarse global-existence receiver has abundant impostors.

## 1. Scope of the negative result
127 tests adding a GLOBAL rational point realizing126's component vector, instead of only independent local cosets. There are polynomial-height relaxed families with such a single global point, actual theta cofactor formula, v=u²,125's square denominator consequence, and original rational-r square compatibility at2,3,infinity and every fresh prime.
There is no proved contraction of the FULL physical realized (M,q,C) support. Global r, other places, actual coefficient/content packet and exact physical height remain essential. Non-torsion, positive Mordell-Weil rank, full Selmer nonemptiness or cuboid existence is NOT asserted.

## 2. Gaussian and CRT construction
Let M>=17 have every prime divisor p=17mod24. Choose one Gaussian prime orientation above each p and let alpha_G be their product with the exponents of M, so Norm(alpha_G)=M. It is primitive: no rational prime divides it because at each split p only one conjugate orientation occurs. Write
alpha_G²=a+i b
after choosing signs and a Gaussian unit so a,b>0. Then
a²+b²=M², gcd(a,b)=1, a odd, 8|b, gcd(ab,M)=1, 1<=a,b<M.
For the parity: each p=1mod8 has a representation r²+t² with r odd and4|t; their oriented products retain odd real coordinate and imaginary coordinate divisible by4, so its square has imaginary part divisible by8. No axis coordinate can vanish in a primitive nontrivial oriented product. Moreover a²=M²-b²>=2M-1, hence a>=6.

Choose t0 satisfying
t0=1 modb,
t0=(8a)^(-1) modM,
1<=t0<=28M².
If 3|b no further3-adic choice is needed.
If 3|a (the only other possibility since a²+b²=M² and3 does not divide M), also choose t0 so F(t0)=9mod27, with F defined in Section5.
This exists: modulo3, F(T)=T²-1, with a simple root atT=1. Hensel lifting F(T)-9 gives a root mod27. Since3 does not divide bM, the27 possible choices t0=1+b(k0+jM),0<=j<27, traverse all residues mod27 while preserving the first two congruences. Here k0 is the least nonnegative solution of1+bk0=(8a)^(-1) modM. This also proves the height bound and gcd(t0,bM)=1.

Set
u=a/b, s=b, t=M²t0, S=s/t, N0=1.
Both u and S are reduced. At every p^lambda||M,
v_p(a²+b²)=v_p(t)=2lambda, a,b,s,t0 units.
These are the full-S normalization equations, NOT a claim that a physical conductor/packet has been realized.

## 3. Actual cofactor and square denominator
Define
Psi=b²-12ab²t0+4a²M²t0²,
q=Psi/4=a²M²t0²-3ab²t0+b²/4.
Because8|b and a,M,t0 are odd, q is odd.
Modulo a, q=b²/4 is a unit; modulo b, q=a²M²t0² is a unit. Thus
g=gcd(Psi,(2ab²)²)=4.
Consequently the actual124 reduced fraction is
theta=A/C, A=M^4*q, C=(ab²)²,
gcd(A,C)=1.
From the fresh CRT equation8a*t0=1modM,
Psi=-b²/2modM, q=-b²/8modM, so gcd(q,M)=1.
Hence every fresh valuation of theta is exactly4lambda, not merely a fourth-power lower bound.125's denominator consequence holds with epsilon=0,d=1.

q>0: the negative term divided by a²M²t0² is at most3/a<=1/2, and b²/4 is nonnegative.
Useful polynomial bounds:
q<=785M^8, A<=785M^12, C<=M^6, t<=28M^4.
These are auxiliary arithmetic heights, NOT physical R.

## 4. A SINGLE global rational point realizes all components
Put v=u²,w=u/S=aM²t0/b² and
P=(X,Z), X=-(v+1), Z=(v+1)(3-2w).
The exact094 identity gives theta=(v+1)((v+1)-12w+4w²)/(4v).
Direct substitution therefore proves
Z²=X(X²+(9+4theta)X+4theta).
Thus P belongs to E_theta(Q), without a rational-r assumption.

At all fresh p, w has valuation2lambda;126 applies with e=v_p(q)=0. The curve has split I_(8lambda), and the SINGLE global P has
kappa_p(P)=+/-2lambda mod8lambda,
component order4 simultaneously at all p|M.
This is a true diagonal global image, not independently selected p-adic points. Still it is not a physical point or a global4-torsion assertion.

Also x_Legendre=N0*s/(16ab*t0)=1/(16a*t0)=1/2modM.
With ell=(theta-3(v+1))/16,
r²_required=ell+x_Legendre(1-x_Legendre)=1/4modp
at every fresh p. It is a unit square in Q_p by Hensel lifting. These local roots do not supply a common rational r.

## 5. The exact MISSING global square condition
For this family define the integral quartic
F(T)=a²M^6*T^4-3ab²M^4*T³-((11a²-b²)M²b²/4)*T²+ab^4*T-b^4/16.
The divisions by4 and16 are integral since8|b.
Substituting the retained endpoint Phi with s=b,t=M²t0 gives
-Phi/M²=16F(t0),
and exactly
r²_required=F(t0)/(4ab²t0)².
Therefore original rational r exists for this family IFF the positive integer F(t0) is an integer square. This is not implied by its global E_theta point.

The stated partial local compatibility is rigorous:
- 2: F(t0)=1mod8, since its leading term is an odd square and all remaining terms are divisible by8.
- 3: if3|b then F(t0)=1mod3; if3|a the CRT choice gives F(t0)=9mod27, valuation2 with square unit.
- fresh p: Section4 gives r²_required=1/4modp.
- real: F(t0)>0. Relative to a²M^6*t0^4, the negative cubic term is at most1/2, the negative quadratic term at most11/(4M²), and the constant at most1/(16a²M²); their sum is less than1 forM>=17. The positive linear term may be ignored.
No claim is made about r at other finite primes, or about its global square. Even a global r here would not by itself establish all physical splitting/packet/height conditions.

## 6. Polynomial-height abundant CURVES, not physical endpoints
Take M=p prime=17mod24 in [L,2L]. Fixed-modulus PNT AP gives (1+o(1))*L/(8logL) primes.
Each resulting reduced A is at most785*(2L)^12 and divisible byp^4 exactly. If a single theta arose from4 distinct such primes, its same reduced numerator would be at leastL^16. ForL>=50 this contradicts the upper bound. Thus each theta has at most3 such prime witnesses, and there are at least(1/24+o(1))*L/logL distinct theta values.

The j-function is
j(theta)=16(16theta²+60theta+81)^3/[theta²(16theta²+56theta+81)].
For a fixed finite j, the equation has degree6 with nonzero leading coefficient. Each j has at most6 rational theta preimages. Hence at least(1/144+o(1))*L/logL distinct j-values, and at least that many distinct Q-isomorphism classes of smooth curves, carry the global point/component and stated coarse adapters.

This lower bound is ONLY for the constructed relaxed curve family in polynomial parameter-height boxes. It is NOT a bound under physical R<=B, not a physical numerator count, and not a full theta-route impossibility theorem. It blocks obtaining O(L^(1-delta)) from the listed relaxed conditions ALONE. Stronger actual height restrictions, remaining local conditions or the original global r equation can remove these impostors.

## 7. Verification and sources
Replay verify_m3_t11_127.py checks85 prime M<=5000 plus M=17²,17*41,41²,17*41*89. All89 are exact global E_theta points; all pass the cofactor/g=4/denominator, simultaneous saturated component arithmetic, and r compatibility at2,3,infinity,fresh primes. All89 fail the global F-square test. This finite failure is not asserted for every member of the infinite construction. None are claimed physical endpoints.
Wolfram expansion verifies the quartic and shows the identity residual is a multiple of a²+b²-M²; it vanishes on the constructed norm relation.
Primary source for the classical AP theorem: MIT18.785 Fall2021 problemset9 Problem5:
https://ocw.mit.edu/courses/18-785-number-theory-i-fall-2021/mit18_785f21_pset9.pdf
126's component theorem source remains J.E.Cremona:
https://johncremona.github.io/papers/component.pdf
The family, CRT refinement, cofactor, remaining quartic and collision/degree count are derived here.

## 8. Scope closure and next branch
RETIRE_ONLY=ThetaGlobalComponentImageAcrossMovingCurves as a STANDALONE global-E-point-existence/component receiver, including adding rational v=u², actual reduced cofactor, square denominator and the listed partial local-r conditions.
KEEP_OPEN=Full physical theta realization using original GLOBAL r, all packet/local constraints and exact R; no global theta support bound proved.
No MW rank, non-torsion, canonical-height theorem, abc/Szpiro or Selmer collapse is imported.

NEXT_RESEARCH_CARD_ID=M3-T11-128
CURRENT_ATTACK=S4GenuineLocalCompatibilityBeyondUniversalNormWitness
NEXT_LEGAL_ACTION=Return to audited123 retained irreducible-S4 frontier: beta=Nm-nalpha, gamma=alpha(aN-balpha), xi=beta/gamma, original [z-theta_root]=[Nn beta]. Separate genuine full descent local/realized evaluation constraints from the universally nonempty supported norm[-1] fiber. Seek a same-R<=B contraction of actually occupied xi/cross-u classes; retain Cl(K_u)[2], evaluation denominator and pole exclusions. Do not label the coarse norm fiber full Selmer. If local conditions merely restate105–107, record no-go; need actual moving-u global compatibility. Theta125/126 structure remains retained, theta full-global-r route open but not next activeattack. TI stays parked.
DO_NOT_REPEAT=No global-E point=>physical implication; no fresh local r=>rational r; no Gaussian primitive u=>cuboid; no relaxed height=>R<=B; no fixedtheta multiplicity multiplication; no component/Tamagawa/old-w doublecharge; no withdrawn120 revival.

GLOBAL_FIXED_POWER_SAVING=false
PRIMARY_GATE_CLOSED=false
M3_T11_PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false

