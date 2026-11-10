# M3-T11-149 — Two-pair obstruction in all degrees; square-free sextic phase receiver

STATUS=PROVED_ALL_DEGREE_TWO_CONJUGATE_PAIR_OBSTRUCTION_AND_EXACT_SEXTIC_RECEIVER
AUDIT_MODE=WITHIN_SESSION_REDERIVATION_AND_EXACT_CHECKS_NOT_EXTERNAL
GLOBAL_COUNTING_CREDIT=0
PRIMARY_GATE_STATUS=OPEN
TI=PARKED
NEXT=M3-T11-150 SquareFreeDegreeSixPhaseCompatibilityOrDirectSupportEstimate

Authority: fresh MAIN / INDEX / RESULT-LEDGER / active ROUTE all148; latest148 standalone research-card and audit read.146 unique degree-preserving lift and147 no-real-zero lemma are retained.148 already excludes one-pair powers in all degrees and the simple two-pair quartic. This card handles arbitrary two-pair multiplicities and gives a concrete receiver for the remaining degree6 case. Do not reread the known history from the beginning.

## 1. Scope, dedupe and result

Use the common degree d of a homogeneous basepoint-free P1_Q parameter map in the138/139 plus projection, with common factors removed. A contained generically open map has, by146, real/rational forms E_i,F_i,R of that same degree satisfying
 E_i^2+F_i^2=R^2, sum E_i^2=R^2.
Their common basepoints are absent. A real zero of R is impossible by147. Original positivity/source/packet/coefficient/orientation/cyclic/content/canonical conditions remain necessary.

We prove that if the complex roots of R occupy at most TWO distinct conjugate pairs, EVERY nonconstant basepoint-free signed lift has an identically zero edge, for arbitrary multiplicities and arbitrary degree. The one-pair case was already148; the new part is two pairs when at least one multiplicity>=2. Together with148's simple two-pair quartic, this excludes the entire two-pair class.

Consequently any nonconstant potentially all-positive contained degree6 P1_Q map must have square-free R with THREE distinct conjugate root pairs. This remaining class is OPEN; existence and nonexistence are not proved. Historical Stage19 M4/odd-M absence and Stage20 Saunderson M6 remain as recorded in M3-HIST28-GEOMETRY-FW-001. No comparison with the current parameter degree or Stage19 M6 absence is claimed. No global counting credit is added.

## 2. Elementary sparse-power zero-multiplicity lemma

Let S(w)=sum_(j=1)^r d_j*w^(ell_j), with nonzero d_j, distinct integer ell_j, r<=3. At any finite w_0!=0, a nonzero S has zero multiplicity at most r-1. Indeed vanishing to order>=r implies its first r Euler derivatives (w*d/dw)^h, h=0..r-1, vanish. Their coefficient matrix is (ell_j^h*w_0^(ell_j)). Its determinant is product w_0^(ell_j) times the nonzero Vandermonde product_(i<j)(ell_j-ell_i). This forces every d_j=0, a contradiction. Negative exponents are allowed because w_0 is nonzero. Equal exponents are grouped first; cancellations can reduce the number of terms or make S identically zero. This is a universal lemma, not a finite exponent search.

## 3. Exhaustive two-pair factor allocations

Suppose R=Q_1^n*Q_2^m up to a real scalar, with distinct definite quadratics, n,m>=1. Use148's real projective normalization, valid also with multiplicities, to write
 R=(L*bar(L))^n*(M*bar(M))^m,
 z=L/bar(L), w=M/bar(M).
Every H_i=E_i+iF_i has
 H_i/R=c_i*z^(a_i)*w^(b_i),
 |c_i|=1, -n<=a_i<=n, -m<=b_i<=m.
This follows exactly from unique factorization of H_i*bar(H_i)=R^2 and conjugation, not a chosen family. If |a_i|<n for all three coordinates, each H_i and bar(H_i), hence all E_i,F_i and R, is divisible by Q_1. This contradicts basepoint-freeness. Thus at least one |a_i|=n.

When one multiplicity is>=2, choose that pair as Q_1, so n>=2. Independently conjugate H_i if needed to arrange a_i>=0; this changes F_i's sign but leaves E_i and every squared identity unchanged. We use this only for the proof, not to relax original signed masks. Let t_0 be the simple pole of z. Since the two root pairs are distinct, w(t_0) is finite and nonzero and w is unramified there. Write r for the number of coordinates with a_i=n, so r=1,2 or3.

## 4. Pole order forces a boundary edge

The sphere identity is
 sum_i [c_i^2*z^(2a_i)*w^(2b_i) + bar(c_i)^2*z^(-2a_i)*w^(-2b_i)] +2=0.

If r=1, its sole leading term has a pole of order2n at t_0 with a nonzero coefficient. All other terms have pole order at most2n-2, or are regular. Cancellation is impossible.

If r=2, factor their pole part as z^(2n)*S(w), where S has at most two powers. Every other term has pole order<=2n-2. Thus S must vanish to order>=2 at w(t_0). Section2 forces S identically zero. Since the two coefficients are nonzero, their exponents must coincide, b_1=b_2, and c_1^2+c_2^2=0. Their conjugate terms cancel identically as well. Therefore E_1^2+E_2^2=R^2, and the original sphere identity forces E_3^2=0: E_3 is identically zero. Relabeling coordinates is harmless.

If r=3, all three positive-pole terms are z^(2n)*S(w), with at most three distinct powers after grouping. The reflected terms are regular (indeed vanish) at t_0, so S must have zero multiplicity>=2n>=4. Section2 permits at most2 for a nonzero S. Hence S is identically zero. Its reflected conjugate sum also vanishes identically, leaving the impossible constant identity2=0.

The cases are exhaustive. Thus arbitrary two-pair multiplicities with at least one>=2 force a zero edge. The remaining n=m=1 case is exactly148 and already has the same conclusion. This establishes the all-degree two-pair obstruction. Legitimate zero-edge boundary maps are preserved; constant maps are also not excluded as perfect-cuboid candidates. The theorem concerns nonconstant maps with no common factor/basepoint.

## 5. Remaining square-free degree6: finite allocation and exact phase receiver

For degree6, the other partitions of root multiplicity are3 and2+1, already excluded by148 and sections3–4. The only remaining possibility is1+1+1. Normalize two upper roots to i,ki with k>0,k!=1 and write the third as u+iv with v>0, distinct from the first two. Then
 R=(t^2+1)(t^2+k^2)((t-u)^2+v^2).
Let alpha=(i,ki,u+iv). For a=(a_1,a_2,a_3) in {-1,0,1}^3 define
 H_a=product_j (t-alpha_j)^(1+a_j)*(t-bar(alpha_j))^(1-a_j), C_a=H_a^2.
There are exactly27 allocations, H_a*bar(H_a)=R^2 and C_-a=bar(C_a), degree12. Every coordinate H_i=c_i H_(a_i), |c_i|=1.

At each root pair j, zero active allocations (all a_ij=0) would make all forms divisible by Q_j. Exactly one active allocation gives an uncancellable order2 pole in the sphere identity, after orienting that coordinate toward the pole. Therefore each column of the3x3 allocation matrix has at least TWO nonzero entries. There are20 possible signed columns, hence20^3=8000 ordered allocation matrices satisfying this necessary local condition, versus27^3=19683 unrestricted ordered triples. This is a finite algebraic pattern reduction, NOT a count of Stage37 endpoints or a proof all8000 survive.

For a fixed allowed allocation triple and fixed real root parameters, write lambda_i=c_i^2=x_i+i*y_i. The FULL signed sphere identity is exactly the following13 real linear coefficient equations plus three unit-circle constraints:
 sum_i [x_i*Re(C_(a_i)) - y_i*Im(C_(a_i))] + R^2 =0,
 x_i^2+y_i^2=1, i=1,2,3.
Equate coefficients of t^h for h=0..12; homogenization includes infinity. Thus a13x6 real linear system with right-hand side -coeff(R^2), intersected with three unit circles, is an exact REAL-lift receiver. Every unit lambda_i has a unit square root c_i, which reconstructs E_i=Re(c_i H_(a_i)), F_i=Im(c_i H_(a_i)); conversely every real polynomial lift gives this system. Basepoint-freeness still must hold, and original endpoint positivity/masks must be checked separately. In the square-free setting the >=2-active condition already guarantees no common signed basepoint at roots of R; elsewhere R is nonzero. This does NOT prove rationality of the reconstructed coefficients: Q descent is a separate unresolved requirement, especially when roots are not individually defined over Q(i).

This receiver accounts for the dependence of all phase functions on one parameter; it never treats three phases as independent Laurent variables. It replaces an unsigned slice or genus observation by the exact original full signed equations.

## 6. Why148's circuit shortcut does not transfer

In degree4, nine squared allocations had a rank8 one-dimensional relation, necessarily involving all eight nonconstant modes. For degree6 there are27 squared allocations in a13-dimensional polynomial coefficient space, so the full relation space always has dimension AT LEAST14. A one-dimensional all-mode circuit is impossible. Exact examples with roots (i,2i,1+i) and (i,3i,2+i) both have rank13 and relation dimension14. These are fixed-root examples, not a universal rank formula or an exclusion theorem. A relation supported on at most six allocation modes plus the center must now be checked using the13x6 receiver and its phase norms; the quartic sparse-support argument cannot simply be repeated.

## 7. Counting scope and verification

A noncontained basepoint-free degree6 Q parameter map has a nonzero degree96 homogeneous pullback of P, hence at most96 projective parameter roots and at most96 eligible endpoints by146's unique inverse. This is occupancy per map, not a global curve-cover bound. A contained generically open degree6 map must have square-free three-pair R; this class is not closed. Positive-genus curves, nonsplit normalization, isolated singular rational points and constant perfect cuboids remain outside the exclusion. No global power saving or nonexistence credit follows.

verify149.py is self-contained standard Python with exact Fraction/Gaussian arithmetic. It checks377 sparse-power Vandermonde determinants,8000 local allocation patterns,54 circle factor identities,162 phase-receiver coefficient identities, four valid two-pair boundary maps with multiplicities (2,1),(3,1),(2,2),(4,3), and rank13 for the two stated sample27-column matrices. The universal theorem is the pole-order/sparse-power proof; finite exponent checks and sample ranks are supporting verification only. Audit is within-session, not external.

## 8. Handoff

Next150: solve or universally obstruct the square-free degree6 allocation/phase system, preserving Q descent and positivity; alternatively prove a direct global eligible-support estimate. Current concrete blocker: uniform compatibility of the13x6 system with three phase unit circles as (k,u,v) and8000 allowed allocation patterns vary, followed by rational descent/original masks. Do not claim a fixed-root rank check solves the uniform problem. One/two-pair classes are now excluded in all degrees and should not be re-enumerated as new credit. Do not identify current parameter degree with historical M-degree or assert Stage19 M6 absence. TI stays parked,120 stays retracted, credit0, gate OPEN. Persist card/audit/replay and all four current controls with readback.
