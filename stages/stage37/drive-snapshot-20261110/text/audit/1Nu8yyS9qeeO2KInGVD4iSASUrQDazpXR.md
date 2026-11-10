# M3-T11-120 — hostile re-audit FAIL: evaluation point is not the rational quartic root

CURRENT_STATUS=RETRACTED_PHYSICAL_ADAPTER / HOSTILE_REAUDIT_FAIL / HISTORICAL_RECORD_RETAINED
CORRECTS=M3-T11-120 and its historical PASS audit; no new research-card ID is assigned.
AUDIT_KIND=Within-session dependency rederivation and exact rational arithmetic; not an external independent review.
POPULATION=The same exact nondegenerate fixed-packet Stage37 physical endpoint population with R<=B, restricted to phi/1+3.

## 1. First invalid inference

M3-T11-106 says the physical evaluation coordinate is z_phys=S/2. M3-T11-109/110 says that on the phi image the polynomial Q_u has a unique rational root vartheta=N/Q0. A rational evaluation point is not thereby a root. These two rational objects cannot be identified merely from the uniqueness of the polynomial's rational root.

The previously audited M3-T11-110 explicitly states: do not identify vartheta with physical z=S/2; vartheta is a root, whereas z is the evaluation point in the etale descent. M3-T11-105 gives the physical condition Q_u(z)/A=-w^2, not Q_u(z)=0.

Thus the opening root lock S=2N/Q0 in M3-T11-120 has no valid physical adapter. Substituting it in later algebra does not establish it on physical endpoints.

## 2. Exact discriminant certificate

Put A=1+u^2 and retain the actual symmetric cubic

f(X)=X^3-S*X^2+E*X-Pi,
E=4u(S-u)/A,
Pi=4u^2*S/A.

The standard cubic discriminant is

Delta=S^2*E^2-4E^3-4S^3*Pi-27Pi^2+18S*E*Pi.

Direct expansion gives the polynomial identity

A^3*Delta/(16u^2)
=A*S^2*(S-u)^2-16u*(S-u)^3-A^2*S^4-27u^2*A*S^2+18u*A*S^2*(S-u)
=-u^2*(A*S^4-16u*S^3+(44u^2-4)*S^2+48u*S-16u^2).

Since the last parenthesis is 16Q_u(S/2), exactly

Delta=-256u^4*Q_u(S/2)/A^3.

For the retained distinct rational anti-roots v_i, let D_diff=product_(i<j)(v_i-v_j). Then Delta=D_diff^2, and

Q_u(z_phys)/A=-(A*D_diff/(16u^2))^2.

On the nonzero-discriminant locus this is a nonzero negative rational square. In particular z_phys is not any root of Q_u, including vartheta. If one forcibly sets z_phys=vartheta, Delta=0 and the symmetric cubic has repeated roots: this is the branch/degenerate locus, not the distinct-root physical adapter used in the retained descent.

This does NOT prove the whole physical phi population empty. The condition z_phys=vartheta was never proved for that population, so contradiction after imposing it cannot eliminate phi.

## 3. Withdrawal scope and retained results

Withdraw M3-T11-120's physical claims:

- S=2N/Q0 and the resulting physical Pi formula;
- Q0 iff c_p=0, Q1 iff c_p=2lambda, and strict-interior phi support empty;
- 3|lambda on all Q1 physical fresh primes, M_phi,1=C1^3, beta1^4|B1;
- the physical Q1 cap M_phi,1<<H^(3/2) and Q1 tail H^(1/2)+H^2/M;
- the total-conductor improvement H+H^2/sqrt(R0) and cap M_rel<<H^(5/2).

The computations made AFTER imposing the root lock, including the special Pi expression, are algebraic conditional identities only. They are not physical theorems. Historical proof text and historical audit remain retained and explicitly superseded by this correction.

Retain independent audited M3-T11-119:

U+iV=i*conj(r+i*s)*((r-2s)+i*s)^3,
E_phi,0(B;H,M0)<<B^o(1)*min(H^2,H+H^2/M0),
M_phi,1<<H^3,
E_phi(B;H,M_rel>=R0)<<B^o(1)*min(H^2,H+H^5/R0),
M_rel<<H^4.

Retain M3-T11-118's fixed norm-squareclass theorem and its 119 feasibility caveat. Retain M3-T11-110's actual interior Q0/Q1 allocation and Q1=>cubic resonance, with no converse or local-density credit. Retraction of the interior-empty claim does not prove that physical interior points exist; their occupancy remains open.

## 4. Correct continuation gate

On the phi polynomial factorization Q_u(z)=A*(z-vartheta)*C_u^(3)(z), with C_u^(3) monic cubic, the true physical relation is

(z_phys-vartheta)*C_u^(3)(z_phys)=-w^2,
z_phys=S/2,
Pi=4u^2*S/A.

Here C_u^(3) is a cubic polynomial, NOT the conductor C_u. This relation is already the split form of audited 105's norm constraint; it receives no new saving credit. Any new use must control genuinely global factor squareclasses or correlate the nonzero difference z_phys-vartheta with the existing physical/conductor coordinates on the same R<=B measure. Do not replay the frozen local tuple.

NEXT_LEGAL_ACTION=Resume the residual Q1-dominant phi gate from 119 using distinct z_phys and vartheta. Seek a genuinely independent same-R<=B global correlation of their nonzero difference/cubic evaluation and conductor support, or pivot to nonlocal S4/theta!=0. No extreme-only phi allocation may be assumed.
DO_NOT_REPEAT=Never infer that a rational evaluation point equals a unique rational polynomial root. Never promote the root-locus Pi formula or the retracted fourth-power tail without a separate valid physical adapter. Never claim phi empty from this re-audit.

VERIFICATION=2,880 exact rational (u,S) evaluations verified the discriminant identity; 510 primitive phi parameters verified Q_u(vartheta)=0 and that imposed S=2vartheta always gives Delta=0. Finite checks support the displayed exact expansion, not physical existence/nonexistence.
SOURCE_LOCATORS=active ROUTE 118.3 (105 physical negative-square norm); 120.1/120.2 (106 evaluation coordinate versus local roots); 125.3 and DO_NOT_REPEAT (110 explicit separation); 135 (119 retained counts); 136 (120 invalid adapter).

LATEST_RESEARCH_CARD=M3-T11-120
LATEST_AUDITED_RESEARCH_CARD=M3-T11-119
LATEST_RESEARCH_CARD_STATUS=RETRACTED_PHYSICAL_ADAPTER
LATEST_REAUDITED_CARD=M3-T11-120
LATEST_REAUDIT_STATUS=FAIL
PROVISIONAL_FRONTIER_CARD=NONE
NEXT_RESEARCH_CARD_ID=M3-T11-121
NO_NEW_CARD_FOR_CORRECTION=true
PHI_PHYSICAL_ROOT_LOCK_PROVED=false
PHI_FRESH_INTERIOR_SUPPORT_EMPTY_PROVED=false
PHI_Q1_GAUSSIAN_FOURTH_POWER_PHYSICAL_PROVED=false
PHI_120_IMPROVED_COUNTING_CREDIT=false
GLOBAL_FIXED_POWER_SAVING=false
PRIMARY_GATE_CLOSED=false
P_OVER_M3_LIMIT_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_CREDIT=false
