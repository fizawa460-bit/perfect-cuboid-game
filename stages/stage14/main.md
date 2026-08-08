# Stage14 — primitive canonical exactly-two-face population

> **STATUS:** `STAGE14_3A_COMPLETE_14_3B_NEXT_14_4_PAUSED`
>
> **TRACK:** integer-space-diagonal / two-integral-face layer
>
> **CANONICAL_WORKING_FILE:** `stages/stage14/main.md`

Stage14 studies primitive canonical cuboids with integer space diagonal and **exactly two** integral face diagonals. The finite census is independently audited through `B=2,000,000`. Stage14 proceeds only through finite directional diagnostics in Stage14-3, then stops before asymptotic work until the one-face / Stage13 proof review is settled.

## §1. Locked counting convention

For `B>=1`, consider positive integers

\[
0<a<b<c,
\qquad \gcd(a,b,c)=1,
\qquad a^2+b^2+c^2=d^2,
\qquad d\le B.
\]

Define face-square indicators

\[
I_{ab}=\mathbf 1_{a^2+b^2=\square},\qquad
I_{ac}=\mathbf 1_{a^2+c^2=\square},\qquad
I_{bc}=\mathbf 1_{b^2+c^2=\square}.
\]

Let

\[
O_{ab,ac}=\sum I_{ab}I_{ac},\qquad
O_{ab,bc}=\sum I_{ab}I_{bc},\qquad
O_{ac,bc}=\sum I_{ac}I_{bc},
\]

and

\[
T=\sum I_{ab}I_{ac}I_{bc}.
\]

The exactly-two directional populations are

\[
N_a^{(2)}=O_{ab,ac}-T,
\qquad
N_b^{(2)}=O_{ab,bc}-T,
\qquad
N_c^{(2)}=O_{ac,bc}-T,
\]

where

```text
a-direction = ab+ac only = smallest shared edge
b-direction = ab+bc only = middle shared edge
c-direction = ac+bc only = largest shared edge
```

and

\[
N_2=N_a^{(2)}+N_b^{(2)}+N_c^{(2)}.
\]

No perfect-cuboid nonexistence assumption is made. Any `T>0` object must be preserved with the full exact diagonal witness.

### §1.1 Stage13 analytic quarantine

Stage13 is under independent proof review. A previously recorded Stage13-derived little-o statement is **not an input to current Stage14 conclusions**.

Current finite work satisfies

```text
STAGE13_CODE_IMPORTED=false
STAGE13_ASYMPTOTIC_RESULT_USED=false
```

## §2. Stage14-2 — frozen finite census

Two materially different exact enumeration routes agree at all 11 audited cutoffs through `B=2,000,000`.

| B | N_a^(2) | N_b^(2) | N_c^(2) | N_2 | T | c-normalized ratio |
|---:|---:|---:|---:|---:|---:|---|
| 1,000 | 2 | 0 | 0 | 2 | 0 | undefined |
| 2,000 | 2 | 2 | 1 | 5 | 0 | `2 : 2 : 1` |
| 5,000 | 6 | 6 | 3 | 15 | 0 | `2 : 2 : 1` |
| 10,000 | 9 | 11 | 5 | 25 | 0 | `1.8 : 2.2 : 1` |
| 20,000 | 16 | 16 | 10 | 42 | 0 | `1.6 : 1.6 : 1` |
| 50,000 | 24 | 24 | 14 | 62 | 0 | `1.714286 : 1.714286 : 1` |
| 100,000 | 33 | 33 | 23 | 89 | 0 | `1.434783 : 1.434783 : 1` |
| 200,000 | 42 | 50 | 24 | 116 | 0 | `1.75 : 2.083333 : 1` |
| 500,000 | 70 | 78 | 40 | 188 | 0 | `1.75 : 1.95 : 1` |
| 1,000,000 | 98 | 101 | 56 | 255 | 0 | `1.75 : 1.803571 : 1` |
| 2,000,000 | 142 | 134 | 80 | 356 | 0 | `1.775 : 1.675 : 1` |

Frozen source:

```text
stages/stage14/data/14-2/final_census_audit.json
```

No triple object was found through `B=2,000,000`. This is only a finite search statement.

## §3. Stage14-3 — finite directional diagnostics only

Stage14-3 studies finite trajectories

\[
N_a^{(2)}:N_b^{(2)}:N_c^{(2)}
\]

and

\[
P_q^{(2)}(B)=\frac{N_q^{(2)}(B)}{N_2(B)}.
\]

It may use ratios, finite differences, shell increments, local slopes, or diagnostic fits, but none may be promoted to an asymptotic theorem in Stage14-3.

### §3.1 Stage14-3a — descriptive directional ledger

Stage14-3a records the frozen trajectory without fitting any model.

Artifacts:

```text
stages/stage14/scripts/14-3/directional_ledger.py
stages/stage14/data/14-3/directional_ledger.json
stages/stage14/archive/stage14-3a-directional-ledger.md
```

#### §3.1.1 Late cumulative trajectory

| B | N_a/N_c | N_b/N_c | N_a/N_b | leader |
|---:|---:|---:|---:|---|
| 100,000 | 1.434783 | 1.434783 | 1.000000 | tie a/b |
| 200,000 | 1.750000 | 2.083333 | 0.840000 | b |
| 500,000 | 1.750000 | 1.950000 | 0.897436 | b |
| 1,000,000 | 1.750000 | 1.803571 | 0.970297 | b |
| 2,000,000 | 1.775000 | 1.675000 | 1.059701 | a |

The exact finite equality

\[
\boxed{N_a^{(2)}/N_c^{(2)}=7/4}
\]

holds at the sampled cutoffs `200k`, `500k`, and `1m`. At `2m` it becomes `1.775`.

This is a **finite plateau observation only**. It is not evidence strong enough to declare `7/4` a limit, invariant, or theorem.

Over the same four late sampled cutoffs,

```text
N_b/N_c = 2.083333 -> 1.950000 -> 1.803571 -> 1.675000
```

while

```text
N_a/N_b = 0.840000 -> 0.897436 -> 0.970297 -> 1.059701.
```

Thus the sampled `b -> a` leader reversal is descriptively better viewed as erosion of the finite `b` advantage while `a/c` remains comparatively stable.

#### §3.1.2 Shell composition

The late shell increments are

```text
100k -> 200k: delta(a,b,c)=(9,17,1)
200k -> 500k: delta(a,b,c)=(28,28,16)
500k -> 1m:   delta(a,b,c)=(28,23,16)
1m   -> 2m:   delta(a,b,c)=(44,33,24)
```

Their sampled leaders are therefore

```text
b -> tie(a,b) -> a -> a.
```

This shows directly that the cumulative directional ratios are being driven by materially different finite shell compositions. A simple monotone-drift interpretation is not justified on the current sparse grid.

#### §3.1.3 What is and is not established

Stage14-3a establishes only:

```text
finite a/b leader crossing between sampled 1m and 2m points
finite a/c=7/4 plateau at sampled 200k, 500k, 1m points
finite decreasing b/c sequence on sampled 200k..2m points
strongly changing shell composition
```

It does not establish:

```text
an asymptotic ratio
an asymptotic growth law
a monotonicity theorem
that 7/4 is a true constant or limit
that the late b/c decline continues
any Stage13-dependent claim
```

### §3.2 Next finite task — Stage14-3b

The sparse late grid is not enough to decide whether the observed plateau/crossing are robust finite features or sampling artifacts.

Stage14-3b therefore densifies the finite cutoff grid, especially from `B=100k` through `B=2m` and near the sampled `a/b` crossing between `1m` and `2m`.

This remains a finite enumeration/diagnostic task and requires no Stage13 analytic input.

## §4. Stop line

Current research policy is

```text
Stage14-3b+ finite directional diagnostics        NEXT / ALLOWED
Stage14-4    true total growth order              PAUSED
Stage14-5    directionwise asymptotic structure  PAUSED
```

Stage14 stops after Stage14-3. Stage14-4 and Stage14-5 resume only after the one-face / Stage13 proof review clarifies which structural results are reliable enough to serve as a proof-level starting point.

```text
STAGE14_3A=COMPLETE
DESCRIPTIVE_LEDGER_COMPLETE=true
A_C_FINITE_PLATEAU_OBSERVED=true
A_B_LEADER_CROSSING_OBSERVED=true
FINITE_RATIO_LIMIT_IDENTIFIED=false
MONOTONE_CONVERGENCE_SUPPORTED=false
STAGE13_ANALYTIC_DEPENDENCY_USED=false
NEXT=Stage14-3b late-range finite cutoff densification
STOP_AFTER_STAGE14_3=true
STAGE14_4_STATUS=PAUSED_PENDING_ONE_FACE_REVIEW
STAGE14_5_STATUS=PAUSED_PENDING_ONE_FACE_REVIEW
```
