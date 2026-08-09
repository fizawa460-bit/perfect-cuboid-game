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
Status: [x] Complete. Define `V_pair(B)` and object-level `P(B)` for compatible shared-`q` points; simultaneous rank or unrelated small points are insufficient.

## 14-t12 — point-conditioned reflected-square parameter gate
Status: [x] Complete.

Conditioning on a raw point and parametrizing the auxiliary right triangle by `r` gives

\[
y^2+B_{t,r}y+1=0,\qquad y=q^2,
\]

with

\[
B_{t,r}=2\frac{1-t^2}{1+t^2}-\frac{(1-r^2)^2}{t^2(1+t^2)r^2}.
\]

Compatibility requires both `D_{t,r}=B_{t,r}^2-4` square and the selected root `y` itself square in the physical height window.

## 14-t13 — discriminant-cover geometry
Status: [x] Complete.

The discriminant factors exactly as

\[
D_{t,r}=\frac{(r^2-2tr-1)(r^2+2tr-1)(r^4+(4t^4-2)r^2+1)}{r^4t^4(1+t^2)^2}.
\]

After removing the square denominator, the normalized cover is

\[
Z^2=(r^2-2tr-1)(r^2+2tr-1)(r^4+(4t^4-2)r^2+1).
\]

The degree-eight branch polynomial has discriminant

\[
2^{40}t^{28}(t-1)^2(t+1)^2(t^2+1)^{12}.
\]

Hence every genuine physical rational base has a squarefree degree-eight branch divisor and a genus-three hyperelliptic discriminant fiber. There are no physical rational branch-collision fibers of genus 0, 1, or 2. The extra root condition `y=q^2` remains essential.

## 14-t14 — genus-three quotient/involution and second-square cover
Status: [>] Next.

Exploit the reciprocal/even branch structure of the genus-three discriminant cover to identify quotient maps and lower-genus factors, then impose the further condition that

\[
y=\frac{-B_{t,r}\pm Z}{2}
\]

is itself a rational square. Classify whether the resulting second cover admits any physical low-degree accumulating components.

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
STAGE14_T13=COMPLETE_DISCRIMINANT_COVER_GENUS_CLASSIFICATION
PRIMARY_TARGET=T(B)=o(sqrt(B))
NEXT=Stage14-t14 genus-three quotient/involution and second-square cover
```
