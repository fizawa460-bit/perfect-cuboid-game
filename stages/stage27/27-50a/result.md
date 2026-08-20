# Stage27-50a — inherited-bracket synthesis after checkpoint40 override

```text
TASK_ID=Stage27-50a
PARENT=Stage27-50
ROUTE_KIND=MAINLINE_SYNTHESIS
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
INHERITED_LOWER_EXPONENT=1/4
INHERITED_UPPER_EXPONENT=1/2_PLUS_EPSILON
TRUE_N2_EXPONENT_IDENTIFIED=false
```

Checkpoint50 begins from the operator-authorized inherited bracket

\[
B^{1/4-o(1)}\lesssim N_2(B)\lesssim B^{1/2+o(1)}.
\]

The purpose of this checkpoint is not to reopen Stage19. It is to classify every downstream Stage27 statement according to which level of exponent knowledge it actually needs.

## A. Statements valid from the bracket alone

The following remain certified without knowing the true exponent:

1. `N_2(B)` is polynomially large along the certified lower construction scale, with exponent at least `1/4-o(1)`;
2. `N_2(B)` is strictly sublinear, with the available upper scale at most `B^{1/2+o(1)}`;
3. any comparison whose conclusion is monotone over the whole interval `[1/4,1/2]` may proceed using interval arithmetic;
4. any downstream claim requiring only separation from exponent `0` or exponent `1` may proceed;
5. finite-range diagnostics such as the previously recorded effective slope near `0.421...` remain diagnostic only and cannot replace the interval.

## B. Statements that require the true exponent

The following must remain unresolved:

1. an equality `N_2(B)=B^{\alpha+o(1)}` with identified `\alpha`;
2. deciding whether the true exponent is exactly `1/2`, strictly below `1/2`, exactly `1/4`, or strictly above `1/4`;
3. any downstream comparison whose sign changes somewhere inside `[1/4,1/2]`;
4. any claim that promotes a finite-range fitted slope to an asymptotic exponent.

## C. Comparison protocol

For a downstream quantity with certified exponent interval `[L,U]`, comparison against `N_2` is allowed only if interval ordering is strict:

- if `U_other < 1/4`, then `N_2` is asymptotically larger on exponent scale;
- if `L_other > 1/2`, then `N_2` is asymptotically smaller on exponent scale;
- otherwise the comparison is unresolved unless a stronger one-sided theorem is available.

Thus Checkpoint50 can legally continue with interval-valued exponent calculus rather than forcing a point estimate.

## D. Stage27-19 freeze semantics

The Stage19 reentry branches r5/r6/r402/r7/r8/r9/r10 are archived as theorem/construction attempts. They do not block Checkpoint50. They may be reopened only after genuinely new input that addresses one of the explicit surviving receivers; merely renaming an old gate is forbidden.

```text
BRACKET_ONLY_SYNTHESIS_PROVED=true
INTERVAL_EXPONENT_CALCULUS_ENABLED=true
POINT_EXPONENT_CLAIMS_FORBIDDEN=true
FINITE_SLOPE_REMAINS_DIAGNOSTIC_ONLY=true
STAGE19_REENTRY_BLOCKS_MAINLINE=false
NEXT_DERIVED_ROUTE=27-50b
ADVANCE_TO_CHECKPOINT60=false
```
