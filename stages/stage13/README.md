# Stage13 — structural analysis

Stage13 studies the primitive canonical exactly-one-face directional counts

\[
N_{ab}(B),\qquad N_{ac}(B),\qquad N_{bc}(B)
\]

for integer-space-diagonal cuboids and explains both the finite near-`2:1:1` observation and its true asymptotic behaviour.

## Current state

```text
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

The canonical living mathematical source is

```text
stages/stage13/main.md
```

with the main theorem in §9 and the final explanatory synthesis in §10.

## Main theorem

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

Stage13 proves

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

Thus

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

## Final explanation

At `B=100000`, the exactly-one population is

```text
(84146, 43180, 40704)
```

with ratio approximately

```text
2.0673 : 1.0608 : 1.
```

Stage13 resolves the difference between that finite ratio and the limiting chamber ratio as follows.

1. **Geometric backbone:** canonical ordering coupled to the one-face real density favors `ab` over `ac` over `bc`; the chamber integrals determine the asymptotic normalized vector.
2. **Finite flattening:** supported-shell richness strongly suppresses the finite `ab` advantage. OE/EE, pure-`G`, parity and primitive-support couplings also produce substantial finite cancellations in the `ac-bc` direction.
3. **Asymptotic recovery:** the arithmetic factor surviving in the leading main term is common across the three directions, so it cancels after normalization and leaves only the chamber vector.
4. **Exactly-one sieve:** pair and triple overlaps are lower order, so overlap removal does not change the leading normalized law.

Hence the finite near-`2:1:1` observation is a **long pre-asymptotic flattening of a stronger chamber bias**, not the limiting law.

## Stage12 bridge

For `q in {ab,ac,bc}`, let `C_prim,q^proj(B)` be the Stage12 primitive oriented records whose distinguished integral face becomes canonical category `q` after sorting. Stage13 proves exactly

\[
C^{\rm proj}_{\rm prim,q}(B)=2A_q(B)
\]

and

\[
C_{\rm prim}(B)=2(A_{ab}+A_{ac}+A_{bc}).
\]

Since every pair overlap and the triple overlap are `o(B(log B)^3)`,

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

Stage12 remains frozen at R09; the directional refinement and overlap removal are Stage13 results.

## Audit and frozen assets

```text
stages/stage13/data/13-7/consolidation_audit_report.json
stages/stage13/data/13-8/bridge_ledger_report.json
stages/stage13/data/13-8/final_cross_reference_audit_report.json
stages/stage13/data/13-9/main_structural_theorem_audit_report.json
stages/stage13/data/13-10/final_explanation_audit_report.json

stages/stage13/archive/stage13-7-final.md
stages/stage13/archive/stage13-8-final.md
stages/stage13/archive/stage13-9-final.md
stages/stage13/archive/stage13-10-final.md
```

Frozen snapshots are provenance; `main.md` remains canonical.

## Logical scope

Stage13 does not currently claim:

- existence or nonexistence of a perfect cuboid;
- an explicit convergence rate;
- an effective threshold for prescribed closeness to the limiting vector;
- monotonicity of the directional ratios;
- an independently peer-reviewed publication proof or certified numerical enclosure for `kappa`.

A perfect cuboid, if one exists, belongs to the lower-order triple-overlap population. Lower-order does not imply empty.

Open questions outside the completed Stage13 scope include the true growth law of the two-face population and effective convergence estimates.
