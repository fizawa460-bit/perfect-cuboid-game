# Stage14-t18 — selected branch local image and packet Fourier bound

## Purpose

Stage14-t17 converts the remaining square lift

\[
r^2=x
\]

on the moving elliptic fiber

\[
C_{0,t}:\quad U^2=A_t(x),\qquad V^2=B_t(x)
\]

into a branch-sensitive generalized-Jacobian squareclass problem.  The eight-point modulus has a seven-dimensional toric `2`-character space, but the Stage14 triple gate uses one specific ramified quadratic character: the cover cut out by `x`.

Stage14-t18 computes the local image of this **selected Stage14 branch character** and derives the first rigorous moving-family Fourier/second-moment inequality.  It does not claim to compute the full seven-dimensional semiabelian descent image.

## 1. The selected branch character

The branch modulus is

\[
\mathfrak m_t=D_0+D_\infty
\]

with eight rational points.  Quadratic branch-monodromy vectors lie in

\[
\{e\in\mathbf F_2^8:\sum e_i=0\},
\]

a space of dimension `7`, matching the split torus rank from t17.

For the Stage14 cover `r^2=x`, the valuation of `x` is odd at all four zero points and all four pole points.  Hence its branch-monodromy vector is

```text
(1,1,1,1,1,1,1,1).
```

So t18 isolates the exact one-dimensional quotient of the branch-modulus descent that is relevant to triple lifting.

## 2. Exact local image: it is full at every place

Write

\[
A_t(x)=1-2(1+2t^2)x+x^2,
\]

\[
B_t(x)=1+(4t^4-2)x+x^2.
\]

Fix any place `v` of `Q` and any physical rational `t`.

For a finite place `v=p`, every class in

\[
\mathbf Q_p^\times/\mathbf Q_p^{\times2}
\]

has representatives with arbitrarily large `p`-adic valuation: multiply any representative by an even power of `p`.  For `x` sufficiently `p`-adically small,

```text
A_t(x), B_t(x) in 1+p Z_p        (p odd),
A_t(x), B_t(x) in 1+8 Z_2        (p=2),
```

and these neighborhoods consist of squares.  Thus every local squareclass occurs as `x(P)` for some `P in C_{0,t}(Q_p)` near one of the rational points above `x=0`.

At the real place, `A_t(0)=B_t(0)=1`, so sufficiently small positive and negative `x` both give real points.  Therefore

\[
\boxed{
\delta_{t,v}\bigl(C_{0,t}(\mathbf Q_v)\bigr)
=\mathbf Q_v^\times/\mathbf Q_v^{\times2}
}
\]

for every place `v`.

This is a decisive direction check.  There is **no local-image density saving** available from the selected squareclass map alone.  Any useful saving must come from global distribution/cancellation of squareclass signatures among physical rational points, not from excluding local classes.

This does not assert that global rational points realize arbitrary products of local signatures simultaneously.

## 3. Canonical moving arithmetic support

For a primitive Pythagorean physical base

\[
F=(S,X,H),\qquad t=X/S,
\]

one has exactly

\[
\operatorname{Supp}\!\bigl(t(t^2-1)(t^2+1)\bigr)
=
\operatorname{Supp}\!\bigl(SXH(S-X)(S+X)\bigr).
\]

This gives a canonical base-level moving place set

\[
S_{\rm base}(F)
=
\{\infty,2\}
\cup
\operatorname{Supp}\!\bigl(SXH(S-X)(S+X)\bigr).
\]

For a physical point `P` with reduced `x(P)=a/b`, the packet may additionally use primes dividing `ab`.  Thus a natural arithmetic packet support is

\[
S_{\rm arith}(F,P)
=
S_{\rm base}(F)\cup\operatorname{Supp}(ab).
\]

The role of this set is **character selection**, not local obstruction.  Stages t7--t10 already forbid interpreting a fixed universal prime set as an independent thinning factor.

## 4. Packet formulation

A sieve packet consists of a finite physical point set `Z`, a common finite place set `S`, and `r` independent quadratic characters

\[
\xi_1,\ldots,\xi_r
\]

of the selected local squareclass data.  Each point `z=(F,P)` receives a signature

\[
\sigma(z)\in\mathbf F_2^r.
\]

Let

\[
M=|Z|,
\qquad
n_a=\#\{z:\sigma(z)=a\},
\qquad
Q=\sum_{a\in\mathbf F_2^r}n_a^2.
\]

A globally square `x(P)` necessarily has zero signature, hence

\[
N_\square(Z)\le n_0.
\]

For `e in F_2^r` define the Fourier sums

\[
C_e=\sum_{z\in Z}(-1)^{e\cdot\sigma(z)}.
\]

Finite Fourier orthogonality gives exactly

\[
n_0=2^{-r}\sum_e C_e
\]

and Parseval gives

\[
\sum_e |C_e|^2=2^rQ.
\]

Since `C_0=M`, the nontrivial character energy is

\[
\boxed{
E_{\ne0}=2^rQ-M^2.
}
\]

## 5. First moving character-sum inequality

Applying Cauchy--Schwarz to the nontrivial Fourier terms yields the exact finite upper bound

\[
\boxed{
N_\square(Z)
\le
\frac{M}{2^r}
+
\sqrt{
(1-2^{-r})
\left(Q-\frac{M^2}{2^r}\right)
}.
}
\]

The two terms have distinct meanings:

1. `M/2^r` is the entropy term expected from `r` independent balanced squareclass bits;
2. `Q-M^2/2^r` is the **signature collision excess**, equivalently the normalized nontrivial Fourier second moment.

This is the first t-track inequality in which the desired global thinning is reduced to a concrete second-moment quantity rather than an informal request for character cancellation.

For a partition into moving packets `Z_j` with ranks `r_j`, a sufficient theorem-scale target is

\[
\sum_j \frac{M_j}{2^{r_j}}=o(\sqrt B)
\]

and

\[
\sum_j
\sqrt{
(1-2^{-r_j})
\left(Q_j-\frac{M_j^2}{2^{r_j}}\right)
}
=o(\sqrt B).
\]

With the physical height window built into every `Z_j`, these two estimates would imply the required square-lift incidence bound and hence, after the fixed Stage14 bookkeeping, `T(B)=o(sqrt(B))`.

Neither estimate is proved in t18.

## 6. What t18 closes

The local-image question for the **selected Stage14 `x`-character** is now completely resolved: it is surjective at every completion, so local obstruction counting cannot be the source of the needed saving.

The remaining analytic problem is sharply identified as a moving squareclass-signature equidistribution / collision-energy problem over physical rational points.

The deterministic audit verifies:

- the seven-dimensional eight-branch character space and all-ones Stage14 monodromy vector;
- local squareclass surjectivity on representative physical fibers at `R`, `Q_2`, and several odd `Q_p`;
- the exact Pythagorean rewrite of the moving bad-parameter support;
- Fourier projector, Parseval energy identity, and the Cauchy--Schwarz packet inequality using exact rational arithmetic.

## Locked boundary

```text
STAGE14_T18=COMPLETE_SELECTED_BRANCH_LOCAL_IMAGE_AND_PACKET_FOURIER_BOUND
BRANCH_CHARACTER_SPACE_DIMENSION=7
STAGE14_X_BRANCH_MONODROMY_ALL_ONES=true
SELECTED_LOCAL_X_SQUARECLASS_IMAGE_FULL_AT_EVERY_PLACE=true
LOCAL_OBSTRUCTION_SAVING_AVAILABLE=false
FULL_SEMIABELIAN_2_DESCENT_IMAGE_COMPUTED=false
MOVING_ARITHMETIC_PLACE_PACKET_DEFINED=true
PACKET_FOURIER_PROJECTOR_EXACT=true
PACKET_PARSEVAL_COLLISION_IDENTITY=true
PACKET_SECOND_MOMENT_UPPER_BOUND=true
PHYSICAL_HEIGHT_WINDOW_RETAINED=true
GLOBAL_CHARACTER_CANCELLATION_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
NEXT=Stage14-t19 instantiate moving packets on the exact physical point ledger and attack squareclass-signature collision excess / family second moment
```
