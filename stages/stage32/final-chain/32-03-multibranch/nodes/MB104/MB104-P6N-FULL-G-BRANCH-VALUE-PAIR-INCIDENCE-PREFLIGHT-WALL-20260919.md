# MB104 P6N — full-G branch-value pair incidence preflight wall — 2026-09-19

Status: **PRE-AUDIT EXACT RETAINED-INTERFACE WALL / NO CREDIT**

## Target

The hostile support is

```text
Sigma = 0000093f442e
nodes = {1,2,3,5,10,14,16,17,18,19,20,21,24,27}.
```

P6D2 and P6H identify the three inertia types and force type-pair totals

```text
(48l,16l,48l)
```

for the unramified branch divisors. P6N asks for strictly finer data: inside each inertia type, recover the two individual branch values in factor 1 and factor 2 and form the exact `2 x 2` node-incidence matrix.

## 1. What the retained 48-node model source-locks

The retained exact node-action adapter `AUTS-NODE-ACTION-SOURCE-NOTE.md` imports:

- the 48 projective box-node coordinates in `[a1,a2,a3,b1,b2,b3,c]`;
- nine exact coordinate substitutions;
- the induced `Aut(S)` action of order `1536`.

It is explicitly a node-action adapter only.

The retained modular adapter `BEAUVILLE-NODE-STABILIZER-TYPE-SOURCE-NOTE.md` identifies the three singular stabilizer types from the unique zero among

```text
b1,b2,b3.
```

It further records that the 48-node model splits into six eight-node blocks and that block pairs

```text
(1,4), (2,5), (3,6)
```

give the three `16`-node stabilizer types.

This is enough to recover the exact hostile support counts

```text
type counts = (6,2,6),
```

but it does not identify, inside any one type, the two individual branch values of `C8/G -> P1` separately in factor 1 and factor 2.

## 2. Why a 2 x 2 incidence matrix cannot be inferred from the current labels

For one inertia generator, the quotient `C8 -> C8/G` has two branch values of that type. A box node in the product comes from a pair of fixed points, so the desired packet-sensitive refinement is a four-cell decomposition

```text
(branch value alpha/beta in factor 1)
    x
(branch value alpha/beta in factor 2).
```

The retained Stage32 node index and canonical coordinates do not currently carry a source-locked map

```text
node index
  -> (individual branch value in factor 1,
      individual branch value in factor 2).
```

The modular source note deliberately stops at the three stabilizer types and says the naming of the other diagonal cusps is immaterial for that adapter. The Aut(S) note likewise supplies no modular fixed-point-orbit labels.

Therefore any split of the 16 nodes of one inertia type into four 4-node branch-value cells would currently be an extra identification, not a retained consequence.

In particular, none of the following is justified from the current sources:

```text
- treating the two eight-node blocks of one type as the two factor branch values;
- splitting by c=0 versus c!=0 and calling that a factor cusp label;
- using sign patterns of a_i or b_i as branch-value labels;
- assigning a diagonal/off-diagonal 2 x 2 pattern from symmetry alone.
```

## 3. Disposition

P6N reaches an exact source-interface wall:

```text
three inertia types                    = exact,
hostile type counts (6,2,6)           = exact,
individual factor branch-value labels = not source-locked,
2 x 2 branch-value incidence           = not derivable without a new adapter.
```

No packet-sensitive incidence constraint stronger than the existing type totals is claimed.

## 4. Reopen trigger and next leaf

Reopen P6N only after a source-complete modular fixed-point adapter identifies, for every retained box node, the individual branch-value orbit in each `C8/G` factor.

The next shallow route is therefore

```text
MB104-P6O-MODULAR-FIXED-POINT-BRANCH-LABEL-ADAPTER-PREFLIGHT.
```

Target: inspect the published modular/theta model (or an exact retained computation derived from it) for a factorwise map from the explicit 48 box-node coordinates to the six branch values of `C8/G`. If no exact map is available without new substantial modular computation, park the incidence route rather than guessing.

## Source locks

Historical archive exact head:

```text
ae6ce8e2feb8233886dec1ca21b6db0ec8dbbb11
```

- `AUTS-NODE-ACTION-SOURCE-NOTE.md` blob `cbe21fdbacb975a726d0c2c8a1ab8fd3b21d0693`;
- `BEAUVILLE-NODE-STABILIZER-TYPE-SOURCE-NOTE.md` blob `a29161602c0b38f0607794e56e61068b8cb9735d`.

Current compact branch:

- P6A hostile support certificate blob `ab16e0757607c702fbc548dd9393d16d6c5f899b`;
- P6D2 note blob `1194fdd228c394d79262579df3930b4d8f619cf9`;
- P6M certificate blob `59aeedc2a9ee0970fa552a2d08fdc67e0f81c4e0`.

## Firewalls

```text
individual_branch_value_labels_source_locked=false
branch_value_2x2_incidence_computed=false
new_packet_obstruction=false
finite_degree_window_proved=false
MB104_complete=false
receiver_credit=false
theorem_credit=false
endpoint_credit=false
perfect_cuboid_existence_claim=false
perfect_cuboid_nonexistence_claim=false
merge_authorized=false
```
