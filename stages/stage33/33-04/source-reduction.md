# Stage33-04 — BR0G physical-boundary residue adapter

```text
STAGE33_UNIT=33-04
UNIT_STATUS=RUNNING
UNIT_CLOSED=false
DOWNSTREAM_RELEASED=false
PREREQUISITE_UNITS=[33-02]
PREREQUISITES_ALL_CLOSED=true
BR0A=DISCHARGED
BR0G=OPEN
THEOREM_CREDIT=false
ENDPOINT_CREDIT=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## Frozen physical boundary

The physical open is

```text
U = S \ D,
```

where the audited geometric boundary contains exactly

```text
24 strict-transform side conics + 48 exceptional curves = 72 components.
```

Stage33-02 supplies the exact `72 x 64` divisor-to-Picard map and the complete `72 x 72` intersection matrix with source/order locks.  Stable component IDs in this unit are tied to the pinned upstream order:

```text
SIDE_A1_001..008 = upstream 1..8
SIDE_A2_001..008 = upstream 9..16
SIDE_A3_001..008 = upstream 17..24
EXC_001..048     = upstream 93..140
```

No component outside this list is silently added or removed.

## Gersten reduction

For the smooth compactification, purity gives the boundary residue complex

```text
Br(S_Qbar)
 -> Br(U_Qbar)
 -> direct_sum_j H^1(Qbar(D_j),Q/Z)
 -> direct_sum_{x in D^(2)} Q/Z.
```

Every boundary component is rational.  If the audited intersection matrix certifies that the resolved boundary is pairwise transverse with no triple points, then the residue contribution supported only at boundary crossings is the cycle module of the boundary dual graph.  In particular, for a graph with `V=72`, `E` codimension-two crossings and `c` connected components,

```text
rank H_1(Gamma,Z) = E - V + c,
```

and prime-by-prime residue compatibility has the same cycle rank.

This unit does not assume the SNC graph shape.  It verifies it exactly from the audited matrix:

```text
side-side off-diagonal block = 0;
exceptional-exceptional off-diagonal block = 0;
side-exceptional entries are 0 or 1.
```

On the smooth resolution, an entry `1` is a unique transverse crossing.  If two side curves met the same exceptional point, their strict transforms would have positive mutual local intersection there, contradicting the exact zero side-side block.  Thus the verified bipartite matrix gives a stable one-edge-per-codimension-two-point inventory and excludes triple boundary crossings.

## Current bounded sub-DAG

```text
04A  stable 72-component inventory
 |
 v
04B  exact side/exceptional incidence and SNC certification
 |
 v
04C  exact integral + mod-p graph boundary maps and cycle basis
 |
 v
04D  attach Galois action on components/codimension-two points
 |
 v
04E  multiquadratic pullback / exceptional residue ledger
 |
 v
04F  exact physical-open unramified residue kernel
      -> BR0G discharge or named residual
```

`04A--04C` are executed by the first production leaf.  Galois/pullback attachment remains explicit downstream work; no BR0G discharge is claimed from graph rank alone.

```text
LEAF_ID=L33-04-PHYSICAL-BOUNDARY-SNC-RESIDUE-SKELETON
CLASS=2
NEW_THEOREM_REQUIRED=false
```

## Source locks

- `stages/stage33/33-02/audit-state.json`
- `stages/stage33/33-02/handoff.json`
- `stages/stage29/29-02f/physical-open-boundary.md`
- `stages/stage29/29-02f/boundary-gersten-receiver.md`
- Stage33-02 final artifact `9505735040`, digest `75eb5c0753b06ea3bad9902d70fd8b59ed24ce190a64882d93935f5760d1ec87`

```text
NEXT_EXPECTED_COMMAND=Stage33-main-batch
```
