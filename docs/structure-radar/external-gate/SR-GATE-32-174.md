# StructureRadar external-gate closure 32 — SR-STR-174 q17-good correlation reconciliation

BATCH_ID=SR-BATCH-EXTERNAL_GATE_CLOSURE-32-R01
PHASE=EXTERNAL_GATE_CLOSURE
STRUCTURE=SR-STR-174
MODE=ONE_GATE_DEEP_ATTACK
GATE_BEFORE=EXTERNAL_GATE
GATE_AFTER=EXTERNAL_GATE
EXTERNAL_GATE_COUNT_BEFORE=13
EXTERNAL_GATE_COUNT_AFTER=13

This batch attacks the next Stage27-20 supporting gate after merged batches30-31. The old SR-STR-174 wording asked for an exact same-measure q17-good/pushforward indicator-correlation lower bound on every principal cell. The merged Stage14 q21-q23 chain shows that this is stronger than the actual structural requirement and identifies a smaller nonnegative first-moment receiver.

## 1. Merged q17-good indicator reduction

Merged Stage14-s7-144..146 proves, on its charged s-route measure, that the q17-good intersection is exactly encoded by

```text
M1_G = sum_lambda 1_G(pi(lambda))
     = sum_{theta in G} a(theta).
```

The associated second moment satisfies

```text
M2_G <= B^o(1) M1_G,
```

so hit support and first moment are fixed-power equivalent. A second collision/dispersion estimate may not be recharged merely to recover the same hit support.

Merged Stage14-s7-147..149 then replaces the Boolean good indicator by the nonnegative q17 reciprocal-CRT witness count `N_G` with

```text
1_G <= N_G <= B^o(1) 1_G,
```

and unfolds the witness first moment exactly into the joint filtered-tau3 / q17 reciprocal-CRT incidence normal form, retaining the scalar and polynomial `(E,m)` charged measures separately and keeping the residual root/canonical/post-column mask separate.

Thus the Stage14 theorem-ready receiver is not an abstract every-cell indicator-correlation theorem. It is a positive joint-incidence first moment with bounded witness multiplicity.

```text
GOOD_INDICATOR_FIRST_MOMENT_ENCODING_PROVED=true
GOOD_INDICATOR_SECOND_MOMENT_AUTOCONTROL_PROVED=true
GOOD_INDICATOR_TO_NONNEGATIVE_Q17_WITNESS_EQUIVALENCE_PROVED=true
JOINT_FILTERED_TAU3_Q17_RECIPROCAL_CRT_INCIDENCE_NORMAL_FORM_PROVED=true
SECOND_MOMENT_RECHARGE_FORBIDDEN=true
```

## 2. Why every-principal-cell correlation is unnecessarily strong

The current Stage27-20 r302 route permits a weighted exceptional-wall-mass conclusion: it is enough to show that high-occupancy MAIN wall slabs carry a fixed-power-small portion of the charged `H_phys^MAIN` mass. Batch30 already rewrites that requirement as a same-MAIN-measure weighted L2/two-copy problem.

Therefore SR-STR-174 need not demand a positive q17-good indicator lower bound on every principal cell. A sufficient supporting statement is an aggregate weighted q17-witness first-moment theorem on the retained high-occupancy MAIN wall mass, provided it is proved in the same `H_phys^MAIN` measure and preserves the physical conditioning.

This is a weakening of the required quantifier, not a theorem claim. No Stage14 s-route lower bound is cross-promoted to MAIN.

## 3. New exact missing adapter

The smallest surviving bridge is

```text
FIRST_MISSING_LEMMA=MAINWallWeightedQ17GoodWitnessJointIncidenceExceptionalMassAdapter
```

A sufficient form is:

> On the retained fixed-width Stage27 MAIN wall dyadic/decorative blocks, identify the q17-good factor inside the exact `H_phys^MAIN` centered/two-copy survivor coefficient with a nonnegative reciprocal-CRT witness count of `B^o(1)` multiplicity, unfold its weighted first moment into the joint filtered-tau3 / q17 reciprocal-CRT incidence normal form, and prove the resulting aggregate exceptional-mass estimate while preserving all physical masks, the correlated modulus/common-parent quantifier order, and coefficient energy. No per-cell lower bound is required if the weighted exceptional-mass conclusion is obtained.

The first two clauses are proved only on the merged Stage14 s-route charged measure. Their transport to `H_phys^MAIN`, and the final fixed-power aggregate estimate there, remain unproved.

## 4. Relation to batches30-31

Batch30 leaves

```text
MAINWallPhysicalCenteredFrequencyToKloostermanFractionTransfer
```

as the exact analytic transform gate for SR-STR-169.

Batch31 leaves

```text
MAINWallPhysicalSelectorCanonicalCorrelationDecompositionAdapter
```

as the selector-side same-measure transport gate for SR-STR-167.

This batch narrows the q17-good supporting branch to one nonnegative weighted joint-incidence adapter. These are complementary gates; they are not independent savings and may not be multiplied.

If the batch31 selector adapter exposes the q17-good branch inside MAIN, the present witness reduction is the canonical next normalization before testing any divisor/AP/dispersion theorem. Conversely, a theorem on the Stage14 s-route witness first moment alone does not close the MAIN receiver.

## 5. External-literature status

No broad literature sweep is repeated here. Merged Work-ciX47/q21, Work-cjX48/q22 and Work-ckX49/q23 already record that the closest AP/divisor architectures do not directly preserve the filtered-tau3 conditioning, witness-dependent reciprocal-CRT predicates, and both charged measures. This batch is a repo-reconciliation/proof-reduction step, not a novelty-by-search-absence claim.

## 6. Firewalls and verdict

- `SR-STR-174` remains `EXTERNAL_GATE`.
- No Stage14 s-route density theorem is cross-promoted to `H_phys^MAIN`.
- The every-principal-cell requirement is superseded only as a restart target; no MAIN weighted exceptional-mass theorem is claimed proved.
- Good-indicator support, witness multiplicity, second moment, and post-mask are charged once.
- Batch30 and batch31 savings, if later proved, are not multiplied without an exact common-measure argument.
- `CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2`.
- `STRICT_SUBSQRT_POWER_SAVING_PROVED=false`.
- No perfect-cuboid existence/nonexistence claim is made.

```text
OLD_EVERY_CELL_GATE_SUPERSEDED_AS_RESTART_POINT=true
Q17_NONNEGATIVE_WITNESS_NORMAL_FORM_REUSED=true
MAIN_WEIGHTED_EXCEPTIONAL_MASS_ADAPTER_PROVED=false
FIRST_MISSING_LEMMA=MAINWallWeightedQ17GoodWitnessJointIncidenceExceptionalMassAdapter
SR_STR_174_STATUS=EXTERNAL_GATE
GATES_CLOSED=0
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=StructureRadar-audit
```
