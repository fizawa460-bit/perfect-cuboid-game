# M3-PESCH-TI-003 — unconditional modular two-isogeny certificates and exact closed-source receiver

STATUS=PROVED_PARAMETER_UNIFORM_CERTIFICATE_CRITERION / TWO_REPLAYED_TI_CLOSED_SOURCES / WITHIN_SESSION_ADVERSARIAL_AUDIT_PASS
SCOPE=Pointwise rank-zero certificates; no infinite-family cardinality, density or weighted saving theorem.
PRIMARY_GATE=M3-PESCH-TI-GATE-001 OPEN
DEPENDENCIES=TI-001 exact endpoint adapter; TI-002 E3 split model/torsion screen; active route's physical mu_B.
1072_AGGREGATE=HOLD
E3_RANK_ZERO_ARITHMETIC_FAMILY_DISTRIBUTION_PROVED=false
GLOBAL_FIXED_POWER_SAVING=false
P_OVER_M3_LIMIT_PROVED=false

## 1. Exact two-isogeny descent interface

For every primitive source p=(m,n), let U=m^2-n^2, V=2mn, W=m^2+n^2 and S=V^2+W^2. TI-002 identifies E3 with

E: Y^2=X^3-2S X^2+U^4 X.

Its kernel-(0,0) two-isogenous curve is

E': Y'^2=X'^3+4S X'^2+16V^2W^2 X'
             =X'(X'+4V^2)(X'+4W^2).

Thus (a,b)=(-2S,U^4), (a',b')=(4S,16V^2W^2). Both are square-b models, but their descent images must BOTH be controlled. A single trivial image does not prove rank zero.

For any model y^2=x^3+a x^2+b x, alpha(O)=[1], alpha((0,0))=[b], alpha((x,y))=[x] otherwise, as a homomorphism to Q*/Q*2. Its kernel is the dual-isogeny image. A signed squarefree representative d of a nontrivial image must divide b; the corresponding cover has coprime integers z,t and an integer c satisfying

c^2=d z^4+a z^2 t^2+(b/d)t^4.                 (C_d)

Derivation: write x=d(z/t)^2 and y=d z c/t^3. The resulting c is rational with integral square, hence integral. At primes not dividing b an odd valuation of x is impossible from the cubic, so no other primes occur in d. Exceptional points O,(0,0) contribute the already retained class 1 here since b is square. The t=0 and z=0 residues are not dropped by the local tests.

For E, x<0 gives a negative cubic; equivalently every term of C_d is negative for d<0 since a<0, b>0. Thus only positive squarefree divisors of U need consideration. For E', both signs of every squarefree divisor of 2VW must be considered, including the prime 2 and primes appearing to even powers in V or W.

The standard two-isogeny formula is

2^rank(E(Q))=|im(alpha)|*|im(alpha')|/4.

One can see the index normalization directly here. E has full rational two-torsion, so [E(Q):2E(Q)]=2^(r+2). The kernel of the dual isogeny lies in the image of the forward isogeny (the two nonzero-root points of E map to (0,0) on E'); composing the quotient maps therefore gives the product of the two descent indices, with no extra factor. This agrees with the general two-isogeny formula.

## 2. Four unconditional classes on E' and a uniform certificate theorem

Let d0=sf(VW)>1 (positive squarefree kernel). TI-002's Fermat argument proves VW nonsquare. The following E' points verify four distinct descent classes:

O -> [1]; (-4V^2,0) -> [-1];
(4VW,8VW(V+W)) -> [d0];
(-4VW,8VW(W-V)) -> [-d0].

These points are rational and nondegenerate because W>V>0. Their cubic identities are checked exactly by the independent verifier. Set T'={1,-1,d0,-d0}.

For a finite list of prime powers q^k, reject d if C_d has NO solution modulo q^k with (z,t) primitive at q (not both divisible by q). Let S_E and S_E' be the remaining candidate sets, retaining 1 and the four known dual classes.

CERTIFICATE THEOREM: if S_E={1} and S_E'=T', then rank(E3(Q))=0 unconditionally. If also p is in TI-002's G_tor, then p is TI_CLOSED by criterion A and has no nondegenerate endpoint fiber.

Proof: every rational point gives a primitive integral cover solution, hence its class survives every modular test. Therefore im(alpha) subset S_E, im(alpha') subset S_E'. The explicit points give equality in the cardinality bounds 1 and 4, so the descent rank formula gives rank zero. No analytic rank, GRH, BSD, Manin constant or Sha assumption is used.

This is a parameter-uniform, executable sufficient criterion. It does NOT prove that an infinite set of primitive sources passes it, or that its complement has small M3 weight. A surviving cover is UNKNOWN; modular survival is not proof of local or rational solubility, and failure of the certificate is not positive rank.

## 3. Complete certificate replay for two sources

The standard-library ti003_descent.py was run for ALL primitive m<=12 (31 sources). Exactly two passed this finite schedule. The other 29 remain UNKNOWN under this schedule. Neither finite completeness nor these 29 statuses concern all primitive sources.

| p | (U,V,W) | S_E | S_E' | result |
|---|---|---|---|---|
| (4,1) | (15,8,17) | {1} | {-34,-1,1,34} | rank 0, torsion 4, TI_CLOSED |
| (9,4) | (65,72,97) | {1} | {-194,-1,1,194} | rank 0, torsion 4, TI_CLOSED |

Both have 7 not dividing UVW and therefore satisfy TI-002's torsion-four screen. These are independently replayed certificates, whether or not their source IDs occur in the unverified external 1072 list. No claim is made that these are previously unknown fibers. They establish a local proof mechanism independent of the disputed external aggregate.

All candidate exclusions for these rows are explicit:

| p | model | rejected squarefree d | obstruction modulus |
|---|---|---|---|
| (4,1) | E | 3,15 | 2^6 |
| (4,1) | E | 5 | 17^2 |
| (4,1) | E' | +/-2,+/-17 | 5^3 |
| (9,4) | E | 5,65 | 3^4 |
| (9,4) | E | 13 | 97 |
| (9,4) | E' | +/-2,+/-3,+/-97,+/-582 | 5^3 |
| (9,4) | E' | +/-6,+/-291 | 13^2 |

The first row's E coefficients are a=-706,b=50625; its E' coefficients are a'=1412,b'=295936. The second row uses S=14593, a=-29186,b=65^4; a'=58372,b'=16*72^2*97^2.

The producer enumerates the two projective affine charts modulo q^k: t=1 with all z; z=1 with t divisible by q. Every primitive pair is unit-equivalent to one of these, and unit scaling multiplies the quartic by a fourth power, preserving squareness. This avoids silently discarding pairs where t is not a unit.

audit_ti003.py separately enumerates EVERY primitive residue pair (z,t), without using the chart optimization. It independently confirmed all 22 rejection witnesses, the explicit dual point identities and the two torsion screens. ti003_certificates.json retains all 31 rows, candidate survivors and exact witnesses, so a new session can replay this result from Drive alone.

## 4. Exact physical-weight connection, without a density substitution

Define C_mod as the primitive sources in G_tor which pass a chosen finite-modulus certificate schedule above. The theorem gives C_mod subset TI_CLOSED. For any chosen certified subset C (including the two replayed sources), use the active route's exact symmetric physical measure:

F_B(C)=sum_{p in C,q}mu_B(p,q),
R_CC(B)=sum_{p,q in C}mu_B(p,q).

Every endpoint has neither source in C. Inclusion-exclusion therefore gives

P(B) <= R_notC_notC(B)
     = M3(B)-2F_B(C)+R_CC(B).

This identity uses the same physical R<=B and one count per canonical object. It holds for coincident sources. Two-source independence is unnecessary. The R_CC term must be restored: simply subtracting 2F_B(C) double-counts objects having both sources closed.

Operationally, C can be enlarged only with verified certificate witnesses; discarded/UNKNOWN rows stay in the complement. The generic criterion enables certification, not an estimate of F_B(C) or R_CC(B). Neither weight was evaluated here. No finite closed set, naked count 2/31, or a constant closed proportion proves P/M3->0.

The existing TI-002 positive-rank/exceptional receiver remains valid. The certificate receiver is an additional exact bound, not independent saving to multiply into TI-002's bound. Use either stronger bound or intersect exclusions on the same mu_B; do not subtract the same effect twice.

## 5. Continuation and limits

NEXT_CARD=M3-PESCH-TI-004 after duplicate check.
NEXT_LEGAL_ACTION=Convert successful modular obstructions into a clearly described arithmetic source family, with membership proved from factorization/Legendre conditions, and assess its exact Master physical source weights. Alternatively derive a useful uniform local-descent upper bound on the weighted uncertified complement. Avoid blind expansion of a finite rank table without a family or weight hypothesis.

UNSOLVED=No infinitude/density for C_mod; no exact numerical or asymptotic physical weights; no all-source torsion theorem; no 1072 worker validation; no EuV-family promotion; no global gate closure.

Primary references checked in this session:
- SageMath official two-isogeny descent documentation, distinction between covers with rational points and everywhere locally soluble covers; rank normalization log2(n1)+log2(n1')-2: https://doc.sagemath.org/html/en/reference/arithmetic_curves/sage/schemes/elliptic_curves/descent_two_isogeny.html
- Ahmadi–Janfada, On quartic Diophantine equations with trivial solutions in the Gaussian integers, IEJA 31 (2022), section 2 recalls the rational two-isogeny maps and signed-divisor quartic framework: https://www.ieja.net/files/papers/volume-31/10-V31-2022.pdf . No Gaussian-field rank theorem is imported into Stage37.

SAVE_CONTRACT=Card, in-session audit, producer, independent verifier and full certificate JSON in Stage37; MAIN/INDEX/LEDGER/active ROUTE/CARD-INDEX updated and read back.
