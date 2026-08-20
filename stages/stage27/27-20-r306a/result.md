# Stage27-20-r306a — materialize the balanced-wall core-scale dichotomy

STATUS=SUBMITTED_PENDING_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_BALANCED_WALL_CORE_DICHOTOMY
PARENT_ROUTE=Stage27-20-r306

The audited wall structure leaves two genuinely different ways to obtain a fixed power without reopening frozen r302:

1. polynomial large-core forcing on all half-power-saturating wall mass;
2. fixed-power sparsity of the complementary low-core population.

Fix a small constant kappa>0 and split the balanced wall packet population P_wall into

P_hi(kappa)={p in P_wall : Q_core(p)>=B^kappa},
P_lo(kappa)={p in P_wall : every legally available charged core/root-line modulus is <B^kappa}.

On P_hi, the already-audited primitive root-line spacing attached to the charged core is allowed exactly once. Thus this branch can contribute a B^{-kappa+o(1)}-scale loss, subject to the existing Stage14/15 packet-count and mask ledger. No second root-line factor is charged.

Therefore the new theorem burden may be placed entirely on P_lo:

MAINWallLowCoreSparsity(kappa):
  |P_lo(kappa)| <= B^(1/2-delta+o(1))

for some fixed kappa,delta>0.

Conversely, if one proves that all half-power-saturating wall packets lie in P_hi(kappa), then the high-core branch itself crosses the wall using the existing one-time spacing factor.

This turns the qualitative Stage27-40ac alternatives into one exact cutoff theorem: prove either P_lo is fixed-power sparse or P_hi contains all saturation mass.

No strict sub-square-root bound is asserted yet.

CORE_SCALE_SPLIT_MATERIALIZED=true
HIGH_CORE_EXISTING_SPACING_REUSABLE_ONCE=true
LOW_CORE_FIXED_POWER_SPARSITY_PROVED=false
LARGE_CORE_FORCING_PROVED=false
R302_REOPENED=false
NEXT_DERIVED_ROUTE=27-20-r306b
ADVANCE_TO_CHECKPOINT50=false
STRICT_SUB_SQRT_UPPER_PROVED=false
