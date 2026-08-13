# Stage14-s5t — optimize the s5 saving budget

## Purpose

Stage14-s5s converted the closed local-character average into the unconditional physical-base bound

```text
#Q_B^phys << B^(399/400+epsilon),
```

using the deliberately conservative `M^(-1/200)` graph saving from s5o.  This stage asks whether `1/200` is structural.

It is not.  The same three-case s5o architecture, with no new analytic theorem, optimizes to

```text
M^(-1/41+epsilon),
```

and therefore

```text
#Q_B^phys << B^(81/82+epsilon).
```

The value `1/41` is optimal only within the current three-case architecture with its existing crude all-short modulus-tuple summation.  It is not claimed to be an arithmetic barrier.

## General thresholds

Let

```text
S=M^sigma
```

be the long-neighbor threshold and

```text
L=M^lambda
```

be the very-long-vertex threshold.

### Case A: long-long edge

If an active reciprocal edge has both endpoints at least `M^sigma`, freeze the other variables and use the quadratic large sieve.  The relative saving is

```text
delta_A=sigma/2.
```

### Case B: no long-long edge, but a very-long vertex

If no long-long edge exists and an active vertex has size at least `M^lambda`, then all of its at-most-three neighbors are shorter than `M^sigma`.  Their product conductor satisfies

```text
Q_i <= M^(3 sigma).
```

The s5n squarefree completion lemma gives

```text
U_i^(-1/2)Q_i^(1/4)
 <= M^(-lambda/2+3 sigma/4),
```

so

```text
delta_B=lambda/2-3 sigma/4.
```

### Case C: all active variables below `M^lambda`

There are at most four active vertices.  The same crude s5o ledger gives

```text
Q <= M^(4 lambda),
#tuples <= M^(4 lambda).
```

For one centered periodic tuple,

```text
O_epsilon(B^epsilon(MQ+Q^2)).
```

Absolute summation over all tuples yields

```text
O_epsilon(B^epsilon[M^(1+8lambda)+M^(12lambda)]).
```

Relative to the physical `M^2` scale,

```text
delta_C1=1-8lambda,
delta_C2=2-12lambda.
```

## Exact optimization

Thus

```text
delta(sigma,lambda)
=min(
  sigma/2,
  lambda/2-3sigma/4,
  1-8lambda,
  2-12lambda
).
```

At the optimum the first three active bottlenecks balance:

```text
sigma/2
=lambda/2-3sigma/4
=1-8lambda.
```

The first equality gives

```text
lambda=5sigma/2.
```

Writing the common saving as `delta=sigma/2` gives

```text
sigma=2delta,
lambda=5delta.
```

Then

```text
delta=1-40delta,
```

hence

```text
delta=1/41,
sigma=2/41,
lambda=5/41.
```

At these values,

```text
delta_A=1/41,
delta_B=1/41,
delta_C1=1/41,
delta_C2=22/41.
```

For `lambda<5sigma/2`, Case B is smaller than Case A and improves as `lambda` increases.  For `lambda>5sigma/2`, Case A is smaller and lowering `lambda` improves the all-short sector without worsening Case A.  Therefore the optimum of this architecture occurs at `lambda=5sigma/2`; balancing Case A with Case C then forces `sigma=2/41`.

So

```text
sup delta(sigma,lambda)=1/41
```

within the present three-case proof.

## Compatibility with the already-closed sectors

Earlier regular-box savings are all larger:

```text
s5l linear central         : 1/5
s5n small/medium           : 1/10
s5n switched-large         : 1/20
s5n double-switched corner : 1/5
s5r root-spacing far       : 3/20
```

and `1/41<1/20`, so none becomes a new bottleneck.

The s5r near-area mixed-completion sector also remains safe.  With `sigma=2/41`, the product of the other at-most-three short linear conductors is

```text
q_0 <= M^(6/41).
```

Its exponent becomes

```text
73/40+3sigma/4
=73/40+3/82
=3053/1640
<2,
```

which saves

```text
227/1640 > 1/41.
```

Hence the full E-transition closure from s5r survives the optimized thresholds.

## Improved local-system theorem

The complete actual finite local 2-descent character system therefore satisfies on regular Euclid boxes

```text
N_local(M)
 <<_epsilon M^(2-1/41+epsilon).
```

This does not promote the stronger arbitrary-coefficient s5g large-sieve candidate.

## Physical cutoff

Stage14-s5s proved

```text
physical hit below B
 => locally soluble supported descent class
```

and

```text
M<=B^(1/2).
```

Therefore

```text
#Q_B^phys
 <<_epsilon
 (B^(1/2))^(2-1/41+epsilon)
 =B^(81/82+epsilon).
```

The subpolynomial per-base cover multiplicity remains absorbed in `epsilon`.

## Real bottleneck after optimization

The old `1/200` loss was bookkeeping.  At the optimized point three losses meet at `1/41`:

```text
long-long QLS edge,
very-long/small-neighbor completion,
all-short periodic tuple summation.
```

The first two are genuine character estimates.  The third comes from the crude absolute bound

```text
#tuples <= M^(4lambda)
```

followed by tuplewise summation.

But later stages s5p/s5q already proved stronger energy information:

```text
auxiliary collision energy costs only B^epsilon,
global local-Fourier coefficient ell^2 energy is bounded,
E-Walsh expansion is ell^2-contractive.
```

So `1/41` is not identified as an arithmetic resonance.  The only focused refinement left inside s5 is to replace the all-short tuplewise absolute sum by the later Hilbert/Fourier energy machinery.

If that does not materially improve the exponent, s5 should close and the square-root-scale problem should move to s6 rather than spawning indefinite substages.

## Boundary

```text
STAGE14_S5T=COMPLETE_SAVING_BUDGET_OPTIMIZATION_AND_ALL_SHORT_BOTTLENECK_ISOLATION
OLD_GRAPH_SAVING_1_OVER_200_STRUCTURAL=false
GRAPH_ESCAPE_GENERAL_THRESHOLD_LEDGER_PROVED=true
GRAPH_ESCAPE_OPTIMAL_SIGMA=2/41
GRAPH_ESCAPE_OPTIMAL_LAMBDA=5/41
GRAPH_ESCAPE_OPTIMAL_SAVING=1/41
OPTIMAL_WITHIN_CURRENT_THREE_CASE_ARCHITECTURE=true
S5R_E_TRANSITION_COMPATIBLE_WITH_OPTIMIZED_THRESHOLDS=true
ACTUAL_LOCAL_SYSTEM_POWER_SAVING_EXPONENT=1/41
ACTIVE_PHYSICAL_BASE_UPPER_BOUND_EXPONENT=81/82
ACTIVE_PHYSICAL_BASE_POWER_SAVING_UPPER_BOUND_IMPROVED=true
ALL_SHORT_ABSOLUTE_TUPLE_SUM_IS_CURRENT_BOTTLENECK=true
NEW_ARITHMETIC_RESONANCE_FOUND=false
FAMILY_LARGE_SIEVE_THEOREM_PROVED=false
GLOBAL_SOLUBILITY_AVERAGED=false
SMALL_POINT_DISTRIBUTION_PROVED=false
SQRT_B_ASYMPTOTIC_PROVED=false
S5T_SUBSTAGE_SPLIT_REQUIRED=false
NEXT=Stage14-s5u
```
