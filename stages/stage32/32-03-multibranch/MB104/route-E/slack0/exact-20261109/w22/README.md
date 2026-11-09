# Exact partial certificate for Problem W, slack zero

Date: 2026-11-09. Scope: (2,2) completely checked; degree-3 cover enumeration completely checked; (2,3) and (3,3) pair searches NOT performed. Do not promote the latter exclusions to theorems.

## Run

Python 3.12, sympy 1.14.0, python-flint 0.9.0.

    python -m pip install sympy==1.14.0 python-flint==0.9.0
    python w22.py --no-sieve
    python degree3_enumeration.py

Run without Python -O: assertions are part of this verifier.
No floating-point equality decisions are used. The wall-clock timings are not mathematical input.

## Degree two: completeness and arithmetic

A degree-two slack-zero map has two distinct branch values in B={0,infinity,1,-1,i,-i}, hence 15 source-isomorphism classes. The octahedral group of the six-point set has 24 elements, generated here by exact three-point alignment and checked by its action on all six points. Its orbits on pairs are the three opposite pairs and twelve adjacent pairs.

Representatives are target-automorphism postcompositions of q0(t)=t^2 and q1(t)=t^2/(t^2+1). Their deck involutions are both t -> -t. We select one representative for each of the 15 branch pairs. The odd-point sets of each shape have eight distinct points; the script verifies their images and labels exactly.

All points lie in K=Q(sqrt(2),sqrt(-1+i)), a degree-eight field. The primitive element sqrt(2)+sqrt(-1+i) has minimal polynomial x^8-4*x^6+24*x^4-8*x^2+100. Arithmetic is exact rational polynomial arithmetic modulo this polynomial.

Let j be the number of label-matched coincidences and h the label-mismatched coincidences. Then omega=16-2*j-h. If omega<=4, h<=omega implies j>=4, hence a label-matched triple exists. Enumerating all unordered triples in the first odd-point set and ordered label-matching triples in the second set is complete. Counts are occurrences, NOT distinct Mobius transformations or curve classes. We reuse the same exact calculation across the two geometric shapes where appropriate.

Every Mobius matrix is constructed projectively with adjugates (no numerical solve). Every pairwise determinant is evaluated exactly in K in --no-sieve mode. Non-birationality for two degree-two maps is equivalent to equality of their deck involutions; with these representatives this is equivalent to the relative Mobius matrix being diagonal or antidiagonal. The test is exact.

Results:
- 15 covers, shapes 3+12.
- 157824 label-matched triple occurrences.
- 12912 geometric shape/triple jobs (reused across representative pairs).
- 826368 field equality decisions in --no-sieve mode.
- Raw omega histogram: 0:6720, 4:576, 6:768, 7:1536, 8:25344, 10:122880.
- All 7296 raw hits with omega<=4 are non-birational.
- Birational hits: zero. The source is P1 throughout, so gamma=0.

Optional default mode uses a homomorphism K -> F_10009 (primitive element maps to 2597) ONLY to prove determinants nonzero. Possible equalities are still checked in K. Distinctness of reduced odd points is asserted. --no-sieve disables all such pruning; the reduction setup remains a diagnostic and has no effect on equality decisions. Both modes returned identical histograms.

The E11 source uses different representatives and prunes to an initial subset of source points in its smaller search. Its raw multiplicity counts should not be compared directly with these full-triple counts.

## Degree three: exact enumeration, not pair exclusion

Order each four-element subset of B and let N send its first three values to 0,infinity,1. Let z be the image of the fourth. Normalize the corresponding critical points to 0,infinity,1. Every cover has the unique form N^{-1} composed with

    F_k(t)=t^2*((2*k-1)*t+2-3*k)/(t-k).

The fourth critical point is c=k*(3*k-2)/(2*k-1), and its value is k*(3*k-2)^3/(2*k-1). Therefore

    H_z(k)=k*(3*k-2)^3-z*(2*k-1)=0.

The numerator/denominator resultant is -2*k^2*(k-1)^2. The derivative numerator is 2*t*(t-1)*((2*k-1)*t-3*k^2+2*k). Infinity has index two since the numerator has degree three and denominator degree one.

For all 15 four-subsets, the verifier checks over Q(i) that H has degree four, gcd(H,H')=1, and gcd(H,k*(k-1)*(2*k-1)*(3*k-2)*(3*k-1))=1. These checks rule out degree loss, colliding critical points, and zero resultant. Thus each of four roots gives one genuine cover, and uniqueness of the three-critical-point normalization shows there is no source-isomorphism duplication. Total 60.

Each map is defined over Q(i,k), of degree at most four over Q(i). Odd-point splitting fields have NOT been constructed. No (2,3) or (3,3) Mobius alignment was run. Their counts and omega distributions are unknown in this certificate.

## Theory notes

1. Four-point normalization does not bound absolute field degree. For j=256*(1-lambda+lambda^2)^3/(lambda^2*(1-lambda)^2), [Q(lambda):Q(j)]<=6, but Q(j) is not bounded by this identity. Six cross-ratio values means six orderings of the SAME unordered configuration, not at most six absolute Galois conjugates of an arbitrary configuration. Descending a cover pair to Q(i,lambda) requires a separate fiberwise Galois invariance and descent argument.

2. Over a common coefficient field K containing i, A=S1 intersect S2 is Galois invariant. If both S_i are transitive Gal(Kbar/K)-sets and A is nonempty, then S1=S2. More generally, A must be a union of full orbits on both sides. This gives an exact factorization sieve, not a universal theorem about those orbits. Enlarging to a common coefficient field may split orbits.

3. Rank-one squareclass classification. Write R_chi=q_chi(f1)/q_chi(f2), with q_e=x, q_b=x^2-1, q_a=x^2+1. If their span has rank one, [R_chi]=w_chi[D] for a nonzero w in F2^3. At each exceptional point the parity difference vector is exactly w. Each leg contributes either 0 or a standard basis vector. Therefore weight(w) is one or two, never three.
- Weight one: only one label can change; the other two label sets agree exactly, Omega=S1 symmetric_difference S2, and m=4.
- Weight two: at every exceptional point both legs are odd but their labels are exchanged between the same two labels. Hence S1=S2. This case is in the equal-support class; no new degree bound is established here for that class.
In particular, rank-one with unequal supports reduces to precisely THREE choices of affected label, with one nontrivial ratio squareclass and two trivial ratios. No degree bound for these three cases is proved here.

## Source inspected

GitHub perfect-cuboid-game, stages/stage32/32-03-multibranch/MB104/route-E/E11-SLACK0-BOLZA-ETALE-AND-BIDEGREE-22.md, blob SHA 6120770fad2c9f24941ca97a0d4668c0fe6d9ca4; and slack0/e11_slack0_small.py, blob SHA 11130601dd20e2f722de0ca216f7f937dbb3c00c. The original source and research ledgers were not modified. Original numerical exclusion is not used as proof.
