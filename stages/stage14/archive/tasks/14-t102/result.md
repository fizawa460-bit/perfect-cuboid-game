# Stage14-t102 — fixed-U prime mover density / energy lemma

## Status

`COMPLETE_FIXED_U_GENERIC_PRIME_MOVER_DENSITY_ENERGY_REDUCTION`

Consumes merged Stage14-t101, merged Stage14-Work-bhX20, merged Stage14-s7-61 as parallel context, and completed immutable Stage14-tH27. No H snapshot is reopened. No global/fixed-U saving is cross-promoted.

The whole-family theorem remains

```text
V(B) << B^(1/2+o(1)),
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

## 1. Restore the generic-prime average before single-prime pigeonholing

Let the surviving fixed-U antipodal quotient occupancy be

```text
f : {+-1}^r -> {0,1},
```

in a Boolean chart for the `r` generic split-prime orientation bits after the already-fixed antipodal gauge choice. As in t96, write

```text
I_p := Inf_p(f)
     = P_x[f(x) != f(x^p)]
```

for the normalized influence of the generic split-prime bit `p`.

Merged t95/t96 gives

```text
Var(f) = mu(1-mu)
       <= (1/4) sum_p I_p.
```

Any square-root-saturating packet surviving t95 has

```text
mu       = B^(-o(1)),
1-mu     = B^(-o(1)),
Var(f)   = B^(-o(1)).
```

The generic-prime count satisfies

```text
r = omega(delta_G) = B^o(1).
```

Therefore, for `r>0`, the normalized mean prime influence

```text
I_bar := (1/r) sum_p I_p
```

satisfies

```text
I_bar >= 4 Var(f)/r = B^(-o(1)).
```

This is stronger than merely selecting one influential bit: the normalized prime-action average itself has exponent-zero mass.

```text
NORMALIZED_GENERIC_PRIME_MEAN_INFLUENCE_EXPONENT_ZERO=true
```

If `r=0`, there is no generic orientation cube and hence no t96/t100 mover branch; the current receiver is vacuous on that packet.

## 2. Exponent-zero mover-prime support density

Define

```text
M = { p : I_p > 0 }.
```

Because `0 <= I_p <= 1`,

```text
sum_p I_p <= |M|.
```

Hence

```text
|M|/r >= I_bar >= 4 Var(f)/r = B^(-o(1)).
```

Thus every square-root-saturating fixed-U packet with a live generic cube has an exponent-zero density of mover-prime bits among its generic split-prime factors.

This does **not** mean a positive constant density, and it does not create a polynomial-length prime family: `r` itself is only `B^o(1)`.

```text
GENERIC_MOVER_PRIME_SUPPORT_DENSITY_EXPONENT_ZERO=true
POLYNOMIAL_LENGTH_PRIME_FAMILY_PROVED=false
```

## 3. Normalized mover energy

Define the prime mover energy

```text
E_move := (1/r) sum_p I_p^2.
```

By Jensen/Cauchy,

```text
E_move >= I_bar^2.
```

Consequently on every square-root-saturating live packet,

```text
E_move = B^(-o(1))
```

in the lower-bound/exponent-zero sense: it cannot be `B^{-delta+o(1)}` for any fixed `delta>0` along a saturating sequence.

This realizes the fixed-U side of the merged Work-bhX20 target

```text
PrimeMoverDensityOrEnergyLemma.
```

```text
FIXED_U_PRIME_MOVER_DENSITY_ENERGY_LEMMA_PROVED=true
NORMALIZED_MOVER_ENERGY_EXPONENT_ZERO=true
```

## 4. Boundary-class localization survives the prime average

For each generic prime `p`, merged t98 covers the physical symmetric difference by three broad elementary boundary classes:

```text
SIGN,
DIV,
PROJ.
```

Let `I_p^SIGN`, `I_p^DIV`, `I_p^PROJ` denote the normalized masses of the corresponding class unions. Then

```text
I_p <= I_p^SIGN + I_p^DIV + I_p^PROJ.
```

Summing over generic primes gives

```text
sum_p I_p
 <= sum_p I_p^SIGN
  + sum_p I_p^DIV
  + sum_p I_p^PROJ.
```

Therefore at least one class `C` satisfies

```text
(1/r) sum_p I_p^C >= I_bar/3 = B^(-o(1)).
```

Since each `I_p^C <= 1`, the support density of class-`C` mover primes is also `B^(-o(1))`.

This is a broad-class statement only. It does not identify one common modulus, one common sign cone, or one common projective class across different primes.

```text
ONE_BOUNDARY_CLASS_HAS_EXPONENT_ZERO_PRIME_AVERAGE=true
COMMON_ELEMENTARY_BOUNDARY_ACROSS_PRIMES_PROVED=false
```

## 5. Interaction with t101 principal/centered split

Merged t101 applies, for every frozen elementary mover boundary incidence `(p,E)`, the exact split

```text
1_E = rho_{p,E} + 1_E^circ,
E[1_E^circ]=0,
E[|1_E^circ|^2]=rho_{p,E}(1-rho_{p,E}).
```

The present prime-average lemma does not remove the principal densities `rho_{p,E}`. Instead it shows that the square-root obstruction cannot be represented by only a fixed-power sparse set of generic prime actions: after averaging over all generic prime bits, mover mass and mover energy remain exponent-zero.

Thus the remaining fixed-U obstruction is an arithmetic prime-boundary incidence problem:

```text
exponent-zero generic-prime mover density/energy
+
principal boundary densities
+
centered boundary discrepancies.
```

No independence between these pieces is asserted.

## 6. Why no new H is opened

Merged tH27 already shows that one frozen SIGN/DIV/PROJ boundary does not receive a uniform fixed-power saving from existing discrepancy technology. Stage14-t102 creates a prime average, but its length is only

```text
r = B^o(1),
```

and the boundary data may change with `p`. Hence this is not yet a standard Bombieri-Vinogradov, large-sieve, Hecke-family, or polynomial prime-density receiver.

A new H target would be premature until the varying mover incidences are compressed to a common arithmetic modulus/energy relation or a polynomial-scale prime/cofactor family.

```text
TH27_COMPLETE_CONSUMED=true
TH27_TARGET_REOPENED=false
TH27_REFINEMENT_REQUESTED=false
TH28_NEEDED=false
```

## 7. Frozen boundary

```text
STAGE14_T102=COMPLETE_FIXED_U_GENERIC_PRIME_MOVER_DENSITY_ENERGY_REDUCTION
MERGED_T101_CONSUMED=true
WORK_BHX20_PRIME_MOVER_TARGET_REALIZED_FIXED_U=true
NORMALIZED_GENERIC_PRIME_MEAN_INFLUENCE_EXPONENT_ZERO=true
GENERIC_MOVER_PRIME_SUPPORT_DENSITY_EXPONENT_ZERO=true
FIXED_U_PRIME_MOVER_DENSITY_ENERGY_LEMMA_PROVED=true
NORMALIZED_MOVER_ENERGY_EXPONENT_ZERO=true
ONE_BOUNDARY_CLASS_HAS_EXPONENT_ZERO_PRIME_AVERAGE=true
COMMON_ELEMENTARY_BOUNDARY_ACROSS_PRIMES_PROVED=false
POLYNOMIAL_LENGTH_PRIME_FAMILY_PROVED=false
TH27_COMPLETE_CONSUMED=true
TH27_TARGET_REOPENED=false
TH27_REFINEMENT_REQUESTED=false
TH28_NEEDED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
PREFERRED_RECEIVER=SharedUCanonicalLPFExponentZeroGenericPrimeMoverDensityEnergyPlusPrincipalCenteredBoundaryIncidence
NEXT=Stage14-t103
```
