# Stage13 — Structural Origin of the 2:1:1 Ratio

## Goal

Stage13 does **not** assume or force an exact `2:1:1` limit. Its goal is to explain why a ratio close to `2:1:1` appears in the finite primitive canonical exactly-one-face count, identify the dominant structural mechanisms, and determine the justified asymptotic law.

Stage12-N1-2 remains frozen at R09 and supplies the analytic foundation for the primitive oriented count.

The canonical mathematical working source remains

```text
stages/stage13/main.md
```

with support scripts/data under task-specific directories. Frozen task-end snapshots may live under `stages/stage13/archive/` as provenance, consistent with `stages/stage13/policy.md`.

## Current status

```text
STAGE12_N1_2=FROZEN_R09
STAGE13_1=COMPLETE
STAGE13_2=COMPLETE
STAGE13_3=COMPLETE_AT_STRUCTURAL_DIAGNOSTIC_LEVEL
STAGE13_4=COMPLETE_AT_STRUCTURAL_FINITE_DIAGNOSTIC_LEVEL
STAGE13_5=COMPLETE
STAGE13_6=COMPLETE_AT_STRUCTURAL_FINITE_DIAGNOSTIC_LEVEL
STAGE13_7=COMPLETE_AT_UNCONDITIONAL_EXACT_ONE_DIRECTIONAL_ASYMPTOTIC_LEVEL
STAGE13_8=COMPLETE
STAGE13_9=COMPLETE_MAIN_STRUCTURAL_THEOREM
NEXT_TASK=Stage13-10 final explanation
```

The Stage13-7 theorem is frozen for provenance in

```text
stages/stage13/archive/stage13-7-final.md
```

and Stage13-8 in

```text
stages/stage13/archive/stage13-8-final.md
```

with machine audits in

```text
stages/stage13/data/13-7/consolidation_audit_report.json
stages/stage13/data/13-8/bridge_ledger_report.json
stages/stage13/data/13-8/final_cross_reference_audit_report.json
stages/stage13/data/13-9/main_structural_theorem_audit_report.json
```

## Research question

The central question remains:

> **Why does the canonical exact-one-face ratio**
> \[
> N_{ab}(B):N_{ac}(B):N_{bc}(B)
> \]
> **appear close to `2:1:1`, and what produces its deviations?**

The finite observation near `2:1:1` is strongly pre-asymptotic. The Stage13 main theorem gives the normalized limiting vector

\[
(0.5347369332313988,
 0.24535917783225203,
 0.21990388893634913),
\]

equivalently

\[
2.431684750178191:1.115756428951881:1.
\]

---

## Phase 1 — Define and decompose

### Task 13-1 — Definition

Fix counted objects, normalization, cutoff, equivalence relation, exactly-one-face condition, and the relation to Stage12 conventions.

Priority: ★★★★★ Required

Status: [x] Complete

### Task 13-2 — Structural decomposition

Decompose the directional counts into raw incidence, overlap correction, canonical size-order, orientation, primitive, parity, representation multiplicity, local-density, and boundary layers.

Priority: ★★★★★ Required

Status: [x] Complete

---

## Phase 2 — Explain the dominant finite ratio

### Task 13-3 — Origin of the leading 2

Status: [x] Complete at structural finite-diagnostic level

Working result: canonical archimedean geometry creates the leading `ab` excess, and arithmetic representation density materially flattens it at accessible cutoffs. The exactly-one sieve, standalone prime `2`, universal Stage12 projection fiber, and largest audited cutoff boundary do not generate the leading effect.

### Task 13-4 — Origin of the two 1s

Status: [x] Complete at structural finite-diagnostic level

Working result: the two near-`1` components are not produced by an exact `ac<->bc` symmetry. At accessible cutoffs, opposite-signed pure-`G` OE/EE and geometric contributions cancel strongly, while primitive support supplies much of the residual positive `ac-bc` tilt.

---

## Phase 3 — Explain the deviation

### Task 13-5 — Define the deviation

For

\[
P(B)=\frac{1}{N_1(B)}(N_{ab}(B),N_{ac}(B),N_{bc}(B)),
\]

define

\[
P_0=\left(\frac12,\frac14,\frac14\right),
\qquad
\Delta(B)=P(B)-P_0,
\]

and

\[
\alpha(B)=P_{ab}(B)-\frac12,
\qquad
\beta(B)=\frac{P_{ac}(B)-P_{bc}(B)}2.
\]

Status: [x] Complete

### Task 13-6 — Classify the finite deviation

Status: [x] Complete at structural finite-diagnostic level

At `B=100000`, the finite exact-one deviation is `beta`-dominated. The main finite flattening of `alpha` is associated with supported-shell richness, while pure-`G` cancellation and primitive-support coupling explain much of the observed `beta` structure. These are finite structural statements, not the limiting law.

### Task 13-7 — Asymptotic behaviour

Priority: ★★★★☆ Supporting

Status: [x] Complete at unconditional exact-one directional asymptotic level

Stage13-7 proves

\[
N_q(B)\sim\frac{\kappa I_q}{3\pi^3}B(\log B)^3,
\qquad q\in\{ab,ac,bc\},
\]

and

\[
N_1(B)\sim\frac{\kappa}{24\pi}B(\log B)^3.
\]

Therefore

\[
P(B)\to
\left(
\frac{8I_{ab}}{\pi^2},
\frac{8I_{ac}}{\pi^2},
\frac{8I_{bc}}{\pi^2}
\right),
\]

and the asymptotic ratio is not `2:1:1`.

The proof chain is:

```text
13-7j   individual pure-G asymptotics
13-7ja  primitive-support scale transition
13-7jb  shell-richness restoration and raw directional asymptotics
13-7jc  exact overlap / face-cuboid reduction
13-7jd  uniform elliptic-height upper bound (historical intermediate route)
13-7je  Kummer/coupled-height reduction (structural intermediate route)
13-7jf  fixed-prime sieve: pair/triple overlaps are lower order; transfer to exact-one
13-7jg  final constant/dependency/order-of-limits audit
```

No perfect-cuboid nonexistence assumption is used. No explicit normalized convergence rate or monotonicity theorem is claimed.

---

## Phase 4 — Connect, state, explain

### Task 13-8 — Structural connection

Priority: ★★★★★ Required

Status: [x] Complete

For `q in {ab,ac,bc}`,

\[
C^{\rm proj}_{\rm prim,q}(B)=2A_q(B)
\]

exactly, and

\[
C_{\rm prim}(B)=2(A_{ab}+A_{ac}+A_{bc}).
\]

Every pair overlap and the triple overlap are lower order, so

\[
\boxed{
N_q(B)=\frac12C^{\rm proj}_{\rm prim,q}(B)+o(B(\log B)^3)
}
\]

and

\[
\boxed{
N_1(B)=\frac12C_{\rm prim}(B)+o(B(\log B)^3).
}
\]

Stage12 remains frozen; no new mathematical bridge lemma was required.

### Task 13-9 — Main structural theorem

Priority: ★★★★★ Required

Status: [x] Complete

The principal Stage13 theorem is now stated canonically in `stages/stage13/main.md` §9:

\[
\boxed{
\mathbf N(B)
=
\frac{\kappa}{3\pi^3}
(I_{ab},I_{ac},I_{bc})
B(\log B)^3
+o(B(\log B)^3).
}
\]

It includes as corollaries:

\[
N_1(B)\sim\frac{\kappa}{24\pi}B(\log B)^3,
\]

\[
\frac{\mathbf N(B)}{N_1(B)}
\to
\frac8{\pi^2}(I_{ab},I_{ac},I_{bc}),
\]

and

```text
ab:ac:bc -> 2.431684750178191 : 1.115756428951881 : 1
```

with the direct Stage12 bridge

\[
N_q(B)=\frac12C^{\rm proj}_{\rm prim,q}(B)+o(B(\log B)^3).
\]

The theorem explicitly records that perfect-cuboid nonexistence is not assumed, no effective convergence rate is proved, no monotonicity is claimed, and independent publication-grade review is still outside the current completion standard.

### Task 13-10 — Final explanation

Give the final answer to why a ratio close to `2:1:1` appears at accessible cutoffs even though the proved limit is the chamber vector above.

Priority: ★★★★★ Required

Status: [>] Next

The final synthesis should connect:

- the canonical chamber geometry that determines the asymptotic vector;
- the finite supported-shell flattening of the `ab` advantage;
- the parity/pure-`G`/primitive-support cancellations affecting `ac-bc`;
- the lower-order nature of exactly-one overlap removal;
- the distinction between a long pre-asymptotic regime and the true limiting law.

It should not introduce a new asymptotic theorem unless a concrete gap is discovered.

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
13-3 Leading-2 finite mechanism [complete]
        |
        v
13-4 Two-near-1 finite mechanism [complete]
        |
        v
13-5 Deviation definition [complete]
        |
        v
13-6 Finite deviation classification [complete]
        |
        v
13-7 Asymptotic behaviour [complete]
        |
        v
13-8 Stage12 bridge consolidation [complete]
        |
        v
13-9 Main structural theorem [complete]
        |
        v
13-10 Final explanation [NEXT]
```

## Completion checklist

Stage13 is complete when:

- [x] the observed ratio has been rigorously defined;
- [x] the candidate structural layers have been separated;
- [x] the dominant finite structural mechanism producing the leading near-`2` has been identified;
- [x] the finite structural relation between the two near-`1` components has been explained;
- [x] a quantitative deviation vector and independent coordinates have been defined;
- [x] the significant finite deviation mechanisms have been structurally classified;
- [x] the asymptotic behaviour of the deviation has been resolved to the justified level;
- [x] the Stage12-to-Stage13 counting bridge has been fully consolidated in canonical form;
- [x] the main structural theorem has been formulated in final Stage13 form;
- [ ] the final explanation has been written.

## Scope note

Stage13 is a structural investigation. The Stage13 main theorem proves a non-`2:1:1` limiting directional vector and a rigorous bridge from the frozen Stage12 oriented theorem at the same project theorem standard as the frozen Stage12 analytic chain. It does not claim perfect-cuboid existence/nonexistence, an independently peer-reviewed publication proof, an explicit convergence rate, or a certified numerical enclosure for `kappa`.
