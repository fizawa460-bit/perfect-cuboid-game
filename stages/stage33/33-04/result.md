# Stage33-04 — BR0G physical-boundary residue production state

```text
STAGE33_UNIT=33-04
UNIT_STATUS=AUDIT_REQUIRED
UNIT_CLOSED=false
DOWNSTREAM_RELEASED=false
BR0G=CLAIMED_DISCHARGED_PENDING_HOSTILE_AUDIT
PHYSICAL_BOUNDARY_72_INVENTORY_COMPLETE=true
BOUNDARY_STABLE_IDS_COMPLETE=true
RESIDUE_INCIDENCE_MATRIX_EXACT=true
MULTIQUADRATIC_PULLBACK_RESIDUES_EXACT=true
EXCEPTIONAL_DIVISOR_RESIDUES_EXACT=true
PHYSICAL_BOUNDARY_OMISSIONS=0
UNRAMIFIED_PHYSICAL_OPEN_KERNEL_EXACT=true
UNRESOLVED_UNKNOWN_IN_SCOPE=0
THEOREM_CREDIT=false
ENDPOINT_CREDIT=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## Exact physical boundary and Gersten cycle kernel

The audited Stage33-02 boundary is reproduced exactly as

```text
24 side strict transforms + 48 exceptional curves = 72 components,
144 transverse codimension-two crossings,
1 connected dual graph,
integral cycle rank = 73.
```

The saturated integral cycle lattice is computed from the exact oriented incidence matrix.  Stable component IDs and all 144 crossing IDs remain tied to the pinned Testa--Stoll order.

The exact boundary Galois action is source-locked from

```text
L = Q(i,sqrt(2)),
Gal(L/Q) ~= V4.
```

On the rank-73 integral cycle lattice the rational character multiplicities are

```text
(+,+)=61,
(-,+)=12,
(+,-)=0,
(-,-)=0.
```

The `sqrt(2)` involution acts trivially on the boundary inventory.  Smith normal form of `cc-I` has rank 12 and its twelve nonzero invariant factors are all `1`.  Therefore there is no hidden finite cokernel correction and the complete Galois-fixed geometric boundary residue-cycle module is exactly

```text
ker(second residue)^{G_Q} ~= (Q/Z)^61.
```

Equivalently every prime-primary part has divisible rank 61.  This statement is an exact boundary/Gersten adapter output; it is not by itself a list of Q-defined Brauer classes.

Evidence from workflow `32701473247`:

```text
workflow_conclusion = success
all_primary_geometric_cycle_certificate_sha256 = de1731dcc5193e160a54b8389311398c09ac1c2798df2cb362e432207b1bd08e
artifact_id = 9510714843
artifact_zip_sha256 = ec2a8768df987ecc0ee8454ac2ff6399ab9cf4bb4a83e524eac90fd05f5658a2
```

## Multiquadratic/Ford pullback is exact

Under the endpoint sign-cover map

```text
[a1:a2:a3:b1:b2:b3:c] -> [a1^2:a2^2:a3^2],
```

all seven line-arrangement factors have explicit square roots

```text
x,y,z,x+y,x+z,y+z,x+y+z
 -> a1,a2,a3,b3,b2,b1,c.
```

Hence every ambient Ford two-symbol already pulls back to zero before concurrence relations are imposed, and therefore the full certified 9-dimensional Ford source group has exact pullback rank zero:

```text
FORD_KUMMER_PULLBACK_RANK=0.
```

The 48 exceptional components are independently classified over the nine base intersection points, and their side/exceptional crossing residues are included in the exact 72-component Gersten matrix.  No exceptional boundary component is omitted.

## Exact exponent-two intrinsic residual

At exponent two, the Q-fixed graph-cycle space has dimension `61`.  The exact secondary-residue footprints from the rank-14 boundary-unit lattice span `44D`, leaving an explicit `17D` quotient.

```text
QFIXED_RESIDUE_CYCLE_DIM_F2=61
UNIT_SYMBOL_SECONDARY_RESIDUE_SPAN_RANK_F2=44
QFIXED_RESIDUAL_QUOTIENT_DIM_F2=17
```

All 17 residual vectors are explicitly materialized, graph-compatible, and V4-fixed.  Their geometric first residues are realizable, the finite V4 divisor-parity obstruction is zero, and the exponent-two arithmetic function/constant-squareclass descent is exact:

```text
TWO_PRIMARY_RESIDUAL_LEAF_COMPLETE=true
Q_DEFINED_RESIDUAL_DIMENSION_F2_AFTER_KNOWN_UNIT_SYMBOL_IMAGE=17
CONSTANT_SQUARECLASS_COCYCLE_DIMENSION_F2=0
```

The exponent-two descent certificate is deliberately scoped only to this `F2` residual and is not used to Kummer-identify odd-primary characters.

```text
qfixed17_function_constant_descent_sha256 = 7f5426c21ba747fa015492c1b93f62fe61c0a3faadb49124d1e94c52ad074e90
```

## Scope boundary against Stage33-03 / Stage33-07

Stage33-04 is the physical-boundary residue adapter.  Its closure output is the exact boundary residue kernel together with Galois action/invariants and exact multiquadratic/exceptional accounting.

It does **not** independently construct the final complete Q-defined Brauer-class inventory.  The frozen Stage33 contract assigns all-primary open-algebraic absolute-Galois terms to Stage33-03 and imports both BR0B and BR0G outputs into Stage33-07 for the complete relevant Q-defined class list.

Therefore the exact

```text
(Q/Z)^61
```

boundary output is not promoted here to sixty-one Q-defined Brauer generators, and no local-evaluation or Brauer--Manin conclusion is taken.

The earlier apparent residual

```text
R33-BR0G-ODD-PRIMARY-ARITHMETIC-CHARACTER-DESCENT
```

is not retained as an internal 33-04 blocker: performing the full Q-defined character/class integration here would duplicate Stage33-03/33-07 responsibilities.  Odd-primary information is preserved in the all-primary `(Q/Z)^61` handoff rather than discarded.

## Closure accounting

The Stage33-04 unit-specific gates are now claimed satisfied:

```text
PHYSICAL_BOUNDARY_72_INVENTORY_COMPLETE=true
BOUNDARY_STABLE_IDS_COMPLETE=true
RESIDUE_INCIDENCE_MATRIX_EXACT=true
MULTIQUADRATIC_PULLBACK_RESIDUES_EXACT=true
EXCEPTIONAL_DIVISOR_RESIDUES_EXACT=true
PHYSICAL_BOUNDARY_OMISSIONS=0
UNRAMIFIED_PHYSICAL_OPEN_KERNEL_EXACT=true
BR0G=CLAIMED_DISCHARGED_PENDING_HOSTILE_AUDIT
UNRESOLVED_UNKNOWN_IN_SCOPE=0
```

No downstream release occurs before hostile audit.

```text
UNIT_STATUS=AUDIT_REQUIRED
UNIT_CLOSED=false
DOWNSTREAM_RELEASED=false
NEXT_EXPECTED_COMMAND=Stage33-audit
```

Firewalls:

```text
Q_DEFINED_COMPLETE_BRAUER_CLASS_LIST=false
BRAUER_MANIN_OBSTRUCTION_CLAIM=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
