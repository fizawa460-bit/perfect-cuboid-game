# Stage14 roadmap — exactly-two integral-face population

## Goal

Count and explain the primitive canonical exactly-two-face population inside the integer-space-diagonal cuboid family.

```text
a-direction = ab+ac only
b-direction = ab+bc only
c-direction = ac+bc only
```

Locked ambient population:

\[
0<a<b<c,\qquad \gcd(a,b,c)=1,\qquad a^2+b^2+c^2=d^2,\qquad d\le B.
\]

Current finite Stage14 work is independent of Stage13 analytic claims while Stage13 remains under external proof review.

## 14-1 — Definition and counting interface

Status: [x] Complete.

## 14-2 — Complete finite enumeration

Status: [x] Complete.

Two materially different exact generation routes agree at all 11 audited cutoffs through `B=2,000,000`.

Canonical audit:

```text
stages/stage14/data/14-2/final_census_audit.json
```

## 14-3 — Finite directional-ratio reconnaissance

Status: [x] Complete.

Only finite diagnostics were allowed. No finite fit was promoted to an asymptotic theorem.

### 14-3a — descriptive directional ledger

Status: [x] Complete.

The coarse late sample exposed an apparent `a/c=7/4` pattern and a cumulative `b -> a` reversal.

### 14-3b — late-range finite cutoff densification

Status: [x] Complete.

The finite population was densified on

```text
B=100,000,150,000,...,2,000,000
step=50,000
39 rows
```

and the exact event stream was inspected around the `a/b` crossing.

The coarse `a/c=7/4` pattern is not stable under densification and is not retained as an invariant or limit candidate.

The last `a/b` crossing in the verified event stream is

```text
d=1,148,545   tie -> a lead
counts after = (107,106,60)
```

with `a>b` at every subsequent exactly-two event state through `B=2,000,000`. This is finite only.

### 14-3c — finite diagnostic synthesis / closure

Status: [x] Complete.

Stage14-3c separates the final record into:

```text
robust finite facts
sparse-grid artifacts / unsupported promotions
open questions for later proof-level work
```

Canonical synthesis:

```text
stages/stage14/data/14-3/final_finite_reconnaissance.json
stages/stage14/archive/stage14-3c-final-finite-reconnaissance.md
```

Locked decision:

```text
STAGE14_3A=COMPLETE
STAGE14_3B=COMPLETE
STAGE14_3C=COMPLETE
STAGE14_3=COMPLETE
FINITE_RECONNAISSANCE_COMPLETE=true
MAX_VERIFIED_B=2000000
DENSE_FINITE_GRID_STEP=50000
A_OVER_C_7_4_LIMIT_SUPPORTED=false
FINAL_A_OVER_B_CROSSING_D_WITHIN_VERIFIED_RANGE=1148545
ASYMPTOTIC_FIT_PERFORMED=false
FINITE_RATIO_LIMIT_IDENTIFIED=false
STAGE13_ANALYTIC_DEPENDENCY_USED=false
```

## STOP LINE — ACTIVE

Current research policy is now active, not merely planned:

```text
Stage14-1   COMPLETE
Stage14-2   COMPLETE
Stage14-3   COMPLETE
Stage14-4   PAUSED_PENDING_ONE_FACE_REVIEW
Stage14-5   PAUSED_PENDING_ONE_FACE_REVIEW
```

There is no planned `14-3d`.

## 14-4 — True total growth order

Status: **paused pending one-face / Stage13 proof review**.

When resumed, begin with

```text
14-4aa  independent two-face parametrization and proof-input audit
```

rather than blindly importing the old Stage13 proof chain. Every Stage13 dependency must be re-audited before use.

## 14-5 — Directionwise asymptotic structure

Status: **paused pending one-face / Stage13 proof review**.

## Open analytic questions retained for restart

- What is the true growth order of `N_2(B)`?
- Do the three exactly-two directions have limiting normalized proportions?
- Does the finite `a` lead persist or reverse again?
- What arithmetic mechanism distinguishes the three shared-edge directions?
- What is the correct proof-level parametrization for two simultaneous Pythagorean-face conditions plus integer space diagonal?
- Which repaired Stage13 tools can be reused safely?
- How does this population compare with the Euler/no-space-diagonal two-face population?
- Can `T(B)>0` ever occur? No nonexistence claim is made.

## Scope boundary

No growth exponent, limiting directional ratio, monotonicity theorem, eventual leader, Euler-side equality, or perfect-cuboid nonexistence result is currently established for Stage14.

```text
STOP_LINE_ACTIVE=true
NEXT=WAIT_FOR_ONE_FACE_REVIEW_BEFORE_STAGE14_4
```
