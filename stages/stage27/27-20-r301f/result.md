# Stage27-20-r301f — exact torus factorization of the space-diagonal branch

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PREFLIGHT
PARENT_ROUTE=Stage27-20-r301e

## 1. Frozen torus coordinates

On the audited Stage14-e two-face torus, for `i=1,2`,

\[
t_i=\frac{q_i-q_i^{-1}}2,
\qquad
h_i=\frac{q_i+q_i^{-1}}2,
\qquad q_i\in\mathbf Q_{>0}^*.
\]

The Stage27 space-diagonal completion condition is

\[
1+t_1^2+t_2^2=w^2.
\]

## 2. Exact factorization

Substitute the torus coordinates and clear the square denominator `4 q_1^2 q_2^2`.  Direct expansion gives

\[
\begin{aligned}
4q_1^2q_2^2(1+t_1^2+t_2^2)
&=4q_1^2q_2^2
+q_2^2(q_1^2-1)^2
+q_1^2(q_2^2-1)^2\\
&=(q_1^2+q_2^2)(q_1^2q_2^2+1).
\end{aligned}
\]

Hence

\[
\boxed{
1+t_1^2+t_2^2
=\frac{(q_1^2+q_2^2)(q_1^2q_2^2+1)}{4q_1^2q_2^2}
}.
\]

Because the denominator is already a rational square, the space-diagonal condition is exactly

\[
\boxed{
(q_1^2+q_2^2)(q_1^2q_2^2+1)\in(\mathbf Q^*)^2.
}
\]

This factorization is target-specific and is not the Stage20 third-face branch equation.

## 3. Squareclass receiver

Put

\[
A=q_1^2+q_2^2,
\qquad
B=q_1^2q_2^2+1.
\]

On the physical positive locus, `A,B>0`.  The condition `AB` square is equivalent to equality of their classes in

\[
\mathbf Q^*/(\mathbf Q^*)^2.
\]

Equivalently there is a positive squareclass `d` and rational `r,s` such that

\[
A=d r^2,
\qquad
B=d s^2.
\]

No boundedness, finiteness, or sparsity theorem for the varying squareclass `d` is claimed here.  The point is to replace a generic K3-cover statement by an exact arithmetic receiver with two coupled norm-type factors.

Over `Q(i)` the two factors split as

\[
q_1^2+q_2^2=(q_1+i q_2)(q_1-i q_2),
\]

\[
q_1^2q_2^2+1=(q_1q_2+i)(q_1q_2-i).
\]

Thus the next legal route is a squareclass / Gaussian-norm analysis on the actual space-diagonal cover, with the primitive physical height ledger retained.

## 4. Stage20 route status

The transferred local sieve in r301e is valid but polynomially dominated by the existing half-power theorem.  The useful new output of the Stage20 reentry is therefore not a stronger bound yet, but the K3-cover identification plus this exact factorized receiver.

A future strict improvement must do at least one of:

1. prove a fixed-power restriction on the squareclass support;
2. prove a uniform fixed-power saving inside one squareclass fiber;
3. couple the factorized receiver to the existing half-power representation without double-charging an already-used variable;
4. produce an equivalent theorem giving `mu<1/2` on the same physical population.

```text
STAGE27_20_R301F_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
SPACE_DIAGONAL_TORUS_FACTORIZATION_PROVED=true
SPACE_DIAGONAL_SQUARECLASS_RECEIVER_DERIVED=true
GAUSSIAN_NORM_FACTOR_STRUCTURE_IDENTIFIED=true
SQUARECLASS_SUPPORT_FIXED_POWER_BOUND_PROVED=false
SQUARECLASS_FIBER_FIXED_POWER_SAVING_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEXT_DERIVED_ROUTE=27-20-r301g
```
