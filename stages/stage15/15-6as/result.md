# Stage15-6as — audit of quadratic-twist canonical-height transfer

Base: Stage15-6ar in the current cycle. Stage15-6ar proved that every small-coordinate-core quartic has exact Jacobian

\[
E_d:\ y^2=x^3-d^2x,
\qquad d=sf(2k\kappa).
\]

Stage15-6as audits whether a known quadratic-twist canonical-height lower bound can be used immediately to count Stage15 points.

This is deliberately an **audit stage**.

## 1. Candidate theorem

The targeted source is Tadahisa Nara, *Lower bounds of the canonical height on quadratic twists of elliptic curves*, Rocky Mountain J. Math. 44 (2014), arXiv:1110.6710.

Nara Theorem 1.1 considers a fixed integral model

\[
E:y^2=x^3+a_2x^2+a_4x+a_6
\]

with discriminant `Delta`, assumes `Delta` is sixth-power-free, and gives an explicit lower bound on non-2-torsion rational points on the squarefree quadratic twists `E_D`.

Nara Remark 1.2 also records the more general non-explicit shape

\[
\hat h(P)>\frac14\log|D|+O(1)
\]

from the standard theory of quadratic twists.

## 2. Direct Nara Theorem 1.1 does not match the Stage15 base curve

The Stage15 Jacobians are twists of

\[
E_1:y^2=x^3-x.
\]

For this integral minimal model

\[
\Delta(E_1)=64=2^6.
\]

Hence its discriminant is **not** sixth-power-free in the literal sense required by Nara Theorem 1.1.

Therefore

```text
NARA_THEOREM_1_1_DIRECTLY_APPLICABLE=false
```

No attempt is made to suppress this bad prime or silently alter the hypothesis. An isomorphic rational model does not by itself supply a new integral fixed model satisfying the stated theorem hypothesis.

## 3. The non-explicit general height shape is still not an immediate Stage15 count

Even if one uses the general quadratic-twist lower-bound species

\[
\hat h(P)\ge c\log|d|-C
\]

for non-torsion points of `E_d`, two exact adapters are still missing.

### 3.1 Stage15 points live first on a 2-covering

The binary quartic

\[
\kappa T^2=F_K(a,b)
\]

is a genus-one 2-covering whose Jacobian is `E_d`. A rational point on the quartic is not literally an `(x,y)` point on `E_d`.

A future use of canonical height must provide an explicit covering map

\[
\pi:C_{K,\kappa}\to E_d
\]

or an equivalent height-compatible identification.

### 3.2 The image must be in the theorem's point class

Nara's theorem excludes 2-torsion. A soluble 2-covering can represent a rational class whose chosen image under a covering/translation can interact with torsion. Stage15 has not proved that every counted quartic point maps to a non-2-torsion point in a fixed, counting-compatible manner.

Thus

```text
STAGE15_QUARTIC_POINT_TO_NONTORSION_TWIST_POINT_PROVED=false
```

## 4. Height lower bounds alone do not aggregate twists

Even after a future covering-height bridge, a lower bound on the minimum canonical height of non-torsion points does not by itself bound the number of twist parameters `d` supporting Stage15 points.

The family `y^2=x^3-d^2x` is the congruent-number twist family; many twists can have rational points. What Stage15 needs is a theorem that counts the **special low-height covering points with the original `(k,kappa)` and product-height constraints**, not merely a per-twist minimum-height statement.

Therefore the direct implication

```text
twist-height lower bound
-> global norm-core aggregation
```

is invalid.

## 5. Audit verdict

```text
AUDIT_STAGE=Stage15-6as
AUDIT_TARGET=J1728_QUADRATIC_TWIST_HEIGHT
AUDIT_VERDICT=BLOCK
EXACT_TWIST_PARAMETER_AVAILABLE=true
NARA_THEOREM_1_1_DIRECTLY_APPLICABLE=false
BLOCK_REASON_1=BASE_DISCRIMINANT_64_NOT_SIXTH_POWER_FREE
GENERAL_QUADRATIC_TWIST_HEIGHT_SHAPE_AVAILABLE=true
COVERING_MAP_HEIGHT_ADAPTER_PROVED=false
NONTORSION_IMAGE_PROVED=false
TWIST_HEIGHT_ALONE_AGGREGATES_d=false
GLOBAL_NORM_CORE_SUM_PROVED=false
```

This `BLOCK` is an applicability verdict, not a theorem that twist arithmetic cannot help.

## 6. Next exact question

Before searching another elliptic theorem, retain the original 6ac branch condition and ask whether the **already-proved low-norm-core size inequality itself** gives enough extra decay in `k` after the 6ar twist repackaging.

That is Stage15-6at. It is an internal accounting audit and does not require another external theorem.

## 7. Frozen exit

```text
STAGE15_6_SUBSTAGE=6as
STAGE15_6AS_AUDIT=true
STAGE15_6AS_AUDIT_VERDICT=BLOCK
STAGE15_6AS_NARA_DIRECT_APPLICABLE=false
STAGE15_6AS_GENERAL_HEIGHT_ROUTE_NOT_CLOSED=true
STAGE15_6AS_COVERING_HEIGHT_ADAPTER_PROVED=false
STAGE15_6AS_GLOBAL_TWIST_COUNT_PROVED=false
STAGE15_6AS_EXIT=LOW_CORE_BRANCH_MEMORY_ACCOUNTING_AUDIT_READY
```