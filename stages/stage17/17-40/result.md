# Stage17-40 - upper-bound ledger

Status: SUBMITTED_FOR_FRESH_AUDIT

## Population

The Stage17 population is unchanged: primitive canonical triples 0<a<b<c, gcd(a,b,c)=1, exactly one integral face diagonal, R<=B, and integral R. On this target the positive space diagonal satisfies d=R.

## Strongest certified upper bound

The audited Stage17-30 adapter identifies this population with the Stage13 exactly-one population. Stage13 proves

N_1(B) ~ (kappa/(24*pi)) B (log B)^3

with positive leading constant. Therefore

N_1(B) = O(B (log B)^3).

This is stronger than the subset bound obtained from Stage16,

N_1(B) <= M_1(B) = O(B^2 log B).

The Stage13 asymptotic also gives the matching lower order, so the upper scale B (log B)^3 is already sharp at order level. In particular N_1(B)=o(B (log B)^3) cannot hold. Formal intrinsic-status classification remains reserved for Stage17-70.

## Mechanism

No new Stage17 sieve is introduced. The upper bound is inherited from the frozen Stage13 exact-one asymptotic. Its Stage17 population and cutoff adapter is identity-only because d=R.

```text
POPULATION=Stage17 B_{1,d}(B)
BEST_UPPER_BOUND=N_1(B)=O(B(log B)^3)
EQUIVALENT_POWER_FORM=B^(1+o(1))
UPPER_BOUND_SOURCE=Stage13 exact-one asymptotic
POPULATION_ADAPTER=IDENTITY_ONLY via d=R
WEAKER_SUBSET_BOUND=N_1(B)<=M_1(B)=O(B^2 log B)
ORDER_SHARP_AT_CURRENT_RESOLUTION=true
NEW_ANALYTIC_INPUT=false
EVIDENCE_LEVEL=PROVED
FINITE_DATA_USED_AS_PROOF=false
```

Checkpoint 40 adds no new leading constant, independence claim, causal claim, or perfect-cuboid conclusion. Checkpoint 50 remains blocked pending fresh Stage17-audit.
