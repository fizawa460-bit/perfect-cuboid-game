# Stage14-s roadmap — Selmer / rank-jump arithmetic track

## Purpose

Stage14-s studies the arithmetic bottlenecks behind active Pythagorean first-face states. For a genuine base state `F`, merged Stage14 gives

\[
\mu(F)<\infty\iff \operatorname{rank}E_F(\mathbf Q)>0.
\]

The finite active count through `B=2,000,000` remains compatible with a square-root scale, but no asymptotic is assumed.

## 14-s1 — exact descent / Selmer interface

Status: [x] Complete.

Locked the integral full-2-torsion model

\[
E_F:W^2=Z(Z-S^2)(Z+X^2)
\]

and deterministic active/inactive PARI rank/Selmer audit. Positive rank alone does not explain physical activity.

## 14-s2 — Pythagorean local Selmer architecture

Status: [x] Complete.

Locked the moving bad-prime support `p|2SXH`, exact projective bad-prime densities, and the `H^{o(1)}` per-base covering-class envelope. A fixed auxiliary-prime product sieve does not yield a power saving in the base count.

## 14-s3 — first-small-point / canonical-height gate

Status: [x] Complete.

Merged result:

```text
physical hit d<=B
=> non-torsion elliptic point
=> canonical height O(log B + log H).
```

Finite audit: actual first-hit points on 96 active fibers have median canonical height `3.6080` and maximum `6.5243`; 29 certified-positive-rank inactive controls with deterministic PARI witnesses have witness-height median `10.2839`. The inactive witnesses are not claimed to be shortest generators. Thus the small-point gate is genuinely distinct from positive rank, while a uniform least-generator distribution remains unproved.

## 14-s4 — compare with the M-degree-4 bisection mechanism

Status: [~] Bridge ready; waiting for merged `14-4ai+` explicit/classified bisection artifact.

Stage14-4ah proves that the unique extremal fixed rational-curve pattern compatible with a `B^(1/2)` contribution is

```text
M.C=4
C -> P1_r has degree 2.
```

The s4 arithmetic bridge is now fixed. For every main-track bisection `C`, supply:

```text
normalization parameter z on C~=P1
degree-two base map r(z)
physical coordinates and M-height d(z)
induced elliptic point P_C(z)
physical-open / non-torsion proof
```

s4 then compares the exact s1 Kummer square class

```text
(Z, Z-S^2, Z+X^2) mod squares
```

and specializes it against the exact active first-hit ledger. For `M.C=4`, the fixed-curve rational-point exponent is `2/4=1/2`, so the geometric and arithmetic height mechanisms are compatible. Existence, classification, finite coverage, and dominance cannot be asserted before `14-4ai+` supplies the curves.

```text
STAGE14_S4=BRIDGE_READY_WAITING_FOR_14_4AI
BISECTION_TO_SELMER_COMPARISON_INTERFACE_LOCKED=true
M_DEGREE4_HEIGHT_EXPONENT_COMPATIBILITY_LOCKED=true
EXPLICIT_M_DEGREE4_BISECTION_IMPORTED=false
FINITE_BISECTION_COVERAGE_MEASURED=false
BISECTION_DOMINANCE_PROVED=false
ACTIVE_VERTEX_SQRT_B_ASYMPTOTIC_PROVED=false
```

## 14-s5 — rank-jump counting synthesis

Status: [ ] Pending completed s4 comparison.

Combine the arithmetic and Kummer results into the strongest theorem-level statement for

\[
V(B)=\#\{F:\mu(F)\le B\}.
\]

No `B^{1/2+o(1)}` statement is promoted until bisection existence/classification and the residual population outside those curves are controlled.

## Scope

Stage14-s does not duplicate `14-t` or the main `14-4` Kummer classification. Selmer dimension is not identified with Mordell--Weil rank, PARI witnesses are not identified with shortest generators, and finite square-root diagnostics are not promoted to asymptotics.

```text
STAGE14_S_TRACK=ACTIVE
STAGE14_S1=COMPLETE
STAGE14_S2=COMPLETE
STAGE14_S3=COMPLETE
STAGE14_S4=BRIDGE_READY_WAITING_FOR_14_4AI
S5_TARGET=RANK_JUMP_COUNTING_SYNTHESIS
NEXT=merge/resume Stage14-s4 when 14-4ai+ lands
```
