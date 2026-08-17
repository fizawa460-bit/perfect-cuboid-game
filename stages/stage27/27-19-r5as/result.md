# Stage27-19-r5as — double-Pell compression after fixing the self-generated kernel

```text
TASK_ID=Stage27-19-r5as
SOURCE_STAGE=Stage19
TRIGGER_CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PARALLEL
PARENT_ROUTE=Stage27-19-r5ar
STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
```

The residual squareclass equations are

\[
a c_s^2\sigma^2+b c_n^2\nu^2
=\kappa c_0^2c'^2,\tag{S1}
\]

\[
b c_0^2\mu^2+a\delta^2\sigma^2
=\kappa c_n^2w'^2,\tag{S2}
\]

\[
a c_0^2\rho^2-b\delta^2\nu^2
=\kappa c_s^2w'^2.\tag{S3}
\]

r5am proved the uniform Pell/norm-form lemma

\[
\#\{(x,y):Ax^2-By^2=N,\ x,y\le H\}
\ll_\varepsilon (ABNH)^\varepsilon
\]

uniformly in positive integer coefficients, using the maximal order of the corresponding real quadratic field.

## 1. Apply the Pell lemma to S1

Fix

\[
(a,b,\delta,c_0,c_s,c_n,\sigma,\kappa).
\]

Then S1 is

\[
\boxed{
\kappa c_0^2c'^2-b c_n^2\nu^2
=a c_s^2\sigma^2.
}
\]

All coefficients and solution heights are polynomially bounded in \(B\) on the existing Stage27 physical-height support. Hence the r5am uniform lemma gives

\[
\boxed{
\#\{(\nu,c')\}\ll_\varepsilon B^\varepsilon.
}
\]

No moving-rank assumption is used.

## 2. Apply the same lemma independently to S2

With the same fixed coefficient tuple, S2 is

\[
\boxed{
\kappa c_n^2w'^2-b c_0^2\mu^2
=a\delta^2\sigma^2.
}
\]

Therefore

\[
\boxed{
\#\{(\mu,w')\}\ll_\varepsilon B^\varepsilon.
}
\]

The two Pell counts may be multiplied for an upper bound. Compatibility with the common Stage19 data can only reduce the count.

## 3. S3 completes rho uniquely

After \((\nu,w')\) is known, S3 gives

\[
\rho^2=
\frac{\kappa c_s^2w'^2+b\delta^2\nu^2}
{a c_0^2}.
\]

Thus there is at most one positive integer \(\rho\).

Consequently:

**Double-Pell completion theorem.** For fixed

\[
\boxed{(a,b,\delta,c_0,c_s,c_n,\sigma,\kappa)},
\]

the number of Stage19 residual completions

\[
(\nu,c',\mu,w',\rho)
\]

is

\[
\boxed{B^{o(1)}}.
\]

This strengthens the usefulness of the r5am compression on the small-kappa side: one no longer needs to fix \(\nu\); fixing the self-generated kernel \(\kappa\) replaces it.

## 4. Small-kappa consequence and remaining support problem

For \(\kappa\le K\), summing over the possible kernels gives, for each fixed seven-tuple

\[
(a,b,\delta,c_0,c_s,c_n,\sigma),
\]

at most

\[
\boxed{K B^{o(1)}}
\]

residual completions.

This is useful only if the number of admissible seven-tuples is controlled with a power saving. That global outer-support theorem is not proved here.

```text
DOUBLE_PELL_COMPRESSION_PROVED=true
S1_UNIFORM_PELL_COUNT_PROVED=true
S2_UNIFORM_PELL_COUNT_REUSED=true
FIXED_ABDELTA_C0CSCN_SIGMA_KAPPA_COMPLETIONS=B^o(1)
SMALL_KAPPA_PER_SEVEN_OUTER_CELL_BOUND=K*B^o(1)
UNIFORM_MORDELL_WEIL_RANK_ASSUMED=false
SEVEN_OUTER_CELL_FIXED_POWER_COUNT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
NEXT_DERIVED_ROUTE=27-19-r5at
NEXT_TARGET=SEVEN_OUTER_CELL_SUPPORT_COUNT_OR_SELF_GENERATED_KAPPA_AVERAGE
```
