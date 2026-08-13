# Stage14-t47 — tH13 shell instantiation and centered spectral detector

## Status

Stage14-t47 directly instantiates the merged Stage14-tH13 sparse many-conductor adapter on the merged Stage14-t46 twist-independent squareclass-character operator.

The stage makes two reductions:

1. it replaces the crude maximum-conductor envelope by the actual dyadic conductor-energy ledger of the frozen t46 base family;
2. it replaces the t45 two-endogenous-prime detector, whose positive expansion has the fixed constant term `1/4`, by an exact centered spectral detector on a growing family of canonical-prime tests.

No critical-strip, `A_11`, or `T(B)=o(sqrt(B))` power saving is claimed.

---

## 1. Inputs from t46 and tH13

For the reciprocal-quotiented frozen population,

```text
H                                  560
distinct squareclasses             544
A1                                 592
distinct canonical test primes      87
canonical-prime coefficient energy 7184
max frozen test prime             1889
max base fundamental discriminant 224158076
```

Stage14-t46 gives a single twist-independent quadratic-character matrix

\[
M(\ell,\kappa)=\chi_{D(\kappa)}(\ell),
\]

because on good rows

\[
\chi_{D(\tau\kappa)}(\ell)
=
\chi_\tau(\ell)\chi_{D(\kappa)}(\ell).
\]

Stage14-tH13 supplies the shell receiver

\[
|\mathcal B_R(Q)|
\ll B^{o(1)}E_\ell^{1/2}E_D(Q)^{1/2}
\min\{(L+Q)^{1/2},(P_RK_R(Q))^{1/2}\}
\]

and the same-modulus / product-kernel dispersion identity.

---

## 2. Actual conductor-energy ledger

The 544 base squareclasses occupy 24 dyadic fundamental-discriminant shells.

For the frozen `B=10000` population the actual nonprincipal weighted conductor energy is

\[
\mathfrak W_D
=
1,739,979,879.
\]

The corresponding crude maximum-range envelope is

\[
(L+D_{\max})A_1
=
132,702,699,280.
\]

Hence

\[
\boxed{
\frac{\mathfrak W_D}{(L+D_{\max})A_1}
\approx0.013111865.
}
\]

So the tH13 conductor-energy refinement is numerically substantial: the actual frozen energy is about `1.31%` of the max-range envelope.

This is not an asymptotic theorem.

Using the tH13 finite exponent proxy

\[
p+k-\max(1/2,q),
\]

only `63` units of the frozen squareclass energy `592` lie in positive-proxy shells, while `529` lie in nonpositive-proxy shells.  Thus the shell ledger alone does not close the critical strip.

The largest weighted shell is the highest frozen conductor shell:

```text
Q=134217728
K=3
E=3
Dmax=224158076
weighted contribution=600465591
```

The high-conductor tail therefore remains quantitatively relevant despite its small support cardinality.

---

## 3. Centered detector removes the `1/4` baseline

Let `r_kappa` denote the multiplicity of squareclass `kappa`, and let `P` be a set of good canonical-prime tests.  Define

\[
W_{p,\kappa}=\sqrt{r_\kappa}\,\chi_\kappa(p),
\]

and its row Gram matrix

\[
G_{p,q}
=
(WW^T)_{p,q}
=
\sum_\kappa r_\kappa\chi_\kappa(p)\chi_\kappa(q).
\]

For the target squareclass `1`, every character value is `1`.  Therefore

\[
r(1)P^2
\le
\|W^T\mathbf 1\|^2
\le
P\lambda_{\max}(G).
\]

Hence the exact centered spectral receiver is

\[
\boxed{
r(1)\le\frac{\lambda_{\max}(G)}{P}.
}
\]

By the Schur bound,

\[
\boxed{
r(1)
\le
\frac HP
+
\frac1P\max_p\sum_{q\ne p}|G_{p,q}|.
}
\]

Unlike the t45 product of two local square tests, this detector has no fixed `1/4` term.  The diagonal contribution is `H/P`, which can decay if the test family grows.

This is an exact reduction, but a uniform physical row-correlation estimate is still needed.

### Frozen single-state diagnostic

```text
P                                      87
H/P                              6.43678
Gram diagonal                    556..560
max |G_pq|                            83
max pair                         (229,461)
max off-diagonal L1 row sum          2085
Schur lambda upper                   2645
power-iteration lambda diagnostic ~1052.06
```

These finite values are diagnostic only.

---

## 4. Principal pair energy is the Hadamard-square Gram problem

For ordered pairs of states, squareclass characters multiply.  Therefore the pair Gram matrix is exactly

\[
G_{\rm pair}=G\circ G,
\]

where `circ` denotes the Hadamard square.

At twist `1`, the pair-squareclass multiplicity is

\[
c(1)=A_1.
\]

The same centered argument gives

\[
\boxed{
A_1\le\frac{\lambda_{\max}(G\circ G)}{P}.
}
\]

and Schur gives

\[
\boxed{
A_1
\le
\frac{H^2}{P}
+
\frac1P\max_p\sum_{q\ne p}|G_{p,q}|^2.
}
\]

Thus the global principal collision problem is now an explicit physical row-correlation problem for the same base character matrix used by t46/tH13.

### Frozen pair diagnostic

```text
max off-diagonal squared row sum          73273
Schur lambda upper                       386873
power-iteration lambda diagnostic     ~361523.71
finite Schur A1 upper                   ~4446.82
actual frozen A1                            592
```

The finite spectral upper bound remains loose; no asymptotic power saving is promoted from it.

---

## 5. Exact proof contract handed to t48

A sufficient single-state condition is:

\[
P\ge B^\rho,
\qquad
\max_p\sum_{q\ne p}|G_{p,q}|
\le HPB^{-\delta}.
\]

Then

\[
r(1)
\le
H B^{-\rho}+H B^{-\delta}.
\]

For the global principal pair energy, it is sufficient that

\[
P\ge B^\rho,
\qquad
\max_p\sum_{q\ne p}|G_{p,q}|^2
\le H^2PB^{-\delta},
\]

because then

\[
A_1
\le
H^2B^{-\rho}+H^2B^{-\delta}.
\]

The missing input is therefore no longer an abstract sparse large sieve.  It is a **uniform physical row-correlation / spectral estimate** for the Stage14 squareclass family, together with the existing tH12 common-refinement aggregation ledger.

This is the target for Stage14-t48.

---

## 6. tH判定

**追加tHは不要。Stage14-tH14はまだ起こさない。**

Stage14-tH13 already contains exactly the same-modulus / product-kernel dispersion receiver needed by the centered Gram expansion.  Stage14-t47 has now specialized that receiver to the physical matrix `G`.

The next missing object is a live arithmetic estimate for the correlations `G_{p,q}`, not another generic adapter.

Reopen tH only if Stage14-t48 exposes a new concrete correlation structure that cannot be expressed through the tH13 receiver.

---

## Locked boundary

```text
STAGE14_T47=COMPLETE_TH13_SHELL_INSTANTIATION_AND_CENTERED_SPECTRAL_DETECTOR_REDUCTION
TH13_USED_DIRECTLY=true
CONDUCTOR_ENERGY_REFINEMENT_INSTANTIATED=true
CENTERED_DETECTOR_REMOVES_ONE_QUARTER_CONSTANT_TERM=true
SINGLE_STATE_TARGET_REDUCES_TO_BASE_OPERATOR_SPECTRAL_NORM=true
PAIR_PRINCIPAL_ENERGY_REDUCES_TO_HADAMARD_GRAM_SPECTRAL_NORM=true
CENTERED_DISPERSION_IS_TH13_PRODUCT_KERNEL_RECEIVER=true
UNIFORM_PHYSICAL_ROW_CORRELATION_POWER_SAVING_PROVED=false
GLOBAL_PRINCIPAL_COLLISION_POWER_SAVING_PROVED=false
GLOBAL_FOURTH_ENERGY_POWER_SAVING_PROVED=false
CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED=false
A_11_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
TH14_NEEDED=false
NEXT=Stage14-t48 prove a uniform physical row-correlation/spectral estimate for the squareclass character Gram matrix, or classify exceptional coherent rows using common-core/canonical-prime geometry
```
