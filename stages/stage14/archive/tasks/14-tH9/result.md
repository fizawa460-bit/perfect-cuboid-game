# Stage14-tH9 — squareclass cross-ratio atlas for one-Cauchy dispersion

## Purpose

Stage14-tH8 standardized the external-auxiliary trilinear packet and the two exact one-Cauchy dispersion routes.  Merged Stage14-t40 has since closed the character-algebra part of the auxiliary-family route: for a pair of physical states `j,j'`, the good auxiliary trace

\[
\chi_\lambda(F_jF_{j'})
\]

is exactly a quadratic Dirichlet character in the auxiliary norm, equivalently a norm-induced quadratic Hecke character over `Q(i)`.

Thus the remaining obstruction is no longer whether a Hecke character exists.  It is the size of the principal squareclass collision and the fourth-order cross-kernel coefficient energy.

Stage14-tH9 turns that remaining object into a reusable squareclass/cross-ratio atlas.  The output is independent infrastructure: it imports merged t40 as a stable demand signal but does not require t41 or any later `t` stage.

No new Stage14 power saving, `A_{1,1}` estimate, or `T=o(sqrt(B))` theorem is claimed.

---

## 1. Squareclass group notation

For every nonzero physical value `F_j`, let

\[
\sigma_j=\operatorname{sqf}(|F_j|)
\]

be its positive squarefree kernel.  Split auxiliary rational primes satisfy `lambda == 1 mod 4`, so the sign of `F_j` is invisible to the local quadratic character; the positive representative is therefore the correct frozen convention for this roadwork.

On positive squarefree integers define

\[
s\oplus t := \operatorname{sqf}(st)
=\frac{st}{\gcd(s,t)^2}.
\tag{9.1}
\]

This is multiplication in the rational squareclass group `Q^*/Q^{*2}` restricted to positive classes.  It has

```text
identity:      1
self inverse:  s xor s = 1
commutative:   s xor t = t xor s
associative:   (s xor t) xor u = s xor (t xor u)
```

where the symbol `xor` denotes `oplus`, not bitwise integer XOR.

The t40 pair kernel is exactly

\[
\boxed{\kappa_{jk}=\sigma_j\oplus\sigma_k.}
\tag{9.2}
\]

Hence the entire one-Cauchy cross-kernel family is an elementary two-torsion squareclass geometry.

---

## 2. Principal kernel is equality of vertex squareclasses

From (9.2),

\[
\kappa_{jk}=1
\iff
\sigma_j=\sigma_k.
\tag{9.3}
\]

For unweighted states, if

\[
r(s)=\#\{j:\sigma_j=s\},
\]

then the principal pair count is

\[
\boxed{A_1=\sum_s r(s)^2.}
\tag{9.4}
\]

This recovers the t40 identification of the principal cross kernel with the global same-squareclass collision energy.

For general coefficients `d_j`, first compress them by squareclass:

\[
W(s)=\sum_{j:\sigma_j=s}d_j.
\tag{9.5}
\]

Then the weighted principal coefficient is exactly

\[
\boxed{A(1)=\sum_s |W(s)|^2.}
\tag{9.6}
\]

Thus all state-level principal collisions may be collapsed to squareclass-level weights before any analytic estimate.

---

## 3. Every pair coefficient is a squareclass autocorrelation

For a cross kernel `kappa`, define

\[
A(\kappa)
=
\sum_{j,k:\,\sigma_j\oplus\sigma_k=\kappa}
 d_j\overline{d_k}.
\tag{9.7}
\]

After the compression (9.5), this becomes

\[
\boxed{
A(\kappa)=
\sum_s W(s)\overline{W(s\oplus\kappa)}.
}
\tag{9.8}
\]

So the full t40 family of pair coefficients is the autocorrelation of one function `W` on the observed squareclass group.

For unweighted states, `W(s)=r(s)` and

\[
R(\kappa)=\sum_s r(s)r(s\oplus\kappa)
\tag{9.9}
\]

counts ordered pairs with pair kernel `kappa`.

This is a strict compression:

```text
state layer        -> squareclass weights W(s)
pair layer         -> autocorrelation A(kappa)
principal layer    -> A(1)
fourth layer       -> ||A||_2^2
```

No information used by the t40 one-Cauchy large-sieve interface is lost.

---

## 4. Fourth-order energy is additive/squareclass energy

T40 requires

\[
E_4=\sum_D |A_D|^2.
\]

For positive squarefree `kappa`, the associated fundamental discriminant

\[
D(\kappa)=
\begin{cases}
\kappa,&\kappa\equiv1\pmod4,\\
4\kappa,&\text{otherwise}
\end{cases}
\tag{9.10}
\]

is injective in `kappa`.  Therefore reindexing by discriminant or by squareclass kernel is lossless:

\[
\boxed{E_4=\sum_\kappa |A(\kappa)|^2.}
\tag{9.11}
\]

In the unweighted case,

\[
\boxed{E_4=\sum_\kappa R(\kappa)^2.}
\tag{9.12}
\]

Equivalently, `E4` counts weighted quadruples satisfying

\[
\sigma_i\oplus\sigma_j
=
\sigma_k\oplus\sigma_l,
\]

or

\[
\boxed{
\sigma_i\oplus\sigma_j\oplus\sigma_k\oplus\sigma_l=1.
}
\tag{9.13}
\]

This is exactly the additive energy of the squareclass multiset, viewed as an elementary 2-group.

The principal contribution is one term of this energy:

\[
E_4=|A(1)|^2+\sum_{\kappa\ne1}|A(\kappa)|^2.
\tag{9.14}
\]

For the frozen t40 population,

```text
states                         1120
distinct squareclasses          544
A1                              2368
E4                          21193216
A1^2                         5607424
off-principal E4            15585792
```

These are finite diagnostics, not asymptotic exponents.

---

## 5. Cross-ratio collision certificate

For two ordered pairs `(i,j)` and `(k,l)`, define the squareclass cross ratio

\[
\rho(i,j;k,l)
=
\kappa_{ij}\oplus\kappa_{kl}
=
\sigma_i\oplus\sigma_j\oplus\sigma_k\oplus\sigma_l.
\tag{9.15}
\]

Then

\[
\boxed{
\rho(i,j;k,l)=1
\iff
\kappa_{ij}=\kappa_{kl}.
}
\tag{9.16}
\]

Thus a fourth-order cross-kernel collision has a one-line exact certificate: the four physical values multiply to a rational squareclass.

The atlas also records the triangle law

\[
\boxed{
\kappa_{ij}\oplus\kappa_{jk}=\kappa_{ik}
}
\tag{9.17}
\]

and the four-cycle law

\[
\boxed{
\kappa_{ij}\oplus\kappa_{jk}\oplus\kappa_{kl}\oplus\kappa_{li}=1.
}
\tag{9.18}
\]

These identities are useful diagnostics when a later incidence decomposition produces several pair kernels that look independent: they are not independent squareclass variables.

---

## 6. Basepoint compression

Fix one observed squareclass `sigma_0`.  Define

\[
v_j=\sigma_j\oplus\sigma_0.
\tag{9.19}
\]

Then every pair kernel is recovered by

\[
\boxed{\kappa_{ij}=v_i\oplus v_j.}
\tag{9.20}
\]

Therefore a complete squareclass atlas needs only one vertex label per state/class plus the group operation.  It never needs to store an independent label for every pair.

This prevents a common combinatorial mistake: treating the `H^2` ordered cross pairs as `H^2` independent arithmetic moduli.  They are generated by `H` vertex squareclasses.

---

## 7. Route-A Hecke certificate after t40

For a good split auxiliary prime `lambda`, t40 proves

\[
\chi_\lambda(F_jF_k)
=
\chi_{D(\kappa_{jk})}(\lambda).
\tag{9.21}
\]

Pulling back from the rational norm gives

\[
\eta_D(z)=\chi_D(Nz),
\tag{9.22}
\]

which is a norm-induced quadratic Hecke character over `Q(i)`.

T9 therefore classifies the auxiliary-family route as follows.

### Nonprincipal kernel

```text
kappa != 1
D = D(kappa)
status = QUADRATIC_HECKE_READY
```

subject to the explicit good-auxiliary condition `lambda not dividing F_j F_k`.

### Principal kernel

```text
kappa = 1
status = PRINCIPAL_COLLISION
analytic character cancellation = none
charge to A(1)
```

### Bad auxiliary incidence

```text
lambda | F_j F_k
status = BAD_AUXILIARY_ZERO
remove/charge separately
```

This is stronger and cleaner than the pre-t40 tH8 certificate: for Route A the Hecke certificate is now proved, while the global energy saving remains open.

---

## 8. Route-B status

T8's physical-packet Cauchy route contains

\[
H_{\mathcal X}(\lambda,\mu)
=
\sum_j
\chi_\lambda(F_j)\chi_\mu(F_j).
\tag{9.23}
\]

At the value level, for good coprimality this is a quadratic Dirichlet character of the integer `F_j` modulo the product `lambda*mu`.

However this alone does **not** supply a multiplicative family in the physical packet variable `j=(pi,gamma)`.  No canonical multiplication law on the Stage14 packet index has been exhibited which turns `F_j` into a multiplicative Gaussian numerator with separated coefficients.

Therefore the correct certificate is

```text
VALUE_LEVEL_QUADRATIC_CHARACTER=true
PHYSICAL_PACKET_MULTIPLICATIVE_PARAMETERIZATION_PROVED=false
PHYSICAL_ROUTE_FI_READY=false
PHYSICAL_ROUTE_HECKE_PACKET_READY=false
```

T9 does not fabricate a two-variable FI representation for Route B.

---

## 9. Exact frozen audit

The deterministic audit imports the actual t36 frozen 1120-state population through the same construction used by t40 and checks:

- t40 frozen counts and energies are reproduced exactly;
- the squareclass operation is involutive and associative on all observed classes used by the audit;
- every pair kernel is `sigma_i xor sigma_j`;
- `R(kappa)` equals the squareclass autocorrelation `sum_s r(s)r(s xor kappa)`;
- `R(1)=A1`;
- `E4=sum_kappa R(kappa)^2`;
- fundamental-discriminant reindexing is injective;
- triangle and sampled four-cycle identities hold;
- sampled cross-ratio equality is equivalent to pair-kernel collision;
- a deterministic signed weighted state family satisfies the compressed weighted autocorrelation identity;
- good auxiliary Route-A traces reproduce the t40 quadratic Dirichlet/Hecke kernel;
- Route-B product characters are correctly classified as value-level quadratic characters only.

The frozen t40 regression values are

```text
states                              1120
distinct squareclasses               544
max squareclass multiplicity           4
A1                                   2368
ordered cross pairs               1254400
distinct cross kernels             132961
E4                               21193216
good reciprocity checks              76437
norm-pullback multiplicativity        1244
```

---

## 10. What tH9 changes for the live proof search

After t40 and tH9, there is no remaining ambiguity in the auxiliary-family character algebra.

The open object is now precisely the squareclass autocorrelation energy of the physical family:

\[
W(s)
\longmapsto
A(\kappa)=\sum_s W(s)\overline{W(s\oplus\kappa)}
\longmapsto
E_4=\sum_\kappa|A(\kappa)|^2.
\tag{9.24}
\]

Consequently, a useful future roadwork stage should attack one of:

1. a two-sided incidence bound for squareclass fibers `W(s)`;
2. a direct autocorrelation-energy inequality for the moving-prime/reverse-fiber geometry;
3. a decomposition into low-energy generic classes plus explicitly classified structured exceptional classes;
4. a Fourier/character analysis on the finite squareclass subgroup generated by a dyadic block, if its rank can be controlled without polynomial loss.

Repeating the Hecke conversion itself is no longer useful.

---

## Boundary

```text
STAGE14_TH9=COMPLETE_SQUARECLASS_CROSS_RATIO_AND_AUTOCORRELATION_ATLAS
TH_REQUIRES_FUTURE_T_RESULT=false
T40_ONE_CAUCHY_HECKE_BOUNDARY_IMPORTED=true
PAIR_KERNEL_IS_SQUARECLASS_DIFFERENCE=true
PRINCIPAL_KERNEL_IFF_EQUAL_SQUARECLASS=true
PAIR_COEFFICIENT_IS_SQUARECLASS_AUTOCORRELATION=true
FOURTH_ENERGY_IS_SQUARECLASS_ADDITIVE_ENERGY=true
CROSS_RATIO_COLLISION_CERTIFICATE_PROVED=true
FUNDAMENTAL_DISCRIMINANT_REINDEXING_LOSSLESS=true
AUXILIARY_ROUTE_QUADRATIC_HECKE_CERTIFICATE_PROVED=true
PHYSICAL_ROUTE_VALUE_LEVEL_QUADRATIC_CHARACTER=true
PHYSICAL_ROUTE_HECKE_PACKET_CERTIFICATE_PROVED=false
GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED=false
GLOBAL_FOURTH_ENERGY_POWER_SAVING_PROVED=false
CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED=false
A_11_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
NEXT=Stage14-tH10 build reusable squareclass-fiber/autocorrelation energy incidence tools for A1 and E4, independent of t41
```
