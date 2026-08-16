# Stage25-reentry-40 — directional two-face mechanism and Stage20 receiver

TASK_ID=Stage25-u22-r004a
PHASE=40
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
PARENT_R009A_PR=1006
PARENT_R009A_MERGE=4eb3349ee8ec02dcabb71bd1be3a48234356606b
TARGET_STAGES=22,16,18
STAGE20_RECEIVER=true

## 1. Population lock

Work in the primitive canonical no-space host

`0<a<b<c`, `gcd(a,b,c)=1`, `R=sqrt(a^2+b^2+c^2)<=B`.

Let `P_a,P_b,P_c` be the raw pair-incidence counts for successful face pairs `ab,ac`, `ab,bc`, `ac,bc`, respectively, with no third-face exclusion. Let `M2,j` be the exactly-two count with shared edge `j`, and let `M3` be the all-three-face Euler-cuboid count.

The face-indicator truth table gives the exact identities

`P_a=M2,a+M3`, `P_b=M2,b+M3`, `P_c=M2,c+M3`,

hence

`M2,a=P_a-M3`, `M2,b=P_b-M3`, `M2,c=P_c-M3`.

All raw-pair contrasts cancel the common `M3` term exactly.

## 2. Directional asymptotic input

The frozen Stage18 directional theorem, recorded in the audited Stage24 interface, is

`M2,j(B) ~ C_j B(log B)^5`, `C_j>0`, for `j=a,b,c`.

The Stage20 theorem gives, for every fixed `eta<1/46`,

`M3(B) <<_eta B(log B)^(5-eta)`.

Therefore for every `j=a,b,c`,

`M3(B)/M2,j(B) <<_{j,eta} (log B)^(-eta) -> 0`,

and consequently

`P_j(B) ~ C_j B(log B)^5`,

`M2,j(B)/P_j(B) = 1-O_{j,eta}((log B)^(-eta)) -> 1`.

Here `M2,j` is literally the subset of the raw pair-incidence chamber `P_j` obtained by requiring the remaining face to be nonsquare, so this ratio is a legitimate literal postfilter survival ratio.

Thus the third-face nonsquare postfilter is lower order in every shared-edge chamber separately, not merely after summing directions.

## 3. Directional Stage22 transition

Stage22's audited source law is

`M1(B) ~ 3/(4*pi^2) B^2 log B`.

Hence for every `j=a,b,c`,

`M2,j(B)/M1(B) ~ (4*pi^2*C_j/3) (log B)^4/B -> 0`.

So the Stage22 sharp scale `(log B)^4/B` occurs in every directional target chamber with a positive leading constant. It is not an averaging artifact caused by only one shared-edge orientation.

Because the exactly-two chambers partition `M2`,

`M2=M2,a+M2,b+M2,c`,

and therefore

`C_M2=C_a+C_b+C_c`,

`M2,j/M2 -> C_j/C_M2 in (0,1)`.

## 4. Stage20-ready receiver

The raw-pair identities isolate the complete Euler population as the same common contaminant in all three directions:

`M3=P_j-M2,j`.

The quantitative Stage20 upper shows this contaminant is lower-order against every `P_j` and every `M2,j` at the Stage18 `B(log B)^5` scale. This gives Stage20/phase60 a clean pair-chamber receiver without changing the Stage20 true-growth problem.

## 5. Fine-mechanism boundary

This phase does not produce a canonical factorization of the relative `(log B)^4` into four independent arithmetic causes. Existing toric/shared-edge interfaces prove the net log power and now its directional robustness, but do not canonically allocate four separate local, valuation, squareclass, or divisor factors.

`G22_LOG4_FINE_MECHANISM` therefore remains open.

## 6. Scope firewall

```text
EXACT_NO_SPACE_MASK_IDENTITIES=true
COMMON_M3_CONTAMINATION_ISOLATED=true
PAIR_CONTRASTS_M3_FREE=true
DIRECTIONAL_THIRD_FACE_POSTFILTER_SURVIVAL_TO_ONE=true
DIRECTIONAL_STAGE22_SHARP_SCALE=true
C_M2_SUM_DIRECTIONAL_CONSTANTS=true
LOG4_DIRECTIONAL_ROBUSTNESS_PROVED_CANDIDATE=true
FOUR_INDEPENDENT_LOG_FACTORS_PROVED=false
FINE_MECHANISM_OPEN=true
TRUE_M3_EXPONENT_IDENTIFIED=false
GLOBAL_M2_THEOREM_CHANGED=false
PERFECT_CUBOID_CONCLUSION=NONE
FINITE_DATA_USED_AS_PROOF=false
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
NEXT_REENTRY_PHASE=50
QUEUED_DERIVED_ROUTE=Stage25-um-r010a
PHASE50_ALLOWED=false
STAGE26_ALLOWED=false
NEXT_EXPECTED_COMMAND=Stage25-reentry-audit
```
