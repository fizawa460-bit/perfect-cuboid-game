# Stage32-18 — d16 Aut symmetry breaking + canonical augmentation

This unit moves the successful `(d,g)=(16,0)` Aut-symmetry scout into the Stage32 main implementation path.

## Production architecture implemented here

1. Rebuild the source-locked Stage32 Picard core.
2. Construct the rank-63 `H^perp` lattice for the affine degree-16 slice and verify that the 140-pairing map has rank 63, hence is injective on these coordinates.
3. Regenerate the nine source-locked geometric Aut generators and close them exactly to `|Aut(S)|=1536`.
4. Select 64 deterministic full-group hash-spread score inequalities for DFS pruning.
5. At every exact surviving leaf, compare the 140-pairing vector against the full 1536-element Aut orbit using the exact deterministic order
   `(<SHA-derived integer score>, <lexicographic 140-pairing>)`.
6. Emit only the unique full-orbit canonical representative.
7. Independently reconstruct the 1536-element group in Python and recheck every emitted canonical representative.

The b6 implementation regression is locked against the completed scout evidence:

- no-symmetry complete survivors: 17,833;
- independently profiled Aut orbit count: 37;
- hash-spread-64 pre-canonical survivors: 232;
- expected full-group canonical survivors: 37 including zero, 36 nonzero.

## Exactness firewall

The full-group leaf canonical decision is exact integer arithmetic, and the pairing-map injectivity check is exact PARI rank computation. However the current Hperp traversal still inherits the scout's `long double` LDL / dual-reach pruning. Therefore Stage32-18 is an implementation checkpoint only until a hostile audit separately certifies traversal completeness or replaces the floating reach pruning with a certified exact enclosure.

Accordingly this unit does **not** grant a complete d16 row, theorem credit, receiver credit, or route discharge.

```text
MAIN_IMPLEMENTATION_ROUTE=AUT_SYMMETRY_BREAKING_PLUS_FULL_GROUP_CANONICAL_AUGMENTATION
FLOATING_REACH_PRUNING_COMPLETENESS_AUDIT_PENDING=true
THEOREM_CREDIT=false
RECEIVER_CREDIT=false
FULL_D16_G0_ROW_COMPLETE=false
FULL_D176_D192_NUMERICAL_ORBIT_CENSUS=false
R29_LG2_NUMERICAL_COMPONENT_COMPLETE=false
R29_LG2=NOT_DISCHARGED
G10_LOWGENUS_PICARD=AMBER
```

Next gate after the functional CI regression passes: hostile audit of traversal completeness before any d16 numerical-row credit.
