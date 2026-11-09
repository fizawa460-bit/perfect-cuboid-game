# Problem W: completion for (2,3) and (3,3)

2026-11-09. Status: exact finite-field computation + elementary characteristic-zero lifting proof. Not independently audited or proof-assistant formalized. Previous (2,2) certificate is retained separately. No research ledger has been modified.

## Statement

Over characteristic zero, for B={0,infinity,1,-1,i,-i} with labels e,b,a in consecutive pairs, there is no pair of rational maps of degrees (2,3) or (3,3), both slack zero, birational onto their co-image, with labelled discrepancy |Omega|<=4. Source P1 ensures gamma=0.

The full splitting field in characteristic zero is NOT constructed. We use exact arithmetic in F_p, p=874009, plus uniquely lifting normalized cubic maps and marked simple fibers. This is not the invalid implication that absence of F_p points implies absence of geometric points. All covers and all their marked odd points split over F_p, and three-point alignment forces every geometric candidate relative Mobius transformation to be F_p-rational.

## 1. Complete enumeration and good reduction

Degree two: one cover per unordered pair of critical values, 15 total. With homogeneous critical values u,v, choose (u_x+v_x*t^2)/(u_z+v_z*t^2). Resultants are units away from 2.

Degree three: four distinct simple critical values (a degree-three fiber cannot contain two points of local degree two). Order the four values y0,y1,y2,y3, choose N(y0)=0,N(y1)=infinity,N(y2)=1, z=N(y3). Normalize their critical points in the same order. Every cover is N^{-1} composed with

 F_k(t)=t^2*((2k-1)t+2-3k)/(t-k),
 H_z(k)=k*(3k-2)^3-z*(2k-1)=0.

This normal form follows by writing P=t^2*(A*t+C), Q=t-k, and imposing F(1)=1,F'(1)=0. A=2k-1,C=2-3k. Hence it is complete and its parameter is unique.

The fourth critical point is c=k*(3k-2)/(2k-1). Exact identities:
- Res(P,Q)=-2*k^2*(k-1)^2.
- derivative numerator =2*t*(t-1)*((2k-1)*t-3k^2+2k).
- disc_k H_z=-2^4*3^9*z^2*(z-1)^2.
- H(0)=z; H(1)=1-z; H(1/2)=-1/16; H(2/3)=-z/3; H(1/3)=(z-1)/3.

For the chosen ordering, z belongs to {-1,i,-i,1+i,1-i}. All z and z-1 are units outside primes over 2. Thus the normalized parameter schemes are finite etale over Z[i,1/6]. There are four distinct valid parameters for each of the 15 four-subsets: 60 covers. Critical points remain distinct and map degrees do not drop at p.

The verifier checks that all these quartics split into four distinct roots in F_p. It also checks that every fiber over B splits completely with exactly the prescribed multiplicities 1 or 2, that P and Q are coprime, and that each odd set has 2n+4 distinct points. These tests certify that every characteristic-zero normalized cover and every marked simple point has a well-defined distinct reduction at a suitable prime above p. Conversely their parameters and marked simple points lift uniquely by Hensel's lemma.

No unbounded denominator assumption is needed. Work in the strict henselian DVR at p after choosing an embedding of the relevant algebraic coefficients. The only fixed denominators in the normalized cover formulas are supported at 2,3; all further frame denominators are units because the three chosen reduced points are distinct.

## 2. Complete relative-Mobius enumeration over the algebraic closure

Write j for label-matched coincidences and h for label-mismatched coincidences. Then omega=nA+nB-2j-h, with nA=2a+4,nB=2b+4. Every point of S_i outside Omega is a label-matched coincidence, so j>=max(nA,nB)-4.

For (2,3), j>=6 and any fixed five of the eight source odd points contain three label-matched points. For (3,3), j>=6 and any fixed seven of the ten source odd points contain three. Enumerate unordered triples among these initial points, then ordered target triples of matching labels. The initial order is the deterministic order of the finite-field root routine; it is fixed before the search. It determines a consistent ordering of the corresponding characteristic-zero lifts.

All points are F_p-rational. A Mobius transformation carrying one such triple to another has entries in F_p, so this procedure also exhausts candidates over Fbar_p. Frame determinants are nonzero, preventing degeneration of the relative transformation. The script uses integer modular arithmetic, never floating-point coincidence tests.

A characteristic-zero incidence survives reduction. Extra incidences may appear after reduction, but distinct points within either odd set do not collide. Thus omega can only decrease. Consequently every characteristic-zero candidate with omega<=4 appears in the finite-field candidate list.

## 3. Computation

15 degree-two maps, 60 degree-three maps. Candidate occurrences include repeated descriptions of the same Mobius transformation; no claim of distinct curve counts is made.

(2,3): 230688 occurrences. Reduced omega histogram:
10:1152, 12:229536. No omega<=4 hits at all.

(3,3): 3287808 occurrences. Reduced omega histogram:
0:8400, 4:496, 6:832, 10:684, 12:73228, 13:1488, 14:3202680.
All 8896 omega<=4 occurrences satisfy the exact polynomial identity
 q_bar composed M_bar = U_bar composed f_bar
for a target Mobius automorphism U_bar preserving the entire six-point set B. Every identity is verified by composing binary forms and cross-multiplying their coefficients. No numerical fiber-constancy test is used. Unclassified hits: zero.

The 24 target automorphisms of B are independently enumerated in Q(i); their reductions remain distinct and account for the 24 finite-field automorphisms found by triple alignment. Thus every U_bar used above lifts to a genuine U preserving B in characteristic zero.

IMPORTANT: the entire histogram is a histogram in the special fiber, not an asserted exact histogram of characteristic-zero non-coincidences. This distinction is immaterial for exclusion. The low-omega hits in (3,3) do lift as composite pairs by Section 4, and their omega values are unchanged. The raw low-omega counts 8400 and 496 therefore also count the corresponding lifted occurrences for the chosen lifted ordering.

## 4. Why composite reduction cannot hide a birational characteristic-zero pair

Here is the elementary lifting lemma specific to degree three; generic openness of birationality would NOT suffice.

Let f,q be normalized characteristic-zero cubic covers from Section 1. Let M be a relative Mobius transformation defined by a triple of their simple points. Suppose reduction satisfies q_bar composed M_bar=U_bar composed f_bar, with U_bar preserving B. Lift U_bar to the target automorphism U in Q(i).

The map g=U composed f has the same four critical values as q: this follows because critical value subsets of B reduce injectively. Match the first three critical values in q's fixed ordering. There is a unique source Mobius transformation L that places the critical points of g over these values at 0,infinity,1. Both N_q composed g composed L and N_q composed q are consequently in the normal form F_k for the same z. Their reductions are the same normalized map, by the displayed reduced identity. Their parameters are therefore roots of the same H_z with the same residue. Since H_z has simple roots modulo p, Hensel uniqueness gives equality of the parameters and hence
 g composed L=q.

Put T0=L^{-1}. Then q composed T0=U composed f, and T0 reduces to M_bar (the three distinct critical points determine that reduction).

Now use the ORIGINAL three simple points defining M. For such a point x, T0(x) lies over U(f(x)), which belongs to B. Its reduction is M_bar(x_bar), equal to the reduction of the specified target point y. Since B reduces injectively, q(y)=U(f(x)) already in characteristic zero. Both T0(x) and y lie in this same simple fiber and reduce to the same simple point. Hensel uniqueness gives T0(x)=y. This holds for all three defining points, so M=T0.

Therefore q composed M=U composed f in characteristic zero: the pair factors through f and is non-birational. This proves that NONE of the reduced composite hits can originate from a birational characteristic-zero candidate.

Combining Sections 2-4 proves both exclusions, without assuming that birationality survives arbitrary reduction and without replacing a quasi-projective problem by an unjustified projective empty-fiber argument.

## 5. What the suggested resultant/projectivity criteria do and do not say

A resultant zero detects at least one common root, not the prescribed collection of differently labelled simple roots. Multiplicities, common factors, determinant nonvanishing and birationality require extra conditions.

For a genuinely projective closed scheme over the localization of the integers, an empty geometric special fiber excludes a nonempty geometric generic fiber by properness. But this search imposes open conditions (map degree, resultant and Mobius determinant nonzero, birationality). Its projective closure includes degenerate and composite configurations. Simply homogenizing equations does not automatically provide the needed empty proper model. Sections 1-4 explicitly handle these issues.

## 6. Rank-one / weight-one lifts to the k=4 setting

Work over C (or Qbar), K=C(t), original pair primitive so K=C(f1,f2). Suppose only label e changes and Omega has four points. Let
 L=K(rho1,rho2), rho_i^2=f_i,
 F the smooth projective connected curve with function field L.

The two unchanged squareclass equations imply
 (rho1^4-1)/(rho2^4-1) and (rho1^4+1)/(rho2^4+1)
are squares in L. Thus the two marked Kummer conditions for k=4 hold on F. The statement concerns the two characters separately, not just their product.

However, put c_e=|S_{1,e} intersect S_{2,e}|. Then
 GENUS(F)=1+c_e.

Proof: the difference of the two quadratic characters is the nontrivial character D branched over Omega. If [f1],[f2] are independent, L/K has degree four, its branch locus is S_{1,e} union S_{2,e}, of cardinality c_e+4; every inertia group has order two. Riemann-Hurwitz gives 2g(F)-2=-8+2(c_e+4)=2c_e. If the characters span rank one, one must be trivial (they are distinct); consequently c_e=0 and L/K is the double cover branched at four points, again genus one.

Moreover (rho1,rho2) is birational onto its co-image: K=C(f1,f2) is contained in C(rho1,rho2), so the latter field is exactly L. Therefore the normalization of the lifted co-image has positive genus, not genus zero. Its projection degrees are [L:K]*a/2 and [L:K]*b/2. In particular, it is never a graph of a rational map P1->P1.

Consequences for E06/E08: the lift does give their marked k=4 squareclass equations, but does NOT give a Mobius correspondence or a co-image of bidegree (1,b). If c_e>0 it also loses the genus<=1 hypothesis on the common source. Even when c_e=0 the lifted co-image has genus one and both projections have degree at least two, so the cited graph exclusions do not apply. No degree upper bound follows from this lift alone.

The other two changed labels are equivalent by the target automorphisms
 A_b(t)=(t-1)/(t+1), A_a(t)=(t-i)/(t+i),
which preserve B and send the changed pair to {0,infinity}. Modulo squares these permute the three character classes. For instance A_b(t) has class q_b(t), A_b(t)^2-1 has class q_e(t), and A_b(t)^2+1 has class q_a(t). Applying the preceding construction to A_chi composed f_i gives genus 1+|S_{1,chi} intersect S_{2,chi}|, and the same positive-genus obstruction.

E06 and E08 were read from the public repository; their k=4 statements are not being extended beyond their stated hypotheses.

## Reproduce

Use Python 3.12, sympy 1.14.0, python-flint 0.9.0 and a C++17 compiler. From the directory containing exact_w:

    sh exact_w/run_complete.sh

The script reruns the exact cubic enumeration, fixes p=874009 (no prime search required), checks splitting/good reduction and the 24 lifted target automorphisms, compiles and executes the full modular alignment, and asserts expected totals. Assertions must remain enabled. The optional prime-discovery run is python exact_w/modular_search.py without an argument.

The computation certifies the finite-field assertions. The characteristic-zero implication is the mathematical proof in Sections 1,2,4, not a claim that a formal proof assistant verified it.
