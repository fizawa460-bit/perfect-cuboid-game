# SR-STR-024 ChatGPT pre-Work external-search follow-up

Date: 2026-08-19  
Baseline: PR #1147.

```text
DIRECT_FULL_TARGET_THEOREM_COUNT=0
CHATGPT_SEARCH_VERDICT=ESCALATE_TO_WORK
ARSENAL_PROMOTION=NO
CARD_STATUS_CHANGE=NO
KEY_NEW_LEAD=Nguyen individual-modulus variance theorem for tau_k
NARROWED_GAP=ConditionedFilteredTau3IndividualModulusVarianceAdapter
```

## Frozen receiver

SR-STR-024 / AR-025 requires every retained cell / valuation pattern `nu` to retain its original scalar or `(E,m)` pair conditioning while controlling the target class of a nonnegative filtered witness sequence `S_nu(a)` modulo `Q_nu | 2UV`. The principal term is `P_nu=A_{nu,0}/phi(Q_nu)`. Generic character-by-character cancellation is not enough because summing a polynomial number of characters can lose the desired saving.

## Search result

No direct theorem was found for the actual filtered/common-core/factor-pair witness sequence.

The strongest new near result is David T. Nguyen, *Variance of the k-fold divisor function in arithmetic progressions for individual modulus* (Acta Arith. 212 (2024), arXiv:2205.02354). For standard smoothed `tau_k`, its fixed-modulus variance theorem is genuinely individual-composite-modulus and does not average over the modulus. For `k=3`, in the range `X=d^c` with `c>2+delta`, the theorem plus `L^infty <= L^2` gives power-saving domination of every target residue class for the **standard** `tau_3` surrogate.

This materially improves the literature map: the old obstacle is no longer merely “need an individual-modulus divisor theorem.” Such a theorem exists for standard `tau_3` variance. The unresolved mismatch is the input sequence.

Irving gives pointwise individual smooth-modulus results for standard `tau`; Fouvry–Kowalski–Michel gives strong `tau_3` pointwise distribution for prime moduli; Wu–Xi improves smooth-modulus divisor AP technology. None supplies an exact adapter from the StructureRadar witness sequence while preserving the original charged measure and all common-core / factor-allocation / primitive masks.

## Narrowed missing adapter

```text
ConditionedFilteredTau3IndividualModulusVarianceAdapter
```

Required: for every retained cell and valuation pattern,

```text
V_nu = sum_{(a,Q_nu)=1} |S_nu(a)-P_nu|^2
```

must be small enough to force domination at the moving target class `rho_nu`, while `S_nu` retains the filtered `tau_3` witness, moving common-core average, reciprocal factor-pair conditions, primitive/coprime masks, and the original scalar or pair charged measure.

A scalarization of the `(E,m)` pair branch is not permitted unless independently proved measure-preserving.

## Focused Work handoff

Do not repeat searches of Grimmelt–Merikoski, Nguyen generalized-divisor papers, Nguyen arXiv:2205.02354, Irving 1403.8031 / 1503.07156, Fouvry–Kowalski–Michel 1304.3199, Wu–Xi 1603.07060, Rodgers–Soundararajan, Frei–Sofos, or generic large-sieve results.

Search only for published fixed-modulus variance/maximal-discrepancy theorems for **weighted or filtered divisor convolutions** that preserve auxiliary coprimality/dyadic/common-core weights, or a published extension of the Nguyen fixed-modulus `tau_3` variance argument to coefficient sequences of this exact type. Check separately for a pair-preserving/bilinear variance theorem for the original `(E,m)` measure.

If no theorem applies, identify the first exact point in the Nguyen/Voronoi or dispersion proof that fails for the StructureRadar coefficient sequence, and state the missing weighted Voronoi / character-moment / bilinear estimate with its modulus and length ranges.

## Firewall

Standard `tau_3` is not the repo witness sequence. No direct transfer or arsenal promotion is justified; SR-STR-024 remains an external gate.