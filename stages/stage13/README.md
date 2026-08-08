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
NEXT=Stage13-9
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

as the canonical living mathematical source. Its §8 now contains the rigorous Stage12-to-Stage13 bridge theorem. Frozen task-end snapshots are provenance only.

## Stage13-7 final directional theorem

With the canonical chamber integrals

```text
I_ab = 0.659705248705705
I_ac = 0.3026997526726076
I_bc = 0.2712955487578571
I_ab+I_ac+I_bc = pi^2/8
```

Stage13-7 proves

\[
N_q(B)\sim \frac{\kappa I_q}{3\pi^3}B(\log B)^3,
\qquad q\in\{ab,ac,bc\},
\]

and

\[
N_1(B)\sim\frac{\kappa}{24\pi}B(\log B)^3.
\]

Therefore

```text
P_inf = (0.5347369332313988,
         0.24535917783225203,
         0.21990388893634913)

N_ab:N_ac:N_bc
 -> 2.431684750178191 : 1.115756428951881 : 1
```

so the limiting ratio is not `2:1:1`.

For the Stage13-5 deviation coordinates,

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

## Stage13-8 — frozen Stage12 to canonical exactly-one bridge

Stage13-8 is complete. It separates the bridge into four layers:

```text
frozen Stage12 primitive oriented records
  -> canonical raw face incidences
  -> directional raw asymptotics
  -> canonical exactly-one counts
```

For `q in {ab,ac,bc}`, let `C_prim,q^proj(B)` be the Stage12 primitive oriented records whose distinguished integral face becomes canonical category `q` after sorting. The exact projection theorem is

\[
\boxed{C^{\rm proj}_{\rm prim,q}(B)=2A_q(B)}
\]

and

\[
\boxed{C_{\rm prim}(B)=2(A_{ab}+A_{ac}+A_{bc}).}
\]

The universal factor `2` is the two orders of the distinguished face legs. It remains exact on multi-face objects and separately in the OE/EE parity strata.

Since Stage13-7 proves every pair overlap and the triple overlap are `o(B(log B)^3)`, the direct bridge is

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

The frozen Stage12 theorem remains only

\[
C_{\rm prim}(B)
\sim
\frac{\kappa}{12\pi}B(\log B)^3
=
\frac{\eta}{12\pi^2}B(\log B)^3,
\qquad \eta=\pi\kappa,
\]

for the primitive oriented count. Stage12 was not reopened; the directional refinement and overlap removal are Stage13 results.

## Stage13-8 final audit

The interface audit and final closure assets are

```text
stages/stage13/scripts/13-8/bridge_ledger.py
stages/stage13/data/13-8/bridge_ledger_report.json
stages/stage13/scripts/13-8/final_cross_reference_audit.py
stages/stage13/data/13-8/final_cross_reference_audit_report.json
stages/stage13/archive/stage13-8-final.md
```

The final 13-8c audit closes:

```text
OBJECT_MAP=CLOSED
CUTOFF_MATCHING=CLOSED
PRIMITIVE_DEFINITION_MATCHING=CLOSED
ORIENTATION_FIBER=CLOSED
CANONICAL_DIRECTION_PARTITION=CLOSED
PARITY_PROJECTION=CLOSED
DIRECTIONAL_CONSTANT_BRIDGE=CLOSED
OVERLAP_TO_EXACT_ONE=CLOSED
STAGE12_FREEZE_BOUNDARY=CLOSED
NEW_MATHEMATICAL_BRIDGE_GAP_FOUND=false
STAGE12_REOPENED=false
```

At `B=100000`, the end-to-end exact checksum is

```text
Stage12 projected = (168424, 86472, 81520)
raw incidence     = ( 84212, 43236, 40760)
pair overlaps     = (    33,    33,    23)
triple overlap    = 0
exactly-one       = ( 84146, 43180, 40704)

336416 = 2*168208
168030 = 336416/2 - 2*89 + 3*0
```

No new mathematical bridge lemma is required.

## Earlier structural synthesis

Stages13-3 through 13-6 explain the accessible finite regime:

- canonical archimedean geometry creates the directional ordering `ab>ac>bc`;
- representation-rich supported shells strongly flatten the finite `ab` excess;
- pure-`G` OE/EE and geometric subregions have opposite `ac-bc` gaps and can cancel strongly;
- primitive support materially changes the finite residual `ac-bc` tilt;
- the exactly-one overlap sieve is tiny at finite audited bounds and lower order asymptotically;
- the universal Stage12 projection multiplicity `2` is direction-neutral.

Thus the near-`2:1:1` observation is a pre-asymptotic cancellation/flattening regime sitting in front of the stronger chamber limit.

## Next — Stage13-9

Stage13-9 will formulate the principal Stage13 structural theorem in one final theorem package. The mathematical ingredients are already available: the finite mechanism analysis, the directional asymptotic vector, the overlap theorem, and the completed Stage12 bridge.

Stage13-9 should not reopen Stage12 or redo Stage13-7. Its job is to state the main theorem cleanly, identify hypotheses/dependencies precisely, and separate theorem claims from finite explanatory diagnostics before Stage13-10 gives the final plain-language structural explanation.

## File rule

Stage13 mathematical corrections normally go directly into canonical `main.md`; Git/PR history records prior versions. Support assets use task-first paths such as

```text
stages/stage13/scripts/13-<task>/<purpose>.py
stages/stage13/data/13-<task>/<purpose>.json
```

Frozen task-end snapshots under `stages/stage13/archive/` are provenance, not replacements for the living canonical file.
