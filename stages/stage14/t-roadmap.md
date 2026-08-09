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
Status: [x] Complete. New reflected gates can occur only at split primes `p|Delta_-`, `p=1 mod 4`, and only on the two residues `q^2=-1 mod p`.

## 14-t9 — Euclid-parameter sparse-residue family sieve target
Status: [x] Complete.

For every odd split prime the exceptional set has exact residue density

\[
\rho_p=2/p,
\]

while inert primes contribute zero. This is not a fixed positive-density sieve and no product-independence is assumed.

The correct analytic object is the joint base-point family `(F,q)`: raw Stage14-s activation/descent conditions first, then reflected split divisors of `Delta_-`, exceptional residues, and the physical small-point window. Single-fiber point counts or average rank alone cannot close this.

## 14-t10 — character-sum / large-sieve realization
Status: [>] Next.

Rewrite the exceptional condition and raw 2-descent constraints as explicit quadratic-character weights over primitive Euclid parameters and the physical point coordinate. Seek averaged cancellation strong enough to give at least a logarithmic saving after raw activation, without assuming independent prime factors.

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
PRIMARY_TARGET=T(B)=o(sqrt(B))
NEXT=Stage14-t10 character-sum / large-sieve realization
```
