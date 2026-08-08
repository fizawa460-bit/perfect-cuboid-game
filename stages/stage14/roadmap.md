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
14-1b  connect to the existing pair-overlap notation and inherited checks  [complete]
14-1c  lock enumeration/output specification                               [complete]
```

Stage14-1b inherits the Stage13 seed rows for `B=1000,...,100000`, the exact `B=100000` vector `(33,33,23)` with total `89`, and the theorem-level ceiling

\[
N_a^{(2)},N_b^{(2)},N_c^{(2)},N_2=o(B(\log B)^3).
\]

This inherited little-o statement is not the true two-face asymptotic scale.

Stage14-1c locks the finite enumeration contract:

```text
- exact integer square tests
- canonical dedup by (a,b,c,d)
- all three face flags recomputed after dedup
- raw pair, triple and exactly-two outputs retained
- all seven inherited rows must be reproduced exactly
- at least one verified cutoff above B=100000 is required
- preferred extension ladder: 200k, 500k, 1m, 2m as feasible
- any T>0 record must preserve a full perfect-cuboid witness
- no growth model is built into the enumerator
```

Machine-readable specifications:

```text
stages/stage14/data/14-1/stage13_pair_interface.json
stages/stage14/data/14-1/enumeration_output_spec.json
```

Stage13 proof-review changes do not affect the finite enumeration contract unless they alter the ambient counting object or inherited finite seed counts; in that case Stage14-1b is re-audited.

Status: [x] Complete.

## 14-2 — Complete finite enumeration

Priority: required

Enumerate

```text
O_ab_ac, O_ab_bc, O_ac_bc
T
N_a^(2), N_b^(2), N_c^(2)
N_2
```

at increasing `d<=B` cutoffs.

Acceptance gate:

1. reproduce all seven inherited Stage13 rows exactly;
2. cross-check the optimized implementation against an independent/literal method on feasible small bounds;
3. extend to at least one verified `B>100000` cutoff;
4. satisfy all row identities exactly;
5. retain any triple witness rather than filtering it away.

Preferred extension ladder is `200000, 500000, 1000000, 2000000` as performance allows.

Status: [>] Next.

## 14-3 — Finite directional-ratio evolution

Priority: required

Study

\[
N_a^{(2)}:N_b^{(2)}:N_c^{(2)}
\]

and normalized proportions over the audited cutoff range. Test whether the directions share one apparent growth scale or separate already at finite size.

Status: not started.

## 14-4 — True total growth order

Priority: major analytic task

Determine the correct asymptotic order of

\[
N_2(B).
\]

Stage13 proves only the inherited ceiling

\[
N_2(B)=o(B(\log B)^3),
\]

so Stage14 must determine the actual scale rather than presuppose one.

Fine-grained substages for this task may begin at `14-4aa`.

Status: not started.

## 14-5 — Directionwise asymptotic structure

Priority: major analytic task

After the total scale is understood, determine whether

\[
N_a^{(2)},\quad N_b^{(2)},\quad N_c^{(2)}
\]

share the same exponent/logarithmic scale, whether direction constants exist, and what geometric/arithmetic mechanism controls their ratios.

A later comparison with the face-diagonal-first / Euler-side two-face layer is natural, but equality of the two directional laws is not assumed.

Fine-grained substages for this task may begin at `14-5aa`.

Status: not started.

## Scope boundary

Stage14 does not assume perfect-cuboid nonexistence. The triple population `T(B)` is retained explicitly and removed from each raw pair count when forming the exactly-two populations.

The fact that the inherited Stage13 finite rows have `T=0` is only a finite observation. The theorem `T=o(B(log B)^3)` is a density statement, not a nonexistence theorem.

No growth exponent, limiting directional ratio, monotonicity, or relation to the Euler-side two-face limit is assumed before it is proved or numerically diagnosed.
