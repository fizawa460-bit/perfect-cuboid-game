# Stage15-6am — coordinate-core size dichotomy and small-kappa quartic gate

Base: Stage15-6al in the same cycle. Stage15-6al produced the new squarefree coordinate-product core

\[
\kappa=\operatorname{sf}(xy)=\operatorname{sf}(pq),
\qquad (k,\kappa)=1,
\]

and proved that its odd part is a legal primitive root-line modulus for both Gaussian pairs. Stage15-6am turns this into a quantitative large-`kappa` estimate and classifies the small-`kappa` remainder.

## 1. Fixed dyadic global block

Fix

```text
squarefree norm core k
finite Gaussian core orientations K_alpha,K_beta
N(z)~Z
N(w)~W
```

inside the exact physical product-height range

\[
kZW\ll B
\]

(and in fact `kZW<=2B` by 6aj).

For each primitive `z`, the value

\[
\kappa(z)=\operatorname{sf}\left(
\Re(K_\alpha z^2)\Im(K_\alpha z^2)
\right)
\]

is uniquely determined. A compatible `w` must have the **same** `kappa` by 6ak/6al.

Thus there is no polynomial sum over candidate `kappa` for a fixed anchor: `kappa` is point-generated but is shared by the two one-point coordinate products, and 6al proves it is a new core disjoint from the old norm core `k`.

## 2. Fixed-anchor root-line count

Fix `z`, hence fix its actual `kappa`. After the `B^o(1)` primewise coordinate-cell/root allocation, the odd part of `kappa` places `w=(u,v)` on one primitive root line modulo `kappa^circ`.

In a dyadic Gaussian box with norm scale `W`, the underlying two-dimensional box has area `O(W)`. Therefore the Stage15 root-line lattice estimate gives

\[
\boxed{
\#\{w:\kappa(w)=\kappa(z)\}
\ll B^{o(1)}\left(1+\frac{W}{\kappa}\right),
}
\]

where the possible factor two between `kappa` and its odd part is absorbed into the constant.

There are `O(Z)` primitive `z` in the corresponding dyadic norm annulus, so for the branch `kappa>=L`, anchoring on `z` gives

\[
\ll B^{o(1)}\left(Z+\frac{ZW}{L}\right).
\]

By symmetry, anchoring on `w` gives

\[
\ll B^{o(1)}\left(W+\frac{ZW}{L}\right).
\]

Taking the better complete count yields

\[
\boxed{
N_{\kappa\ge L}(k;Z,W)
\ll B^{o(1)}
\left(\min(Z,W)+\frac{ZW}{L}\right).
}
\]

This is a genuine global-coordinate estimate: no outer toric-pair sum has been inserted.

## 3. Square-root collapse on the large coordinate-core branch

Choose the dyadic threshold

\[
L\ge\sqrt{ZW}.
\]

Then

\[
\min(Z,W)\le\sqrt{ZW},
\qquad
\frac{ZW}{L}\le\sqrt{ZW},
\]

so

\[
\boxed{
N_{\kappa^2\ge ZW}(k;Z,W)
\ll (ZW)^{1/2}B^{o(1)}.
}
\]

Using `kZW<=2B`, this is

\[
\boxed{
N_{\kappa^2\ge ZW}(k;Z,W)
\ll (B/k)^{1/2}B^{o(1)}.
}
\]

This is a **fiberwise square-root collapse in the two-Gaussian support**. It is not yet a whole-family `B^{1/2}` theorem because 6am does not sum the moving norm core `k` or the complementary small-`kappa` branch.

```text
STAGE15_6AM_LARGE_COORDINATE_CORE_BOUND=true
STAGE15_6AM_LARGE_COORDINATE_CORE_SQRT_COLLAPSE=true
```

## 4. Exact small-kappa one-point quartic

The remaining branch is

\[
\boxed{\kappa^2<ZW.}
\]

For one Gaussian core `K=A+iB_1` and primitive `z=a+ib`, define

\[
f_K(a,b)=A(a^2-b^2)-2B_1ab,
\]

\[
g_K(a,b)=B_1(a^2-b^2)+2Aab.
\]

The coordinate-core condition is exactly

\[
\boxed{
f_K(a,b)g_K(a,b)=\kappa t^2}
\]

for some integer `t`.

On the affine chart `b=1`, the two quadratic factors are

\[
f(t)=At^2-2B_1t-A,
\]

\[
g(t)=B_1t^2+2At-B_1.
\]

Their discriminants and resultant are

\[
\boxed{\operatorname{disc}(f)=\operatorname{disc}(g)=4k,}
\]

\[
\boxed{\operatorname{Res}(f,g)=-4k^2.}
\]

Since `k>0`, each quadratic has two distinct roots over `Qbar` and the two root sets are disjoint. Therefore the binary quartic `f_K g_K` has four distinct projective roots.

Consequently the double cover

\[
\boxed{\mathcal E_{K,\kappa}:\ \kappa T^2=f_K(a,b)g_K(a,b)}
\]

is a smooth geometrically integral genus-one quartic over `Qbar`.

This is a **one-point** genus-one receiver, smaller than the two-quadric family of 6ai. The small-`kappa` population consists of two such one-point quartic conditions, for `K_alpha,z` and `K_beta,w`, sharing the same small `kappa`, coupled only through

\[
kN(z)N(w)\le2B
\]

and the reconstructed physical masks.

```text
STAGE15_6AM_SMALL_KAPPA_ONE_POINT_QUARTIC=true
STAGE15_6AM_SMALL_KAPPA_QUARTIC_GEOMETRIC_GENUS=1
```

## 5. Why this is the natural cycle stop

The exact algebraic reductions have now produced two clean branches:

```text
kappa^2 >= ZW
  -> primitive root-line spacing
  -> (ZW)^(1/2) * B^o(1) per fixed k/dyadic/core block

kappa^2 < ZW
  -> smooth one-point quartic genus-one receiver
  -> no further unused exact square parameter or common-support modulus identified
```

The second branch is no longer blocked by ambiguity about the physical height, moving outer curve index, core recharge, or singular/conic degeneration. Its next step is a genuine counting/theorem audit for a moving quartic family under the exact hyperbola measure.

Opening that analytic theorem species is a different phase, so the requested `Stage15-6-cycle` stops here rather than silently importing a determinant-method, rank, Selmer, or averaged-curve theorem.

## 6. Arsenal / proof-accounting verdict

```text
AR-009=ACTIVE_ON_LARGE_COORDINATE_CORE
AR-016=FINITE_CORE/CELL/ROOT_MULTIPLICITY_ONLY
AR-010=GLOBAL_OUTER_RECONSTRUCTION_ALREADY_CONSUMED
AR-023/024=GLOBAL_MEASURE_PRESERVED
AR-027=MANDATORY_IF_AVERAGED_GENUS_ONE_THEOREM_IS_CONSIDERED_NEXT
AR-028=PASS; kappa IS COPRIME TO AND DISTINCT FROM k
AR-030=PHYSICAL_MASKS_REMAIN_POSTFILTERS
```

Stage14-s7-48/sH48 remain useful warning analogies for Gaussian coordinate-product correlations, but their balanced Stage14 packet theorem species is not the same as the present small-`kappa` quartic-hyperbola family.

## 7. Frozen exit

```text
STAGE15_6_SUBSTAGE=6am
STAGE15_6AM_STARTING_GATE=COORDINATE_CORE_SIZE_DICHOTOMY
STAGE15_6AM_FIXED_ANCHOR_KAPPA_IS_UNIQUE=true
STAGE15_6AM_LARGE_COORDINATE_CORE_BOUND=true
STAGE15_6AM_LARGE_COORDINATE_CORE_BOUND_FORM=min(Z,W)+ZW/L
STAGE15_6AM_LARGE_COORDINATE_CORE_SQRT_COLLAPSE=true
STAGE15_6AM_HIGH_BRANCH_THRESHOLD=kappa^2>=Z*W
STAGE15_6AM_SMALL_KAPPA_ONE_POINT_QUARTIC=true
STAGE15_6AM_SMALL_KAPPA_QUARTIC_SEPARABLE=true
STAGE15_6AM_SMALL_KAPPA_QUARTIC_GEOMETRIC_GENUS=1
STAGE15_6AM_SMALL_KAPPA_GLOBAL_COUNT_PROVED=false
STAGE15_6AM_NORM_CORE_k_GLOBAL_SUM_PROVED=false
STAGE15_6AM_LOW_CORE_GLOBAL_COUNT_PROVED=false
STAGE15_6AM_CAUSAL_THINNING_EXPONENT_DERIVED=false
STAGE15_6AM_EXIT=LARGE_COORDINATE_CORE_CONTROLLED_SMALL_KAPPA_QUARTIC_THEOREM_GATE
```

`Stage15-6-cycle` stops at this theorem boundary.