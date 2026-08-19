# StructureRadar external-gate closure 31 — SR-STR-167 physical-selector decomposition reconciliation

BATCH_ID=SR-BATCH-EXTERNAL_GATE_CLOSURE-31-R01
PHASE=EXTERNAL_GATE_CLOSURE
STRUCTURE=SR-STR-167
MODE=ONE_GATE_DEEP_ATTACK
GATE_BEFORE=EXTERNAL_GATE
GATE_AFTER=EXTERNAL_GATE
EXTERNAL_GATE_COUNT_BEFORE=13
EXTERNAL_GATE_COUNT_AFTER=13

This batch attacks the supporting Stage27-20 gate `SR-STR-167` after audited batch30 reduced `SR-STR-169` to the exact MAIN nonzero-frequency covariance bridge. The purpose is not to force a nonexistent full multiplicative factorization of the physical selector. Instead it reconciles the old broad gap against later merged Stage14 reductions and identifies the smallest same-measure adapter still missing for the current MAIN receiver.

## 1. The old broad gap is no longer the correct restart point

`SR-STR-167` was classified as `EXTERNAL_GATE` because the actual physical selector had no proved bounded-complexity multiplicative / Gaussian-Hecke phase decomposition. The merged Stage14 chain sharpens this substantially:

- `Stage14-s7-58`: the Gaussian/root-orientation component has a Walsh/Hecke expansion with `2^omega(C_*)=B^o(1)` phases and coefficient `l1` cost 1; finite gcd/primitivity admits Mobius expansion, while the full selector is explicitly nonmultiplicative.
- `Stage14-s7-59`: the positive physical uplift is an exact `O(1)` martingale telescoping sum of mask-level influences: orientation, gcd/Mobius, balanced allocation, range/separation, charged-once chart, reciprocal completion.
- `Stage14-s7-60..64`: balanced allocation and reciprocal completion are shown to share one charged packet, single-prime influence is localized, fresh residue sparsity is exhausted, and the range-stable arithmetic branch collapses to one Boolean primitive-slope physical acceptance predicate rather than an independent product of densities.
- `Stage14-s7-65..71` and mainline `4dz..4ef`: the Boolean acceptance is decomposed through its actual primitive integer/Gaussian allocation witnesses; the first reciprocal equation becomes a reconstructed identity, and the remaining reciprocal arithmetic is primitive Gaussian norm divisibility on a charged-once candidate fiber.
- `Stage14-sH71`, `s7-72..74`, and `4eg..4ek`: common-core scale stratification yields the canonical correlation-only boundary. Small common core returns to canonical balanced integer/Gaussian three-divisor correlation; polynomial common core has power-small principal Gaussian root density and can saturate only through centered Gaussian root discrepancy, which after character expansion becomes concentrated exact-modulus projective collision energy or diffuse variable-modulus canonical-allocation norm-divisor-graph discrepancy.

Therefore the repo already proves a bounded **structural selector decomposition/no-go**: the physical selector is not globally multiplicative, but it decomposes into finitely many charged-once mask influences and then into exact canonical correlation receivers. Requiring a full Hecke factorization of every physical mask is unnecessarily strong and is not the correct current gate.

```text
FULL_PHYSICAL_SELECTOR_HECKE_FACTORIZATION_PROVED=false
BOUNDED_MASK_INFLUENCE_DECOMPOSITION_PROVED=true
CANONICAL_CORRELATION_ONLY_REDUCTION_PROVED=true
GENERIC_BALANCED_DIVISOR_STANDALONE_SAVING_FORBIDDEN=true
RECIPROCAL_COMPLETION_DOUBLE_CHARGE_FORBIDDEN=true
```

## 2. Exact surviving correlation receivers in the merged Stage14 measure

The merged Stage14 decomposition leaves the physical selector in the following charged-once alternatives:

```text
LOW COMMON CORE:
  CanonicalBalancedIntegerGaussianThreeDivisorCorrelationDensity

POLYNOMIAL COMMON CORE / CONCENTRATED EXACT MODULUS:
  ConcentratedExactCommonCoreProjectiveCollisionEnergy

POLYNOMIAL COMMON CORE / DIFFUSE MODULUS:
  DiffusePolynomialCommonCoreCanonicalAllocationNormDivisorGraphDiscrepancy
```

These are not three independent savings. They are branches of one physical acceptance decomposition. The principal Gaussian root mode on fixed positive common-core exponent is already power-small; saturation is carried by the centered discrepancy branch. On subpolynomial common core, the obstruction returns to the canonical allocation correlation rather than yielding a new local density factor.

## 3. Relation to the batch30 MAIN receiver

Batch30 works in the exact Stage27 MAIN wall measure

```text
H_x = H_phys^MAIN(P,U;B)
```

and reduces the high-occupancy theorem to the nonzero-frequency two-copy covariance of the frozen MAIN survivor indicator. The Stage14 selector reductions above are canonical structural theorem sources, but they cannot simply be cross-promoted into `H_phys^MAIN`: the current MAIN wall packet has its own conditioning and normalization, and the post-close firewall forbids changing measure or recharging already-counted local/root factors.

The smallest missing bridge is therefore:

```text
FIRST_MISSING_LEMMA=MAINWallPhysicalSelectorCanonicalCorrelationDecompositionAdapter
```

A sufficient form is:

> On each retained fixed-width Stage27 MAIN wall dyadic/decorative block, decompose the exact centered/nonzero-frequency `H_phys^MAIN` survivor coefficient into `B^o(1)` charged-once pieces matching the merged Stage14 canonical correlation receivers above, with coefficient `L1/L2` energies dominated by the original MAIN physical energy, all range/separation/chart/primitive/nested-divisor masks retained, and no change in the correlated modulus quantifier order.

If this adapter is proved, the batch30 transfer problem no longer starts from an opaque full physical selector. The concentrated polynomial-core piece can be tested against Kloosterman/projective-collision machinery, while the diffuse and low-core pieces retain their own exact correlation receivers. No branch may be replaced by a different-measure average or multiplied by another branch's saving.

## 4. Why this is progress but not closure

The repo-native Stage14 chain proves that the old demand for a global multiplicative/Hecke factorization was too coarse. It also supplies the exact finite structural decomposition and the canonical arithmetic receivers. What remains unproved is the **same-MAIN-measure transport of that decomposition with coefficient norms**. That is precisely the ingredient needed before batch30's Kloosterman-fraction transfer can be applied safely.

No new external literature sweep is needed for this reconciliation batch. The already-audited batch30 Work fallback remains focused on `MAINWallPhysicalCenteredFrequencyToKloostermanFractionTransfer`; this batch narrows the selector side that such a transfer must preserve.

## 5. Firewalls and verdict

- `SR-STR-167` remains `EXTERNAL_GATE`.
- No claim is made that the full physical selector is multiplicative.
- The Stage14 decomposition is reused only as a structural theorem source; no fixed-U/T-route or different-measure saving is promoted to `H_phys^MAIN`.
- Branch alternatives are not multiplied as independent density savings.
- `CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2`.
- `STRICT_SUBSQRT_POWER_SAVING_PROVED=false`.
- No perfect-cuboid existence/nonexistence claim is made.

```text
OLD_BROAD_GATE_SUPERSEDED_AS_RESTART_POINT=true
BOUNDED_MASK_INFLUENCE_DECOMPOSITION_PROVED=true
CANONICAL_CORRELATION_RECEIVERS_IDENTIFIED=true
MAIN_MEASURE_ADAPTER_PROVED=false
FIRST_MISSING_LEMMA=MAINWallPhysicalSelectorCanonicalCorrelationDecompositionAdapter
SR_STR_167_STATUS=EXTERNAL_GATE
GATES_CLOSED=0
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=StructureRadar-audit
```
