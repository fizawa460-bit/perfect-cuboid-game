# Stage14-4fj — interior reciprocal-window occupancy to physical squareclass-divisor incidence

## Status

`COMPLETE_INTERIOR_RECIPROCAL_WINDOW_OCCUPANCY_TO_PHYSICAL_DIVISOR_INCIDENCE`

Consumes batch-local `Stage14-4fh/4fi`, merged `Stage14-4fg`, merged `Stage14-s7-89`, and merged `Stage14-Work-brX30`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Endpoint branch has been removed

Fix one exponent cell

```text
n=B^(nu+o(1)),
|N_*|>=B^(mu-o(1)),
0<mu<=nu<=rho-delta,
rho=1/4-phi<=1/24.
```

Choose

```text
theta>nu-mu
```

as in 4fi. The two radial endpoint strips contain only `o(B^mu)` integers, so a surviving heavy ray has an interior set

```text
N_int(theta)
```

with

```text
|N_int(theta)|>=B^(mu-o(1)).
```

For each `n in N_int(theta)`, the exact geometric reciprocal L-window `W(n)` has logarithmic width at least

```text
B^(-theta+o(1)).
```

## 2. Keep the full physical candidate predicate

For fixed `n`, define the charged candidate set

```text
C(n)
 := {L:
      sqrt(sqf(L)*L) | c0*n,
      gcd(sqf(L),K_Z)=1,
      L in W(n)}.
```

Define the residual physical Boolean

```text
w_phys(n,L) in {0,1}
```

to retain every transported mask not already represented by the two root-size windows, including the primitive/gcd, canonical orientation, reverse-completion, parity/two-primary, and frozen chart conditions.

Then the interior accepted-radial selector is exactly

```text
A_int(n)
 = 1_{ exists L in C(n) with w_phys(n,L)=1 }.
```

No independence between `C(n)` and `w_phys` is assumed.

```text
FULL_TRANSPORTED_PHYSICAL_WEIGHT_RETAINED=true
PHYSICAL_MASK_INDEPENDENCE_ASSUMED=false
```

## 3. Existential support and incidence mass are exponent-equivalent

Merged 4fg and brX30 give uniformly on the polynomial Stage14 range

```text
#C(n)=B^o(1).
```

Define the physical interior incidence count

```text
I_int
 := sum_{n in N_int(theta)}
      sum_{L in C(n)} w_phys(n,L).
```

Pointwise,

```text
A_int(n)
 <= sum_{L in C(n)} w_phys(n,L)
 <= #C(n)*A_int(n).
```

Therefore

```text
sum_n A_int(n)
 <= I_int
 <= B^o(1) * sum_n A_int(n).
```

Thus the existential accepted-`n` support and the charged physical `(n,L)` incidence count have the same fixed-power exponent. In particular a surviving heavy ray forces

```text
I_int >= B^(mu-o(1)).
```

This conversion uses the fixed-`n` fiber exactly once; it is not an additional saving.

```text
INTERIOR_EXISTENTIAL_SUPPORT_INCIDENCE_EXPONENT_EQUIVALENT=true
INTERIOR_PHYSICAL_INCIDENCE_REQUIRED_EXPONENT=mu
FIXED_N_L_FIBER_USED_ONCE=true
```

## 4. Minimal heavy receiver

The global heavy branch is no longer most naturally an opaque existence density. After endpoint removal and finite-fiber conversion it is the explicit incidence problem

```text
sum_{n~B^nu}
sum_{
  L squareclass-admissible,
  L in W(n),
  log-width W(n)>=B^(-theta+o(1))
}
  w_phys(n,L),
```

with

```text
theta>nu-mu,
I_int>=B^(mu-o(1)).
```

The same reciprocal `(n,L)` coordinate is the merged s-route coordinate by brX30, but no s count is multiplied and no fixed-U prime/projective measure is imported.

The new minimal heavy receiver is

```text
FixedPrimitiveRayFixedAgreementPairInteriorShortReciprocalSquareclassDivisorPhysicalIncidence
WithMassExponentMuAndWindowExponentThetaGreaterThanNuMinusMu.
```

This is a material receiver change.

```text
CURRENT_HEAVY_RAY_RECEIVER=FixedPrimitiveRayFixedAgreementPairInteriorShortReciprocalSquareclassDivisorPhysicalIncidenceWithMassExponentMuAndWindowExponentThetaGreaterThanNuMinusMu
RECEIVER_MATERIALLY_CHANGED=true
```

## 5. H decision

No new heavy-ray H audit is opened yet. The arithmetic incidence is theorem-shaped, but the coefficient sequence `w_phys(n,L)` still bundles the canonical/reverse-completion masks. Applying a generic short-divisor theorem before opening that weight would repeat the same mask-preservation error already recorded by earlier H audits.

The next internal mainline stage should decompose `w_phys(n,L)` into the part already forced by `(n,L)` and the genuinely residual physical Boolean/correlation. Only then should a new heavy-ray H target be frozen if a standard theorem contract exists.

Existing non-heavy mainline H gates remain pending and unchanged.

```text
NEW_HEAVY_MAIN_H_NEEDED=false
EXISTING_NONHEAVY_MAIN_H_GATES_PENDING=true
MAIN_ROUTE_H_NEEDED=false
MAIN_ROUTE_H_REQUEST=NONE
MAIN_ROUTE_H_TARGET=NONE
MAIN_ROUTE_H_BLOCKING=false
NEXT=Stage14-4fk
```
