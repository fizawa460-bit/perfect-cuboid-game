# Stage13-13fs — R07 curved-region self-contained closure

> STATUS: `STAGE13_13FS_R07_CURVED_REGION_CLOSURE`
>
> PURPOSE: close the final theorem-level R07 blocker by making the passage from local rectangular asymptotics and one-dimensional Vaaler approximation to the sharp curved physical region completely explicit in one proof-facing lemma.
>
> INPUTS: the zero/nonzero harmonic rectangle interfaces already established in Stage13, R07 Gate A (`13-13fq`) for the retained Hecke family, and R07 Gate B (`13-13fr`) for fixed-S residue refinements.
>
> SCOPE: geometry/error transfer only. No theorem constant is changed.

Write

\[
\Lambda=\log B,
\qquad
H_0=U=e^{\Lambda^{1/4}},
\qquad
\eta=\Lambda^{-8},
\qquad
L=\lfloor\Lambda^4\rfloor,
\qquad
N=64.
\]

The physical region in the outer Pythagorean variables is

\[
\mathscr D_B
=
\{(h,r,s): h(r^2+s^2)\le 2B\},
\]

with the canonical parity and coprimality conditions understood. The core is

\[
\mathscr D_B^{\rm core}
=
\mathscr D_B\cap\{h\ge H_0,\ r\ge U,\ s\ge U\}.
\]

The goal is to justify the sharp physical count from the rectangle formula with total error `o(B\Lambda^3)` and to separate three logically different boundaries:

1. Vaaler endpoints in the one-dimensional chamber angle;
2. strict canonical equality walls such as repeated sides;
3. the curved height boundary `h(r^2+s^2)=2B`.

They are treated independently below.

---

## 1. Where Vaaler acts — and where it does not

Fix a distinguished face `q`. In the `q`-adapted spherical coordinates from `13-12ag`, write

\[
x_i=\sin\theta\cos\alpha,
\qquad
x_j=\sin\theta\sin\alpha,
\qquad
x_k=\cos\theta.
\]

The Gelfand--Leray weight satisfies

\[
w_q\,d\omega=d\theta\,d\alpha.
\]

For fixed outer angle `psi=pi/2-theta`, the canonical chamber condition cuts the inner angle `alpha` into a bounded union of intervals

\[
E_q(\psi)\subset (0,\pi/2).
\]

Thus Vaaler's trigonometric majorant/minorant is applied only to the one-dimensional indicator

\[
1_{E_q(\psi)}(\alpha).
\]

It is **not** used to approximate the curved physical cutoff `h(r^2+s^2)\le2B`. That cutoff is handled separately by the multiplicative box decomposition in §§3--7.

For every interval component `I` of `E_q(\psi)`, degree `L` Vaaler polynomials satisfy

\[
P^-_{I,L}\le 1_I\le P^+_{I,L},
\]

\[
\widehat P^\pm_{I,L}(0)=|I|\pm\frac1{L+1},
\]

and for `1\le |m|\le L`,

\[
|\widehat P^\pm_{I,L}(m)|
\le
\frac1{\pi|m|}+\frac1{L+1}<1.
\]

The number of interval components of `E_q(\psi)` is uniformly bounded because the chamber inequalities are fixed algebraic comparisons among the three normalized coordinates. Hence summing interval majorants changes these bounds only by a fixed absolute factor.

### 1.1 Endpoint convention is harmless for the discrete count

A Vaaler endpoint occurs when `alpha` lies on a chamber equality wall. In the canonical integer problem these are the strict-equality exclusions (`a=b`, `b=c`, or the corresponding repeated-side degeneracies after permutation). Such records are excluded exactly by the canonical convention before asymptotics are taken.

Therefore using the midpoint value at a Vaaler discontinuity cannot add or remove a valid canonical object.

This is an exact discrete statement, not a measure-zero argument.

### 1.2 The physical cutoff is not a Vaaler endpoint

The condition `d\le B` is equivalent here to

\[
h(r^2+s^2)\le2B.
\]

It is not an endpoint of `E_q(\psi)` and is never assigned a midpoint convention. Equality at `d=B` is retained exactly because the physical count uses `\le`; boxes meeting that height boundary are handled by the shell argument in §6.

Hence

```text
VAALER_ENDPOINTS=CANONICAL_ANGLE_EQUALITY_WALLS_ONLY
PHYSICAL_CUTOFF_HANDLED_BY_VAALER=false
PHYSICAL_CUTOFF_INEQUALITY=d<=B
```

---

## 2. Wings removed before the Fourier expansion

The small-height wing satisfies, by the positive zero-mode majorant and partial summation,

\[
\sum_{h\le H_0}\frac{a_0(h)}h\ll\log H_0=\Lambda^{1/4}.
\]

With the two base channels contributing at most `\Lambda^2`, this gives

\[
\boxed{\mathcal E_{\rm small\,h}\ll B\Lambda^{9/4}}.
\]

Similarly

\[
\sum_{r\le U}\frac{b_0(r)}r\ll(\log U)^2=\Lambda^{1/2},
\]

and the union of `r<U` and `s<U` gives

\[
\boxed{\mathcal E_{\rm small\,coord}\ll B\Lambda^{5/2}}.
\]

Both are `o(B\Lambda^3)`. We remove these wings before inserting Vaaler. Consequently every retained nonzero harmonic is analyzed only on the core where all three multiplicative variables are at least `e^{\Lambda^{1/4}}`; this is the source of the stretched-exponential saving used later.

---

## 3. Multiplicative mesh and exact box count

Partition each positive coordinate into half-open multiplicative intervals

\[
[e^{j\eta},e^{(j+1)\eta}).
\]

Every point of `\mathscr D_B` has

\[
h\le B,
\qquad
r,s\le\sqrt{2B}<2B.
\]

Thus one coordinate needs at most

\[
1+\left\lceil\frac{\log(2B/H_0)}\eta\right\rceil
\le
2+\frac{\log(2B)}\eta
=
O(\Lambda^9)
\]

intervals. The deliberately crude three-coordinate bound is therefore

\[
\boxed{N_{\rm box}=O(\Lambda^{27}).}
\]

No curvature saving is used in this count. Ignoring the curved constraint only increases the number of boxes and is therefore safe for all subsequent upper bounds.

```text
MESH_PER_COORD=O(log(2B)/eta)=O((log B)^9)
BOX_COUNT=O((log B)^27)
```

---

## 4. Uniform rectangle remainder on every core box

Consider a box

\[
\mathcal R(H,R,S):
H<h\le e^\eta H,
\quad
R<r\le e^\eta R,
\quad
S<s\le e^\eta S.
\]

Assume it meets `\mathscr D_B`. Since

\[
F(h,r,s):=h(r^2+s^2)
\]

changes by at most `e^{3\eta}` on one such box,

\[
H(R^2+S^2)\ll B.
\]

Using `2RS\le R^2+S^2`,

\[
\boxed{HRS\ll B}
\]

uniformly for every core box meeting the physical region.

The zero-mode finite-order Perron expansions have remainder order `N=64`. A remainder in the `h` channel costs at worst

\[
H\Lambda^{-64}\cdot R\Lambda\cdot S\Lambda
\ll B\Lambda^{-62}.
\]

A remainder in a base channel leaves at most one other base logarithm and is no larger; products of two or more remainder terms are smaller. The mixed Wiener correction has finite logarithmic moments, so fixed convolution shifts preserve this uniform estimate.

Hence every core box satisfies

\[
\boxed{\mathcal E_{64}(\mathcal R)\ll B\Lambda^{-62}}.
\]

Summing even this worst-case estimate over all `O(\Lambda^{27})` boxes gives

\[
\boxed{
\mathcal E_{\rm finite,total}
\ll B\Lambda^{-35}.
}
\]

This is why the per-box endpoint error is uniform even for boxes close to the curved boundary: the only geometric input used in the bound is the uniform consequence `HRS\ll B` of intersecting the physical region.

```text
FINITE_REMAINDER_N=64
PER_BOX_FINITE_REMAINDER=O(B(log B)^-62)
FINITE_REMAINDER_AFTER_ALL_BOXES=O(B(log B)^-35)
```

---

## 5. Rectangle power tails after all boxes

Fix `epsilon=1/16`. The rectangle power-tail interface is

\[
\mathcal E_{\rm pow}(\mathcal R)
\ll
\Lambda^{C_{\rm rect}}
\bigl(
H^{3/4+\epsilon}RS
+HR^{3/4+\epsilon}S
+HRS^{3/4+\epsilon}
\bigr).
\]

Because `1/4-\epsilon=3/16`, `HRS\ll B`, and every core coordinate is at least `e^{\Lambda^{1/4}}`, each term is

\[
\ll
B\Lambda^{C_{\rm rect}}
\exp\{-\tfrac3{16}\Lambda^{1/4}\}.
\]

After all boxes,

\[
\boxed{
\mathcal E_{\rm pow,total}
\ll
B\Lambda^{C_{\rm rect}+27}
\exp\{-\tfrac3{16}\Lambda^{1/4}\}.
}
\]

For every fixed `A>0`, this is `o(B\Lambda^{-A})`.

---

## 6. The curved physical boundary is a thin multiplicative shell

If a box intersects `F=2B`, then throughout the whole box

\[
2Be^{-3\eta}
\le F(h,r,s)\le
2Be^{3\eta}.
\]

Thus every boundary box is contained in a shell of logarithmic thickness `6\eta`.

The cumulative zero-mode main term on a fixed parity/chamber sector is homogeneous of degree one in the height and has logarithmic degree at most three:

\[
M_q(X)=X\,P_{q,3}(\log X)+O(X\Lambda^2),
\]

where the coefficient functions in the bounded angular variables are piecewise `C^1` with bounded first derivatives. For `|\tau|\le3\eta`, the mean-value theorem gives

\[
M_q(e^\tau B)-M_q(B)
=O(|\tau|B\Lambda^3).
\]

Therefore the total main-polynomial mass of all boxes intersecting the curved boundary is

\[
O(\eta B\Lambda^3)=O(B\Lambda^{-5}).
\]

All analytic rectangle remainders from boundary boxes are already subsets of the global sums in §§4--5, so they are not counted again. Hence

\[
\boxed{
\mathcal E_{\rm boundary}
\ll
B\Lambda^{-5}
+B\Lambda^{-35}
+B\Lambda^{C_{\rm rect}+27}e^{-(3/16)\Lambda^{1/4}}.
}
\]

The equality points `F=2B` are included on the physical side because the original indicator is `1_{F\le2B}`. The shell estimate only controls the uncertainty of boxes crossing the boundary; it does not alter that exact convention.

```text
CURVED_BOUNDARY_SHELL=2B*exp(+-3eta)
CURVED_BOUNDARY_MAIN_MASS=O(B(log B)^-5)
PHYSICAL_EQUALITY_POINTS_RETAINED=true
```

---

## 7. Interior mesh variation — why there is no extra box factor

Remove the boundary-intersecting boxes. On every remaining box the physical indicator `1_{F\le2B}` is constant.

Pass to logarithmic coordinates

\[
u=\log h,
\qquad v=\log r,
\qquad w=\log s.
\]

The zero-mode main density on each fixed chamber/parity sector is piecewise `C^1`. Its integral and the integral of the absolute first derivatives are both bounded by

\[
O(B\Lambda^3).
\]

For a rectangular mesh of width at most `\eta` in each logarithmic coordinate, the cellwise mean-value estimate gives

\[
\sum_{\mathcal R\ {m interior}}
\left|
\int_{\mathcal R}f-
 f(\xi_{\mathcal R})\operatorname{vol}(\mathcal R)
\right|
\le
C\eta
\int_{\mathscr D_B^{\rm core}}
(|\partial_u f|+|\partial_v f|+|\partial_w f|).
\]

Therefore

\[
\boxed{\mathcal E_{\rm mesh}\ll\eta B\Lambda^3= B\Lambda^{-5}.}
\]

There is no factor `N_box`: the right side already sums the local variations by integrating the derivative majorant over the whole region. Multiplying once more by the number of cells would count the same total variation repeatedly.

```text
MESH_ERROR=O(B(log B)^-5)
EXTRA_BOX_FACTOR_IN_MESH_ERROR=false
```

---

## 8. Mixed logarithmic shifts are global, not per-box losses

Write the mixed correction as

\[
C_0(\mathbf s)
=
\sum_{u,v,w}
\frac{c_0(u,v,w)}{u^{s_h}v^{s_r}w^{s_s}}.
\]

The phase-uniform weighted Wiener estimate gives, for every fixed integer `m`,

\[
\sum_{u,v,w}
\frac{|c_0(u,v,w)|(1+\log(uvw))^m}{uvw}<\infty.
\]

For `0\le j\le3`,

\[
(\log(X/n))^j-(\log X)^j
=O\bigl((1+\log n)(1+\log X)^{j-1}\bigr).
\]

Thus every nonconstant convolution shift lowers the available logarithmic degree by at least one. Summing the Wiener coefficients absolutely **before** the final geometric Riemann sum yields

\[
\boxed{\mathcal E_{\rm mixed\ shift}\ll B\Lambda^2.}
\]

This term is global and must not be multiplied by `N_box`.

---

## 9. Retained Vaaler harmonics on the core

The nonzero Fourier modes are inserted only after the wings have been removed. R07 Gate A supplies fixed constants `delta_H>0`, `C_H,D_H>=0` such that, for every retained `ell>=1`,

\[
S_\ell(X)
\ll
X^{1-\delta_H}(1+\ell)^{C_H}(\log(2X))^{D_H}.
\]

Since the smallest core variable is `e^{\Lambda^{1/4}}`, the ordinary sharp-sum estimate contributes a factor

\[
e^{-\delta_H\Lambda^{1/4}}
\]

relative to the positive zero-mode scale. The two base channels contribute at most `\Lambda^2`, so one retained harmonic contributes globally

\[
\ll
B\Lambda^{D_H+2}(1+\ell)^{C_H}
e^{-\delta_H\Lambda^{1/4}}.
\]

The Vaaler coefficient is `<1` and supplies no positive harmonic power. With `L=\lfloor\Lambda^4\rfloor`,

\[
\sum_{1\le\ell\le L}(1+\ell)^{C_H}
=O(\Lambda^{4C_H+4}).
\]

Hence

\[
\boxed{
\mathcal E_{\rm harm,core}
\ll
B\Lambda^{4C_H+D_H+6}
e^{-\delta_H\Lambda^{1/4}}
=o_A(B\Lambda^{-A})
}
\]

for every fixed `A>0`.

The zero-mode Vaaler bracket excess is `O(1/L)`. Multiplying by the positive raw mass `O(B\Lambda^3)` gives

\[
\boxed{\mathcal E_{\rm Vaaler,0}\ll B\Lambda^{-1}.}
\]

The one-dimensional Fourier approximation therefore reaches the curved physical count by the following exact order:

```text
remove wings by positivity
-> fix outer angle / approximate only inner chamber intervals by Vaaler
-> evaluate rectangle zero/nonzero modes on the multiplicative core
-> sum interior boxes
-> control F=2B boundary boxes by the multiplicative shell
-> restore the sharp physical inequality F<=2B.
```

At no point is a one-dimensional Vaaler polynomial used as an approximation to the two/three-dimensional curved height boundary.

---

## 10. Complete R07 curved-region ledger

All errors are now explicit:

| source | global bound |
|---|---|
| small height | `O(B Lambda^(9/4))` |
| small base coordinate | `O(B Lambda^(5/2))` |
| Vaaler zero-mode excess | `O(B Lambda^(-1))` |
| finite Perron remainders after all boxes | `O(B Lambda^(-35))` |
| rectangle power tails | `o_A(B Lambda^(-A))` |
| curved boundary shell | `O(B Lambda^(-5))` plus already-counted rectangle remainders |
| interior mesh variation | `O(B Lambda^(-5))` |
| mixed logarithmic shifts | `O(B Lambda^2)` |
| retained nonzero harmonics | `o_A(B Lambda^(-A))` |

Every displayed error is `o(B\Lambda^3)`. Therefore the sharp physical zero-mode asymptotic and the removal of nonzero harmonics survive the passage from rectangles to the actual curved region.

In particular, if the rectangle arithmetic gives common coefficient `Theta` and chamber kernel `J_q`, then

\[
\boxed{
A_q(B)=\Theta J_qB(\log B)^3+o(B(\log B)^3).
}
\]

This gate does not recalibrate `Theta`; the Stage12 calibration remains the later independent step already fixed in R06.

---

## 11. Review-facing closure of the R06 objections

The R06 curved-region objection is closed for the following precise reasons.

1. **Box count:** per coordinate `O(log(2B)/eta)=O(\Lambda^9)`, total `O(\Lambda^27)`.
2. **Per-box uniformity:** every box meeting the physical region satisfies `HRS\ll B`, giving the same `O(B\Lambda^-62)` finite Perron bound even at the boundary.
3. **Accumulation:** `27-62=-35`.
4. **Power tails:** the core lower cutoff produces `exp(-(3/16)\Lambda^(1/4))`, surviving all box powers.
5. **Boundary:** a crossing box lies in `2Be^{-3eta}\le F\le2Be^{3eta}` and its main mass is `O(eta B\Lambda^3)`.
6. **Mesh:** total first variation, not worst-cell times cell count, gives `O(eta B\Lambda^3)`.
7. **Vaaler-to-geometry route:** Vaaler approximates only the inner angular interval indicator; the curved height condition is handled separately by boxes and a shell.
8. **Endpoints:** chamber equality walls are excluded exactly from the discrete canonical count; `F=2B` is retained exactly and is not a Vaaler endpoint.

---

## 12. Gate locks

```text
STAGE13_13FS=COMPLETE_R07_CURVED_REGION_SELF_CONTAINED_CLOSURE
R07_GATE_C=COMPLETE
R07_CURVED_REGION_FULL_LEMMA_IN_REVIEW_TARGET=true
R07_PER_BOX_UNIFORMITY_EXPLICIT=true
R07_BOUNDARY_MESH_DERIVATION_EXPLICIT=true
R07_VAALER_TO_CURVED_REGION_ROUTE_EXPLICIT=true
R07_VAALER_APPLIES_ONLY_TO_INNER_ANGLE_INTERVALS=true
R07_PHYSICAL_CUTOFF_HANDLED_BY_MULTIPLICATIVE_SHELL=true
R07_VAALER_ENDPOINT_DISCRETE_CONVENTION_EXPLICIT=true
R07_PHYSICAL_EQUALITY_POINTS_RETAINED=true
MESH_PER_COORD=O(log(2B)/eta)=O((log B)^9)
BOX_COUNT=O((log B)^27)
PER_BOX_FINITE_REMAINDER=O(B(log B)^-62)
FINITE_REMAINDER_AFTER_ALL_BOXES=O(B(log B)^-35)
POWER_TAIL_SAVING=exp(-(3/16)(log B)^(1/4))
CURVED_BOUNDARY_MAIN_MASS=O(B(log B)^-5)
MESH_ERROR=O(B(log B)^-5)
MIXED_LOG_SHIFT_BOUND=O(B(log B)^2)
RETAINED_HARMONIC_POLYLOG=4*C_H+D_H+6
R07_REPAIR_BLOCKERS_OPEN=0
R07_GATE_D_HARDENING_REMAINS=true
R06_IMMUTABLE=true
THEOREM_CHANGED=false
THEOREM_CONTRACT_REOPEN_REQUIRED=false
PROMOTE_TO_13_13G=false
NEXT=13-13ft
```
