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

The Stage14-4ah third-square cover of the physical Kummer surface has branch class `2M`. On an extremal rational bisection with

\[
M\cdot C=4,
\]

the restricted branch degree is `8`. A transverse restriction has eight odd branch points and normalized genus

\[
\boxed{3}.
\]

Thus a generic raw-pair `sqrt(B)` accumulating bisection does **not** remain rational or elliptic after imposing the third square. A low-genus triple restriction requires at most four odd branch points, i.e. exceptional branch contact/tangency.

```text
STAGE14_T4=COMPLETE_ELLIPTIC_COMPRESSION_AND_KUMMER_RESTRICTION
ELLIPTIC_FACTOR_COUNT=5
GEOMETRIC_ELLIPTIC_J_TYPES=3
RAW_PAIR_FACTOR=E_R
THIRD_FACE_FACTOR=E_W
PHYSICAL_TRIPLE_IMPLIES_E_R_POSITIVE_RANK_SPECIALIZATION=true
KUMMER_TRIPLE_BRANCH_CLASS=2M
M_DEGREE4_RESTRICTED_BRANCH_DEGREE=8
GENERIC_M_DEGREE4_TRIPLE_LIFT_GENUS=3
LOW_GENUS_TRIPLE_RESTRICTION_REQUIRES_ODD_BRANCH_SUPPORT_LE_4=true
T_O_SQRT_B_PROVED=false
```

## 14-t5 — transfer gate

Status: [>] Next, but conditional on the main-track degree-four bisection classification / branch-contact audit.

Use

\[
N_2(B)=E(B)-3T(B)
\]

to transfer a proved raw-pair law only after the surviving triple restrictions are controlled at the same scale. If the main `14-4` track produces the physical `M`-degree-4 bisections, the immediate t-side task is to compute the odd branch support of the `2M` third-square divisor on each one.

## Scope boundary

Stage14-t is a population-counting track, not a finite-search proof of perfect-cuboid nonexistence.

```text
STAGE14_T_TRACK=ACTIVE
STAGE14_T1=COMPLETE_BASELINE_AND_THEOREM_GAP
STAGE14_T2=COMPLETE_QUANTITATIVE_BOUNDARY
STAGE14_T3=COMPLETE_HUMBERT_EDGE_AND_ELLIPTIC_SPLITTING
STAGE14_T4=COMPLETE_ELLIPTIC_COMPRESSION_AND_KUMMER_RESTRICTION
PRIMARY_TARGET=T(B)=o(sqrt(B))
NEXT=Stage14-t5 transfer gate / branch-contact audit after main-track bisection classification
```
