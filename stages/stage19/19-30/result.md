# Stage19-30 — ratio / thinning law

Status: **SUBMITTED_FOR_FRESH_AUDIT**

Stage19 is the literal Stage15 numerator population `A_2(B)`, while Stage18 is the matched exactly-two population `B_2(B)` with count `M_2(B)`. Thus the immediate source/target ratio for this population state is

\[
\frac{N_2(B)}{M_2(B)}.
\]

## 1. Frozen quantitative survival law

Stage15 already certified, on the same primitive/canonical physical measure and the same exact cutoff `R<=B`,

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

For every fixed `delta<1/2`, one may equivalently write

\[
\frac{N_2(B)}{M_2(B)}\ll_\delta B^{-\delta}.
\]

This is a certified polynomial upper thinning law, not an asymptotic for the ratio.

## 2. Independent zero-density route

Stage15 also proved

\[
\frac{N_2(B)}{M_2(B)}\to0
\]

independently of the Stage14 half-power numerator bound, using equality of coupled Gaussian-norm squareclasses and fixed-prime valuation-parity filters. That local mechanism does **not** prove the exponent `1/2` or any fixed `delta>0` by itself.

Accordingly the checkpoint keeps two theorem species separate:

1. **quantitative survival ceiling** from Stage14 numerator + Stage15 denominator;
2. **independent causal zero-density theorem** from Stage15 squareclass sieving.

The second route must not be credited with paying for the half-power.

## 3. Stage24 boundary

The displayed ratio is necessarily the Stage18-to-Stage19 survival fraction because those are the matched source and target populations. Stage19 records the already certified law because checkpoint30 requires a survival classification.

Stage24 still owns the deeper transition study: whether this cost is intrinsic to the space-diagonal condition after two faces are integral, how it compares with Stage16S and Stage21, and how the mechanism interacts with previously charged face conditions. No such interaction classification is made here.

## 4. Finite data are diagnostic only

Stage19-20 froze the exact counts through `B=100000`, where `N_2(100000)=89`. The predeclared survivor-slope gate `N_2>=200` fails. The finite table is therefore not used to infer a survivor exponent, asymptotic constant, or sharpness.

## 5. Non-claims

- no asymptotic `N_2(B)~C B^{1/2}`;
- no matching lower bound;
- no proof that exponent `1/2` is intrinsic or sharp;
- no independence claim for the space-diagonal condition;
- no directional survivor asymptotic;
- no perfect-cuboid conclusion.

```text
EVIDENCE_LEVEL=PROVED
SOURCE_POPULATION=Stage18 B_2(B)
TARGET_POPULATION=Stage19 A_2(B)
SURVIVAL_RATIO=N_2(B)/M_2(B)
QUANTITATIVE_LAW=N_2/M_2 <<_epsilon B^(-1/2+epsilon)(log B)^(-5)
ZERO_DENSITY=true
ASYMPTOTIC_RATIO_CLAIM=false
HALF_POWER_INTRINSIC_CLAIM=false
STAGE24_DEEP_TRANSITION_RESERVED=true
FINITE_DATA_USED_AS_PROOF=false
AUDIT_REQUIRED=true
NEXT_CHECKPOINT_AFTER_PASS=40
CODEX_REQUIRED=false
```
