# M3-T11-147 — Degree-two and odd-parameter obstruction in the full signed projection

STATUS=PROVED_LOW_PARAMETER_DEGREE_ADAPTER_WITH_BOUNDARY_CLASSIFICATION
AUDIT_MODE=WITHIN_SESSION_ADVERSARIAL_REDERIVATION_NOT_EXTERNAL
GLOBAL_COUNTING_CREDIT=0
PRIMARY_GATE_STATUS=OPEN
TI=PARKED
NEXT=M3-T11-148 DegreeFourFullSignedCurveAllocationOrDirectSupportEstimate

Authority: fresh MAIN / INDEX / RESULT-LEDGER / active ROUTE all146; latest146 card and audit read. Use146's full139 eliminant and degree-preserving unique inverse, with original138 positive endpoint masks retained. T11-120 remains retracted. No full-history reread.

## 1. Historical dedupe and exact scope

The current ledger already records M3-HIST28-GEOMETRY-FW-001: on the earlier blow-up/K3 models with quasi-polarization M, Stage19 physical M-degree4 rational curves and every odd physical M-degree are absent; Stage20 has the Saunderson M-degree6 curve. Stage19 M-degree6 absence is NOT proved. Those historical results remain authority and receive no new credit here. We have NOT identified that M-degree with the parameter degree in the138/139 plus projection. The contribution here is an explicit positivity proof in the146 lift coordinates, its degree-preserving projection receiver, and bounded noncontained-conic occupancy. It is not a claim of a new global low-degree spectrum or of Stage19 M-degree6 absence.

Parameter degree d below means the common degree of a homogeneous basepoint-free map from P1_Q to [A_1:A_2:A_3:R], after removing common factors. It does not mean genus, the earlier M-degree, or the degree of an arbitrary multiply-covered image. Real coefficients suffice for the obstruction. Constant maps are explicitly excluded from the nonconstant conclusion.

## 2. Pass from projection to a basepoint-free signed polynomial lift

Suppose the map is contained in P=0, and the146 open mask R*product(A_i*q_i*K_i) is not identically zero, where q_i=2R^2-A_i^2 and K_i=R^2-A_i^2. By146 over Q(t), there is a unique Y_i in Q(t) with Y_i^2=q_i and sum A_iY_i=-R^2. A rational function whose square is a polynomial is a polynomial (reduce numerator and denominator in the UFD Q[t]). Its degree is at most d. Homogenization gives degree-d forms Y_i; then
 E_i=(A_i+Y_i)/2, F_i=(A_i-Y_i)/2,
 E_i^2+F_i^2=R^2, sum E_i^2=R^2.
These identities hold globally as polynomial identities, including at excluded parameter values. If R,E_i,F_i all vanished at a complex projective parameter, A_i=E_i+F_i would also vanish, contradicting basepoint-freeness of the original map. Thus the lifted forms have no common basepoint. Original positivity, source, packet, content, orientation and canonical masks are still required for endpoints.

## 3. Odd parameter degree is impossible

At a real projective zero of R, sum E_i^2=0 forces every E_i=0; then E_i^2+F_i^2=0 forces every F_i=0. This is a forbidden common basepoint. Therefore R has no real projective zero. A nonzero real homogeneous form of odd degree satisfies R(-s,-t)=-R(s,t); continuity on the real unit circle forces a zero. R identically zero would force all lifted forms zero. Hence every basepoint-free map as above has even parameter degree.

This is a statement about global real/P1_Q parameter maps. It does not exclude all odd-degree algebraic curves, elliptic cubics, positive-genus curves, or isolated rational points on singular curves with nonrational normalization branches. Multiplying forms by a common polynomial does not change the minimal map degree and cannot circumvent the proof.

## 4. Degree two: every nonconstant lift has an identically zero edge

For d=2, R is a definite real quadratic. Change its overall sign if needed and write R=L*bar(L), where L and bar(L) are distinct complex linear forms. For each i,
 (E_i+iF_i)(E_i-iF_i)=L^2*bar(L)^2.
Neither factor is zero; unique factorization and conjugation leave exactly three allocations of the two quadratic factors: (L^2,bar(L)^2), (L*bar(L),L*bar(L)), or the reversed first allocation. In the middle case E_i=a_i R and F_i=b_i R, with a_i^2+b_i^2=1. In either other case, after absorbing the reversed allocation into conjugation,
 E_i=(c_i L^2+bar(c_i)bar(L)^2)/2, |c_i|=1.
Put z=L/bar(L), a nonconstant rational function. For m rotating coordinates, the identity sum E_i^2/R^2=1 becomes the Laurent identity
 m/2 + sum_fixed a_i^2 + (z^2 sum_rot c_i^2 + z^(-2) sum_rot bar(c_i)^2)/4 = 1.
Its coefficients imply sum_rot c_i^2=0 and m/2+sum_fixed a_i^2=1. The cases are exhaustive:
 - m=0: all coordinates proportional to R; the projective image is constant and the quadratic forms share R, so this is not a basepoint-free degree-two map.
 - m=1: c_i^2 cannot vanish, impossible.
 - m=3: the constant coefficient is3/2, impossible.
 - m=2: the sole fixed coordinate has a_k=0, so E_k is identically zero. The two rotating phases have opposite squares, giving the familiar boundary Pythagorean conic.
Therefore a nonconstant degree-two curve cannot have three strictly positive edges at any parameter. Boundary conics do exist: R=s^2+t^2, E=(t^2-s^2,2st,0), F=(2st,s^2-t^2,R). This example also satisfies the original signed plus identities with A=E+F,Y=E-F. It must not be discarded as an algebraic impossibility; positivity excludes it.

## 5. Exact receivers and limitations

A smooth geometrically irreducible Q-conic with a rational point has its degree-two rational parameterization by lines through that point. If such a conic is contained in P=0 and contains an eligible positive rational point, its open mask is generic, so sections2–4 give a contradiction. If it is not contained, pullback P is a nonzero homogeneous degree32 form and has at most32 distinct projective parameter roots. Uniqueness146 gives at most32 eligible endpoints on the conic, including the parameter at infinity. No height cutoff is needed for this occupancy bound.

A reducible conic of two Q-lines has at most32 eligible endpoints by145/146, and a doubled Q-line at most16. A conjugate pair of non-Q lines has at most one Q-point, their intersection: a rational point on one lies on its conjugate too. We do not exclude that isolated intersection as a physical point. These distinctions prevent applying the smooth parameter argument to a nonsplit singular conic.

More generally, a noncontained degree-d basepoint-free P1_Q parameter map has at most16d preimages, hence at most16d eligible endpoints. A contained generically open odd-degree map is impossible. For nonconstant contained P1_Q maps with potentially positive edges, the first remaining parameter degree is4. Quartic maps are NOT excluded. Curves of positive genus, nonsplit normalization issues and the number/cost of curves covering the Stage37 population remain unresolved. None of these occupancy constants establishes a global count or exponent saving.

## 6. Reproducible supporting verification

verify147.py uses exact Fraction arithmetic, 12 rational unit phases, 24 individual circle identities and13,824 triples. The sphere identity survives for216 all-fixed triples and144 two-rotating triples; none with one or three rotating coordinates survive. Every two-rotating solution has its fixed edge zero. It checks196 odd antipodal evaluations and the boundary example's signed plus identities. These are supporting checks; the universal exclusion is the factor-allocation/Laurent-coefficient proof, not the finite grid. There are no new rational perfect-cuboid examples or global counting certificates.

## 7. Handoff

Next148: investigate full signed degree-four basepoint-free polynomial maps, splitting square-free and repeated quadratic factors of R and preserving all positivity/original packet masks; alternatively prove a direct global eligible-support estimate. Do not promote unsigned slice curves, small searches, genus facts, fixed-curve occupancy or an uncosted cover to credit. Do not identify current parameter degree with historical M-degree without a proved comparison. Do not restart parked TI or reopen retracted120. GLOBAL_COUNTING_CREDIT=0, PRIMARY_GATE_STATUS=OPEN.
