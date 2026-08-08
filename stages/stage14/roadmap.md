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

Status: [x] Complete.

Locked ambient population:

\[
0<a<b<c,
\qquad \gcd(a,b,c)=1,
\qquad a^2+b^2+c^2=d^2,
\qquad d\le B.
\]

Stage13 is under independent proof review. Its analytic claims are not inputs to current Stage14 finite work.

## 14-2 — Complete finite enumeration

Status: [x] Complete.

Two materially different exact generation routes agree at all 11 audited cutoffs through `B=2,000,000`.

```text
B=1,000        (2,0,0)      N2=2    T=0
B=2,000        (2,2,1)      N2=5    T=0
B=5,000        (6,6,3)      N2=15   T=0
B=10,000       (9,11,5)     N2=25   T=0
B=20,000       (16,16,10)   N2=42   T=0
B=50,000       (24,24,14)   N2=62   T=0
B=100,000      (33,33,23)   N2=89   T=0
B=200,000      (42,50,24)   N2=116  T=0
B=500,000      (70,78,40)   N2=188  T=0
B=1,000,000    (98,101,56)  N2=255  T=0
B=2,000,000    (142,134,80) N2=356  T=0
```

Canonical audit:

```text
stages/stage14/data/14-2/final_census_audit.json
```

## 14-3 — Finite directional-ratio evolution

Priority: required and final active Stage14 block before the stop line.

Stage14-3 uses only the frozen Stage14-2 census and direct finite extensions. It may diagnose finite ratios, proportions, differences, shells, local slopes, or candidate fits, but it must not promote them to asymptotic theorems.

### 14-3a — descriptive directional ledger

Status: [x] Complete.

Artifacts:

```text
stages/stage14/scripts/14-3/directional_ledger.py
stages/stage14/data/14-3/directional_ledger.json
stages/stage14/archive/stage14-3a-directional-ledger.md
```

Main late-range observations:

```text
B=200k:  a/c=1.75   b/c=2.083333   a/b=0.84
B=500k:  a/c=1.75   b/c=1.95       a/b=0.897436
B=1m:    a/c=1.75   b/c=1.803571   a/b=0.970297
B=2m:    a/c=1.775  b/c=1.675      a/b=1.059701
```

Thus `a/c=7/4` occurs exactly at the three sampled cutoffs `200k`, `500k`, and `1m`, but Stage14 records this only as a finite plateau. The cumulative leader changes from `b` at 1m to `a` at 2m.

Late shell increments are

```text
100k -> 200k: (9,17,1)
200k -> 500k: (28,28,16)
500k -> 1m:   (28,23,16)
1m   -> 2m:   (44,33,24)
```

so shell composition itself changes strongly across the sampled range.

No ratio limit, monotonicity theorem, or growth law is inferred.

### 14-3b — late-range finite cutoff densification

Status: [>] Next.

Purpose: determine whether the apparent `a/c` plateau and `a/b` leader crossing are robust finite features or artifacts of the sparse cutoff grid.

The natural focus is the range from roughly `B=100k` through `B=2m`, with extra resolution near the `a/b` crossing between the sampled `1m` and `2m` points.

This remains a finite-data task. No Stage13 analytic claim is needed.

## STOP LINE after Stage14-3

Current research policy is to stop Stage14 after the finite Stage14-3 diagnostics.

The one-face / Stage13 proof is under external review, so beginning the harder two-face asymptotic proof before the reliable one-face machinery is identified would amount to proceeding without a trustworthy proof-level map.

## 14-4 — True total growth order

Status: **paused pending one-face / Stage13 proof review**.

## 14-5 — Directionwise asymptotic structure

Status: **paused pending one-face / Stage13 proof review**.

## Scope boundary

Stage14 does not assume perfect-cuboid nonexistence. `T(B)` remains explicit and any `T>0` witness must be preserved and independently verified.

The fact that all currently verified rows through `B=2,000,000` have `T=0` is only a finite observation. No growth exponent, limiting directional ratio, monotonicity, or relation to the Euler-side two-face limit is assumed before it is independently established.
