# Stage27-19-r402c — reduced tau core-scale receiver

```text
TASK_ID=Stage27-19-r402c
OWNER_STAGE=Stage27
SOURCE_STAGE=Stage19
TRIGGER_CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY
PARENT_ROUTE=Stage27-19-r402b
STATUS=SUBMITTED_AS_MULTI_ROUTE_BATCH_PENDING_FRESH_AUDIT
STRICT_SUB_SQRT_UPPER_PROVED=false
```

For a Stage19 toric point in reduced positive slope coordinates set

\[
A=s^2(m^2+n^2),\qquad D=n^2(r^2-s^2),\qquad \tau=A/D.
\]

Write

\[
\tau=p/q,\qquad (p,q)=1,
\]

and define

\[
g=\gcd(A,D).
\]

Then canonically and exactly

\[
\boxed{A=pg,\qquad D=qg},
\]

so every realized tau value has the integer-core receiver

\[
\boxed{s^2(m^2+n^2)=pg,\qquad n^2(r^2-s^2)=qg.}
\]

Stage27-19-r402a proved on the exact physical cutoff `R<=B` that

\[
A<2B^2,\qquad D<2B^2.
\]

With `H(tau)=max(p,q)` this gives

\[
pg<2B^2,\qquad qg<2B^2
\]

and hence

\[
\boxed{g<\frac{2B^2}{H(\tau)}}.
\]

On a dyadic band `T<=H(tau)<2T`,

\[
\boxed{g\ll B^2/T}.
\]

Two Stage19 objects have the same reduced tau exactly when their primitive pairs `(p,q)` agree. Their unreduced pairs are `(A_i,D_i)=g_i(p,q)`. Thus off-diagonal same-tau collisions are organized by `(p,q,g_1,g_2)` plus two representations of the displayed core equations.

No support saving, divisor saving, representation bound, or independence assertion follows from the core-height inequality alone.

```text
REDUCED_TAU_CORE_SCALE_DERIVED=true
TAU_CORE_SCALE_GCD_DEFINED=true
TAU_CORE_EQUATIONS_PROVED=true
TAU_CORE_HEIGHT_TRADEOFF_PROVED=true
TAU_CORE_HEIGHT_BOUND=g<2B^2/H(tau)
TAU_DYADIC_CORE_BOUND=g<<B^2/T
CORE_TRADEOFF_FIXED_POWER_SAVING_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEXT_DERIVED_ROUTE=27-19-r402d
```
