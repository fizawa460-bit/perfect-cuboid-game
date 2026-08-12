# Stage15-6bd — eliminate the global norm-core sum by the physical diagonal product

Base: merged Stage15-6bc (`PR #850`, merge commit `9f0e284b`). The previous exit isolated a weighted same-twist / same-2-descent-cell second-moment gate. Before importing such a theorem, 6bd asks whether the moving norm core `k` is actually an independent summation variable in the exact squareclass coordinates.

Audit/advance verdict: `PASS`.

## 1. One-state quartic value determines k

For one retained coordinate-squareclass state, write

\[
f=\kappa_f c^2,\qquad g=\kappa_g e^2,
\qquad (\kappa_f,\kappa_g)=1,
\qquad \kappa_f\kappa_g=\kappa,
\]

with the exact norm equation from 6ao/6bb

\[
\boxed{F:=f^2+g^2=\kappa_f^2c^4+\kappa_g^2e^4=kZ^2.}
\]

Here `k` is squarefree. Therefore

\[
\boxed{k=\operatorname{sf}(F),\qquad Z=\sqrt{F/k}.}
\]

So `k` is reconstructed from the quartic value and is not a free outer parameter.

## 2. Two-state common-k condition is one product-square equation

For the two retained states define

\[
F_1=kZ^2,\qquad F_2=kW^2.
\]

For positive integers, equality of squarefree parts is equivalent to their product being a square. Hence

\[
\boxed{\operatorname{sf}(F_1)=\operatorname{sf}(F_2)
\iff F_1F_2=S^2}
\]

for a unique positive integer `S`. On an actual Stage15 pair,

\[
\boxed{S=\sqrt{F_1F_2}=kZW.}
\]

Conversely, a pair of one-state quartic values with `F_1F_2` square automatically reconstructs the common squarefree norm core

\[
k=\operatorname{sf}(F_1)=\operatorname{sf}(F_2).
\]

No summation over unrelated norm cores remains.

## 3. Exact physical height

Stage15-6aj proved

\[
R=\frac{2}{\gamma}kZW,
\qquad \gamma\in\{2,4\},
\]

where `gamma` is the projective 2-primary normalization. Therefore

\[
\boxed{S=kZW=\frac{\gamma}{2}R.}
\]

Thus the physical cutoff `R<=B` gives the exact absolute cutoff

\[
\boxed{S\le2B.}
\]

More precisely, `S=R` in the `gamma=2` branch and `S=2R` in the `gamma=4` branch.

## 4. New global receiver

After the already-proved unique coordinate squareclass decompositions, the remaining global condition can be written as

```text
choose two primitive one-state coordinate pairs
F1 = kappa_f1^2*c1^4 + kappa_g1^2*e1^4
F2 = kappa_f2^2*c2^4 + kappa_g2^2*e2^4
with the same coordinate core
kappa_f1*kappa_g1 = kappa_f2*kappa_g2 = kappa
and
F1*F2 = S^2,  S <= 2B.
```

The common norm core is then reconstructed as `sf(F1)=sf(F2)`. This receiver preserves the physical product height and does not replace the physical measure by a scalar proxy.

## 5. Proof-accounting consequence

The obstruction from 6ap/6aq should no longer be phrased as a polynomial sum

\[
\sum_k B^{5/8}k^{-1/2}.
\]

That sum arose from conditioning first on `k`. In the exact global coordinates, `k` is a derived squarefree kernel of `F_1,F_2`.

This does **not** yet prove the desired half-power bound. It removes an artificial outer summation and replaces it by a single product-square support condition.

```text
AR-023=PASS_PHYSICAL_PAIR_MEASURE_RETAINED
AR-024=PASS_NO_CONDITIONED_MEASURE_PROMOTION
AR-028=PASS_k_IS_RECONSTRUCTED_NOT_RECHARGED
```

## 6. Frozen exit

```text
STAGE15_6_SUBSTAGE=6bd
STAGE15_6BD_AUDIT_VERDICT=PASS
STAGE15_6BD_ONE_STATE_k_RECONSTRUCTED_FROM_F=true
STAGE15_6BD_COMMON_k_EQUIVALENT_TO_PRODUCT_SQUARE=true
STAGE15_6BD_GLOBAL_RECEIVER=F1*F2=S^2
STAGE15_6BD_PHYSICAL_DIAGONAL_PRODUCT=S=k*Z*W
STAGE15_6BD_PHYSICAL_CUTOFF=S<=2B
STAGE15_6BD_EXPLICIT_SUM_OVER_k_ELIMINATED=true
STAGE15_6BD_HALF_POWER_COUNT_PROVED=false
STAGE15_6BD_EXIT=FIXED_PHYSICAL_DIAGONAL_FIBER_AUDIT_READY
```

Next: Stage15-6be audits the multiplicity above a fixed `S` before any external second-moment theorem is imported.
