# Stage14-q16 — rectangular distinct-product capacity literature radar

## Gate

`14-q` gate: **RUN**.

Source snapshot:

```text
MAIN_SHA=f9c3116fc82cacbcb494a055b40bb0daa825e19e
LATEST_Q=Stage14-q15
```

The post-q15 merged receiver has materially changed. Merged `Stage14-4fw..4fy` and `Stage14-Work-bxX36` eliminate the moving divisor-window normalization problem on the fixed-`E` two-sided branch and replace it by the exact rectangular multiplication image

```text
P(D,V)={d*v:d in D,v in V},
```

where, on one frozen packet,

```text
D = Z_{>0} intersect sqrt(I_X/(alpha*E0)),
V = Z_{>0} intersect sqrt(I_Y/(beta*E0)).
```

Thus `D` and `V` are finite integer intervals, hence finite arithmetic progressions of common difference one after the already-frozen exponent-cell intersections.

On a principal rectangle write

```text
#D=B^(kappa_D+o(1)),
#V=B^(kappa_V+o(1)),
#P(D,V)=B^(pi+o(1)),
```

with

```text
kappa_D+kappa_V >= mu-o(1).
```

The literature question for mechanism `P` is now exact:

```text
Can #P(D,V) be smaller than #D#V by a fixed B-power
on such interval rectangles?
```

The conditional physical-lift mechanism is a separate question and is not included in this ambient product-set audit.

## 1. Xu--Zhou: product sets of arithmetic progressions

Max Wenqiang Xu and Yunkun Zhou, *On product sets of arithmetic progressions*, arXiv:2201.00104.

Primary source:

```text
https://arxiv.org/abs/2201.00104
```

The paper proves near-quadratic lower bounds for product sets of finite arithmetic progressions and explicitly gives asymmetric extensions for two progressions. Its proof is formulated through multiplicative-energy bounds and Cauchy--Schwarz.

For Stage14 this is directly relevant because the merged 4fw factor windows are themselves finite integer intervals, not arbitrary physical subsets.

The theorem-scale consequence needed here is only exponent-level:

```text
|D*V| >= |D||V| / (log(max(|D|,|V|)))^(O(1)+o(1))
```

through the asymmetric arithmetic-progression product-set result / its multiplicative-energy reduction. Therefore, whenever both factor-window lengths are polynomial in `B`,

```text
#P(D,V)=#D#V * B^(-o(1)),
```

and hence

```text
pi = kappa_D+kappa_V.
```

At the fixed-power exponent level there is no multiplication-image compression.

```text
XU_ZHOU_ASYMMETRIC_AP_PRODUCT_SET=DIRECT_FOR_FIXED_E_AMBIENT_RECTANGLE
FIXED_E_POLYNOMIAL_POLYNOMIAL_PRODUCT_COMPRESSION_EXPONENT=0
```

This is a lower bound on the ordinary ambient product image only. It does not lower-bound the original physical support.

## 2. Subpolynomial-side rectangles require no external theorem

Suppose one side is `B^o(1)` and the other side is polynomial. Choose any fixed nonzero element from the smaller nonempty factor set. Multiplication by that fixed integer is injective on the other factor set, so

```text
#P(D,V) >= max(#D,#V).
```

Since

```text
min(#D,#V)=B^o(1),
```

we obtain

```text
#P(D,V) >= #D#V * B^(-o(1)).
```

Thus the same exponent identity holds:

```text
pi=kappa_D+kappa_V.
```

This includes bounded-side endpoint rectangles as long as the factor sets are nonempty.

```text
SUBPOLYNOMIAL_SIDE_INJECTIVE_SLICE_SUFFICES=true
SUBPOLYNOMIAL_SIDE_PRODUCT_COMPRESSION_EXPONENT=0
```

## 3. Ford multiplication-table theory as benchmark

Kevin Ford, *Integers with a divisor in (y,2y]*, arXiv:math/0607473, and the full divisor-interval work underlying the multiplication-table order of magnitude.

Primary source:

```text
https://arxiv.org/abs/math/0607473
```

Ford's multiplication-table result shows that the classical square box `[N]*[N]` does have many collisions, but the loss is logarithmic rather than a fixed power of `N`.

For q16 this supports the same exponent-level boundary:

```text
multiplicative collisions can be numerous,
but ordinary interval product images retain full polynomial exponent.
```

Ford is no longer the cleanest direct adapter because merged 4fw has already straightened the Stage14 object to a rectangular product set, for which Xu--Zhou directly supplies the arithmetic-progression product-set framework.

```text
FORD_MULTIPLICATION_TABLE=BACKGROUND_CONSISTENT_WITH_ZERO_POWER_COMPRESSION
```

## 4. 2026 restricted-prime multiplication tables

Jeremy Schlitt, *Multiplication Tables for Integers with Restricted Prime Factors*, arXiv:2603.19212.

Primary source:

```text
https://arxiv.org/abs/2603.19212
```

This extends Ford-type multiplication-table/divisor-window counting to integers whose prime factors lie in a prime set of prescribed relative density.

It is not needed for the fixed-`E` ambient rectangle because `D,V` in 4fw are plain integer intervals and no prime-factor restriction remains in the ordinary upper envelope. It may become relevant only if a later route reimposes a theorem-compatible prime-factor support before taking the product image.

```text
SCHLITT_2026_RESTRICTED_PRIME_MULTIPLICATION_TABLE=ADVISORY_ONLY
```

## 5. Exact Stage14 consequence

The merged fixed-`E` two-sided receiver separates

```text
P = ambient distinct-product capacity loss,
C = conditional physical-lift loss inside P(D,V).
```

q16 now resolves `P` at the fixed-power exponent level.

For every nonempty principal rectangle:

- if both factor windows are polynomial, Xu--Zhou gives only polylogarithmic product compression;
- if one factor window is subpolynomial, the elementary injective-slice lower bound gives only subpolynomial compression.

Hence uniformly at the Stage14 exponent scale,

```text
#P(D,V)=B^(kappa_D+kappa_V+o(1)),
pi=kappa_D+kappa_V,
FIXED_POWER_DISTINCT_PRODUCT_COMPRESSION=false.
```

Consequently a principal rectangle satisfying

```text
kappa_D+kappa_V >= mu-o(1)
```

cannot be closed by ambient multiplication collisions alone. Any fixed-power deficit of the physical accepted support must come from the conditional lift (or from a later additional physical restriction not present in the ordinary ambient `P(D,V)`).

This does **not** prove

```text
physical support = P(D,V)
```

and it does not give a whole-family saving. The physical support remains only a subset of the ordinary product image.

```text
FIXED_E_DISTINCT_PRODUCT_CAPACITY_FIXED_POWER_SAVING_AVAILABLE=false
FIXED_E_DISTINCT_PRODUCT_CAPACITY_FULL_EXPONENT_PROVED=true
FIXED_E_CONDITIONAL_PHYSICAL_LIFT_REMAINS=true
```

## 6. Non-cross-promotion boundaries

The q16 product-set conclusion is scoped to the exact fixed-`E` 4fw rectangle.

It is not automatically valid for:

```text
- the polynomial-E s outer-pair ordinary-divisor envelope, because rectangular straightening is unproved there;
- fixed-E primitive endpoint completion, which has no divisor/product obstruction left;
- polynomial-E fixed-product residual local-mask/completion branch;
- fixed-U Gaussian-prime short-interval occupancy;
- the non-heavy three-divisor, projective-mover or diffuse Gaussian-factor H targets.
```

```text
Q16_PRODUCT_SET_TO_POLYNOMIAL_E_CROSS_PROMOTION_PROVED=false
Q16_PRODUCT_SET_TO_FIXED_U_CROSS_PROMOTION_PROVED=false
Q16_PRODUCT_SET_TO_PHYSICAL_LIFT_CROSS_PROMOTION_PROVED=false
```

## 7. Handoff

Mainline should consume q16 before spending an external H stage on multiplication-map collision energy.

The useful internal handoff is

```text
Q16_XU_ZHOU_RECTANGULAR_PRODUCT_CAPACITY_CONSUMPTION_TEST
```

with the expected fixed-power conclusion

```text
pi=kappa_D+kappa_V
```

on every nonempty fixed-`E` principal rectangle, after separately handling subpolynomial-side rectangles by injective slicing.

After that consumption, the fixed-`E` two-sided mechanism should reduce to

```text
PrincipalRectangularProductFullExponentConditionalPhysicalLiftDeficit
```

rather than opening a multiplication-collision H target.

A new external search for the conditional physical lift is premature until main/s open that Boolean into a stable theorem-shaped arithmetic coefficient.

```text
Q16_NEW_PRODUCT_CAPACITY_H_NEEDED=false
Q16_CONDITIONAL_LIFT_EXTERNAL_SEARCH_TRIGGERED=false
```

## Locks

```text
STAGE14_Q16=COMPLETE_RECTANGULAR_PRODUCT_CAPACITY_LITERATURE_RADAR
STAGE14_Q_GATE=RUN
SOURCE_MAIN_SHA=f9c3116fc82cacbcb494a055b40bb0daa825e19e
LATEST_PREVIOUS_Q=Stage14-q15
Q15_MOVING_INTERVAL_NORMALIZATION_REMAINS=false
FIXED_E_RECTANGULAR_PRODUCT_SET_THEOREM_READY=true
XU_ZHOU_ASYMMETRIC_AP_PRODUCT_SET=DIRECT_FOR_FIXED_E_AMBIENT_RECTANGLE
SUBPOLYNOMIAL_SIDE_INJECTIVE_SLICE_SUFFICES=true
FIXED_E_DISTINCT_PRODUCT_CAPACITY_FULL_EXPONENT_PROVED=true
FIXED_E_DISTINCT_PRODUCT_CAPACITY_FIXED_POWER_SAVING_AVAILABLE=false
FIXED_E_CONDITIONAL_PHYSICAL_LIFT_REMAINS=true
DIRECT_PHYSICAL_LIFT_THEOREM_FOUND=false
CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2
STRICT_SUBSQRT_POWER_SAVING_FROM_LITERATURE_PROVED=false
```
