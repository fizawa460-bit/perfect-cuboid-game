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
Status: [x] Complete.

The reflected quartic satisfies

\[
R^2=(q^2+1)^2+4\frac{1-s}{s}q^2.
\]

For `s=X^2/S^2`, the new reflected moving factor is

\[
\Delta_-=S^2-X^2.
\]

At an odd new prime `p | Delta_-`, the reflected square condition is locally automatic whenever `q^2+1` is a `p`-adic unit. Hence inert primes `p == 3 mod 4` contribute no new local gate. Only split primes `p == 1 mod 4` can be nontrivial, and only on the two exceptional residues

\[
q^2\equiv-1\pmod p.
\]

Thus the remaining triple sieve is a moving split-prime sparse-residue problem, not a fixed-prime positive-density sieve.

## 14-t9 — Euclid-parameter split-prime exceptional-residue large sieve
Status: [>] Next.

Parameterize primitive first faces by Euclid variables and study the split prime divisors of `Delta_-=S^2-X^2`. Combine:

1. raw Stage14-s 2-descent activation classes;
2. split divisors `p | Delta_-`, `p == 1 mod 4`;
3. exceptional residues `q^2 == -1 mod p`;
4. the physical logarithmic small-point window.

The target is a genuine family-level saving after raw activation. No independence among prime divisors may be assumed.

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
PRIMARY_TARGET=T(B)=o(sqrt(B))
NEXT=Stage14-t9 Euclid-parameter split-prime exceptional-residue large sieve
```
