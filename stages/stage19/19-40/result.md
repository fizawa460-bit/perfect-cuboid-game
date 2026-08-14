# Stage19-40 — upper-bound ledger

Status: **SUBMITTED_FOR_FRESH_AUDIT**

## 1. Strongest certified whole-family upper bound

Because Stage19 is literally the Stage14/15 physical exactly-two population with integral space diagonal and the exact cutoff adapter `d=R`, the strongest frozen whole-family ceiling transfers without modification:

\[
\boxed{N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}}
\]

for every `epsilon>0`. Equivalently,

\[
\boxed{N_2(B)\ll B^{1/2+o(1)}}.
\]

This ranges over the complete primitive canonical Stage19 family. It is not a fixed-direction, fixed-fiber, or averaged statement.

## 2. What pays for the half-power

The half-power is inherited from the frozen Stage14 whole-family theorem. Its proof chain is global:

1. exact two-face gluing gives a raw pair graph with `N_2(B)<=E(B)`;
2. every active face has uniformly only `B^{o(1)}` bounded-height neighbors on the associated elliptic fiber;
3. complete balanced-packet reductions and host/reconstruction bounds cover every physical chamber;
4. the resulting whole-family exponent is `1/2`, with only `B^{o(1)}` losses.

Thus the fixed-power ceiling is paid by the **Stage14 global graph / elliptic-fiber / complete-host proof chain**. The Stage15 Gaussian-squareclass mechanism proves zero density independently but does not pay for this fixed half-power ceiling.

## 3. Numerical weapon check against sharpness

The Stage14 numerical observatory is now an explicit reusable weapon. For Stage19 the exact-two mask is selected from its retained face-mask ledger, so the finite population matches Stage19 exactly after the adapter `d=R`.

```text
NUM_REUSE_CHECK=PASS
NUM_ASSETS_REUSED=NUM-R01,NUM-R02,NUM-R03 / AR-040
NUM_POPULATION_MATCH=ADAPTER_PROVED
NUM_EVIDENCE_LEVEL=EXACT_FINITE_CENSUS + EXACT_REGRESSION_ORACLE + PROVED_ALGORITHM_EXACT_REGRESSION
NUM_NEW_COMPUTATION_JUSTIFIED=NOT_REQUIRED
```

The exact census gives

\[
N_2(250m)=2657,
\quad N_2(300m)=2866,
\quad N_2(400m)=3194,
\quad N_2(500m)=3495.
\]

The normalized quantity `N_2(B)/sqrt(B)` is

```text
250m: 0.1680434349
300m: 0.1654685871
400m: 0.1597000000
500m: 0.1563011516
```

This is compatible with the proved square-root-plus-subpower ceiling, but compatibility is not proof of sharpness. More importantly, the predeclared terminal stability test requires all primary metrics to drift by at most 2% on three consecutive transitions. It fails at 300m→400m and 400m→500m. For `R0=N_2/sqrt(B)`, the relative drifts on those transitions are about `3.6121%` and `2.1746%` respectively.

Therefore the new exact finite weapon strengthens the **negative sharpness verdict**:

- the old sample-size gate `N_2>=200` is no longer an obstacle;
- nevertheless the square-root-normalized finite panel has not stabilized under its own predeclared rule;
- hence finite evidence still cannot certify exponent `1/2` as intrinsic or sharp.

At `B=500m` the finite census also has `T=0`, but that is not a perfect-cuboid nonexistence theorem.

## 4. Sharpness status

The bound remains one-sided. Neither Stage14 nor the new numerical weapon proves

\[
N_2(B)\asymp B^{1/2}
\]

or a matching lower bound. Nor is there a certified strict improvement

\[
N_2(B)\ll B^{1/2-\delta}
\]

for fixed `delta>0`.

Thus checkpoint40 records the strongest certified upper ledger while keeping

```text
MATCHING_LOWER_BOUND=false
HALF_POWER_SHARP=false
HALF_POWER_INTRINSIC=UNRESOLVED
STRICT_SUB_SQRT_BOUND=false
```

The new numerical evidence explains *why* the project should not promote sharpness merely because the count has reached thousands.

## 5. Relation to checkpoint30

Combining the theorem ceiling with the frozen Stage18 denominator

\[
M_2(B)\sim C_{M_2}B(\log B)^5
\]

gives exactly the Stage19-30 quantitative survival ceiling

\[
\frac{N_2(B)}{M_2(B)}\ll_\varepsilon B^{-1/2+\varepsilon}(\log B)^{-5}.
\]

No extra saving is double charged and the finite census is not used as proof of this law.

## 6. Non-claims

- no matching lower bound;
- no `N_2(B)~C sqrt(B)` asymptotic;
- no proof that `1/2` is the true exponent;
- no strict sub-square-root theorem;
- no claim that Stage15 local parity filters yield the half-power;
- no perfect-cuboid conclusion from finite `T=0`;
- no asymptotic conclusion from finite regression locks.

```text
EVIDENCE_LEVEL=PROVED_WITH_EXACT_FINITE_DIAGNOSTIC
UPPER_BOUND=N_2(B) <<_epsilon B^(1/2+epsilon)
EQUIVALENT_FORM=N_2(B) << B^(1/2+o(1))
BOUND_SOURCE=Stage14 whole-family theorem
PAYING_MECHANISM=global pair graph + uniform elliptic-fiber multiplicity + complete balanced-host reconstruction
STAGE15_LOCAL_SIEVE_PAYS_HALF_POWER=false
NUM_MAX_B=500000000
NUM_N2_AT_MAX=3495
NUM_SAMPLE_SIZE_GATE=PASS
NUM_TERMINAL_STABILITY_GATE=FAIL
MATCHING_LOWER_BOUND=false
HALF_POWER_SHARP=false
HALF_POWER_INTRINSIC=UNRESOLVED
STRICT_SUB_SQRT_BOUND=false
AUDIT_REQUIRED=true
NEXT_CHECKPOINT_AFTER_PASS=50
CODEX_REQUIRED=false
```