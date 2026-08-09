# Stage14-t roadmap — triple-gate side track

## Purpose

Stage14-t controls the triple/perfect-cuboid correction term in

\[
E(B)=N_2(B)+3T(B).
\]

It is separate from the main `14-4` raw-pair/Kummer track and the `14-e` ambient track.

## 14-t1 — baseline and theorem gap
Status: [x] Complete.

## 14-t2 — quantitative boundary
Status: [x] Complete.

## 14-t3 — Humbert-Edge splitting
Status: [x] Complete.

## 14-t4 — elliptic compression and Kummer restriction
Status: [x] Complete.

## 14-t5 / t5a — fixed minimal-curve transfer gate
Status: [x] Complete. Stage14-4ak eliminates the final fixed physical `M`-degree-4 mechanism.

## 14-t6 — reflected moving double-small-point gate
Status: [x] Complete. Triple points require compatible logarithmic small points on the reflected quotient pair `E_+(s), E_+(-s)`.

## 14-t7 — shared-q conic and fixed-prime boundary
Status: [x] Complete. The exact conic relation is useful structurally but the naive fixed-prime square-class sieve is vacuous on physical bases.

## 14-t8 — reflected moving-prime local boundary
Status: [x] Complete. At new reflected primes the local square condition is automatic unless the easy unit argument degenerates at `q^2=-1 mod p`.

## 14-t9 — Euclid sparse-residue formulation
Status: [x] Complete, with interpretation corrected by t10.

## 14-t10 — character-sieve direction audit
Status: [x] Complete. The sparse reflected residue support is an exceptional regime where automatic local solubility stops, not a necessary thinning condition for every triple.

## 14-t11 — compatible paired small-point activation
Status: [x] Complete.

For each primitive oriented physical base `F`, define `mu_R(F)` as the first raw physical height and `mu_pair(F)` as the first height of a compatible shared-`q` point on the genus-5 Humbert--Edge fiber product. Then

\[
\mu_R(F)\le\mu_{pair}(F),\qquad V_{pair}(B)\le V_R(B).
\]

The new t-side conditional thinning factor is

\[
\theta_{pair}(B)=V_{pair}(B)/V_R(B).
\]

This is strictly stronger than simultaneous positive rank or unrelated small points on the two reflected elliptic quotients: both projections must arise from the same rational `q`.

At object level define `P(B)` as the number of compatible physical pairs `(F,q)` below height `B`.

## 14-t12 — point-conditioned reflected-square parameter gate
Status: [x] Complete.

Condition on an already-existing raw point

\[
W^2=q^4+2\frac{1-t^2}{1+t^2}q^2+1,
\qquad h^2=1+t^2.
\]

The reflected square is equivalent to the rational right-triangle condition

\[
W^2+\left(\frac{2q}{th}\right)^2=R^2.
\]

Parametrizing this conic by `r in Q` gives

\[
W=\frac{q(1-r^2)}{thr},\qquad
R=\frac{q(1+r^2)}{thr}.
\]

Writing `y=q^2`, substitution into the raw quartic gives the reciprocal quadratic

\[
y^2+B_{t,r}y+1=0,
\]

with

\[
B_{t,r}=2\frac{1-t^2}{1+t^2}
-\frac{(1-r^2)^2}{t^2(1+t^2)r^2}.
\]

Thus compatibility requires the discriminant

\[
D_{t,r}=B_{t,r}^2-4
\]

to be a rational square **and** the chosen quadratic root `y` itself to be a rational square satisfying the physical height cutoff. The second condition is essential.

This converts the t11 moving genus-5 shared-`q` gate into an explicit lower-dimensional auxiliary cover over `(t,r)` without assuming any local-density independence.

## 14-t13 — auxiliary discriminant-cover geometry
Status: [>] Next.

Factor and normalize the `(t,r)` discriminant-square cover, determine its generic genus/fibration type, and audit whether it contains rational/elliptic low-degree components capable of accumulating under the physical height. Retain the additional `y=q^2` square-root condition throughout.

Primary target remains

\[
T(B)=o(\sqrt B).
\]

## Scope boundary

Stage14-t is a population-counting track, not a finite-search proof of perfect-cuboid nonexistence.

```text
STAGE14_T_TRACK=ACTIVE
STAGE14_T1=COMPLETE_BASELINE_AND_THEOREM_GAP
STAGE14_T2=COMPLETE_QUANTITATIVE_BOUNDARY
STAGE14_T3=COMPLETE_HUMBERT_EDGE_AND_ELLIPTIC_SPLITTING
STAGE14_T4=COMPLETE_ELLIPTIC_COMPRESSION_AND_KUMMER_RESTRICTION
STAGE14_T5=COMPLETE_FIXED_M4_TRANSFER_GATE_ZERO_CASES
STAGE14_T6=COMPLETE_MIRROR_DOUBLE_SMALL_POINT_GATE
STAGE14_T7=COMPLETE_SHARED_Q_CONIC_AND_LOCAL_SIEVE_BOUNDARY
STAGE14_T8=COMPLETE_REFLECTED_MOVING_PRIME_LOCAL_BOUNDARY
STAGE14_T9=COMPLETE_EUCLID_SPARSE_RESIDUE_SIEVE_FORMULATION
STAGE14_T10=COMPLETE_CHARACTER_SIEVE_DIRECTION_AUDIT
STAGE14_T11=COMPLETE_COMPATIBLE_PAIRED_ACTIVATION_FORMULATION
STAGE14_T12=COMPLETE_CONDITIONAL_REFLECTED_SQUARE_PARAMETER_GATE
PRIMARY_TARGET=T(B)=o(sqrt(B))
NEXT=Stage14-t13 auxiliary discriminant-square cover geometry
```
