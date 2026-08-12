# Stage14-4gh — bounded witness multiplicity reduces reciprocal support exactly to one K-free CRT first moment

## Status

`COMPLETE_RECIPROCAL_SUPPORT_TO_KFREE_DIVISOR_CRT_FIRST_MOMENT_THEOREM_INTERFACE`

Consumes batch-local `Stage14-4gf/4gg`, merged `Stage14-4ge`, and merged `Stage14-Work-bzX38/q17`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Use the actual nonnegative witness count

For `(u,v) in R_prim`, define

```text
N_rec(u,v):=#Omega_rec(u,v).
```

Merged 4gd gives uniformly

```text
0 <= N_rec(u,v) <= B^o(1),                         (1)
```

and by definition

```text
T_rec={(u,v):N_rec(u,v)>0}.                         (2)
```

Let

```text
S_1:=sum_{(u,v) in R_prim} N_rec(u,v).              (3)
```

Because every accepted pair contributes at least one witness and at most `B^o(1)` witnesses, (1)--(2) imply exactly

```text
#T_rec <= S_1 <= B^o(1)*#T_rec.                    (4)
```

Therefore `S_1` and `#T_rec` have the same fixed-power exponent.

```text
RECIPROCAL_SUPPORT_EXPONENT_EQUALS_FIRST_MOMENT_EXPONENT=true
```

## 2. The q17 second moment is not logically required

Write

```text
#R_prim=B^(kappa+o(1)),
#T_rec=B^(sigma_rec+o(1)),
S_1=B^(lambda_rec+o(1)).
```

Equation (4) gives

```text
lambda_rec=sigma_rec,                               (5)
```

hence

```text
delta_rec=kappa-sigma_rec
         =kappa-lambda_rec.                         (6)
```

Thus a uniform lower bound

```text
S_1 >= B^(kappa-o(1))                               (7)
```

proves

```text
delta_rec=0
```

at fixed-power scale, while a uniform upper bound

```text
S_1 <= B^(kappa-eta+o(1))                           (8)
```

for fixed `eta>0` proves a reciprocal support deficit at least `eta` on that cell.

The first/second-moment Cauchy--Schwarz route suggested by q17 remains valid but is stronger than necessary because the pointwise witness multiplicity bound (1) is already merged. No second moment may be demanded merely to transfer a first moment to support.

```text
Q17_SECOND_MOMENT_SUPPORT_TRANSFER_REQUIRED=false
Q17_FIRST_MOMENT_ALONE_CONTROLS_SUPPORT_AT_B_POWER_SCALE=true
```

## 3. Exact first-moment arithmetic after 4gg

Stage14-4gg writes every witness, after peeling primes supported on the frozen coefficient product `K_*`, using

```text
t_p | m^circ,
t_q | m^circ,
f_-*f_+=t_p*t_q,
```

plus `K_*`-supported core labels and the exact CRT conditions

```text
G_+*f_+ + G_-*f_- == 0 (mod 2U),
G_+*f_+ - G_-*f_- == 0 (mod 2V),                    (9)
```

with all bare parity/positivity/endpoint filters retained.

Consequently `S_1` is now a nonnegative, theorem-shaped divisor-allocation incidence over the primitive rectangle. There is no remaining support-versus-multiplicity logical gap inside the reciprocal layer: the only missing information is the size of this first moment itself.

The seeded branch from 4gf supplies one explicit subcase with `S_1=B^(kappa+o(1))`; the seedless branch is the genuine moving divisor-allocation CRT problem.

```text
KFREE_RECIPROCAL_FIRST_MOMENT_EXACT_THEOREM_SPECIES=true
SEEDED_FIRST_MOMENT_FULL_EXPONENT=true
SEEDLESS_FIRST_MOMENT_UNIFORM_EXPONENT_PROVED=false
```

## 4. Receiver and headroom ledger

Merged 4ge has

```text
heavy survival:
kappa-delta_rec-delta_post>=mu.
```

Using (6), this is equivalently

```text
lambda_rec-delta_post>=mu.                          (10)
```

Thus near threshold `kappa=mu+o(1)`, a surviving seedless packet requires the K-free reciprocal first moment to be exponent-full and the post-mask deficit to be zero at fixed-power scale. Above threshold, any first-moment deficit must be compared against the actual capacity headroom together with the residual post-mask deficit; the two are not independently multiplied.

The fixed-E two-sided receiver is therefore materially sharpened from an existential reciprocal-support object to

```text
FixedComplementaryDilationTwoSidedPrincipalRectangular
KFreeMovingDivisorAllocationTwoLevelCRTFirstMomentDeficit
VersusConditionalRootCanonicalPostColumnCompletionDeficit
WithCapacityHeadroomKappaMinusMu.
```

```text
CURRENT_FIXED_E_TWO_SIDED_RECEIVER=FixedComplementaryDilationTwoSidedPrincipalRectangularKFreeMovingDivisorAllocationTwoLevelCRTFirstMomentDeficitVersusConditionalRootCanonicalPostColumnCompletionDeficitWithCapacityHeadroomKappaMinusMu
RECEIVER_MATERIALLY_CHANGED=true
```

## 5. Frozen new heavy H contract

The internal algebra is now stable enough for an independent theorem audit on the seedless reciprocal layer. Freeze the new heavy target as

```text
FixedAgreementPairKFreeMovingDivisorAllocationTwoLevelCRTFirstMomentAsymptoticOrPowerDeficit
```

with contract:

```text
background:
  one fixed-E principal primitive rectangle R_prim,
  fixed ray/agreement data (x,y,U,V),
  frozen coefficient-prime support K_*;

moving variables:
  m^circ=(uv)^circ,
  t_p|m^circ,
  t_q|m^circ,
  f_-f_+=t_p t_q,
  K_*-supported core labels of total B^o(1) witness multiplicity;

retain exactly:
  the two CRT congruences (9),
  primitive gcd(u,v)=1,
  all bare positivity/parity/endpoint-small filters already inside Omega_rec,
  charged-once quantifier order;

audit goal:
  prove a uniform first-moment asymptotic/full-exponent lower bound,
  or a uniform fixed-power first-moment upper deficit on the relevant principal cells,
  or a rigorous parameter-dependent dichotomy;
  do not use the residual R_post mask and do not cross-promote fixed-U prime occupancy.
```

q17's Grimmelt--Merikoski / Irving / Nguyen / Frei--Sofos / Bettin leads are advisory inputs to this clean-room audit, not theorem claims.

Because this stage itself is a material receiver/theorem-interface change, the current batch stops here under the common contract. The next main batch must consume the frozen H decision before advancing ordinary `Stage14-4gi`; if the H audit leaves an unresolved external gate, the next batch stops there.

```text
NEW_HEAVY_MAIN_H_NEEDED=true
NEW_HEAVY_MAIN_H_TARGET=FixedAgreementPairKFreeMovingDivisorAllocationTwoLevelCRTFirstMomentAsymptoticOrPowerDeficit
MAIN_ROUTE_H_NEEDED=true
MAIN_ROUTE_H_REQUEST=FixedAgreementPairKFreeMovingDivisorAllocationTwoLevelCRTFirstMomentAsymptoticOrPowerDeficit
MAIN_ROUTE_H_TARGET=FixedAgreementPairKFreeMovingDivisorAllocationTwoLevelCRTFirstMomentAsymptoticOrPowerDeficit
MAIN_ROUTE_H_BLOCKING=false
EXISTING_NONHEAVY_MAIN_H_GATES_PENDING=true
WHOLE_MAINLINE_BLOCKED_BY_H=false
NEXT=Stage14-4gi
```

## Boundary

```text
STAGE14_4GH=COMPLETE_RECIPROCAL_SUPPORT_TO_KFREE_DIVISOR_CRT_FIRST_MOMENT_THEOREM_INTERFACE
RECIPROCAL_SUPPORT_EXPONENT_EQUALS_FIRST_MOMENT_EXPONENT=true
Q17_SECOND_MOMENT_SUPPORT_TRANSFER_REQUIRED=false
Q17_FIRST_MOMENT_ALONE_CONTROLS_SUPPORT_AT_B_POWER_SCALE=true
KFREE_RECIPROCAL_FIRST_MOMENT_EXACT_THEOREM_SPECIES=true
SEEDED_FIRST_MOMENT_FULL_EXPONENT=true
SEEDLESS_FIRST_MOMENT_UNIFORM_EXPONENT_PROVED=false
CURRENT_FIXED_E_TWO_SIDED_RECEIVER=FixedComplementaryDilationTwoSidedPrincipalRectangularKFreeMovingDivisorAllocationTwoLevelCRTFirstMomentDeficitVersusConditionalRootCanonicalPostColumnCompletionDeficitWithCapacityHeadroomKappaMinusMu
RECEIVER_MATERIALLY_CHANGED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEW_HEAVY_MAIN_H_NEEDED=true
MAIN_ROUTE_H_NEEDED=true
NEXT=Stage14-4gi
```