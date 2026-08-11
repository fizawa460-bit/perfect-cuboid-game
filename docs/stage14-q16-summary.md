# Stage14-q16 summary

`14-q` gate: **RUN**.

Latest merged main at dispatch:

```text
f9c3116fc82cacbcb494a055b40bb0daa825e19e
```

Merged `4fw..4fy + Work-bxX36` materially supersede q15's moving divisor-window receiver. On the fixed-`E` two-sided branch the ordinary upper envelope is now exactly

```text
P(D,V)={d*v:d in D,v in V},
```

with `D,V` finite integer intervals. Surviving principal rectangles satisfy

```text
#D=B^(kappa_D+o(1)),
#V=B^(kappa_V+o(1)),
kappa_D+kappa_V>=mu-o(1).
```

## Literature verdict

Xu--Zhou's asymmetric product-set theorem for finite arithmetic progressions is directly applicable to the fixed-`E` ambient rectangle when both factor windows are polynomial. It gives only polylogarithmic loss from pair capacity, hence

```text
#P(D,V)=#D#V*B^(-o(1))
```

at Stage14 exponent scale.

If one factor window is `B^o(1)`, no external theorem is needed: freezing one nonzero element of the smaller side gives an injective copy of the larger side, so again

```text
#P(D,V)=#D#V*B^(-o(1))
```

at exponent scale.

Therefore on every nonempty fixed-`E` principal rectangle

```text
pi=kappa_D+kappa_V.
```

The ambient multiplication image cannot supply a fixed `B`-power saving.

```text
STAGE14_Q16=COMPLETE_RECTANGULAR_PRODUCT_CAPACITY_LITERATURE_RADAR
STAGE14_Q_GATE=RUN
XU_ZHOU_ASYMMETRIC_AP_PRODUCT_SET=DIRECT_FOR_FIXED_E_AMBIENT_RECTANGLE
SUBPOLYNOMIAL_SIDE_INJECTIVE_SLICE_SUFFICES=true
FIXED_E_DISTINCT_PRODUCT_CAPACITY_FULL_EXPONENT_PROVED=true
FIXED_E_DISTINCT_PRODUCT_CAPACITY_FIXED_POWER_SAVING_AVAILABLE=false
```

Ford multiplication-table theory is consistent with this conclusion: collisions create logarithmic-scale compression, not fixed-power compression. The 2026 restricted-prime multiplication-table theorem is advisory only because the current ordinary upper envelope has no retained restricted-prime condition.

## Remaining mechanism

q16 resolves only the ambient distinct-product mechanism `P`. It does **not** identify the physical support with `P(D,V)`.

The fixed-`E` two-sided branch should therefore reduce to

```text
PrincipalRectangularProductFullExponentConditionalPhysicalLiftDeficit.
```

The remaining fixed-power source, if any, is the Stage14-specific conditional physical lift inside the product support.

```text
FIXED_E_CONDITIONAL_PHYSICAL_LIFT_REMAINS=true
DIRECT_PHYSICAL_LIFT_THEOREM_FOUND=false
```

No new product-capacity H audit is warranted. Mainline should first consume

```text
Q16_XU_ZHOU_RECTANGULAR_PRODUCT_CAPACITY_CONSUMPTION_TEST
```

and open the conditional lift internally before another external theorem search.

## Scope locks

The q16 result is not cross-promoted to the polynomial-`E` s branch, whose rectangular straightening is still unproved, and it is unrelated to fixed-U Gaussian-prime occupancy.

```text
Q16_PRODUCT_SET_TO_POLYNOMIAL_E_CROSS_PROMOTION_PROVED=false
Q16_PRODUCT_SET_TO_FIXED_U_CROSS_PROMOTION_PROVED=false
Q16_PRODUCT_SET_TO_PHYSICAL_LIFT_CROSS_PROMOTION_PROVED=false
Q16_NEW_PRODUCT_CAPACITY_H_NEEDED=false
Q16_CONDITIONAL_LIFT_EXTERNAL_SEARCH_TRIGGERED=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_FROM_LITERATURE_PROVED=false
```

q parks after q16 until the conditional physical-lift coefficient becomes theorem-shaped, the polynomial-`E` branch gains a stable product-set normalization, or another genuinely new stable obstruction/theorem appears.
