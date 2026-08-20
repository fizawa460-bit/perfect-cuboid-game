# Stage27-19-r7b — SR-STR-169 correlation-adapter test after r6d compression

```text
TASK_ID=Stage27-19-r7b
PARENT=Stage27-19-r7a
CARD=SR-STR-169
CHECKPOINT=40
CURRENT_MU=1/2
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
```

The receiver change from r6d removes polynomial multiplicity inside a fixed `(p,q,g)` core.  Hence the dyadic mass can be written, up to `B^{o(1)}`, as the nonnegative incidence count

\[
M_T=\sum_{(p,q)}\sum_{g\ll B^2/T} I_T(p,q,g),\qquad I_T\in\{0,1\},
\]

where `I_T(p,q,g)=1` iff at least one physical Stage19 realization exists.

This is a genuine simplification relative to the old Stage14 `H_phys^MAIN` sparse-weight receiver: the pushforward coefficient at each core is subpower.  However SR-STR-169's quantitative weapons are signed/correlation mechanisms.  To use them one must further represent `I_T` (or a centered version) as a bilinear/multivariable arithmetic correlation on variables with theorem-compatible independent coefficient structure.

The core equations show that a realization is equivalent to the existence of square divisors `s^2|pg`, `n^2|qg` satisfying

\[
pg/s^2-n^2=\square,\qquad qg/n^2+s^2=\square,
\]

plus the physical masks.  Expanding either square condition by quadratic characters, additive Fourier detection, or square-sieve weights reintroduces a nontrivial detector whose coefficients are coupled through the same `(p,q,g,n,s)` variables.  No repo-native identity turns the nonnegative support indicator into a separated signed correlation with zero fixed-power loss.

Therefore r6d removes the old polynomial **weight** obstruction but not the decisive **correlation adapter** obstruction.  The old Work failure is not blindly inherited; it is re-tested and narrowed to the exact new statement:

```text
FIRST_MISSING_ADAPTER=R402HCoreIncidenceToSeparatedSignedCorrelation
```

A sufficient adapter would express every dyadic `M_T` or its second moment as `B^{o(1)}` theorem-compatible signed bilinear/multivariable forms while preserving the exact physical masks and without reusing Stage15 squareclass or earlier spacing savings.

No such adapter is currently proved.  Hence SR-STR-169 remains an external gate for the r402h receiver, but for a strictly narrower reason than before.

```text
R6D_SUBPOWER_PUSHFORWARD_WEIGHT_TRANSFER=PASS
OLD_STAGE14_POLYNOMIAL_WEIGHT_OBSTRUCTION_REMOVED=true
SIGNED_CORRELATION_ADAPTER_PROVED=false
SR169_DIRECT_THEOREM_IMPORT_LEGAL=false
SR169_R402H_STATUS=EXTERNAL_GATE_NARROWED
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
ADVANCE_TO_CHECKPOINT50=false
NEXT_DERIVED_ROUTE=27-19-r7c
NEXT_TARGET=SR161_ONE_VARIABLE_SEPARATION_OR_L2_COVARIANCE_REDUCTION
```
