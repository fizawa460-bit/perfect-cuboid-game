# Stage15-6ap - two-sided kappa-fiber coupling and fixed-k 5/8 bound

Base: Stage15-6ao in the current cycle. Stage15-6ao proved the uniform pointwise one-state estimate

\[
M_K(\kappa;Z)
\ll_\varepsilon B^\varepsilon k^{1/8}Z^{1/4}
\]

for every fixed norm core `k`, Gaussian orientation `K`, coordinate core `kappa`, and dyadic Gaussian norm scale `N(z)~Z`.

Stage15-6ap combines the two Gaussian states that must share the same `kappa`. The key bookkeeping point is that `kappa` is unique for each one-state point, so its number of possible values is never multiplied into the estimate.

## 1. Fiber notation

Fix

```text
squarefree norm core k
Gaussian core orientations K_alpha,K_beta with norm k
dyadic N(z)~Z, N(w)~W
```

inside

\[
kZW\le 2B.
\]

Let

\[
A_\kappa
=\#\{z:\ N(z)\asymp Z,\ \operatorname{sf}(x(z)y(z))=\kappa\},
\]

\[
B_\kappa
=\#\{w:\ N(w)\asymp W,\ \operatorname{sf}(p(w)q(w))=\kappa\}.
\]

A compatible Stage15 pair must occur in the diagonal coupling

\[
\sum_\kappa A_\kappa B_\kappa.
\]

All final physical masks only reduce this sum.

## 2. L-infinity bounds from 6ao

Uniformly in `kappa`,

\[
\boxed{
A_\kappa\ll B^\varepsilon k^{1/8}Z^{1/4},
\qquad
B_\kappa\ll B^\varepsilon k^{1/8}W^{1/4}.
}
\]

Write

\[
U_Z=B^\varepsilon k^{1/8}Z^{1/4},
\qquad
U_W=B^\varepsilon k^{1/8}W^{1/4}.
\]

## 3. L1 host mass has no kappa multiplicity

Every primitive `z` has one uniquely determined coordinate core `kappa`. Therefore

\[
\sum_\kappa A_\kappa\ll Z,
\qquad
\sum_\kappa B_\kappa\ll W,
\]

because a primitive Gaussian annulus of norm scale `Z` contains `O(Z)` lattice points, and similarly for `W`.

This is a host count, not an arithmetic saving.

Consequently the crude diagonal couplings already satisfy

\[
\sum_\kappa A_\kappa B_\kappa
\ll \min(U_ZW,U_WZ).
\]

No factor `#\{kappa\}` occurs.

## 4. Symmetric energy coupling

Since `A_kappa,B_kappa` are nonnegative,

\[
\sum_\kappa A_\kappa^2
\le (\max_\kappa A_\kappa)\sum_\kappa A_\kappa
\ll U_ZZ,
\]

and similarly

\[
\sum_\kappa B_\kappa^2\ll U_WW.
\]

Cauchy-Schwarz gives

\[
\sum_\kappa A_\kappa B_\kappa
\le
\left(\sum A_\kappa^2\right)^{1/2}
\left(\sum B_\kappa^2\right)^{1/2}.
\]

Hence

\[
\boxed{
N_k(Z,W)
\ll_\varepsilon
B^\varepsilon k^{1/8}(ZW)^{5/8}.
}
\]

This bound is symmetric in the two Gaussian states and applies to **any subset of coordinate cores**, in particular the small-`kappa` branch left by 6am.

```text
STAGE15_6AP_SMALL_KAPPA_FIXED_K_COUNT_PROVED=true
STAGE15_6AP_FIXED_K_DYADIC_BOUND=k^(1/8)*(Z*W)^(5/8)*B^epsilon
```

## 5. Insert the exact physical product height

Stage15-6aj proved

\[
kZW\le2B.
\]

Therefore

\[
k^{1/8}(ZW)^{5/8}
\le
2^{5/8}B^{5/8}k^{1/8-5/8}.
\]

Thus every fixed-`k`, fixed-orientation, fixed-dyadic block satisfies

\[
\boxed{
N_k(Z,W)
\ll_\varepsilon
B^{5/8+\varepsilon}k^{-1/2}.
}
\]

This is the first quantitative closure of the formerly open small-`kappa` branch.

It is weaker than the 6am square-root bound on the large-`kappa` subset, but it works uniformly with no lower bound on `kappa`, including `kappa=1`.

## 6. Relation to the large-kappa branch

The two valid estimates are now

```text
large coordinate core kappa^2 >= ZW:
  N << (ZW)^(1/2) B^o(1)                         [6am]

all kappa, hence also small coordinate core:
  N << k^(1/8) (ZW)^(5/8) B^epsilon             [6ap]
```

So the coordinate-core dichotomy no longer contains an uncounted branch.

```text
STAGE15_6AP_COORDINATE_CORE_DICHOTOMY_QUANTITATIVELY_CLOSED=true
```

## 7. What remains is the norm-core aggregation

The estimate above is still conditioned on the common norm core `k`. The Gaussian orientations of one fixed `k` cost only

\[
r_2(k)^2=B^{o(1)},
\]

but the **number of possible norm cores `k`** is not `B^o(1)`.

A naive sum of

\[
B^{5/8}k^{-1/2}
\]

over all polynomially possible `k` is not a legal thinning proof and can lose a polynomial power. Uniqueness of `k` per physical point prevents double counting, but does not by itself bound the total diagonal mass over all `k`.

Thus the next obstruction is no longer genus-one geometry or coordinate-core density. It is:

```text
GLOBAL_NORM_CORE_DIAGONAL_AGGREGATION_UNDER_PRODUCT_HEIGHT
```

Stage15-6aq must audit whether the already-proved low/high norm-core machinery from 6aa-6ac, the Stage14 Arsenal, or a new uniform theorem can control this final `k` aggregation without recharging the same norm-core information.

## 8. Firewalls

```text
AR-016=finite K orientations and dyadic partitions only
AR-023/024=global Gaussian measure retained
AR-027=not needed for the pointwise Heath-Brown input
AR-028=coordinate core kappa charged once; norm core k not recharged here
AR-030=physical masks remain postfilters
```

No claim is made that `sum_k k^(-1/2)` is subpolynomial.

## 9. Frozen exit

```text
STAGE15_6_SUBSTAGE=6ap
STAGE15_6AP_STARTING_GATE=TWO_SIDED_KAPPA_FIBER_COUPLING
STAGE15_6AP_KAPPA_VALUE_COUNT_MULTIPLIED=false
STAGE15_6AP_SMALL_KAPPA_FIXED_K_COUNT_PROVED=true
STAGE15_6AP_FIXED_K_DYADIC_BOUND=k^(1/8)*(Z*W)^(5/8)*B^epsilon
STAGE15_6AP_FIXED_K_PHYSICAL_BOUND=B^(5/8+epsilon)*k^(-1/2)
STAGE15_6AP_COORDINATE_CORE_DICHOTOMY_QUANTITATIVELY_CLOSED=true
STAGE15_6AP_NORM_CORE_GLOBAL_SUM_PROVED=false
STAGE15_6AP_LOW_CORE_GLOBAL_COUNT_PROVED=false
STAGE15_6AP_CAUSAL_THINNING_EXPONENT_DERIVED=false
STAGE15_6AP_EXIT=GLOBAL_NORM_CORE_AGGREGATION_AUDIT_READY
```
