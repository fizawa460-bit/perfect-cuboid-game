# Stage27-19-r5ai — residual exact-height versus cross-gcd cancellation dichotomy

```text
TASK_ID=Stage27-19-r5ai
SOURCE_STAGE=Stage19
TRIGGER_CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PARALLEL
PARENT_ROUTE=Stage27-19-r5ah
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
PARALLEL_LANE=true
```

Stage27-19-r5ah eliminates the primitive toric gcd exactly. On every Stage19 survivor,

\[
R=\frac{h}{\varepsilon}\,\kappa\,L,
\qquad
L=w'c'=\frac{wc}{C},
\]

where

\[
C=(m,r)(m,s_0)(r,n_0),
\qquad \varepsilon\in\{1,2\}.
\]

Thus the remaining exact-height question is quantitative: how much of the square-root product `wc` is left after the only legal primitive cancellation `C`?

## 1. Exact cancellation ratio

Because `C|wc`, define the positive integer

\[
\boxed{L=\frac{wc}{C}\ge1.}
\]

Then

\[
\boxed{R=(h/\varepsilon)\kappa L.}
\]

There is no additional real-valued or hidden gcd term. In particular, on `R<=B`,

\[
\boxed{h\kappa L\le2B.}
\]

## 2. A uniform threshold split

Fix any `theta` with `0<=theta<=1`. Split Stage19 survivors into

\[
\mathcal A_\theta=\{L\ge B^\theta\}
\]

and

\[
\mathcal C_\theta=\{L<B^\theta\}.
\]

On the residual-height side `A_theta`,

\[
\boxed{h\kappa\le2B^{1-\theta}.}
\]

On the cancellation side `C_theta`, since `L=wc/C`,

\[
\boxed{C>\frac{wc}{B^\theta}.}
\]

Thus every survivor satisfies the exact dichotomy

\[
\boxed{
L\ge B^\theta
\quad\text{or}\quad
C> wc/B^\theta.
}
\]

This makes the next counting input precise. A strict-subhalf theorem may be obtained by proving a fixed-power bound for the population with small `h*kappa` on the first side and a fixed-power rarity theorem for near-total cross-gcd cancellation on the second side.

## 3. What this route does not prove

The inequality `h*kappa<=2B` alone does not give a new `N_2` exponent. Nor is a positive lower bound for `L` stronger than `1` currently proved uniformly. Actual Stage19 survivors can have `kappa=1`, so one may not replace the exact product by a heuristic that assumes a large squarefree kernel.

Likewise, the existence of the explicit product

\[
C=(m,r)(m,s_0)(r,n_0)
\]

does not itself prove that large `C` is rare. That is the new arithmetic incidence problem.

The value of the route is closure: after r5ah-r5ai there are only two legal places where a fixed-power gain can come from inside the exact-height strategy. Hidden `Gamma` behavior is no longer a third possibility.

```text
RESIDUAL_EXACT_HEIGHT_FACTOR_DEFINED=true
RESIDUAL_EXACT_HEIGHT_FACTOR=L=w*c/C=w_prime*c_prime
RESIDUAL_FACTOR_POSITIVE_INTEGER=true
EXACT_HEIGHT_PRODUCT=R=(h/epsilon)*kappa*L
THRESHOLD_DICHOTOMY_PROVED=true
RESIDUAL_LARGE_SIDE=h*kappa<=2*B^(1-theta)
CANCELLATION_LARGE_SIDE=C>w*c/B^theta
HIDDEN_GAMMA_BRANCH_CLOSED=true
SMALL_H_KAPPA_POPULATION_FIXED_POWER_BOUND_PROVED=false
LARGE_CROSS_GCD_CANCELLATION_SPARSE_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
BATCH_STOP_REASON=NEXT_STEP_REQUIRES_UNIFORM_COUNT_FOR_SMALL_H_KAPPA_OR_LARGE_CROSS_GCD_CANCELLATION
NEXT_DERIVED_ROUTE=27-19-r5aj
NEXT_TARGET=UNIFORM_CROSS_GCD_CANCELLATION_COUNT_OR_SMALL_H_KAPPA_INCIDENCE_THEOREM
CODY_USEFUL_FOR_NEXT_ROUTE=true
```
