# Stage25-10 discovery ledger

CHECKPOINT=10
STATUS=REPAIRED_PENDING_FRESH_AUDIT
STAGE=Stage25
TRANSITION=Stage16->Stage19

## Normative repository-reuse handoff

```text
REPO_REUSE_PREFLIGHT=PASS
REUSE_SEARCH_SCOPE=ARSENAL,NUM_INDEX,STAGES,SUPPLEMENTS,ARCHIVE,PRS
REUSED_RESULTS=stages/stage21/final.md;stages/stage22/22-controller.json;stages/stage23/post-stage24-r01/controller.json;stages/stage24/final.md;stages/stage19/post-stage24-50-supersession.md;docs/stage14-num-reuse-index.md;PR#967;PR#977;PR#978;PR#979
REUSE_MATCH_STATUS=MIXED
STRONGEST_KNOWN_CHECK=PASS
STRONGER_PRIOR_RESULT_FOUND=true
NEW_RESEARCH_JUSTIFIED=NOT_REQUIRED_AT_CHECKPOINT10_CONTRACT_FREEZE
```

`STRONGER_PRIOR_RESULT_FOUND=true` has two concrete reasons:

1. Stage21 carries the audited exact asymptotic `M1(B)~3/(4*pi^2) B^2 log B`, strictly stronger than the older Stage16 `M1(B) asymp B^2 log B` interface.
2. Stage24 checkpoint50 supersedes the historical Stage19 constant lower floor by `N2(B)>>sqrt(log B)` and proves target unboundedness.

No stronger compatible whole-population Stage25 endpoint theorem was found beyond these already-audited interfaces.

## Concrete Stage21-28 discovery evidence

```text
DISCOVERY_CHECKPOINT=Stage25-10
SEARCHED_PATHS=docs/stage16-28-reuse-preflight.md;docs/stage14-num-reuse-index.md;docs/stage14-15-bound-attack-map.md;docs/stage14-15-bound-deep-review-queue.md;stages/stage16/final.md;stages/stage21/final.md;stages/stage22/22-controller.json;stages/stage23/post-stage24-r01/controller.json;stages/stage24/final.md;stages/stage19/post-stage24-50-supersession.md;historical PRs #967,#977,#978,#979
SEARCH_TERMS=Stage16 Stage19 M1 N2 combined thinning; exactly-one exactly-two space diagonal; M2/M1 N2/M2 N1/M1 N2/N1; integral-space exactly-two; half-power upper; mixed-parity C17; population adapter
STRUCTURAL_SIGNATURES=two-path square Stage16-Stage17-Stage18-Stage19; endpoint quotient factorization; exactly-one/exactly-two disjoint masks; integral-space diagonal; paired norms; overlap intersection; moving-modulus upper attacks
DEPENDENCY_NEIGHBORS=Stage16,Stage16S,Stage17,Stage18,Stage19,Stage21,Stage22,Stage23,Stage24,Stage14-num,Stage14/15 bound-attack ledger
CANDIDATES_FOUND=C25-10-A,C25-10-B,C25-10-C,C25-10-D,C25-10-E,C25-10-F,C25-10-G,R25-10-01,R25-10-02,R25-10-03,R25-10-04,R25-10-05,R25-10-06,R25-10-07
CANDIDATES_ACCEPTED=C25-10-A Stage21 exact M1 source asymptotic;C25-10-B Stage22 M2/M1 path law;C25-10-C Stage24 final N2 lower/upper and N2/M2 law;C25-10-D post-Stage24 Stage23 N2/N1 law;C25-10-E Stage19 post-Stage24 lower supersession;C25-10-F NUM-R01 exact target adapter;C25-10-G NUM-R06/R07 diagnostic-only path reuse
CANDIDATES_REJECTED_WITH_REASON=R25-10-01 Stage16 M1-asymp interface is valid but weaker than audited Stage21 exact asymptotic;R25-10-02 historical Stage19 finite floor is valid but superseded as strongest lower interface by Stage24-50;R25-10-03 S1415-ATTACK-0215,0216,0710/Q02 toric ambient results have population mismatch for direct N2 endpoint lower transfer;R25-10-04 S1415-ATTACK-0724,0728,0729,0731/Q05 are future uniform moving-curve theorem gates, not stronger audited Stage25-10 inputs;R25-10-05 S1415-ATTACK-0748/Q06 is an exact physical-height support receiver but has no certified global support bound stronger than the inherited N2 upper;R25-10-06 S1415-ATTACK-0791,0793,0794,0796,0800,0771,0772,0804,0807,0809,0811,0812,0814,0816,0817/Q07-Q10 are internally exhausted without a materially new equation or same-measure theorem and are not reopened at checkpoint10;R25-10-07 S1415-ATTACK-0817,0818,0819,0820/Q11 gives qualitative fixed-prime zero density only and cannot replace or multiply the inherited half-power upper
POPULATION_ADAPTERS_PROVED=A25-10-1 Stage21 source M1 is literal Stage16 primitive/canonical exactly-one population under R<=B;A25-10-2 Stage22 M2/M1 uses matched primitive/canonical adjacent strata under the same R<=B cutoff and is a population-size ratio, not objectwise survival;A25-10-3 Stage24 N2/M2 is literal Stage18 subset by R integral under the same cutoff;A25-10-4 post-Stage24 Stage23 N2/N1 uses matched primitive/canonical Stage17/19 counts with d=R and is a population-size ratio;A25-10-5 NUM-R01 -> select primitive canonical exact-two face-mask records with d=R<=B to obtain the Stage19 N2 finite target;A25-10-6 NUM-R06/R07 have no direct Stage25 endpoint adapter and are retained only as intermediate-path diagnostics
DISCOVERY_LEDGER_STATUS=COMPLETE
```

## Search modes executed

```text
DIRECT_TERMS=Stage16 Stage19 M1 N2 combined thinning
SYNONYMS_NOTATION=exactly-one exactly-two space diagonal adjacent-stratum population ratio
STRUCTURAL_SIGNATURES=two-path square Stage16-Stage17-Stage18-Stage19; endpoint quotient factorization
DEPENDENCY_NEIGHBORS=Stage21 Stage22 Stage23 Stage24 Stage16S Stage14-num Stage14/15-bound-attack
```

## Accepted candidates and strongest interfaces

### C25-10-A — source upgrade

Stage16 final proves `M1(B) asymp B^2 log B`, but audited Stage21 imports the stronger exact asymptotic on the literal same source population:

\[
M_1(B)\sim\frac{3}{4\pi^2}B^2\log B.
\]

Verdict: `PROMOTE_STRONGER_FROZEN_SOURCE_INTERFACE`.

### C25-10-B — Stage22 path-A first leg

The audited Stage22 controller freezes

\[
M_2(B)/M_1(B)\sim (4\pi^2C_{M_2}/3)(\log B)^4/B.
\]

The population/cutoff match is exact at the physical-object level, but this is an adjacent-stratum population-size ratio because exactly-one and exactly-two masks are disjoint.

Verdict: `ACCEPT_PATH_A_FIRST_LEG`.

### C25-10-C — Stage24 target and path-A second leg

The audited Stage24 final bundle supplies

\[
\sqrt{\log B}\ll N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}
\]

and

\[
B^{-1}(\log B)^{-9/2}\ll N_2/M_2
\ll_\varepsilon B^{-1/2+\varepsilon}(\log B)^{-5}.
\]

Verdict: `ACCEPT_CURRENT_TARGET_AND_PATH_A_SECOND_LEG`.

### C25-10-D — post-Stage24 Stage23 path-B second leg

The audited reinvestigation freezes

\[
B^{-1}(\log B)^{-5/2}\ll N_2/N_1
\ll_\varepsilon B^{-1/2+\varepsilon}(\log B)^{-3}.
\]

Verdict: `ACCEPT_CURRENT_PATH_B_SECOND_LEG`.

### C25-10-E — target supersession metadata

Historical Stage19 had only the finite lower floor. Audited Stage24-50 supersedes the current lower interface with `N2(B)>>sqrt(log B)` and unboundedness while preserving the historical audit as correct at its original time.

Verdict: `USE_POST_STAGE24_CURRENT_TARGET_INTERFACE`.

### C25-10-F/G — NUM reuse

The Stage14 numerical reuse index explicitly routes Stages23-25 to `NUM-R01/R06/R07` after an exact intersection adapter.

- `NUM-R01`: accepted as an exact finite target oracle after selecting exact-two mask records.
- `NUM-R06/R07`: accepted only as intermediate-path diagnostics; they are not a direct Stage25 denominator oracle.

Verdict: `REUSE_FIRST; DO_NOT_LAUNCH_NEW_CENSUS_AT_CP10`.

## Rejected candidate ledger

### R25-10-01 — weaker Stage16 endpoint statement

`M1(B) asymp B^2 log B` remains true but is rejected as the strongest source interface because Stage21 already has the exact leading asymptotic.

### R25-10-02 — historical finite Stage19 floor

`N2(B)>=3495` for sufficiently large frozen finite cutoff remains true but is rejected as the current strongest lower interface because Stage24-50 proves `N2(B)>>sqrt(log B)`.

### R25-10-03 — Q02 ambient toric route

`S1415-ATTACK-0215`, `0216`, `0710` are reusable for toric coordinates/thin-set discipline but their ambient population is not a direct Stage25 target lower theorem. No `B(log B)^5` scale may be transferred to `N2`.

### R25-10-04 — Q05 moving genus-one gate

`S1415-ATTACK-0724`, `0728`, `0729`, `0731` require a new uniform moving-curve/same-measure theorem. They are future theorem gates, not a stronger already-audited checkpoint10 interface.

### R25-10-05 — Q06 Kummer support receiver

`S1415-ATTACK-0748` supplies an exact physical-height receiver but no global `|S(B)|` theorem. It cannot supersede `N2(B)<<_epsilon B^(1/2+epsilon)`.

### R25-10-06 — Q07-Q10 exhausted internal routes

The exact-reconstruction, pointwise-gcd, dispersion/occupancy, and Pell/ideal residual-switch clusters were later executed or negatively certified. Stage25-10 introduces no materially new equation, height monotonicity, same-measure estimate, spectral theorem, or ideal-average theorem that licenses reopening them.

### R25-10-07 — Q11 fixed-prime local sieve

`S1415-ATTACK-0817` through `0820` prove a qualitative fixed-prime zero-density mechanism. They do not give effective growing-modulus uniformity and therefore cannot be promoted to a new fixed-power saving or multiplied with the Stage14 half-power upper.

## New deductions at checkpoint10

### D25-10-1 — endpoint ratio is not literal survival

Because `M1` counts exactly-one-face objects and `N2` counts exactly-two-face objects, the source/target sets are disjoint by mask. Hence `N2/M1` is a matched population-size ratio, not a conditional survival probability.

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

Multiplying Stage22 and Stage24 transition ratios, or Stage21 and Stage23 transition ratios, is legal because numerator/denominator cancellation is exact. It is not legal to multiply extra local-sieve, thin-cover, or independent-proof savings on top unless a separate theorem establishes a new independent factor.

### D25-10-4 — total thinning and internal interaction are separate questions

Even if checkpoint30 identifies a strong total decay law for `N2/M1`, that alone does not decide whether applying space before the second face is asymptotically more or less costly than applying it after the second face. The Stage24 second-order interaction sign remains unresolved at entry.

### D25-10-5 — three-way consistency test

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
DISCOVERY_AUDIT_VERDICT=PENDING_REAUDIT
```
