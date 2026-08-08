# Stage13 — structural analysis

Stage13 studies the primitive canonical exactly-one-face directional counts

\[
N_{ab}(B),\qquad N_{ac}(B),\qquad N_{bc}(B)
\]

and explains both the finite near-`2:1:1` observation and its asymptotic behaviour.

## Current state

```text
STAGE13_1=COMPLETE
STAGE13_2=COMPLETE
STAGE13_3=COMPLETE_AT_STRUCTURAL_DIAGNOSTIC_LEVEL
STAGE13_3A=COMPLETE
STAGE13_3B=COMPLETE
STAGE13_3C=COMPLETE
STAGE13_3D=COMPLETE
STAGE13_3E=COMPLETE
STAGE13_3F=COMPLETE
STAGE13_4=COMPLETE_AT_STRUCTURAL_FINITE_DIAGNOSTIC_LEVEL
STAGE13_4A=COMPLETE
STAGE13_4B=COMPLETE
STAGE13_4C=COMPLETE
STAGE13_5=COMPLETE
STAGE13_6=COMPLETE_AT_STRUCTURAL_FINITE_DIAGNOSTIC_LEVEL
STAGE13_7=COMPLETE_AT_UNCONDITIONAL_EXACT_ONE_DIRECTIONAL_ASYMPTOTIC_LEVEL
STAGE13_8=COMPLETE
STAGE13_9=COMPLETE_MAIN_STRUCTURAL_THEOREM
NEXT=Stage13-10
```

The active roadmap is

```text
stages/stage13/roadmap.md
```

and the Stage13 working-file policy is

```text
stages/stage13/policy.md
```

The policy designates

```text
stages/stage13/main.md
```

as the canonical living mathematical source. Its §8 contains the rigorous Stage12-to-Stage13 bridge and §9 contains the Stage13 main structural theorem. Frozen task-end snapshots are provenance only.

## Main structural theorem

Let

\[
\mathbf N(B)=\bigl(N_{ab}(B),N_{ac}(B),N_{bc}(B)\bigr).
\]

With the canonical chamber integrals

```text
I_ab = 0.659705248705705
I_ac = 0.3026997526726076
I_bc = 0.2712955487578571
I_ab+I_ac+I_bc = pi^2/8
```

Stage13-9 records the principal theorem

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

Thus, categorywise,

\[
N_q(B)\sim\frac{\kappa I_q}{3\pi^3}B(\log B)^3,
\qquad q\in\{ab,ac,bc\},
\]

and

\[
N_1(B)\sim\frac{\kappa}{24\pi}B(\log B)^3.
\]

The normalized limit is

```text
P_inf = (0.5347369332313988,
         0.24535917783225203,
         0.21990388893634913)

N_ab:N_ac:N_bc
 -> 2.431684750178191 : 1.115756428951881 : 1
```

so the limiting ratio is not `2:1:1`.

Relative to the finite baseline `(1/2,1/4,1/4)`,

```text
alpha -> 0.034736933231398814
beta  -> 0.01272764444795145

Delta_inf = ( 0.034736933231398814,
             -0.004640822167747971,
             -0.03009611106365087 )
```

At `B=100000`, by contrast,

```text
alpha ~= 0.0007796226864250431
beta  ~= 0.007367731952627507
```

so the finite near-`2:1:1` vector is strongly pre-asymptotically flattened.

No monotone convergence or explicit secondary convergence rate is claimed.

## Stage12 bridge

For `q in {ab,ac,bc}`, let `C_prim,q^proj(B)` be the Stage12 primitive oriented records whose distinguished integral face becomes canonical category `q` after sorting. Stage13-8 proves exactly

\[
C^{\rm proj}_{\rm prim,q}(B)=2A_q(B)
\]

and

\[
C_{\rm prim}(B)=2(A_{ab}+A_{ac}+A_{bc}).
\]

The universal factor `2` is the two orders of the distinguished face legs and is direction-neutral.

Since Stage13-7 proves every pair overlap and the triple overlap are `o(B(log B)^3)`, the direct Stage12-to-main-theorem bridge is

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

No perfect-cuboid nonexistence assumption is used.

Stage12 remains frozen at R09 and supplies only the primitive oriented count theorem, primitive convention, and `kappa/eta` constant ledger. The directional refinement and overlap removal are Stage13 results.

## Structural synthesis

Stages13-3 through 13-6 explain the accessible finite regime, while Stages13-7 through 13-9 determine and package the asymptotic law.

- canonical archimedean geometry creates the directional ordering `ab>ac>bc` and the chamber vector that survives asymptotically;
- representation-rich supported shells strongly flatten the finite `ab` excess;
- pure-`G` OE/EE and geometric subregions have opposite `ac-bc` gaps and can cancel strongly;
- primitive support materially changes the finite residual `ac-bc` tilt;
- the exactly-one overlap sieve is tiny at finite audited bounds and lower order asymptotically;
- the universal Stage12 projection multiplicity `2` is direction-neutral;
- asymptotically, arithmetic population factors change the absolute scale but not the leading normalized chamber vector.

Thus the near-`2:1:1` observation is a pre-asymptotic cancellation/flattening regime sitting in front of the stronger chamber limit.

## Audit assets

```text
stages/stage13/data/13-7/consolidation_audit_report.json
stages/stage13/data/13-8/bridge_ledger_report.json
stages/stage13/data/13-8/final_cross_reference_audit_report.json
stages/stage13/scripts/13-9/main_structural_theorem_audit.py
stages/stage13/data/13-9/main_structural_theorem_audit_report.json
```

The Stage13-9 audit checks the chamber normalization, directional ratios, deviation vector, exact factor-2 projection, and finite `B=100000` inclusion-exclusion checksum. It introduces no new analytic theorem.

## Logical scope

The main theorem neither proves nor disproves the existence of a perfect cuboid. A perfect cuboid, if one exists, lies in the triple-overlap population, which Stage13 proves is lower order relative to the one-face main term.

Stage13 also does not currently claim:

- an explicit convergence rate;
- an effective threshold for prescribed closeness to the limiting vector;
- monotonicity of the directional ratios;
- independent publication-grade verification of the fixed-modulus analytic input.

## Next — Stage13-10

Stage13-10 is the final explanatory synthesis. Its job is not to discover another asymptotic constant, but to give the clean answer to the original question:

> Why do accessible finite counts look close to `2:1:1` even though the proved asymptotic limit is approximately `2.4317:1.1158:1`?

It should connect the finite shell/primitive/parity cancellations with the asymptotic chamber theorem in one readable narrative, while preserving the distinction between finite diagnostics and theorem-level claims.

## File rule

Stage13 mathematical corrections normally go directly into canonical `main.md`; Git/PR history records prior versions. Support assets use task-first paths such as

```text
stages/stage13/scripts/13-<task>/<purpose>.py
stages/stage13/data/13-<task>/<purpose>.json
```

Frozen task-end snapshots under `stages/stage13/archive/` are provenance, not replacements for the living canonical file.
