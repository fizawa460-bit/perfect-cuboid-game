# Stage32 32-03 — Z1-Z30 survivor comparison — 2026-09-19

Status: **BREADTH COMPLETE / SURVIVOR COMPARISON ONLY / NO MATHEMATICAL CREDIT**

## Target

Close the whole `R29-LG2-MB` population by proving

```text
g(normalization) in {0,1}
=> d <= D
```

or an equivalent finite Picard/intersection window.

The comparison is based on four practical questions:

1. Is the native theorem conclusion population-wide?
2. Does it have strict slack against balanced `000707` rather than equality?
3. Can the next test be performed from retained Stage32 data without rebuilding W16-H?
4. If it works, does it actually imply a finite window rather than only rigidity/filtering?

---

## Survivor A — Z2 canonical-orbifold canonical-degree inequality

**Disposition: PRIMARY.**

Retained numerical facts:

```text
canonical orbifold X:
K_X^2 = 16
c2_orb(X) = 8
s2_orb = 8 > 0
sigma_orb = c2_orb/K^2 = 1/2
```

The balanced hostile ray satisfies the exact slope relation

```text
K_X.C = 2 * deg K_orb(source).
```

Therefore any source-valid population theorem of the shape

```text
K_X.C <= A * deg K_orb(source) + B
```

with `A<2` immediately cuts the tail.

Round 6 Z30 gives an even sharper source target: Miyaoka's smooth aggregate theorem would formally give total low-genus canonical-degree budget `16` after replacing `c2` by `c2_orb`. The substitution is not presently justified, but it shows that the retained orbifold invariants are on the correct side of the exact threshold.

### Next cheap gate A1

Do a theorem/source audit only:

```text
Does an established Miyaoka/McQuillan/Langer/Sakai/orbifold
canonical-degree theorem apply to:
- a canonical surface with 48 A1 quotient singularities,
- curves that may pass through those singularities with multibranch contact,
- normalization genus 0 or 1,
and produce either A<2 or an aggregate total-degree bound?
```

Stop if every available theorem requires the curve to avoid the singular locus, be smooth in the ambient surface, or introduces a boundary/contact term with coefficient >=1 that restores the balanced equality.

Why first: this is the only survivor whose native conclusion is already the desired population-wide degree inequality.

---

## Survivor B — Z21 root-lattice Hodge + Z4' localization/equality breaking

**Disposition: SECONDARY / EXACT INTERNAL ROUTE.**

Z21 is the only new route that already proved a nontrivial piece of the desired finite window:

```text
D^2 + (1/2)sum M_i^2 <= d^2/16.
```

Together with Z11:

```text
g=1, N<8 => d <= 16N/(8-N),
g=0, N<=4 impossible,
g=0, N=5,6,7 => d<=6,17,49.
```

Thus any unbounded sequence must have `N>=8`.

Balanced `000707` is the exact equality model:

```text
N=14,
M_i=8l,
M=d=112l,
D#=7lH,
Cauchy equality + Hodge equality + Z11 equality.
```

This converts the vague multibranch problem into an equality-breaking problem.

### Next cheap gate B1

Classify what an actual carrier must satisfy if Z21 is an equality or near-equality case, then compare that with the retained packet semantics:

```text
Hodge equality -> D# numerically proportional to H
Cauchy equality -> all nonzero M_i equal
Z11 equality -> all differential/contact slack exhausted
```

Ask whether the full R29 packet can realize all three simultaneously outside the known balanced formal ray. If a population theorem forces either
- `N<=7`, or
- nonuniform `M_i`, or
- any strict excess `M>d+O(1)`,
then Z21 converts it into a finite window.

This is the natural composition point for Z4' global singularity localization/collision. No conductor-CB/W16 materialization is needed.

---

## Survivor C — Z12 adaptive higher-order symmetric/jet differentials

**Disposition: TERTIARY / HIGH-UPSIDE RESERVE.**

Z11 shows exactly why fixed-order symmetric differentials stop:

```text
d <= M + 4g - 4,
balanced: g=1, M=d.
```

So the missing theorem must either reduce the coefficient of `M` below one or charge multiplicity/branch complexity more than linearly.

Z12 remains alive because the old W5/order-two tests only ruled out fixed finite order and fixed finite jet depth. They did not rule out an order that grows with contact complexity or a twisted/logarithmic differential whose local weight is multiplicity-sensitive.

### Next cheap gate C1

Before constructing anything, derive the minimum asymptotic local weight needed on the balanced packet. A useful differential must yield a global inequality whose balanced leading term is strictly positive; an architecture whose local penalty is only `1 * M + O(1)` is dead before any section search.

Only if the coefficient test passes should one search explicit higher-order cuboid differentials.

---

## Lower reserves

### Z5' packet-sensitive arithmetic product theorem

Generic product-cover, correspondence, and Nielsen/passport arguments were killed by H5/H6/Z6/Z13/Z20/Z26. It remains logically possible that the exact cuboid packet imposes a special arithmetic relation not visible to generic cover theory. Keep as reserve, but it currently requires more branch-specific input than A/B/C.

### Z3 strong effective-cone / fixed-component theorem

The ray is effective for every `l`, and the known zero-pairing quartics are not fixed. Only a genuinely complete stable-base/effective-cone theorem could revive it. Lower priority than A/B/C.

### Z16' Vojta bounded-gonality canonical-degree theorem shape

Conceptually strong, but retained only as conditional/conjectural input. It is not an active proof route unless a proved theorem with the needed singular/orbifold hypotheses is found.

---

## Recommended three-pass deepening order

```text
Pass A: Z2-A1 source theorem applicability audit
Pass B: Z21/Z4'-B1 equality-case classification
Pass C: Z12-C1 asymptotic coefficient gate
```

Run these as three independent short gates before committing to a long subproject.

Decision rule:

```text
If A1 finds a valid theorem with coefficient <2 -> pursue A immediately.
Else if B1 forces any strictness away from the balanced equality tuple -> pursue B.
Else if C1 admits a differential architecture with balanced coefficient gain -> pursue C.
Otherwise reopen Z5'/Z3 rather than returning automatically to W16-H.
```

## Final Z1-Z30 portfolio

```text
PRIMARY:
  Z2 canonical-orbifold canonical-degree / aggregate low-genus bound

SECONDARY:
  Z21 root-lattice Hodge partial window
  + Z4' localization/equality breaking

TERTIARY:
  Z12 adaptive higher-order symmetric/jet differentials

RESERVES:
  Z5' packet-sensitive arithmetic
  Z3 strong stable-base/effective-cone theorem

CONDITIONAL ONLY:
  Z16' Vojta bounded-gonality theorem shape

HARD / ABSORBED:
  all remaining Z routes as tested
```

## Firewalls

```text
breadth_Z1_Z30_complete=true
finite_degree_window_proved=false
MB104_complete=false
R29_LG2_MB_discharged=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
merge_authorized=false
```
