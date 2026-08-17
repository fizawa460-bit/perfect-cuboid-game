# Stage27-20-r301o — soluble delta fibers share one Mordell--Weil group

STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PREFLIGHT
PARENT_ROUTE=Stage27-20-r301n
SOURCE_STAGE=Stage20

## 1. Soluble fibers are genus-one coverings of the same elliptic curve

R301n proves that for one fixed physical first coordinate `x=q1`, every squareclass fiber

\[
C_{x,\delta}:\quad
x^2+y^2=\delta r^2,
\qquad
x^2y^2+1=\delta s^2
\]

has the same Jacobian `E_x/Q`, independently of `delta`.

For an actually occupied Stage27 fiber, a physical survivor supplies a rational point on `C_{x,delta}`. Hence that genus-one torsor is soluble and, after choosing any rational base point, is noncanonically isomorphic over `Q` to its Jacobian `E_x`.

Therefore the Mordell--Weil rank attached to every occupied squareclass above one fixed `x` is exactly

\[
\boxed{r_x=\operatorname{rank}E_x(\mathbf Q),}
\]

not a separately moving rank `r_{x,delta}`.

## 2. Delta is covering/descent data, not rank entropy

The audited quartic

\[
\delta V^2=
(\delta z^2-(x^2+1)^2)
(\delta z^2-(x^2-1)^2)
\]

is a standard degree-two genus-one covering model. When it is soluble, its covering structure determines a Kummer/descent class for the common elliptic curve `E_x`; changing `delta` changes this covering data but not the ambient Mordell--Weil group.

This corrects the overly pessimistic interpretation that every moving `(x,delta)` pair may carry an unrelated rank. The only genuinely moving rank parameter in this decomposition is `x`.

## 3. What is and is not uniform now

For a fixed `x`, the rank is now uniform across all occupied `delta`. R301h also gives

\[
|D_x(B)|=B^{o(1)}
\]

for the number of possible squareclasses over that `x`.

However, this does **not** yet imply

\[
\sum_{\delta\in D_x(B)}w_{x,\delta}(B)=B^{o(1)}
\]

uniformly in moving `x`. A rational isomorphism from a soluble torsor to `E_x` depends on a chosen rational point, and the naive height-comparison constants may vary with the covering/model. To count all physical points one still needs either:

1. a uniform explicit covering map with polynomially controlled height distortion; or
2. an averaged height/regulator theorem for the common-Jacobian family `E_x` and its soluble coverings.

Thus the common-Jacobian theorem removes **rank variation in delta**, but not the remaining height/regulator obstruction.

## 4. Sharpened bookkeeping gate

Define the aggregate fixed-`x` weight

\[
W_x(B):=\sum_{\delta\in D_x(B)}w_{x,\delta}(B).
\]

If a new theorem gives uniformly

\[
W_x(B)\ll B^{\phi+o(1)}
\]

and independently

\[
|Q(B)|\ll B^{\sigma+o(1)},
\]

then exactly as in r301j,

\[
N_2(B)\ll B^{\sigma+\phi+o(1)},
\]

so strict progress still requires

\[
\boxed{\sigma+\phi<\frac12}.
\]

The structural gain is that `phi` may now be attacked using one elliptic curve `E_x` per `x`, rather than a separate rank problem for every squareclass.

```text
STAGE27_20_R301O_STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
SOLUBLE_DELTA_FIBERS_SHARE_ONE_MORDELL_WEIL_GROUP=true
RANK_VARIATION_IN_DELTA_ELIMINATED=true
DELTA_INTERPRETED_AS_COVERING_DESCENT_DATA=true
FIXED_X_SQUARECLASS_COUNT_SUBPOLYNOMIAL_RETAINED=true
UNIFORM_FIXED_X_AGGREGATE_SUBPOWER_PROVED=false
UNIFORM_COVERING_HEIGHT_TRANSFER_PROVED=false
MAX_AGGREGATE_PROGRESS_GATE=sigma+phi<1/2
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
NEXT_DERIVED_ROUTE=27-20-r301p
```
