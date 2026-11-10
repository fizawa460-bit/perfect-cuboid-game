# M3-T11-126 — Theta cofactor, minimal discriminant and physical component packet
DATE=2026-09-30
STATUS=PROVED_EXACT_REDUCTION_AND_COMPONENT_ADAPTER / WITHIN_SESSION_ADVERSARIAL_AUDIT_PASS / NO_NEW_GLOBAL_COUNTING_CREDIT
PRIMARY_GATE=M3-T11-GATE-001 OPEN
AUDIT_MODE=Within-session adversarial rederivation, not external/independent-agent review.
CURRENT_AUTHORITY=Drive MAIN/INDEX/RESULT-LEDGER/active ROUTE125.
DEPENDENCIES=audited093 theta carrier/saturation/fixed fiber;094 actual cofactor;095 Z and old-w identity;096 translated model/Kummer firewall;124 reduced fraction;125 denominator constraint. TIparked;120withdrawn;123retained.

## Scope and attempted gate
Same nondegenerate exact-R<=B fixed packet, generic full-S theta!=0 physical endpoints. Numerator support contraction requested by125 is NOT established. Direct cofactor square compatibility did not yield a sparse numerator theorem. This card instead gives an exact elliptic reduction/component packet that keeps M and q, and proves that its standalone local coset receiver is still only subpower. No physical points are manufactured from the packet.

Use theta=A/C reduced, C>0, A=M^4*q, q!=0 integer, gcd(A,C)=1. Here q=N0*Psi/g is the actual124/125 reduced cofactor, not095's tangent slope. Denote the latter slope by h=3-2w, w=u/S.
N=a²+b²=M²N0, t=M²t0, u=a/b, v=u². Every fresh p^lambda||M has p odd, p=1mod4, p!=3, b and C units, v_p(v+1)=2lambda, v_p(w)=2lambda.

## 1. Integral global adapter and distinct support blocks
Audited096 translates the curve to
E_theta: Z²=X³+(9+4theta)X²+4theta*X,
with physical point X=-(v+1), Z=(v+1)*h.
Clear denominators by X'=C²X,Y'=C³Z:
E_int: Y'²=X'³+C(9C+4A)X'²+4AC³X'.
This is a Q-isomorphism; its discriminant is NOT claimed globally minimal.

Put D=16A²+56AC+81C². Direct invariants are
c4=16C²(16A²+60AC+81C²),
Delta=256A²C^8D=256M^8q²C^8(16M^8q²+56M^4qC+81C²).
D>0: its binary quadratic discriminant56²-4*16*81=-2048 is negative.
Since gcd(q,C)=1 and D=81C² modq, gcd(|q|,D) divides81.
Also gcd(M,D)=1: modulo every fresh p|M, D=81C² is a unit.
These are exact support separations, not independent probabilities or a radical/height theorem. q need not be coprime to M on the p=1mod12 overvaluation branch.

## 2. Fresh minimal discriminant, conductor and Tamagawa numbers
At fresh p^lambda||M let e=v_p(q)>=0. Then
v_p(Delta)=8lambda+2e, v_p(c4)=0.
The model E_int is integral and minimal at this p: a nonminimal integral change lowering Delta by12 positive valuation would make the new c4 valuation negative. Its reduction is
Y'²=X'²(X'+9C²),
with a node at(0,0) and distinct rational tangent slopes +/-3C. Thus it is split multiplicative.
Consequently
Kodaira type I_n, n=8lambda+2e;
minimal discriminant exponent n;
elliptic conductor exponent f_p=1;
Tamagawa number c_p=n;
component group E(Q_p)/E^0(Q_p)=Z/nZ.
This curve's elliptic conductor is DISTINCT from the physical M_rel conductor.
Its fresh elliptic conductor contribution is rad(M), while its fresh minimal discriminant contribution is M^8*prod_{p|M}p^(2v_p(q)). No claim about primes outside M or global minimality.

On p=5mod12, audited093 rational-r compatibility forces e=0, so n=8lambda exactly. Do not extend that saturation to p=1mod12 or to synthetic E_theta points lacking the original rational-r condition.

## 3. Component class of the actual point
At fresh p, h=3-2w is a unit. Therefore
v_p(X')=v_p(Y')=2lambda.
The point reduces to the node, hence lies outside E^0(Q_p).
For split multiplicative minimal models the component distance, up to simultaneous sign, is min(v_p(2Y'+a1X'+a3),n/2). Here a1=a3=0 and p is odd, so
kappa_p(P)=+/-2lambda modn.
Its exact component order is
(8lambda+2e)/gcd(8lambda+2e,2lambda).
If e=0 this is4. The rational2torsion T=(0,0) reduces to the node and has component class n/2. Thus on every saturated fresh prime (in particular every p=5mod12),
2P-T lies in E^0(Q_p), and4P lies in E^0(Q_p).
These are statements in the component quotient, NOT global equations 2P=T or4P=O, NOT torsion claims about P, and NOT global divisibility or Selmer collapse.

This presentation retains valuations erased by ordinary Kummer, but the point valuations come from the same095 old-w/tangent structure already charged. It gives no additional local saving.

## 4. Standalone component-product boundary
For the toy product of fresh component groups, requiring each class to be one of +/-2lambda admits2 classes among n (the two are distinct since n>4lambda). Its formal uniform-component proportion is prod_{p|M}2/n_p.
This toy proportion is NOT a sampling law for physical points.
Even this local product cannot produce a fixed power on physical-induced polynomial heights:
n_p=8lambda+2e <=8(lambda+1)(e+1),
so
prod_{p|M}n_p <=8^omega(M)*tau(M)*tau(|q|)=B^o(1).
Use standard divisor bounds and M,|q|<=B^O(1) from the retained rational-height interface. Thus the inverse toy proportion is at most B^o(1), also on the exact-saturation n=8lambda branch.
No density, root orientation, Tamagawa factor, Kummer or old-w factor may be multiplied into independent physical savings. A global restriction on the diagonal Mordell-Weil image or actual moving curves would be extra information; no such bound is proved here.

## 5. Sources and verification
Primary technical sources checked this batch:
- J.E.Cremona, Computing in Component Groups of Elliptic Curves, author preprint https://johncremona.github.io/papers/component.pdf, introduction and Section2. It identifies the split component group and gives the component-distance formula on a minimal model.125/093/095 supply the physical valuations inserted here.
- SageMath project source https://github.com/sagemath/sage/blob/develop/src/sage/schemes/elliptic_curves/ell_local_data.py, multiplicative branch: c4 unit -> I_n, split ->c_p=n, f_p=1.
- LMFDB reviewed definition by Cremona/Jones https://www.lmfdb.org/knowledge/show/ec.split_multiplicative_reduction confirms the nodal tangent criterion.
No quotations are reproduced.

verify_m3_t11_126.py checks440 exact synthetic E_theta points from oriented Gaussian powers at p=5,13,17,29, lambda1..4. It verifies reduced A=M^4q, fresh c4/Delta valuations, point coordinates, support gcd and component-order arithmetic.163 p=5mod12 cases satisfying the necessary local rational-r detector have e=0. Synthetic overvaluation examples atp5 fail that detector and are explicitly NONPHYSICAL.
The component theorem and Tate reduction rules are applied analytically; no Sage local-data algorithm was run. Finite checks do not prove physical realization or asymptotic bounds.
Wolfram exact symbolic replay checks c4, Delta, substitution A=M^4q and remainder81C² without protected-symbol warnings.

## Audit and continuation
WITHIN_SESSION_ADVERSARIAL_AUDIT=PASS within these scopes.
Checks: cubic polynomial discriminant differs from elliptic Delta by16; clearing denominators weights2/3 and scaling C^12; c4unit ensures fresh minimality; C,b,3 are freshunits; split tangent slopes; q cofactor not tangenth; component equality only modulo n; overvaluation cannot be suppressed; elliptic vs physical conductor; local coset product is subpower and not physical density.
GLOBAL_COUNTING_CREDIT=0
NEXT_RESEARCH_CARD_ID=M3-T11-127
CURRENT_ATTACK=ThetaGlobalComponentImageAcrossMovingCurves
NEXT_LEGAL_ACTION=Test whether the GLOBAL rational-point image in prod_{p|M}E_theta(Q_p)/E_theta^0(Q_p), together with actual q=N0*Psi/g, v=u², original rational-r and exact R<=B, forces a sparse realized(M,q,C) support beyond the local +/-2lambda packet. Seek a proved global height/Mordell-Weil/curve-occupancy theorem; do not assume Szpiro/abc, rank bounds, full Selmer collapse or component independence. If only old-w/local data reappear, record scoped no-go and pivot to retained S4 realized norm-kernel/cross-u.125 scoped b-height tail retained; TI stays parked.
DO_NOT_REPEAT=No global minimalDelta claim; no ellipticconductor=M; no componentorder4=>P order4; no global2P=T; no p1mod12 exactsaturation; no multiplication of Tamagawa/coset factors; no syntheticphysicalpoints; no retracted120.

GLOBAL_FIXED_POWER_SAVING=false
PRIMARY_GATE_CLOSED=false
M3_T11_PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false

