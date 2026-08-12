# Stage15-6-cycle — 6bl through 6bo

Base: merged PR #852 (`5a677730`).

## Visible audit ledger

```text
6bl  joint outer/inner actual-core rootline index     PASS
6bm  physical toric congruence-neighbourhood adapter PASS
6bn  Huang effective-uniformity promotion            BLOCK
6bo  hybrid 3/4 exponent interface                    NEW_GATE
```

The cycle returns to the original moving S/O core but changes the global-charge formulation: the actual core defines one codimension-two product congruence locus of local density `q^-2`, rather than an outer-conditioned `q^-1` partner count.

The existing fixed-core quartic estimate controls `q<=Q` by `B^(5/8+o(1))*Q^(1/2)`. A legal aggregate toric estimate `B^(1+o(1))/Q` for `q>Q` would balance at `Q=B^(1/4)` and yield a first self-contained causal exponent `3/4`.

Huang arXiv:2111.01509v3 is the correct effective-equidistribution theorem species, but this cycle does not certify that its explicit error term is uniform enough through the required polynomial modulus window. That quantitative extraction is the next exact gate.

```text
STAGE15_6_CYCLE_START=6bl
STAGE15_6_CYCLE_END=6bo
STAGE15_6_CYCLE_AUDIT_LEDGER=PASS,PASS,BLOCK,NEW_GATE
STAGE15_6_CYCLE_JOINT_ACTUAL_CORE_INDEX=q^2
STAGE15_6_CYCLE_TORIC_ADELIC_ADAPTER=true
STAGE15_6_CYCLE_HUANG_THEOREM_SPECIES_MATCH=true
STAGE15_6_CYCLE_HUANG_B14_WINDOW_CERTIFIED=false
STAGE15_6_CYCLE_CONDITIONAL_CAUSAL_EXPONENT=3/4
STAGE15_6_CYCLE_UNCONDITIONAL_CAUSAL_3_4_PROVED=false
STAGE15_6_CYCLE_CAUSAL_HALF_POWER_REDERIVED=false
STAGE15_6_CYCLE_EXIT=UNIFORM_TORIC_CONGRUENCE_WINDOW_FOR_CAUSAL_THREE_QUARTERS
```