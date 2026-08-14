# Stage24-50 — lower bound / construction breakthrough

EVIDENCE_LEVEL=PROVED_PENDING_FRESH_AUDIT
CHECKPOINT=50
STATUS=SUBMITTED_FOR_FRESH_AUDIT

## 1. Result

Checkpoint50 finds a new infinite primitive Stage19 construction by reopening the Stage15-2 explicit two-face family at its parity boundary.

The key genus-one curve is

\[
\boxed{C_{17}:\ p^4+q^4=17Z^2.}
\]

For a coprime positive solution define

\[
e=4pq,\qquad x=4p^2-q^2,\qquad y=4q^2-p^2,
\qquad D=17Z.
\]

Then

\[
e^2+x^2=(4p^2+q^2)^2,
\]
\[
e^2+y^2=(4q^2+p^2)^2,
\]
\[
e^2+x^2+y^2=D^2.
\]

The quartic has positive Mordell-Weil rank. In the physical open cone

\[
1<q/p<\frac{1+\sqrt2}{2}
\]
there are infinitely many rational points. They yield primitive canonical boxes with `(a,b,c)=(x,y,e)` and integral space diagonal.

The points where the remaining face is also square lie on a genus-five curve, so by Faltings there are only finitely many such exceptions inside this family. Hence infinitely many members have **exactly two** integral face diagonals.

Therefore, subject to fresh audit,

\[
\boxed{N_2(B)\to\infty.}
\]

Using standard elliptic height growth and equidistribution on the real elliptic component gives the quantitative lower bound

\[
\boxed{N_2(B)\gg\sqrt{\log B}.}
\]

Thus the current Stage24 theorem stack becomes

\[
\boxed{\sqrt{\log B}\ll N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.}
\]

No positive power lower bound is proved.

## 2. Positive-rank certificate

In affine coordinates `t=q/p`, `z=Z/p^2`, the curve is

\[
17z^2=t^4+1.
\]

It maps to

\[
E:Y^2=X^3-1156X
\]
by

\[
X=-4t^2/z^2,
\qquad
Y=4t(t^4-1)/z^3.
\]

The point `(t,z)=(2,1)` maps to

\[
P=(-16,120).
\]

Exact good-reduction computation gives

\[
\#E(\mathbf F_{31})=32,
\quad
\#E(\mathbf F_{41})=52,
\quad
\operatorname{ord}(P\bmod31)=16.
\]

The standard reduction injection for rational torsion would force a rational torsion order to divide `4`, contradicting the order-16 reduction. Hence `P` is infinite order, so the genus-one quartic has positive rank.

The complete proof and exact arithmetic are in:

- `u19-r501a-quartic-family.md`;
- `quartic_family_audit.py`.

## 3. Physical population map

For a reduced rational point `t=q/p`, the quantity `Z=p^2z` is automatically integral because `17Z^2` is an integer and `17` is squarefree.

The parameters `p,q` have opposite parity: both odd would make `p^4+q^4=2 (mod16)`, impossible for `17Z^2`.

Primitivity follows directly from coprimality. Every odd prime dividing `e=4pq` misses at least one of `x,y`, and opposite parity makes one of `x,y` odd. Thus

\[
\gcd(e,x,y)=1.
\]

Inside the cone `1<q/p<(1+sqrt(2))/2`,

\[
0<x<y<e,
\]
so no cutoff, canonical, or multiplicity adapter is needed. Distinct reduced positive parameter ratios give distinct boxes because `x+y` and `y-x` recover `p^2+q^2` and `q^2-p^2`.

An exact physical-cone witness is

\[
(p,q,Z)=(38,43,569)
\]
and

\[
(a,b,c,D)=(3927,5952,6536,9673).
\]

This witness is only a regression anchor; infinitude comes from the positive-rank curve.

## 4. Exactly-two mask

The only remaining mask is whether

\[
x^2+y^2
\]
is a square. After dividing by `p^4`, this becomes

\[
w^2=17t^4-16t^2+17.
\]

Together with `17z^2=t^4+1`, the normalization is a connected degree-four biquadratic cover of `P1`. The two quartic branch sets are simple and disjoint, giving eight branch values and genus

\[
g=5
\]
by Riemann-Hurwitz.

Faltings therefore makes the third-square rational sublocus finite. The construction proves infinitely many **exactly-two** boxes, not merely at-least-two boxes.

No conclusion about the global perfect-cuboid population is made.

## 5. Quantitative lower derivation

Choose a non-torsion rational point `R` on `C_17` and a physical rational point `Q0` in the open cone. After replacing `R` by `2R` if needed, the sequence

\[
Q_n=Q_0+nR
\]
is equidistributed on its real circle component. A fixed positive proportion of `n<=N` therefore lands in a smaller open subinterval of the physical cone.

For the fixed rational function `t`, standard elliptic height theory gives

\[
h(t(Q_n))=O(n^2).
\]

If `t(Q_n)=q_n/p_n` is reduced,

\[
\max(p_n,q_n)\le e^{Cn^2}.
\]

The corresponding space diagonal obeys

\[
D_n=17Z_n\le\sqrt{34}\max(p_n,q_n)^2\le e^{C'n^2}.
\]

Thus `n<=c sqrt(log B)` lies below height `B` for a sufficiently small fixed `c`. Bounded degree of the `t` projection and injectivity of the physical parameter map leave `gg N` distinct boxes. Removing the finite genus-five exceptional set has no asymptotic effect.

Hence

\[
N_2(B)\gg\sqrt{\log B}.
\]

This is a genuine asymptotic lower bound but has polynomial exponent zero.

## 6. Fresh-search policy compliance

The fresh lower surgeon generated four candidate classes. F50-S1 is a breakthrough; F50-S2 is the general symmetric-multiplier quartic class; F50-S3 is the direct common-squarefree-core route; F50-S4 is the common-leg divisor-plus-space receiver.

Because the checkpoint is positive, the policy requiring at least eight old dead branches to be reopened **if the result is negative** is not triggered. The most relevant old branch, Stage23 R60-01, is revalidated directly. Its mod-16 death remains valid only for the historical odd/odd specialization; the mixed-parity variant revives the broader algebraic formula.

## 7. Numerical reuse

```text
NUM_REUSE_CHECK=PASS
NUM_ASSETS_REUSED=NUM-R01,NUM-R02,NUM-R03,24-14num-r201,24-14num-r202
NUM_POPULATION_MATCH=EXACT
NUM_EVIDENCE_LEVEL=EXACT_FINITE_ORACLE_PLUS_NEW_THEOREM_CONSTRUCTION
NUM_NEW_COMPUTATION_JUSTIFIED=TARGETED_CONSTRUCTION_REGRESSION_ONLY
```

No census extension is used to prove the theorem.

## 8. Supersession boundary

The historical Stage19 checkpoint50/final statements that unboundedness and an infinite primitive construction were unproved were correct at their audit time. If this checkpoint receives fresh PASS, those two status lines require history backflow as superseded-by-Stage24 facts.

The historical statement `no positive-power lower bound` remains current.

No frozen historical Stage19 file is rewritten before fresh audit.

## 9. Non-claims

- no `N2(B)>>B^delta` for any fixed `delta>0`;
- no matching `B^(1/2-o(1))` lower bound;
- no `N2(B)~C sqrt(B)` law;
- no true polynomial exponent identified;
- no claim that exponent `1/2` is intrinsic;
- no perfect-cuboid existence or nonexistence conclusion;
- no finite-census extrapolation.

```text
DISCOVERY_CHECKPOINT=50
FRESH_STAGE19_LOWER_SURGEON_FIRST=true
FRESH_LOWER_CANDIDATES=4
BREAKTHROUGH_FOUND=true
STAGE18_EXPLICIT_FAMILY_SPACE_LIFT_TEST=PASS_MIXED_PARITY_VARIANT
STAGE19_UNBOUNDEDNESS_PROVED=true
INFINITE_PRIMITIVE_STAGE19_CONSTRUCTION_PROVED=true
LOWER_BOUND_CLASS=LOGARITHMIC_UNBOUNDED
NEW_LOWER_BOUND=N2(B)>>sqrt(log B)
POSITIVE_POWER_LOWER_BOUND_PROVED=false
MATCHING_HALF_POWER_LOWER_BOUND_PROVED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
HALF_POWER_INTRINSIC_PROVED=false
FINITE_DATA_USED_AS_PROOF=false
HISTORY_SUPERSESSION_BACKFLOW_REQUIRED_AFTER_AUDIT_PASS=true
DISCOVERY_AUDIT_REQUIRED=true
DISCOVERY_AUDIT_VERDICT=PENDING
AUDIT_REQUIRED=true
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=50
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=Stage24-audit
CODEX_REQUIRED=false
```
