# Stage27-19-r5at — fixed-physical-diagonal kappa entropy collapse

```text
TASK_ID=Stage27-19-r5at
SOURCE_STAGE=Stage19
TRIGGER_CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PARALLEL
PARENT_ROUTE=Stage27-19-r5aq-r5as
STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
```

The exact r5ah physical-height factorization is

\[
R=\frac h\varepsilon\,\kappa L,
\qquad L=w'c'\ge1,
\]

with \(h/\varepsilon\in\mathbf Z_{>0}\). In particular

\[
\boxed{\kappa\mid R.}
\]

The repaired r5aq-r5as batch also gives the double-Pell completion theorem: for fixed

\[
(a,b,\delta,c_0,c_s,c_n,\sigma,\kappa)
\]

the residual completion multiplicity is \(B^{o(1)}\).

## 1. Candidate kernels at fixed physical diagonal

Fix an integer \(R\le B\). Every Stage19 squarefree kernel is a positive divisor of \(R\). Therefore

\[
\#\{\kappa:\kappa\mid R\}\le \tau(R)=B^{o(1)}.
\]

The additional facts that \(\kappa\) is squarefree and all its prime factors are \(1\pmod4\) only reduce this set.

For a dyadic range \(K\le\kappa<2K\), the same conclusion holds:

\[
\boxed{
\#\{\kappa\mid R:K\le\kappa<2K\}\le B^{o(1)}.
}
\]

Thus the factor of \(K\) that appeared in the naive varying-modulus union bound of r5ar is not intrinsic once the physical diagonal is fixed.

## 2. Fixed-seven-tuple plus fixed-R fiber

Now fix

\[
(a,b,\delta,c_0,c_s,c_n,\sigma,R).
\]

For every admissible divisor \(\kappa\mid R\), r5as gives only \(B^{o(1)}\) residual completions. Summing over at most \(\tau(R)=B^{o(1)}\) admissible kernels gives

\[
\boxed{
\#\{\text{Stage19 completions for fixed }(a,b,\delta,c_0,c_s,c_n,\sigma,R)\}
=B^{o(1)}.
}
\]

This removes the small-kappa factor `K` from r5as after conditioning on the actual physical diagonal.

Equivalently, Stage19 now has a subpower fiber over the support projection

\[
(a,b,\delta,c_0,c_s,c_n,\sigma,R).
\]

## 3. Scope

This is a fiber theorem, not yet a support theorem. There may still be many admissible pairs consisting of a seven-variable outer cell and a physical diagonal \(R\le B\). Summing the fixed-R statement over all \(R\) without a support estimate would pay a full factor \(B\).

```text
FIXED_R_KAPPA_ENTROPY_COLLAPSE_PROVED=true
KAPPA_DIVIDES_PHYSICAL_R_REUSED=true
FIXED_R_ADMISSIBLE_KAPPA_COUNT=B^o(1)
FIXED_SEVEN_OUTER_PLUS_R_COMPLETIONS=B^o(1)
SMALL_KAPPA_K_FACTOR_REMOVED_AT_FIXED_R=true
FIXED_R_SUPPORT_COUNT_FIXED_POWER_BOUND_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
NEXT_DERIVED_ROUTE=27-19-r5au
```