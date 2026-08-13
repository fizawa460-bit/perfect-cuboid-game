# Stage14-4dg

Stage14-4dg consumes merged `Stage14-4df`, merged `Stage14-s7-48`, and merged frozen `Stage14-sH48`.

The six-block square-root receiver is rewritten in primitive rotated coordinates

```text
m=D+A,
n=D-A,
mn = epsilon_- u_* R J,
m^2+n^2 = 2 epsilon_+ C_* S T.
```

For a fixed primitive quarter-pair `(m,n)`, the admissible plus and minus balanced cell factorizations are divisor-many.  Let `W_+(m,n)` and `W_-(m,n)` count those side-specific factorizations after all inherited scale, squarefree, pairwise-separation, and local physical masks are imposed.  Up to the already-frozen `B^o(1)` completion multiplicity, the physical saturation count is bounded by

```text
I(B)=sum W_+(m,n) W_-(m,n).
```

Writing `mu_+` and `mu_-` for the averages of the two weights over the primitive quarter-pair base gives the exact identity

```text
I(B)
 = |P_B| mu_+ mu_-
 + sum (W_+-mu_+)(W_--mu_-).
```

This identifies two logically separate tasks.  A centered dispersion estimate controls the covariance term, but it does not remove the principal density term.  Merged `sH48` certifies that the currently available one-sided balanced-divisor and sum-of-two-squares results do not give a uniform fixed `B`-power saving for that principal marginal product.

Therefore the next mainline receiver is

```text
ConditionallyCenteredPrimitiveQuarterPairProductNormDualBalancedCellFactorizationDispersionWithPrincipalDensityControl
```

and not merely an unqualified centered dispersion problem.

The whole-family exponent remains `1/2`.  No new mainline H is requested before an explicit conditional/local centering adapter and its principal density are constructed.

Next mainline stage: `Stage14-4dh`.
