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

For the finite block, Stage33-11 proves Stage A exact zero on all 26 directions. It does not, without a new adapter, compute the 26 Stage B HS values or produce 26 Q-defined lifts. The constant cokernel is not covered by the 26-direction certificate and remains a separate parametric HS map.

The machine-readable certificate is `stage33-12-exact-obstruction-inventory.json`, generated and independently replayable by `assemble_exact_obstruction_inventory.py`.

## Current exit state

```text
ARITHMETIC_HS_D2_COMPUTED=false
GLOBAL_Q_BR0G_RESIDUE_LIFTS_COMPLETE=false
COMPLETE_RELEVANT_Q_DEFINED_CLASS_LIST_FOR_STAGE33_BRAUER_SCOPE=false
STAGE33_07_HOSTILE_REAUDIT=NOT_RUN
STAGE33_12_CLOSED=false
```

The next exact leaf is to compute the constant two-primary HS map and the 26 named finite HS values, or equivalently materialize and residue-check explicit Q-defined lifts for those inputs. The known Q-defined prefix must not be recomputed.

All Stage33-07/08/40, theorem, endpoint, and perfect-cuboid firewalls remain closed.
