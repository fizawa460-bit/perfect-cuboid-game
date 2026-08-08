# Stage14 — exactly-two integral-face population

Stage14 studies primitive canonical cuboids with integer space diagonal and exactly two integral face diagonals.

## Current state

```text
STAGE14_1=COMPLETE
STAGE14_2=COMPLETE
STAGE14_3A=COMPLETE
STAGE14_3B=COMPLETE
STAGE14_3C=COMPLETE
STAGE14_3=COMPLETE
FINITE_RECONNAISSANCE_COMPLETE=true
MAX_VERIFIED_B=2000000
DENSE_FINITE_GRID_STEP=50000
STAGE13_ANALYTIC_DEPENDENCY_USED=false
STOP_LINE_ACTIVE=true
NEXT=WAIT_FOR_ONE_FACE_REVIEW_BEFORE_STAGE14_4
STAGE14_4_STATUS=PAUSED_PENDING_ONE_FACE_REVIEW
STAGE14_5_STATUS=PAUSED_PENDING_ONE_FACE_REVIEW
```

Canonical source: `stages/stage14/main.md`.

## Counting convention

\[
0<a<b<c,\qquad \gcd(a,b,c)=1,\qquad a^2+b^2+c^2=d^2,\qquad d\le B.
\]

The exactly-two directions are

```text
a = ab+ac only = smallest shared edge
b = ab+bc only = middle shared edge
c = ac+bc only = largest shared edge
```

with

\[
N_a^{(2)}=O_{ab,ac}-T,\qquad
N_b^{(2)}=O_{ab,bc}-T,\qquad
N_c^{(2)}=O_{ac,bc}-T.
\]

No perfect-cuboid nonexistence assumption is made.

## Frozen finite census

Two materially different exact generation routes agree at all 11 audited cutoffs through `B=2,000,000`. At the ceiling,

\[
(N_a^{(2)},N_b^{(2)},N_c^{(2)})=(142,134,80),\qquad N_2=356,\qquad T=0.
\]

No triple object was found through this finite ceiling; this is not a nonexistence proof.

## Stage14-3 finite reconnaissance

Stage14-3a exposed an apparent coarse `a/c=7/4` plateau and a late `b -> a` leader reversal. Stage14-3b densified the range `100k..2m` at 50k spacing and followed the exact event stream near the crossing.

The `7/4` pattern does not survive densification and is rejected as a stable finite law or limiting candidate.

The verified late `a/b` event sequence is

```text
d=1,083,121   a-b: -1 ->  0
d=1,096,685   a-b:  0 -> -1
d=1,127,185   a-b: -1 ->  0
d=1,148,545   a-b:  0 -> +1
```

From `d=1,148,545` through `B=2,000,000`, every subsequent exactly-two event state has `a>b`. This is a finite-range statement only.

Final synthesis:

```text
stages/stage14/data/14-3/final_finite_reconnaissance.json
stages/stage14/archive/stage14-3c-final-finite-reconnaissance.md
```

## What is still unknown

Stage14 has not identified the true growth order of `N_2(B)`, a limiting directional vector, an eventual leader, monotonicity, an Euler-side two-face relation, or whether `T(B)` ever becomes positive.

## Stage13 isolation and active stop line

Current Stage14 finite conclusions use neither Stage13 code nor a Stage13 asymptotic theorem.

```text
14-1   complete
14-2   complete
14-3   complete
14-4   paused pending one-face / Stage13 review
14-5   paused pending one-face / Stage13 review
```

There is no planned `14-3d`. When Stage14 resumes, the recommended first analytic task is `14-4aa`: independent two-face parametrization and proof-input audit, with every imported Stage13 dependency explicitly re-audited.
