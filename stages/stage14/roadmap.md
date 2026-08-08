# Stage14 roadmap — exactly-two integral-face population

## Goal

Count and explain the primitive canonical exactly-two-face population inside the integer-space-diagonal cuboid family.

The three canonical directions are indexed by their shared edge:

```text
a-direction = ab+ac only
b-direction = ab+bc only
c-direction = ac+bc only
```

## 14-1 — Definition and counting interface

Priority: required

```text
14-1a  lock ambient object, exactly-two categories, raw-pair/triple ledger   [complete]
14-1b  connect to historical pair-overlap notation and checksums             [complete]
14-1c  lock enumeration/output specification                                [complete]
```

Locked ambient population:

\[
0<a<b<c,
\qquad \gcd(a,b,c)=1,
\qquad a^2+b^2+c^2=d^2,
\qquad d\le B.
\]

Stage13 is under independent proof review. Its analytic claims are not inputs to current Stage14 finite work.

Status: [x] Complete.

## 14-2 — Complete finite enumeration

Priority: required

### 14-2a — standalone historical reproduction

Status: [x] Complete.

The Stage14 production enumerator

```text
stages/stage14/scripts/14-2/two_face_census.py
```

imports no Stage13 counting code and reproduces the historical seven rows exactly.

### 14-2b — verified extension above B=100000

Status: [x] Complete.

The same Stage14-owned enumerator reaches the full preferred ladder:

```text
B=200,000      (42,50,24)    N2=116   T=0
B=500,000      (70,78,40)    N2=188   T=0
B=1,000,000    (98,101,56)   N2=255   T=0
B=2,000,000    (142,134,80)  N2=356   T=0
```

The finite leader is `b` through `B=1m`, then `a` at `B=2m`.

### 14-2c — finite-census closure / audit

Status: [x] Complete.

A logically separate audit route is implemented at

```text
stages/stage14/scripts/14-2/shared_leg_crosscheck.py
```

It joins two Pythagorean faces on a shared leg first, then tests the integer space diagonal. This differs from the production route, which starts from a distinguished face and glues that face diagonal into a space-diagonal Pythagorean triple.

The two routes agree exactly at all 11 audited cutoffs:

| B | N_a^(2) | N_b^(2) | N_c^(2) | N_2 | T |
|---:|---:|---:|---:|---:|---:|
| 1,000 | 2 | 0 | 0 | 2 | 0 |
| 2,000 | 2 | 2 | 1 | 5 | 0 |
| 5,000 | 6 | 6 | 3 | 15 | 0 |
| 10,000 | 9 | 11 | 5 | 25 | 0 |
| 20,000 | 16 | 16 | 10 | 42 | 0 |
| 50,000 | 24 | 24 | 14 | 62 | 0 |
| 100,000 | 33 | 33 | 23 | 89 | 0 |
| 200,000 | 42 | 50 | 24 | 116 | 0 |
| 500,000 | 70 | 78 | 40 | 188 | 0 |
| 1,000,000 | 98 | 101 | 56 | 255 | 0 |
| 2,000,000 | 142 | 134 | 80 | 356 | 0 |

All exact pair/triple/exactly-two identities pass. No triple object is found in the verified range; this is not a perfect-cuboid nonexistence result.

Canonical audit records:

```text
stages/stage14/data/14-2/final_census_audit.json
stages/stage14/data/14-2/shared_leg_crosscheck_report.json
stages/stage14/archive/stage14-2c-census-closure.md
```

Decision:

```text
STAGE14_2=COMPLETE
FINITE_CENSUS_FROZEN=true
INDEPENDENT_GENERATION_ROUTES=2
ALL_11_ROWS_MATCH=true
MAX_VERIFIED_B=2000000
STAGE13_ANALYTIC_DEPENDENCY_USED=false
```

## 14-3 — Finite directional-ratio evolution

Priority: required

Study

\[
N_a^{(2)}:N_b^{(2)}:N_c^{(2)}
\]

and normalized proportions over the frozen 11-row census. Account explicitly for the finite leader reversal. Candidate fits or extrapolations may be used only as diagnostics, not as theorems.

Stage14-3 should also record what later analytic work would need to explain, so it can serve as a finite-data map once the one-face proof review is settled.

Status: [>] Next.

## STOP LINE after Stage14-3

Current research policy is to stop Stage14 after the finite Stage14-3 diagnostics.

The reason is structural: the one-face / Stage13 proof is under external review, so beginning the harder two-face asymptotic proof before the reliable one-face machinery is identified would amount to proceeding without a trustworthy map.

## 14-4 — True total growth order

Priority: major analytic task

Determine the correct asymptotic order of

\[
N_2(B).
\]

Status: **paused pending one-face / Stage13 proof review**.

When resumed, fine-grained substages may begin at `14-4aa`.

## 14-5 — Directionwise asymptotic structure

Priority: major analytic task

Determine the directionwise scales/constants and the mechanism controlling their ratios.

Status: **paused pending one-face / Stage13 proof review**.

When resumed, fine-grained substages may begin at `14-5aa`.

## Scope boundary

Stage14 does not assume perfect-cuboid nonexistence. `T(B)` remains explicit and any `T>0` witness must be preserved and independently verified.

The fact that all currently verified rows through `B=2,000,000` have `T=0` is only a finite observation. No growth exponent, limiting directional ratio, monotonicity, or relation to the Euler-side two-face limit is assumed before it is independently established.
