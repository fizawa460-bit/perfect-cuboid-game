# M3-T11-139 — Exact integer degree-eight cover and squared-diagonal Heron divisor receiver

STATUS=PROVED_EXACT_INTEGER_COVER_AND_HERON_DIVISIBILITY
AUDIT_MODE=WITHIN_SESSION_ADVERSARIAL_REDERIVATION_NOT_EXTERNAL
GLOBAL_COUNTING_CREDIT=0
PRIMARY_GATE_STATUS=OPEN
TI=PARKED
NEXT=M3-T11-140 JointHeronSquareDivisorPhysicalProjectiveSupport

## Current authority and scope
MAIN/INDEX/RESULT-LEDGER/active ROUTE current138, standalone138, targeted134 signed inverse and fresh denominator router are the current sources. Targeted Heron/projective text lookup in ROUTE found no earlier integer Heron receiver; bare signed-circle equations and eliminant remain133/134/138, not new underlying identities. No full-history reread. Keep exact primitive physical R, canonical ordered/sign-witnessed endpoints and every original content/coefficient/parity/orientation/cyclic mask. Fresh assertions retain134/137 odd split finite nonzero-u original-packet scope.120 physical adapter stays retracted.

## 1. Monic integer cover in Z=R^2
Use138's primitive integer plus vector A_i=e_i+f_i. Introduce integer minus vector B_i=e_i-f_i (NOT the historical anti-root denominators B_i; in this card call these Bminus_i).
Set Z=R^2 and
 Q_i=A_i^2(2Z-A_i^2),
 D_A(Z)=Z^4+sum Q_i^2-2Z^2 sum Q_i-2sum_(i<j)Q_i Q_j,
 P_A(Z)=D_A(Z)^2-64Z^2 Q_1 Q_2 Q_3.
Then P_A is an integer MONIC polynomial of degree8 in Z for every fixed nonzero integer A. This is the homogeneous form of138's scale polynomial: with r=(A_1/A_3,A_2/A_3,1), K=A_3^2/Z, H_r(K)=P_A(Z)/Z^8. Its leading monic coefficient cannot specialize away even if the degree in K drops.

Define four integer quadratic forms
 F_0=A_1^2+A_2^2+A_3^2,
 F_i=F_0-2A_i^2 (i=1,2,3),
 C_A=sum A_i^8-2sum_(i<j)A_i^4 A_j^4=-F_0 F_1 F_2 F_3.
Then D_A(0)=C_A and P_A(0)=C_A^2.

## 2. Stronger integer divisor necessity from the physical signed lift
Actual minus coordinates satisfy
 A_i^2+Bminus_i^2=2Z, sum A_i Bminus_i=-Z.
Consequently Q_i=(A_i Bminus_i)^2. The signed-sphere eliminant before squaring gives the exact sign
 D_A(Z)=-8Z product_i(A_i Bminus_i).
Indeed delta_i=A_i Bminus_i/Z has sum delta_i=-1; the radical-free bracket equals -8product delta_i, obtained by squaring that signed-sum relation twice. Thus Z divides D_A(Z). Since D_A(Z)=C_A modulo Z,
 R^2 divides C_A=-F_0 F_1 F_2 F_3.
Merely applying the rational-root theorem to P_A would only give R^2|C_A^2; the signed lift is needed for the stronger R^2|C_A.

When C_A is nonzero, every physical R is among the positive integers whose square divides |C_A|, followed by the exact P_A and physical lift tests. Since |C_A|<=24H_+^8, the divisor list is H_+^o(1);138 already gives the sharper at-most8 physical fibers. This does not count moving A and gives no new power saving.

Do not discard C_A=0. F_0>0, so this is one of the three quadratic carriers F_i=0. Then the square-divisor list is not finite and cannot serve as a generic enumeration step. P_A is still monic degree8, so138's physical fiber bound survives. Example A=(3,4,5) has C_A=0 but P_A(1)!=0: a vanishing factor alone is not a lift.

## 3. Exact signed integer reconstruction, retaining all masks
For a primitive odd nonzero A and a positive integer R, a physical signed lift is exactly a choice of integers Bminus_i such that
 Bminus_i^2=2R^2-A_i^2, sum A_i Bminus_i=-R^2,
 e_i=(A_i+Bminus_i)/2>0, f_i=(A_i-Bminus_i)/2.
A candidate also requires all original Stage37 packet and canonical-witness masks.

Proof of the elementary cuboid direction assertion: the square equations imply e_i^2+f_i^2=R^2; the signed sum gives sum e_i^2=R^2. Odd A forces R odd whenever these integer square equations hold (if R even, the right side for Bminus_i^2 is7 mod8), and Bminus_i odd, so e_i,f_i are integers. Positivity then supplies the three opposite-face diagonals. The endpoint is primitive automatically: a prime dividing every e_i divides R by the sphere equation, then every f_i by its circle equation, hence every A_i, contradicting gcd(A)=1.
Conversely an actual primitive endpoint with its chosen signed f gives these identities. The overall projective sign must be chosen to match positive edges; independently flipping A coordinates changes the projective point.

P_A(R^2)=0 and R^2|C_A are necessary, not sufficient. Check integer minus squares, actual signed sum, positive edges, and original packet masks explicitly. On134's open mask at most one positive ordered direction comes from each Z, hence at most8 endpoints per plus point, as138. Boundary samples below are not counted as endpoints.

## 4. Fresh square allocation into three quadratic forms — exact but dependent
Let p^lambda||m_i be an original odd split fresh relative prime, with v_p(R)=lambda and p outside all frozen contents. Write actual normalized anti-roots v_i and S as134/137. Directly from A_j^2=R^2(1+d_j),
 F_0/R^2=3+S, F_j/R^2=1+v_j.
At the target, v_i is a unit and v_i=u modp^(2lambda), with u^2=-1 modp^(2lambda). Since p is odd, 1+u is a unit (u=-1 modp would force2=0). Therefore
 v_p(F_i)=2lambda,
 v_p(F_0)=v_p(F_j)=0 for j!=i,
using v_p(S)=v_p(v_j)=-2lambda at the other two roots.
Hence if M_rel=m_1 m_2 m_3,
 m_i^2|F_i, zeta_i=F_i/m_i^2 is an integer, gcd(zeta_i,M_rel)=1,
 gcd(F_0,M_rel)=1.
If M_rel>1, all four F factors are nonzero: at any fresh prime all factors have the just-proved finite valuations. Thus C_A=0 forces M_rel=1 in this original fresh scope. Relative-fresh-empty packets must remain a separate branch.

For R<=B, |F_i|<=4R^2 and F_0<=6R^2, giving
 0<|zeta_i|<=4(B/m_i)^2 when M_rel>1.
Combining the global squared-diagonal divisor with this disjoint fresh allocation yields
 (R/M_rel)^2 | F_0 zeta_1 zeta_2 zeta_3.
Here R/M_rel is an integer but must not be replaced by a frozen packet constant; content and all-same/core support are retained.

NOVELTY FIREWALL: the fresh form allocation is a dependent integral pullback of the old actual unit/pole root-line, not a new character or probability restriction. From F_i/R^2=1+v_i its exact meaning is visible. Pairwise-coprime fresh factors do not authorize independent densities or multiplication of consumed savings. The new usable representation is the global monic integer equation, stronger signed-lift divisor, and exact candidate/lift interface on the physical height scale.

## Verification and audit
Python PASS:2000 generic integer/homogeneous identities;1488 signed primitive zero-edge Pythagorean boundary lifts;77 bounded p^2 abstract unique-factor samples;1 zero-Heron false-converse check. Boundary samples are not positive endpoints. Fresh samples test only the algebraic at-most-one factor hit for p-unit A, not full physical,137 witness, or all packet reconstruction.
Symbolic output {8,1,0,0}: monic degree8, coefficient1, Heron constant identity zero, constant-square identity zero.
Within-session audit rederived the sign before squaring and R^2 divisor, distinguished the weaker rational-root claim, retained the zero-Heron branch, proved reconstruction parity/primitivity, and identified fresh allocation as old root-line pullback. No positive physical endpoint was found or enumerated. This is not external auditing.

## Handoff
M3-T11-140: seek a nonlocal bound for the realized primitive plus support through the joint integer equation, signed minus-square lift, and quadratic square-divisor allocation with exact R<=B. Treat C_A=0 / M_rel=1 separately rather than dividing by zero or assuming fresh support. A count of divisor choices for fixed A is already consumed by138's bounded fiber. Moving A, contents and R/M_rel still require a uniform theorem. Do not count all ambient triples as physical or recycle leading-character/CRT screens. Existing primary and hard one-twelfth budgets unchanged; support power bound unproved; global credit0, gateOPEN, TI parked.

