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

The Pythagorean-chain majorant gives

\[
T(B)=O(B(\log B)^5),
\]

while the stronger frozen Stage13 result remains

\[
T(B)=o(B(\log B)^3).
\]

Neither reaches `o(sqrt(B))`.

## 14-t3 — Humbert-Edge splitting

Status: [x] Complete.

Every genuine fixed-base triple fiber is a type-4 Humbert--Edge genus-5 curve with branch set

\[
\{\infty,0,1,-1/s,1/(1-s)\},\qquad s=t^2,
\]

and

\[
J(C_t)\sim_{\mathbf Q}E_{U_0,t}\times E_{U_1,t}\times E_{U_2,t}\times E_{W,t}\times E_{R,t}.
\]

There are no physical singular/lower-genus or rational extra-automorphism exceptional fibers.

## 14-t4 — elliptic compression and Kummer restriction

Status: [x] Complete.

The five elliptic quotients have only three geometric j-types. With `s=t^2`,

\[
j_+(s)=256\frac{(s^2+s+1)^3}{s^2(s+1)^2},
\]

\[
j_0(s)=256\frac{(s^4-s^2+1)^3}{s^4(s-1)^2(s+1)^2},
\]

\[
j_-(s)=256\frac{(s^2-s+1)^3}{s^2(s-1)^2}.
\]

The pairings are

```text
E_U0, E_R -> j_+
E_U1      -> j_0
E_U2, E_W -> j_-
```

so geometrically

\[
J(C_t)_{\overline{\mathbf Q}(s)}\sim E_+^2\times E_0\times E_-^2.
\]

`E_R` is exactly the Stage14 raw-pair elliptic factor. By Stage14-4af every physical triple point therefore lies over a positive-rank specialization of `E_R`.

The third-square cover has branch class `2M`; on an extremal rational bisection with `M.C=4`, a transverse restriction has normalized genus `3`.

## 14-t5 / t5a — fixed minimal-curve transfer gate

Status: [x] Complete.

Stage14-4ak independently verifies that the final split singular-anticanonical `M`-degree-4 mechanism has an empty required parity coset. Hence

```text
PHYSICAL_Q_RATIONAL_M4_BISECTION_EXISTS=false
FIXED_CURVE_SQRTB_MECHANISM_REJECTED=true
```

and the t5 root-by-root third-square branch audit has zero actual roots to process. This removes the fixed minimal-bisection contamination path for `T(B)` but does not prove `T(B)=o(sqrt(B))`.

## 14-t6 — reflected moving double-small-point gate

Status: [x] Complete.

After the fixed-curve void, the relevant raw and third-face elliptic quotients satisfy the exact mirror identity

\[
\boxed{j_W(s)=j_R(-s)}.
\]

Moreover

\[
j_R(s)-j_W(s)=512\frac{(s^2+1)(s^2-s-1)(s^2+s-1)}{s(s-1)^2(s+1)^2},
\]

so the two quotient curves never have equal j-invariant at a physical rational base `s>0`, `s!=1`.

A physical triple with `d<=B` therefore requires compatible rational points on the reflected pair

\[
E_+(s),\qquad E_+(-s),
\]

coming from the same Humbert--Edge point / physical `q`, with both induced points in logarithmic canonical-height windows of shape `O(log B + log H)`.

This is the moving triple gate left after 4ak. No nonisogeny theorem or simultaneous-small-point density estimate is claimed.

## 14-t7 — simultaneous reflected-pair sieve

Status: [>] Next.

Attack the remaining gate by one or more of:

1. simultaneous first-small-point counting for `E_+(s)` and `E_+(-s)`;
2. shared-`q` local incompatibility / descent-class sieve;
3. a uniform physical-height rational-point estimate on the moving Humbert--Edge fiber product.

The target remains

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
PRIMARY_TARGET=T(B)=o(sqrt(B))
NEXT=Stage14-t7 simultaneous reflected-pair small-point/local-compatibility sieve
```
