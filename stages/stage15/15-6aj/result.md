# Stage15-6aj — exact physical height bridge for the genus-one receiver

Base: merged Stage15-6ai (`PR #841`, merge commit `cad267c7`). Stage15-6ai classified every physical low-core one-point receiver as a smooth geometrically integral genus-one complete intersection of two quadrics in `P^3`. Its open gate was the exact relation between the physical cutoff `R<=B`, the Gaussian-square coordinates `(z,w)`, and the coefficient/height size of the moving curve.

Stage15-6aj closes that bridge. No genus-one counting theorem is applied.

## 1. Exact raw gcd factorization

For primitive positive toric pairs

\[
(m,n)=1,\qquad (r,s)=1,
\]

write

\[
h_\alpha=\gcd(mr,ns),\qquad h_\beta=\gcd(ms,nr).
\]

The raw shared-edge coordinates are

\[
E=4mnrs,
\quad X=2rs(m^2-n^2),
\quad Y=2mn(r^2-s^2),
\]

and `G=gcd(E,X,Y)`.

Prime by prime, every odd prime entering `G` must divide exactly one member of `(m,n)` and exactly one member of `(r,s)`. Its valuation is therefore exactly the minimum valuation in one of the four cross gcds. Since

\[
h_\alpha=\gcd(m,s)\gcd(n,r),
\qquad
h_\beta=\gcd(m,r)\gcd(n,s),
\]

the odd part of `G` is the odd part of `h_alpha h_beta`.

At `2`, primitive pairs are either odd-odd or mixed parity. Direct valuation gives

\[
\boxed{G=\gamma h_\alpha h_\beta,}
\]

where

\[
\boxed{
\gamma=
\begin{cases}
4,&m,n,r,s\text{ all odd},\\
2,&\text{otherwise}.
\end{cases}}
\]

This identity is exact; `G` is no longer an uncontrolled raw/physical scaling variable on the low-core square-lift receiver.

```text
STAGE15_6AJ_RAW_GCD_FACTORIZATION=true
STAGE15_6AJ_G_OVER_CROSS_GCD_PRODUCT_IN={2,4}
```

## 2. Exact physical height factorization

Merged 6ac/6ad write

\[
\alpha_0=\frac{mr+i ns}{h_\alpha}=K_\alpha z^2,
\qquad
\beta_0=\frac{ms+i nr}{h_\beta}=K_\beta w^2,
\]

with

\[
N(K_\alpha)=N(K_\beta)=k.
\]

Put

\[
Z=N(z)=|z|^2,
\qquad
W=N(w)=|w|^2.
\]

Then the Stage15-4 factors satisfy

\[
A=h_\alpha^2 k Z^2,
\qquad
B_0=h_\beta^2 k W^2.
\]

The raw space diagonal is

\[
R_{\rm raw}=2\sqrt{AB_0}=2h_\alpha h_\beta kZW.
\]

Dividing by the exact gcd above gives

\[
\boxed{
R=\frac{2}{\gamma}kZW.
}
\]

Equivalently,

```text
gamma=2 -> R=kZW
gamma=4 -> R=kZW/2
```

Hence the physical cutoff is exactly a Gaussian norm hyperbola:

\[
\boxed{kZW\le2B.}
\]

No raw toric box and no unknown `G` remains in this upper-height receiver.

```text
STAGE15_6AJ_EXACT_PHYSICAL_HEIGHT_FACTORIZATION=true
STAGE15_6AJ_PHYSICAL_HEIGHT_FORMULA=R=(2/gamma)*k*N(z)*N(w)
STAGE15_6AJ_PRODUCT_HEIGHT_CUTOFF=k*N(z)*N(w)<=2B
```

## 3. Projective point height

Because `Z,W>=1`, every physical point satisfies

\[
Z\le\frac{2B}{k},
\qquad
W\le\frac{2B}{k}.
\]

Therefore for the integral projective representative

\[
[a:b:u:v],\qquad z=a+ib,\quad w=u+iv,
\]

we have

\[
\boxed{
H_{\rm naive}:=\max(|a|,|b|,|u|,|v|)
\le \sqrt{2B/k}
\le \sqrt{2B}.
}
\]

More importantly, the physical cutoff is not merely a max-height ball; it retains the sharper product relation `kZW<=2B`. Any future determinant/elliptic argument should preserve this dyadic product structure rather than immediately replace it by the weaker `H_naive<=sqrt(2B)`.

## 4. Coefficient size of the exact two-quadric model

Write

\[
K_\alpha=A+iB_1,
\qquad
K_\beta=C+iD,
\qquad A^2+B_1^2=C^2+D^2=k.
\]

The exact quadrics from 6ai have coefficients built from

```text
M=mn h_beta,
H=h_alpha,
m^2,n^2,
A,B_1,C,D.
```

From the physical inverse under `R<=B`, merged 6ab gives

\[
m,r\le2B,\qquad n,s\le B.
\]

Thus

\[
h_\alpha\le ns\le B^2,
\qquad
h_\beta\le\min(ms,nr)\le2B^2.
\]

The exact product-height formula also gives `k<=2B`. Therefore

\[
|A|,|B_1|,|C|,|D|\le\sqrt{k}\le\sqrt{2B}.
\]

Consequently every coefficient of the integral two-quadric model is bounded by

\[
\boxed{H_{\rm coeff}\ll B^{9/2},}
\]

and in particular by a uniform integral polynomial envelope

\[
\boxed{H_{\rm coeff}\ll B^5.}
\]

This is sufficient to state an external theorem species without hidden superpolynomial coefficient growth.

## 5. Pencil discriminant marker

Stage15-6ai uses

\[
s_0=m^2+n^2,
\qquad d_0=m^2-n^2,
\]

and the nondegeneracy marker

\[
\Delta_{\rm pencil}^*=d_0^2s_0^2(s_0^2-d_0^2)^2.
\]

Under the same physical bounds,

\[
0<\Delta_{\rm pencil}^*\le102400 B^{16}.
\]

This is a **pencil discriminant marker**, not a claim about a minimal Weierstrass discriminant. Any future Jacobian model must account separately for changes of variables and integral minimization.

## 6. Measure and quantifier bridge

The exact Stage15 low-core count may now be described without changing the physical measure:

```text
physical survivor R<=B
-> unique toric data
-> legally charged core/orientation/cross-gcd decoration
-> integral point [a:b:u:v] on the exact smooth (2,2) genus-one curve
-> k*N(z)*N(w)<=2B
-> all positivity/primitivity/canonical/exactly-two masks retained
```

Thus 6aj proves the forward height adapter needed for **upper bounds**. It does not claim that every rational point of projective height `<=sqrt(2B/k)` corresponds to a physical object; physical masks remain monotone postfilters under AR-030.

## 7. What this does not yet solve

Even with a uniform per-curve rational-point bound, summing naively over all outer pairs `(m,n)` would change the proof accounting and can be far too large. Stage15-6ai already showed that the curve moves with `m/n`.

Therefore 6aj does not yet apply a determinant-method or elliptic-rank theorem. The next exact question is whether the outer pair is actually an independent family parameter after the Gaussian-square coordinates are retained, or whether it reconstructs from the point itself.

```text
STAGE15_6AJ_GENUS_ONE_COUNTING_THEOREM_APPLIED=false
STAGE15_6AJ_NAIVE_SUM_OVER_OUTER_CURVES_LICENSED=false
```

## 8. Frozen exit

```text
STAGE15_6_SUBSTAGE=6aj
STAGE15_6AJ_STARTING_GATE=PHYSICAL_TO_GENUS_ONE_HEIGHT_ADAPTER
STAGE15_6AJ_RAW_GCD_FACTORIZATION=true
STAGE15_6AJ_GAMMA_VALUES=2,4
STAGE15_6AJ_EXACT_PHYSICAL_HEIGHT_FACTORIZATION=true
STAGE15_6AJ_PRODUCT_HEIGHT_CUTOFF=k*N(z)*N(w)<=2B
STAGE15_6AJ_PROJECTIVE_HEIGHT_BOUND=sqrt(2B/k)
STAGE15_6AJ_COEFFICIENT_HEIGHT_BOUND=O(B^5)
STAGE15_6AJ_PENCIL_DISCRIMINANT_MARKER_BOUND=O(B^16)
STAGE15_6AJ_FORWARD_HEIGHT_MEASURE_ADAPTER_PROVED=true
STAGE15_6AJ_GENUS_ONE_COUNTING_THEOREM_APPLIED=false
STAGE15_6AJ_NAIVE_SUM_OVER_OUTER_CURVES_LICENSED=false
STAGE15_6AJ_LOW_CORE_GLOBAL_COUNT_PROVED=false
STAGE15_6AJ_EXIT=EXACT_PRODUCT_HEIGHT_AND_OUTER_RECONSTRUCTION_AUDIT_READY
```

Stage15-6aj stops at the exact height bridge.