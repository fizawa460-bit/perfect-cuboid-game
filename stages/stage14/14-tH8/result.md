# Stage14-tH8 — external-auxiliary Gaussian-spin trilinear adapter

## Purpose

Stage14-tH7 closed and PARKed the first roadworks cycle `tH1--tH6`.  The live `t` route then produced a genuinely new infrastructure demand.

Merged Stage14-t39 proved that the critical-strip square detector cannot be inserted directly into the Friedlander--Iwaniec two-variable Gaussian Dirichlet-symbol bilinear theorem:

- using the natural Stage14 Gaussian coefficient as the FI modulus makes the `Psi/Phi` character constant or zero;
- keeping the external square-sieve prime preserves a nontrivial detector, but the trace is nonmultiplicative in the moving Gaussian prime;
- the external auxiliary prime therefore survives as an independent third variable.

The stable analytic object is consequently

\[
\boxed{
\mathcal T
 =
 \sum_{\varpi\in\mathcal L}
 \sum_{x\in\mathcal X}
 a_{\varpi}d_x
 \chi_{N\varpi}(P_x),
}
\tag{H8.1}
\]

where

```text
varpi  = primary Gaussian prime above the external split auxiliary prime,
lambda_varpi = N(varpi),
x      = one combined physical packet, usually (pi,gamma),
P_x    = the integer Stage14 Psi/Phi polynomial value,
a_varpi, d_x = arbitrary bounded/weighted coefficients.
```

Stage14-tH8 does **not** attempt to pretend that (H8.1) is already an FI bilinear form.  It builds the exact adapter needed before any FI or quadratic-Hecke theorem may legally be called:

1. a canonical trilinear packet record;
2. the two exact one-Cauchy dispersion identities;
3. diagonal/off-diagonal kernel separation;
4. explicit FI-ready and quadratic-Hecke-ready certificates;
5. an exponent ledger for any block which eventually earns an FI certificate.

No future `t40` result is required.

---

## 1. Imported stable boundary from t39

The following merged t39 facts are treated as demand specifications:

```text
FI_DIRICHLET_SYMBOL_DEFINITION_MATCHED=true
FI_PROPOSITION_21_3_BALANCED_POWER_SAVING_AVAILABLE=true
NATURAL_MODULUS_PSI_TRACE=CONSTANT_OR_ZERO
NATURAL_MODULUS_PHI_TRACE=CONSTANT_OR_ZERO
EXTERNAL_AUXILIARY_PSI_TRACE_MULTIPLICATIVE=false
EXTERNAL_AUXILIARY_PHI_TRACE_MULTIPLICATIVE=false
AUXILIARY_ROOT_ROTATION_PRESERVES_SEPARATED_COEFFICIENTS=false
DIRECT_TWO_VARIABLE_FI_TRANSFER_VALID=false
EXTERNAL_AUXILIARY_THIRD_VARIABLE_ESSENTIAL=true
```

These facts forbid a raw two-variable shortcut.  They do not forbid FI technology after a legitimate dispersion/differencing step exposes a new cross-kernel.

Thus the tH8 rule is:

> **never call an FI/Hecke theorem on the raw trace; call it only on a cross-kernel carrying an explicit readiness certificate.**

---

## 2. Canonical external-auxiliary packet

Collapse the physical pair `(pi,gamma)` into one packet label `x` without discarding either component internally.  The canonical roadworks record is

```text
ExternalAuxiliarySpinPacket:
  auxiliary:
    varpi
    lambda = N(varpi)
    primary = true
    split = true

  physical:
    canonical_prime_pi
    descended_packet_gamma
    branch in {visible_same, visible_opposite, invisible}

  detector:
    P_x
    kind in {Psi_product, Phi_product, other_exact_factorization}
    good_prime_mask

  coefficients:
    a_varpi
    d_x

  provenance:
    t38_factorization
    t39_external_modulus_boundary
```

The packet intentionally retains the external modulus and physical packet as different variables.

```text
EXTERNAL_AUXILIARY_AND_PHYSICAL_PACKET_IDENTIFIED=false
TRILINEAR_VARIABLE_SEPARATION_PRESERVED=true
```

---

## 3. Exact auxiliary-family dispersion identity

Write

\[
F_{\varpi}
 =
 \sum_{x\in\mathcal X}d_x\chi_{N\varpi}(P_x).
\]

Then

\[
\mathcal T=\sum_{\varpi}a_{\varpi}F_{\varpi}.
\]

Cauchy in the external auxiliary variable gives

\[
\boxed{
|\mathcal T|^2
\le
\left(\sum_{\varpi}|a_{\varpi}|^2\right)
\sum_{\varpi}|F_{\varpi}|^2.
}
\tag{H8.2}
\]

Because each quadratic character is real-valued in `{0,+1,-1}`,

\[
\begin{aligned}
\sum_{\varpi}|F_{\varpi}|^2
&=
\sum_{x,y}d_x\overline{d_y}
\sum_{\varpi}
\chi_{N\varpi}(P_x)\chi_{N\varpi}(P_y)\\
&=
\sum_{x,y}d_x\overline{d_y}
K_{\mathcal L}(x,y),
\end{aligned}
\]

where

\[
\boxed{
K_{\mathcal L}(x,y)
=
\sum_{\varpi\in\mathcal L}
\chi_{N\varpi}(P_xP_y).
}
\tag{H8.3}
\]

The equality remains exact on bad states because `0*chi=0` and the Legendre/Jacobi symbol is multiplicative including zero.

This is the first legal post-dispersion object.

### Diagonal

For `x=y`,

\[
\boxed{
K_{\mathcal L}(x,x)
=
\#\{\varpi\in\mathcal L:N\varpi\nmid P_x\}.
}
\tag{H8.4}
\]

Thus the diagonal is explicit and nonnegative.

### Off-diagonal

For `x\ne y`, the cancellation problem is

\[
\boxed{
K_{\mathcal L}^{\rm off}(x,y)
=
\sum_{\varpi}
\chi_{N\varpi}(P_xP_y).
}
\tag{H8.5}
\]

No FI or Hecke interpretation of (H8.5) is asserted merely from its appearance.

---

## 4. Exact physical-packet dispersion identity

There is a second legal Cauchy direction.  Put

\[
G_x
=
\sum_{\varpi\in\mathcal L}
 a_{\varpi}\chi_{N\varpi}(P_x).
\]

Then

\[
\boxed{
|\mathcal T|^2
\le
\left(\sum_x|d_x|^2\right)
\sum_x|G_x|^2.
}
\tag{H8.6}
\]

Expanding the second moment gives

\[
\sum_x|G_x|^2
=
\sum_{\varpi,\omega}
 a_{\varpi}\overline{a_\omega}
H_{\mathcal X}(\varpi,\omega),
\]

with

\[
\boxed{
H_{\mathcal X}(\varpi,\omega)
=
\sum_{x\in\mathcal X}
\chi_{N\varpi}(P_x)
\chi_{N\omega}(P_x).
}
\tag{H8.7}
\]

For `varpi=omega`,

\[
H_{\mathcal X}(\varpi,\varpi)
=
\#\{x:N\varpi\nmid P_x\}.
\tag{H8.8}
\]

For `varpi\ne omega`, (H8.7) is a genuine two-modulus cross-correlation.  Again, it must be certified before importing a bilinear theorem.

---

## 5. Why both Cauchy directions are retained

The two routes solve different structural problems.

### Route A — auxiliary-family dispersion

```text
sum_varpi sum_x
  -> Cauchy in varpi
  -> one moving modulus varpi
  -> pair of physical packets (x,y)
  -> K_L(x,y)=sum_varpi chi_{Nvarpi}(P_x P_y)
```

This is naturally suited to a **quadratic-character family in the external modulus** if the numerator family `P_xP_y` can be encoded as a genuine Gaussian/ray-class numerator independent of `varpi`.

### Route B — physical-packet dispersion

```text
sum_varpi sum_x
  -> Cauchy in x
  -> pair of external moduli (varpi,omega)
  -> one physical packet x
  -> H_X(varpi,omega)
```

This may be useful if the product of the two external characters can be converted to a single squarefree/ray-class modulus or if reciprocity exposes a Gaussian symbol between `varpi` and `omega`.

Neither route is declared universally superior.  tH8 freezes both so the live proof does not have to redo the algebra.

---

## 6. FI-ready certificate

A post-dispersion block may use the Friedlander--Iwaniec Gaussian Dirichlet-symbol bilinear theorem only if it supplies a record

```text
FIDirichletSymbolCertificate:
  denominator_variable = w
  numerator_variable   = z

  w_primary_primitive = proved
  z_primary_primitive_or_legal_extension = proved
  coprimality_mask = explicit

  exact_trace_identity:
    trace(w,z) = kappa_w * kappa_z * (z/w)

  separation:
    z_independent_of_w = true
    kappa_w_depends_only_on_w = true
    kappa_z_depends_only_on_z = true
    coefficients_factor_as_alpha_w_beta_z = true

  dyadic_norm_ranges:
    N(w) ~ M
    N(z) ~ N

  theorem_hypotheses_checked = true
```

The crucial condition is **separation**.  A `w`-dependent rotation of `z` is not a certificate, because it turns `beta_z` into a coupled coefficient.

By merged t39,

```text
RAW_STAGE14_EXTERNAL_TRACE_FI_READY=false
RAW_STAGE14_NATURAL_SELF_TRACE_FI_USEFUL=false
```

The first is nonmultiplicative; the second is constant/zero.

---

## 7. Quadratic-Hecke-ready certificate

FI is not the only legal receiver.  A post-dispersion block may instead expose a quadratic Hecke/ray-class family.

The minimum roadworks certificate is

```text
QuadraticHeckeFamilyCertificate:
  character_family = eta_w
  denominator_or_conductor_variable = w
  numerator_element_or_ideal = Z

  Z_independent_of_w = true
  conductor_formula = explicit
  primitive/imprimitive_reduction = explicit
  bad_prime_mask = explicit
  coefficient_separation = true
  family_second_moment_theorem_hypotheses_checked = true
```

This definition is intentionally theorem-agnostic.  It does not claim that either (H8.5) or (H8.7) already satisfies it.

```text
AUXILIARY_DISPERSION_QUADRATIC_HECKE_CERTIFICATE_PROVED=false
PHYSICAL_DISPERSION_QUADRATIC_HECKE_CERTIFICATE_PROVED=false
```

---

## 8. Formal FI Type-I/II exponent transfer

Merged t39 records the FI Section 21 estimate

\[
Q(M,N)
\ll
(M+N)^{1/12}(MN)^{11/12+\varepsilon}.
\tag{H8.9}
\]

Relative to the trivial `MN`, and writing

\[
M=B^\mu,\qquad N=B^\nu,
\]

the polynomial exponent is

\[
\frac{\max(\mu,\nu)}{12}
+\frac{11(\mu+\nu)}{12}
=
\mu+\nu-\frac{\min(\mu,\nu)}{12}.
\]

Hence any block carrying a valid FI certificate has the formal saving

\[
\boxed{
\delta_{\rm FI}
=
\frac{\min(\mu,\nu)}{12}.
}
\tag{H8.10}
\]

Equivalently,

\[
Q(M,N)
\ll
MN\,\min(M,N)^{-1/12+\varepsilon}
\]

up to a harmless absolute factor from `M+N<=2 max(M,N)`.

In the balanced range `M=N=X`, this is the frozen t39 gain

\[
\boxed{X^{-1/12+\varepsilon}}.
\tag{H8.11}
\]

This ledger is **conditional on the certificate**.  tH8 does not assign (H8.10) to the raw Stage14 trilinear form.

---

## 9. Interaction with the first tH road cycle

If a cross-kernel earns an FI or quadratic-Hecke certificate, the old tH cycle becomes reusable immediately:

```text
new cross-kernel theorem
  -> tH4 weighted L2-safe transfer
  -> tH5 exact Gaussian-pair coefficient energy
  -> tH6 exponent receiver
```

The tH7 stress gate already proved that these roads cost only `B^o(1)` under their declared hypotheses.

Thus cycle 2 does not duplicate tH1--tH6.  It only builds the missing bridge from the trilinear external-modulus object to a legal analytic family.

---

## 10. Canonical dispersion-kernel record

Later support or live stages should use

```text
ExternalAuxiliaryDispersionKernel:
  source_packet: ExternalAuxiliarySpinPacket

  cauchy_direction:
    AUXILIARY_FAMILY | PHYSICAL_PACKET

  source_l2_budget:
    auxiliary_energy = sum |a_varpi|^2
    physical_energy  = sum |d_x|^2

  diagonal:
    exact_good_state_count

  off_diagonal:
    kernel_formula
    factorization_data

  readiness:
    fi_certificate = null | FIDirichletSymbolCertificate
    quadratic_hecke_certificate = null | QuadraticHeckeFamilyCertificate

  forbidden_shortcuts:
    raw_external_trace_to_FI = false
    natural_self_modulus_as_nontrivial_detector = false
    modulus_dependent_rotation_with_separated_coefficients = false
```

This is the stable handoff object for tH9 or any later live-t consumer.

---

## 11. Deterministic audit

The dedicated audit uses exact integer arithmetic on deterministic `Psi/Phi` packets.

Frozen sample:

```text
external split primes                  5
physical Psi/Phi packets              55
local character evaluations          275
nonzero evaluations                   267
zero/bad-prime evaluations              8
Legendre product checks             15125
```

With deterministic integer coefficient sequences it obtains

```text
T direct                                27
|T|^2                                  729

auxiliary coefficient L2               55
Route-A second moment                 2845
Route-A Cauchy RHS                  156475
Route-A cross expansion               2845
Route-A diagonal contribution         1959
Route-A off-diagonal contribution      886

physical coefficient L2               404
Route-B second moment                 2485
Route-B Cauchy RHS                 1003940
Route-B cross expansion               2485
Route-B diagonal contribution         2947
Route-B off-diagonal contribution     -462
```

The negative Route-B off-diagonal contribution is allowed and is a useful diagnostic: the adapter preserves signed cross-correlation rather than replacing it by a positive collision count.

The audit also checks 36 exact rational exponent pairs `(mu,nu)` and verifies

\[
(\mu+\nu)-
\left[
\frac{\max(\mu,\nu)}{12}
+\frac{11(\mu+\nu)}{12}
\right]
=
\frac{\min(\mu,\nu)}{12}.
\]

---

## 12. What tH8 closes and what it does not

### Closed

- canonical representation of the external-auxiliary trilinear object;
- exact Cauchy/dispersion identities in both legal directions;
- diagonal/off-diagonal decomposition;
- FI readiness contract;
- quadratic-Hecke readiness contract;
- formal FI saving ledger for certified blocks;
- direct reuse interface into tH4--tH6.

### Not closed

- conversion of the actual Stage14 off-diagonal kernel to `(z/w)`;
- quadratic-Hecke interpretation of the actual off-diagonal kernel;
- a trilinear power saving;
- critical-strip power saving;
- `A_{1,1}` power saving or `T=o(sqrt(B))`.

The next independent support problem is therefore no longer architectural.  It is algebraic:

> factor the Route-A and Route-B off-diagonal `Psi/Phi` kernels and search for exact cross-ratio / reciprocity / Gaussian-symbol identities which can satisfy one of the certificates above.

That can proceed without waiting for Stage14-t40.

---

## Boundary

```text
STAGE14_TH8=COMPLETE_EXTERNAL_AUXILIARY_GAUSSIAN_SPIN_DISPERSION_ADAPTER
TH_REQUIRES_FUTURE_T_RESULT=false
T39_EXTERNAL_AUXILIARY_TRILINEAR_BOUNDARY_IMPORTED=true
EXTERNAL_AUXILIARY_SPIN_PACKET_STANDARDIZED=true
AUXILIARY_FAMILY_CAUCHY_DISPERSION_IDENTITY_PROVED=true
PHYSICAL_PACKET_CAUCHY_DISPERSION_IDENTITY_PROVED=true
DISPERSION_DIAGONALS_EXPLICIT=true
FI_DIRICHLET_SYMBOL_CERTIFICATE_DEFINED=true
QUADRATIC_HECKE_FAMILY_CERTIFICATE_DEFINED=true
RAW_STAGE14_EXTERNAL_TRACE_FI_READY=false
RAW_STAGE14_NATURAL_SELF_TRACE_FI_USEFUL=false
CERTIFIED_FI_BLOCK_SAVING=min(mu,nu)/12
AUXILIARY_DISPERSION_FI_CERTIFICATE_PROVED=false
PHYSICAL_DISPERSION_FI_CERTIFICATE_PROVED=false
AUXILIARY_DISPERSION_QUADRATIC_HECKE_CERTIFICATE_PROVED=false
PHYSICAL_DISPERSION_QUADRATIC_HECKE_CERTIFICATE_PROVED=false
CRITICAL_SQRT_ELL_STRIP_POWER_SAVING_PROVED=false
A_11_POWER_SAVING_PROVED=false
T_O_SQRT_B_PROVED=false
PERFECT_CUBOID_NONEXISTENCE_PROVED=false
NEXT=Stage14-tH9 build an exact off-diagonal Psi/Phi factorization and cross-ratio atlas for both dispersion kernels, testing FI/Hecke readiness without waiting for t40
```
