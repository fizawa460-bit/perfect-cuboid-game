# Stage32-07 — degree-8 bounded-multiplicity signature-cell pilot

This is the first Stage32-main-batch step after the degree-4 row closure.  It does **not** reuse the binary-exceptional Stage32-05/32-06 assumption at degree 8.

At `d=8`, the exact dual caps are

```text
known nonexceptional intersection <= 4
exceptional intersection <= 2
```

so the 48 selected exceptional coordinates live in `0..2` and the 16 selected normal coordinates live in `0..4`.

The pilot builds an exact bounded-multiplicity replacement for the binary MITM layer:

1. source-lock the rank-64 Picard core and reverify all 140 dual-cap certificates;
2. reconstruct the selected 64-coordinate transform (`det=2^38`, inverse denominator 8) and the canonical q-tail HNF quotient;
3. verify that the degree-8 q-tail domain `0..4` reaches exactly the same mod-8 subgroup as `0..3`: every q-tail generator has order dividing 4, so the extra value 4 contributes residue zero;
4. split the 48 exceptional coordinates into the same `16+4+4` A/B/C halves, but use exact dynamic programming over values `0,1,2` rather than combinations of binary masks;
5. preserve the total A/B/C multiplicities and quotient signature together, including the exact number of exceptional assignments represented by every compressed state;
6. join left/right states only when their quotient signatures can be completed by a legal q-head total and the q-tail residue subgroup;
7. treat every matched `(aggregate, split, left signature, right signature)` as an immutable **signature cell**.  This partitions the bounded exceptional assignments without materializing them one by one;
8. for solve-mode parents, run one exact QF_NIA problem per signature cell with all 64 lattice-image congruences, all 140 cap inequalities, degree/mass identities, q-head sum, exact side multiplicities and the adjunction quadratic inequality.  SAT is retained; UNKNOWN receives no closure credit; only UNSAT for every cell closes a parent.

The discovery workflow deliberately uses three solve parents of increasing size plus one count-only stress parent.  The stress parent measures compression of the bounded exceptional space but receives no mathematical closure credit.

## Audited bounded result from PR #1352

Hostile audit verdict:

```text
AUDIT_VERDICT=PASS_D8_G0_E2_COMPLETE_NUMERICAL_AUT_ORBIT_SLICE
MERGE_ALLOWED=true
ADVANCE_ALLOWED=true
```

The complete bounded numerical slice `(d,g,e)=(8,0,2)` is now accepted at numerical-orbit scope:

```text
aggregate-feasible a values = {53,54}
a=53 numerical classes      = 32
a=54 numerical classes      = 160
total numerical classes     = 192
Aut(S) order                 = 1536
Aut orbit count              = 1
full orbit size              = 192
```

The final enumeration is deterministic finite `qhead 4 + qtail 6+6`, not an SMT-timeout closure.  The `a=54` parent was reproduced on the audited head with the same parent/survivor hashes.  The Aut(S) action is re-exported from the locked Stoll upstream source, and the induced permutation group is independently reconstructed with order 1536.

Accepted complete-slice certificate:

```text
D8_G0_E2_NUMERICAL_ORBIT_SLICE_COMPLETE=true
canonical_sha256=694fc24a13b51464c510b5812a60e9ea7a6746113db91a6d85c55f9234b4250f
```

This is **not** effectivity credit and does not close the full degree-8 row.

Mandatory firewalls remain:

```text
THEOREM_CREDIT=false
RECEIVER_CREDIT=false
FULL_D8_G0_ROW_COMPLETE=false
FULL_D176_D192_NUMERICAL_ORBIT_CENSUS=false
R29_LG2_NUMERICAL_COMPONENT_COMPLETE=false
R29_LG2=NOT_DISCHARGED
R29_LG2_EFF=NOT_DISCHARGED
R29_LG2_MB=NOT_DISCHARGED
G10_LOWGENUS_PICARD=AMBER
```

## Next Class-2 wall

The higher-mass parents are the unresolved successor.  The exact signature inventory already gives:

```text
e8/a36  :     95,973 exceptional assignments ->   53 signature cells
e10/a30 :    703,688 exceptional assignments ->  134 signature cells
e20/a0  : 1,032,477,716 exceptional assignments -> 1,182 signature cells
```

The generic QF_NIA cell solver times out on representative nontrivial cells.  Do not promote UNKNOWN, do not substitute longer timeouts, and do not materialize the billion-state stress parent.  The successor must introduce an independently exact symmetry-aware or lattice-aware cell solver/reducer.

## Scope stop

Stage32-07 itself is complete at the audited `e=2` numerical-orbit slice.  Work beyond that point belongs to the next Stage32 unit.  Effectivity, the full `d=8` row, the full low-degree census, and all Stage29 receiver credit remain open.
