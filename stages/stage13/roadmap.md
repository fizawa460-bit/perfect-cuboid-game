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
STAGE13_5=COMPLETE
STAGE13_6=COMPLETE_AT_STRUCTURAL_FINITE_DIAGNOSTIC_LEVEL
NEXT_TASK=Stage13-7 asymptotic behaviour of the deviation
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

Canonical destination: `stages/stage13/main.md` §3

Priority: ★★★★★ Required

Status: [x] Complete at structural finite-diagnostic level

Working result: canonical archimedean geometry creates the leading `ab` excess, and arithmetic representation density materially flattens it toward the observed near-`2`. The exactly-one sieve, standalone prime `2`, universal Stage12 projection fiber, and largest audited cutoff boundary do not generate the leading effect. This is not yet a categorywise asymptotic theorem.

### Task 13-4 — Origin of the two 1s

Explain why the `ac_only` and `bc_only` components are close, and determine whether the two near-`1` contributions arise from the same mechanism or from different mechanisms with similar size.

Canonical destination: `stages/stage13/main.md` §4

Priority: ★★★★★ Required

Status: [x] Complete at structural finite-diagnostic level

Working result: the two near-`1` components are not produced by one exact `ac<->bc` symmetry. At late audited scales, pure-`G` OE/EE and low/high geometric subregions have opposite signed `ac-bc` gaps and cancel strongly. A relatively stable primitive-support factor near `1.06` then supplies most of the residual `ac>bc` tilt, while supported-shell restoration is close to neutral for `ac/bc` at `B=100000`. No asymptotic equality is claimed.

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

Use the two independent coordinates

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

At `B=100000`, exact-one gives

\[
\alpha\approx0.0007796,
\qquad
\beta\approx0.0073677,
\]

so `|beta|/|alpha|≈9.45`. This is finite only.

Canonical destination: `stages/stage13/main.md` §5

Support:

```text
stages/stage13/scripts/13-5/deviation.py
stages/stage13/data/13-5/deviation_report.json
```

Priority: ★★★★★ Required

Status: [x] Complete

### Task 13-6 — Classify the deviation

Classify `alpha`, `beta`, and the full deviation vector by the structural layers already isolated in Stages13-3 and 13-4.

The classification deliberately distinguishes exact transitions from comparison models and controls; it does **not** sum every mechanism as though they were one orthogonal causal decomposition.

At `B=100000` the common-coordinate ledger is:

```text
layer                 alpha          beta
archimedean geometry  +0.0347369     +0.0127276
G-neutral             +0.0394378     +0.0002325
shell-neutral         +0.0361159     +0.0068666
raw                    +0.0006421     +0.0073599
exact-one              +0.0007796     +0.0073677
outer-half raw         +0.0009925     +0.0069049
OE raw                 +0.0200227     +0.0086447
EE raw                 -0.0256078     +0.0056199
```

The exact finite normalized-weight transitions give

```text
G-neutral -> shell-neutral : Delta alpha ~= -0.003322, Delta beta ~= +0.006634
shell-neutral -> raw       : Delta alpha ~= -0.035474, Delta beta ~= +0.000493
raw -> exact-one           : Delta alpha ~= +0.000138, Delta beta ~= +0.0000078
```

Hence the main finite flattening of the leading-half mode `alpha` is associated with restoration of supported-shell richness, while the pure-`G` profile nearly cancels `beta`; primitive-support coupling then restores most of the positive residual `beta`. OE and EE have opposite raw `alpha` signs and reconstruct raw exactly; after pure-`G` deweighting their `ac/bc` gaps also have opposite signs. The largest outer-half control changes the raw modes only slightly. The Stage12 universal projection factor `2` is exactly invisible in normalized directional proportions, and standalone prime-`2` admissibility remains category-symmetric before canonical/order coupling.

This is a finite structural classification only. Geometry is a comparison model, OE/EE a stratification, boundary a control, and the fiber factor an exact null; they must not be added indiscriminately as causal vectors.

Canonical destination: `stages/stage13/main.md` §6

Support:

```text
stages/stage13/scripts/13-6/classify_deviation.py
stages/stage13/data/13-6/deviation_classification_report.json
```

Priority: ★★★★★ Required

Status: [x] Complete at structural finite-diagnostic level

### Task 13-7 — Asymptotic behaviour

Study whether

\[
\alpha(B),\qquad \beta(B),\qquad \Delta(B)
\]

tend to zero, tend to nonzero limits, remain oscillatory at visible scale, or admit identifiable secondary terms. Separate what finite data suggest from what can actually be proved.

Canonical destination: `stages/stage13/main.md` §7

Priority: ★★★★☆ Supporting

Status: [>] Next

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
13-6 Deviation classification [complete: structural finite diagnostic]
        |
        v
13-7 Asymptotic behavior [next]
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
- [x] the significant finite deviation mechanisms have been structurally classified;
- [ ] the asymptotic behavior of the deviation has been resolved to the justified level;
- [ ] the Stage12-to-Stage13 counting bridge has been fully consolidated for exact-one directional counts;
- [ ] the main structural theorem has been proved;
- [ ] the final explanation answers why the ratio naturally appears.

## Scope note

Stage13 is a structural investigation. It does not assume that the limiting ratio is exactly `2:1:1`.

The canonical mathematical truth for active Stage13 work is the latest merged `stages/stage13/main.md`. Historical initial files remain useful provenance, but future repair-by-new-file proliferation is intentionally avoided.
