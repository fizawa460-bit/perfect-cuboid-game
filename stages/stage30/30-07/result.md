# Stage30-07 — eight marked K8 defect transport

```text
STAGE=30-07
OWNER=CHATGPT_MAIN_BATCH
STATUS=SUBMITTED_PENDING_AUDIT
SOURCE_RECEIVER=R29-KUM5
```

## Result

Using the audited Stage29 K8 description and the audited Stage30-06/06C source-derived semilinear adapter, all eight marked defects are transported explicitly.

Write

```text
A=[[a,b],[c,a]] in sl2(F2)
kappa(A)=I+4A mod 8.
```

The exact `K8 ~= G0` adapter on the one-factor `X(8)` sign deck is

```text
phi(A)=(a+b,a+c,a) on (u,v,w).
```

Since

```text
U=u1u2=2b1
V=v1v2=2b2
W=w1w2=2b3,
```

the same three bits give an endpoint sign-deck representative on `(b1,b2,b3)`.

The source derivation is locked in `source-lock.md`; the finite builder and independent verifier check equivariance under all 24 residual elements.

## Complete eight-row table

| defect | `A` | ordinary class | ordinary orbit | stabilizer | sigma | endpoint adapter image | marked Q-class |
|---|---|---|---:|---:|---|---|---|
| `K8-000` | `[[0,0],[0,0]]` | zero | W0 / 1 | 24 | self | identity | singleton |
| `K8-001` | `[[0,0],[1,0]]` | nonzero_det0 | W1 / 3 | 8 | self | `delta_{b2}` | singleton |
| `K8-010` | `[[0,1],[0,0]]` | nonzero_det0 | W1 / 3 | 8 | self | `delta_{b1}` | singleton |
| `K8-011` | `[[0,1],[1,0]]` | det1_nonidentity | W2 / 3 | 8 | self | `delta_{b1,b2}` | singleton |
| `K8-100` | `[[1,0],[0,1]]` | identity (`A=I`) | W3 / 1 | 24 | self | `delta_{b1,b2,b3}` | singleton |
| `K8-101` | `[[1,0],[1,1]]` | det1_nonidentity | W2 / 3 | 8 | self | `delta_{b1,b3}` | singleton |
| `K8-110` | `[[1,1],[0,1]]` | det1_nonidentity | W2 / 3 | 8 | self | `delta_{b2,b3}` | singleton |
| `K8-111` | `[[1,1],[1,1]]` | nonzero_det0 | W1 / 3 | 8 | self | `delta_{b3}` | singleton |

The legacy Stage29 ordinary label `identity` in the `K8-100` row refers to the matrix `A=I` in `sl2(F2)`.  Its actual defect element is

```text
kappa=I+4I=5I mod 8,
```

so it is not the group identity defect.

## Ordinary orbit versus marked arithmetic class

The residual `S4` conjugation action factors through `S3` and simply permutes the three endpoint sign bits.  Hence the ordinary orbit sizes are exactly

```text
1,3,3,1
```

for Hamming weights `0,1,2,3`.

But the arithmetic marking is retained.  The audited sigma action on K8 is trivial and K8 is abelian, so the marked twisted equivalence relation is equality.  Therefore

```text
MARKED_Q_DESCENT_CLASS_COUNT=8
```

and no two rows are collapsed arithmetically.

## No elimination

This stage locates every defect in the endpoint sign-deck adapter; it does not prove any defect impossible.

```text
K8_DEFECT_CLASSIFICATION_EXECUTED=true
K8_DEFECT_ROW_COUNT=8
ORDINARY_S4_ORBIT_SIZES=1,3,3,1
MARKED_Q_DESCENT_CLASS_COUNT=8
SIGMA_ACTION_ON_K8=TRIVIAL
DEFECT_ELIMINATION_COUNT=0
```

## Recursive classification

```text
L30-EIGHT-K8-DEFECT-TRANSPORT
  = CLASS1_SUBMITTED_EXACT_FINITE_CLASSIFICATION

L30-PHYSICAL-ENDPOINT-ADAPTER
  = CLASS1_NEXT_30-08_PENDING_AUDIT

NEW_CLASS3_THEOREM_GATE
  = NONE
```

`R29-KUM5` is intentionally not marked discharged in 30-07.  Stage30-08 must still certify the exact scope on the physical endpoint open and decide whether the completed action/cocycle/defect adapter discharges the receiver or leaves a smaller residual leaf.

## Reproducibility

```text
stages/stage30/30-07/build_defect_transport.py
stages/stage30/30-07/defect-classification.json
stages/stage30/30-07/verify_defect_transport.py
stages/stage30/30-07/source-lock.md
```

The independent verifier reconstructs `PSL2(Z/4)`, checks the frozen Task-A ID order, rebuilds the source `S3` sign action, verifies the adapter for every `(g,kappa)` pair, checks stabilizers, verifies trivial sigma transport directly modulo 8, and checks all eight stored rows.

## Firewalls

```text
K8_EQUALS_V_MOD=false
C_SIGMA_EQUALS_KAPPA=false
ORDINARY_S4_ORBIT_EQUALS_MARKED_ARITHMETIC_CLASS=false
PHYSICAL_ENDPOINT_EXCLUSION_PROVED=false
R29_KUM5_DISCHARGED=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## Gate

```text
AUDIT_REQUIRED=true
AUDIT_VERDICT=PENDING
MERGE_ALLOWED=false
ADVANCE_ALLOWED=false
NEXT_ITEM_AFTER_AUDIT_PASS=30-08_PHYSICAL_ENDPOINT_ADAPTER
NEXT_EXPECTED_COMMAND=Stage30-audit
```
