# Stage14-s7-64 — primitive rational-slope contraction and physical acceptance predicate

## Status

`COMPLETE_PRIMITIVE_RATIONAL_SLOPE_CONTRACTION_AND_PHYSICAL_ACCEPTANCE_PREDICATE`

Consumes only merged sources: `Stage14-s7-63`, `Stage14-Work-bjX22`, `Stage14-4dw`, `Stage14-4dx`, `Stage14-s7-46`, `Stage14-s7-47`, and latest main through merged `Stage14-q12 / t104`. No fixed-U theorem or q12 literature result is cross-promoted as a saving.

The canonical whole-family theorem remains

```text
V(B) << B^(1/2+o(1)),
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2,
SQRT_B_UPPER_BOUND_PROVED=true,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

Merged 4dx already transports the fixed-prime/fixed-root survivor to projective slope/scale coordinates. Stage14-s7-64 consumes that transport and adds three s-specific contractions:

1. after the primitive-direction reduction, the apparent scale coordinate is not an independent polynomial coordinate;
2. the active six-block source/target chart has only `B^o(1)` labels and one chart may be frozen;
3. balanced allocation plus reciprocal completion reduces to one Boolean existence predicate on primitive rational slopes, with only `B^o(1)` witness multiplicity.

## 1. Primitive rational slope absorbs the apparent scale coordinate

Write the complementary factors as

```text
r = g a,
s = g b,
gcd(a,b)=1,
0<a<b.
```

Merged s7-63 gives

```text
g=B^o(1),
```

and merged Work-bjX22 gives `B^(1/2-o(1))` distinct primitive directions on any square-root-saturating fixed-prime/fixed-root survivor.

Define the reduced rational slope

```text
u=a/b.
```

For reduced `u`, the positive primitive pair `(a,b)` is unique. Thus the merged 4dx coordinates

```text
projective slope t=r/s,
scale q=s
```

are not two independent arithmetic coordinates once the primitive-direction theorem is imposed: the denominator `b` is part of the height of the reduced slope itself, while the only remaining scale-copy factor is `g=B^o(1)`.

```text
PRIMITIVE_RATIONAL_SLOPE_DETERMINES_PRIMITIVE_PAIR=true
RESIDUAL_COMMON_SCALE_MULTIPLICITY=Bo1
INDEPENDENT_POLYNOMIAL_SCALE_AFTER_PRIMITIVE_REDUCTION=false
```

This is a coordinate contraction, not a power saving.

## 2. Exact slope formulas from merged 4dx

The complementary-square variables satisfy

```text
r=D-A,
s=D+A,
D=g(a+b)/2,
A=g(b-a)/2.
```

For the fixed heavy Gaussian mover prime `ell_*`, merged 4dw/4dx give

```text
r^2+s^2=2 ell_* x,
rs=y.
```

Hence

```text
x = g^2(a^2+b^2)/(2 ell_*),
y = g^2ab,

x/y = (u+u^(-1))/(2 ell_*),
A/D = (1-u)/(1+u).
```

Therefore the merged 4dx norm-ratio, angle, balanced/interior and range transport may be read directly as conditions on the reduced primitive slope and its height, with only `B^o(1)` ambiguity from `g`.

```text
MERGED_4DX_PROJECTIVE_SLOPE_TRANSPORT_IMPORTED=true
NORM_RATIO_MASKS_TRANSPORT_TO_PRIMITIVE_SLOPE=true
COMPLEMENTARY_ANGLE_MASKS_TRANSPORT_TO_PRIMITIVE_SLOPE=true
ABSOLUTE_SCALE_ONLY_HAS_Bo1_EXTRA_MULTIPLICITY=true
```

## 3. Fixed root line remains full exponent

Merged Work-bjX22 freezes one Gaussian root orientation. On the primitive pair this is

```text
a == epsilon_* i_* b (mod ell_*),
i_*^2 == -1 (mod ell_*),
ell_*=B^o(1).
```

Merged 4dx already proves that this fixed projective residue line gives no fresh fixed-power saving.

The primitive height is

```text
H=max(a,b)=B^(1/4+o(1)).
```

A fixed positive-width slope interval together with one fixed root line modulo `ell_*` is compatible with

```text
H^2/(ell_* log H)=B^(1/2-o(1))
```

primitive pairs: take prime denominators `b~H`; the numerator interval contains `H/ell_*` candidates in the required residue class, and at most one candidate is divisible by the prime denominator.

Thus the archimedean windows and the already-frozen root congruence cannot by themselves break square root.

```text
FIXED_WIDTH_SLOPE_ROOT_LINE_AMBIENT_EXPONENT=1/2
ARCHIMEDEAN_SLOPE_WINDOW_ALONE_GIVES_FIXED_POWER_SAVING=false
PRIMITIVE_ROOT_LINE_ALONE_GIVES_FIXED_POWER_SAVING=false
```

## 4. Freeze one atomic mover chart

The six separated atomic norm blocks are

```text
PLUS:  C_*, S, T,
MINUS: u_*, R, J.
```

For one active split-prime allocation flip, the core source/target placement is one of at most

```text
3*3=9
```

plus/minus atomic placement labels. State orientation and endpoint/2-primary decorations enlarge this only to a `B^o(1)` chart dictionary.

Merged Work-bjX22 proves the common finite-label freezing principle. Consequently one complete atomic mover-chart label may be frozen on a square-root-saturating subsequence without fixed-power loss.

```text
ATOMIC_MOVER_CORE_CHART_LABEL_COUNT_LE_9=true
FULL_MOVER_CHART_DICTIONARY_SIZE=Bo1
ONE_ATOMIC_MOVER_CHART_CAN_BE_FROZEN=true
CHART_LABEL_IS_NOT_INDEPENDENT_FIXED_POWER_SUPPORT=true
```

This removes charged-once chart identification as a separate polynomial coordinate. It does not supply a saving.

## 5. Balanced allocation plus reciprocal completion is one existence predicate

After fixing

```text
ell_*, root orientation, atomic chart, primitive slope (a:b),
```

and one allowed `g=B^o(1)`, the complementary state values `x,y` are fixed by Section 2.

In the frozen chart the corresponding plus/minus cofactor products are therefore fixed up to the already-frozen `B^o(1)` decorations. Merged s7-46 proves that their physical balanced cell splits

```text
M_+=S*T,
M_-=R*J
```

have only divisor-many, hence `B^o(1)`, possibilities whenever they exist.

Merged s7-46 also proves that after those allocation data are fixed, signed reciprocal / second reciprocal / post-column completion has `B^o(1)` multiplicity. Merged s7-47 proves that balanced split existence alone is not fixed-power sparse and that balanced allocation and reciprocal completion may not be double charged as independent savings.

Define the Boolean predicate

```text
A_phys(a,b)=1
```

iff there exists an allowed `g=B^o(1)` and at least one balanced six-block allocation in the frozen chart that admits the full physical reciprocal/post-column completion.

Then

```text
BALANCED_ALLOCATION_WITNESS_MULTIPLICITY_PER_DIRECTION=Bo1
RECIPROCAL_COMPLETION_MULTIPLICITY_PER_ALLOCATION=Bo1
PHYSICAL_ACCEPTANCE_WITNESS_MULTIPLICITY_PER_DIRECTION=Bo1
BALANCED_AND_RECIPROCAL_DOUBLE_CHARGE_ALLOWED=false
FULL_PHYSICAL_ACCEPTANCE_COLLAPSES_TO_ONE_BOOLEAN_SLOPE_PREDICATE=true
```

Crucially, `B^o(1)` witness multiplicity does **not** imply sparse acceptance: `A_phys` could still be true on a full-exponent set of primitive slopes.

## 6. Relation to merged q12 and t104

Merged q12 concerns the earlier Gaussian norm-ratio collision receiver. Merged 4dv/Work-bjX22/s7-63/4dx have already discharged collision energy as a localization device on the present s receiver. Therefore q12's Parkkonen–Paulin transfer target is not the current minimal s object and is not used as a theorem source for a saving here.

Merged t104 freezes a full elementary boundary action in the fixed-U coefficient space. The abstract finite-label freezing principle is already available globally from Work-bjX22, but no arithmetic adapter identifies the t104 fixed-U boundary with the present primitive-slope predicate.

```text
MERGED_Q12_COLLISION_LITERATURE_CROSS_PROMOTED_TO_S7_64=false
MERGED_T104_FIXED_U_BOUNDARY_CROSS_PROMOTED_TO_S7_64=false
FIXED_U_TO_GLOBAL_ARITHMETIC_ADAPTER_PROVED=false
```

## 7. Minimal remaining arithmetic receiver

All of the following have now been discharged as independent polynomial support on the range-stable s arithmetic branch:

```text
heavy mover-prime label,
Gaussian root orientation,
collision energy,
proportional scale copies,
projective scale as an independent coordinate,
atomic mover chart label,
reciprocal completion multiplicity.
```

The surviving archimedean conditions are `O(1)` slope/height windows and are not individually power-sparse.

The unresolved arithmetic object is exactly the density of primitive coprime pairs `(a,b)` of height `B^(1/4+o(1))`, on one fixed Gaussian root line and inside the transported slope windows, for which

```text
A_phys(a,b)=1.
```

New minimal receiver:

```text
FullConductorInteriorDensePrimitiveQuarterPythagorean
FixedSubpolynomialGaussianPrimeFixedRootFixedAtomicChart
PrimitiveRationalSlopeBalancedReciprocalExistenceDensity.
```

No theorem here proves

```text
# { (a,b): A_phys(a,b)=1 }
 << B^(1/2-delta)
```

for any fixed `delta>0`.

```text
TRANSPORTED_PHYSICAL_ACCEPTANCE_FIXED_POWER_DEFICIT_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 8. Next internal split

Before opening a new H, expand `A_phys` into the actual allocation witnesses and determine which arithmetic component survives after the chart freeze:

```text
(a) balanced divisor-in-window conditions on the reconstructed norm/cofactor values,
(b) disjoint smooth/rough prime-allocation conditions,
(c) a genuinely coupled reciprocal-completion acceptance condition.
```

This decomposition determines the correct external theorem class, if one is needed.

## 9. H decision

No new auxiliary H is needed at s7-64. The receiver has only now become a single explicit arithmetic acceptance predicate on primitive rational slopes, and the internal witness decomposition is still unexhausted.

```text
S7_64_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
```

## Boundary

```text
STAGE14_S7_64=COMPLETE_PRIMITIVE_RATIONAL_SLOPE_CONTRACTION_AND_PHYSICAL_ACCEPTANCE_PREDICATE
MERGED_S7_63_IMPORTED=true
MERGED_WORK_BJX22_IMPORTED=true
MERGED_4DW_IMPORTED=true
MERGED_4DX_IMPORTED=true
MERGED_S7_46_FINITE_FIBER_IMPORTED=true
MERGED_S7_47_BALANCED_SPLIT_BOUNDARY_IMPORTED=true
MERGED_Q12_COLLISION_LITERATURE_CROSS_PROMOTED_TO_S7_64=false
MERGED_T104_FIXED_U_BOUNDARY_CROSS_PROMOTED_TO_S7_64=false
PRIMITIVE_RATIONAL_SLOPE_DETERMINES_PRIMITIVE_PAIR=true
RESIDUAL_COMMON_SCALE_MULTIPLICITY=Bo1
INDEPENDENT_POLYNOMIAL_SCALE_AFTER_PRIMITIVE_REDUCTION=false
FIXED_WIDTH_SLOPE_ROOT_LINE_AMBIENT_EXPONENT=1/2
ATOMIC_MOVER_CORE_CHART_LABEL_COUNT_LE_9=true
FULL_MOVER_CHART_DICTIONARY_SIZE=Bo1
ONE_ATOMIC_MOVER_CHART_CAN_BE_FROZEN=true
BALANCED_ALLOCATION_WITNESS_MULTIPLICITY_PER_DIRECTION=Bo1
RECIPROCAL_COMPLETION_MULTIPLICITY_PER_ALLOCATION=Bo1
PHYSICAL_ACCEPTANCE_WITNESS_MULTIPLICITY_PER_DIRECTION=Bo1
FULL_PHYSICAL_ACCEPTANCE_COLLAPSES_TO_ONE_BOOLEAN_SLOPE_PREDICATE=true
TRANSPORTED_PHYSICAL_ACCEPTANCE_FIXED_POWER_DEFICIT_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_64_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
REMAINING_RECEIVER=FullConductorInteriorDensePrimitiveQuarterPythagoreanFixedSubpolynomialGaussianPrimeFixedRootFixedAtomicChartPrimitiveRationalSlopeBalancedReciprocalExistenceDensity
NEXT=Stage14-s7-65
```
