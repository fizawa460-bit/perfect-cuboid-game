# Stage27-19-r7c — SR-STR-161 one-variable separation / L2 covariance test

```text
TASK_ID=Stage27-19-r7c
PARENT=Stage27-19-r7b
CARD=SR-STR-161
CHECKPOINT=40
CURRENT_MU=1/2
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
```

SR-STR-161 is usable only after genuine one-variable coefficient separation (or an L2/covariance reduction producing such blocks).  On a fixed core `(p,q,g)`, r6d gives the exact reconstruction conditions

\[
s^2\mid pg,\quad n^2\mid qg,
\]

\[
pg/s^2-n^2=m^2,\qquad qg/n^2+s^2=r^2.
\]

A naive character expansion of the two square conditions produces symbols whose moduli/arguments both depend on the shared divisor variables `n,s` and the same core `(p,q,g)`.  In particular the natural coefficient matrix is correlated rather than a product `alpha_u beta_v`, and fixing one of `n,s` merely moves the dependence into the other square condition.  The divisor-many number of fixed-core witnesses is `B^{o(1)}`, but this does not by itself furnish cancellation across the polynomially many realized cores.

Cauchy/Parseval can separate variables only by replacing the support problem with a second/fourth moment that still contains the same coupled square detector.  No zero-loss covariance identity in the current repository turns that moment into finitely many SR-STR-161-compatible rectangular/hyperbolic Jacobi blocks.

Hence the exact missing internal adapter is

```text
FIRST_MISSING_ADAPTER=R402HCoreSquareConditionsToSeparatedQuadraticCharacterBlocks
```

with the required properties: `B^{o(1)}` block count, original dyadic `(T,g)` quantifiers, physical masks retained, and no recharge of the Stage15 squareclass predicate.

```text
FIXED_CORE_WITNESS_ENTROPY_SUBPOWER=true
ONE_VARIABLE_COEFFICIENT_SEPARATION_PROVED=false
L2_COVARIANCE_ZERO_LOSS_REDUCTION_PROVED=false
SR161_LARGE_SIEVE_IMPORT_LEGAL=false
SR161_R402H_STATUS=EXTERNAL_GATE_NARROWED
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
ADVANCE_TO_CHECKPOINT50=false
NEXT_DERIVED_ROUTE=27-19-r7d
NEXT_TARGET=R7_SYNTHESIS_AND_ROUTE_SELECTION
```
