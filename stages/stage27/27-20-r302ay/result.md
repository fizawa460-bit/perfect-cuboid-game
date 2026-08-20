# Stage27-20-r302ay — one same-measure weighted collision-moment theorem suffices

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_MAIN_HIGH_OCCUPANCY
PARENT_ROUTE=Stage27-20-r302ax
SOURCE_STAGE=Stage20

R302ax defines the nonnegative packet statistic

```text
Z(W,C)
 = s_q(C)^3
   * [sum_f |W(f)|^4]
     / [sum_f |W(f)|^2]^2,
```

with `Z=0` when the denominator vanishes, and proves that a packet with

```text
Z(W,C) <= B^{-2kappa}
```

has local quadratic-root selector deficit `B^{-kappa+o(1)}`.

This converts the remaining problem to an aggregate moment theorem rather than an every-packet theorem.

Let `H_packet` denote the exact disintegration of the already-charged `H_phys^MAIN` wall measure used throughout r302d-h. Suppose that for some fixed `gamma>0`,

```text
sum_packet H_packet Z(W,C)
 <= B^{-gamma+o(1)}
    sum_packet H_packet.
```

Fix `0<kappa<gamma/2` and define

```text
Bad = {packet : Z(W,C)>B^{-2kappa}}.
```

Markov on the **same physical measure** gives

```text
sum_{Bad} H_packet
 <= B^{-(gamma-2kappa)+o(1)}
    sum_packet H_packet.
```

On the complementary good packets, r302ax gives a deterministic arithmetic power `B^{-kappa+o(1)}`. On the bad packets, monotonicity `F_MAIN<=H_phys^MAIN` absorbs their contribution. Hence r302d/h yield a positive same-measure occupancy deficit with exponent

```text
min(kappa, gamma-2kappa)>0.
```

Choosing `kappa=gamma/3` balances the two terms and gives `gamma/3` before the already-recorded later exponent losses.

Thus the current checkpoint40 MAIN route has been reduced to one concrete positive theorem:

```text
FIRST_MISSING_LEMMA=
MAINWallSingularityWeightedResidueFourthMomentCollisionDeficit
```

A sufficient statement is exactly the weighted `Z`-mean inequality above, uniformly for the retained fixed-width wall and frozen masks.

This theorem is strictly coefficient-specific and same-measure. It does not require arbitrary `c`, every-packet equidistribution, or a separate off-diagonal Kloosterman fixed-power theorem.

SR-STR-173 supplies the correct support/moment and no-scalarization firewall, but the repository does not currently prove that its existing witness moments equal this `W`-residue fourth moment with the singularity factor `s_q(C)^3`. That identification/theorem remains the new mathematical input.

```text
STAGE27_20_R302AY_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
WEIGHTED_Z_MEAN_IMPLIES_BAD_PACKET_EXCEPTIONAL_MASS=true
GOOD_BAD_PACKET_CLOSURE_PROVED=true
BALANCED_KAPPA_EQUALS_GAMMA_OVER_3=true
ONE_FIXED_POWER_THEOREM_SUFFICIENT=true
ARBITRARY_COEFFICIENT_OPERATOR_THEOREM_REQUIRED=false
SEPARATE_OFFDIAGONAL_FIXED_POWER_REQUIRED=false
SINGULARITY_WEIGHTED_RESIDUE_FOURTH_MOMENT_DEFICIT_PROVED=false
MAIN_ARITHMETIC_HOST_CORRELATION_POWER_DEFICIT_PROVED=false
WALL_SLAB_AGGREGATE_DEFICIT_THEOREM_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
CURRENT_CHECKPOINT=40
ADVANCE_TO_CHECKPOINT50=false
NEXT_DERIVED_ROUTE=27-20-r302az
NEXT_BATCH=Stage27-20-r302-main-batch
```