# Stage32-05 — exact fixed-weight MITM quotient closure

Stage32-05 now promotes the successful feasibility probe into a full exact bounded-parent solver for two Stage32-04 residual parents:

- `d6-g1-e2-a39`
- `d6-g1-e10-a15`

It still carries **no receiver credit** and **no Stage29 theorem discharge**. Any bounded-parent closure remains `audit_status=PENDING` until an independent hostile audit/recomputation accepts the new reducer and the residual QF_NIA checks.

## Exact architecture

1. Source-lock the Stage32 Picard core from run `32624596141`.
2. Re-derive the 140 Stage32-04 dual-cap certificates and verify every identity over the locked rank-64 primitive Picard basis. The required canonical certificate SHA256 is `75224aee543dcd4a56e814503765d1e1e69514b237fb900688243546ea6b4d03`.
3. Reconstruct the 64 selected-intersection coordinate system, requiring determinant `2^38`, inverse denominator `8`, and Smith invariants `1^40,2^14,4^6,8^4`.
4. Use the exact aggregate coefficient structure of the 48 exceptional coordinates: 32 type-A, 8 type-B, 8 type-C. The first four selected normal coordinates have one common aggregate triple; the remaining 12 have zero degree/mass aggregate contribution.
5. For those final 12 coordinates, compute the column-HNF of `[C_tail | 8I]`. Each tail generator has order at most 4, so its allowed values `0..3` span the full cyclic subgroup. An independent finite reachable-set DP must equal the HNF subgroup size exactly (`16384 = 2^14`).
6. Form the exact additive quotient signature `K = (8 H^{-1}) * inverse_integer (mod 8)`. The 12 q-tail columns vanish in this quotient.
7. Split each exceptional aggregate type evenly (`16+16`, `4+4`, `4+4`) and exhaustively enumerate all type-count splits. Hash-join the two halves in the q-tail quotient, including the exact q-head aggregate signature.
8. Materialize every exceptional assignment surviving the exact quotient join. No sampling is used in this stage.
9. Pass every surviving assignment to the same exact denominator-8 intersection-coordinate QF_NIA conditions, now with only 16 selected-normal variables free. Enforce all 140 cap inequalities, lattice-image congruences, degree/mass identities, and exact adjunction quadratic inequality. `SAT` is recorded; `UNKNOWN` receives no credit; only `UNSAT` closes a candidate.
10. With `--proof`, persist a compressed Z3 proof and SHA256 for every UNSAT residual candidate.

Local pre-CI regression of the exact reducer gives:

- `d6-g1-e2-a39`: 0 exceptional candidates after the exact quotient join;
- `d6-g1-e10-a15`: 672 exceptional candidates passed to the 16-variable exact QF_NIA backend;
- q-tail reachable residue count: 16384.

These are regression expectations only until CI independently reproduces them.

## Firewalls

```text
THEOREM_CREDIT=false
AUDIT_STATUS=PENDING
RECEIVER_CREDIT=false
LOW_DEGREE_PREFIX_COMPLETE=false
FULL_D176_D192_NUMERICAL_ORBIT_CENSUS=false
R29_LG2=NOT_DISCHARGED
R29_LG2_EFF=NOT_DISCHARGED
R29_LG2_MB=NOT_DISCHARGED
G10_LOWGENUS_PICARD=AMBER
```

A passing Stage32-05 workflow claims only exact bounded closure of the named parent(s), pending independent audit. It does not complete the 183-row low-degree census, prove orbit completeness, discharge effectivity/multibranch receivers, or resolve the perfect cuboid problem.
