# Stage14-t roadmap — triple-gate side track

## Purpose

Stage14-t controls the triple/perfect-cuboid correction term in

\[
E(B)=N_2(B)+3T(B).
\]

It is separate from the main `14-4` raw-pair/Kummer track and the `14-e` ambient track.

## 14-t1 — baseline and theorem gap

Status: [x] Complete.

Locked: fixed physical genus-5 fiber; physical height `v asymp sqrt(Bg/S1)`; exact finite `T(B)=0` through `B=2,000,000` with no nonexistence inference.

## 14-t2 — quantitative boundary

Status: [x] Complete.

The Pythagorean-chain majorant gives `T(B)=O(B(log B)^5)` while the stronger frozen Stage13 result remains `T(B)=o(B(log B)^3)`. Neither reaches `o(sqrt(B))`.

## 14-t3 — Humbert-Edge splitting

Status: [x] Complete.

Every genuine fixed-base triple fiber is a type-4 Humbert--Edge genus-5 curve and its Jacobian splits over `Q` into five elliptic factors. There are no physical singular/lower-genus or rational extra-automorphism exceptional fibers.

## 14-t4 — elliptic compression and Kummer restriction

Status: [x] Complete.

The five elliptic quotients have three geometric j-types, with `E_R` the raw-pair factor and `E_W` the third-face factor. The third-square cover has branch class `2M`; a transverse restriction to an extremal `M.C=4` bisection would have genus 3.

## 14-t5 / t5a — fixed minimal-curve transfer gate

Status: [x] Complete.

Stage14-4ak proves the required parity coset for the final fixed `M`-degree-4 split mechanism is empty. Hence the t5 root-by-root triple audit has zero roots to process. This removes the fixed minimal-bisection contamination path but does not prove `T(B)=o(sqrt(B))`.

## 14-t6 — reflected moving double-small-point gate

Status: [x] Complete.

The relevant moving quotient pair obeys `j_W(s)=j_R(-s)`. A physical triple requires compatible rational points on `E_+(s)` and `E_+(-s)`, from the same physical `q`, with both in logarithmic canonical-height windows.

## 14-t7 — shared-q conic and local-sieve boundary

Status: [x] Complete.

For `s=t^2`, `A=(1-s)/(1+s)`, `C=2/s-1`, the shared quartics satisfy

\[
R^2-W^2=\frac{4q^2}{s(1+s)}.
\]

On a physical Pythagorean base `1+t^2=h^2`, the coefficient is a rational square and every triple forces the auxiliary rational Pythagorean relation

\[
W^2+\left(\frac{2q}{th}\right)^2=R^2.
\]

Thus the shared lift is an explicit conic compatibility condition. However the naive fixed-prime difference-squareclass sieve is vacuous on physical bases; no independent local `1/2` loss may be inferred from this identity.

## 14-t8 — reflected 2-descent on moving bad-prime support

Status: [>] Next.

Retain the individual raw/reflected quartics and compare their 2-descent/Kummer square classes on the same moving support. Use the Stage14-s handoff that physical Kummer support lies in primes dividing the moving first-face arithmetic data. The goal is to determine whether simultaneous reflected compatibility loses a positive density or logarithmic factor after raw activation.

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
PRIMARY_TARGET=T(B)=o(sqrt(B))
NEXT=Stage14-t8 reflected-pair 2-descent classes on moving bad-prime support
```
