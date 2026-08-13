# Stage15-6cf — physical-height-aware divisor switch

Base: Stage15-6ce. Main-batch work unit 2.

Start from the exact expansion
\[
\sum_{P\in A(B)}G_S(P)G_O(P)=\sum_{d,e}\varphi(d)\varphi(e)N_{d,e}(B).
\]
Instead of summing fixed-modulus density to arbitrary `(d,e)`, perform a divisor switch at dyadic product `D=de` using the physical variables themselves. For each state, divisors with `de>D_0` are paired with complementary cofactors in the four channel forms; divisors with `de<=D_0` retain the projective root-line conditions.

This produces the exact two-range receiver:

1. **small modulus** `de<=D_0`: root-line congruence count under the physical height;
2. **large modulus** `de>D_0`: complementary-divisor count controlled by the sizes of the channel forms rather than by a fictitious uniform density.

The switch is measure-correct and does not double charge `k_S,k_O`. However a polynomially uniform estimate for the small-modulus physical count and a sharp enough complementary-form average are not yet both proved, so the first moment remains open.

```text
STAGE15_6_SUBSTAGE=6cf
STAGE15_6CF_PHYSICAL_DIVISOR_SWITCH_EXACT=true
STAGE15_6CF_SMALL_RANGE=de<=D0
STAGE15_6CF_LARGE_RANGE=de>D0_COMPLEMENTARY_DIVISORS
STAGE15_6CF_MEASURE_CORRECT=true
STAGE15_6CF_NO_DOUBLE_CHARGE=true
STAGE15_6CF_FIRST_MOMENT_PROVED=false
STAGE15_6CF_EXIT=TWO_RANGE_BOUND_AUDIT_READY
```