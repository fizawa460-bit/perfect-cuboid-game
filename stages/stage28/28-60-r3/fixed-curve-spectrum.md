# Stage28-60-r3 — fixed rational-curve spectrum comparison

```text
ROUTE=R21_FIXED_CURVE_SPECTRUM_COMPARISON
CHECKPOINT=60
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
```

Checkpoint60-r2 reduced the direct bridge to the interaction-curvature threshold

\[
J_{28}=I_{face}/I_{sp}\quad\text{versus}\quad (\log B)^{-2}.
\]

The first new post-r2 question is whether the two completion covers already differ at the level of low-degree physical rational curves under the common quasi-polarization.

## Stage19 space cover: the degree-four mechanism is absent

The audited Stage14-4ah/4ai/4ak chain identifies the physical quasi-polarization

\[
M=\pi^*(-K_Y),\qquad M^2=8,
\]

and proves that every physical rational curve has `M.C>=4`.  Stage14-4ak then closes the sole remaining `M.C=4` mechanism by the exact Shimada anti-invariant-lattice parity-coset computation:

```text
PHYSICAL_Q_RATIONAL_M4_BISECTION_EXISTS=false
FIXED_CURVE_SQRTB_MECHANISM_REJECTED=true
```

Since Stage14-4ai had already exhausted the other degree-four image/splitting possibilities, there is no physical Q-rational fixed curve of M-degree four on the Stage19 space-cover model.

For a fixed rational curve of M-degree `m`, the restricted height has degree `m` on `P1`, so Schanuel gives polynomial contribution `B^(2/m)` up to the usual field/metric constants.  Consequently any finite union of fixed physical rational curves on the Stage19 space cover contributes at most

\[
\boxed{O(B^{2/5})}
\]

at the polynomial-exponent level.

This is a fixed-curve statement only.  It does not bound the full Stage19 population, because Stage14-4al already shows that the observed square-root-scale finite signal, if real asymptotically, must come from a collective moving-fibre/rank-jump/first-small-point mechanism rather than a fixed degree-four curve.

## Stage20 third-face cover: a degree-six rational family is present

The audited generalized Saunderson map is homogeneous of degree six in the coprime Euclid parameters `(r,s)`:

```text
u=r^2-s^2
v=2rs
w=r^2+s^2
A=u(4v^2-w^2)
B=v(4u^2-w^2)
C=4uvw
```

(up to harmless signs/absolute values on the physical chamber).  The three edge coordinates have no common nonconstant polynomial factor.  Hence the induced projective rational curve has physical coordinate degree six.  On the audited injective cone `1/8<=s/r<=4/5`, the output is generically one-to-one and

\[
r^6\le w^3\le R\le 8r^6.
\]

Thus this fixed rational curve contributes the already-audited target scale

\[
\boxed{\Theta(B^{1/3})}
\]

on its positive-density rational parameter sector.

## What the spectrum comparison proves

There is a genuine causal asymmetry that was not visible from the common `degree-two / K3 / -2K_Y / sieve-dimension-two` ledger:

```text
STAGE19_FIXED_M4_CURVE=ABSENT
STAGE20_FIXED_DEGREE6_SAUNDERSON_CURVE=PRESENT
STAGE19_FINITE_FIXED_CURVE_EXPONENT_MAX_CERTIFIED=2/5
STAGE20_FIXED_CURVE_EXPONENT_AT_LEAST=1/3
```

This still does **not** order `M3` and `N2`.  Stage19 could have physical rational curves of M-degree 5 or 6, and more importantly its global count may be controlled by collective moving-fibre activation rather than any finite set of fixed curves.

The useful new boundary is therefore:

```text
FIXED_CURVE_SPECTRUM_IS_A_REAL_CAUSAL_DIFFERENTIAL=true
FIXED_CURVE_SPECTRUM_ALONE_RESOLVES_J28_THRESHOLD=false
NEXT_FIXED_CURVE_FINITE_RECEIVER=classify physical Stage19 M-degrees 5 and 6 and compare with Stage20 degree<=6 spectrum
GLOBAL_COMPLEMENT_RECEIVER_STILL_REQUIRED=true
```

No perfect-cuboid joint endpoint is used.