# Stage14-t35 — shared-prime dispersion and the fixed-U fiber barrier

## Purpose

Stage14-t34 removed the arbitrary-order Mellin obstruction by converting the full `mu_4`-trivial character family into a Gaussian additive large-sieve problem. Its remaining loss came from tensorising the `U` and `V` variables with independent auxiliary moduli.

Stage14-t35 keeps the auxiliary Gaussian prime modulus shared. The resulting collision kernel is genuinely thinner:

\[
\varpi\mid U-uU',\qquad \varpi\mid V-vV',\qquad u,v\in\mu_4.
\]

The main conclusions are:

1. for an off-diagonal pair, the number of auxiliary split primes that can create a collision is bounded by a divisor count of explicit Gaussian differences;
2. once the auxiliary rational norm `lambda=N(varpi)` exceeds `8M`, where `N(U),N(U')<=2M`, a `U`-collision is no longer merely congruential: it forces exact equality up to a Gaussian unit;
3. the physical norm hyperbola then decomposes into fixed-`U` fibers of size
   \[
   J(U)\ll (N/M)B^{o(1)},\qquad N:=B/\ell;
   \]
4. this yields a same-modulus positive-dispersion estimate that removes the polynomial `sqrt(M)` loss of t34;
5. however, after generic Mellin-packet Cauchy/duality the resulting square-detector bound is only
   \[
   (M^2+N)B^{o(1)},
   \]
   so it reaches the ambient norm-hyperbola scale but does not beat it by a fixed power.

Thus the next obstruction is no longer a positive collision count. It is **signed auxiliary-trace cancellation inside a fixed `U` fiber**.

No global `A_11` power saving is claimed in t35.

## 1. Shared-prime collision kernel

Work on a fixed canonical prime `ell` and a dyadic direction-cofactor shell

\[
M<N(U)=m\le2M.
\]

The physical cofactor variable satisfies

\[
N(V)=k\delta,\qquad k\mid\varepsilon m,
\qquad \frac{\varepsilon\ell m\delta}{2}\le B.
\]

Put

\[
N:=B/\ell.
\]

For split auxiliary Gaussian primes `varpi` with rational norm

\[
\lambda=N(\varpi)\asymp L,
\]

t34 quotient-character orthogonality shows that an off-diagonal spectral collision requires

\[
\boxed{
\varpi\mid U-uU',\qquad
\varpi\mid V-vV'
}
\tag{35.1}
\]

for some `u,v in mu_4`.

This is the information lost by independent tensorisation.

## 2. Exact large-modulus injection in the U-variable

Assume

\[
N(U),N(U')\le2M.
\]

For any Gaussian unit `u`,

\[
N(U-uU')
\le (|U|+|U'|)^2
\le 8M.
\]

If `varpi` divides a nonzero Gaussian integer `z`, then

\[
N(\varpi)\le N(z).
\]

Therefore

\[
\boxed{
\lambda>8M,\quad
\varpi\mid U-uU'
\Longrightarrow
U=uU'
}
\tag{35.2}
\]

in `Z[i]` itself.

So for auxiliary primes above `8M`, the `U` coordinate is **injective modulo Gaussian units**. All nontrivial same-modulus collisions occur inside one exact `U`-orbit fiber.

This is stronger than the norm congruence

\[
\lambda\mid N(U)-N(U').
\]

## 3. Off-diagonal prime-support bound

After (35.2), fix an exact `U` orbit and take two distinct `V` orbits. For a collision at `varpi`, some `v in mu_4` satisfies

\[
\varpi\mid V-vV'.
\]

If `V` and `V'` are not unit-equivalent, all four Gaussian differences are nonzero. Define

\[
\mathfrak D(V,V')
:=
\prod_{v\in\mu_4}N(V-vV').
\]

If `N(V),N(V')<=N_0`, then

\[
N(V-vV')\le8N_0,
\]

hence

\[
\mathfrak D(V,V')\le(8N_0)^4.
\]

Every rational split prime `lambda>=L` causing a collision divides `\mathfrak D(V,V')`. Therefore

\[
\boxed{
\nu_L(V,V')
\le
\frac{\log \mathfrak D(V,V')}{\log L}
\le
4\frac{\log(8N_0)}{\log L}.
}
\tag{35.3}
\]

Thus a fixed off-diagonal pair can collide for only `B^{o(1)}` auxiliary primes. No equidistribution hypothesis is needed for (35.3); it is an elementary divisor-support bound.

## 4. Physical fixed-U fiber size

Fix `ell`, `epsilon` and one Gaussian `U` with

\[
N(U)=m\asymp M.
\]

The allowed `V` norms are

\[
N(V)=k\delta,
\qquad
k\mid\varepsilon m,
\qquad
\delta\le \frac{2B}{\varepsilon\ell m}.
\]

Using

\[
r_2(n)\le4\tau(n)=n^{o(1)},
\]

the number of integral Gaussian representatives in the fiber satisfies

\[
\begin{aligned}
J(U)
&\le
\sum_{k\mid\varepsilon m}
\sum_{\delta\le 2B/(\varepsilon\ell m)}
r_2(k\delta)\\
&\ll
\frac{B}{\ell m}B^{o(1)}.
\end{aligned}
\]

Hence on `m~M`,

\[
\boxed{
J(U)\ll \frac{N}{M}B^{o(1)},
\qquad N=B/\ell.
}
\tag{35.4}
\]

The whole unsieved norm skeleton still has mass `N B^{o(1)}` as in t32.

## 5. Same-modulus positive dispersion

Let `H` be a unit-quotiented physical state set on the fixed `(ell,M)` shell and let `P(L)` be the number of admissible split auxiliary primes in `[L,2L]`.

For each auxiliary prime let `C_varpi(H)` count ordered state pairs satisfying the two simultaneous unit-congruences (35.1).

Assume `L>8M`. The exact `U` injection (35.2) and the off-diagonal support bound (35.3) give

\[
\boxed{
\sum_{\varpi\asymp L}C_\varpi(H)
\ll
P(L)|H|
+R_L\sum_U J(U)^2,
}
\tag{35.5}
\]

where

\[
R_L\ll\frac{\log B}{\log L}.
\]

Since

\[
\sum_UJ(U)^2
\le J_{\max}|H|,
\]

(35.4) yields

\[
\boxed{
\sum_{\varpi\asymp L}C_\varpi(H)
\ll
\left(
P(L)+R_L\frac{N}{M}B^{o(1)}
\right)|H|.
}
\tag{35.6}
\]

This is the same-modulus dispersion gain t34 was missing. The off-diagonal term is controlled by the physical fiber size `N/M`, not by the full hyperbola mass `N`.

## 6. What this recovers from t34

The t34 independent tensor product paid a lower envelope

\[
2N\sqrt M.
\]

The shared-prime dispersion collapses the `U`-collision to an exact unit orbit once `L>8M`, so the positive collision analysis no longer carries the polynomial `sqrt(M)` loss.

In this precise sense,

\[
\boxed{
\text{the tensor }\sqrt M\text{ loss is recovered in t35.}
}
\]

This is genuine progress: higher-order Mellin modes are closed by t34, and the independent-modulus geometry is closed by t35.

## 7. Why positive dispersion still does not prove the power saving

To pass from the full `mu_4` character family back to the actual Stage14 trace, a generic Mellin-packet Cauchy/duality step still loses the complete positive spectral energy.

Combining that step with (35.6), `P(L)=L^{1-o(1)}` and the minimal injection scale `L\asymp M` gives only the schematic detector bound

\[
\boxed{
N_{\rm square}(M,N)
\ll
(M^2+N)B^{o(1)}.
}
\tag{35.7}
\]

The important comparison is with the correct ambient norm-hyperbola mass

\[
|H|\ll N B^{o(1)}.
\]

The `N` term in (35.7) is therefore still ambient size. If `M^2>N`, the diagonal term is worse; if `M^2\le N`, the fiber term remains of size `N`.

Thus the **positive collision theorem alone cannot supply a fixed power saving below the norm hyperbola**.

This does not contradict the strong complete torus cancellation from t32. It shows that generic absolute-value/Cauchy treatment destroys the sign information responsible for that cancellation.

## 8. Correct next target: signed fixed-U fiber cancellation

After t35 the useful architecture is

```text
arbitrary Mellin orders
    -> closed by t34 Gauss transform

independent U/V moduli
    -> closed by t35 shared-prime injection

fixed U orbit
    -> V norms k*delta, k|epsilon*m
    -> signed Stage14 auxiliary trace remains
```

The next estimate must keep the actual signed trace inside one fixed `U` fiber rather than replace it by the complete positive character family.

Schematically, for fixed `U`, one must control

\[
\sum_{\delta}
\sum_{k\mid\varepsilon m}
\sum_{N(V)=k\delta}
\chi_\lambda(\widetilde F_{\ell,U}(V))
\]

uniformly over the admissible split auxiliary primes, while retaining the physical interval and local visible/invisible labels.

This is the precise target for Stage14-t36.

## 9. Frozen finite audit

The deterministic audit uses the original `a,b,p,q<=40` search, but imposes a genuine fixed height cutoff

\[
B=10000
\]

and retains only states satisfying

\[
B_{\min}\le10000,
\qquad
\ell^2>4\cdot10000.
\]

This gives

```text
super-sqrt states                 1120
visible                            282
invisible                          838
max m                                5
max N(V)                            74
U-unit fibers                      129
max frozen U-fiber size             32
sum fiber-size^2                 15568
```

The auxiliary split primes

```text
53, 61, 73, 89, 97
```

all satisfy `lambda>8*max(m)=40`, so the exact `U`-orbit injection can be audited directly.

Frozen collision energies are

```text
lambda   total energy   ordered off-diagonal
  53        2166              1046
  61        2044               924
  73        1860               740
  89        1834               714
  97        1790               670
```

No residue bucket contains two distinct integral `U`-unit orbits.

Across the five auxiliary primes, after removing exact `(U,V)` unit-orbit duplicates, the off-diagonal prime-support histogram is

```text
collides at 1 sampled prime: 533 pairs
collides at 2 sampled primes: 142 pairs
maximum sampled support:        2 primes
```

All `675` non-orbit colliding pairs satisfy the divisor-product bound (35.3). Exact full-unit-orbit duplicates account for `246` unordered pairs and, as expected, collide at all five sampled primes.

These computations diagnose the collision geometry only; the asymptotic estimates (35.3)--(35.7) are the mathematical content.

## Literature boundary

The additive Gaussian large sieve used in t34 remains the correct order-free analytic input. Baier--Bansal record Huxley's `Z[i]` large sieve with `(Q^2+N)` strength and develop sparse Gaussian moduli, including Gaussian primes. Stage14-t35 does not require a new black-box theorem beyond that input: the new bound is obtained by elementary shared-prime divisibility and the physical norm-fiber structure.

Reference: S. Baier and A. Bansal, *Large sieve with sparse sets of moduli for Z[i]*, arXiv:1811.07300.

## Boundary

```text
STAGE14_T35=COMPLETE_SHARED_PRIME_DISPERSION_AND_FIBER_BARRIER
SHARED_PRIME_COLLISION_DIVISOR_BOUND=true
L_GT_8M_FORCES_U_UNIT_ORBIT=true
PHYSICAL_U_FIBER_BOUND=N/M*B^o(1)
SAME_MODULUS_POSITIVE_DISPERSION_BOUND=true
TENSOR_SQRT_M_LOSS_RECOVERED=true
GENERIC_PACKET_CAUCHY_BOUND=(M^2+N)*B^o(1)
GENERIC_PACKET_CAUCHY_CLOSES_NORM_HYPERBOLA=false
SIGNED_TRACE_FIBER_CANCELLATION_PROVED=false
NORM_INDEX_HYPERBOLIC_CORRELATION_POWER_SAVING_PROVED=false
VISIBLE_BRANCH_POWER_SAVING_PROVED=false
INVISIBLE_BRANCH_POWER_SAVING_PROVED=false
JOINT_COVER_CONDITIONED_SMOOTH_POWER_SAVING_PROVED=false
A_11_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
NEXT=Stage14-t36 prove signed auxiliary-trace cancellation inside fixed-U fibers (V norm k*delta, k|epsilon*m), using the same-modulus injection to avoid reintroducing the U-dimension loss
```
