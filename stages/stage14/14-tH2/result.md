# Stage14-tH2 — divisor-coupled Gaussian norm-index hyperbola engine

## Purpose

Stage14-tH1 fixed Gaussian primary/ray-class/conductor conventions. Stage14-tH2 now isolates the arithmetic skeleton already present in merged Stage14-t32,

\[
N(U)=m,\qquad N(V)=k\delta,\qquad k\mid \varepsilon m,
\qquad m\delta\le Y,
\]

where the finite state factor `epsilon` is fixed on each local/canonical packet.

The purpose is to remove the awkward divisor condition `k|epsilon*m` exactly, expose the shared norm factor, and produce a reusable hyperbola decomposition which later large-sieve or coefficient-energy stages can consume without redoing Stage14 geometry.

No t35-or-later identity is required and no Stage14 power saving is claimed here.

---

## 1. Exact divisor reparameterisation

Given a tuple

```text
m >= 1, delta >= 1, k | epsilon*m,
```

define

\[
g=\gcd(k,\varepsilon),\qquad
h=k/g,\qquad
r=m/h.
\]

Then

\[
g\mid\varepsilon,
\qquad
\gcd\!\left(h,\frac{\varepsilon}{g}\right)=1,
\qquad
h\mid m.
\]

Indeed, write `epsilon=g*epsilon'`. Since

\[
gh\mid g\varepsilon' m
\]

and `gcd(h,epsilon')=1`, one has `h|m`.

Conversely, from

\[
g\mid\varepsilon,
\qquad
\gcd\!\left(h,\frac{\varepsilon}{g}\right)=1,
\qquad
m=hr,
\]

put

\[
k=gh.
\]

Then

\[
\gcd(k,\varepsilon)=g,
\qquad
k\mid\varepsilon m.
\]

Thus there is an exact bijection

\[
\boxed{
(m,k,\delta)
\longleftrightarrow
(g,h,r,\delta)
}
\tag{H2.1}
\]

with

\[
\boxed{
 m=hr,\qquad k=gh,
\qquad g\mid\varepsilon,
\qquad \gcd(h,\varepsilon/g)=1.
}
\tag{H2.2}
\]

The physical hyperbola becomes simply

\[
\boxed{hr\delta\le Y.}
\tag{H2.3}
\]

This is the first main tH2 output: the divisor condition is replaced by a finite `g|epsilon` state and one shared factor `h`.

---

## 2. Unified Gaussian norm form

Under (H2.2), the two Gaussian norm indices are

\[
\boxed{
N(U)=hr,
\qquad
N(V)=gh\delta.
}
\tag{H2.4}
\]

The same factor `h` occurs in both norms.

Therefore, after fixing the finite state `g`, the Stage14-shaped arithmetic object has the canonical form

```text
shared factor: h
free U-side factor: r
free V-side factor: delta
budget: h*r*delta <= Y
N(U)=h*r
N(V)=g*h*delta
```

The divisor coupling has not disappeared; it has been converted into an explicit shared norm factor. This is substantially cleaner for later spectral and coefficient-energy arguments.

```text
DIVISOR_CONDITION_REMOVED_BY_EXACT_BIJECTION=true
SHARED_GAUSSIAN_NORM_FACTOR=h
FINITE_EPSILON_STATE=g_divides_epsilon
```

---

## 3. Exact summation identity

For every test function `F`, with no positivity assumption,

\[
\boxed{
\sum_{\substack{m\delta\le Y}}
\sum_{k\mid\varepsilon m}
F(m,k,\delta)
=
\sum_{g\mid\varepsilon}
\sum_{\substack{hr\delta\le Y\\(h,\varepsilon/g)=1}}
F(hr,gh,\delta).
}
\tag{H2.5}
\]

This is an exact identity, not an upper-bound relaxation.

Hence every later tH stage may work on `(g,h,r,delta)` and recover the original Stage14 norm-index sum without multiplicity loss.

---

## 4. Generalised balanced hyperbola split

Fix `g,h` and put

\[
T=Y/h.
\]

The remaining sharp condition is

\[
r\delta\le T.
\]

The two Gaussian norm sizes are proportional to

\[
M=hr,
\qquad
N=gh\delta.
\]

So equality of norm scales occurs near

\[
r\asymp g\delta.
\]

Define the real thresholds

\[
R_0=\sqrt{gT}=\sqrt{gY/h},
\qquad
D_0=\sqrt{T/g}=\sqrt{Y/(gh)}.
\tag{H2.6}
\]

If simultaneously `r>R0` and `delta>D0`, then `r*delta>T`, impossible. Therefore every admissible point lies in at least one of the two arms

```text
R-arm: r <= R0,
D-arm: delta <= D0.
```

Their overlap rectangle is automatically inside the hyperbola because

\[
R_0D_0=T.
\]

Thus for every function `G`,

\[
\boxed{
\sum_{r\delta\le T}G(r,\delta)
=
\sum_{\substack{r\delta\le T\\r\le R_0}}G
+
\sum_{\substack{r\delta\le T\\\delta\le D_0}}G
-
\sum_{\substack{r\le R_0\\\delta\le D_0}}G.
}
\tag{H2.7}
\]

This is the exact Dirichlet-hyperbola identity aligned to the Gaussian norm balance, not the arbitrary symmetric split `r~delta`.

---

## 5. One Gaussian norm is short in each unbalanced arm

At the balance thresholds,

\[
hR_0=\sqrt{ghY},
\qquad
ghD_0=\sqrt{ghY}.
\]

Hence:

- on the `R`-arm, `N(U)=hr <= sqrt(ghY)`;
- on the `D`-arm, `N(V)=gh*delta <= sqrt(ghY)`;
- on the overlap rectangle, both norms are at most `sqrt(ghY)`;
- outside the overlap, exactly one norm is forced above the balance scale and the other remains below it.

So the hyperbola decomposition automatically produces a **short Gaussian norm variable** in every piece.

\[
\boxed{
\min(N(U),N(V))\le \sqrt{ghY}.
}
\tag{H2.8}
\]

This inequality is of course also immediate from

\[
N(U)N(V)=g h^2 r\delta\le ghY,
\]

but (H2.7) gives the exact summation architecture needed later.

```text
GAUSSIAN_BALANCE_SCALE=sqrt(g*h*Y)
EVERY_HYPERBOLA_POINT_HAS_ONE_SHORT_NORM=true
EXACT_BALANCED_HYPERBOLA_IDENTITY_PROVED=true
```

---

## 6. Dyadic block engine

Put

```text
h in [H,2H),
r in [R,2R),
delta in [D,2D)
```

with `H,R,D` powers of two.

Every admissible tuple occupies exactly one dyadic block and any active block satisfies

\[
HRD\le Y.
\tag{H2.9}
\]

The full rectangular box containing that block has product volume scale

\[
(2H)(2R)(2D)=8HRD\le 8Y.
\tag{H2.10}
\]

The Gaussian norm ranges are

\[
HR\le N(U)<4HR,
\qquad
gHD\le N(V)<4gHD.
\tag{H2.11}
\]

Thus the ratio of the two norm scales is controlled entirely by

\[
\frac{R}{gD};
\]

the shared factor `H` cancels.

A later spectral stage may therefore classify blocks using only

```text
balanced: R comparable to g*D
U-long:   R >> g*D
V-long:   R << g*D.
```

There are only

\[
O_\varepsilon((\log 2Y)^3)
\]

possible `(H,R,D)` blocks for each finite `g|epsilon` state.

No fixed power of `Y` is lost in dyadic decomposition.

---

## 7. Exact sharp-cutoff policy

Stage14-tH2 deliberately does **not** replace

\[
hr\delta\le Y
\]

by a full rectangular box in signed character sums.

The permitted downstream interfaces are:

1. retain the exact product cutoff inside each dyadic block;
2. use the exact two-arm identity (H2.7);
3. if a later theorem requires smooth weights, introduce a smooth partition there and record its Mellin/Perron truncation cost explicitly.

This avoids the recurrent error of treating a hyperbolic region as if it were a Cartesian product without paying for the boundary.

```text
SHARP_HYPERBOLA_RECTANGULARIZED_WITHOUT_ERROR=false
EXACT_PRODUCT_CUTOFF_RETAINED=true
```

---

## 8. Gaussian representation multiplicity costs no fixed power

For an integer `n`,

\[
r_2(n)\le4\tau(n).
\]

Hence for one transformed tuple,

\[
r_2(hr)\,r_2(gh\delta)
\le16\tau(hr)\tau(gh\delta).
\tag{H2.12}
\]

For fixed finite `epsilon`, `g|epsilon` is bounded. By the standard divisor bound, for every `eta>0`,

\[
\tau(n)\ll_\eta n^\eta.
\]

Also, elementarily,

\[
\#\{(h,r,\delta):hr\delta\le Y\}
\le
Y(1+\log Y)^2.
\tag{H2.13}
\]

Therefore the full unsieved Gaussian-representation mass obeys

\[
\boxed{
\sum_{g\mid\varepsilon}
\sum_{\substack{hr\delta\le Y\\(h,\varepsilon/g)=1}}
r_2(hr)r_2(gh\delta)
\ll_{\varepsilon,\eta}Y^{1+\eta}.
}
\tag{H2.14}
\]

So divisor and Gaussian representation multiplicities consume only `Y^o(1)`, not a positive exponent.

This is an envelope only; coefficient **energy** and collisions are intentionally reserved for tH5.

```text
GAUSSIAN_REPRESENTATION_MULTIPLICITY_FIXED_POWER_LOSS=false
UNSIEVED_HYPERBOLA_MASS=Y^(1+epsilon)
COEFFICIENT_COLLISION_ENERGY_CLOSED=false
```

---

## 9. Canonical downstream block record

Later tH stages should use the following record.

```text
GaussianHyperbolaBlock:
  epsilon_state: fixed bounded integer
  g: divisor of epsilon_state
  gcd_condition: gcd(h,epsilon_state/g)=1
  shared_factor_range: h in [H,2H)
  U_free_range: r in [R,2R)
  V_free_range: delta in [D,2D)
  sharp_budget: h*r*delta <= Y
  U_norm: h*r
  V_norm: g*h*delta
  U_norm_scale: H*R
  V_norm_scale: g*H*D
  balance_ratio: R/(g*D)
  balance_norm_scale: sqrt(g*H*Y) up to dyadic constants
```

This record is independent of any particular t-stage square detector or character family.

---

## 10. Deterministic audit

The dedicated audit enumerates all original and transformed tuples for

```text
epsilon in {1,2,3,4,6,8,12}
Y = 256.
```

Frozen checks:

```text
original tuples k|epsilon*m, m*delta<=Y       82740
transformed tuples                             82740
unique transformed tuples                      82740
bijection failures                                  0

exact R-arm memberships                        59711
exact D-arm memberships                        39848
overlap memberships                            16819
R + D - overlap                                82740
hyperbola-cover failures                            0

active dyadic (epsilon,g,H,R,D) blocks          3114
max full-box product / Y                           8

max U norm audited                               256
max V norm audited                              3072
exact Gaussian representation-pair mass       926416
r2(n)<=4*tau(n) product violations                  0
```

The audit independently reconstructs the original tuple from every transformed tuple and vice versa.

---

## 11. Interaction with the live t route

Stage14-tH2 does not depend on merged t34 or any later t result.

If t supplies an all-character Mellin/Hecke block, tH2 provides immediately:

```text
k|epsilon*m
  -> finite g-state + shared h
  -> exact h*r*delta hyperbola
  -> one-short-norm two-arm split
  -> dyadic Gaussian norm blocks
  -> only subpolynomial divisor/representation multiplicity.
```

If the live t spectral object changes again, this arithmetic engine remains valid because it is an exact identity on the norm-index skeleton itself.

---

## Proof boundary

```text
STAGE14_TH2=COMPLETE_DIVISOR_COUPLED_GAUSSIAN_NORM_HYPERBOLA_ENGINE
TH_MINIMUM_FROZEN_T_INPUT=Stage14-t32
TH_REQUIRES_FUTURE_T_RESULT=false
DIVISOR_REPARAMETERIZATION_BIJECTION_PROVED=true
TRANSFORMED_VARIABLES=g,h,r,delta
TRANSFORMED_IDENTITIES=m=h*r,k=g*h
FINITE_G_STATE=g_divides_epsilon
SHARED_GAUSSIAN_NORM_FACTOR=h
EXACT_SUMMATION_IDENTITY_PROVED=true
EXACT_BALANCED_HYPERBOLA_IDENTITY_PROVED=true
EVERY_HYPERBOLA_POINT_HAS_ONE_SHORT_NORM=true
DYADIC_BLOCK_COUNT=polylogarithmic
SHARP_HYPERBOLA_RECTANGULARIZED_WITHOUT_ERROR=false
GAUSSIAN_REPRESENTATION_MULTIPLICITY_FIXED_POWER_LOSS=false
COEFFICIENT_COLLISION_ENERGY_CLOSED=false
ALL_CHARACTER_MELLIN_HECKE_LARGE_SIEVE_PROVED=false
NORM_INDEX_HYPERBOLIC_CORRELATION_POWER_SAVING_PROVED=false
A_11_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
NEXT=Stage14-tH3
```
