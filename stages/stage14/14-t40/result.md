# Stage14-t40 — one-Cauchy cross-kernel and quadratic-Hecke dispersion boundary

## Purpose

Stage14-t39 showed that the external auxiliary split prime cannot be inserted directly into the Friedlander–Iwaniec two-variable Gaussian Dirichlet-symbol form.  With the internal/natural modulus the Stage14 trace becomes constant, while with an external auxiliary modulus the Stage14 trace is nonmultiplicative in the moving Gaussian prime.

Stage14-t40 performs the next operation explicitly: one Cauchy/differencing step in the external auxiliary variable.

The outcome is an important partial success.  The nonmultiplicative Stage14 trace is replaced by an exact **quadratic character in the auxiliary norm**.  Equivalently, after differencing, the auxiliary variable is a norm-induced quadratic Hecke character over `Q(i)`.

The remaining obstruction is no longer character multiplicativity.  It is the energy of the cross squareclasses:

- the principal cross-kernel is exactly the global same-squareclass collision energy;
- the nonprincipal part requires a fourth-order cross-kernel energy and pays the conductor height of the pairwise squarefree kernels.

Thus t40 defines a valid quadratic-Hecke large-sieve interface, but does not yet prove the critical-strip power saving.

## 1. Trilinear form and one Cauchy step

Write the external-auxiliary trilinear sum schematically as

\[
\mathcal T
=\sum_{\lambda\in\Lambda} a_\lambda
  \sum_{j\in\mathcal J} d_j\,\chi_\lambda(F_j),
\qquad j=(\pi,\gamma),
\tag{40.1}
\]

where `lambda` is a good split rational auxiliary prime, `pi` is the moving canonical Gaussian prime, and `gamma` is the descended packet.

Let

\[
P=|\Lambda|.
\]

Cauchy in the auxiliary variable gives

\[
|\mathcal T|^2
\le
P\sum_{\lambda\in\Lambda}
\left|\sum_j d_j\chi_\lambda(F_j)\right|^2.
\tag{40.2}
\]

Expanding,

\[
|\mathcal T|^2
\le
P\sum_{j,j'}d_j\overline{d_{j'}}
K_\Lambda(j,j'),
\tag{40.3}
\]

where

\[
\boxed{
K_\Lambda(j,j')
=\sum_{\lambda\in\Lambda}
\chi_\lambda(F_jF_{j'}).
}
\tag{40.4}
\]

This is the exact cross-kernel created by one differencing step.

## 2. Pairwise squarefree kernel

Let

\[
\kappa_j=\operatorname{sqfree}(|F_j|)
\]

and

\[
\boxed{
\kappa_{j,j'}
=\operatorname{sqfree}(|F_jF_{j'}|).
}
\tag{40.5}
\]

Because `kappa_j,kappa_j'` are squarefree,

\[
\boxed{
\kappa_{j,j'}
=\frac{\kappa_j\kappa_{j'}}{\gcd(\kappa_j,\kappa_{j'})^2}.
}
\tag{40.6}
\]

Associate to a positive squarefree integer `kappa` the positive fundamental discriminant

\[
D(\kappa)
=\begin{cases}
\kappa,&\kappa\equiv1\pmod4,\\
4\kappa,&\text{otherwise}.
\end{cases}
\tag{40.7}
\]

For an odd auxiliary prime `lambda` not dividing `F_jF_j'`, square factors disappear and

\[
\chi_\lambda(F_jF_{j'})
=\left(\frac{\kappa_{j,j'}}{\lambda}\right)
=\chi_{D(\kappa_{j,j'})}(\lambda).
\tag{40.8}
\]

This formula automatically retains the `2`-adic squareclass through the fundamental discriminant; no artificial restriction to `lambda=1 mod 8` is needed.

Therefore

\[
\boxed{
K_\Lambda(j,j')
=\sum_{\lambda\in\Lambda}^{\rm good}
\chi_{D(\kappa_{j,j'})}(\lambda)
+\text{bad-prime correction}.
}
\tag{40.9}
\]

The cross-kernel is now a genuine quadratic Dirichlet character in the auxiliary norm.

## 3. Quadratic-Hecke interpretation over Q(i)

Let `varpi` be a Gaussian prime above `lambda`, so

\[
N(\varpi)=\lambda.
\]

For a fundamental discriminant `D`, define

\[
\boxed{
\eta_D(z)=\chi_D(N(z)).
}
\tag{40.10}
\]

Since the norm is multiplicative,

\[
\eta_D(z_1z_2)=\eta_D(z_1)\eta_D(z_2).
\]

Thus `eta_D` is a quadratic norm-induced Hecke character on `Q(i)` (away from the finite conductor/bad-prime set), and

\[
\eta_D(\varpi)
=\chi_D(\lambda).
\tag{40.11}
\]

This is the key success of t40:

> one Cauchy step removes the t39 nonmultiplicativity obstruction in the auxiliary variable.

The relevant large-sieve interface is now genuine.  Goldmakher–Louvel's quadratic large sieve over number fields applies to quadratic Hecke families; because this particular family is norm-induced from `Q`, the classical rational quadratic large sieve is already sufficient for the auxiliary variable.

## 4. Principal cross-kernel

The principal character occurs exactly when

\[
\kappa_{j,j'}=1.
\]

By (40.6), this is equivalent to

\[
\boxed{
\kappa_j=\kappa_{j'}.
}
\tag{40.12}
\]

Hence the principal coefficient is exactly the global rational-squareclass collision energy.

If

\[
r(\kappa)=\#\{j:\kappa_j=\kappa\},
\]

then in the unweighted case

\[
\boxed{
A_1
=\sum_\kappa r(\kappa)^2.
}
\tag{40.13}
\]

Every pair of Stage14 targets belongs to the trivial squareclass, so

\[
R^2\le A_1.
\tag{40.14}
\]

This term cannot be canceled by a quadratic large sieve: it is the principal character.

The fiberwise energy results from t36/t37 do not yet bound (40.13), because there both sides were not allowed to move simultaneously through the full critical-strip `(pi,gamma)` family.

## 5. Nonprincipal aggregation and fourth-order energy

For every fundamental discriminant `D`, put

\[
A_D
=\sum_{\substack{j,j'\\D(\kappa_{j,j'})=D}}
 d_j\overline{d_{j'}}.
\tag{40.15}
\]

The nonprincipal part of (40.3) has the form

\[
\sum_{D\ne1} A_D
\sum_{\lambda\in\Lambda}a_\lambda\chi_D(\lambda).
\tag{40.16}
\]

Define the fourth-order cross-kernel energy

\[
\boxed{
E_4=\sum_D |A_D|^2.
}
\tag{40.17}
\]

If all relevant cross conductors satisfy

\[
|D|\le K
\]

and the auxiliary norms are in a range `lambda<=Q`, Cauchy followed by a quadratic large sieve gives schematically

\[
\boxed{
\left|\sum_{D\ne1}A_DS_D\right|
\ll
E_4^{1/2}(K+Q)^{1/2}P^{1/2}(KQ)^\varepsilon.
}
\tag{40.18}
\]

Therefore the one-Cauchy dispersion bound becomes

\[
\boxed{
|\mathcal T|^2
\ll
P^2A_1
+P^{3/2}(K+Q)^{1/2}E_4^{1/2}(KQ)^\varepsilon
+\mathcal E_{\rm bad}.
}
\tag{40.19}
\]

This is the correct quadratic-Hecke boundary produced by one differencing step.

## 6. Pairwise bad auxiliary primes

Equation (40.8) assumes

\[
\lambda\nmid F_jF_{j'}.
\]

If `lambda` divides a square factor of `F_jF_j'`, it may disappear from the squarefree kernel while the original Legendre symbol is zero.  Therefore the kernel character alone does not represent those bad incidences.

This is a finite-divisor error, not a new spectral obstruction.  Every physical `F_j` has polynomial size in `B`, so it has only `B^{o(1)}` distinct prime divisors.  The pairwise bad auxiliaries can therefore be excluded or charged separately at subpolynomial state loss.

## 7. Safe conductor bound

From the physical bounds

\[
a^2+b^2\le2B,
\qquad
p^2+q^2\le2B,
\]

we have

\[
|a|,|b|,|p|,|q|\le\sqrt{2B}.
\]

Each t28 linear factor

\[
g_i\in\{bp-aq,\ aq+bp,\ bq-ap,\ bq+ap\}
\]

therefore satisfies

\[
|g_i|\le4B.
\]

Hence

\[
|F_j|=|g_1g_2g_3g_4|\le256B^4.
\tag{40.20}
\]

For a pair,

\[
\kappa_{j,j'}\le |F_jF_{j'}|\le2^{16}B^8,
\]

and the fundamental discriminant obeys the safe bound

\[
\boxed{
|D(\kappa_{j,j'})|\le2^{18}B^8.
}
\tag{40.21}
\]

Thus a completely generic conductor-aspect quadratic large sieve carries a potentially very large `K` cost.  The number-field large sieve is valid, but conductor control is not automatically strong enough to close the critical strip.

## 8. What t40 closes and what remains

Closed in t40:

- the external auxiliary trace becomes multiplicative after one differencing step;
- the cross-kernel is a genuine quadratic Dirichlet character in the auxiliary norm;
- equivalently it is a norm-induced quadratic Hecke character over `Q(i)`;
- a valid quadratic-Hecke large-sieve interface is obtained.

Still open:

- the global principal collision energy `A_1`;
- the fourth-order cross-kernel energy `E_4`;
- reduction of the safe conductor scale below the crude `B^8` barrier;
- the critical `ell=B^(1/2+o(1))` power saving.

The natural next stage is therefore an energy/incidence stage rather than another character-identification stage.

## Frozen audit

The t36 frozen population is regenerated and t40 computes the global squareclass and pair-kernel energies.  It also checks the good-auxiliary identity

\[
\chi_\lambda(F_jF_{j'})
=\chi_{D(\kappa_{j,j'})}(\lambda)
\]

on a deterministic pair sample, verifies multiplicativity of the norm-induced character, and checks the safe `B^8` conductor bound.

Exact frozen counts are stored in

`stages/stage14/data/14-t40/cross_kernel_hecke_dispersion.json`.

## Locked boundary

```text
STAGE14_T40=COMPLETE_ONE_CAUCHY_QUADRATIC_HECKE_CROSS_KERNEL_AND_ENERGY_BOUNDARY
ONE_CAUCHY_REMOVES_EXTERNAL_TRACE_NONMULTIPLICATIVITY=true
CROSS_KERNEL_IS_QUADRATIC_DIRICHLET_CHARACTER_IN_AUXILIARY_NORM=true
CROSS_KERNEL_IS_NORM_INDUCED_QUADRATIC_HECKE_CHARACTER_OVER_QI=true
QUADRATIC_HECKE_LARGE_SIEVE_INTERFACE_VALID=true
PRINCIPAL_CROSS_KERNEL_EQUALS_GLOBAL_SQUARECLASS_COLLISION=true
FOURTH_ORDER_CROSS_KERNEL_ENERGY_REQUIRED=true
SAFE_CROSS_CONDUCTOR_BOUND=2^18*B^8
GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED=false
GLOBAL_FOURTH_ENERGY_POWER_SAVING_PROVED=false
CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED=false
CANONICAL_PRIME_SUM_POWER_SAVING_PROVED=false
A_11_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
NEXT=Stage14-t41 analyze the principal and fourth-order cross-kernel energies globally by combining the t38 moving-prime genus-one fibers with the t37 reverse fibers
```
