# Stage15-6bz — weighted modulus summation audit

Base: Stage15-6by. Main-batch work unit 2.

The divisor expansion alone does **not** give the desired first moment from the fixed-modulus density. If one inserts only
\[
N_{d,e}(B)\lesssim B^{1+o(1)}/(de)^2
\]
then the weights `phi(d)phi(e)` leave a harmonic-scale double sum. More importantly, Stage15-6bu already certified that the physical primitive height is not a free four-variable box because of the moving gcd normalizer.

Therefore the formal local index cannot be summed uniformly to polynomial modulus without an additional physical-height argument. This prevents an illicit promotion of the expected `(de)^-2` density into the 6bx theorem.

The useful split is dyadic in `D=de`: small `D` can use fixed/moderate-level root-line counting; large `D` must be controlled by a structural bound relating channel gcd product to the physical height or to an already charged exact variable.

```text
STAGE15_6_SUBSTAGE=6bz
STAGE15_6BZ_FIXED_MODULUS_DENSITY_SUFFICIENT=false
STAGE15_6BZ_MOVING_NORMALIZER_FIREWALL=true
STAGE15_6BZ_ILLICIT_CROSS_PROMOTION=false
STAGE15_6BZ_REQUIRED_SPLIT=SMALL_MODULUS_VS_LARGE_GCD_PRODUCT
STAGE15_6BZ_EXIT=STRUCTURAL_GCD_PRODUCT_HEIGHT_SEARCH_READY
```