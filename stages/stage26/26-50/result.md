# Stage26-50 — Saunderson construction lower ledger

EVIDENCE_LEVEL=PROVED_DERIVED_THEOREM_CANDIDATE
CHECKPOINT=50
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
DEPENDS_ON=Stage20,Stage18,Stage25-reentry-60,Stage26-30,Stage26-40

## 1. Explicit primitive canonical Euler subfamily

Use the audited Stage20 Saunderson construction. For every even integer `m>=10`, Stage20 constructs one distinct primitive canonical Euler cuboid and proves the common Euclidean height bound

\[
R(m)<31m^6.
\]

Hence every even `m>=10` with

\[
m\le (B/31)^{1/6}
\]

produces a distinct object counted by `M3(B)`.

Define the certified construction count

\[
\boxed{
F_S(B):=\max\left(0,\left\lfloor\frac12(B/31)^{1/6}\right\rfloor-4\right).
}
\]

This is exactly the number of even integers `m>=10` satisfying the displayed sufficient cutoff condition. Therefore

\[
\boxed{M_3(B)\ge F_S(B)}.
\]

Writing

\[
\boxed{c_S:=\frac{1}{2\,31^{1/6}}},
\]

one has

\[
\boxed{F_S(B)=c_SB^{1/6}+O(1)}.
\]

Thus the Stage20 lower theorem is strengthened here from an anonymous Vinogradov constant to an explicit audited subfamily coefficient:

\[
\liminf_{B\to\infty}\frac{M_3(B)}{B^{1/6}}\ge c_S>0.
\]

This is a lower statement for one explicit subfamily. It is not an asymptotic formula for `M3`.

## 2. Construction floor for the Stage26 adjacent-stratum ratio

Stage18 gives

\[
M_2(B)\sim C_{M_2}B(\log B)^5,\qquad C_{M_2}>0.
\]

Therefore the explicit family gives

\[
\boxed{
\liminf_{B\to\infty}
B^{5/6}(\log B)^5\frac{M_3(B)}{M_2(B)}
\ge \frac{c_S}{C_{M_2}}>0.
}
\]

Equivalently,

\[
\frac{M_3(B)}{M_2(B)}
\not=o\!\left(B^{-5/6}(\log B)^{-5}\right).
\]

This does **not** say that `B^(-5/6)(log B)^(-5)` is the true scale. The full Euler population may be much larger than the Saunderson subfamily.

## 3. Literal physical-object completion floor

Checkpoint30 proved

\[
H_{\ge2}(B)=M_2(B)+M_3(B)\sim C_{M_2}B(\log B)^5
\]

and

\[
\Phi(B)=\frac{M_3(B)}{H_{\ge2}(B)}.
\]

Hence the same explicit subfamily yields

\[
\boxed{
\liminf_{B\to\infty}
B^{5/6}(\log B)^5\Phi(B)
\ge \frac{c_S}{C_{M_2}}>0.
}
\]

Thus the literal third-face completion fraction tends to zero by checkpoint30/40, but it cannot decay faster than the certified construction floor above.

## 4. Raw-incidence completion floors

Checkpoint30 also proved

\[
P(B)=M_2(B)+3M_3(B)\sim C_{M_2}B(\log B)^5,
\qquad
\Theta(B)=\frac{3M_3(B)}{P(B)}.
\]

Every Saunderson Euler cuboid contributes three completed shared-edge incidences. Therefore

\[
\boxed{
\liminf_{B\to\infty}
B^{5/6}(\log B)^5\Theta(B)
\ge \frac{3c_S}{C_{M_2}}>0.
}
\]

For each fixed shared-edge chamber `j`, the audited phase60 receiver gives

\[
P_j(B)\sim C_jB(\log B)^5,\qquad C_j>0,
\]

and every Euler cuboid contributes exactly once to that chamber. Hence

\[
\boxed{
\liminf_{B\to\infty}
B^{5/6}(\log B)^5\Theta_j(B)
\ge \frac{c_S}{C_j}>0.
}
\]

No directional asymptotic for `M3` is used.

## 5. Combined Stage26 corridor after checkpoints40 and50

Checkpoint40 gives, for every fixed `0<delta<1/46`,

\[
\frac{M_3}{M_2},\ \Phi,\ \Theta,\ \Theta_j
=o((\log B)^{-\delta}).
\]

Checkpoint50 supplies a constructive nonvanishing floor at the much smaller scale `B^(-5/6)(log B)^(-5)`.

Thus the current certified corridor remains wide:

\[
B^{-5/6}(\log B)^{-5}
\ \lesssim\ \text{completion rate}\
=o((\log B)^{-\delta})
\qquad(0<\delta<1/46),
\]

with a positive explicit lower `liminf` constant supplied by the Saunderson subfamily.

The two sides do not match, so the true Euler-brick/completion exponent remains open.

## 6. Construction mechanism and boundary

The load-bearing construction facts imported from Stage20 are:

```text
PARAMETER=m even, m>=10
ONE_PARAMETER_PYTHAGOREAN_INPUT=(m^2-1,2m,m^2+1)
OUTPUT=primitive Euler cuboid
CANONICAL_ORDERING_PROVED=true
INJECTIVITY_PROVED=true
EUCLIDEAN_HEIGHT_BOUND=R<31m^6
EXPLICIT_FAMILY_COUNT=F_S(B)
```

Checkpoint50 does not claim that this one-parameter family explains the bulk geometry of `M3`. It proves a durable constructive floor only.

```text
TASK_ID=Stage26-50
CHECKPOINT=50
EXPLICIT_SAUNDERSON_COUNT_CANDIDATE=true
EXPLICIT_SUBFAMILY_COEFFICIENT_CANDIDATE=true
ADJACENT_RATIO_POSITIVE_LIMINF_CANDIDATE=true
PHI_POSITIVE_LIMINF_CANDIDATE=true
THETA_POSITIVE_LIMINF_CANDIDATE=true
DIRECTIONAL_THETA_POSITIVE_LIMINF_CANDIDATE=true
LOWER_SCALE_MATCHING_TRUE_SCALE_PROVED=false
M3_ASYMPTOTIC_PROVED=false
TRUE_M3_EXPONENT_IDENTIFIED=false
FINITE_DATA_USED_AS_ASYMPTOTIC_PROOF=false
PERFECT_CUBOID_CONCLUSION=NONE
AUDIT_STATUS=PENDING
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT=60
MERGE_ALLOWED=false
NEXT_EXPECTED_COMMAND=Stage26-audit
```
