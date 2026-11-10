# M3-T11-138 — Primitive physical half-angle projective height and degree-eight inverse

STATUS=PROVED_PHYSICAL_PROJECTIVE_HEIGHT_AND_UNIFORM_EIGHT_FIBER
AUDIT=WITHIN_SESSION_ADVERSARIAL_REDERIVATION_PASS_NOT_EXTERNAL
GLOBAL_COUNTING_CREDIT=0
PRIMARY_GATE=M3-T11-GATE-001 OPEN
TI=PARKED
NEXT=M3-T11-139 PrimitiveHalfAngleProjectiveDegreeEightExactRSupport

## Authority and scope
Continue MAIN/INDEX/RESULT-LEDGER/active ROUTE current137, latest137 card, and targeted133/134 inverse/height and older Fricke discussion. No full-history reread. T11 remains primary; TI remains parked. Work on actual primitive integer positive cuboid edges e_i, space diagonal R, signed opposite-face diagonals f_i, e_i^2+f_i^2=R^2, sum e_i^2=R^2, gcd(e_1,e_2,e_3)=1. Preserve canonical orientation, original content/coefficient/cyclic/parity packet masks, exact physical R, one endpoint one count. The at-most-eight inverse uses134 finite nonzero-u nondegenerate open mask. No quartic-theta/physical-antiroot identification;120 physical adapter remains retracted.

## 1. Primitive global plus vector, with no projection content loss
Put x_i=e_i/R, y_i=f_i/R, d_i=2x_i y_i, S=sum d_i, v_i=S-2d_i. Define A_i=e_i+f_i and w_i=x_i+y_i=A_i/R, so w_i^2=1+d_i.

R is odd: if R were even, sum e_i^2=0 mod4 forces all three edges even. Each e_i,f_i has opposite parity, hence A_i is odd. Also A_i is nonzero: e_i=-f_i would give R^2=2e_i^2, impossible for nonzero integers.

The integer triple A is primitive. If an odd prime p divided all A_i, then f_i=-e_i modp, so 2e_i^2=R^2 for each i. Summing gives 2R^2=3R^2 modp, forcing p|R and then p|all e_i, a contradiction. The prime2 cannot divide A. Consequently gcd(A_1,A_2,A_3)=1: the projective representative has no moving common divisor. In addition gcd(A_i,R)=h_i=gcd(e_i,R): after dividing by h_i, the primitive circle pair C_i,F_i and hypotenuse D_i=R/h_i satisfy gcd(C_i+F_i,D_i)=1. For an odd prime divisor of D_i and C_i+F_i the same circle calculation forces both C_i,F_i divisible; D_i is odd.

## 2. Uniform physical-height equivalence
The standard projective height H_+=H([A_1:A_2:A_3]) is exactly max|A_i|. The upper bound is H_+<=sqrt(2)R. Since sum x_i^2=1 and sum y_i^2=2, Cauchy gives
sum (A_i/R)^2=3+2 sum x_i y_i >=3-2sqrt(2).
Thus
((sqrt(2)-1)/sqrt(3))R <= H_+ <= sqrt(2)R,
and in particular R/5 <= H_+ <= sqrt(2)R.
These constants are independent of content packets. This is a proved pushforward of the physical R measure; it is not an arbitrary ambient-height replacement.

## 3. Actual global ratios couple all three leading receivers
Define t_1=A_2/A_3, t_2=A_3/A_1, t_3=A_1/A_2. They are nonzero rational numbers with t_1 t_2 t_3=1 and each reduced rational height at most H_+. Put z_i=t_i+t_i^-1 and g_i=z_i^2/4. Direct expansion gives
z_1^2+z_2^2+z_3^2-z_1 z_2 z_3=4,
(g_1+g_2+g_3-1)^2=4g_1 g_2 g_3.
Each g_i and g_i-1 is a rational square, and g_i>=1 over the real numbers.

At a137 fresh p^lambda||m_i the corresponding leading receiver is g_i modulo p^(2lambda), with the appropriate physical ratio or its reciprocal and its inherited unit/square masks. These are three actual global ratios with product1, not the single CRT residue T of137 made into a global rational parameter. No independent character probabilities may be multiplied.

Novelty firewall: bare Fricke identities already occur in ROUTE26–31 for Gaussian norm-one phases. The new claim here is the physical integer plus-vector, its primitive projective height uniformly comparable to R, and the finite physical inverse below. Old phase sign/rootline assertions do not transfer automatically.

## 4. A degree-at-most-eight inverse, never an identically zero scale polynomial
Fix a projective point with all A_i nonzero and write r=(A_1/A_3,A_2/A_3,1). The remaining physical scale K=w_3^2=(A_3/R)^2 is a positive rational square. Define
d_i(K)=K r_i^2-1, S(K)=sum d_i(K), v_i(K)=S(K)-2d_i(K),
q_i(K)=1-d_i(K)^2=K(2r_i^2-Kr_i^4).
Then define
H_r(K)=[1+sum q_i^2-2sum q_i-2sum_(i<j)q_i q_j]^2-64q_1 q_2 q_3.
This is the134 signed-sphere eliminant T(v(K)). It has degree at most8 and H_r(0)=1 for every r. Therefore no specialization of r makes the scale equation identically zero, even when the leading degree drops.

To see necessity directly, set delta_i=x_i^2-y_i^2. Then delta_i^2=q_i and sum delta_i=-1. Eliminating the signed square roots from this relation gives precisely the displayed H_r(K). Equivalently it is (SE+P)^2-S^2 P(4S-P), where E=sum_(i<j)v_i v_j and P=product v_i.

Every physical preimage has H_r(K)=0. There are at most8 rational K values. On the134 nondegenerate open mask each K determines d and v, and the positive normalized physical direction is unique by134; its primitive integer endpoint is unique. Hence each projective plus point has at most8 canonical physical endpoint preimages in this scope. This is a uniform bound, not a claim of degree exactly8 at every point.

The converse requires K>0 a rational square, all 2-Kr_i^2 rational nonzero squares, compatible signed sphere lift and positive x, actual plus-vector signs matching the fixed projective point up to one simultaneous global sign, and all original packet and exact-R masks. Roots alone are not physical endpoints. Independent sign flips change the projective point. Zero-edge test samples below do not enlarge the theorem's endpoint scope.

## 5. Same-measure support receiver, no counting credit
Let E_pkt(B) be the canonically witnessed physical endpoint population in the stated open packet with R<=B. Let A_+(B) be the cardinality of projective plus points realized by exactly that population. Then
A_+(B) <= E_pkt(B) <=8 A_+(B).
Their projective heights are <=sqrt(2)B, and any physical preimage of a projective point of height<=H has R<=5H. Do not replace this realized image by all P^2(Q) of bounded height or all rational roots of H_r.

The fixed8 fiber is a structural receiver, not a fixed-power saving and not an independent density. The required moving support estimate remains open. Existing primary receiver P(B)<=B^o(1) A_1,1(B), its fixed-power budget, and the old hard one-twelfth branch budget are unchanged. A sufficient bound on the applicable hard-branch realized support would be B^(1/12-delta), with fixed delta>0, on the original physical measure; none is proved here.

## Verification and audit
Python replay:1000 generic scale-polynomial cases,1000 coupled-ratio identities,1488 signed primitive zero-edge Pythagorean boundary samples. All PASS. Boundary samples check primitive plus vector, gcd(A_i,R), height inequalities, rational-ratio height, and scale equation; they are not positive cuboid endpoints. Positive physical endpoints enumerated=0.
Symbolic replay returns {8,1,0,0}: generic degree8, constant1, Fricke identity zero, g identity zero.
The audit rederived gcd and Cauchy bounds, ruled out identically zero scale fibers by constant1, checked134 uniqueness scope, separated canonical signed witnesses from arbitrary sign branches, and checked prior Fricke novelty. This is within-session auditing, not an independent external audit. Finite verification supports algebra replay; proofs above establish the uniform assertions.

## Handoff
M3-T11-139: count the realized primitive physical projective plus-vector with the degree-eight rational-square scale lift and height comparable to exact R, uniformly in original packets. First enforce all actual sign/positivity/content masks; seek a nonlocal moving-support estimate. Do not return to settled leading character screens, treat CRT T as a single global ratio, or charge fixed fibers as a power saving.135 singular empty carrier,134 D-only fresh routing,137 leading-square witnesses,120 retraction, global credit0 and gateOPEN remain in force.

