# Stage14-num-α6 — independent equality matrix and regression pack

> STATUS: `STAGE14_NUM_ALPHA6=PENDING_GITHUB_ACTIONS_FINAL_LOCK`
>
> CLASSIFICATION: exact finite-enumeration validation; no asymptotic claim.

## Goal

Remove the remaining risk that the alpha engine only agrees with the ordinary Stage14 census at one frozen cutoff or because both paths share too much validation code.

## Independent small-cutoff gate

At

```text
B = 1,000, 5,000, 20,000, 100,000, 200,000, 500,000
```

run both:

1. the merged alpha5 diagonal-first Gaussian/collision/pruning stream;
2. the ordinary Stage14-num3 shared-face-hypotenuse / outer-Pythagorean enumerator with one deterministic chunk.

Require equality of the raw canonical `(a,b,c,d,mask)` sets, then summarize through the ordinary num3 summarizer. This is a direct algorithm-vs-algorithm comparison, not only a count comparison.

## Large frozen matrix

Run alpha5 once through `B=10,000,000`, then take nested subsets at:

```text
B = 2,000,000, 5,000,000, 10,000,000.
```

Compare every subset through the independent num3 summarizer against:

- Stage14-num1 frozen baseline at B=2m;
- Stage14-num3 independently generated milestone manifests at B=5m and B=10m.

For every frozen row require counts, object count, object-key SHA, object+mask SHA, graph counts, vertex SHA, and edge SHA.

## Why this is stronger than alpha5

Alpha5 already matched B=2m, but alpha6 tests multiple independent cutoffs and two distinct ordinary-data sources. It also checks nesting of the alpha census as B increases.

No performance crossover claim is made here. Alpha7 remains the first stage allowed to compare ordinary-num and alpha end-to-end wall time under matched output semantics.

```text
MEANINGFUL_END_TO_END_SPEEDUP_PROVED=false
NEXT_AFTER_SUCCESS=Stage14-num-alpha7
```
