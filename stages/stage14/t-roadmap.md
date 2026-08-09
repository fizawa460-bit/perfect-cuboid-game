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

At object level define `P(B)` as the number of compatible physical pairs `(F,q)` below height `B`. A theorem for `T(B)` must control `P(B)` directly or combine a paired-base count with a compatible-point multiplicity bound.

The raw/main activation factorization therefore extends as

\[
\frac{V_{pair}}A=
\frac\Sigma A\frac R\Sigma\frac{V_R}R\frac{V_{pair}}{V_R}.
\]

The first three gates belong mainly to main/Stage14-s; the final shared-`q` gate is the t-side target.

The finite exact census through `B=2,000,000` has 490 raw active oriented face vertices and zero retained triple objects. This remains finite diagnostic evidence only.

## 14-t12 — point-conditioned reflected-square average
Status: [>] Next.

Condition on an already existing raw physical small point `(F,q)` and average the indicator that the reflected quartic at the **same q** is also a square. Equivalently, average physical-height rational points on the moving genus-5 fiber product after raw activation.

Seek a theorem of the form

\[
P(B)=o(\sqrt B)
\]

or a conditional-density saving strong enough to combine with the raw activation/multiplicity bounds.

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
PRIMARY_TARGET=T(B)=o(sqrt(B))
NEXT=Stage14-t12 point-conditioned reflected-square average / moving fiber-product small-point bound
```
