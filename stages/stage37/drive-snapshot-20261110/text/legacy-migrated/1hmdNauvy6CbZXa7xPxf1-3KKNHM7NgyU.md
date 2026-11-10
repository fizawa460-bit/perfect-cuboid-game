# M3-T11-129 — A globally compatible S4 pole class survives every nonpole local residual evaluation test

STATUS=PROVED_EXPLICIT_S4_FAMILY_AND_LOCAL_IMAGE / WITHIN_SESSION_ADVERSARIAL_AUDIT_PASS / GLOBAL_COUNTING_CREDIT0
TYPE=GLOBAL_SIGNATURE_INTERSECTION_CERTIFICATE / RESIDUAL_DESCENT_POLE_FIREWALL
POPULATION=Retained irreducible-S4 rational-u frontier. The constructed family consists of algebraic residual-curve packets ONLY; no member is claimed a physical endpoint.
HEIGHT=Original physical R<=B stays authoritative. H=max(|a|,b) below is explicitly an auxiliary reduced-u height, not a physical height.
DEPENDS_ON=105 necessary residual quartic;106 z=S/2;109 S4 router;123 integral packet;128 exact real image. Finite-field factorization/Frobenius and elementary local square criteria.
ALIASES=S4SquareNormGlobalSignatureWitness; ResidualPoleClassNonpoleLocalPersistence; S4PythagoreanAPImpostor.
DUPLICATE_OF=NONE. Targeted ledger/active-route searches found123's universal gamma and128's gamma exclusion, but no globally realized alternate class with certifiedS4 and nonpole local persistence.
SUPERSEDES=No retained theorem.128's gamma exclusion remains valid. Resolves nonemptiness of128's refined real packet on the explicit family below, not all S4 u.

## 1. An explicit infinite four-real S4 family
For every integer k>=0 put r=8+66k and
a=2r, b=r²-1, c=r²+1, u=a/b, N=a²+b²=c².
r is even, gcd(a,b)=1, a>0,b>0. The reduced u are distinct (2r/(r²-1) is strictly decreasing forr>1). Set
D0=2b²-25a²=2(r⁴-52r²+1)>0 forr>=8.
Use123/128's quartic
F(X)=N X⁴-8abX³+(11a²-b²)X²+6abX-a².
It is separable with four real roots by128.

Every r in this progression has r=8mod3 and r=8mod11. Consequently
F mod3 = X⁴+2X²+2,
F mod11 = (X+2)(X³+8X²+8X+4).
Both reductions have leading coefficient1 and are squarefree. The mod3 quartic has no linear or quadratic factor: no roots, and for a factorization into monic quadratics the constant terms must be1,2, the zero cubic/linear coefficients force the linear coefficient0, and then the quadratic coefficient would be0 rather than2. The mod11 cubic has no root: its values at0,...,10 are4,10,5,6,8,6,6,3,3,1,3. It also does not vanish at-2.
Thus F is irreducible overQ and its Galois group contains a4-cycle and a3-cycle. A subgroup ofS4 containing both has order divisible by12; the order12 subgroup isA4 and has no4-cycle. Hence Gal(F/Q)=S4 for EVERY k>=0. This is an explicit congruence certificate, with no Hilbert irreducibility, GRH or density assumption.
The first example is r8,a16,b63,c65,D01538,
F=4225X⁴-8064X³-1153X²+6048X-256.

## 2. The alternate globally realized class
The residual genus1 curve C_u: w²=-F(z)/N has the rational non-root point
P0=(z=0,w=a/c), since -F(0)/N=(a/c)².
This is an EXCLUDED physical pole, not a physical endpoint. It nevertheless produces a genuine global residual evaluation class.

Let theta be a root ofF, alpha=Ntheta, G(X)=N³F(X/N). AtP0, n1,m0 give
c0=beta0=-alpha,
Norm(c0)=-a²N³=-(a c³)².
c0 is a unit at every prime ideal outside123's S_K (primes over2aND0), so[c0] lies in the supported norm[-1] fiber. As N=c²,
[-theta]=[N c0]=[c0] in K*/K*²,
and also in its rational-scalar quotient. No denominator has been discarded from a general physical point; the equality is specific to this point and squareN.

With gamma=alpha(aN-balpha), define the explicit norm-kernel class
xi0=c0/gamma=-1/(aN-balpha).
Then
Norm(xi0)=1/(a²N³(a²+2b²)²)=(1/(a c³(a²+2b²)))²,
and[xi0] belongs toV_u.128's ordered roots yield
sign(c0)=+---, sign(gamma)=-+--, sign(xi0)=--++.
Therefore --++ belongs to sigma_inf(V_u) intersectT_u for EVERY member of this certifiedS4 family. In particular128's real-compatible packet is nonempty here. xi0 is nontrivial because it has two negative real embeddings. No signature surjectivity, class-group computation or norm-kernel triviality is inferred.

## 3. Removing the pole from EACH LOCAL point set does not remove its class
This is stronger than merely presenting the forbidden pointP0. For every finite rational prime p, let v_p be normalized byv_p(p)=1, also on finite extensions. For any root theta ofF in an algebraic closureQ_p,
v_p(theta)<=2v_p(a).
Proof: if its valuation exceeded2v_p(a)>=0, every nonconstant term ofF(theta) would have valuation greater than its constant term-a², since all coefficients are integral. Their sum could not vanish.

Choose depth d_p=3+2v_p(a) and z_p=p^d_p. Then, simultaneously at all factors ofK tensorQ_p,
v_p(z_p/theta)>=3,
beta(z_p)/c0=(Nz_p-alpha)/(-alpha)=1-z_p/theta
is a square. For oddp, a unit congruent1 modulo the maximal ideal is square. Atp2, valuation>=3 exceeds twicev_2(2); the usual Hensel square criterion works even in ramified finite extensions. Thus the NORMALIZED local class is exactly[c0].

Furthermore F(z_p)/F(0) is a rationalp-adic unit congruent1 modulo p³. Indeed
F(z)/F(0)=1-(6b/a)z-((11a²-b²)/a²)z²+(8b/a)z³-(N/a²)z⁴,
and at the chosen depth every nonconstant term has valuation>=3. Hence
-F(z_p)/N=(a/c)²*F(z_p)/F(0)
is a nonzero square inQ_p. There is a local point with z_p!=0, F(z_p)!=0, and the SAME evaluation squareclass. In fact a sufficiently small open neighborhood around0 has this property, so any additional finite list of z-coordinate poles can also be avoided. This does not establish the full physical packet conditions on such points.

At infinity choose a sufficiently small nonzero real z near0. F(z)<0 and1-z/theta_i>0 at all four roots, so the same real class is realized. Complex places present no squareclass restriction. The local points at different places are chosen SEPARATELY; no single common nonzero rationalz or physical lift is produced.

The original evaluation class is[z-theta]. In this family N is a rational square and the constructed finite z_p is integral (n1), so its local original class also equals[c0]. For arbitrary physical z=m/n continue to restore[Nn gamma xi]. No general n-removal is licensed.

Conclusion: this global class survives every place's residual non-root, nonpole local evaluation image, including all bad primes2aND0. Excluding z0 from the local source does NOT exclude its descent class. A full residual fake-Selmer computation (with its correct rational-scalar quotient) cannot remove the class merely by this local exclusion. This is only aboutC_u, not the full physical genus2 cover or exact-height lift.

## 4. Scope of the obstruction
The auxiliary height here is H=b=r²-1. Thus H<=H0 contains (1/66)*sqrt(H0)+O(1) distinct certifiedS4 u in this family, all carrying the globally compatible class and local nonpole representatives. This is an auxiliary-parameter count ONLY. It gives no lower bound on physical endpoints underR<=B, no allS4 nonemptiness theorem, and no impossibility theorem for the full physical route.

RETIRE_ONLY=On this squareN S4 family, a standalone screen based on residual supported norm, real compatibility, all finite residual local compatibility and deletion of pole coordinates from local evaluation sources. Such a screen keeps every member above.
KEEP_OPEN=Actual global nonpole residual points; full physical-cover lift; simultaneous coefficient/content/splitting constraints; exactR<=B; compatibility across movingu. Other S4 u may still have empty local-compatible packets.
Retain123's Cl(K_u)[2] factor and128's signature-kernel cardinality. One exhibited class per movingu neither computes the full packet nor gives a physical count. No105–107 local density is recharged. No129 condition closesM3-T11-GATE-001.

## 5. Verification and primary references
Replay checks26 AP members r=8+66k,k0..25: primitive squareN, four-real roots by exact rational Sturm arithmetic, independent mod3 factor exhaustion and mod11 cubic certificate, integer matrix determinants for Norm(c0) and Norm(aN-balpha), norm-kernel square and --++ sign. It also performs286 exact rational local square checks at eleven primes per member, including all bad primes2,5,13,769 forr8. The all-prime claim is proved inSection3, not extrapolated from finite tests. No physical endpoints or class groups computed.
Wolfram checksD0 and the mod3/mod11 factorization independently. The replay's initial companion-matrix coefficient mistakenly included an extraN in the cubic coefficient; it was corrected to-8ab before any result promotion. The retained script/output pass all assertions.
Primary sources: J.S.Milne, Fields and Galois Theory(v5.10), Chapter4, factorization modulo good primes and cycle types; https://www.jmilne.org/math/CourseNotes/FT.pdf (author site https://www.jmilne.org/math/).
Bruin–Stoll, Two-cover descent on hyperelliptic curves, arXiv:0803.2052v2, Sections4–6 for local evaluation images/scalar quotients. https://arxiv.org/html/0803.2052v2
The AP family, explicit xi0 and quantitative local persistence are proved here; no quoted source supplies a physical lift.

NEXT_RESEARCH_CARD_ID=M3-T11-130
CURRENT_ATTACK=S4FullPhysicalLiftBeyondResidualPoleClass
NEXT_LEGAL_ACTION=Start from129's explicit S4 squareN family and the original105/106 physical equations. Derive the full physical-cover lift above[c0]/[xi0], with actual z=S/2, denominatorn, all packet/splitting constraints and exactR<=B. Determine which extra global equation distinguishes actual physical evaluations from residual genus1/local nonpole impostors; seek a same-measure moving-u theorem. Do not repeat residual norm/sign/local-pole screening or claimP0 physical. Retain non-squareN S4 complement as open,123 classgroups,128 sign table,120 retraction and105–107 no-double-charge. TI stays parked; theta full original-r gate remains open but inactive.
DO_NOT_REPEAT=No local nonpole representative=>common global nonpole point; no residual rational point=>full physical lift; no auxiliaryH count=>R count; no universal allS4 claim from this AP; no gamma-exclusion=>packetempty.
AUDIT_MODE=Within-session adversarial rederivation, not external audit.
GLOBAL_COUNTING_CREDIT=0
GLOBAL_FIXED_POWER_SAVING=false
PRIMARY_GATE_CLOSED=false
M3_T11_PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false
