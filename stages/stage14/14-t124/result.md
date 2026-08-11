# Stage14-t124 — discharge the finite D4-boundary atomic branch and isolate selected-class depletion

## Status

`COMPLETE_FINITE_D4_BOUNDARY_ATOMIC_BRANCH_DISCHARGE`

Consumes merged Stage14-t123, merged Stage14-t74/t89/t122, and merged Stage14-Work-bpX28 on latest merged main.

Fix the t123 exceptional packet and write

```text
H = sum_{g in G_amb} A_m(g),
B_bd={g in G_amb : k0*m*g in {1,2}},
H_bd=sum_{g in B_bd} A_m(g),
H_nb=H-H_bd.
```

Merged t122 shows that the only possible failure of the finite Gaussian sign/canonical normalization lies on the D4 boundary. Merged t74 gives the exact physical short-cover chamber

```text
r=q-p,
t=q+p,
0<r<t.
```

Hence every actual physical cover satisfies

```text
q>p>0,
```

so neither an axis point nor a diagonal point can itself contribute to the physical count. The D4-boundary atoms are therefore rejected atoms of the ambient principal measure, exactly as required by the t123 support-complement interpretation.

Let `T` denote the full selected physical prime count for this fixed packet. Split the proof target by the ambient boundary mass.

For any fixed `delta>0`, choose a fixed `theta` with

```text
0<theta<delta.
```

### Boundary-heavy packet

If

```text
H_nb <= B^(-theta+o(1)) H,
```

then the actual count is supported only on nonboundary norms. The projective class family, primitive-orientation fiber and all remaining finite/divisor labels have total multiplicity `B^o(1)`, so the charged-once trivial prime bound gives

```text
T <= B^o(1) H_nb
  <= B^(-theta+o(1)) H.
```

Thus a boundary-heavy packet is already a valid fixed-power core-saving packet. No theorem about the atomic boundary weight is needed.

### Boundary-light packet

Otherwise

```text
H_nb > B^(-theta+o(1)) H.
```

The nonboundary principal mass is polynomially comparable to the original charged baseline. If one still seeks the original target

```text
T <= B^(-delta+o(1)) H,
```

then necessarily

```text
T <= B^(-(delta-theta)+o(1)) H_nb.
```

Since `delta-theta>0`, a fixed positive power is retained after replacing the baseline by `H_nb`.

Merged t122 gives a physical sign/canonical representative on every nonboundary primitive orbit. Therefore the ell-independent support mechanism can no longer furnish an independent fixed positive power loss on this normalized family. Any remaining fixed-power saving must come from the other t114/t123 mechanism:

```text
PhysicalSelectedProjectiveClassNearTotalPrimeDepletion
```

with the exact cofactor-dependent prime interval, selected projective class, fixed packet data and charged-once rules retained.

Therefore the finite-boundary atomic concentration from t123/Work-bpX28 is not a separate live theorem receiver. It is a proof-case split:

```text
boundary-heavy -> already closed by core support loss;
boundary-light -> normalize to H_nb and pass to selected-class depletion.
```

This materially changes the minimal fixed-U receiver to the selected-projective-class depletion problem on the nonboundary physical cofactor family.

No new tH is needed yet. Merged tH26 and tH28 remain the relevant negative boundaries for generic Hecke/projective equidistribution and unmasked projected-norm sieves. The next internal stage should freeze the exact nonboundary cofactor-to-projective-class map together with its prime interval and determine whether the depletion condition has further deterministic structure before opening tH29.

```text
D4_BOUNDARY_ATOMS_CONTRIBUTE_TO_ACTUAL_PHYSICAL_COUNT=false
BOUNDARY_HEAVY_PACKET_CORE_SAVING_CLOSED=true
BOUNDARY_LIGHT_PACKET_NONBOUNDARY_BASELINE_POLYNOMIALLY_COMPARABLE=true
BOUNDARY_LIGHT_TARGET_RETAINS_FIXED_POSITIVE_POWER=true
FINITE_BOUNDARY_ATOMIC_CONCENTRATION_AS_SEPARATE_RECEIVER_SUPERSEDED=true
SELECTED_CLASS_NEAR_TOTAL_DEPLETION_IS_ONLY_LIVE_FIXED_U_MECHANISM=true
RECEIVER_MATERIALLY_CHANGED=true
FIXED_U_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
TH29_NEEDED=false
PREFERRED_RECEIVER=SharedUNonboundaryPhysicalCofactorSelectedProjectiveClassNearTotalPrimeDepletion
NEXT_INTERNAL_TARGET=NonboundaryCofactorSelectedProjectiveClassMapAndPrimeIntervalFreezing
NEXT=Stage14-t125
```
