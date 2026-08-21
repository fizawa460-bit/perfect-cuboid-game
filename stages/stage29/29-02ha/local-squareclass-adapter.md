# Stage29-02ha — local squareclass adapter on the base plane

For every odd prime `p`, the seven-line arrangement has the same characteristic-zero incidence pattern. Inclusion–exclusion gives

\[
\#(\mathbf P^2\setminus D)(\mathbf F_p)
= (p^2+p+1)-\bigl(7(p+1)-6(3-1)-3(2-1)\bigr)
= (p-3)^2.
\]

Thus the geometric host outside the branch locus has an exact elementary point count.

For a base point

\[
q\in (\mathbf P^2\setminus D)(\mathbf F_p),
\]

the fiber has an `F_p`-point exactly when the seven nonzero values

```text
x, y, z, x+y, x+z, y+z, x+y+z
```

lie in one common quadratic-character class. Equivalently, after dividing by one reference form, all six ratios are squares in `F_p^*`.

This is the finite-field reduction of the global torsor class `delta(q)` from `exact-sign-cover-model.md`.

## What this buys downstream

It gives Stage29-09 a literal endpoint local receiver with no Gaussian-prime or angular-sector adapter:

```text
R29-KUM-LOC1=SevenLinearFormCommonSquareclassLocalDensity
R29-KUM-LOC2=BranchValuationTransitionLedgerAtBadReductionOfPhysicalPoints
```

The first is an exact character-sum problem on a fixed seven-line arrangement. The second is necessary because a hypothetical rational point may reduce onto the branch divisor at finitely many primes; zero nonbranch counts at a small prime are therefore divisibility constraints, not a global nonexistence proof.

No multiplication with earlier Stage14/15 sieve savings is permitted without a matched physical-height and measure adapter.

```text
LOCAL_HOST_COUNT=(p-3)^2_for_odd_p
LOCAL_LIFT_CRITERION=COMMON_QUADRATIC_CHARACTER
GLOBAL_NONEXISTENCE_FROM_SMALL_PRIMES=false
```
