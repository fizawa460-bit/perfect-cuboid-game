# Stage27-19-r5ae — norm-support-only barrier

```text
TASK_ID=Stage27-19-r5ae
SOURCE_STAGE=Stage19
TRIGGER_CHECKPOINT=40
ROUTE_KIND=UPPER_REENTRY_PARALLEL
PARENT_ROUTE=Stage27-19-r5ad
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
PARALLEL_LANE=true
```

r5ac proved the exact necessary restrictions
\[
p\in\mathcal S_2,\qquad g\in\mathcal S_2,\qquad p+q\in\mathcal S_2,
\]
and r402c gives the dyadic core-height ceiling `g << B^2/T` on `T<=H(p/q)<2T`.

This route asks whether those restrictions alone could possibly force the joint support below the half-power wall. The answer is no: their ambient necessary-condition set already contains a family of order `B` labels in every broad interior dyadic band. Therefore any fixed-power improvement must use the diagonal reconstruction equations / squareclass intersection, not just the three norm-support predicates and the core-height ceiling.

## 1. Ambient necessary-condition set

For a dyadic height `T`, define the ambient set
\[
\mathcal A_T(B)=\left\{(p,q,g):
(p,q)=1,
\ T\le\max(p,q)<2T,
\ p,g,p+q\in\mathcal S_2,
\ 1\le g\le \frac{B^2}{4T}
\right\}.
\]
The factor `1/4` is deliberately stronger than the r402c order-of-magnitude ceiling, so every constructed label is comfortably inside that necessary height corridor.

Assume `T` lies in an interior range such as
\[
16\le T\le B^2/16.
\]
Choose integers
\[
\sqrt T\le x\le\sqrt{3T/2}
\]
and
\[
1\le z\le\frac{B}{2\sqrt T}.
\]
Set
\[
\boxed{p=x^2,\qquad q=1,\qquad g=z^2.}
\]
Then:

- `(p,q)=1`;
- `T<=H(p/q)=x^2<2T`;
- `p=x^2+0^2` is a sum of two squares;
- `g=z^2+0^2` is a sum of two squares;
- `p+q=x^2+1^2` is a sum of two squares;
- `g=z^2<=B^2/(4T)`.

Thus every such pair `(x,z)` gives a distinct element of `A_T(B)`.

The `x` interval contains `gg T^(1/2)` integers and the `z` interval contains `gg B/T^(1/2)` integers, uniformly away from the endpoints. Hence
\[
\boxed{\#\mathcal A_T(B)\gg B.}
\]

No claim is made that these ambient labels are realized Stage19 objects. That is exactly the point: the three norm-support restrictions plus the core-height inequality leave far too many labels to prove the desired realized-support bound by themselves.

## 2. Consequence for the r5 restart strategy

The desired strict-subhalf restart would require, uniformly in dyadic `T`,
\[
K_T(B)\ll B^{1/2-\delta+o(1)}
\]
for the **realized** joint `(tau,g)` support.

But the r5ac predicates and r402c height ceiling, treated only as necessary membership tests, define an ambient set of size `gg B`. Therefore no argument that merely counts

```text
p in S2,
g in S2,
p+q in S2,
g << B^2/T
```

can deliver the required fixed-power support theorem. Logarithmic density savings from the two-squares conditions are structurally irrelevant to this power target unless they are coupled to the exact diagonal equations.

The next route must use at least one of the load-bearing equations
\[
m^2=ah-d^2n_0^2,
\qquad
r^2=bh+d^2s_0^2,
\]
or equivalently the intersection
\[
\kappa w^2=bm^2+pd^2,
\qquad
\kappa w^2=ar^2-qd^2.
\]
That is a genuine moving-family incidence/counting problem.

```text
NORM_SUPPORT_ONLY_POWER_SAVING_BARRIER_PROVED=true
AMBIENT_NECESSARY_CONDITION_FAMILY_SIZE=gg_B
R5AC_PLUS_CORE_HEIGHT_ALONE_INSUFFICIENT_FOR_STRICT_SUBHALF=true
DIAGONAL_RECONSTRUCTION_MUST_BE_USED_FOR_NEXT_POWER_SAVING=true
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
BATCH_STOP_REASON=NEXT_STEP_REQUIRES_GENUINE_MOVING_DIAGONAL_INCIDENCE_THEOREM
NEXT_DERIVED_ROUTE=27-19-r5af
NEXT_TARGET=UNIFORM_INCIDENCE_COUNT_ON_MOVING_DIAGONAL_TWO_QUADRICS_WITH_PHYSICAL_HEIGHTS
CODY_USEFUL_FOR_NEXT_ROUTE=true
```
