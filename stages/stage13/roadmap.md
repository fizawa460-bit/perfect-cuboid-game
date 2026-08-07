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
STAGE13_4=ACTIVE
STAGE13_4A=COMPLETE
STAGE13_4B=COMPLETE
NEXT_TASK=Stage13-4c scaling of ac/bc cancellation
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

The analysis must distinguish at least:

- raw incidence versus exact-one overlap correction;
- canonical size-order geometry;
- full-orientation symmetry;
- primitive projection;
- parity / 2-adic structure;
- representation multiplicity;
- odd-prime local densities;
- cutoff and boundary effects;
- the exact Stage12-to-Stage13 fiber map.

Canonical destination: `stages/stage13/main.md` §3

Priority: ★★★★★ Required

Status: [x] Complete at structural finite-diagnostic level

Working result: canonical archimedean geometry creates the leading `ab` excess, and arithmetic representation density materially flattens it toward the observed near-`2`. This is not yet a categorywise asymptotic theorem.

### Task 13-4 — Origin of the two 1s

Explain why the `ac_only` and `bc_only` components are close, and determine whether the two near-`1` contributions arise from the same mechanism or from different mechanisms with similar size.

Canonical destination: `stages/stage13/main.md` §4

Priority: ★★★★★ Required

Status: [>] Active

Stage13-4a established the finite layer ledger. At `B=100000`, the `ac/bc` gap survives the exact-one sieve and outer-half boundary essentially unchanged. Supported shell-neutralization also leaves the aggregate ratio near `1.061`, while pure `G(p)` deweighting moves it to about `1.002`. OE and EE respond to shell-neutralization in opposite directions.

Stage13-4b shows that the pure-`G` near equality is itself a cancellation rather than a proved symmetry. At `B=100000`, pure-`G` OE has `ac/bc=0.95422` and weighted gap about `-254.28`, while EE has `ac/bc=1.04547` and gap about `+277.86`; the residual total gap is only about `+23.58`, giving aggregate `1.00202`. The outer half preserves the same sign split. Across smaller cutoffs the pure-`G` aggregate is not uniformly near `1`, so no stable equality law has yet been established. Geometric bins defined by `g=w_ac/w_bc` also cross from `bc`-heavy to `ac`-heavy, and the primitive-support factor `R_all/R_prim` systematically favors `ac` over `bc`. Therefore no cutoff-preserving weight-preserving exact `ac<->bc` involution can explain the finite totals; the current explanation is cross-stratum arithmetic/geometric cancellation.

Next: Stage13-4c — test how that OE/EE and geometric cancellation scales with `B` and whether a stable secondary balance law can be isolated.

---

## Phase 3 — Explain the deviation

### Task 13-5 — Define the deviation

Introduce a quantitative deviation vector or scalar `Delta` from the reference proportion

\[
\left(\frac12,\frac14,\frac14\right).
\]

Canonical destination: `stages/stage13/main.md` §5

Priority: ★★★★★ Required

Status: [ ] Not started

### Task 13-6 — Classify the deviation

Decompose the deviation into structurally meaningful components such as overlap, canonical boundary, multiplicity, parity/local, and finite-cutoff effects.

Canonical destination: `stages/stage13/main.md` §6

Priority: ★★★★★ Required

Status: [ ] Not started

### Task 13-7 — Asymptotic behaviour

Study whether the deviation tends to zero, tends to another limit, remains bounded away from zero, or has identifiable secondary terms.

Canonical destination: `stages/stage13/main.md` §7

Priority: ★★★★☆ Supporting

Status: [ ] Not started

---

## Phase 4 — Connect with Stage12

### Task 13-8 — Structural connection

Construct the rigorous bridge from the frozen Stage12 primitive oriented count to the Stage13 canonical exact-one-face directional counts.

Objects include:

- the Stage12 parameter records;
- the map to canonical objects / distinguished faces / orientations;
- fiber multiplicity;
- `kappa`, `eta` and local factors;
- overlap removal;
- parity and canonical-order restrictions.

No automatic constant-factor identification is permitted before the fiber multiplicity is established.

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
13-4 Origin of two 1s [active: 4a/4b complete, 4c next]
        |
        v
13-5/6/7 Deviation analysis
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
- [ ] the relation between the two near-`1` components has been explained;
- [ ] every significant deviation has been structurally classified;
- [ ] the Stage12-to-Stage13 counting bridge has been fully consolidated for exact-one directional counts;
- [ ] the main structural theorem has been proved;
- [ ] the final explanation answers why the ratio naturally appears.

## Scope note

Stage13 is a structural investigation. It does not assume that the limiting ratio is exactly `2:1:1`.

The canonical mathematical truth for active Stage13 work is the latest merged `stages/stage13/main.md`. Historical initial files remain useful provenance, but future repair-by-new-file proliferation is intentionally avoided.
