# Stage13 — Structural Origin of the 2:1:1 Ratio

## Goal

Stage13 does **not** assume or force an exact `2:1:1` limit. Its goal is to explain why a ratio close to `2:1:1` appears in the finite primitive canonical exactly-one-face count, identify the dominant structural mechanisms, determine the justified asymptotic law, and connect that law rigorously to the frozen Stage12 oriented theorem.

Stage12-N1-2 remains frozen at R09.

The canonical mathematical working source is

```text
stages/stage13/main.md
```

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
STAGE13_10=COMPLETE_FINAL_EXPLANATION
STAGE13=COMPLETE
NEXT_STAGE13_TASK=NONE
```

The final normalized directional law is

\[
P(B)\to
\left(
\frac{8I_{ab}}{\pi^2},
\frac{8I_{ac}}{\pi^2},
\frac{8I_{bc}}{\pi^2}
\right)
\]

with

```text
P_inf = (0.5347369332313988,
         0.24535917783225203,
         0.21990388893634913)

ab:ac:bc -> 2.431684750178191 : 1.115756428951881 : 1
```

so the limiting law is not `2:1:1`.

---

## Phase 1 — Define and decompose

### Task 13-1 — Definition

Status: [x] Complete

Fix the primitive canonical object, space-diagonal cutoff, exactly-one condition and the directional labels `ab/ac/bc`.

### Task 13-2 — Structural decomposition

Status: [x] Complete

Separate raw incidence, overlap correction, canonical chamber, orientation, primitive, parity, representation multiplicity, local-density and boundary layers.

---

## Phase 2 — Explain the finite directional shape

### Task 13-3 — Origin of the leading 2

Status: [x] Complete at structural finite-diagnostic level

Canonical archimedean geometry creates the `ab` excess. Arithmetic representation density materially flattens it at accessible cutoffs. The exactly-one sieve, standalone prime `2`, universal Stage12 projection fiber and largest audited boundary do not create the leading effect.

### Task 13-4 — Origin of the two near-1 components

Status: [x] Complete at structural finite-diagnostic level

There is no exact `ac<->bc` symmetry. Opposite-signed OE/EE and pure-`G` contributions cancel strongly, while primitive support supplies much of the residual positive `ac-bc` finite tilt.

---

## Phase 3 — Quantify and resolve the deviation

### Task 13-5 — Define the deviation

Status: [x] Complete

For

\[
P_0=(1/2,1/4,1/4),
\qquad
\Delta(B)=P(B)-P_0,
\]

define

\[
\alpha(B)=P_{ab}(B)-1/2,
\qquad
\beta(B)=\frac{P_{ac}(B)-P_{bc}(B)}2.
\]

### Task 13-6 — Classify the finite deviation

Status: [x] Complete at structural finite-diagnostic level

Supported-shell richness dominates the diagnosed finite flattening of `alpha`; parity/pure-`G` cancellations and primitive support explain much of the finite `beta` structure.

### Task 13-7 — Asymptotic behaviour

Status: [x] Complete at unconditional exact-one directional asymptotic level

For `q in {ab,ac,bc}`,

\[
N_q(B)\sim\frac{\kappa I_q}{3\pi^3}B(\log B)^3,
\]

and

\[
N_1(B)\sim\frac{\kappa}{24\pi}B(\log B)^3.
\]

Pair and triple overlaps are `o(B(log B)^3)` with no perfect-cuboid nonexistence assumption.

---

## Phase 4 — Connect, state and explain

### Task 13-8 — Stage12 structural connection

Status: [x] Complete

The exact directional projection is

\[
C^{\rm proj}_{\rm prim,q}(B)=2A_q(B),
\]

hence

\[
N_q(B)=\frac12C^{\rm proj}_{\rm prim,q}(B)+o(B(\log B)^3).
\]

Stage12 remains frozen and no new bridge lemma is required.

### Task 13-9 — Main structural theorem

Status: [x] Complete

The principal vector theorem is

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

It records the normalized chamber limit, Stage12 bridge, deviation corollary and logical scope.

### Task 13-10 — Final explanation

Status: [x] Complete

The apparent finite/asymptotic discrepancy is resolved as follows:

- the canonical chamber and one-face real density create the persistent `ab>ac>bc` geometric backbone;
- finite supported-shell richness strongly flattens the `ab` advantage;
- finite parity/pure-`G`/primitive-support couplings create substantial cancellations in the `ac-bc` direction;
- the exactly-one overlap correction is not the source of the near-`2:1:1` shape and is asymptotically lower order;
- the arithmetic factor surviving in the leading main term is common across directions, so it cancels after normalization and the chamber vector returns.

Therefore

```text
finite near-2:1:1
= long pre-asymptotic flattening of the stronger chamber bias
```

as explanatory shorthand, not as an exact algebraic identity.

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
13-8 Stage12 bridge [complete]
        |
        v
13-9 Main structural theorem [complete]
        |
        v
13-10 Final explanation [complete]
        |
        v
STAGE13 COMPLETE
```

## Completion checklist

- [x] observed ratio rigorously defined;
- [x] structural layers separated;
- [x] dominant finite mechanism behind the leading near-`2` identified;
- [x] finite relation between the two near-`1` components explained;
- [x] deviation coordinates defined;
- [x] significant finite deviation mechanisms classified;
- [x] asymptotic directional behaviour resolved;
- [x] Stage12-to-Stage13 counting bridge consolidated;
- [x] main structural theorem stated;
- [x] final finite-versus-asymptotic explanation written.

## Scope boundary after completion

Stage13 does **not** settle:

- perfect-cuboid existence or nonexistence;
- the true growth law of the two-face population;
- an explicit convergence rate or effective closeness threshold;
- monotonicity of the directional ratios;
- independent publication-grade verification.

Those are outside the completed Stage13 claim and can be assigned to later work without reopening Stage13 unless a concrete contradiction is found.

## Final assets

```text
stages/stage13/main.md
stages/stage13/README.md
stages/stage13/data/13-10/final_explanation_audit_report.json
stages/stage13/archive/stage13-10-final.md
```
