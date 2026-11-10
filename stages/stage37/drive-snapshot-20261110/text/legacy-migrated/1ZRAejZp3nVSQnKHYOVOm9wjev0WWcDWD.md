# M3-T11-123 — S4 integral descent packet and universal negative-square norm witness

STATUS=PROVED_EXACT_STRUCTURE / WITHIN_SESSION_HOSTILE_AUDIT_PASS / NO_NEW_COUNTING_CREDIT
TYPE=EXACT_NONLOCAL_SUPPORT_ADAPTER / UNIVERSAL_NORM_WITNESS / COUNTING_FIREWALL
POPULATION=Existing nondegenerate fixed-content/coefficient Stage37 physical endpoints on exact R<=B, restricted to the irreducible S4 rational-u complement classified by audited109. One physical endpoint is one count. Algebraic witness identities also hold in the degree-four etale algebra whenever the quartic is separable; no exceptional branch count is imported.
HEIGHT=Exact physical R<=B. H=max(|a|,b) is only an auxiliary height of reduced u=a/b, a!=0, b>0. No raw parameter-box substitution.
DEPENDS_ON=Audited105 residual quartic and physical negative-square norm; audited106 z_phys=S/2; audited109 specialization router; audited036 fixed-u physical fibers only for the no-new-count comparison; audited106/107 local no-double-charge firewall. Standard ideal valuation, Dirichlet S-unit and localized class-group facts are proved/recalled below.
ALIASES=S4IntegralGeneratorSupport; S4EvaluationDenominatorScalarCorrection; S4UniversalMinusOneNormWitness; S4NormKernelPacketClassGroupBarrier.
DUPLICATE_SEARCH=Targeted MAIN, INDEX, RESULT-LEDGER, active ROUTE, NEGATIVE-REGISTER and CARD-INDEX searches for unramified support, integral generator, class group, S-unit, discriminant, denominator normalization and norm witness. 105 owns the physical norm [-1]; it does not give the integral packet or universal witness below. 106/107 own the interior local tuple and are not reopened.
DUPLICATE_OF=NONE
SUPERSEDES=No previous theorem. Refines the open nonlocal S4 frontier with explicit coordinates and retires only empty coarse norm-fiber screening and support-label enumeration as standalone saving mechanisms.

## 1. Integral model and exact scalar correction

Put N=a^2+b^2, Delta0=2b^2-25a^2, T0=a^2+2b^2 and
F(X)=N X^4-8ab X^3+(11a^2-b^2)X^2+6ab X-a^2.
Then F=b^2 Q_u and its monic version F/N defines K_u on the S4 complement.

Let theta be its root and alpha=N theta. The integral monic polynomial of alpha is
G(X)=N^3 F(X/N)
=X^4-8abX^3+N(11a^2-b^2)X^2+6abN^2X-a^2N^3.

Exact discriminants:
disc(F)=16a^2 N^2 Delta0^3,
disc(G)=16a^2 N^8 Delta0^3.
Delta0!=0 for nonzero rational u, since 25(a/b)^2=2 has no rational solution.
The order Z[alpha] need not be maximal. Its index has no prime outside disc(G), which is all that the proof needs; do not equate order and field discriminants.

Write the actual physical z=S/2=m/n in lowest terms, n>0. Define
beta=N m-n alpha=N n(z-theta).
It is an algebraic integer and is nonzero since the physical norm is nonzero on the retained distinct-root locus.

For F_h(m,n)=N m^4-8abm^3n+(11a^2-b^2)m^2n^2+6abmn^3-a^2n^4,
Norm(beta)=N^3 F_h(m,n).
Audited105 gives F(z)/N=-w^2 for a nonzero rational w. Hence
Norm(beta)=-(N^2 n^2 w)^2.

The exact original squareclass is
[z-theta]=[N n beta] in K_u^*/K_u^{*2}.
This scalar correction is essential. beta is NOT generally the original class. The actual evaluation denominator has been removed from the normalized packet, not silently removed from the physical descent class.

## 2. Denominator-free finite-prime support theorem

Let S_u be the set of rational primes dividing 2aNDelta0, and S_K the prime ideals of O_K above S_u. Define
K(S_K,2)={ [c] in K^*/K^{*2}: v_P(c) is even for all P outside S_K }.

For every retained physical point,
[beta] belongs to K(S_K,2).

Proof: take p not in S_u. The order Z[alpha] is maximal and etale at p, N is a p-unit, and G mod p is squarefree.
If p divides n, primitiveness makes m a p-unit; beta=N m-n alpha is a unit at every prime above p.
If p does not divide n, beta can vanish only where alpha has residue N m/n in F_p. Squarefreeness means at most one prime ideal divides beta, and that prime has residue degree one. The p-valuation of Norm(beta) is therefore exactly its ideal valuation there. The norm is a negative rational square, so this valuation is even. All other valuations are zero.
This proves the statement, including primes in the moving evaluation denominator n. It is an ideal squareclass theorem, not an assertion that beta itself is an S-unit or a square.

At these odd good primes, the corresponding quadratic extension K(sqrt(beta))/K is unramified. Archimedean signs are retained; no positivity or full local Selmer condition is inferred.

## 3. Universal negative-square norm witness

Define the nonzero algebraic integer
gamma=alpha(aN-b alpha).

Exactly,
Norm(alpha)=-a^2 N^3,
Norm(aN-b alpha)=a^2 N^3 T0^2,
Norm(gamma)=-(a^2 N^3 T0)^2.

The second identity is the evaluation F(a/b)=a^2 T0^2/b^4. All quantities in the square are nonzero for a!=0, b>0.

Furthermore [gamma] belongs to K(S_K,2), with NO enlargement by primes of b or T0.
Proof: outside S_u, alpha is a unit by its norm. If p divides b, aN-b alpha is a unit everywhere. If p does not divide b, only the one degree-one prime with alpha=aN/b mod p can divide the second factor, and its norm valuation is even because Norm(aN-b alpha)=a^2N^3T0^2. The same good-order argument as Section2 applies.

Therefore the coarse supported norm fiber
H_u^-={c in K(S_K,2): [Norm(c)]=[-1]}
is NONEMPTY for every rational u on the retained S4 complement:
[gamma] belongs to H_u^-.

This is stronger than merely noting that physical points have norm [-1]. No physical point was used to construct gamma. Screening u by emptiness of this particular coarse supported norm fiber can never remove a u.

Important boundary: H_u^- is NOT the full genus-2 fake Selmer set, NOT the everywhere locally soluble descent image, and NOT the realized physical point image. gamma need not lift to any physical point or any full genus-2 two-cover. Smaller/local-compatible sets can still be empty. No Perfect Cuboid existence is inferred.

## 4. The remaining object is a norm-kernel coset

Let
V_u=ker(Norm: K(S_K,2) -> Q^*/Q^{*2}).
Then exactly H_u^-=[gamma] V_u.

For a physical point set
xi=beta/gamma.
It satisfies [xi] in V_u, and the original class is recovered as
[z-theta]=[N n gamma xi].

This preserves genuinely non-norm information instead of taking its norm and declaring it trivial. Neither xi nor V_u is proved trivial or fixed. The audited106/107 primewise tuple remains consumed; this construction gives no additional local selector at those primes.

## 5. Explicit finite-label bound and its missing counting adapter

There is the standard exact sequence
1 -> O_{K,S_K}^*/O_{K,S_K}^{*2}
  -> K(S_K,2)
  -> Cl(O_{K,S_K})[2]
  -> 1.
The map sends a class with even valuations outside S_K to the ideal square root class. Surjectivity follows because a 2-torsion ideal class has a square principal ideal in the localized ring.

Dirichlet gives |O_{K,S_K}^*/O_{K,S_K}^{*2}|=2^(r1+r2+|S_K|), and degree4 gives r1+r2<=4, |S_K|<=4|S_u|.
The localized class group is a quotient of Cl(K); for a finite abelian group, a quotient has no larger F2 dimension modulo2, so
|Cl(O_{K,S_K})[2]|<=|Cl(K)[2]|.
Consequently
|V_u|=|H_u^-| <= |K(S_K,2)|
<=2^(4+4 omega(|2aNDelta0|)) |Cl(K_u)[2]|.

No class groups were computed or assumed odd. No uniform B^o(1) bound for this moving quartic family is proved here.
For H=max(|a|,b), |2aNDelta0|<=100H^5 and |disc(K_u)|<=|disc(G)|<=64,000,000H^24. In a retained polynomial physical height range the elementary 2^omega factor is B^o(1); the class-group factor must remain.

Even an additional small-class-group theorem would only give few labels PER u. Audited036 already gives B^o(1) physical endpoints per fixed u. It would not reduce the number of moving realized u values, and labels in different K_u cannot be identified without an exact cross-field adapter. No bound on occupied u, no support-cardinality contraction and no fixed-power endpoint saving follows from this finite-label count.

## 6. Result and continuation

PROVED: exact integral generator/discriminant; normalized physical beta has no odd ideal valuation outside S_u; exact original scalar correction [N n beta]; universal supported negative-square norm witness gamma; explicit remaining norm-kernel coset with class-group-aware cardinality.

RETIRED_AS_STANDALONE_SAVING: empty coarse norm-fiber screen; divisor/support-label enumeration per moving u; assumption that bounded rational bad support automatically makes a moving quartic class group negligible.

OPEN_S4_GATE: a genuinely non-norm local-compatible/global realization obstruction or a same-R<=B cross-u theorem controlling the realized xi image, preserving original scalar N n, class-group data, fixed-u multiplicity and exceptional phi/psi complements. No blanket S4 no-go or full Selmer collapse is claimed.

No same-measure global support/dispersion theorem emerged from this coarse packet attack. Execute MAIN122's specified backup: next M3-T11-124 should start ThetaFourthPowerMovingSupportBeyondKummer, with audited096 Kummer/2-isogeny firewall and095 tangent-coordinate no-double-charge retained. Consult093/095/096 and the matching canonical ledger cards only; do not reread full history. Keep this explicit S4 kernel gate as a retained alternative; reopen it for genuinely new realization information, not another norm/support enumeration.

DO_NOT_REPEAT=Do not identify beta with z-theta; restore N n. Do not equate K(S_K,2) or H_u^- with the full Selmer set. Do not infer physical points from gamma. Do not erase Cl(K_u)[2], confuse an even ideal with a principal square, equate disc(G) to field discriminant, identify labels across moving fields, or charge finite labels per u as a second fixed-u saving. Do not revive106/107 primewise selectors,120 root lock, or122 phi support route.
REOPEN_CONDITION=An audited normalization/ideal argument fails, or a new exact same-measure theorem controls the realized norm-kernel/local-compatible image across moving fields.
AUDIT_MODE=Within-session adversarial rederivation, exact Wolfram symbolic resultants/discriminants and independent standard-library Python integer determinant checks; not externally staffed audit.
VERIFICATION=182 primitive signed u packets; 182 independent 7x7 discriminant determinants; 1,092 beta norm determinants; 182 gamma norm determinants; 1,962 good-prime support checks. These support the exact proof and enumerate no physical endpoints. No class-group/GRH computation is used.
REFERENCE=Bruin–Stoll, Two-cover descent on hyperelliptic curves, arXiv:0803.2052v2, Section6 for finite unramified squareclass packets and distinction from locally compatible fake Selmer sets. Used for method context only; the Stage37 integral scalar and witness identities are proved here. https://arxiv.org/html/0803.2052v2
NEXT_RESEARCH_CARD_ID=M3-T11-124
NEXT_ATTACK=ThetaFourthPowerMovingSupportBeyondKummer
GLOBAL_FIXED_POWER_SAVING=false
M3_T11_PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false

