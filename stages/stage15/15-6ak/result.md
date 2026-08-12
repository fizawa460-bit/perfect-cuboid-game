# Stage15-6ak — reconstruct the moving toric outer pair from the Gaussian-square point

Base: Stage15-6aj in the same cycle. Stage15-6aj proved the exact height factorization

\[
R=\frac{2}{\gamma}kN(z)N(w),\qquad \gamma\in\{2,4\}.
\]

Stage15-6ak asks whether the moving outer pair `(m,n)` from the genus-one family is an independent polynomial family parameter that must be summed after a per-curve count. It is not.

## 1. Primitive reduced coordinates

Write the two primitive Gaussian square lifts as

\[
\alpha_0=x+i y=K_\alpha z^2,
\qquad
\beta_0=p+i q=K_\beta w^2,
\]

with

\[
\gcd(x,y)=\gcd(p,q)=1,
\qquad x,y,p,q>0
\]

in the physical positive orientation.

On every physical point,

\[
x=\frac{mr}{h_\alpha},\quad
 y=\frac{ns}{h_\alpha},\quad
 p=\frac{ms}{h_\beta},\quad
 q=\frac{nr}{h_\beta}.
\]

Therefore

\[
\boxed{
\left(\frac mn\right)^2=\frac{xp}{yq},
\qquad
\left(\frac rs\right)^2=\frac{xq}{yp}.
}
\]

The cross-gcd normalizers cancel completely.

## 2. One square condition, not two

The product of the two displayed ratios is

\[
\frac{x^2}{y^2},
\]

which is already a rational square. Hence either ratio is a rational square if and only if the other is.

For positive integers, `A/B` is a rational square exactly when `AB` is an integer square. Thus

\[
\boxed{
\frac{xp}{yq}\in\mathbf Q^{\times2}
\iff
xypq\in\mathbf Z^2.
}
\]

So the global toric compatibility of the two primitive reduced Gaussian values is the single condition

\[
\boxed{xypq\text{ is a square}.}
\]

## 3. Converse reconstruction theorem

Conversely, let `(x,y)` and `(p,q)` be positive primitive pairs satisfying `xypq` square. Then

\[
\frac mn:=\sqrt{\frac{xp}{yq}},
\qquad
\frac rs:=\sqrt{\frac{xq}{yp}}
\]

are positive rational numbers. Reduce each to coprime numerator/denominator pairs `(m,n)` and `(r,s)`.

The identities imply

\[
\frac{mr}{ns}=\frac{x}{y},
\qquad
\frac{ms}{nr}=\frac{p}{q}.
\]

Hence there are positive rationals `h_alpha,h_beta` with

\[
mr=h_\alpha x,\quad ns=h_\alpha y,
\qquad
ms=h_\beta p,\quad nr=h_\beta q.
\]

Prime-valuation comparison using the reduced fractions shows these normalizers are integers. Because the coordinate pairs are primitive,

\[
\boxed{
h_\alpha=\gcd(mr,ns),\qquad h_\beta=\gcd(ms,nr).}
\]

Thus the reconstruction is exactly the Stage15 cross-gcd normalization, not merely a rational parametrization.

The primitive pairs `(m,n),(r,s)` are unique because their positive ratios are fixed.

```text
STAGE15_6AK_PRODUCT_SQUARE_TORIC_COMPATIBILITY_IFF=true
STAGE15_6AK_OUTER_PAIR_RECONSTRUCTION_UNIQUE=true
STAGE15_6AK_INNER_PAIR_RECONSTRUCTION_UNIQUE=true
STAGE15_6AK_CROSS_GCDS_RECONSTRUCTED=true
```

## 4. Consequence for the genus-one family viewpoint

Stage15-6ai correctly proved that if `(m,n)` is fixed first, the projective genus-one curve moves with the outer ratio. But 6ak shows that a retained **integral Gaussian-square point** already determines that ratio.

Therefore a proof that counts global physical survivors should not perform

```text
sum over all outer (m,n)
  then count all rational points on C_{m,n,...}
```

unless it can show that this disintegration is quantitatively harmless. There is an exact alternative:

```text
choose global Gaussian-square/core data
-> impose one coordinate-product square condition
-> reconstruct unique toric pairs
-> apply physical masks
```

The moving curve is a valid local model, but its outer index is derived data in this global coordinate system.

This resolves the proof-accounting danger identified in 6aj.

```text
STAGE15_6AK_NAIVE_POLYNOMIAL_OUTER_CURVE_SUM_REQUIRED=false
STAGE15_6AK_GLOBAL_GAUSSIAN_COORDINATE_MEASURE_AVAILABLE=true
```

## 5. Global exact receiver after 6ak

Up to the already-legal `B^o(1)` finite Gaussian core/orientation decorations, every physical low-core survivor is represented by

```text
squarefree k
K_alpha,K_beta in Z[i], N(K_alpha)=N(K_beta)=k
primitive z,w in Z[i]
alpha0=K_alpha*z^2=x+i y primitive positive
beta0 =K_beta *w^2=p+i q primitive positive
x*y*p*q is a square
k*N(z)*N(w)<=2B
```

followed by the exact reconstruction above and the original physical postfilters.

The product-height cutoff is inherited from 6aj. The exactly-two, canonical-order, direction and positivity filters remain monotone postfilters for upper bounds.

This is a measure-preserving decorated cover of the original physical population. The only multiplicity is the already-charged finite/subpolynomial choice of Gaussian core orientations/units, not a polynomial outer-pair multiplicity.

## 6. Arsenal accounting

This is a new Stage15 exact reconstruction theorem, but its proof-engineering role is exactly the AR-010/016 lesson:

```text
AR-010=SECOND_USE_AS_GLOBAL_OUTER_RECONSTRUCTION_FIREWALL
AR-016=FINITE_GAUSSIAN_CORE_ORIENTATION_MULTIPLICITY_ONLY
AR-023=OUTER_PAIR_NOT_SCALARIZED; IT_IS_RECONSTRUCTED_POINTWISE
AR-024=NO_KERNEL_SAVING_TRANSFER
AR-028=NO_RECHARGE_OF_CORE/CROSS_GCD DATA
AR-030=PHYSICAL_POSTFILTERS_RETAINED
```

No Stage14 counting exponent is imported.

## 7. What remains

The genus-one family average is no longer the first obstruction. The exact remaining global arithmetic condition is the square density of

\[
\boxed{
\Re(K_\alpha z^2)\Im(K_\alpha z^2)
\Re(K_\beta w^2)\Im(K_\beta w^2)
}
\]

under

\[
kN(z)N(w)\le2B.
\]

The next stage should decompose this square condition primewise before any external theorem search.

## 8. Frozen exit

```text
STAGE15_6_SUBSTAGE=6ak
STAGE15_6AK_STARTING_GATE=IS_MOVING_OUTER_PAIR_AN_INDEPENDENT_COUNTING_INDEX
STAGE15_6AK_PRODUCT_SQUARE_TORIC_COMPATIBILITY_IFF=true
STAGE15_6AK_TORIC_COMPATIBILITY=x*y*p*q_is_square
STAGE15_6AK_OUTER_PAIR_RECONSTRUCTION_UNIQUE=true
STAGE15_6AK_INNER_PAIR_RECONSTRUCTION_UNIQUE=true
STAGE15_6AK_CROSS_GCDS_RECONSTRUCTED=true
STAGE15_6AK_NAIVE_POLYNOMIAL_OUTER_CURVE_SUM_REQUIRED=false
STAGE15_6AK_GLOBAL_GAUSSIAN_COORDINATE_MEASURE_AVAILABLE=true
STAGE15_6AK_LOW_CORE_GLOBAL_COUNT_PROVED=false
STAGE15_6AK_EXIT=GLOBAL_COORDINATE_PRODUCT_SQUARECLASS_DECOMPOSITION_READY
```

Stage15-6ak stops at the global reverse reconstruction.