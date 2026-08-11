# Stage14-s7-113 — two-level prefilter versus existential completion deficit ledger on all four s realizations

## Status

`COMPLETE_TWO_LEVEL_PRECOMPLETION_FILTER_AND_EXISTENTIAL_REVERSE_COMPLETION_DEFICIT_RECEIVER`

Consumes batch-local `Stage14-s7-111/112` and merged `Stage14-Work-byX37`.

```text
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 1. Uniform exponent ledger

Fix one already-charged heavy realization/cell from any of the four s branches. Write

```text
#S_amb  = B^(kappa+o(1)),
#S_pre  = B^(sigma+o(1)),
#S_phys = B^(tau+o(1)),
```

for the exact nested supports from s7-112,

```text
S_phys subseteq S_pre subseteq S_amb.
```

Define

```text
delta_pre := kappa-sigma >= 0,
delta_ext := sigma-tau >= 0.
```

These are cardinality-exponent differences on nested sets. Hence identically

```text
tau = kappa-delta_pre-delta_ext.                  (1)
```

Equation (1) is bookkeeping, not an independence assumption and not multiplication of separately proved probabilities.

A heavy survivor requires

```text
kappa-delta_pre-delta_ext >= mu.                  (2)
```

Equivalently the total physical deficit must obey

```text
delta_pre+delta_ext <= kappa-mu.                  (3)
```

```text
TWO_LEVEL_COMPLETION_DEFICIT_LEDGER_EXACT=true
PREFILTER_AND_EXTENSION_DEFICITS_INDEPENDENT_ASSUMED=false
HEAVY_SURVIVAL_LEDGER=kappa_minus_delta_pre_minus_delta_ext_ge_mu
```

## 2. Interpretation near and above capacity threshold

If a branch lies at near-threshold ambient capacity

```text
kappa=mu+o(1),
```

then any heavy survivor forces

```text
delta_pre=o(1),
delta_ext=o(1).
```

Thus both the deterministic reconstructed prefilter and the existential reverse/post-column completion support must be exponent-full on a surviving near-threshold sequence.

If instead

```text
kappa>=mu+eta
```

for fixed `eta>0`, a theorem need only beat the actual headroom `kappa-mu`; no branch-independent positive deficit is forced merely by survival.

This is exactly analogous to the capacity-headroom logic already merged in 4gb, now with the physical deficit opened into two quantifier layers.

```text
NEAR_THRESHOLD_SURVIVOR_FORCES_ZERO_PREFILTER_DEFICIT=true
NEAR_THRESHOLD_SURVIVOR_FORCES_ZERO_EXTENSION_DEFICIT=true
ABOVE_THRESHOLD_REQUIRED_SAVING_DEPENDS_ON_ACTUAL_HEADROOM=true
```

## 3. Apply the ledger to the four s realizations without multiplying branches

The four alternative heavy realizations become:

```text
(A) fixed-E primitive endpoint:
    reconstructed one-dimensional candidate support
    -> deterministic prefilter
    -> existential reverse/post-column completion;

(B) fixed-E two-sided principal rectangle:
    full-exponent rectangular/coprime candidate support
    -> deterministic prefilter
    -> existential reverse/post-column completion;

(C) polynomial-E fixed primitive product:
    reconstructed one-dimensional E support
    -> deterministic prefilter
    -> existential reverse/post-column completion;

(D) polynomial-E polynomial primitive product:
    full-exponent fibered candidate support
    -> deterministic prefilter
    -> existential reverse/post-column completion.
```

The ambient multiplication/product mechanisms in (B) and (D) are already exhausted by merged Work-byX37 and are not new terms in (2). The four branch supports are alternatives inside one charged heavy family and are not multiplied.

```text
S_BRANCH_DEFICITS_MULTIPLICABLE=false
AMBIENT_PRODUCT_COMPRESSION_RECHARGED=false
UNITARY_RECOVERY_RECHARGED=false
```

## 4. Material receiver change

The previous Work-byX37 language

```text
conditional physical completion/lift
```

is now opened to the exact two-level receiver

```text
DeterministicReconstructedPrecompletionFilterDeficit
VERSUS
ExistentialReversePostColumnPhysicalCompletionSupportDeficit
```

with branch-specific ambient headroom `kappa-mu` retained.

Accordingly the s heavy receiver is now

```text
FixedEEndpointPrecompletionFilterVersusExistentialReversePostColumnCompletionWithHeadroom
OR
FixedETwoSidedPrecompletionFilterVersusExistentialReversePostColumnCompletionWithHeadroom
OR
PolynomialEFixedProductPrecompletionFilterVersusExistentialReversePostColumnCompletionWithHeadroom
OR
PolynomialEPolynomialProductFiberedPrecompletionFilterVersusExistentialReversePostColumnCompletionWithHeadroom.
```

```text
CURRENT_S_RECEIVER=FixedEEndpointPrecompletionFilterVersusExistentialReversePostColumnCompletionWithHeadroom_OR_FixedETwoSidedPrecompletionFilterVersusExistentialReversePostColumnCompletionWithHeadroom_OR_PolynomialEFixedProductPrecompletionFilterVersusExistentialReversePostColumnCompletionWithHeadroom_OR_PolynomialEPolynomialProductFiberedPrecompletionFilterVersusExistentialReversePostColumnCompletionWithHeadroom
RECEIVER_MATERIALLY_CHANGED=true
```

## 5. H and Work decisions

No new sH is justified yet.

The extension witness family `R(chi)` is now isolated as an existence support, but its defining reverse/post-column equations have not yet been opened into a stable theorem contract. Likewise, `C_pre` is a deterministic Boolean but no merged result proves that all of its component predicates have `B^o(1)` distortion or a theorem-ready arithmetic form.

The next s-local task is therefore to open the actual reverse/post-column witness equations and, separately, identify which prefilter predicates are already forced/frozen versus genuinely moving arithmetic restrictions.

This stage reaches the `s7-113` component of merged Work-byX37's normal revisit condition.

```text
S7_113_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_H_NEEDED=false
WORK_BYX37_REVISIT_TRIGGER_S7_113_REACHED=true
NEXT=Stage14-s7-114
```

## Boundary

```text
STAGE14_S7_113=COMPLETE_TWO_LEVEL_PRECOMPLETION_FILTER_AND_EXISTENTIAL_REVERSE_COMPLETION_DEFICIT_RECEIVER
TWO_LEVEL_COMPLETION_DEFICIT_LEDGER_EXACT=true
HEAVY_SURVIVAL_LEDGER=kappa_minus_delta_pre_minus_delta_ext_ge_mu
NEAR_THRESHOLD_SURVIVOR_FORCES_ZERO_PREFILTER_DEFICIT=true
NEAR_THRESHOLD_SURVIVOR_FORCES_ZERO_EXTENSION_DEFICIT=true
WORK_BYX37_REVISIT_TRIGGER_S7_113_REACHED=true
RECEIVER_MATERIALLY_CHANGED=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_113_NEW_AUXILIARY_H_NEEDED=false
NEXT=Stage14-s7-114
```