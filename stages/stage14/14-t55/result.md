# Stage14-t55 — shared-U projective complete trace and centered-selector reduction

## Purpose

Stage14-t54 reduced the largest frozen principal stratum to a fixed primitive Gaussian cofactor `U` with a genuine two-coordinate family `(pi,V)` and showed that the one-variable t36/t38 bounds do not globalize.

Stage14-t55 keeps the fixed-U divisor fan and asks whether the two-dimensional character kernel itself has enough complete cancellation before the physical selector is imposed.

The answer is yes for the dominant invisible/invisible shared-U stratum: the complete projective trace is exactly `O(p)`, i.e. square-root size relative to the `P1 x P1` box of size `asymp p^2`.  The remaining obstruction is therefore not the algebraic character kernel but the correlation of the physical fixed-U selector with that kernel.

No global principal-collision or `T=o(sqrt(B))` claim is made.

## 1. Shared-U branch split

The merged t54 frozen family has six post-residue distinct-ell shared-U principal blocks.  Exact reconstruction gives

```text
invisible / invisible     5
invisible / visible       1
```

Thus the dominant shared-U stratum has

\[
A_c=\pi U,\qquad P_c=V,
\]

with the canonical Gaussian prime `pi` and primitive Gaussian cover cofactor `V` as independent projective coordinates.  The one mixed-branch block is retained as a separate exceptional slice.

## 2. Quartic squareclass is a rational cross-ratio

For a physical state write

\[
t=\frac ab,\qquad x=\frac pq.
\]

Set

\[
A=b^2p^2-a^2q^2,\qquad B=b^2q^2-a^2p^2.
\]

The universal four-linear kernel is

\[
F=AB.
\]

But

\[
\frac{F}{A/B}=B^2,
\]

so `F` and `A/B` have the same rational squareclass.  Therefore

\[
\boxed{
[F]=\left[\frac{x^2-t^2}{1-t^2x^2}\right].
}
\tag{55.1}
\]

This was checked exactly on all 560 reciprocal frozen states.  It is an identity, not a finite-data heuristic.

## 3. Projective character kernel

For an odd prime `l`, on

\[
(A:B),(P:Q)\in \mathbf P^1(\mathbf F_l)
\]

define

\[
K_l((A:B),(P:Q))
=
\chi_l\!\left((B^2P^2-A^2Q^2)(B^2Q^2-A^2P^2)\right).
\tag{55.2}
\]

Because each projective rescaling enters to fourth degree, the Legendre value is well-defined on `P1 x P1`.

Let

\[
\Sigma_l=\sum_{\mathbf P^1(\mathbf F_l)^2}K_l.
\]

### Exact evaluation

On the affine chart put `t=A/B`, `x=P/Q`.  For nonzero `t,x`, use

\[
u=x/t,\qquad v=tx.
\]

Then

\[
(x^2-t^2)(1-t^2x^2)
=t^2(u^2-1)(1-v^2),
\]

and the number of preimages of `(u,v)` is

\[
1+\chi_l(v/u).
\]

After separating the two factored sums and adding the affine zero rows and the two projective infinity boundaries, one obtains:

- if `l == 1 (mod 4)`, with

\[
A_l=\sum_{z\in\mathbf F_l}\chi_l(z^3-z),
\]

then

\[
\boxed{\Sigma_l=4l+A_l^2;}
\tag{55.3}
\]

- if `l == 3 (mod 4)`, the odd symmetry forces `A_l=0` and the remaining boundary terms cancel, giving

\[
\boxed{\Sigma_l=0.}
\tag{55.4}
\]

Now `A_l=-a_l` for the elliptic curve

\[
E:y^2=x^3-x.
\]

Hasse gives `|a_l|<=2 sqrt(l)`, hence for split auxiliary primes

\[
\boxed{0\le\Sigma_l\le 8l.}
\tag{55.5}
\]

This is the optimal two-dimensional square-root scale relative to the complete projective box of size `(l+1)^2`.

The audit verifies (55.3)--(55.5) by direct complete summation for eleven split primes and verifies (55.4) for eleven inert primes.

## 4. Fixed U does not alter the complete trace

Multiplication by a fixed Gaussian cofactor `U=u+iv` acts on canonical-prime projective slope by

\[
(r:s)\mapsto (ur-vs:vr+us).
\]

For an auxiliary prime not dividing `N(U)`, this is a `PGL_2(F_l)` bijection.  Therefore the fixed-U invisible complete trace is still exactly `Sigma_l`.

The frozen audit performs 22 explicit fixed-U/PGL2 complete-sum checks.

Bad auxiliary primes dividing `N(U)` form only the same bounded logarithmic support already handled by the t50 bad-prime mechanism and are not a new obstruction.

## 5. Two split auxiliary primes

For distinct split primes `lambda,mu`, CRT gives

\[
\Sigma_{\lambda\mu}
=
\Sigma_\lambda\Sigma_\mu.
\]

Using (55.5),

\[
\boxed{
|\Sigma_{\lambda\mu}|
\le64\lambda\mu.
}
\tag{55.6}
\]

The audit checks the corresponding product bound for all 55 pairs among the eleven frozen split test primes.

The complete residue universe has size

\[
|\Omega_{\lambda\mu}|
=(\lambda+1)^2(\mu+1)^2
\asymp (\lambda\mu)^2.
\]

Thus the average character on the complete projective box is only

\[
O((\lambda\mu)^{-1}).
\]

## 6. Constant-density physical selector term closes

Fix an invisible fixed-U physical fiber and let

\[
\nu_{U,m}(z)
\]

be its residue multiplicity on the complete projective box modulo

\[
m=\lambda\mu.
\]

Write

\[
R_U=\sum_z\nu_{U,m}(z),\qquad
b_{U,m}=\nu_{U,m}-\frac{R_U}{|\Omega_m|}\mathbf 1.
\]

Then the physical character sum decomposes exactly as

\[
S_{U,m}
=
\frac{R_U}{|\Omega_m|}\Sigma_m
+
\langle b_{U,m},K_m\rangle.
\tag{55.7}
\]

By (55.6), for `lambda,mu~L`,

\[
\left|\frac{R_U}{|\Omega_m|}\Sigma_m\right|
\ll \frac{R_U}{L^2}.
\]

Hence over `P^2` auxiliary-prime pairs the constant-density contribution is

\[
\ll B^{o(1)}\frac{R_U^2P^2}{L^4}.
\]

The merged t38 global critical-family bound gives

\[
R_U\le B^{1/2+o(1)}.
\]

Therefore any auxiliary scale

\[
L=B^\rho,\qquad \rho>1/8,
\]

already gives

\[
\frac{R_U}{L^4}=o(1),
\]

so the constant-density term is below the target `R_U P^2 B^o(1)` scale.

This reuses exactly the same strict threshold `rho>1/8` that appeared in t51, but for a different purpose: here it kills the complete-density mean rather than residue aliasing.

## 7. Remaining theorem

After the complete trace and constant-density mean are removed, the live object is

```text
SharedUInvisibleCenteredProjectiveSelectorDispersion
```

with target

\[
\boxed{
\sum_{\lambda\ne\mu}
\left|
\langle b_{U,\lambda\mu},K_{\lambda\mu}\rangle
\right|^2
\ll
R_U P^2 B^{o(1)}.
}
\tag{55.8}
\]

The fixed-U divisor fan, branch masks, interval/reconstruction conditions and signed aggregation must remain inside `b_{U,m}`.  Pair-to-cross-kernel collapse before this estimate is still forbidden because it reintroduces the unresolved fourth-energy coefficient.

Equation (55.8) is strictly narrower than the t54 `SharedUBipartiteSquareclassEnergy`: the algebraic complete kernel and its constant component are now solved.  What remains is a centered selector-discrepancy/dispersion theorem.

## 8. tH decision

`tH15` is still needed, but its task is now narrower.

It no longer needs to discover a two-dimensional complete character bound: t55 supplies the exact optimal complete trace.  It should address only the physical fixed-U divisor-fan selector against the centered projective kernel, i.e. (55.8), or produce a precise impossibility boundary.

No tH16 is indicated.

## Locked boundary

```text
STAGE14_T55=COMPLETE_SHARED_U_PROJECTIVE_TRACE_AND_CENTERED_SELECTOR_REDUCTION
SHARED_U_INVISIBLE_COMPLETE_PROJECTIVE_TRACE_PROVED=true
SHARED_U_CONSTANT_DENSITY_MEAN_CLOSED=true
SHARED_U_CENTERED_PROJECTIVE_SELECTOR_DISPERSION_REQUIRED=true
SHARED_U_CENTERED_PROJECTIVE_SELECTOR_DISPERSION_PROVED=false
SHARED_U_BIPARTITE_SQUARECLASS_ENERGY_PROVED=false
SHARED_U_CANONICAL_PRIME_PRINCIPAL_INCIDENCE_PROVED=false
UV_TRANSVERSE_CROSS_GOOD_LD2_KUMMER_INCIDENCE_PROVED=false
GENERIC_CROSS_GOOD_LD2_KUMMER_PRINCIPAL_INCIDENCE_PROVED=false
GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED=false
GLOBAL_FOURTH_ENERGY_POWER_SAVING_PROVED=false
CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED=false
A_11_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
TH15_NEEDED=true
NEXT=Stage14-t56 attack SharedUInvisibleCenteredProjectiveSelectorDispersion; consume tH15 if available, keep the one mixed-branch block separate, and use the exact P1xP1 complete trace before any cross-kernel collapse
```
