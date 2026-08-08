# Stage14-3a — descriptive directional ledger

## Purpose

Stage14-3a begins finite directional analysis from the frozen Stage14-2 census without importing Stage13 code or using any Stage13 asymptotic statement.

This substage is deliberately descriptive. It records ratios, proportions, pairwise differences, leaders, and shell increments. It does **not** fit a growth law or infer a limiting vector.

Source:

```text
stages/stage14/data/14-2/final_census_audit.json
```

Derived machine-readable ledger:

```text
stages/stage14/data/14-3/directional_ledger.json
```

Reproduction script:

```text
stages/stage14/scripts/14-3/directional_ledger.py
```

## Frozen cumulative trajectory

| B | `(N_a,N_b,N_c)` | `N_a/N_c` | `N_b/N_c` | `N_a/N_b` | leader |
|---:|---:|---:|---:|---:|---|
| 1,000 | `(2,0,0)` | undef | undef | undef | a |
| 2,000 | `(2,2,1)` | 2.0000 | 2.0000 | 1.0000 | tie a/b |
| 5,000 | `(6,6,3)` | 2.0000 | 2.0000 | 1.0000 | tie a/b |
| 10,000 | `(9,11,5)` | 1.8000 | 2.2000 | 0.8182 | b |
| 20,000 | `(16,16,10)` | 1.6000 | 1.6000 | 1.0000 | tie a/b |
| 50,000 | `(24,24,14)` | 1.7143 | 1.7143 | 1.0000 | tie a/b |
| 100,000 | `(33,33,23)` | 1.4348 | 1.4348 | 1.0000 | tie a/b |
| 200,000 | `(42,50,24)` | 1.7500 | 2.0833 | 0.8400 | b |
| 500,000 | `(70,78,40)` | 1.7500 | 1.9500 | 0.8974 | b |
| 1,000,000 | `(98,101,56)` | 1.7500 | 1.8036 | 0.9703 | b |
| 2,000,000 | `(142,134,80)` | 1.7750 | 1.6750 | 1.0597 | a |

## Late-range observations

The late finite trajectory separates into two visibly different motions.

First,

\[
\frac{N_a}{N_c}=rac74
\]

holds **exactly** at all three sampled cutoffs

```text
B=200,000
B=500,000
B=1,000,000
```

before moving only slightly to

\[
\frac{142}{80}=1.775
\]

at `B=2,000,000`.

This is recorded only as a **finite a/c plateau**. Three exact sampled equalities do not establish a limit, an invariant, or a theorem.

Second, over the same late range,

```text
N_b/N_c:
2.083333 -> 1.950000 -> 1.803571 -> 1.675000
```

while

```text
N_a/N_b:
0.840000 -> 0.897436 -> 0.970297 -> 1.059701.
```

Thus the observed `b -> a` leader reversal at 2m is better described, at finite scale, as the erosion of the previous `b` advantage while the `a/c` ratio stays comparatively stable.

Again this is descriptive, not asymptotic.

## Shell composition

Cumulative ratios can hide where the motion comes from, so Stage14-3a also records increments between audited cutoffs.

Two late shells are especially contrasting:

```text
100k -> 200k:  delta(a,b,c) = (9,17,1)
1m   -> 2m:    delta(a,b,c) = (44,33,24)
```

At 100k->200k the new population is strongly `b`-heavy and nearly absent in `c`; at 1m->2m the new population is `a`-led. This directly explains why the cumulative leader can reverse without requiring any monotone ratio model.

The intermediate late shells are

```text
200k -> 500k: (28,28,16)
500k -> 1m:   (28,23,16)
```

so the finite shell leader changes from `b`, to a/b tie, to `a`, to `a` across these sampled intervals.

## What 14-3a establishes

It establishes only finite-data facts:

1. the 11 frozen cumulative rows have a nontrivial leader history;
2. `a/b` crosses from below one to above one between the sampled 1m and 2m cutoffs;
3. `a/c=7/4` occurs exactly at 200k, 500k and 1m, then shifts slightly at 2m;
4. `b/c` decreases across the four sampled late cutoffs;
5. shell composition changes materially, so cumulative ratio motion is not well described as a simple monotone drift on the current grid.

It does **not** establish:

```text
an asymptotic ratio
an asymptotic growth law
a monotonicity theorem
that 7/4 is a true limiting or exact constant
that the late b/c decline continues
any Stage13-dependent statement
```

## Next finite task

The natural next diagnostic is to densify the cutoff grid in the late range, especially around the `a/b` crossing and the apparent `a/c` plateau. This is assigned to Stage14-3b.

Stage14-4 remains paused.

```text
STAGE14_3A=COMPLETE
DESCRIPTIVE_LEDGER_COMPLETE=true
A_C_FINITE_PLATEAU_OBSERVED=true
A_B_LEADER_CROSSING_OBSERVED=true
FINITE_RATIO_LIMIT_IDENTIFIED=false
MONOTONE_CONVERGENCE_SUPPORTED=false
STAGE13_ANALYTIC_DEPENDENCY_USED=false
NEXT=Stage14-3b late-range finite cutoff densification
STAGE14_4_STATUS=PAUSED_PENDING_ONE_FACE_REVIEW
```
