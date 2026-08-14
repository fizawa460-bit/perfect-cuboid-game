# Stage19-30 — ratio / thinning law

Status: **SUBMITTED_FOR_FRESH_AUDIT**

Stage19 is the literal Stage15 numerator population `A_2(B)`, while Stage18 is the matched exactly-two population `B_2(B)` with count `M_2(B)`. Thus the immediate source/target ratio is

\[
\frac{N_2(B)}{M_2(B)}.
\]

## 1. Frozen quantitative survival law

Stage15 certified, on the same primitive/canonical physical measure and exact cutoff `R<=B`,

\[
M_2(B)\sim C_{M_2}B(\log B)^5,\qquad C_{M_2}>0,
\]

and Stage14 supplies the matched whole-family numerator bound

\[
N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.
\]

Therefore

\[
\boxed{
\frac{N_2(B)}{M_2(B)}
\ll_\varepsilon
B^{-1/2+\varepsilon}(\log B)^{-5}
}
\]

and in particular

\[
\boxed{\frac{N_2(B)}{M_2(B)}\to0}.
\]

For every fixed `delta<1/2`, equivalently

\[
\frac{N_2(B)}{M_2(B)}\ll_\delta B^{-\delta}.
\]

This is a certified polynomial upper thinning law, not an asymptotic for the ratio.

## 2. Independent zero-density route

Stage15 also proved

\[
\frac{N_2(B)}{M_2(B)}\to0
\]

independently of the Stage14 half-power numerator bound, using equality of coupled Gaussian-norm squareclasses and fixed-prime valuation-parity filters. That local mechanism does **not** prove exponent `1/2` or any fixed `delta>0` by itself.

Accordingly this checkpoint keeps two theorem species separate:

1. quantitative survival ceiling from Stage14 numerator + Stage15 denominator;
2. independent causal zero-density theorem from Stage15 squareclass sieving.

The second route is not credited with paying for the half-power.

## 3. Numerical-reuse preflight and extended exact census

The newly promoted Stage14 numerical observatory was inspected before any new computation.

```text
NUM_REUSE_CHECK=PASS
NUM_ASSETS_REUSED=NUM-R01,NUM-R02,NUM-R03 / AR-040
NUM_POPULATION_MATCH=ADAPTER_PROVED
NUM_POPULATION_ADAPTER=select exact-two face mask from the retained Stage14 at-least-two ledger; d=R gives d<=B iff R<=B
NUM_EVIDENCE_LEVEL=EXACT_FINITE_CENSUS + EXACT_REGRESSION_ORACLE + PROVED_ALGORITHM_EXACT_REGRESSION
NUM_NEW_COMPUTATION_JUSTIFIED=NOT_REQUIRED
```

The Stage14 observatory counts primitive canonical integral-space cuboids under `d<=B` and retains the exact face mask. Selecting the exactly-two mask therefore gives exactly the Stage19 finite population; no ambient `M_2` transfer is made.

The frozen nested exact counts include

| `B` | `N_2(B)` |
|---:|---:|
| 250,000,000 | 2,657 |
| 300,000,000 | 2,866 |
| 400,000,000 | 3,194 |
| 500,000,000 | 3,495 |

At `B=500,000,000`, the directional split is

\[
(N_a,N_b,N_c)=(1374,1371,750),
\]

with `T=0` in this finite census. The latter is **not** a perfect-cuboid nonexistence statement.

This extended census supersedes the earlier *diagnostic range* statement `N_2(100000)=89<200`: the predeclared sample-size gate `N_2>=200` is now passed. It does not change the already audited Stage19-20 record historically; it supplies stronger later-stage finite evidence.

However, the stronger data do **not** certify a survivor exponent. The Stage14 terminal finite-stability gate tracks

\[
R_0(B)=\frac{N_2(B)}{\sqrt B}.
\]

Its values are approximately

```text
B=250m: R0=0.1680434349
B=300m: R0=0.1654685871
B=400m: R0=0.1597000000
B=500m: R0=0.1563011516
```

and the predeclared 2% stability rule fails on 300m→400m and 400m→500m. Thus the new weapon removes the old small-sample objection but still does not justify `N_2(B)~C sqrt(B)` or sharpness of exponent `1/2`.

## 4. Stage24 boundary

The displayed ratio is necessarily the Stage18-to-Stage19 survival fraction because those are the matched source and target populations. Stage19 records the already certified law because checkpoint30 requires a survival classification.

Stage24 still owns the deeper transition study: whether this cost is intrinsic to the space-diagonal condition after two faces are integral, how it compares with the other transition/control lanes, and how the mechanism interacts with previously charged face conditions. No such interaction classification is made here.

## 5. Non-claims

- no asymptotic `N_2(B)~C B^{1/2}`;
- no matching lower bound;
- no proof that exponent `1/2` is intrinsic or sharp;
- no independence claim for the space-diagonal condition;
- no directional limiting law;
- finite `T=0` is not perfect-cuboid nonexistence;
- numerical regression is not theorem proof.

```text
EVIDENCE_LEVEL=PROVED_WITH_EXACT_FINITE_DIAGNOSTIC
SOURCE_POPULATION=Stage18 B_2(B)
TARGET_POPULATION=Stage19 A_2(B)
SURVIVAL_RATIO=N_2(B)/M_2(B)
QUANTITATIVE_LAW=N_2/M_2 <<_epsilon B^(-1/2+epsilon)(log B)^(-5)
ZERO_DENSITY=true
ASYMPTOTIC_RATIO_CLAIM=false
HALF_POWER_INTRINSIC_CLAIM=false
NUM_SAMPLE_SIZE_GATE=PASS
NUM_STABILITY_GATE=FAIL
STAGE24_DEEP_TRANSITION_RESERVED=true
FINITE_DATA_USED_AS_PROOF=false
AUDIT_REQUIRED=true
NEXT_CHECKPOINT_AFTER_PASS=40
CODEX_REQUIRED=false
```