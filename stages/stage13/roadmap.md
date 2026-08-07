# Stage13 — Structural Origin of the 2:1:1 Ratio

## Goal

The objective of Stage13 is **not** to assume or force an exact `2:1:1` limit.

The goal is to explain why a ratio close to `2:1:1` appears in the finite canonical exact-one-face count, identify the dominant structural mechanism, and isolate the sources of the remaining deviation.

Stage12-N1-2 is frozen at R09 and supplies the analytic foundation for the primitive oriented count.

## Working-file policy

Stage13 follows:

```text
stages/stage13/policy.md
```

The canonical mathematical working source is

```text
stages/stage13/main.md
```

Task 13-1 through 13-10 are sections of that single living document. The completed initial sources are retained under `stages/stage13/initial/` and are imported into `main.md` when Stage13-3 work begins.

Repair-only patch documents are nondefault. Mathematical corrections are made directly in the relevant section of `main.md`; Git/PR history records the changes. Stage-specific data and scripts use task subdirectories under `stages/stage13/`.

External review is on demand, not a gate for every edit.

## Current status

```text
STAGE12_N1_2=FROZEN_R09
STAGE13_1=COMPLETE
STAGE13_2=COMPLETE
STAGE13_3=COMPLETE_AT_STRUCTURAL_DIAGNOSTIC_LEVEL
STAGE13_4=COMPLETE_AT_STRUCTURAL_FINITE_DIAGNOSTIC_LEVEL
STAGE13_4A=COMPLETE
STAGE13_4B=COMPLETE
STAGE13_4C=COMPLETE
STAGE13_5=COMPLETE
NEXT_TASK=Stage13-6 classify the deviation
```

## Research question

The central question is:

> **Why does the canonical exact-one-face ratio**
> \[
> N_{ab}(B):N_{ac}(B):N_{bc}(B)
> \]
> **appear close to `2:1:1`, and what produces its deviations?**

The reference finite observation at `B=100000` is recorded in Stage13-1; it is motivation, not an asymptotic theorem.

---

## Phase 1 — Define and decompose

### Task 13-1 — Definition

Fix counted objects, normalization, cutoff, equivalence relation, exact-one-face condition, and the relation to Stage12 conventions.

Initial source: `stages/stage13/initial/definition.md`

Canonical destination: `stages/stage13/main.md` §1

Priority: ★★★★★ Required

Status: [x] Complete

### Task 13-2 — Structural decomposition

Decompose the directional counts into raw incidence, overlap correction, canonical size-order, orientation, primitive, parity, representation multiplicity, local-density, and boundary layers.

Initial source: `stages/stage13/initial/structural-decomposition.md`

Canonical destination: `stages/stage13/main.md` §2

Priority: ★★★★★ Required

Status: [x] Complete

---

## Phase 2 — Explain the dominant ratio

### Task 13-3 — Origin of the leading 2

Determine the mathematical origin of the leading factor near `2` in the `ab_only` component.

The analysis distinguishes raw incidence versus exact-one overlap correction, canonical size-order geometry, full-orientation symmetry, primitive projection, parity / 2-adic structure, representation multiplicity, odd-prime local densities, cutoff/boundary effects, and the exact Stage12-to-Stage13 fiber map.

Canonical destination: `stages/stage13/main.md` §3

Priority: ★★★★★ Required

Status: [x] Complete at structural finite-diagnostic level

Working result: canonical archimedean geometry creates the leading `ab` excess, and arithmetic representation density materially flattens it toward the observed near-`2`. This is not yet a categorywise asymptotic theorem.

### Task 13-4 — Origin of the two 1s

Explain why the `ac_only` and `bc_only` components are close, and determine whether the two near-`1` contributions arise from the same mechanism or from different mechanisms with similar size.

Canonical destination: `stages/stage13/main.md` §4

Priority: ★★★★★ Required

Status: [x] Complete at structural finite-diagnostic level

Stage13-4a established the finite layer ledger. At `B=100000`, the `ac/bc` gap survives the exact-one sieve and outer-half boundary essentially unchanged. Supported shell-neutralization also leaves the aggregate ratio near `1.061`, while pure `G(p)` deweighting moves it to about `1.002`.

Stage13-4b showed that the pure-`G` near equality is a cancellation rather than a proved symmetry. At `B=100000`, pure-`G` OE is `0.95422` with negative weighted gap while EE is `1.04547` with positive weighted gap. Geometric bins also cross from `bc`-heavy to `ac`-heavy, and primitive support systematically favors `ac`.

Stage13-4c scales this structure. The exact finite layer identity

```text
r_raw(B) = r_G(B) * F_prim(B) * F_shell(B)
```

separates pure-`G`, primitive-support and supported-shell effects. For `B>=10000`, `F_prim` stays in the narrow range `1.05872..1.06499`. At `B=100000`,

```text
1.0607458 = 1.0020209 * 1.0588757 * 0.9997457.
```

The outer half `50000<d<=100000` independently reproduces opposite OE/EE pure-`G` signs (`0.95636` versus `1.05368`) and the low-`g` to high-`g` crossing (`0.9087, 0.9729, 1.0605, 1.1176`). Thus the two near-`1` components are structurally explained at the audited finite scale as cross-stratum cancellation plus a relatively stable primitive-support tilt, not by one exact `ac<->bc` symmetry. The cancellation is not stable at all smaller bounds or annuli, so no asymptotic equality or exact secondary constant is claimed.

---

## Phase 3 — Explain the deviation

### Task 13-5 — Define the deviation

For the exact-one proportions

\[
P(B)=\frac{1}{N_1(B)}(N_{ab}(B),N_{ac}(B),N_{bc}(B)),
\]

define

\[
P_0=\left(\frac12,\frac14,\frac14\right),\qquad
\Delta(B)=P(B)-P_0.
\]

Since the components of `Delta` sum to zero, use the two coordinates

\[
\alpha(B)=P_{ab}(B)-\frac12,
\qquad
\beta(B)=\frac{P_{ac}(B)-P_{bc}(B)}2,
\]

so that exactly

\[
\Delta(B)=\alpha(B)\left(1,-\frac12,-\frac12\right)
+\beta(B)(0,1,-1).
\]

`alpha` is the leading-vs-pair mode; `beta` is the split of the two near-`1` components. Exact `2:1:1` is equivalent to `alpha=beta=0`.

At `B=100000`, exact-one gives

\[
\alpha=\frac{131}{168030}\approx0.0007796,
\qquad
\beta=\frac{619}{84015}\approx0.0073677.
\]

Thus `|beta|/|alpha|≈9.45` at the largest audited cutoff; the finite normalized deviation is dominated in coordinate size by the `ac/bc` split rather than by failure of `ab` to equal one half. No trend or limit is inferred from this definition.

Canonical destination: `stages/stage13/main.md` §5

Support:

```text
stages/stage13/scripts/13-5/deviation.py
stages/stage13/data/13-5/deviation_report.json
```

Priority: ★★★★★ Required

Status: [x] Complete

### Task 13-6 — Classify the deviation

Decompose `alpha`, `beta`, and the full deviation vector into structurally meaningful components such as overlap, canonical geometry, parity/local arithmetic, representation density, primitive support, and finite-cutoff effects.

Canonical destination: `stages/stage13/main.md` §6

Priority: ★★★★★ Required

Status: [>] Next

### Task 13-7 — Asymptotic behaviour

Study whether the deviation tends to zero, tends to another limit, remains bounded away from zero, or has identifiable secondary terms.

Canonical destination: `stages/stage13/main.md` §7

Priority: ★★★★☆ Supporting

Status: [ ] Not started

---

## Phase 4 — Connect with Stage12

### Task 13-8 — Structural connection

Construct the rigorous bridge from the frozen Stage12 primitive oriented count to the Stage13 canonical exact-one-face directional counts.

Objects include the Stage12 parameter records, the map to canonical objects / distinguished faces / orientations, fiber multiplicity, `kappa`, `eta` and local factors, overlap removal, parity and canonical-order restrictions.

Canonical destination: `stages/stage13/main.md` §8

Priority: ★★★★★ Required

Status: [ ] Not started

Note: Stage13-3d already proved the exact primitive oriented-to-canonical raw-incidence projection multiplicity `2` and transferred the Stage12 total asymptotic to `A_ab+A_ac+A_bc`; Task 13-8 will later consolidate that bridge together with overlap removal and the remaining directional structure.

### Task 13-9 — Main structural theorem

Formulate and prove the principal structural result in a form such as

\[
\text{directional count vector}
=
\text{dominant structural term}
+
\text{explicit correction terms}.
\]

Canonical destination: `stages/stage13/main.md` §9

Priority: ★★★★★ Required

Status: [ ] Not started

---

## Phase 5 — Final synthesis

### Task 13-10 — Final explanation

Answer:

> **Why does a ratio close to `2:1:1` naturally emerge?**

Canonical destination: `stages/stage13/main.md` §10

Priority: ★★★★★ Required

Status: [ ] Not started

---

## Dependency graph

```text
Stage12 R09 frozen
        |
        v
13-1 Definition [complete]
        |
        v
13-2 Structural decomposition [complete]
        |
        v
13-3 Origin of leading 2 [complete: structural finite diagnostic]
        |
        v
13-4 Origin of two 1s [complete: structural finite diagnostic]
        |
        v
13-5 Deviation definition [complete]
        |
        v
13-6 Deviation classification [next]
        |
        v
13-7 Asymptotic behavior
        |
        v
13-8 Rigorous Stage12 bridge
        |
        v
13-9 Main structural theorem
        |
        v
13-10 Final explanation
```

## Completion checklist

Stage13 is complete when:

- [x] the observed ratio has been rigorously defined;
- [x] the candidate structural layers have been separated;
- [x] the dominant finite structural mechanism producing the leading near-`2` has been identified;
- [x] the finite structural relation between the two near-`1` components has been explained;
- [x] a quantitative deviation vector and independent coordinates have been defined;
- [ ] every significant deviation has been structurally classified;
- [ ] the Stage12-to-Stage13 counting bridge has been fully consolidated for exact-one directional counts;
- [ ] the main structural theorem has been proved;
- [ ] the final explanation answers why the ratio naturally appears.

## Scope note

Stage13 is a structural investigation. It does not assume that the limiting ratio is exactly `2:1:1`.

The canonical mathematical truth for active Stage13 work is the latest merged `stages/stage13/main.md`. Historical initial files remain useful provenance, but future repair-by-new-file proliferation is intentionally avoided.
