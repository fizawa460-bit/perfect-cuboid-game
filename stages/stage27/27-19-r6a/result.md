# Stage27-19-r6a — occupied-`R` squareclass collision receiver

```text
TASK_ID=Stage27-19-r6a
SOURCE_STAGE=Stage19
TRIGGER_CHECKPOINT=40
ROUTE_KIND=OCCUPIED_R_SUPPORT_REENTRY
PARENT_ROUTE=Stage27-19-r5ax
STATUS=BATCH_SUBMITTED_PENDING_FRESH_AUDIT
```

r5aw/r5ax reduce the global upper problem to occupied space-diagonal support:

\[
S_2(B)=\#\{R\le B:N_{2,R}>0\},
\qquad
S_2(B)\le N_2(B)\le B^{o(1)}S_2(B).
\]

So a strict sub-square-root upper bound must now produce a fixed-power deficit for occupied `R` (unless the frozen r5 lane is reopened by its separate same-measure boundary theorem).

## 1. Exact fixed-`R` support receiver

Take an exactly-two physical cuboid in a direction where the two integral faces share edge `e`. Write the other edges as `x,y`, the two integral face diagonals as `A,B`, and the integral space diagonal as `R`. Then

\[
e^2+x^2=A^2,
\qquad
e^2+y^2=B^2,
\qquad
e^2+x^2+y^2=R^2.
\]

Therefore

\[
A^2+y^2=R^2,
\qquad
B^2+x^2=R^2.
\]

Thus

\[
\alpha=A+i y,
\qquad
\beta=B+i x
\]

are two positive Gaussian representations of norm `R^2`.

Define

\[
P=AB-xy,
\qquad
Q=AB+xy.
\]

Using `A^2=e^2+x^2` and `B^2=e^2+y^2`,

\[
\begin{aligned}
PQ
&=A^2B^2-x^2y^2\\
&=(e^2+x^2)(e^2+y^2)-x^2y^2\\
&=e^2(e^2+x^2+y^2)\\
&=(eR)^2.
\end{aligned}
\]

Since `Q>0` and `PQ>0`, also `P>0`. Hence **every occupied `R` produces a pair of positive norm-`R^2` Gaussian representations for which `P Q` is a square**.

Conversely, suppose positive integers `(A,y)` and `(B,x)` satisfy

\[
A^2+y^2=B^2+x^2=R^2,
\qquad A>x,
\]

and `PQ` is a square. Since

\[
PQ=R^2(A^2-x^2),
\]

and an integer with rational square root has integral square root, `A^2-x^2=e^2` for some integer `e>0`. The equality of the two norm equations then gives `B^2-y^2=e^2`. After imposing the original primitive/canonical and exactly-two mask `x^2+y^2` nonsquare, this reconstructs the physical `N2` object.

So occupied-`R` support is exactly a **square-incidence problem among pairs of Gaussian divisors of norm `R^2`, with the physical masks retained**.

## 2. Squarefree-kernel collision form

For positive integers `P,Q`, `PQ` is a square iff there is a unique positive squarefree integer `d` and positive integers `u,v` with

\[
P=d u^2,
\qquad
Q=d v^2.
\]

Hence every physical survivor satisfies

\[
\boxed{\operatorname{sqf}(AB-xy)=\operatorname{sqf}(AB+xy)}.
\]

Moreover

\[
AB=\frac d2(u^2+v^2),
\qquad
xy=\frac d2(v^2-u^2),
\qquad
eR=d u v.
\]

This is the first support-level collision receiver that does not count an already occupied fixed-`R` fiber again.

### Exact Stage19 witness

For the known primitive exactly-two survivor

\[
(R,e,x,y,A,B)=(1073,840,448,495,952,975),
\]

one gets

\[
P=706440=210\cdot58^2,
\qquad
Q=1149960=210\cdot74^2,
\]

so the common squarefree kernel is `d=210` and

\[
840\cdot1073=210\cdot58\cdot74.
\]

## 3. Why representation multiplicity alone cannot be the next theorem

A much weaker necessary condition is merely that `R^2` have at least two positive two-square representations. That condition has no fixed-power sparsity at all.

Indeed for every `m>=1`, with `R=25m`,

\[
R^2=(24m)^2+(7m)^2=(20m)^2+(15m)^2.
\]

Thus at least `floor(B/25)` integers `R<=B` satisfy the two-representation condition. Its support has polynomial exponent `1`.

Therefore the new route must use the **squareclass collision and physical masks**, not merely the number of Gaussian representations of `R^2`.

## 4. Counting interface

Let `Rep^+(R)` be the ordered positive pairs `(a,b)` with `a^2+b^2=R^2`. Since

\[
r_2(R^2)\le4\tau(R^2)=R^{o(1)},
\]

there are only `R^{o(1)}` ordered representation pairs to test at one `R`. Define the support collision event by the existence of two members `(A,y),(B,x)` of `Rep^+(R)` satisfying

1. `A>x`;
2. `(AB-xy)(AB+xy)` is a square;
3. the reconstructed `e` obeys the original primitive/canonical masks;
4. `x^2+y^2` is nonsquare.

The next useful theorem is therefore a bound of the form

\[
\#\{R\le B:\text{this collision event occurs}\}
\ll B^{1/2-\eta+o(1)}
\]

for some fixed `eta>0`, or any other fixed-power improvement over the current `B^{1/2+o(1)}` support bound.

This is a new support-count problem, not a restart of the frozen r5 boundary packet or SR-STR-224.

```text
OCCUPIED_R_GAUSSIAN_PAIR_RECEIVER_PROVED=true
OCCUPIED_R_PQ_IDENTITY=PQ=(eR)^2
OCCUPIED_R_SQUAREFREE_KERNEL_COLLISION_PROVED=true
OCCUPIED_R_COLLISION_RECONSTRUCTION_WITH_PHYSICAL_MASKS_PROVED=true
TWO_REPRESENTATIONS_ONLY_FIXED_POWER_DEFICIT_PROVED=false
TWO_REPRESENTATIONS_POSITIVE_DENSITY_HOST=R_multiple_of_25
FIXED_R_CANDIDATE_PAIR_COUNT=R^o(1)
OCCUPIED_R_SUPPORT_FIXED_POWER_DEFICIT_PROVED=false
STRICT_SUB_SQRT_UPPER_PROVED=false
NEW_MU_LT_HALF_PROVED=false
TRUE_N2_EXPONENT_IDENTIFIED=false
ADVANCE_TO_CHECKPOINT50=false
AUDIT_REQUIRED=true
MERGE_ALLOWED=false
NEXT_DERIVED_ROUTE=27-19-r6b
NEXT_TARGET=OCCUPIED_R_SQUARECLASS_COLLISION_SIEVE_WITH_PHYSICAL_MASKS
NEXT_EXPECTED_COMMAND=Stage27-19-r5-audit_OR_STAGE27-19-r6-audit
```
