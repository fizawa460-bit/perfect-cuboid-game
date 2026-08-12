# Stage15-6-cycle — 6az through 6bc

Base: merged PR #849.

## Audit ledger

```text
6az  Petit complete-2-descent small-height size implication   BLOCK
6ba  AR-012 reverse divisor reconstruction trigger            BLOCK
6bb  minimal rational reciprocal receiver                     PASS
6bc  weighted same-twist descent-cell second moment           NEW_GATE
```

## Cycle path

### 6az
The exact complete descent does not force every physical Stage15 point into Petit's almost-minimal-height subfamily. Product height controls the two-state product but not the individual descent height. Petit remains valid mathematics but is not applied to the whole Stage15 population.

### 6ba
The equations `U^2-kV_-^2=d`, `U^2-kV_+^2=-d` are rational. Clearing the common denominator introduces the moving square `T^2`, so AR-012's fixed-right-hand-side divisor reconstruction does not trigger.

### 6bb
Using `f=kappa_f*c^2`, `g=kappa_g*e^2`, `T=ce`, the moving denominator is exactly one primitive ratio `c/e` and

\[
(V_++V_-)(V_+-V_-)=4\kappa/\lambda^2.
\]

The remaining equation is the already-counted quartic

\[
\kappa_f^2c^4+\kappa_g^2e^4=kZ^2.
\]

No fresh AR-010 saving is charged.

### 6bc
After the two blocked shortcuts, the remaining family is exact:

```text
same twist d=sf(2*k*kappa)
same 2-descent cell k
B^o(1) splits/decorations per d
one uniform degree-4 pointwise bound per fixed cell
two rational quartic states coupled by k*Z*W <= 2B
```

The unresolved theorem species is

```text
UniformCongruentNumberTwist
Same2DescentCellWeightedRationalPointSecondMoment
UnderStage15ProductHeight
```

## Frozen cycle exit

```text
STAGE15_6_CYCLE_START=6az
STAGE15_6_CYCLE_END=6bc
STAGE15_6_CYCLE_AUDIT_LEDGER=BLOCK,BLOCK,PASS,NEW_GATE
STAGE15_6_CYCLE_PETIT_WHOLE_FAMILY_ROUTE_BLOCKED=true
STAGE15_6_CYCLE_AR012_FALSE_TRIGGER_BLOCKED=true
STAGE15_6_CYCLE_RATIONAL_RATIO_RECEIVER_MINIMAL=true
STAGE15_6_CYCLE_FIXED_CELL_POINTWISE_QUARTIC_BOUND_AVAILABLE=true
STAGE15_6_CYCLE_WEIGHTED_SAME_TWIST_SECOND_MOMENT_PROVED=false
STAGE15_6_CYCLE_GLOBAL_NORM_CORE_AGGREGATION_PROVED=false
STAGE15_6_CYCLE_CAUSAL_HALF_POWER_REDERIVED=false
STAGE15_6_CYCLE_EXIT=WEIGHTED_SAME_TWIST_DESCENT_CELL_SECOND_MOMENT_THEOREM_GATE
```

Next continuation must audit or prove this exact weighted second-moment species. Do not restart Petit small-height or AR-012 without a new exact adapter.
