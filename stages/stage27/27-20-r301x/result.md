# Stage27-20-r301x — the natural q1/q0 slope collision energy is purely diagonal

STATUS=AUDITED_PASS_MERGED
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PREFLIGHT
PARENT_ROUTE=Stage27-20-r301w
SOURCE_STAGE=Stage20

## 1. Critical occupied set and the exact slope adapter

Let `Q_crit(B)` be the occupied first-coordinate support on the r301v critical segment. By r301t,

\[
q_0=\frac{q_1-1}{q_1+1}
\]

is a rational inverse to

\[
q_1=\frac{1+q_0}{1-q_0}
\]

on the physical range. Hence the natural Stage14 face-slope projection is injective on `Q_crit(B)`.

## 2. Exact collision ledger

For each rational Stage14 slope `r`, define

\[
m(r)=\#\{q_1\in Q_{\rm crit}(B):q_0(q_1)=r\}.
\]

Injectivity gives

\[
m(r)\in\{0,1\}.
\]

Therefore the ordinary collision energy is exactly

\[
\boxed{\sum_r m(r)^2=|Q_{\rm crit}(B)|},
\]

and the off-diagonal same-slope collision count is

\[
\boxed{\sum_r m(r)(m(r)-1)=0}.
\]

Thus the most immediate `occupied-slope collision` interpretation produces no extra incidence structure at all: every occupied `q1` has its own `q0`.

## 3. What a useful energy receiver would have to change

A nontrivial energy route must introduce a genuinely different, coarser arithmetic invariant `pi(q1)` or a separate bilinear relation. If

\[
m_\pi(t)=\#\{q_1\in Q_{\rm crit}(B):\pi(q_1)=t\},
\]

then Cauchy only gives

\[
|Q_{\rm crit}(B)|^2\le |\pi(Q_{\rm crit}(B))|\sum_t m_\pi(t)^2.
\]

To turn this into a fixed-power support bound requires independent quantitative control of both the image support and the corresponding energy (or an equivalent off-diagonal theorem). Merely renaming the injective `q0` coordinate cannot do it.

No such new coarser invariant with an audited fixed-power collision theorem is present in the current receiver package.

## 4. Outcome

The natural q1/q0 collision lane is closed exactly, not heuristically. A future energy attack remains legal only after a new non-injective arithmetic projection or independent bilinear collision relation is supplied.

```text
STAGE27_20_R301X_STATUS=AUDITED_PASS_MERGED
Q1_Q0_MOBIUS_BIJECTION_RETAINED=true
NATURAL_Q0_COLLISION_MULTIPLICITY_LE_1=true
NATURAL_Q0_COLLISION_ENERGY_EQUALS_SUPPORT=true
NATURAL_Q0_OFFDIAGONAL_COLLISIONS=0
NATURAL_SLOPE_ENERGY_FIXED_POWER_SAVING_PROVED=false
NEW_COARSE_ARITHMETIC_INVARIANT_PROVED=false
CRITICAL_Q1_SUPPORT_FIXED_POWER_DEFICIT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
NEXT_DERIVED_ROUTE=27-20-r301y
STOP_REASON=NEW_NONINJECTIVE_ARITHMETIC_PROJECTION_OR_OFFDIAGONAL_COLLISION_THEOREM_REQUIRED
```
