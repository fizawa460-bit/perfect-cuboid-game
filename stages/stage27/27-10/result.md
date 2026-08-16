# Stage27-10 — true-`N2` exponent attack contract and route preflight

```text
TASK_ID=Stage27-10
CHECKPOINT=10
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
EVIDENCE_LEVEL=CONTRACT_AND_ROUTE_PREFLIGHT
NEW_N2_EXPONENT_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
```

## 1. Entry gate

Stage26 checkpoint70 hostile audit passed in PR #1020 and the PR merged as

```text
8b0472db36c1113198251a7d9646b8c7bfe80331
```

Stage26 is therefore lifecycle-closed. Its audit did not mathematically authorize a next stage; the operator subsequently selected Stage27 by issuing `Stage27-main-batch`. This selection changes workflow only, not any theorem.

## 2. Exact population contract

Stage27 reopens the Stage18 -> Stage19 transition only at the downstream research level.

Source:

\[
M_2(B)=\#\{0<a<b<c,\gcd(a,b,c)=1,R\le B,\text{ exactly two integral face diagonals}\}.
\]

Target:

\[
N_2(B)=\#\{\text{same objects with }R\in\mathbf Z\}.
\]

Thus

\[
\boxed{\mathcal N_2(B)=\mathcal M_2(B)\cap\{R\in\mathbf Z\}}
\]

is a literal subset under the same primitive/canonical physical-object measure and the exact same cutoff

\[
R=\sqrt{a^2+b^2+c^2}\le B.
\]

No incidence multiplicity or comparable-height adapter is introduced.

## 3. Strongest current theorem surface

The synchronized post-Stage25 receiver gives

\[
\boxed{B^{1/4}\ll N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}}.
\]

Directionally,

\[
\boxed{N_{2,j}(B)\gg_j B^{1/4}},\qquad j=a,b,c.
\]

Stage18 supplies

\[
M_2(B)\sim C_{M_2}B(\log B)^5,\qquad C_{M_2}>0,
\]

so the current literal survival corridor is

\[
\boxed{
B^{-3/4}(\log B)^{-5}
\ll
\frac{N_2(B)}{M_2(B)}
\ll_\varepsilon
B^{-1/2+\varepsilon}(\log B)^{-5}
}.
\]

The true `N2` exponent remains unknown.

## 4. Lower route opened

The current quarter-power families R501/R502 have a structural scale: their usable parameter sets have quadratic mass while the physical height is order `T^8`, yielding `B^(1/4)` after primitivity, canonicalization, fiber and exact-two controls.

Stage27 will test whether the quarter-power bottleneck is artificial. A valid upgrade must improve the parameter-mass/height/fiber balance, for example by:

- restoring a higher-dimensional family hidden by a specialization;
- finding a lower-degree height family;
- proving a stronger fiber invariant that permits more parameters;
- constructing a genuinely new primitive Stage19 family.

This route is not allowed to count scalar multiples or third-face Euler cuboids as Stage19 objects.

## 5. Upper route opened

The current whole-family theorem

\[
N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}
\]

is still the upper wall. The fixed-prime squareclass sieve proves zero density, but its ordered fixed-finite-prime limit is not a growing-modulus power-saving theorem.

A strict sub-half upper therefore requires genuinely new uniformity or a new same-measure rational-point theorem. Candidate attack classes are:

```text
MOVING_FAMILY_UNIFORMITY
GROWING_MODULUS_SIEVE_UNIFORMITY
STRONGER_SPACE_SQUARE_COVER_POINT_COUNT
NEW_HEIGHT_MONOTONE_DESCENT_OR_TORSOR
EXTERNAL_THEOREM_WITH_EXACT_ADAPTER
```

## 6. Stage26 reuse boundary

Stage26 proved

\[
M_3(B)\gg_\varepsilon B^{1/3-\varepsilon}
\]

for the no-space Euler-cuboid population. Those objects have three integral face diagonals and are outside the Stage19 exactly-two population. Therefore

```text
STAGE26_M3_LOWER_TRANSFERRED_TO_N2=false
POPULATION_MISMATCH_FIREWALL=PASS
```

The Stage26 divisor-fiber strategy may be reused only as a method template after a new Stage19-compatible invariant is proved.

## 7. Finite-data route

Stage19 has an exact finite census including

\[
N_2(500,000,000)=3495.
\]

Checkpoint20 may reuse that census and directional counts to calculate effective exponents and route diagnostics. These values may guide theorem attacks but cannot identify the asymptotic exponent.

## 8. Exit

Checkpoint10 proves no new exponent theorem. It freezes the target, the current corridor, the legal routes and the population firewalls.

```text
POPULATION_MATCH=true
CUTOFF_MATCH=true
MULTIPLICITY_MATCH=true
LITERAL_SUBSET_TRANSITION=true
CURRENT_N2_LOWER=N2(B)>>B^(1/4)
CURRENT_N2_UPPER=N2(B)<<_epsilon B^(1/2+epsilon)
ALL_DIRECTIONAL_QUARTER_POWER_LOWER=true
TRUE_N2_EXPONENT_IDENTIFIED=false
MATCHING_HALF_POWER_LOWER_PROVED=false
STRICT_SUB_SQRT_WHOLE_FAMILY_UPPER_PROVED=false
STAGE26_M3_LOWER_TRANSFERRED_TO_N2=false
FINITE_DATA_USED_AS_ASYMPTOTIC_PROOF=false
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=20
MERGE_ALLOWED=false
PERFECT_CUBOID_CONCLUSION=NONE
NEXT_EXPECTED_COMMAND=Stage27-audit
```
