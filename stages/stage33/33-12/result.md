# Stage33-12 MAIN exact assembly checkpoint

Status: `MAIN_IN_PROGRESS_EXACT_OBSTRUCTION_INVENTORY_MATERIALIZED`

This checkpoint performs the first exact arithmetic Hochschild--Serre assembly after the audited Stage33-11 exit. It does not close Stage33-12 or Stage33-07.

## Exact progress

The audited predecessor interfaces are source-locked and separated into the two required descent stages:

1. localization connecting map (`delta_loc`): exact zero on all 26 finite directions;
2. Hochschild--Serre `d2`: still requires its own computation on the remaining two-primary blocks.

The following already Q-defined blocks have exact HS image zero, because each is already in the image of `Br(U)`:

* the complete BR0B all-primary block;
* the 44 explicit Q-defined U44 quaternion classes;
* the Q-defined exact-order-two proper class J2;
* the zero seven-line block.

The odd-primary repair is exact and complete: the globally liftable part of the odd constant-boundary cokernel is zero, so no new odd-primary Q-defined residue-lift block remains beyond BR0B.

## Exact remaining obstruction inventory

Only two two-primary blocks remain:

1. the parametric constant-character cokernel
   `coker(rho: BR0B[2^infinity] -> Hom_cont(G_Q,Q_2/Z_2)^48 direct_sum Hom_cont(G_Q(i),Q_2/Z_2)^12)`;
2. the finite quotient `(Z/2)^23 direct_sum (Z/4)^3`, with the 26 named directions `A2_01..A2_26`.

The full constant cokernel is not claimed liftable. Its actually liftable residue subgroup modulo BR0B injects into the ten-dimensional proper invariant `Br(Sbar)[2]^G_Q`, modulo Q-defined zero-boundary proper classes. Since J2 supplies one such nonzero dimension, this unknown liftable subgroup has F2 dimension at most 9, cardinality at most 512, and exponent 2. Determining which residue tuples form that finite subgroup remains open.

For the finite block, Stage33-11 proves Stage A exact zero on all 26 directions. It does not, without a new adapter, compute the 26 Stage B HS values or produce 26 Q-defined lifts. The constant cokernel is not covered by the 26-direction certificate and remains a separate parametric HS map.

The function-level scalar adapter has now also been computed. The 14 exact Stage33-11 generators contain 134 nontrivial side/exceptional boundary-function packages. Reconstructing their occurrence scalars from the two retained #1430 ambient-function artifacts gives 564 admissible `cc/ct` source-target comparisons, and every scalar ratio is exactly `1`. The audited Stage33-11f Q-defined automorphism/XOR span transports this zero scalar correction to all 26 directions. Therefore the finite block does not mix with the constant cokernel through boundary-function multiplicative constants. This does not rule out a later coupling in the still-unmaterialized global Gersten 2-cochain or HS differential.

The machine-readable certificate is `stage33-12-exact-obstruction-inventory.json`, generated and independently replayable by `assemble_exact_obstruction_inventory.py`.

## Current exit state

```text
ARITHMETIC_HS_D2_COMPUTED=false
GLOBAL_Q_BR0G_RESIDUE_LIFTS_COMPLETE=false
COMPLETE_RELEVANT_Q_DEFINED_CLASS_LIST_FOR_STAGE33_BRAUER_SCOPE=false
STAGE33_07_HOSTILE_REAUDIT=NOT_RUN
STAGE33_12_CLOSED=false
```

The next exact leaf is now strictly above the boundary-function level: compute a global Gersten 2-cochain / HS differential for the constant two-primary block and the 26 finite directions, or equivalently materialize and residue-check explicit Q-defined lifts. The known Q-defined prefix and the zero boundary scalar adapter must not be recomputed.

All Stage33-07/08/40, theorem, endpoint, and perfect-cuboid firewalls remain closed.
