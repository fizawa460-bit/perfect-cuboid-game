# Stage14-Work-bhX20 — single-prime mover/stabilizer taxonomy across global and fixed-U routes

## Status

`COMPLETE_SINGLE_PRIME_MOVER_STABILIZER_TAXONOMY_AND_NO_CROSS_PROMOTION`

Consumes merged `Stage14-Work-bgX19`, `Stage14-4dq`, `Stage14-s7-60`, `Stage14-t100`, and frozen `Stage14-tH27` on latest main. Unmerged descendants are not theorem sources.

The canonical whole-family theorem remains

```text
V(B) << B^(1/2+o(1)),
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

## 1. Global single-prime action

Merged s7-60 localizes any square-root-saturating zero-mode arithmetic uplift to one active split prime `ell` whose allocation bit changes the physical admissibility of the same charged-once six-block packet. With all other prime allocations frozen, the two states are tested by

```text
X=C_*ST,
Y=u_*RJ,
(X+Y)/2 = D^2,
(X-Y)/2 = A^2,
```

plus the retained physical side masks and only `B^o(1)` reciprocal completion multiplicity.

Call the prime a global stabilizer if the two allocation states have identical physical acceptance for every state in the frozen packet, and a global mover otherwise. Then any prime contributing nonzero local influence is necessarily a mover, and any square-root-saturating arithmetic uplift requires an exponent-zero mover influence.

```text
GLOBAL_SINGLE_PRIME_STABILIZER_MOVER_TAXONOMY_DEFINED=true
GLOBAL_STABILIZER_INFLUENCE_ZERO_BY_DEFINITION=true
GLOBAL_SQRT_REQUIRES_EXPONENT_ZERO_MOVER_INFLUENCE=true
```

This is a charged-once relabeling of the merged s7-60 single-prime influence, not a second source of saving.

## 2. Fixed-U single-prime action

Merged t100 proves the corresponding fixed-U stabilizer/mover reduction explicitly. A generic Gaussian split-prime orientation switch acts by the matrices

```text
M_+=[[A,-B],[B,A]],
M_-=[[A,B],[-B,A]],
```

and the surviving elementary boundary is one of

```text
SIGN: indefinite quadratic-cone mover,
DIV : nontrivial fixed-divisor residue mover,
PROJ: nontrivial endpoint projective mover.
```

Stabilizer actions give exactly zero influence.

```text
FIXED_U_STABILIZER_MOVER_TAXONOMY_PROVED=true
FIXED_U_STABILIZER_INFLUENCE_ZERO_PROVED=true
FIXED_U_SQRT_REQUIRES_ELEMENTARY_BOUNDARY_MOVER=true
```

## 3. Common prime-action language

Both routes now admit the same abstract two-state action diagram:

```text
frozen packet + one prime p
        |
      action_p
      /      \
 state 0    state 1
      \      /
 physical acceptance
```

with

```text
stabilizer : acceptance is invariant under action_p,
mover      : acceptance changes on a nonzero subset,
influence  : normalized mass of the symmetric difference.
```

Hence

```text
COMMON_SINGLE_PRIME_ACTION_LANGUAGE_PROVED=true
COMMON_STABILIZER_MOVER_DICHOTOMY_PROVED=true
COMMON_INFLUENCE_AS_SYMMETRIC_DIFFERENCE_LANGUAGE_PROVED=true
```

This strictly sharpens bgX19's generic physical-boundary language.

## 4. Why no arithmetic adapter is proved

The global and fixed-U actions are still different arithmetic maps.

Global:

```text
allocation of one rational split prime between disjoint divisor cells
-> changed products X,Y
-> simultaneous complementary-square tests
-> retained balanced/range/chart masks.
```

Fixed-U:

```text
Gaussian conjugation of one p-primary factor
-> explicit linear forms L_+,L_-
-> SIGN/DIV/PROJ elementary boundary tests.
```

No finite-fiber map identifies the global two-square mover event with one t100 SIGN/DIV/PROJ mover event. In particular the global square tests are quadratic conditions on products whose coefficients depend on the frozen complementary allocation; t100's elementary boundaries live after fixed-U and fixed norm conditioning.

Therefore

```text
GLOBAL_MOVER_TO_FIXED_U_ELEMENTARY_MOVER_MAP_PROVED=false
FIXED_U_MOVER_TO_GLOBAL_TWO_SQUARE_MOVER_MAP_PROVED=false
COMMON_ARITHMETIC_ADAPTER_PROVED=false
SAVING_CROSS_PROMOTABLE=false
```

## 5. tH27 use

Merged tH27 is consumed only as the immutable external-theorem audit for one fixed-U elementary boundary. It is not promoted to the global six-block prime-allocation packet.

```text
TH27_MERGED_CONSUMED_AS_FIXED_U_AUDIT=true
TH27_GLOBAL_CROSS_PROMOTION_PROVED=false
TH28_NEEDED=false
```

No new H is required by this integrated stage. The next missing object is internal and explicit.

## 6. Next integrated receiver

The smallest common unresolved problem is no longer “find a boundary”. It is to measure how often an active prime acts as a mover after all other coordinates are frozen.

Define the target:

```text
Prime Mover Density / Energy Lemma
```

with two route-specific realizations:

```text
GLOBAL:
  bound the density/energy of primes whose allocation flip changes the
  simultaneous complementary-square physical acceptance;

FIXED-U:
  bound the density/energy of generic primes whose conjugation acts as a
  SIGN/DIV/PROJ mover under all retained canonical-LPF masks.
```

A common theorem would require an explicit common modulus/energy representation before any saving can be cross-promoted.

## Boundary

```text
STAGE14_WORK_BHX20=COMPLETE_SINGLE_PRIME_MOVER_STABILIZER_TAXONOMY_AND_NO_CROSS_PROMOTION
STAGE14_WORK_TOOLBOX_X=RUN
TOOLBOX_COMPONENT_COMPLETE=true
X_COMPONENT_COMPLETE=true
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
GLOBAL_SINGLE_PRIME_STABILIZER_MOVER_TAXONOMY_DEFINED=true
GLOBAL_STABILIZER_INFLUENCE_ZERO_BY_DEFINITION=true
GLOBAL_SQRT_REQUIRES_EXPONENT_ZERO_MOVER_INFLUENCE=true
FIXED_U_STABILIZER_MOVER_TAXONOMY_PROVED=true
FIXED_U_STABILIZER_INFLUENCE_ZERO_PROVED=true
FIXED_U_SQRT_REQUIRES_ELEMENTARY_BOUNDARY_MOVER=true
COMMON_SINGLE_PRIME_ACTION_LANGUAGE_PROVED=true
COMMON_STABILIZER_MOVER_DICHOTOMY_PROVED=true
COMMON_INFLUENCE_AS_SYMMETRIC_DIFFERENCE_LANGUAGE_PROVED=true
GLOBAL_MOVER_TO_FIXED_U_ELEMENTARY_MOVER_MAP_PROVED=false
FIXED_U_MOVER_TO_GLOBAL_TWO_SQUARE_MOVER_MAP_PROVED=false
COMMON_ARITHMETIC_ADAPTER_PROVED=false
SAVING_CROSS_PROMOTABLE=false
TH27_MERGED_CONSUMED_AS_FIXED_U_AUDIT=true
TH27_GLOBAL_CROSS_PROMOTION_PROVED=false
MAINLINE_H_NEEDED=false
S_ROUTE_H_NEEDED=false
FIXED_U_H_NEEDED=false
TH28_NEEDED=false
NEXT_REVISIT_CONDITION=4ds_and_s7-62_and_t102_or_material_mover_density_trigger
NEXT_INTERNAL_TARGET=PrimeMoverDensityOrEnergyLemma
```
