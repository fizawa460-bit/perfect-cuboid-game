# M3-T11-146 — Open-mask rational square collapse and explicit unique signed inverse

STATUS=PROVED_FIELD_LEVEL_SIGNED_LIFT_EQUIVALENCE_AND_DEGREE_PRESERVING_CURVE_LIFT
AUDIT_MODE=WITHIN_SESSION_ADVERSARIAL_REDERIVATION_NOT_EXTERNAL
GLOBAL_COUNTING_CREDIT=0
PRIMARY_GATE_STATUS=OPEN
TI=PARKED
NEXT=M3-T11-147 GlobalSignedPolynomialCurveExceptionsOrDirectSupportEstimate

Authority: fresh MAIN / INDEX / RESULT-LEDGER / active ROUTE all145;145 and audit read,139 eliminant and138 original plus coordinates retained. Semantic comparison distinguishes this from134 four-square reduction,145 trace over C(t) for affine lines, and old anti-root/quartic inverses. No previous full139 gradient inverse or arbitrary-field converse was found. No full-history reread. We extend145's trace argument over the BASE FIELD, rather than C(t) alone, and use the complete139 eliminant.

## 1. Define the exact open mask

Over a field K of characteristic0, take R,A_1,A_2,A_3 in K and define
 Z=R^2, q_i=2R^2-A_i^2, Q_i=A_i^2*q_i,
 K_i=R^2-A_i^2,
 D=Z^4+sum Q_i^2-2Z^2*sum Q_i-2sum_(i<j) Q_i*Q_j,
 P=D^2-64Z^2*Q_1*Q_2*Q_3.
Assume the OPEN MASK
 R*product_i(A_i*q_i*K_i)!=0.
This mask contains the original positive rational signed endpoints in the138/139 projection: A_i are nonzero primitive odd plus coordinates; q_i=Y_i^2 cannot vanish rationally when R!=0 because Y_i=0 would give A_i^2=2R^2. Also K_i=-2e_i*f_i!=0 because all positive edges and face hypotenuses are nonzero. No newly discarded physical endpoints are hidden in this mask. Original source/coefficient/orientation/cyclic/content/canonical restrictions are still required for the Stage37 population.

## 2. P=0 forces ALL three q_i to be squares in K

By139 P is the product of eight factors R^2+sum epsilon_i*A_i*sqrt(q_i). If P=0 in K, one factor vanishes in the multiquadratic FIELD extension L=K(sqrt(q_1),sqrt(q_2),sqrt(q_3)). Absorb its signs into Y_i. Then
 Y_i^2=q_i, sum A_iY_i=-R^2.
For a nonsquare q_i, a sign-changing K-automorphism of L exists, so the normalized trace of Y_i is0. A square q_i has Y_i in K. The trace of the displayed sum therefore forces at least one square q_i.
If exactly TWO q_i are squares, the remaining nonzero A_iY_i would have to belong to K, contradicting nonsquareness. If exactly ONE, say q_k, is square, trace gives A_kY_k=-R^2, hence
 A_k^2*(2R^2-A_k^2)=R^4,
 (A_k^2-R^2)^2=0,
 contradicting K_k!=0. ZERO squares contradicts trace directly. Thus ALL THREE are squares IN THE BASE FIELD K.
Dependencies among the squareclasses do not affect this argument; no independence hypothesis is used. Conversely any signed lift with the stated sum gives P=0 by the exact norm identity. Therefore on the open mask P=0 is equivalent to the EXISTENCE of a signed K-lift. Over Q this supplies all rational square tests; over Q(t) it supplies global rational-function square tests. It does not remove positivity or the original packet masks.

## 3. There is exactly ONE signed lift on the open mask

Suppose two sign branches vanish. Subtracting their sums shows a nonempty subset of the three nonzero terms U_i=A_iY_i has sum0. A one-term subset is impossible by the mask; all three would contradict sum U_i=-R^2!=0. If two terms cancel, the remaining term equals -R^2 and the same square calculation forces its K_i=0. Thus two branches cannot vanish. All Y_i are nonzero, so this proves uniqueness of the signed tuple, including over algebraic closure.
In particular each original eligible (A,R) pair reconstructs at most ONE ordered positive edge triple and at most one canonical endpoint. The old at-most8 sign bound was safe but loose.145's per-line endpoint bound improves from128 to16 on this mask; projection occupancy16 itself is unchanged. This is a constant improvement, NOT an exponent or global credit.

## 4. Polynomial-gradient formula recovers the lift without choosing square roots

Let g_i=partial P/partial A_i, with R and the other A_j held fixed. On the unique vanishing branch put C=product of the seven OTHER signed factors. Then C!=0 and differentiating the exact product gives
 g_i=C*(Y_i-A_i^2/Y_i)=2C*K_i/Y_i.
Thus every g_i is nonzero on the open mask P=0. Define
 h=sum_i A_i*K_i*g_j*g_k, where {i,j,k}={1,2,3},
 N_i=-R^2*K_i*g_j*g_k.
Using sum A_iY_i=-R^2 gives
 h=-4*C^2*R^2*K_1*K_2*K_3/(Y_1*Y_2*Y_3)!=0,
 Y_i=N_i/h.
All expressions N_i,h are polynomials in the original A,R with rational coefficients. The ratio is homogeneous of degree1, so the original scaling and exact R are preserved. It is an explicit rational inverse on the stated open; no irreducibility claim for the whole P surface or unspecified normalization is needed. The nonzero gradients also show this open of the eliminant is smooth.

For implementation one can compute
 dQ_i/dA_i=4A_iK_i,
 dD/dQ_i=2Q_i-2Z^2-2sum_(j!=i) Q_j,
 g_i=4A_iK_i*[2D*(dD/dQ_i)-64Z^2*product_(j!=i) Q_j].
Then evaluate h and N_i exactly. Do not replace the denominator h by an approximate nonzero test.

For integer A,R on this open, q_i are integers and their rational square roots Y_i are necessarily integers (a reduced rational denominator cannot square to an integer). If the retained odd-A mask holds, Y_i are odd and e_i=(A_i+Y_i)/2,f_i=(A_i-Y_i)/2 are integers. Their exact identities are
 e_i^2+f_i^2=R^2,
 sum e_i^2=R^2,
 f_i^2=e_j^2+e_k^2.
Positivity of the e_i and the original canonical/packet filters remain essential. Primitive A implies primitive edges: a common edge divisor divides integer R, then all f_i, then all A_i. This does not certify an original T11 source packet from P alone.

## 5. Consequence for nonlinear contained curves

Let R(t),A_i(t) be rational polynomials of degree<=d representing a rational parameter curve, with no common projective base factor. If P(t) is NOT identically0, degree(P(t))<=16d gives at most16d parameter values, with the homogeneous formulation counting infinity as well. This is only an intersection bound, not a global cover count.
If P(t)=0 identically and the open mask holds GENERICALLY, apply section2 with K=Q(t): all q_i are squares in Q(t), and the UNIQUE signed tuple Y_i is in Q(t). Since q_i are polynomials, their rational-function square roots have no finite denominator (UFD valuation argument); hence Y_i are polynomials of degree<=d. Homogenizing gives a degree-preserving signed lift of the parameter map. There are no hidden constant twists requiring later arithmetic root selection. The gradient inverse supplies the same tuple.

Thus a nonlinear rational curve generically meeting the physical open cannot be certified by the eliminant alone and then treated as a weaker moving-square enlargement: it ALREADY carries a global signed polynomial lift. Classifying low-degree contained curves must solve those global identities, not merely test local leading characters or CRT squares.
If some K_i is identically0, the positive real signed population is empty by145's sum e_i^2=R^2 argument. If R or A_i is identically0, the original physical mask is empty. q_i identically0 is impossible over Q(t) when R!=0. Isolated failures of the mask do not add positive rational physical endpoints by the same rational/positivity checks. No assertion that nonboundary nonlinear rational curves do not exist is made. No genus, finite rational-point classification, or curve-count exponent is proved.

## 6. Current counting receiver after the collapse

For the original retained canonical chart, the physical image is counted by primitive integer (A,R) in the original exact height window R<=B, satisfying P=0, the open mask, and positivity/original packet masks applied to the UNIQUE inverse above. The separate square tests are redundant after imposing the FULL eliminant on this open. This is not a new independent sieve condition.
At-most8 fixed-pair sign multiplicity and145's128-per-line bound are sharpened; they cannot generate a fixed power saving. Ambient integer hypersurface counting is not automatically the physical A_1,1 support estimate. A low-degree curve cover must retain actual realized support and separately control the number and heights of the curves. The primary B^(1/3-eta) gate remains unproved.

## Verification and within-session audit

Exact replay:198 real algebraic signed lifts generated from integer sphere coordinates;594 gradient-inverse coordinate identities Y_i*h=N_i;198 unique-branch checks. The face witnesses in these samples are algebraic square roots, and at least one is nonrational in EVERY sample. They are NOT rational/integer perfect cuboids or positive physical endpoints. The quotient algebra of three square roots checks polynomial identities exactly, including dependencies, without floating roots.
Small rational integer projection census:22261 positive A/R candidates,293 P-zero points,all293 on A_i^2=R^2 boundary;0 off-boundary hits. This census does not prove global emptiness. Its scope is explicit; the infinite field theorem is the trace/uniqueness/gradient proof, not the finite scan. Physical endpoints enumerated0.
Within-session adversarial audit checked the BASE-field trace, dependent squareclasses, all three alternative square counts, nonzero q/A/R/K masks, uniqueness subset cases, differentiation constants, gradient and h nonvanishing, homogeneous scaling, integer root/parity/primitive-edge inference, polynomial-root denominator removal, and empty boundary charts. No external audit.

## Handoff

147: use the unique inverse/full signed polynomial lift to study actual nonlinear exceptional curves or a direct integer support estimate on P with original masks. A degree2 parameter curve on the nonboundary open must lift with all seven coordinates of degree<=2; that is a concrete low-degree exception classification problem, NOT a proved exclusion. Alternatively seek a global noncircular support theorem on the eliminant. Do not repeat line/Pell occupancy, multiply rational square conditions that are now automatic, or infer global scarcity from inverse uniqueness.145 projected-line16,144 unsigned logarithmic bounds,143 unsigned firewall,142 bare-cover OmegaB,141 necessity,140 properness,139 norm/eliminant,138 physical height,120 retraction and TI parking retained. GLOBAL_COUNTING_CREDIT=0; all closure/limit/nonexistence flags remain false.
