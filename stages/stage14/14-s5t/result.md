# Stage14-s5t — optimize the s5 saving budget and identify the real bottleneck

## Purpose

Stage14-s5s converted the closed local-character average of s5r into the first unconditional physical-base power-saving upper bound

```text
#Q_B^phys << B^(399/400+epsilon).
```

That exponent inherited the deliberately conservative `M^(-1/200)` graph-escape saving from s5o.  The purpose of s5t is to determine whether `1/200` is structural or merely bookkeeping.

It is bookkeeping.

Without changing any analytic theorem used in s5o--s5r, one can retune the two graph thresholds and improve the uniform Euclid-scale saving from

```text
M^(-1/200+epsilon)
```

to

```text
M^(-1/41+epsilon).
```

The corresponding physical-cutoff upper bound improves from

```text
B^(399/400+epsilon)
```

to

```text
B^(81/82+epsilon).
```

The value `1/41` is the exact optimum **inside the current three-case s5o escape architecture with the existing crude all-short modulus-tuple summation**.  It is not asserted to be an arithmetic barrier.  In fact the optimizer shows that the next bottleneck is precisely the all-short periodic bookkeeping, not a reciprocal-character resonance.

No new external theorem is used.

---

## 1. General thresholds

Work on a regular Euclid box of physical scale `M`, so area is `asymp M^2` and perimeter is `asymp M`.

Replace the concrete s5o thresholds by

```text
S = M^sigma,
L = M^lambda,
```

where

```text
0 < sigma < lambda < 1.
```

`S` is the long-neighbor threshold.  `L` is the very-long-vertex threshold used when no long-long edge exists.

The K4 graph still has maximum degree three.

---

## 2. Case A — a long-long edge

If an active reciprocal edge has both endpoints at least `M^sigma`, the freeze-one-edge quadratic large sieve gives relative saving

```text
delta_A = sigma/2.
```

Indeed the relative factor is

```text
sqrt(1/U_i + 1/U_j) <= M^(-sigma/2).
```

No other active graph variables change this exponent, by s5p/s5q Hilbert contraction.

---

## 3. Case B — no long-long edge, but a very-long vertex

Assume there is no long-long edge and some active vertex has size

```text
U_i >= M^lambda.
```

Every neighbor is then shorter than `M^sigma`.  Since the degree is at most three, the product conductor seen from `i` satisfies

```text
Q_i <= M^(3 sigma).
```

The s5n squarefree completion lemma gives relative factor

```text
U_i^(-1/2) Q_i^(1/4)
 <= M^(-lambda/2 + 3 sigma/4).
```

Thus the Case-B saving is

```text
delta_B = lambda/2 - 3 sigma/4.
```

We require `delta_B>0`, equivalently `lambda>3 sigma/2`.

---

## 4. Case C — every active graph variable is below the very-long threshold

Now every active variable is below `M^lambda`.  There are at most four active vertices, so the product modulus and the number of modulus tuples satisfy the same crude s5o bounds

```text
Q <= M^(4 lambda),
#tuples <= M^(4 lambda).
```

For one fixed tuple, the centered periodic estimate is

```text
O_epsilon(B^epsilon (M Q + Q^2)).
```

Summing it crudely over all tuples gives

```text
O_epsilon(B^epsilon [M^(1+8 lambda) + M^(12 lambda)]).
```

Relative to `M^2`, the two savings are

```text
delta_C1 = 1 - 8 lambda,
delta_C2 = 2 - 12 lambda.
```

The first term is the relevant one at the optimum below.

---

## 5. Exact optimization

The uniform saving delivered by this architecture is

```text
delta(sigma,lambda)
 = min(
     sigma/2,
     lambda/2 - 3 sigma/4,
     1 - 8 lambda,
     2 - 12 lambda
   ).
```

At an interior optimum, improving one of the first three bottlenecks while leaving another smaller is impossible.  Hence set

```text
sigma/2
 = lambda/2 - 3 sigma/4
 = 1 - 8 lambda.
```

The first equality gives

```text
lambda = 5 sigma/2.
```

Write the common saving as

```text
delta = sigma/2.
```

Then

```text
sigma = 2 delta,
lambda = 5 delta.
```

The third equality becomes

```text
delta = 1 - 40 delta,
```

so

```text
boxed: delta = 1/41,
boxed: sigma = 2/41,
boxed: lambda = 5/41.
```

At these values,

```text
delta_A = 1/41,
delta_B = 1/41,
delta_C1 = 1/41,
delta_C2 = 22/41.
```

Thus all three actual escape mechanisms meet exactly at the same limiting exponent.

### Optimality within the present architecture

This is not just a convenient choice.

If `lambda < 5 sigma/2`, then `delta_B < delta_A`; increasing `lambda` improves the B bottleneck until equality is reached, while the all-short loss remains the only counter-pressure.

If `lambda > 5 sigma/2`, then `delta_A < delta_B`; decreasing `lambda` improves the all-short sector without worsening A until equality is reached.

Once `lambda=5 sigma/2`, balancing `delta_A` with `delta_C1` forces exactly `sigma=2/41`.

Therefore

```text
sup delta(sigma,lambda) = 1/41
```

for the existing three-case proof with the current crude all-short tuple summation.

---

## 6. Compatibility with s5n boundary estimates

The optimized graph saving must not undercut earlier single-edge boundary sectors.

The previously proved regular-box savings include

```text
s5l linear central                : M^(-1/5)
s5n small/medium linear           : M^(-1/10)
s5n switched-large linear         : M^(-1/20)
s5n double-switched corner        : M^(-1/5)
s5r root-spacing far sector       : M^(-3/20)
```

and

```text
1/41 < 1/20.
```

Hence none of those sectors becomes the new bottleneck.

---

## 7. Compatibility with the s5r near-area E sector

The only place where s5r explicitly used the old s5o parameter `eta=1/100` was the near-area Case B in which every other linear neighbor is short.

With the optimized long threshold

```text
sigma = 2/41,
```

the product of the at-most-three other linear conductors satisfies

```text
q_0 <= M^(3 sigma) = M^(6/41).
```

The s5r mixed squarefree Gauss-completion exponent becomes

```text
73/40 + 3 sigma/4
 = 73/40 + 3/82
 = 3053/1640
 < 2.
```

Thus that sector still saves

```text
2 - 3053/1640
 = 227/1640
 > 1/41.
```

If another long linear neighbor exists, the optimized Case-A graph escape gives exactly `M^(-1/41)`.

Therefore the complete E-transition closure of s5r remains valid with the improved global budget.

---

## 8. Improved actual local-system theorem

Combining s5q tensor contraction, s5r root-sawtooth closure, and the optimized graph budget gives on every regular Stage14 Euclid box

```text
N_local(M)
 <<_epsilon
 M^(2 - 1/41 + epsilon).
```

This concerns the actual complete finite local 2-descent character system of s5f, not the stronger arbitrary-coefficient candidate of s5g.

Hence

```text
ACTUAL_LOCAL_SYSTEM_SAVING_EXPONENT = 1/41.
```

The old `1/200` value is superseded as a conservative bookkeeping choice.

---

## 9. Improved physical-base upper bound

Stage14-s5s proved the one-sided implication

```text
physical hit below B
 => locally soluble supported descent class,
```

and the Euclid scale conversion

```text
M <= B^(1/2).
```

Therefore

```text
#Q_B^phys
 <<_epsilon
 (B^(1/2))^(2 - 1/41 + epsilon)
 = B^(1 - 1/82 + epsilon)
 = B^(81/82 + epsilon).
```

The subpolynomial per-base cover multiplicity from s2 remains absorbed into `epsilon`.

Thus

```text
ACTIVE_PHYSICAL_BASE_UPPER_BOUND_EXPONENT = 81/82.
```

This is still far from the observed/sought square-root scale `B^(1/2)`, but it is a substantial quantitative improvement obtained without adding a new analytic theorem.

---

## 10. What is now the real bottleneck?

The optimization is diagnostic.

At the optimum, the three equal losses are

```text
long-long QLS edge            : 1/41,
very-long/small-neighbor completion : 1/41,
all-short periodic tuple sum  : 1/41.
```

The first two are genuine uses of square-root/quarter-power character estimates.  The third, however, comes from the deliberately crude bound

```text
#tuples <= M^(4 lambda)
```

followed by absolute summation of the centered periodic estimate over every tuple.

Later stages s5p/s5q proved much stronger information that s5o did not yet possess:

```text
auxiliary state collision energy costs only B^epsilon,
global local-Fourier coefficient ell^2 energy is bounded,
state-split E Walsh expansion is ell^2-contractive.
```

Therefore `1/41` should **not** be interpreted as a structural arithmetic barrier.  The next plausible improvement is to revisit only the all-short periodic sector using the later Hilbert/Fourier energy machinery instead of tuplewise absolute summation.

That is a single focused problem, not a reopening of the entire s5 analysis.

---

## 11. Stage-boundary decision

s5t therefore answers the question posed by s5s:

```text
old 1/200 bottleneck structural?       no
old 1/200 bottleneck bookkeeping?      yes
same architecture optimized?           yes, to 1/41
new arithmetic resonance discovered?   no
analysis tree reopening?                no
```

A further improvement beyond `1/41` requires changing only the all-short aggregation step, most naturally by using the s5q Fourier-energy contraction.  If that refinement does not materially change the exponent, s5 should be closed and the square-root-scale problem passed to s6 rather than spawning indefinite s5 substages.

---

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
NEXT=Stage14-s5u use the s5q Fourier/Hilbert energy to replace the all-short tuplewise absolute sum, then either improve the exponent once more or close s5 and hand the square-root-scale gap to s6
```
