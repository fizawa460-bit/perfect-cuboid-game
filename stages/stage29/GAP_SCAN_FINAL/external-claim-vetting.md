# Stage29 GAP_SCAN_FINAL — external claimed-proof quarantine — audited addendum

Search cutoff: 2026-08-22.

This file is deliberately separated from theorem credit. A public claim, title, abstract, or index entry does not alter Stage29 unless the exact argument is source-locked and survives universal-coverage/admissibility audit.

## EXT-CLAIM-TAHA-EPB-2026

Source family: Taha Muhammad, *Euler Perfect Box* and *Euler Perfect Box 2nd Way*, Cambridge Open Engage working-paper versions through May 2026. Primary public locator: DOI `10.33774/coe-2024-47ld9-v4` for *Euler Perfect Box* Version 4.

The displayed Case-A implication is invalid: showing that `g^2` is unequal to one selected complete square does not show that `g^2` is not a square. The current Cambridge page contains a public scholarly comment dated 2026-07-16 giving the explicit counterexample `(a,b,c,g)=(3,4,12,13)` to that inference. The separate 2nd-Way paper does not supply a universal endpoint reduction repairing this defect.

```text
EXT_CLAIM_TAHA_EPB_2026=REJECTED_DISPLAYED_ARGUMENT_NONSEQUITUR
UNIVERSAL_PERFECT_CUBOID_NONEXISTENCE_PROVED=false
ROUTE_CREDIT=false
```

This is a rejection of the displayed proof argument, not a statement about the author's intent.

## EXT-CLAIM-SHLYGIN-2026

Public index: Maximus Shlygin, *Euler Brick (Perfect Cuboid) - Complete Proof*, Synapse entry dated 18 March 2026. The index points to a purported Zenodo DOI `10.5281/zenodo.19049680`.

The accessible abstract claims a local algebraic-differential route:

```text
cuboid ring
-> triangular-remainder coordinates
-> low-degree local shell
-> tangent/readout branch detection
-> elimination of all local branches
-> global nonexistence.
```

The abstract alone is not sufficient to audit the load-bearing implications, in particular:

1. the exact definition of the local/strict-core scheme and its relation to the physical rational endpoint;
2. why a hypothetical rational/integral endpoint point must yield the particular nontrivial branch used by the argument;
3. why low-degree shell/tangent information exhausts higher-order or other local support;
4. why the branch eliminations do not merely constrain a chosen local model while leaving endpoint points outside it;
5. compatibility with the known nonempty geometric endpoint surface over algebraic closures.

The final audit searched the exact title and DOI but did not source-lock a primary full manuscript from Zenodo. Therefore the disposition remains quarantine, not rejection-by-absence and not theorem credit.

```text
EXT_CLAIM_SHLYGIN_2026=QUARANTINED_PRIMARY_FULL_TEXT_SOURCELOCK_PENDING
ROUTE_CREDIT=false
NEW_ACTIVE_RECEIVER_CREATED=false
```

If a primary full manuscript later becomes available, reopen only for hostile verification of the five load-bearing implications above.

## EXT-YELLE-2026

Fresh audit found Stéphane Yelle, *An Elementary Obstruction to the Existence of a Perfect Cuboid*, arXiv `2602.00239`, current HTML generated 2026-02-09.

The arXiv abstract wording can sound like a global obstruction, so the full current text was checked rather than relying on the abstract. The current manuscript explicitly states in the introduction that its purpose is **not** to claim a definitive impossibility result, and the conclusion explicitly states that the analysis does **not** resolve existence of a perfect cuboid. Its proved/argued scope is a triangular-remainder analysis of selected rigid/flexible cyclic-gluing strategies, with a symmetric-closure lemma and exploratory divisibility/descent mechanism.

Accordingly this is not a competing global nonexistence proof and it creates no new Stage29 receiver. Any triangular-remainder structural ideas are already within the broad parametric/local architecture and do not discharge `PESCH-E1`, the full endpoint rational-point kernel, or any other Class-3 kernel.

```text
EXT_YELLE_2026=CURRENT_VERSION_EXPLICITLY_SCOPED_NOT_GLOBAL_RESOLUTION
PRIMARY_FULL_TEXT_SOURCELOCKED=true
ROUTE_CREDIT=false
NEW_ACTIVE_RECEIVER_CREATED=false
```

## Audited firewall

The three fresh public items therefore classify as:

```text
FRESH_EXTERNAL_ITEM_COUNT=3
REJECTED_DISPLAYED_PROOF_COUNT=1
SOURCELOCK_PENDING_COUNT=1
SCOPED_NOT_GLOBAL_RESOLUTION_COUNT=1
NEW_THEOREM_CREDIT_COUNT=0
NEW_ACTIVE_RECEIVER_COUNT=0
```

They do not change:

```text
FINAL_ACTIVE_KERNEL_COUNT=13
GREEN_ROUTE_COUNT=1
AMBER_ROUTE_COUNT=10
P_OVER_M3_SCALE_KNOWN=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```
