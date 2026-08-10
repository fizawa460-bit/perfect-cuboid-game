# Stage14-toolbox-ax — first-consumer audit and five-eighths receiver refresh

## Status

`COMPLETE_FIRST_CONSUMER_AUDIT_AND_FIVE_EIGHTHS_RECEIVER_REFRESH`

Stage14-toolbox-aw ended with the explicit instruction

```text
Stage14-toolbox-ax audit the first 4cq/s7-30/t69 consumers against the refreshed three-quarter certificates.
```

This stage performs exactly that audit on merged current main.  It does not re-prove the underlying arithmetic.  It follows each source stage only far enough to identify its first legal merged consumer and then refreshes the toolbox receiver/exponent ledger to the strongest currently merged certificate.

The three source lines have advanced as follows:

```text
4cq   -> X8 / 4cr
s7-30 -> s7-31
t69   -> t70
```

The merged `s7-31` theorem is now stronger than the `2/3` 4-route promotion, so the shared whole-family toolbox exponent is `5/8`.  The fixed-`U` t-line remains a distinct coefficient space and is not promoted from that global certificate.

---

## 1. 4cq first consumers

Merged `4cq` established the dual common-core Cayley divisor lock and the alternative charged-once exponent

```text
E_dual <= 1/2 + 2phi - c.
```

Its first merged consumers are `X8` and `4cr`.

### X8

Merged `X8` legally combines the independent s7-30 and 4cq bounds blockwise by taking a minimum, not by multiplying putative savings:

```text
E_X8
 <= min(
      max(theta+phi+1/8, 1-2theta),
      5/4-2theta
    )
 <= 2/3.
```

It identifies the temporary `2/3` saturation

```text
theta=7/24,
phi=1/4,
c=1/3
```

and the receiver

```text
Theta7Over24QuarterPhiCommonGcdCayleyGaussianQuotientEnergy.
```

### 4cr

Merged `4cr` promotes the same `2/3` estimate into the 4/mainline ledger and adds the exact Cayley sign allocation

```text
C_- C_+ = C_*,
gcd(C_-,C_+)=1,
```

with opposite/same Gaussian orientations on `C_-`/`C_+`.  Its receiver is

```text
TwoThirdsCayleyGaussianCommonGcdRootProductIncidence.
```

These are valid structural certificates.  They are no longer the strongest whole-family exponent certificates after merged `s7-31`.

```text
FOUR_CQ_TWO_THIRDS_CERTIFICATE_VALID=true
FOUR_CQ_TWO_THIRDS_CERTIFICATE_CURRENT_GLOBAL_BARRIER=false
```

---

## 2. s7-30 first consumer

The canonical merged `s7-30` is PR #517, whose charged-once second-root-pair count proves

```text
V(B) << B^(11/16+o(1)).
```

with receiver

```text
TopCornerOppositeSignedQuotientCommonGcdRootProductIncidence.
```

There was a later alternative PR #521 with the same stage label, but it was closed without merge and is not a canonical source on main.  The repository's merged `14-s7-30/result.md` is the `11/16` theorem from PR #517.

Its first merged consumer `s7-31` identifies the only source of the `sqrt(M)` loss: treating

```text
h=gcd(c_k^+,c_k^-)
```

as free.  Physical reducedness plus merged 4ci instead gives, after outer `(C,u_res)` is fixed,

```text
oddpart(h)^2 | C*u_res.
```

Thus the admissible common gcds are divisor-many, and the nonprimitive second-root-pair bound sharpens to

```text
#(c_k^+,c_k^-)
 << B^o(1) * (1 + M/C).
```

The full-strip charged-once exponent becomes

```text
E(theta,phi)
 <= max(2theta,1-2theta)
 <= 5/8.
```

Therefore the strongest merged whole-family certificate is now

```text
V(B) << B^(5/8+o(1)).
```

with live s/global receiver

```text
FiveEighthsTwoBoundaryCommonCoreReciprocalIncidence.
```

Its possible saturation geometry is

```text
upper edge:  theta=5/16, 3/16<=phi<=1/4
lower corner: theta=phi=3/16.
```

No external theorem, determinant method, large sieve, or H/tH result is used in this promotion.

---

## 3. t69 first consumer

Merged `t69` decomposes the noncanonical Cayley common support into four pairwise-coprime orientation components

```text
J++, J--, J+-, J-+
```

and defines the full common modulus

```text
J = J++ J-- J+- J-+.
```

Its first merged consumer `t70` corrects the planned `extra-only` dichotomy.  The full common support must be used before radial uncharging:

```text
T69_EXTRA_ONLY_DICHOTOMY_SUPERSEDED=true
FULL_COMMON_SUPPORT_MUST_BE_USED_BEFORE_RADIAL_UNCHARGING=true.
```

Prime-power root orientations CRT-compress to one primitive linear root line

```text
v_j*u_i == lambda*u_j*v_i (mod J),
```

with only `B^o(1)` orientations.  For a fixed anchor the partner count is

```text
N_i(J;M) <= (1 + M/J) B^o(1).
```

Hence the large-full-`J` branch is near-linear.  The surviving fixed-`U` receiver is the small-common-support branch

```text
SharedUPrivateLargestPrimeSmallCommonSupportPhysicalSquareScaleEnergy.
```

`tH18` is consumed.  `tH19` is not yet required because t70 still leaves unused exact fixed-`U` Gaussian/cover structure for t71.

This t-line receiver is not equivalent to the global s/common-core receiver and does not alter the `5/8` whole-family exponent.

---

## 4. Cross-route promotion rules after ax

The legal current toolbox ledger is:

1. `4cq -> X8/4cr` supplies valid dual-Cayley/Gaussian structure and a proved `2/3` global bound, but that exponent is superseded by `s7-31`.
2. `s7-30 -> s7-31` supplies the strongest merged whole-family theorem, `5/8`.
3. `t69 -> t70` supplies a fixed-`U` small-`J` square-scale receiver only; it is not cross-promoted into the whole-family bound.
4. The old aw `3/4` receiver `QuarterPhiCommonCorePrimitiveFourRootQuadraticValueEnergy` is historical, as are the intermediate `11/16` and `2/3` barriers.
5. The closed-unmerged alternative s7-30 PR #521 must not be used as a canonical theorem source.
6. No savings from the 4/s/t lines are multiplied together.  Only independently proved bounds on the same counted universe may be compared by `min`.

---

## 5. Supervisor decision

No toolbox-H continuation is opened.

The current unresolved objects are already exact arithmetic receivers:

```text
GLOBAL/S:
FiveEighthsTwoBoundaryCommonCoreReciprocalIncidence

FIXED-U/T:
SharedUPrivateLargestPrimeSmallCommonSupportPhysicalSquareScaleEnergy
```

Neither is an unverified theorem import masquerading as a proof, and neither is equivalent to the other.

The next toolbox audit should follow the first consumers of `4cr`, `s7-31`, and `t70`, while guarding the `5/8` certificate against stale `3/4`, `11/16`, or `2/3` promotion metadata.

---

## Boundary

```text
STAGE14_TOOLBOX_AX=COMPLETE_FIRST_CONSUMER_AUDIT_AND_FIVE_EIGHTHS_RECEIVER_REFRESH
MERGED_TOOLBOX_AW_IMPORTED=true
FIRST_4CQ_CONSUMERS_AUDITED=true
FIRST_S7_30_CONSUMER_AUDITED=true
FIRST_T69_CONSUMER_AUDITED=true
CANONICAL_MERGED_S7_30_PR=517
CLOSED_UNMERGED_ALTERNATE_S7_30_PR_521_CANONICAL=false
X8_TWO_THIRDS_MINIMAX_PROVED=true
FOUR_CR_TWO_THIRDS_MAINLINE_PROMOTION_PROVED=true
FOUR_CQ_TWO_THIRDS_CERTIFICATE_CURRENT_GLOBAL_BARRIER=false
S7_31_FIXED_OUTER_COMMON_GCD_SQUARE_DIVISIBILITY_PROVED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=5/8
IMPROVEMENT_OVER_TOOLBOX_AW_3_4=1/8
CURRENT_GLOBAL_S_RECEIVER=FiveEighthsTwoBoundaryCommonCoreReciprocalIncidence
CURRENT_GLOBAL_S_RECEIVER_PROVED=false
T69_EXTRA_ONLY_DICHOTOMY_SUPERSEDED=true
T70_LARGE_FULL_COMMON_SUPPORT_ROOTLINE_BRANCH_NEAR_LINEAR=true
CURRENT_FIXED_U_RECEIVER=SharedUPrivateLargestPrimeSmallCommonSupportPhysicalSquareScaleEnergy
CURRENT_FIXED_U_RECEIVER_PROVED=false
GLOBAL_S_AND_FIXED_U_RECEIVERS_EQUIVALENT=false
TH18_CONSUMED=true
TH19_NEEDED=false
TOOLBOX_H_CONTINUATION_NEEDED=false
TOOLBOX_ROUTE_BLOCKED=false
NEW_AX_WHOLE_FAMILY_POWER_SAVING_PROVED=false
NEXT=Stage14-toolbox-ay audit first 4cr/s7-31/t70 consumers against the five-eighths certificate
```
