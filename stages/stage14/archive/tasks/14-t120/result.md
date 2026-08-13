# Stage14-t120 — relocate cofactor-core saving to generic scalar-norm support

## Status

`COMPLETE_GENERIC_SPLIT_PRIME_PHYSICAL_NORM_SUPPORT_RELOCATION_AND_TWO_BRANCH_RECEIVER`

Consumes Stage14-t119 on the same batch branch together with merged `Stage14-Work-boX27` and merged `Stage14-t114`.

By t119, expand the `B^o(1)` exceptional multiplier/label family and freeze one admissible exceptional packet

```text
(m,e),
```

at charged-once `B^o(1)` cost. The scalar cofactor norm is now

```text
n=m*g,
```

with

```text
gcd(g,E_U)=1,
every odd p|g satisfies p==1 mod 4.
```

For each generic norm `g`, let

```text
F_g={primitive generic split-prime orientation labels epsilon above g}.
```

Merged t91/t116 give uniformly

```text
1<=|F_g|<=B^o(1)
```

on nonempty primitive norm fibers. Let

```text
A_m(g):=A(m*g)>=0
```

be the exact t114/t115 prime-principal weight, and let

```text
S_{m,e}(g,epsilon) in {0,1}
```

be the remaining ell-independent global physical Boolean after the frozen exceptional-local predicate is satisfied.

Define

```text
H_{m,e}
 := sum_g A_m(g)|F_g|,

M_{m,e}
 := sum_g A_m(g)
      sum_{epsilon in F_g} S_{m,e}(g,epsilon),

G_phys(m,e)
 := {g: exists epsilon in F_g with S_{m,e}(g,epsilon)=1}.
```

The merged Work-boX27 subpolynomial-fiber support-relocation lemma applies exactly with

```text
y=g,
f=epsilon,
w_y=A_m(g).
```

Hence for any fixed `delta>0`, a core deficit

```text
M_{m,e} <= B^(-delta) H_{m,e}
```

forces

```text
sum_{g in G_phys(m,e)} A_m(g)
 <= B^(-delta+o(1)) sum_g A_m(g).
```

Thus a fixed-power loss cannot live purely in a nonzero orientation density inside one generic norm fiber. Once the inner orientation fiber is `B^o(1)`, the loss must appear as a weighted deficit in the polynomial set of generic scalar norms that admit at least one physical orientation.

Combining this with the exact t114 principal-versus-selected-class dichotomy yields the new fixed-U two-branch receiver:

```text
(A') ExceptionalMultiplierConditionedGenericSplitPrimePhysicalNormSupportDeficit
```

or

```text
(C) PhysicalSelectedProjectiveClassNearTotalPrimeDepletion.
```

The t117 mechanisms

```text
ExceptionalLocalAdmissibleNormSupportWeightedDensityDeficit
```

and

```text
GenericSplitPrimeOrientationPhysicalPrincipalDensityDeficit
```

are therefore structurally superseded as independent mechanisms. Their only legal fixed-power manifestation after t118/t119 and Work-boX27 is the weighted generic norm-support deficit above.

This is a material receiver change. It agrees with the broader merged Work-boX27 statement `WeightedPhysicalScalarNormSupportDeficit OR selected-class depletion`, but now identifies the actual scalar outer variable after exceptional packet support is peeled:

```text
g = generic split-prime cofactor norm coprime to E_U.
```

No new tH audit is opened. Merged tH26 already rules out treating the unresolved global orientation coefficient as a theorem-ready Hecke/spin coefficient, and merged tH28 rules out a generic unmasked projected-norm sieve saving. The new support predicate still contains the full existential physical orientation Boolean and must be opened internally before a fresh theorem audit is justified.

```text
GENERIC_ORIENTATION_FIBER_SIZE=Bo1
GENERIC_NORM_SUPPORT_RELOCATION_APPLIED=true
ORIENTATION_DENSITY_AS_INDEPENDENT_POWER_SOURCE_SUPERSEDED=true
EXCEPTIONAL_LOCAL_DENSITY_AS_INDEPENDENT_POWER_SOURCE_SUPERSEDED=true
GENERIC_PHYSICAL_NORM_SUPPORT_IS_POLYNOMIAL_OUTER_RECEIVER=true
SELECTED_CLASS_NEAR_TOTAL_DEPLETION_BRANCH_RETAINED=true
RECEIVER_MATERIALLY_CHANGED=true
FIXED_U_POWER_SAVING_PROVED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_PROVED=false
T_ROUTE_H_NEEDED=false
T_ROUTE_H_REQUEST=NONE
T_ROUTE_H_TARGET=NONE
T_ROUTE_H_BLOCKING=false
TH29_NEEDED=false
PREFERRED_RECEIVER=SharedUExceptionalMultiplierConditionedGenericSplitPrimePhysicalNormSupportDeficitOrSelectedProjectiveClassNearTotalPrimeDepletion
NEXT_INTERNAL_TARGET=GenericSplitPrimePhysicalNormSupportBooleanArithmeticDecomposition
NEXT=Stage14-t121
```
