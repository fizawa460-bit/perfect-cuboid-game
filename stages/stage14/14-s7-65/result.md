# Stage14-s7-65 — primitive-slope physical witness decomposition and coprime binary-form contraction

## Status

`COMPLETE_PRIMITIVE_SLOPE_PHYSICAL_WITNESS_DECOMPOSITION_AND_COPRIME_BINARY_FORM_CONTRACTION`

Consumes only merged sources on latest main at branch creation:

- merged `Stage14-s7-64`,
- merged `Stage14-4dy`,
- merged `Stage14-s7-46`, `s7-47`, `s7-59`, `s7-60`,
- merged `Stage14-4dx`,
- merged `Stage14-Work-bkX23`,
- latest main through `51a0228d727103abb7f73bcc1cf5be244e60cbb2`.

Unmerged descendants are advisory only.

The canonical whole-family theorem remains

```text
V(B) << B^(1/2+o(1)),
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2,
SQRT_B_UPPER_BOUND_PROVED=true,
STRICT_SUBSQRT_POWER_SAVING_PROVED=false.
```

Merged s7-64 and 4dy reduce the global arithmetic receiver to one Boolean physical-acceptance predicate

```text
A_phys(a,b) in {0,1}
```

on primitive rational slopes

```text
gcd(a,b)=1,
0<a<b,
H=max(a,b)=B^(1/4+o(1)),
```

on one fixed subpolynomial Gaussian root line and one frozen atomic chart. Both explicitly schedule one more internal witness decomposition before any new H. Stage14-s7-65 performs that decomposition.

## 1. Primitive slope reconstruction

Write the complementary factors as in merged s7-64 / 4dy:

```text
r=g a,
s=g b,
gcd(a,b)=1,
g=B^o(1).
```

Then

```text
D=(r+s)/2=g(a+b)/2,
A=(s-r)/2=g(b-a)/2.
```

Therefore exactly

```text
D^2+A^2 = g^2(a^2+b^2)/2,
D^2-A^2 = g^2ab.
```

In the odd / fixed-2-primary normalization of merged s7-46, define the primitive binary-form cores

```text
F_+(a,b)=oddpart(a^2+b^2),
F_-(a,b)=oddpart(ab).
```

The frozen Gaussian mover prime `ell_*` lies on the plus norm side; dividing out that already charged fixed factor and the allowed `g=B^o(1)` / endpoint decorations leaves the same two primitive arithmetic cores up to `B^o(1)` multiplicative support.

```text
PRIMITIVE_SLOPE_PLUS_CORE_IS_SUM_OF_TWO_SQUARES=true
PRIMITIVE_SLOPE_MINUS_CORE_IS_PRODUCT_AB=true
RESIDUAL_SCALE_AND_ENDPOINT_DECORATIONS=Bo1
```

## 2. Exact cross-sign coprimality of the primitive cores

For `gcd(a,b)=1`,

```text
gcd(a^2+b^2,a)=1,
gcd(a^2+b^2,b)=1.
```

Hence

```text
boxed:
gcd(a^2+b^2,ab)=1.
```

Passing to odd parts and dividing by the already-frozen plus-side Gaussian prime cannot create a new common prime. Thus

```text
boxed:
gcd(F_+,F_-)=1.
```

All fixed-power plus/minus common-prime overlap is therefore absent already at the primitive binary-form level. Any residual common support can only come from the previously allowed common scale / endpoint / 2-primary decorations, whose total multiplicity is `B^o(1)`.

This sharpens the earlier pairwise-separation conclusion of merged s7-47 in the primitive-slope coordinates:

```text
PRIMITIVE_BINARY_FORM_CORE_GCD_ONE=true
CROSS_SIGN_FIXED_POWER_PRIME_SHARING_IMPOSSIBLE=true
CROSS_SIGN_PRIME_SEPARATION_AUTOMATIC_UP_TO_Bo1=true
CROSS_SIGN_DISJOINTNESS_IS_NOT_AN_INDEPENDENT_DENSITY_SELECTOR=true
```

No saving is charged here; one redundant obstruction is removed.

## 3. Expand the physical witness

Fix one primitive pair `(a,b)` in the transported archimedean windows and on the fixed root line. For each allowed `g=B^o(1)` and frozen endpoint/2-primary decoration, merged s7-46 reconstructs the two complementary cofactor products

```text
M_+(a,b,g),
M_-(a,b,g),
```

which, in the normalized packet, satisfy

```text
M_+ = S*T,
M_- = R*J.
```

A physical witness consists of

```text
w=(g, decoration, S,T,R,J, reciprocal/post-column witness)
```

subject to all retained conditions:

```text
(1) S*T=M_+ and R*J=M_-,
(2) S,T lie in their balanced physical windows,
(3) R,J lie in their balanced physical windows,
(4) R,S,T,J satisfy the squarefree / pairwise-coprime cell masks,
(5) all within-form prime-allocation / smooth-rough side masks hold,
(6) the frozen chart/orientation labels hold,
(7) signed reciprocal / second reciprocal / post-column completion exists.
```

Merged s7-46 gives, for a fixed primitive direction and normalized outer data,

```text
# balanced allocation witnesses = B^o(1),
# reciprocal completions per allocation = B^o(1).
```

Thus

```text
# physical witnesses per primitive slope = B^o(1).
```

Equivalently,

```text
A_phys(a,b)=1
```

iff at least one witness in a `B^o(1)`-sized fiber satisfies the full conjunction above.

```text
PHYSICAL_ACCEPTANCE_WITNESS_EXPANSION_EXPLICIT=true
PHYSICAL_WITNESS_MULTIPLICITY_PER_PRIMITIVE_SLOPE=Bo1
FINITE_WITNESS_MULTIPLICITY_IMPLIES_DENSITY_SAVING=false
```

## 4. Balanced divisor windows do not by themselves give the missing power

Merged s7-47 already proves that balanced squarefree split existence by itself is not fixed-power sparse in the ambient cofactor range: full-exponent semiprime families admit such splits.

Therefore neither

```text
exists S*T=M_+ in balanced windows
```

nor

```text
exists R*J=M_- in balanced windows
```

can be charged as a standalone `B^{-delta}` density factor on the current receiver without using correlation with the binary-form values and the remaining physical completion.

Merged 4dx/4dy likewise show that transported balanced/interior range restrictions are only `O(1)` positive-width slope/height windows, not fixed-power-thin sets.

```text
BALANCED_DIVISOR_WINDOW_ALONE_FIXED_POWER_SAVING=false
ARCHIMEDEAN_SLOPE_WINDOW_ALREADY_DISCHARGED=true
```

## 5. What remains of the prime-allocation conditions

The prime-allocation masks split into two logically different pieces.

Cross-sign separation between the plus and minus primitive cores is automatic by Section 2 and therefore cannot carry a new density loss.

Within one form, however, the physical cells still require a legal allocation of prime factors of

```text
F_+(a,b)
```

between the plus cells and of

```text
F_-(a,b)=oddpart(ab)
```

between the minus cells, with balanced windows and the retained squarefree/support masks.

Because `gcd(a,b)=1`, every divisor `d|ab` decomposes uniquely as

```text
d=d_a d_b,
d_a|a,
d_b|b,
gcd(d_a,d_b)=1.
```

Thus the minus-side balanced allocation is an exact divisor-allocation problem on the two coprime primitive coordinates `a,b`; it is not an extra cross-sign prime-collision problem.

The plus-side allocation is the corresponding divisor-allocation problem on the Gaussian norm value `a^2+b^2`, after removing the already-frozen `ell_*` and subpolynomial decorations.

```text
CROSS_SIGN_ALLOCATION_COMPONENT_DISCHARGED=true
MINUS_BALANCED_ALLOCATION_REDUCES_TO_DIVISORS_OF_COPRIME_A_AND_B=true
PLUS_BALANCED_ALLOCATION_LIVES_ON_SUM_OF_TWO_SQUARES_NORM=true
WITHIN_FORM_ALLOCATION_REMAINS_ARITHMETIC=true
```

## 6. Reciprocal completion is coupled to the same allocation witness

Merged s7-60 proves

```text
BALANCED_ALLOCATION_AND_RECIPROCAL_COMPLETION_SHARE_ONE_COORDINATE_PACKET=true
RECIPROCAL_COMPLETION_INDEPENDENT_FIXED_POWER_SUPPORT=false.
```

Therefore reciprocal/post-column completion is not a second support length that can be multiplied by a balanced-divisor saving. It is a Boolean admissibility test on the same divisor-allocation witness.

For one allocation witness `w_alloc=(S,T,R,J,...)`, write

```text
Q_recip(w_alloc) in {0,1}
```

for existence of signed reciprocal / second reciprocal / post-column completion. Schematically,

```text
A_phys(a,b)
 = OR_{w_alloc in W(a,b)}
     [ B_bal(w_alloc)
       * P_within(w_alloc)
       * Q_recip(w_alloc) ],
```

where

```text
|W(a,b)|=B^o(1).
```

No independence between the three factors is asserted or available.

```text
RECIPROCAL_COMPLETION_IS_BOOLEAN_ON_BALANCED_ALLOCATION_WITNESS=true
BALANCED_AND_RECIPROCAL_DOUBLE_CHARGE_ALLOWED=false
JOINT_BALANCED_RECIPROCAL_SELECTOR_REMAINS=true
```

## 7. Principal-density formulation on the frozen slope family

Merged 4dy / Work-bkX23 define the frozen primitive-slope background family `Omega_G(B)` and

```text
mu_G = E_{Omega_G} A_phys.
```

On any square-root-saturating subsequence,

```text
mu_G=B^(-o(1))
```

in the exponent-zero lower-bound sense. Hence the missing theorem is exactly a fixed-power upper bound for the density of primitive slopes whose two coprime binary-form values admit at least one jointly physical balanced-allocation / reciprocal witness.

All of the following are now discharged as independent fixed-power density carriers:

```text
common scale,
projective scale,
Gaussian root label,
atomic chart label,
cross-sign prime sharing,
balanced-split multiplicity,
reciprocal-completion multiplicity,
archimedean slope-window width.
```

The live arithmetic content is the correlated existence problem

```text
F_+(a,b)=oddpart(a^2+b^2),
F_-(a,b)=oddpart(ab),
gcd(F_+,F_-)=1,
```

with legal balanced within-form divisor allocations and coupled reciprocal acceptance.

New minimal receiver:

```text
FullConductorInteriorDensePrimitiveQuarterPythagorean
FixedSubpolynomialGaussianPrimeFixedRootFixedAtomicChart
CoprimeBinaryFormsBalancedDivisorAllocationReciprocalAcceptancePrincipalDensity.
```

```text
CURRENT_GLOBAL_PRINCIPAL_DENSITY_RECEIVER=FullConductorInteriorDensePrimitiveQuarterPythagoreanFixedSubpolynomialGaussianPrimeFixedRootFixedAtomicChartCoprimeBinaryFormsBalancedDivisorAllocationReciprocalAcceptancePrincipalDensity
FIXED_POWER_ACCEPTANCE_DENSITY_DEFICIT_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
```

## 8. What s7-66 should test

The next internal task should not reopen collision energy, common-prime overlap, chart variation, or generic balanced-divisor density.

It should work directly with the two primitive binary forms

```text
ab,
a^2+b^2
```

on the fixed Gaussian root line and ask whether simultaneous legal balanced allocations plus `Q_recip=1` force one of:

```text
(a) a growing-modulus divisor constraint,
(b) a short divisor interval with fixed-power deficit,
(c) a low-degree relation between a divisor of ab and a Gaussian divisor of a^2+b^2,
(d) or a genuine theorem-ready correlated divisor-density problem.
```

This is strictly smaller than the old six-block or collision-energy receivers.

## 9. H decision

No new auxiliary H is opened at s7-65.

Reason: the witness decomposition has now exposed a new exact elementary contraction, `gcd(a^2+b^2,ab)=1`, and the next step is still internal: write the remaining within-form divisor allocations in primitive `(a,b)` coordinates and test for a direct low-degree/growing-modulus relation before launching another literature theorem audit.

```text
S7_65_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
```

## Boundary

```text
STAGE14_S7_65=COMPLETE_PRIMITIVE_SLOPE_PHYSICAL_WITNESS_DECOMPOSITION_AND_COPRIME_BINARY_FORM_CONTRACTION
MERGED_S7_64_IMPORTED=true
MERGED_4DY_IMPORTED=true
MERGED_S7_46_IMPORTED=true
MERGED_S7_47_IMPORTED=true
MERGED_S7_59_IMPORTED=true
MERGED_S7_60_IMPORTED=true
MERGED_4DX_IMPORTED=true
MERGED_WORK_BKX23_IMPORTED=true
PRIMITIVE_SLOPE_PLUS_CORE_IS_SUM_OF_TWO_SQUARES=true
PRIMITIVE_SLOPE_MINUS_CORE_IS_PRODUCT_AB=true
PRIMITIVE_BINARY_FORM_CORE_GCD_ONE=true
CROSS_SIGN_FIXED_POWER_PRIME_SHARING_IMPOSSIBLE=true
CROSS_SIGN_PRIME_SEPARATION_AUTOMATIC_UP_TO_Bo1=true
CROSS_SIGN_DISJOINTNESS_IS_NOT_AN_INDEPENDENT_DENSITY_SELECTOR=true
PHYSICAL_ACCEPTANCE_WITNESS_EXPANSION_EXPLICIT=true
PHYSICAL_WITNESS_MULTIPLICITY_PER_PRIMITIVE_SLOPE=Bo1
BALANCED_DIVISOR_WINDOW_ALONE_FIXED_POWER_SAVING=false
CROSS_SIGN_ALLOCATION_COMPONENT_DISCHARGED=true
MINUS_BALANCED_ALLOCATION_REDUCES_TO_DIVISORS_OF_COPRIME_A_AND_B=true
PLUS_BALANCED_ALLOCATION_LIVES_ON_SUM_OF_TWO_SQUARES_NORM=true
WITHIN_FORM_ALLOCATION_REMAINS_ARITHMETIC=true
RECIPROCAL_COMPLETION_IS_BOOLEAN_ON_BALANCED_ALLOCATION_WITNESS=true
BALANCED_AND_RECIPROCAL_DOUBLE_CHARGE_ALLOWED=false
JOINT_BALANCED_RECIPROCAL_SELECTOR_REMAINS=true
FIXED_POWER_ACCEPTANCE_DENSITY_DEFICIT_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
SQRT_B_UPPER_BOUND_PROVED=true
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
S7_65_NEW_AUXILIARY_H_NEEDED=false
S_ROUTE_BLOCKED_WAITING_FOR_H=false
REMAINING_RECEIVER=FullConductorInteriorDensePrimitiveQuarterPythagoreanFixedSubpolynomialGaussianPrimeFixedRootFixedAtomicChartCoprimeBinaryFormsBalancedDivisorAllocationReciprocalAcceptancePrincipalDensity
NEXT=Stage14-s7-66
```
