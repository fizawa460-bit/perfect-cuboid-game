# Stage29 GAP_SCAN_FINAL — external claimed-proof quarantine

Search cutoff: 2026-08-22.

This file is deliberately separated from theorem credit. A public claim of a complete proof does not alter Stage29 unless the exact argument is source-locked and survives universal-coverage/admissibility audit.

## EXT-CLAIM-TAHA-EPB-2026

Source family: Taha Muhammad, *Euler Perfect Box* and *Euler Perfect Box 2nd Way*, Cambridge Open Engage working-paper versions through May 2026.

Publicly displayed argument pattern:

- write ordered edges in forms such as `b=a+r`, `c=a+k`;
- compare the expression for `g^2=a^2+b^2+c^2` with a selected complete-square decomposition;
- infer that because the selected internal terms are unequal, `g^2` cannot be a square.

The displayed implication is invalid. A sum being a square does not require equality with the particular internal decomposition selected by the proof. Showing that one proposed identity between intermediate terms fails does not exclude every square representation of the total integer.

The paper's case labels by edge ordering do not repair this algebraic non sequitur.

```text
EXT_CLAIM_TAHA_EPB_2026=REJECTED_DISPLAYED_ARGUMENT_NONSEQUITUR
UNIVERSAL_PERFECT_CUBOID_NONEXISTENCE_PROVED=false
ROUTE_CREDIT=false
```

This is a rejection of the displayed proof argument, not a statement about the author's intent.

## EXT-CLAIM-SHLYGIN-2026

Public index: Maximus Shlygin, *Euler Brick (Perfect Cuboid) - Complete Proof*, Synapse entry dated 18 March 2026, pointing to a Zenodo DOI.

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

The full primary manuscript was not source-locked by this scan. Therefore the correct Stage29 disposition is quarantine, not rejection-by-absence and not theorem credit.

```text
EXT_CLAIM_SHLYGIN_2026=QUARANTINED_PRIMARY_FULL_TEXT_SOURCELOCK_PENDING
ROUTE_CREDIT=false
NEW_ACTIVE_RECEIVER_CREATED=false
```

Fresh audit should attempt primary full-text acquisition if available. If source-locked, the audit must test the five points above before changing any Stage29 state.

## Firewall

Neither claim changes:

```text
FINAL_ACTIVE_KERNEL_COUNT=13
GREEN_ROUTE_COUNT=1
AMBER_ROUTE_COUNT=10
P_OVER_M3_SCALE_KNOWN=false
```

and neither is counted as a published endpoint theorem in the Stage29 final gap surface.
