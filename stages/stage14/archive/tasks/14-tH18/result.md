# Stage14-tH18 — private canonical-prime opposite-sign root-modulus large-sieve audit

## Purpose

Merged Stage14-t67 has already removed every radial/combinatorial issue that should not be charged to the next analytic receiver.  In a fixed

```text
(U, epsilon, k, h)
```

packet it replaces the old `(ell,delta)` hyperbola by the single odd root modulus

\[
M=\ell H D,
\qquad
H=\operatorname{odd}(h),
\qquad
D=\operatorname{odd}(\delta),
\tag{H18.1}
\]

with

\[
\ell=\operatorname{LPF}_{\rm odd}(M),
\qquad
2HD<\ell,
\tag{H18.2}
\]

and the exact opposite-sign root orientation

\[
\rho^2\equiv +\kappa\pmod{\ell H},
\qquad
\rho^2\equiv -\kappa\pmod D.
\tag{H18.3}
\]

After same-`M`, same-`ell`, and nested-canonical-prime pairs are removed, the only live principal pair is cross-modulus and **private**:

\[
\ell_1\nmid M_2,
\qquad
\ell_2\nmid M_1.
\tag{H18.4}
\]

Stage14-tH18 independently audits only

```text
PrivateCanonicalPrimeOppositeSignRootModulusLargeSieve
```

and in particular does **not** reopen:

```text
(ell,delta) hyperbola multiplicity
CRT root count
fixed-M lift multiplicity
same-ell squareclass energy
nested canonical-prime incidence
```

The conclusion is negative for direct theorem import but positive for the reduction: the private packet admits an exact CRT reciprocal-phase formulation, the generic additive large sieve gives only a `Q^2+N` scale, and the Fouvry--Iwaniec `Q+N` quadratic-root phenomenon does not directly apply because the two quadratic root families carry mutually moving reciprocal twists.  The missing theorem can therefore be stated exactly.

No new whole-family power saving is claimed here.

---

## 1. Imported t67 locks; no double charging

Throughout, `H=odd(h)` is fixed and a physical state supplies

\[
M=\ell H D,
\qquad
c=M/\ell=HD<\ell/2.
\tag{H18.5}
\]

Merged t67 proves:

```text
ell = LPF_odd(M)
D = M/(ell*H)
2*sqrt(B) < M <= 2B/k
fixed-M physical multiplicity = B^o(1)
same-M energy = near-linear
same-ell energy = near-linear
nested canonical-prime incidence = near-linear
```

All of these are theorem inputs, not tH18 proof obligations.

For a live private pair `s_1,s_2`, t67 also proves

\[
\gcd(M_1,M_2)=\gcd(c_1,c_2).
\tag{H18.6}
\]

In particular neither private largest prime occurs in the common modulus.

```text
T67_RADIAL_COLLAPSE_REOPENED=false
T67_FIXED_M_REOPENED=false
T67_SAME_ELL_REOPENED=false
T67_NESTED_PAIR_REOPENED=false
```

---

## 2. The mixed root is globally a fixed quartic root, but orientation is essential

From (H18.3), on every prime-power factor of `M`,

\[
\rho^4\equiv\kappa^2.
\]

Hence globally

\[
\boxed{\rho^4\equiv\kappa^2\pmod M.}
\tag{H18.7}
\]

Equivalently every physical root lies among roots of the fixed reducible quartic

\[
X^4-\kappa^2=(X^2-\kappa)(X^2+\kappa).
\tag{H18.8}
\]

This observation is useful but cannot erase the t66/t67 side allocation.  The physical subset is not the set of all roots of (H18.8):

- the canonical factor `ell*H` is assigned to `X^2-kappa`;
- the cover factor `D` is assigned to `X^2+kappa`;
- `ell` is the private largest prime and occurs to exponent one.

Thus any quartic/biquadratic ideal parameterisation must retain the factor-orientation label.

```text
GLOBAL_BIQUADRATIC_ROOT_ENVELOPE_PROVED=true
OPPOSITE_SIGN_ROOT_ORIENTATION_DROPPABLE=false
```

---

## 3. Exact cross-modulus root-fraction spacing

Because merged t66 proves `gcd(M,kappa)=1`, (H18.3) implies

\[
\gcd(\rho,M)=1.
\tag{H18.9}
\]

Therefore `rho/M` is a reduced rational point.

Take two distinct private states.  Put

\[
g=\gcd(M_1,M_2)=\gcd(c_1,c_2)
\tag{H18.10}
\]

and

\[
\Delta_{12}=\rho_1M_2-\rho_2M_1.
\tag{H18.11}
\]

Since both terms in (H18.11) are divisible by `g`,

\[
g\mid\Delta_{12}.
\tag{H18.12}
\]

The fractions cannot be equal: equality of two reduced positive fractions would force `M_1=M_2`, already removed by t67.  Hence `Delta_12 != 0`, and the circular distance obeys the universal Farey-scale lower bound

\[
\boxed{
\left\|\frac{\rho_1}{M_1}-\frac{\rho_2}{M_2}\right\|
\ge
\frac{g}{M_1M_2}
=
\frac1{\operatorname{lcm}(M_1,M_2)}.
}
\tag{H18.13}
\]

Privacy gives a second exact fact, but it points in the opposite direction from a hoped-for spacing gain.  Modulo the private prime `ell_1`,

\[
\Delta_{12}\equiv \rho_1M_2\not\equiv0\pmod{\ell_1},
\tag{H18.14}
\]

and similarly `ell_2` does not divide `Delta_12`.  Thus the private canonical primes are **not** forced factors of the cross determinant.  The only forced divisibility visible from the t67 structure is the common cofactor `g=gcd(c_1,c_2)`.

Consequently privacy alone does not upgrade (H18.13) to `1/Q` spacing for `M_i~Q`.

### Explicit legal close-pair guard

The deterministic audit freezes the following synthetic packet with

```text
kappa = 1
H = 1
M1 = 229 * 65 = 14885
M2 = 233 * 65 = 15145
rho1 = 2062
rho2 = 2098
```

where `65=5*13`, all odd local primes are `1 mod 4`,

```text
rho_i^2 = +1 mod ell_i
rho_i^2 = -1 mod 65
2*65 < ell_i
ell1 not|M2
ell2 not|M1.
```

Yet

\[
\left|\frac{2062}{14885}-\frac{2098}{15145}\right|
=
\frac4{3468205}
<
\frac1{15145}.
\tag{H18.15}
\]

So a proof based only on pairwise `1/Q` separation is impossible even inside the exact private opposite-sign model.

```text
PRIVATE_PRIME_FORCES_ONE_OVER_Q_SPACING=false
PRIVATE_CLOSE_ROOT_FRACTION_COUNTERMODEL_RECORDED=true
```

---

## 4. Generic additive large sieve: valid, but it has the `Q^2` barrier

Let `Omega(Q)` be any dyadic family of t67 private root fractions

\[
\rho/M,
\qquad Q<M\le2Q.
\]

Each modulus has only `B^o(1)` admissible CRT roots, already certified in t66.  With only the generic reduced-fraction spacing (H18.13), the ordinary additive large sieve gives the safe bound

\[
\boxed{
\sum_{(M,\rho)\in\Omega(Q)}
\left|
\sum_{n\in I}a_ne\!\left(\frac{n\rho}{M}\right)
\right|^2
\ll
(N+Q^2)B^{o(1)}
\sum_{n\in I}|a_n|^2,
}
\tag{H18.16}
\]

for an interval `I` of length `N`.

This is a legal fallback theorem, but the `Q^2` term is polynomially too large in the t67 super-square-root band.  The desired root-specific phenomenon is the Fouvry--Iwaniec scale `Q+N`, not the generic Farey scale `Q^2+N`.

```text
GENERIC_PRIVATE_ROOT_FRACTION_LARGE_SIEVE_PROVED=true
GENERIC_PRIVATE_ROOT_FRACTION_LARGE_SIEVE_SCALE=(Q^2+N)*B^o(1)
GENERIC_LARGE_SIEVE_CLOSES_PRIVATE_RECEIVER=false
```

---

## 5. Exact CRT reciprocal-phase factorisation

Put

\[
A=\ell H,
\qquad
D=M/A,
\qquad
(A,D)=1.
\tag{H18.17}
\]

Let

\[
\alpha\equiv\rho\pmod A,
\qquad
\beta\equiv\rho\pmod D.
\]

Then

\[
\alpha^2\equiv+\kappa\pmod A,
\qquad
\beta^2\equiv-\kappa\pmod D.
\tag{H18.18}
\]

CRT reconstructs

\[
\rho\equiv
\alpha D\overline D_A
+
\beta A\overline A_D
\pmod{AD},
\tag{H18.19}
\]

where `bar(D)_A` denotes the inverse of `D mod A`, etc.  Therefore the additive root phase factors exactly as

\[
\boxed{
e_M(n\rho)
=
e_A(n\alpha\overline D_A)
\,e_D(n\beta\overline A_D).
}
\tag{H18.20}
\]

Equation (H18.20) is the central tH18 structural identity.

It explains both why quadratic-root technology is relevant and why the standard one-variable theorem is not a direct import.  The `+kappa` root and `-kappa` root are each classical quadratic-root families, but each carries the inverse of the **other moving modulus** as its additive twist.

```text
OPPOSITE_SIGN_CRT_RECIPROCAL_PHASE_FACTORIZATION_PROVED=true
MOVING_CROSS_RECIPROCAL_TWISTS_PRESERVED=true
```

---

## 6. Fouvry--Iwaniec root large sieve: near-perfect shape, wrong quantifiers

The Fouvry--Iwaniec Gaussian-prime machinery supplies a large sieve for roots of a fixed quadratic congruence.  A standard quoted form for roots `nu^2+1=0 mod d`, `d~D_0`, with one **fixed** coprime twist `q`, is

\[
\sum_{d\sim D_0}
\sum_{\nu^2+1\equiv0(d)}
\left|
\sum_{n\le N}\gamma_n e_d(\nu n\overline q)
\right|^2
\ll
(qD_0+N)\sum|\gamma_n|^2.
\tag{H18.21}
\]

This is precisely the kind of linear-in-modulus scale that would be valuable here.

However, (H18.20) is not one instance of (H18.21):

1. there are simultaneously a `+kappa` root modulus `A` and a `-kappa` root modulus `D`;
2. the twist on the `A` side is `D^{-1} mod A`;
3. the twist on the `D` side is `A^{-1} mod D`;
4. both `A` and `D` move;
5. the private largest-prime condition is attached to `A` through `ell=LPF(AD)`;
6. the physical root is the product phase, not either factor separately.

Freezing `D` makes the `A`-side theorem look classical, but summing over moving `D` by Cauchy reintroduces the opposite side and loses the sought near-linear scale.  The same happens with the roles reversed.

Thus the Fouvry--Iwaniec root large sieve is an **adapter source**, not a theorem that can be cited directly for the t67 packet.

```text
FOUVRY_IWANIEC_QUADRATIC_ROOT_LARGE_SIEVE_RELEVANT=true
FOUVRY_IWANIEC_DIRECT_IMPORT_VALID=false
FI_DIRECT_IMPORT_FAILURE=moving_reciprocal_cross_twists_and_two_root_factors
```

---

## 7. DFI / Toth / Ngo Weyl-root equidistribution does not directly close the private pair

Duke--Friedlander--Iwaniec and later Toth/Ngo study Weyl sums of roots of a **fixed quadratic polynomial** as the modulus varies.  Those results provide deep cancellation unavailable from generic Farey spacing.

The t67 packet differs at the theorem interface:

- the global root condition is the oriented product of `X^2-kappa` and `X^2+kappa`;
- the factor allocation varies with `M`;
- the private largest prime is required to lie on the `+kappa` side;
- the analytic phase contains the mutually moving inverses in (H18.20).

Forgetting the orientation and using only `rho^4=kappa^2 mod M` is not legitimate, because it adds roots with the wrong canonical/cover allocation.  Conversely, treating one quadratic factor at a time leaves the other moving reciprocal twist.

```text
DFI_NGO_ROOT_WEYL_TECHNOLOGY_RELEVANT=true
DFI_NGO_DIRECT_IMPORT_VALID=false
```

---

## 8. Biquadratic ideal/root orientation: correct algebraic envelope, no ready large sieve

The four local orientations

\[
\pm\sqrt\kappa,
\qquad
\pm i\sqrt\kappa
\tag{H18.22}
\]

suggest the compositum

\[
K=\mathbf Q(i,\sqrt\kappa).
\tag{H18.23}
\]

as the natural algebraic bookkeeping field.  At odd good primes the t66 orientation is exactly the choice between the two quadratic factors of (H18.8), and the private canonical prime is a distinguished prime-ideal component on the `+kappa` side.

This does give a plausible ideal parameterisation of the root labels.  But the existing general large sieve over number fields controls additive/multiplicative characters or well-spaced algebraic residue data after a modulus/ideal family is specified.  It does not automatically produce the root-fraction estimate with the cross-reciprocal phase (H18.20).

In particular an ideal parameterisation alone does not remove the `Q^2` Farey barrier; one still needs a spacing/trace theorem adapted to the selected root ideals and their rational root fractions.

```text
BIQUADRATIC_IDEAL_ORIENTATION_PARAMETERIZATION_PLAUSIBLE=true
ALGEBRAIC_NUMBER_FIELD_LARGE_SIEVE_DIRECT_IMPORT_VALID=false
```

---

## 9. Recent modular-square-root bilinear technology is adjacent, not identical

Recent work on bilinear sums and additive energies of modular square roots gives additional evidence that nontrivial root-energy estimates can outperform generic spacing.  However the currently available statements concern different modulus geometries (notably prime or square-modulus variants) and do not contain the t67 combination

```text
composite M=A*D
opposite quadratic signs
mutually moving reciprocal twists
private largest-prime tag on A
```

as a theorem specialization.

```text
RECENT_MODULAR_SQRT_BILINEAR_TECHNOLOGY_RELEVANT=true
RECENT_MODULAR_SQRT_BILINEAR_DIRECT_IMPORT_VALID=false
```

---

## 10. Exact new theorem contract

The right analytic theorem is not a generic large sieve for all fractions and not a squareclass-character large sieve.

Define

```text
PrivateReciprocalCrossTwistOppositeSignRootLargeSieve (PRCTORLS)
```

as follows.

Fix `(U,epsilon,k,h)`, a squareclass kernel `kappa`, and a dyadic modulus band `M~Q`.  Let

\[
M=AD,
\qquad
A=\ell H,
\qquad
\ell=\operatorname{LPF}_{\rm odd}(M),
\qquad
2(M/\ell)<\ell,
\tag{H18.24}
\]

with

\[
\alpha^2\equiv+\kappa\pmod A,
\qquad
\beta^2\equiv-\kappa\pmod D,
\tag{H18.25}
\]

and retain only the t67 private cross-modulus part after same-`M`, same-`ell`, and nested pairs have been removed.

The desired FI-scale inequality is

\[
\boxed{
\sum_{(A,D,\alpha,\beta)\in\Omega_{\rm priv}(Q)}
\left|
\sum_{n\in I}a_n
 e_A(n\alpha\overline D_A)
 e_D(n\beta\overline A_D)
\right|^2
\ll
(Q+N)B^{o(1)}\sum_{n\in I}|a_n|^2.
}
\tag{H18.26}
\]

By (H18.20), this is equivalently the additive large sieve on the physical mixed root fractions `rho/M`, but with the full opposite-sign/private arithmetic retained.

A theorem of shape (H18.26), together with the root-line Fourier/dispersion adapter used by the live t-route, would remove the `Q^2` generic spacing loss without importing squareclass coefficient energy or `E4`.

At present (H18.26) is not proved by any theorem certified in Stage14.

```text
PRIVATE_RECIPROCAL_CROSS_TWIST_OPPOSITE_SIGN_ROOT_LARGE_SIEVE_PROVED=false
```

The user-facing receiver name remains

```text
PrivateCanonicalPrimeOppositeSignRootModulusLargeSieve
```

with PRCTORLS as its exact missing analytic core.

---

## 11. What tH18 proves and what it rules out

### Proved adapters / identities

- t67 no-double-charge boundary is preserved;
- every physical mixed root satisfies the fixed quartic envelope `rho^4=kappa^2 mod M`;
- root fractions are reduced;
- private cross determinant is nonzero and has only the common cofactor forced into it;
- private largest primes do not force improved determinant divisibility;
- generic additive large sieve gives `(Q^2+N)B^o(1)`;
- exact opposite-sign CRT reciprocal-phase factorisation (H18.20).

### Direct imports rejected

- pure pairwise spacing / ordinary additive large sieve at target scale;
- Fouvry--Iwaniec one-root-family theorem without a new cross-twist adapter;
- DFI/Toth/Ngo fixed-quadratic Weyl theorem without an orientation/cross-twist adapter;
- generic algebraic-number-field large sieve after merely naming the biquadratic field;
- squareclass pre-collapse or `E4` coefficient energy.

### Minimal analytic obstruction

```text
PrivateReciprocalCrossTwistOppositeSignRootLargeSieve
```

or an equivalent direct private-root dispersion theorem that gains one full modulus power over the generic `Q^2` large-sieve scale.

---

## 12. Literature compatibility notes

The external literature is used only to compare theorem hypotheses and scales.

- Fouvry--Iwaniec, *Gaussian primes*, Acta Arith. 79 (1997): source of the quadratic-root large-sieve phenomenon used in later formulations.
- Duke--Friedlander--Iwaniec, *Equidistribution of roots of a quadratic congruence to prime moduli*, Ann. of Math. 141 (1995): fixed-quadratic root Weyl sums.
- H. T. Ngo, *On roots of quadratic congruences*, Bull. London Math. Soc. 56 (2024): strengthened positive-discriminant root Weyl estimates and arithmetic-progression modulus distribution.
- Huxley, *The large sieve inequality for algebraic number fields* (1968): general algebraic-number-field large-sieve framework.
- Matthew Welsh, *Parameterizing roots of polynomial congruences* (2020 preprint): ideal parameterisation viewpoint for polynomial roots.
- Stephan Baier, 2026 modular-square-root bilinear series: recent additive-energy/bilinear estimates, adjacent but not a direct theorem for the t67 mixed modulus.

No external theorem is promoted here to a proof of (H18.26).

---

## Locked boundary

```text
STAGE14_TH18=COMPLETE_PRIVATE_CANONICAL_ROOT_MODULUS_LARGE_SIEVE_APPLICABILITY_AUDIT
MERGED_T67_IMPORTED=true
T67_RADIAL_COLLAPSE_REOPENED=false
T67_FIXED_M_REOPENED=false
T67_SAME_ELL_REOPENED=false
T67_NESTED_PAIR_REOPENED=false
GLOBAL_BIQUADRATIC_ROOT_ENVELOPE_PROVED=true
OPPOSITE_SIGN_ROOT_ORIENTATION_DROPPABLE=false
PRIVATE_ROOT_FRACTIONS_REDUCED=true
PRIVATE_CROSS_DETERMINANT_NONZERO=true
PRIVATE_CROSS_DETERMINANT_FORCED_GCD_EQUALS_COMMON_COFACTOR=true
PRIVATE_CANONICAL_PRIMES_FORCE_CROSS_DETERMINANT_DIVISIBILITY=false
PRIVATE_PRIME_FORCES_ONE_OVER_Q_SPACING=false
PRIVATE_CLOSE_ROOT_FRACTION_COUNTERMODEL_RECORDED=true
GENERIC_PRIVATE_ROOT_FRACTION_LARGE_SIEVE_PROVED=true
GENERIC_PRIVATE_ROOT_FRACTION_LARGE_SIEVE_SCALE=(Q^2+N)*B^o(1)
GENERIC_LARGE_SIEVE_CLOSES_PRIVATE_RECEIVER=false
OPPOSITE_SIGN_CRT_RECIPROCAL_PHASE_FACTORIZATION_PROVED=true
MOVING_CROSS_RECIPROCAL_TWISTS_PRESERVED=true
FOUVRY_IWANIEC_QUADRATIC_ROOT_LARGE_SIEVE_RELEVANT=true
FOUVRY_IWANIEC_DIRECT_IMPORT_VALID=false
DFI_NGO_ROOT_WEYL_TECHNOLOGY_RELEVANT=true
DFI_NGO_DIRECT_IMPORT_VALID=false
BIQUADRATIC_IDEAL_ORIENTATION_PARAMETERIZATION_PLAUSIBLE=true
ALGEBRAIC_NUMBER_FIELD_LARGE_SIEVE_DIRECT_IMPORT_VALID=false
RECENT_MODULAR_SQRT_BILINEAR_TECHNOLOGY_RELEVANT=true
RECENT_MODULAR_SQRT_BILINEAR_DIRECT_IMPORT_VALID=false
PRIVATE_RECIPROCAL_CROSS_TWIST_OPPOSITE_SIGN_ROOT_LARGE_SIEVE_PROVED=false
PRIVATE_CANONICAL_PRIME_OPPOSITE_SIGN_ROOT_MODULUS_LARGE_SIEVE_PROVED=false
SHARED_U_PRIVATE_CANONICAL_PRIME_ROOT_MODULUS_ENERGY_PROVED=false
E4_COEFFICIENT_ENERGY_USED=false
MINIMAL_REMAINING_OBSTRUCTION=PrivateReciprocalCrossTwistOppositeSignRootLargeSieve
T_ROUTE_BLOCKED_WAITING_FOR_TH18=false
NEXT=Stage14-t68 consume the exact CRT cross-twist identity and attack private root dispersion directly
```
