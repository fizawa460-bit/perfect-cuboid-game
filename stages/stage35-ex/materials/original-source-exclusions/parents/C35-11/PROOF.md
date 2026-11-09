# Stage35EX C35-11 — certified global arithmetic and reduced-support 2-descent
DATE=2026-10-11 JST
FORMAL_AUTHORITY=V74_GOAL4AK / Section334 unchanged
ACTIVE_ROUTE=INNER_BRANCH_B_INFINITE_ORDER_CLASS_RANK_GROWTH
STATUS=SCOPED_MATHEMATICAL_AUDIT_PASS_COMPUTER_ASSISTED
SIGNED_INDEX6_PHYSICAL_EXCLUDED=false
BRANCH_B_CLOSED=false
STAGE35_CLOSED=false
E1_PROVED=false
GITHUB_ACCESSED=false

## Theorem
For C3': y²=f(x)=xP(-x), P=t⁶−5t⁵−8t⁴−5t³−8t²−5t−1, let J3=Jac(C3'). Then dim Sel²(J3/Q)=2, rank J3(Q)=1 and Sha(J3/Q)[2]=0.
This is a scoped proof about J3, not the genus2 Jacobian of y²=−P(u), not Section334's auxiliary Hc, and not a Stage35 closure certificate.

## Standard theorem instantiated, not a fake descent
Michael Stoll, Implementing 2-descent for Jacobians of hyperelliptic curves, Acta Arith.98(2001),245–277, §4, Lemmas4.1,4.3,4.4, Prop4.6, Cor4.7:
https://www.impan.pl/shop/en/publication/transaction/download/product/83397
f is monic, integral, separable and odd degree7. Its étale algebra L=Q[X]/f is Q×K with X=(0,−t), K=Q[t]/P. Under the norm-kernel identification H¹(Q,J3[2])=ker(N:L*/L*²→Q*/Q*²), a class alpha in K*/K*² is represented by (N(alpha),alpha); the rational coordinate is determined modulo squares, NOT an extra independent S-unit factor.
For ordinary points the Kummer pair is (x,x+t). For T0=(0,0)−infty the branch formula gives (f'(0),t)=(−1,t). For a degree2 divisor with monic support U the pair is (U(0),U(−t)); the degree sign is positive. This verifies the conventions used by C35-09, including both quadratic witnesses.

## New support reduction
Disc(f)=2^16*3461. Proposition4.6 says that at any odd p with p² not dividing disc(f), the local Kummer image is the unramified kernel of valuations. Hence 3461, despite bad reduction, requires no S-unit support. Cor4.7 gives S={infty,2}. It is safe and sufficient for an upper bound to retain only these facts: Sel² is contained in K squareclasses with even valuations outside2, and its restriction at2 lies in the genuine Kummer image. Real and3461 calculations are no longer load-bearing for this upper bound.

## Independent global certification
PARI/GP2.15.4 bnfinit(P,1), bnfcertify(b)=1. This removes GRH dependence of the number-field data; it is NOT a call to a genus3 TwoSelmerGroup routine.
Discriminant55376, signature(2,2), class number1, power-order index64, roots of unity{±1}. C35-09's supplied basis has integral change matrix of determinant1 relative to PARI's maximal order.
The supplied U1,U2,U3 have PARI exponent columns (1,0,0),(1,0,1),(−1,−1,0), with determinant1; their roots-of-unity signs are retained. Thus they generate the FULL unit lattice, not just a finite-index subgroup.
pi2=(−2,−1,1,2,1,0) in the supplied basis has principal ideal precisely the unique prime above2, exponent1; e=3,f=2. Therefore the global ambient space is generated freely modulo squares by −1,U1,U2,U3,pi2, dimension5, exactly32 classes. No hidden class-group2 classes or missing unit-squareclasses remain.
For completeness PARI also certifies the two primes above3461, (e,f)=(2,1),(1,4), and that GA,GB generate them separately; the old128-candidate enumeration was exhaustive too.

## Complete local image at2
The maximal order O/8 is computed by exact integral multiplication; all36 products checked against rational polynomial reduction. There are48 unit residues mod2,196608 units mod8 and1536 square units. Squares depend on residues mod4. Hence the unit-squareclass quotient has128 elements. A unit congruent to a square mod8 is a true square in the unique degree6 local field: error valuation at least9, strictly greater than2v(2)=6, so Hensel applies. Uniformizer parity plus this unit quotient gives the complete local squareclass test.
The four witnesses are T0, the point x=−180, and the traces of points with x=29+sqrt(−1014) and x=16+alpha, alpha²=alpha+1. C35-09's exact polynomial evaluations and mod16 Hensel witnesses were reexecuted and audited: the proposed roots are units; errors have valuations8>4 in the ramified quadratic and4>2 in the unramified quadratic. Their traces are genuine Q2-rational degree2 divisors. Their pairwise16 product classes are distinct.
P is irreducible overQ2 because its local algebra has one field factor of degree6. Thus f has exactly2 irreducible local factors, dim J3(Q2)[2]=1, and Stoll Lemma4.4 gives dim J3(Q2)/2J3(Q2)=3+1=4. The four independent witnesses EXHAUST the local image.
Testing the32 global classes against that exact16-class image leaves masks0,3,5,6, i.e.1,−U1,−U2,U1U2. This proves dim Sel²≤2 without any real or3461 computation.

## Lower bound and rank without Coleman
T0 and D2=(U=x²−x−1,V=−4x) are actual rational Jacobian classes. The new verifier checks V²=f modU and explicit square-root identities inK:
R_T² U2+t=0 modP,
R_D² U1U2−(t²+t−1)=0 modP,
R_T=(5+17t+5t²+13t³+17t⁴−3t⁵)/4,
R_D=(−9−19t−9t²−25t³−15t⁴+3t⁵)/4.
Thus delta(T0)=−U2 and delta(D2)=U1U2. Fundamental-unit certification makes these two independent global classes. J3(Q)/2J3(Q) therefore has dimension≥2.
P irreducible overQ gives dim J3(Q)[2]=1. For any finitely generated group, dim J(Q)/2J(Q)=rank+dim J(Q)[2]. Hence rank≥1. The Selmer upper bound yields rank≤1, dim Sel²=2 and Sha[2]=0. No numerical log nonzero test or uncertain torsion enumeration is needed.

## Audit and novelty
The whole retained INDEX was searched for C35/Selmer/Schaefer/Coleman/fixedP/genus3, plus NEGATIVE/HOLD/retracted/source-primitivity entries. C35-06–10's local witnesses, cosets and square-root identities are OLD. New credit is the unconditional PARI global certification, determinant1 unit saturation, Stoll's support reduction128→32, and the Coleman-free rank/Sha proof. S324/S328/S333/S334 concern different Jacobians. S275 noncritical-H HOLD and all source/physical gates remain unchanged.

## Reproduction
Run global_cert.gp with PARI/GP≥2.15; verify BNFCERTIFY=1, SUPPLIED_BASIS_DET=1, UNIT_TRANSITION_DET=1 and principal-ideal decompositions. Run selmer/c35_11_reduced_support.py with Python3+SymPy. It contains no independent_3461 import, real-sign filtering or random local-image sampling. Compare reduced_support.log. Source files and outputs are in the accompanying ZIP.
