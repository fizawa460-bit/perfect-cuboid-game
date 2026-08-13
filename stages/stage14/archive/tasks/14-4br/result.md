# Stage14-4br — weighted cross-factor threshold optimization

## Purpose
Merged Stage14-4bq proves `V(B)<<B^(61/63+o(1))`; the unique bottleneck is the cross sector from merged Stage14-4bm.

There, with `gamma=4/21`, `X2_cross>=B^gamma` and `X2_cross<=2^a*c*h^2`, where `c=gcd(H,X2)_odd` and `h^2|X2` is the squarefull-excess receiver.

4bm used thresholds `gamma/3, gamma/3, gamma/6`. This stage optimizes thresholds according to the actual counting savings of `2^a`, `c`, and `h`.

## Weighted split
If `2^a<B^delta`, `c<B^delta`, and `h<B^delta`, then `2^a*c*h^2<B^(4delta)`. Hence `X2_cross>=B^gamma` forces at least one of `2^a>=B^delta`, `c>=B^delta`, `h>=B^delta` whenever `4delta<=gamma`.

The optimal common threshold is `delta=gamma/4=1/21`.

## Counting
Merged 4bm already proves uniformly

- `2^a>=A => E<<B^(1+o(1))/A`,
- `c>=C => E<<B^(1+o(1))/C`,
- `h>=H0 => E<<B^(1+o(1))/H0`.

Putting `A=C=H0=B^(1/21)` gives all three sub-sectors `<<B^(20/21+o(1))`. Therefore

`E_cross(B)<<B^(20/21+o(1))`.

The improvement over 4bm is `61/63-20/21=1/63`.

## Whole-family recombination
Merged 4bq gives the other exhaustive sectors:

- small partner leg: `B^(20/21+o(1))`;
- good-cell residual: `B^(13/14+o(1))`.

Since `13/14<20/21`, the whole physical family now satisfies

`V(B)<<B^(20/21+o(1))`.

Relative to the pre-post-local exponent `41/42`, the cumulative saving is `41/42-20/21=1/42`. The remaining gap to square root is `20/21-1/2=19/42`.

No new external theorem, density heuristic, or independence assumption is used; this is an exact optimization of already-merged deterministic cross receivers. Merged t40 and s7-03 were checked for compatibility but are not needed as theorem inputs here.

## Boundary
```text
STAGE14_4BR=OPTIMIZED_CROSS_FACTOR_THRESHOLD_AND_WHOLE_FAMILY_20_21_BOUND
MERGED_4BM_CROSS_DECOMPOSITION_IMPORTED=true
MERGED_4BQ_FIRST_FULL_POST_LOCAL_SAVING_IMPORTED=true
CROSS_WEIGHTED_THRESHOLD_DELTA=1/21
CROSS_SECTOR_BOUND=B^(20/21+o(1))
CROSS_SECTOR_IMPROVEMENT_OVER_61_63=1/63
CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=20/21
CUMULATIVE_POST_LOCAL_SAVING_FROM_41_42=1/42
FULL_DIRECT_POST_LOCAL_POSITIVE_SAVING_PROVED=true
REMAINING_GAP_TO_SQRT=19/42
SQRT_B_UPPER_BOUND_PROVED=false
SQRT_B_ASYMPTOTIC_PROVED=false
NEXT=Stage14-4bs
```
