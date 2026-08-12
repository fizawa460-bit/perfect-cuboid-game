# Stage15-6bc — weighted same-twist descent-cell second-moment gate

Base: Stage15-6bb. Audit verdict: `NEW_GATE`.

The previous stages have now removed three false continuations:

1. Petit almost-minimal height is not a whole-family consequence of the Stage15 product height (`6az`).
2. AR-012 does not trigger after clearing the moving rational denominator (`6ba`).
3. The denominator is exactly the already-counted primitive rational ratio on the degree-four quartic (`6bb`).

What remains can be stated without geometric ambiguity.

For each retained two-state packet:

- `d=sf(2*k*kappa)` is one squarefree congruent-number twist;
- `d` determines `k*kappa`, with only `B^o(1)` coprime splits and orientation/cell decorations;
- both states lie in the same rational complete-2-descent cell `[X]=1`, `[X-d]=[X+d]=[k]`;
- each state lies on the fixed-cell quartic

\[
\kappa_f^2c^4+\kappa_g^2e^4=kZ^2;
\]

- the two states are coupled by the exact physical product height

\[
kZW\le 2B.
\]

Stage15-6ao supplies a uniform pointwise degree-four bound for every fixed cell. What is missing is a whole-family estimate that sums the **pair multiplicity on the same twist/descent cell** without paying a polynomial number of norm cores/twists.

Freeze the required theorem/adapter species as

```text
UniformCongruentNumberTwist
Same2DescentCellWeightedRationalPointSecondMoment
UnderStage15ProductHeight
```

A usable statement must be every-family or carry an exceptional-set contribution strong enough for the Stage15 weight. Average rank, almost-all twists, or the Petit almost-minimal subfamily alone do not close it.

No new theorem is applied in this stage.

## Frozen exit

```text
STAGE15_6_SUBSTAGE=6bc
STAGE15_6BC_AUDIT=true
STAGE15_6BC_AUDIT_VERDICT=NEW_GATE
STAGE15_6BC_PETIT_WHOLE_FAMILY_ROUTE_BLOCKED=true
STAGE15_6BC_AR012_ROUTE_BLOCKED=true
STAGE15_6BC_FIXED_CELL_POINTWISE_QUARTIC_BOUND_AVAILABLE=true
STAGE15_6BC_TWIST_DETERMINES_k_times_kappa=true
STAGE15_6BC_WEIGHTED_SAME_TWIST_SECOND_MOMENT_PROVED=false
STAGE15_6BC_GLOBAL_NORM_CORE_AGGREGATION_PROVED=false
STAGE15_6BC_CAUSAL_HALF_POWER_REDERIVED=false
STAGE15_6BC_EXIT=WEIGHTED_SAME_TWIST_DESCENT_CELL_SECOND_MOMENT_THEOREM_GATE
```
