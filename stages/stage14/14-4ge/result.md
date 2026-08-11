# Stage14-4ge — split fixed-E completion into reciprocal divisor/CRT solvability and residual physical acceptance

## Status

`COMPLETE_FIXED_E_COMPLETION_TO_RECIPROCAL_SOLVABILITY_VERSUS_POST_MASK_DEFICIT_LEDGER`

Consumes batch-local `Stage14-4gc/4gd` and merged `Stage14-4gb`, `Stage14-q16`, and `Stage14-Work-byX37`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Principal primitive pair baseline

On one fixed `E=E0` two-sided principal rectangle, 4gc gives the primitive pair family

```text
R_prim={(u,v):u in D,v in V,gcd(u,v)=1},
#R_prim=B^(kappa+o(1)),
kappa>=mu-o(1).
```

The accepted physical pair support has the same exponent as the accepted outer-product support:

```text
T_phys={(u,v) in R_prim:C_pair(u,v)=1},
#T_phys=B^(tau+o(1)),
tau=tau_phys.
```

Merged 4gb therefore has

```text
delta_comp=kappa-tau,
heavy survival: kappa-delta_comp>=mu.              (1)
```

## 2. Bare reciprocal solvability support

Batch-local 4gd defines the exact subpolynomial candidate set `Omega_rec(u,v)`.  Define the bare reciprocal selector

```text
B_rec(u,v)
 :=1{Omega_rec(u,v) is nonempty}
```

and its support

```text
T_rec
 := {(u,v) in R_prim:B_rec(u,v)=1}.
```

This selector retains the exact algebraic reciprocal requirements already opened in 4gd:

```text
p | H0*x*u*v,
q | H0*y*u*v,
F_-*F_+=4*r*s*epsilon_k*p*q,
F_+ + F_- == 0 (mod 2U),
F_+ - F_- == 0 (mod 2V),
```

plus positivity/parity and the frozen endpoint-small divisibility filters used in the reciprocal reconstruction.

It does **not** include the residual root-origin, canonical allocation/orientation or post-column physical mask `R_post`.

Write

```text
#T_rec=B^(sigma_rec+o(1)),
0<=sigma_rec<=kappa.
```

Define the reciprocal-solvability deficit

```text
delta_rec:=kappa-sigma_rec>=0.                     (2)
```

## 3. Residual physical acceptance inside the reciprocal support

From 4gd,

```text
C_pair(u,v)=1
 iff
exists omega in Omega_rec(u,v) with R_post(u,v;omega)=1.
```

Hence

```text
T_phys subseteq T_rec.
```

Define the conditional post-mask deficit exponent

```text
delta_post:=sigma_rec-tau>=0.                      (3)
```

The `B^o(1)` candidate multiplicity of `Omega_rec(u,v)` ensures that this support ledger is not hiding a polynomial witness multiplicity.  The residual Boolean still contains, exactly once, every root-origin/cell, canonical allocation/orientation, reverse/post-column and finite two-primary condition not already used by the bare reciprocal system.

```text
RECIPROCAL_SUPPORT_PHYSICAL_SUPPORT_NESTED=true
FIXED_PAIR_RECIPROCAL_CANDIDATE_MULTIPLICITY=Bo1
POST_MASK_DEFICIT_IS_CONDITIONAL_SUPPORT_DEFICIT=true
```

## 4. Exact deficit decomposition

Equations (2)--(3) give the identity

```text
delta_comp
 = kappa-tau
 = (kappa-sigma_rec)+(sigma_rec-tau)
 = delta_rec+delta_post.                            (4)
```

Therefore the heavy survival condition (1) becomes exactly

```text
boxed:
kappa-delta_rec-delta_post>=mu.                    (5)
```

This is a nested-support exponent identity.  It is **not** a claim that reciprocal solvability and the post-mask are probabilistically independent, and the two deficits must not be multiplied or recharged on different copies of the packet.

```text
COMPLETION_DEFICIT_EXACTLY_SPLITS_AS_DELTA_REC_PLUS_DELTA_POST=true
RECIPROCAL_AND_POST_DEFICITS_INDEPENDENT_ASSUMED=false
RECIPROCAL_AND_POST_SAVINGS_RECHARGED=false
```

## 5. Threshold consequences

### Near-threshold rectangles

If

```text
kappa=mu+o(1),
```

then survival in (5) forces

```text
delta_rec=o(1),
delta_post=o(1),
```

because both deficits are nonnegative.  Thus a near-threshold survivor requires **both** the bare reciprocal divisor/CRT selector and the residual physical post-mask to have full fixed-power exponent.

### Super-threshold rectangles

If

```text
kappa>=mu+eta,
```

then survival allows losses only under the combined headroom budget

```text
delta_rec+delta_post<=kappa-mu.                    (6)
```

A future theorem for either mechanism is useful only at the strength actually needed to beat the remaining headroom after the other mechanism is retained.

```text
NEAR_THRESHOLD_SURVIVAL_FORCES_RECIPROCAL_DEFICIT_ZERO_AT_FIXED_POWER=true
NEAR_THRESHOLD_SURVIVAL_FORCES_POST_MASK_DEFICIT_ZERO_AT_FIXED_POWER=true
SUPERTHRESHOLD_COMBINED_DEFICIT_BUDGET=kappa_minus_mu
```

## 6. Material receiver change

Merged 4gb left one opaque completion deficit.  The exact 4gd reconstruction and the present nested-support ledger replace it by two explicit noninterchangeable mechanisms:

```text
(R)
FixedAgreementPairRadialLinearTwoLevelDivisorCRTReciprocalSolvabilitySupport

(P)
ConditionalRootOriginCanonicalAllocationPostColumnPhysicalAcceptance
inside the actual reciprocal candidate support.
```

Thus the fixed-E two-sided receiver is now

```text
FixedComplementaryDilationTwoSidedPrincipalRectangular
ReciprocalDivisorCRTSupportDeficitVersusConditionalRootCanonicalPostColumnCompletionDeficit
WithCapacityHeadroomKappaMinusMu.
```

This is a mathematically material receiver change, so the main batch stops here under the shared contract.

```text
CURRENT_FIXED_E_TWO_SIDED_RECEIVER=FixedComplementaryDilationTwoSidedPrincipalRectangularReciprocalDivisorCRTSupportDeficitVersusConditionalRootCanonicalPostColumnCompletionDeficitWithCapacityHeadroomKappaMinusMu
RECEIVER_MATERIALLY_CHANGED=true
WORK_BYX37_REVISIT_TRIGGER_4GE_REACHED=true
```

## 7. H decision

No new heavy H is opened at this boundary.  The reciprocal selector is now explicit, but it still contains a nested choice

```text
p|H0*x*u*v,
q|H0*y*u*v,
then a fixed-(U,V) factor-pair CRT condition on 4*r*s*epsilon_k*p*q.
```

The next internal step should test whether this selector already has full fixed-power exponent by an explicit divisor choice / CRT construction on principal cells, or whether a genuine divisor-correlation theorem is required.  Freezing an H target before that test could ask for a theorem stronger than the actual Stage14 headroom requires.

The residual post-mask remains a separate Stage14-specific receiver.  Existing non-heavy mainline H gates remain pending and are not altered.

```text
NEW_HEAVY_MAIN_H_NEEDED=false
MAIN_ROUTE_H_NEEDED=false
MAIN_ROUTE_H_REQUEST=NONE
MAIN_ROUTE_H_TARGET=NONE
MAIN_ROUTE_H_BLOCKING=false
EXISTING_NONHEAVY_MAIN_H_GATES_PENDING=true
WHOLE_MAINLINE_BLOCKED_BY_H=false
NEXT=Stage14-4gf
```

## Boundary

```text
STAGE14_4GE=COMPLETE_FIXED_E_COMPLETION_TO_RECIPROCAL_SOLVABILITY_VERSUS_POST_MASK_DEFICIT_LEDGER
COMPLETION_DEFICIT_EXACTLY_SPLITS_AS_DELTA_REC_PLUS_DELTA_POST=true
NEAR_THRESHOLD_SURVIVAL_FORCES_RECIPROCAL_DEFICIT_ZERO_AT_FIXED_POWER=true
NEAR_THRESHOLD_SURVIVAL_FORCES_POST_MASK_DEFICIT_ZERO_AT_FIXED_POWER=true
CURRENT_FIXED_E_TWO_SIDED_RECEIVER=FixedComplementaryDilationTwoSidedPrincipalRectangularReciprocalDivisorCRTSupportDeficitVersusConditionalRootCanonicalPostColumnCompletionDeficitWithCapacityHeadroomKappaMinusMu
WORK_BYX37_REVISIT_TRIGGER_4GE_REACHED=true
RECEIVER_MATERIALLY_CHANGED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
NEW_HEAVY_MAIN_H_NEEDED=false
NEXT=Stage14-4gf
```