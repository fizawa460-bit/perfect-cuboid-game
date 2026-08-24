# Stage33-04 — BR0G physical-boundary residue production state

Hostile audit of PR #1362 accepts the exact geometric/two-primary prefix but rejects promotion to BR0G closure.

```text
STAGE33_UNIT=33-04
UNIT_STATUS=BLOCKED_NEW_KERNEL
UNIT_CLOSED=false
DOWNSTREAM_RELEASED=false
BR0G=OPEN
PHYSICAL_BOUNDARY_72_INVENTORY_COMPLETE=true
BOUNDARY_STABLE_IDS_COMPLETE=true
RESIDUE_INCIDENCE_MATRIX_EXACT=true
MULTIQUADRATIC_PULLBACK_RESIDUES_EXACT=true
EXCEPTIONAL_DIVISOR_RESIDUES_EXACT=true
PHYSICAL_BOUNDARY_OMISSIONS=0
UNRAMIFIED_PHYSICAL_OPEN_KERNEL_EXACT=false
UNRESOLVED_UNKNOWN_IN_SCOPE=1
NEW_KERNEL_ID=R33-BR0G-ODD-PRIMARY-ARITHMETIC-CHARACTER-DESCENT
THEOREM_CREDIT=false
ENDPOINT_CREDIT=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
```

## Audited exact prefix

Final functional head: `47cb96b6cd7acaa19f7fc51e9f72a8dc8e36964c`.

Final-head workflow evidence:

```text
run = 32701829304
conclusion = success
artifact = 9510818470
artifact_zip_sha256 = 4c2d15df6394004addfb5ae99c40d0161b00174c59f12a5c6069061ca30afb3a
all_primary_geometric_cycle_certificate_sha256 = 5b8516e39805a6dc9082b222f08ec425dbb9a6d4449ccbd52eee2c98ea81aeb9
two_primary_function_constant_descent_sha256 = 0fad4339d6554a6546544686c1e54772f43e2a3d0f789f6fa8cdf635ea2250ef
```

The physical boundary is exactly

```text
24 side strict transforms + 48 exceptional curves = 72 components,
144 transverse codimension-two crossings,
1 connected dual graph,
integral incidence rank = 71,
integral cycle rank = 73.
```

The saturated cycle lattice and source-locked boundary action give

```text
ct = identity,
rank(cc-I) = 12,
Smith nonzero factors(cc-I) = [1 x 12],
geometric permutation-cycle fixed module = (Q/Z)^61.
```

At exponent two the exact graph-level decomposition is

```text
QFIXED_RESIDUE_CYCLE_DIM_F2=61
UNIT_SYMBOL_SECONDARY_RESIDUE_SPAN_RANK_F2=44
QFIXED_GRAPH_RESIDUAL_DIM_F2=17
```

and the stored 44+17 vectors independently span the full 61-dimensional Q-fixed cycle space.

The seven-line/Ford source pulls back with exact rank zero because the six affine ratios against `Ls=x+y+z` become squares on the endpoint sign/Kummer cover.

## Why the unit is not CLOSED

The final certificates themselves retain

```text
arithmetic_odd_character_descent_complete=false
all_primary_physical_open_unramified_kernel_complete=false
br0g_discharged=false
new_residual_kernel=R33-BR0G-ODD-PRIMARY-ARITHMETIC-CHARACTER-DESCENT
```

The completed function/constant-squareclass leaf is explicitly `EXPONENT_TWO_RESIDUAL_ONLY`; it does not identify odd-primary `H^1(-,Z/l)` boundary characters.

The authoritative Stage33-04 closure gate requires `UNRAMIFIED_PHYSICAL_OPEN_KERNEL_EXACT=true` and `BR0G=DISCHARGED`. The Stage29 boundary-Gersten receiver also keeps one-variable residue arithmetic/Galois descent inside the BR0G boundary problem. No hostile-audited contract repair has moved this named residual to Stage33-03 or Stage33-07.

Accordingly the previous pre-audit closure interpretation is superseded. Stage33-03 and Stage33-05 may continue concurrently, but Stage33-06 is not released by Stage33-04.

See `audit.md`, `audit-state.json`, and `handoff.json` for the authoritative audited state.

```text
AUDIT_VERDICT=PASS_EXACT_PREFIX_BLOCKED_NEW_KERNEL_AFTER_REJECTING_PREMATURE_BR0G_CLOSURE
NEXT_EXPECTED_COMMAND=Stage33-main-batch
```
