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

Stage13 is under independent proof review. Its analytic claims are not inputs to current Stage14 finite work.

## 14-1 — Definition and counting interface

Status: [x] Complete.

## 14-2 — Complete finite enumeration

Status: [x] Complete.

Two materially different exact generation routes agree at all 11 audited cutoffs through `B=2,000,000`.

Canonical audit:

```text
stages/stage14/data/14-2/final_census_audit.json
```

## 14-3 — Finite directional-ratio evolution

Priority: required and final active Stage14 block before the stop line.

Only finite diagnostics are allowed here. No finite fit is promoted to an asymptotic theorem.

### 14-3a — descriptive directional ledger

Status: [x] Complete.

The coarse late sample showed an apparent `a/c=7/4` plateau at `200k,500k,1m` and a cumulative `b -> a` leader reversal between `1m` and `2m`.

Artifacts:

```text
stages/stage14/scripts/14-3/directional_ledger.py
stages/stage14/data/14-3/directional_ledger.json
stages/stage14/archive/stage14-3a-directional-ledger.md
```

### 14-3b — late-range finite cutoff densification

Status: [x] Complete.

The production finite census was densified on

```text
B=100,000,150,000,...,2,000,000
step=50,000
39 rows
```

and the exact space-diagonal event stream was inspected around the `a/b` crossing.

Main findings:

1. The coarse repeated equality `a/c=7/4` is not a stable finite law. The 50k grid moves substantially between the coarse sample points, so no invariant or limit is inferred.
2. The finite `a/b` crossing is localized by exact event values:

```text
d=1,083,121   b lead -> tie
 d=1,096,685  tie -> b lead
 d=1,127,185  b lead -> tie
 d=1,148,545  tie -> a lead
```

After `d=1,148,545`, `a>b` at every subsequent exactly-two event state through the verified ceiling `B=2,000,000`.

This is finite only; eventual asymptotic dominance is unknown.

Artifacts:

```text
stages/stage14/scripts/14-3/late_range_densification.py
stages/stage14/data/14-3/late_range_densification.json
stages/stage14/archive/stage14-3b-late-range-densification.md
```

Decision:

```text
STAGE14_3B=COMPLETE
DENSE_FINITE_GRID_STEP=50000
A_OVER_C_7_4_LIMIT_SUPPORTED=false
A_B_CROSSING_LOCALIZED=true
FINAL_A_OVER_B_CROSSING_D_WITHIN_VERIFIED_RANGE=1148545
ASYMPTOTIC_FIT_PERFORMED=false
```

### 14-3c — finite diagnostic synthesis / stop-line preparation

Status: [>] Next.

Purpose:

- consolidate what the finite census actually establishes;
- separate robust finite observations from artifacts of sparse sampling;
- record the open questions any later Stage14-4 proof must explain;
- close Stage14-3 and enforce the current stop line.

No Stage13 theorem is needed for this synthesis.

## STOP LINE after Stage14-3

Current research policy is to stop Stage14 after finite Stage14-3 diagnostics.

## 14-4 — True total growth order

Status: **paused pending one-face / Stage13 proof review**.

## 14-5 — Directionwise asymptotic structure

Status: **paused pending one-face / Stage13 proof review**.

## Scope boundary

Stage14 does not assume perfect-cuboid nonexistence. `T(B)` remains explicit and any `T>0` witness must be preserved and independently verified.

No growth exponent, limiting directional ratio, monotonicity theorem, eventual leader, or Euler-side equality is currently established for the two-face population.
