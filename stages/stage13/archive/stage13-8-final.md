# Stage13-8 final — frozen bridge-completion snapshot

> **STATUS:** `STAGE13_8_COMPLETE`
>
> **SCOPE:** frozen task-end provenance snapshot; canonical living mathematics remains `stages/stage13/main.md`

## Purpose

Stage13-8 consolidates the rigorous bridge from the frozen Stage12 primitive oriented count to the Stage13 primitive canonical exactly-one directional counts. 13-8a audited the object/interface map, 13-8b integrated the theorem into canonical `main.md`, and 13-8c performed the final cross-reference, notation, dependency, finite-checksum and freeze-boundary audit.

No new analytic theorem is introduced in 13-8c.

## Frozen Stage12 input

Stage12 remains frozen at R09 and supplies only

\[
C_{\rm prim}(B)
\sim
\frac{\kappa}{12\pi}B(\log B)^3
=
\frac{\eta}{12\pi^2}B(\log B)^3,
\qquad \eta=\pi\kappa,
\]

for its primitive oriented distinguished-face count.

Stage12 is not reinterpreted as a canonical or exactly-one theorem.

## Exact projection

For \(q\in\{ab,ac,bc\}\), let \(C^{\rm proj}_{\rm prim,q}(B)\) be the Stage12 primitive oriented records whose distinguished integral face becomes canonical category \(q\). Then, for every \(B\),

\[
\boxed{C^{\rm proj}_{\rm prim,q}(B)=2A_q(B)}
\]

and

\[
\boxed{C_{\rm prim}(B)=2(A_{ab}+A_{ac}+A_{bc}).}
\]

The factor \(2\) is exactly the two orders of the two distinguished face legs. It remains exact on multi-face objects because raw incidence retains the distinguished face, and it holds separately in the OE/EE parity strata.

## Directional constants

With

\[
P_q=\frac{8I_q}{\pi^2},
\qquad \sum_qP_q=1,
\]

Stage13 gives

\[
C^{\rm proj}_{\rm prim,q}(B)
\sim
\frac{\kappa}{12\pi}P_qB(\log B)^3,
\]

and therefore

\[
\boxed{
A_q(B)
\sim
\frac{\kappa I_q}{3\pi^3}B(\log B)^3.
}
\]

Equivalently,

\[
A_q(B)\sim\frac{\eta I_q}{3\pi^4}B(\log B)^3.
\]

## Exactly-one transfer

The exact category identities are

\[
N_{ab}=A_{ab}-O_{ab,ac}-O_{ab,bc}+T
\]

and cyclically. Stage13-7 proves every pair overlap and \(T\) are

\[
o(B(\log B)^3).
\]

Hence

\[
\boxed{
N_q(B)
=
\frac12C^{\rm proj}_{\rm prim,q}(B)
+o(B(\log B)^3)
}
\]

and

\[
\boxed{
N_1(B)
=
\frac12C_{\rm prim}(B)
+o(B(\log B)^3).
}
\]

No perfect-cuboid nonexistence assumption is used.

Consequently,

\[
N_q(B)\sim\frac{\kappa I_q}{3\pi^3}B(\log B)^3,
\qquad
N_1(B)\sim\frac{\kappa}{24\pi}B(\log B)^3.
\]

The normalized limit is

```text
P_inf = (0.5347369332313988,
         0.24535917783225203,
         0.21990388893634913)

ab:ac:bc
 -> 2.431684750178191 : 1.115756428951881 : 1
```

and is not `2:1:1`.

## Finite end-to-end lock at B=100000

```text
Stage12 projected = (168424, 86472, 81520)
raw incidence     = ( 84212, 43236, 40760)
pair overlaps     = (    33,    33,    23)
triple overlap    = 0
exactly-one       = ( 84146, 43180, 40704)
```

Thus

```text
336416 = 2*168208
168030 = 336416/2 - 2*89 + 3*0
```

exactly.

## 13-8c audit result

The final machine-readable audit is

```text
stages/stage13/data/13-8/final_cross_reference_audit_report.json
```

with executable checker

```text
stages/stage13/scripts/13-8/final_cross_reference_audit.py
```

The audit closes all bridge categories:

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

The fixed-modulus congruence refinement in the Stage13-7 overlap proof remains a Stage13 extension at the same accepted theorem-application level as the frozen Stage12 machinery. Independent publication-grade review is not claimed.

## Completion decision

```text
STAGE13_8A=COMPLETE
STAGE13_8B=COMPLETE_CANONICAL_BRIDGE_INTEGRATION
STAGE13_8C=COMPLETE_FINAL_AUDIT
STAGE13_8=COMPLETE
NEW_MATHEMATICAL_BRIDGE_GAP_FOUND=false
STAGE12_REOPENED=false
NEXT=Stage13-9 main structural theorem
```
