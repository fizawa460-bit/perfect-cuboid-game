# Stage27-20-r302h — fixed-power L1, L2, and exceptional-tail forms are equivalent up to exponent loss

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_WALL_OCCUPANCY
PARENT_ROUTE=Stage27-20-r302g
SOURCE_STAGE=Stage20

Retain the r302g notation and suppose `H>0`. Put

\[
\mu_x=H_x/H,
\]

so `mu` is a probability measure on the same physical MAIN fibers and `0<=rho_x<=1`.

## 1. L2 implies L1

If for some fixed `sigma>0`

\[
\sum_x\mu_x\rho_x^2\le B^{-\sigma+o(1)},
\tag{R302-OCC2}
\]

then Cauchy gives

\[
\sum_x\mu_x\rho_x
\le \left(\sum_x\mu_x\rho_x^2\right)^{1/2}
\le B^{-\sigma/2+o(1)}.
\]

Thus a weighted second-moment fixed-power deficit is sufficient, but its square-root loss must be charged explicitly.

## 2. L1 implies L2

Since `0<=rho<=1`, one has `rho^2<=rho`. Hence

\[
\sum_x\mu_x\rho_x\le B^{-\delta+o(1)}
\]

implies

\[
\sum_x\mu_x\rho_x^2\le B^{-\delta+o(1)}.
\]

Therefore existence of some positive fixed-power L1 saving is equivalent to existence of some positive fixed-power L2 saving, although the numerical exponents need not coincide.

## 3. Exceptional-tail form

For fixed `alpha>0`, define the high-occupancy set

\[
E_\alpha=\{x:\rho_x>B^{-\alpha}\}.
\]

If for fixed `alpha,beta>0`

\[
\mu(E_\alpha)\le B^{-\beta+o(1)},
\tag{R302-TAIL}
\]

then

\[
\sum_x\mu_x\rho_x
\le B^{-\alpha}+\mu(E_\alpha)
\le B^{-\min(\alpha,\beta)+o(1)}.
\]

Conversely, if the L1 mean is `<=B^{-delta+o(1)}`, Markov at threshold `B^{-delta/2}` gives

\[
\mu(E_{\delta/2})\le B^{-\delta/2+o(1)}.
\]

Hence, at the level of whether a positive fixed power exists, same-measure weighted L1, weighted L2, and a high-occupancy exceptional-mass theorem are equivalent up to constant losses in the exponent.

This closes the idea that merely switching from first to second moment is itself a new source of saving. The new input must be arithmetic control of the physical occupancy distribution.

```text
STAGE27_20_R302H_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
SAME_MEASURE_OCCUPANCY_L2_IMPLIES_L1=true
SAME_MEASURE_OCCUPANCY_L1_IMPLIES_L2=true
SAME_MEASURE_OCCUPANCY_TAIL_IMPLIES_L1=true
SAME_MEASURE_OCCUPANCY_L1_IMPLIES_TAIL=true
FIXED_POWER_OCCUPANCY_L1_L2_TAIL_EXISTENCE_EQUIVALENT=true
SECOND_MOMENT_REWEIGHTING_ALONE_NEW_SAVING=false
MAIN_OCCUPANCY_FIXED_POWER_DEFICIT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
ADVANCE_TO_CHECKPOINT50=false
NEXT_DERIVED_ROUTE=27-20-r302i
```
