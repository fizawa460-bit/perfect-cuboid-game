# Stage25-10 discovery ledger

CHECKPOINT=10
STATUS=COMPLETE_PENDING_FRESH_AUDIT
STAGE=Stage25
TRANSITION=Stage16->Stage19

## Search modes executed

```text
DIRECT_TERMS=Stage16 Stage19 M1 N2 combined thinning
SYNONYMS_NOTATION=exactly-one exactly-two space diagonal adjacent-stratum population ratio
STRUCTURAL_SIGNATURES=two-path square Stage16-Stage17-Stage18-Stage19; endpoint quotient factorization
DEPENDENCY_NEIGHBORS=Stage21 Stage22 Stage23 Stage24 Stage16S Stage14-num
```

## Strongest interfaces found

### S25-10-A — source upgrade

Stage16 final proves `M1(B) asymp B^2 log B`, but audited Stage21 imports the stronger exact asymptotic on the literal same source population:

\[
M_1(B)\sim\frac{3}{4\pi^2}B^2\log B.
\]

Verdict: `PROMOTE_STRONGER_FROZEN_SOURCE_INTERFACE`.

### S25-10-B — target supersession

Historical Stage19 had only the finite lower floor. Audited Stage24-50 supersedes the current lower interface with

\[
N_2(B)\gg\sqrt{\log B}
\]

and unboundedness/infinite primitive construction, while preserving the upper

\[
N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.
\]

Verdict: `USE_POST_STAGE24_CURRENT_TARGET_INTERFACE`.

### S25-10-C — both intermediate paths are fully audited

Path A: `M1 -> M2 -> N2` uses Stage22 then Stage24.

Path B: `M1 -> N1 -> N2` uses Stage21 then audited post-Stage24 Stage23.

No missing population/cutoff adapter was found. All four counts use primitive canonical physical objects under the same `R<=B` convention, with `d=R` on integral-space populations.

Verdict: `TWO_PATH_LATTICE_AVAILABLE`.

### S25-10-D — NUM reuse

The Stage14 numerical reuse index explicitly lists Stage23-25 as intersection-diagnostic consumers. `NUM-R01` is an exact target oracle after the exactly-two mask; `NUM-R06/R07` remain intermediate-path diagnostics. They do not supply the Stage25 source denominator directly.

Verdict: `REUSE_FIRST; DO_NOT_LAUNCH_NEW_CENSUS_AT_CP10`.

## New deductions at checkpoint10

### D25-10-1 — endpoint ratio is not literal survival

Because `M1` counts exactly-one-face objects and `N2` counts exactly-two-face objects, the source/target sets are disjoint by mask. Hence `N2/M1` is a matched population-size ratio, not a conditional survival probability.

This prevents a common semantic error before any asymptotic quotient is taken.

### D25-10-2 — exact two-path algebraic identity

For nonzero intermediate counts,

\[
\frac{N_2}{M_1}
=
\frac{M_2}{M_1}\frac{N_2}{M_2}
=
\frac{N_1}{M_1}\frac{N_2}{N_1}.
\]

This is exact arithmetic on counts. It requires no independence assumption.

### D25-10-3 — multiplication is legal only as path identity

Multiplying Stage22 and Stage24 transition ratios, or Stage21 and Stage23 transition ratios, is legal because numerator/denominator cancellation is exact. It is **not** legal to multiply extra local-sieve, thin-cover, or independent-proof savings on top of those path ratios unless a separate theorem establishes a new independent factor.

This distinction is the main Stage25 double-charge firewall.

### D25-10-4 — total thinning and internal interaction are separate questions

Even if checkpoint30 identifies a strong total decay law for `N2/M1`, that alone does not decide whether applying space before the second face is asymptotically more or less costly than applying it after the second face. The Stage24 second-order interaction sign remains unresolved at entry.

### D25-10-5 — Stage25 has a natural consistency test unavailable to a single-edge transition

The same endpoint ratio can be derived through two audited paths. Checkpoint30 can therefore use direct endpoint division plus both path factorizations as a three-way consistency audit. A mismatch would signal a population/cutoff/multiplicity transcription error rather than a new mathematical phenomenon.

## Potential reusable weapons / outputs

```text
W25-10-1=TWO_PATH_COUNT_RATIO_IDENTITY_WITH_NONPROBABILISTIC_FIREWALL
W25-10-2=COMBINED_TRANSITION_DOUBLE_CHARGE_AUDIT_TEMPLATE
W25-10-3=ENDPOINT_DIRECT_QUOTIENT_VS_PATH_PRODUCT_CONSISTENCY_CHECK
```

Promotion decision is deferred to checkpoint70.

## Computation decision

No new computation is justified at checkpoint10. Checkpoint20 must first inventory existing Stage16/Stage21 source counts and Stage19/Stage24 target counts on a common grid, then use NUM-R01/R06/R07 where legally matched.

```text
NUM_REUSE_CHECK=PASS
NUM_ASSETS_REUSED=NUM-R01,NUM-R06,NUM-R07
NUM_POPULATION_MATCH=ADAPTER_PROVED
NUM_NEW_COMPUTATION_JUSTIFIED=NOT_REQUIRED_AT_CHECKPOINT10
```

## Open questions handed forward

1. What matched finite `M1,N2` grid already exists without new large computation?
2. What is the certified combined ratio bracket/asymptotic class at checkpoint30?
3. Can the upper endpoint be sharpened specifically from the combined-path structure without double counting existing Stage24 mechanisms?
4. Does the C17 target family exhaust any meaningful lower-side Stage25 mechanism, or is there a stronger Stage25-specific construction receiver?
5. Can checkpoint60 determine an order-of-conditions interaction sign, or must it remain unresolved?

```text
DISCOVERY_LEDGER_STATUS=COMPLETE
DISCOVERY_AUDIT_REQUIRED=true
DISCOVERY_AUDIT_VERDICT=PENDING
```
