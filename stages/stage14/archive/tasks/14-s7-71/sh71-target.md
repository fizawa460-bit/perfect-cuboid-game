# Stage14-sH71 immutable target — canonical-allocation conditional primitive Gaussian root density

This file formalizes, without changing, the theorem contract already frozen in merged `Stage14-s7-71/result.md`. The s-batch omitted a standalone target file; the user has explicitly dispatched `Stage14-sH71` with requested object `CanonicalAllocationConditionalPrimitiveGaussianRootDensity`. From this commit onward this target is immutable under `stages/stage14/H-PROTOCOL.md`.

```text
H_STAGE=Stage14-sH71
AUDITED_THROUGH=Stage14-s7-71
SOURCE_SNAPSHOT_SHA=76bc8a4e59d8d220c58552e42dafef7d12ef55a3
REQUESTED_OBJECT=CanonicalAllocationConditionalPrimitiveGaussianRootDensity
TARGET_FROZEN=true
H_SOURCE_SNAPSHOT_FROZEN=true
RUNNING_SH71_MAY_CHASE_LATER_S_STAGES=false
```

## Frozen background and quantifier order

Let `Omega_can(B)` be the canonical allocation-bearing primitive-slope family from merged s7-68/s7-71. The height scale is

```text
H=B^(1/4+o(1)).
```

Freeze all packet data already fixed before s7-71: heavy Gaussian mover/root/chart, dyadic/range/angular cell, canonical balanced integer/Gaussian allocation witness, denominator/tag/orientation data, squarefree/coprime allocation masks and every charged-once finite-fiber decoration.

For each

```text
omega in Omega_can(B)
```

there is a charged-once set

```text
R(omega)
```

of `B^o(1)` primitive opposite-reciprocal candidates

```text
(C0,X0,Y0)
```

satisfying

```text
gcd(X0,Y0)=1,
gcd(C0,X0*Y0)=1,
```

with every odd prime of `C0` already Gaussian split and the local square root of `-1` / Gaussian orientation frozen by the physical packet.

Define

```text
A_root(omega)=1
```

iff at least one charged-once candidate in `R(omega)` satisfies

```text
C0 | X0^2+Y0^2.
```

Equivalently, after the frozen local root orientation is assembled,

```text
X0 == i_C*Y0 (mod C0),
i_C^2 == -1 (mod C0),
```

up to already charged `B^o(1)` two-primary/unit decorations.

## Exact audit question

Determine whether existing literature proves, uniformly over every frozen physical packet,

```text
# {omega in Omega_can(B): A_root(omega)=1}
  << |Omega_can(B)| * B^(-delta+o(1))
```

for some fixed `delta>0`, or an equivalent incidence/dispersion estimate implying that bound.

The theorem must retain the actual correlation among

```text
C0,
(X0,Y0),
canonical allocation witness,
primitive slope,
physical range/chart/angular masks,
```

and the charged-once existential `B^o(1)` candidate fiber. It is not legal to replace `Omega_can(B)` by an independent box, average over unrelated moduli, recharge the Gaussian splitting/root condition, or count the same `C0` root line as a second independent spacing modulus.

## Candidate theorem technologies

Audit at least:

```text
Duke-Friedlander-Iwaniec type equidistribution of roots of quadratic congruences,
large sieve for roots of -1 / quadratic congruences,
Gaussian/Kloosterman or Salié-root dispersion,
bilinear modular-square-root estimates,
divisor-correlated norm-form sieve,
Gaussian prime / Hecke equidistribution where relevant.
```

A theorem controlling only an unweighted modulus average or an independent coefficient sequence is advisory unless an exact mask-preserving adapter to the frozen conditional family is proved.

## Do not reopen

```text
FIRST_RECIPROCAL_EQUATION_TAUTOLOGICAL_AFTER_CANONICAL_ALLOCATION=true
POST_COLUMN_REVERSE_COMPLETION_INDEPENDENT_POLYNOMIAL_SELECTOR=false
SECOND_RECIPROCAL_ROOT_LINE_MODULUS_IS_C0=true
INDEPENDENT_SECOND_GROWING_MODULUS_PRODUCED=false
ROOT_LINE_DOUBLE_CHARGE_ALLOWED=false
SECOND_RECIPROCAL_DIVISOR_SWITCH_FIBER=Bo1
FRESH_DIVISOR_SWITCH_POWER_SAVING_PROVED=false
LOCAL_GAUSSIAN_SPLITTING_RECHARGE_ALLOWED=false
```

## Required verdict fields

```text
STAGE14_SH71=COMPLETE_...
S7_71_SNAPSHOT_RETAINED=true
DIRECT_GAUSSIAN_ROOT_EQUIDISTRIBUTION_THEOREM_APPLICABLE=true|false
ROOT_LARGE_SIEVE_DIRECTLY_APPLICABLE=true|false
BILINEAR_ROOT_DISPERSION_DIRECTLY_APPLICABLE=true|false
DIVISOR_CORRELATED_NORM_FORM_SIEVE_DIRECTLY_APPLICABLE=true|false
CANONICAL_BACKGROUND_PSEUDORANDOMNESS_ADAPTER_PROVED=true|false
FULL_PHYSICAL_MASKS_RETAINED=true|false
UNIFORM_FIXED_POWER_CONDITIONAL_DENSITY_SAVING_PROVED=true|false
CERTIFIED_CONDITIONAL_DENSITY_SAVING_EXPONENT=...
WHOLE_FAMILY_CROSS_PROMOTION_PROVED=true|false
STRICT_SUBSQRT_POWER_SAVING_PROVED=true|false
MINIMAL_REMAINING_OBSTRUCTION=...
PREFERRED_NEXT_INTERNAL_REDUCTION=...
NEXT_H_NEEDED=true|false
```
