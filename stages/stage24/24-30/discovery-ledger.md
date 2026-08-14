# Stage24-30 discovery ledger

CHECKPOINT=30
ROLE=THEOREM_LEVEL_SURVIVOR_LAW
SEARCH_STATUS=COMPLETE_FOR_CHECKPOINT30

## Search targets

The checkpoint30 policy required more than the first quotient bound. The search therefore covered:

1. Stage18 absolute source theorem and directional asymptotics;
2. Stage19 whole-family upper theorem and local squareclass zero-density theorem;
3. Stage15 toric/thin-set machinery behind the Stage18 denominator;
4. leading-constant availability;
5. directional refinements;
6. independent proof routes for Stage18 -> Stage19 zero density;
7. checkpoint20 / r202 million-scale finite evidence as diagnostics only.

## Source-level findings

### D30-1 quantitative quotient route

Frozen interfaces:

- `M2(B) ~ C_M2 B(log B)^5`, `C_M2>0`;
- `N2(B) <<_epsilon B^(1/2+epsilon)`.

Because Stage19 is literally Stage18 intersect `{R integral}` under the same cutoff and object measure,

`N2(B)/M2(B) <<_epsilon B^(-1/2+epsilon)(log B)^(-5) -> 0`.

No adapter or multiplicity factor occurs.

### D30-2 leading-constant search

Stage15-2b identifies `C_M2` as a positive toric/Tamagawa chamber constant and proves

`C_M2=C_a+C_b+C_c`, with each `C_j>0`.

However Stage15-2b explicitly records `M2_ASYMPTOTIC_CONSTANT_EXPLICIT=false`; no closed numerical formula for `C_M2` or the directional constants is frozen. The Stage14 numerator bound also has only an implicit `epsilon`-dependent constant. Therefore checkpoint30 cannot print a rigorous leading constant for the quantitative survivor upper bound.

Finite estimates such as `M2(1m)/(1m (log 1m)^5)` are diagnostic and are not substituted for `C_M2`.

### D30-3 directional quantitative refinement

Stage15 proves

`M2,j(B) ~ C_j B(log B)^5`, `C_j>0`, for `j=a,b,c`.

Since `N2,j(B)<=N2(B)`, each direction satisfies

`N2,j(B)/M2,j(B) <<_{epsilon,j} B^(-1/2+epsilon)(log B)^(-5) -> 0`.

This proves direction-by-direction zero relative density but not directional survivor constants or ordering.

### D30-4 inherited independent local-sieve route

Stage19/Stage15 supply the exact squareclass event

`R integral iff sf(A)=sf(B)`.

For good split primes `p=1 mod 4`, local acceptance is `rho_p=1-4/p+O(p^-2)`. Taking `B->infinity` for each fixed finite prime set before enlarging that set gives independently

`N2(B)/M2(B)->0`.

This is a causal zero-density theorem, not the source of the half-power quantitative rate.

### D30-5 new thin-cover route

The Stage18 shared-edge toric surface has equations

`u^2=e^2+x^2`, `v^2=e^2+y^2`.

Adjoin the space-diagonal square root

`w^2=e^2+x^2+y^2`.

Over the geometric function field,

`e^2+x^2+y^2 = u^2+y^2 = (u+i y)(u-i y)`.

On a generic component of the divisor `u+i y=0` in the dense torus with `y!=0`, the other factor is nonzero, so the valuation of the radicand is one. Hence the radicand is not a square in the geometric function field. The double cover is therefore geometrically integral and generically degree two.

Its rational image in the Stage18 torus is a type-II thin subset. Stage15-2b already verifies the almost-Fano/equidistribution hypotheses on the same toric resolution and anticanonical height `R`, and invokes Browning-Loughran thin-set zero density. Thus the space-integral Stage19 points satisfy

`N2(B)=o(B(log B)^5)`

and consequently

`N2(B)/M2(B)->0`.

This route is independent of both the Stage14 half-power upper theorem and the split-prime squareclass sieve. It supplies no effective fixed-power saving.

The same global thin-image bound plus `M2,j(B)~C_j B(log B)^5` also gives `N2,j/M2,j->0` for each direction.

## Numerical consistency only

Checkpoint20 exact matched census reaches

`B=1,000,000: M2=13,817,725, N2=255, ratio=1.8454557461521345e-5`.

Directional finite survivor ratios are approximately

- a: `2.1338972629e-5`;
- b: `1.7363540622e-5`;
- c: `1.6429982018e-5`.

The observed order `a>b>c` is not promoted to a limiting statement. The finite effective ratio slope changes materially between the 1k->100k and 100k->1m windows, so no empirical power is promoted.

## Checkpoint30 boundary

PROVED_QUANTITATIVE_RATIO=true
PROVED_RATIO_ZERO_DENSITY=true
PROVED_DIRECTIONAL_ZERO_DENSITY=true
INDEPENDENT_ZERO_DENSITY_ROUTES=3
ROUTE_1=WHOLE_FAMILY_UPPER_DIVIDED_BY_SOURCE_ASYMPTOTIC
ROUTE_2=FIXED_PRIME_SQUARECLASS_SIEVE
ROUTE_3=GEOMETRICALLY_INTEGRAL_SPACE_SQUARE_DOUBLE_COVER_THIN_IMAGE
LEADING_CONSTANT_EXPLICIT=false
TRUE_RATIO_EXPONENT_IDENTIFIED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
HALF_POWER_INTRINSIC_PROVED=false
FINITE_DATA_USED_AS_PROOF=false
