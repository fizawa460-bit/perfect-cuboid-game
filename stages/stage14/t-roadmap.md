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

The exceptional residues have density `2/p` at split primes. They are a sparse moving set, but t10 verifies that they are not a necessary condition for triple points; they are the exceptional set where the automatic local argument stops.

## 14-t10 — character-sieve direction audit
Status: [x] Complete.

For reduced `q=u/v` and odd `p` away from denominator primes,

\[
q^2\equiv-1\pmod p
\iff
p\mid u^2+v^2.
\]

Thus the reflected exceptional support is the odd support of

\[
\gcd(\Delta_-,u^2+v^2).
\]

However this is an **error/exception set**, not a thinning condition satisfied by every triple. If no such exceptional prime occurs, the new reflected local tests are automatic. Therefore a large sieve for this gcd support can simplify exceptional bookkeeping but cannot by itself prove a power saving for `T(B)`.

The main saving must come from the global simultaneous condition already isolated in t6: compatible physical small points on `E_+(s)` and `E_+(-s)` with the same Humbert--Edge/shared-`q` lift.

## 14-t11 — paired reflected activation count
Status: [>] Next.

Define and attack the paired activation population

\[
V_{\pm}(B)=\#\{F:\ E_+(s_F),E_+(-s_F)\text{ both admit compatible physical small points}\}.
\]

Seek either

\[
V_{\pm}(B)=o(\sqrt B)
\]

or a relative thinning theorem `V_pm(B)=o(V(B))` that can be combined with the main/raw activation law. The t8 exceptional-prime sieve is retained only as a secondary error decomposition.

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
PRIMARY_TARGET=T(B)=o(sqrt(B))
NEXT=Stage14-t11 paired reflected activation count / global compatibility target
```
