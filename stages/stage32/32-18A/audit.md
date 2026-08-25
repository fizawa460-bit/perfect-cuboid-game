# Stage32-18A hostile audit — PR #1382

Verdict: `PASS_EXACT_B6_TRAVERSAL_CERTIFICATE_AND_STABLE_AUT_PROVENANCE`.

Audited functional head: `17a34b41e6c98db77c76d433fa69591353b4ed08`.
Authoritative workflow: `32808355343` / job `97682781166` (SUCCESS).
Authoritative artifact: `stage32-18a-d16-b6-exact-traversal-certificate`, id `9549064522`, ZIP SHA256 `ac5f78b4123f7e5cf8396b8c0c784e973c6dee325f90e32aece407237b7e08da`.

This audit closes the two defects left by the Stage32-18 audit: uncertified floating traversal at b6 and runtime-dependent Aut provenance. It grants an exact **b6 certification gate** only. It does not close the d16 row and does not prove that the fast floating traversal is mathematically complete for larger future bounds.

## 1. Exact traversal completeness

The independent certifier reconstructs the rank-63 LDL decomposition over `boost::multiprecision::cpp_rational` and checks `L D L^T = Q` entry-by-entry exactly. Positive pivots are required at every step.

For the reverse DFS, the identity

`Q(z) = sum_i D_i (z_i + sum_{j>i} L_{j,i} z_j)^2`

is therefore exact. At coordinate `i`, the code chooses an integer radius `R` with `R^2 > remaining/D_i`, hence the enumerated interval is an exact rational **superset** of every feasible integer coordinate. Every candidate is then retained for descent only after the exact test `D_i t_i^2 <= remaining`. No floating radius can remove a branch.

The 140 cap rows are converted exactly to the LDL coordinates. A branch is rejected only when the exact rational Cauchy–Schwarz certificate

`dist(center,[0,cap])^2 > remaining * sum_{k<=i} a_k^2/D_k`

holds. `long double` quantities are used only to decide whether to spend time attempting this exact check. If the floating scheduler is inaccurate it can only miss a pruning opportunity; it cannot itself reject a branch.

The 64 Aut breaker inequalities are not used for traversal pruning in the exact certifier. They are evaluated only at leaves with exact integer arithmetic. Norm and all 140 pairings are also recomputed exactly at leaves using `__int128`. The exact traversal finished at 2,595,339 nodes, far below the 100,000,000 node guard.

Exact b6 result:

```text
nodes                         = 2,595,339
coordinate trials             = 7,076,172
exact cap-prune checks         = 16,763,653
exact certified cap prunes    =   524,319
complete b6 cap survivors     =    17,833
+ 64 exact Aut breakers       =       232
+ full order-1536 canonical   =        37 (36 nonzero)
norm histogram                = {0:1,2:1,4:7,6:28}
```

Audit verdict on b6 traversal completeness: **PASS**.

## 2. Aut provenance repair

The previous audit found that `export_aut_action_locked.py` included `magma_elapsed_seconds` in its advertised canonical payload. Stage32-18A leaves that historical export untouched and defines the mathematical Aut content hash after removing only

- `magma_elapsed_seconds`, and
- the legacy derived `canonical_sha256_without_this_field`.

The audit independently recomputed this content hash from the new artifact:

`7aa6c9be4a91a25549950e1e45c2349146c6ea4cd035ff9133b41e9de3032bc3`.

The prior Stage32-18 artifact had elapsed time `23.949964` and legacy hash `48c10caf...`; the Stage32-18A artifact has elapsed time `23.777706` and legacy hash `5d704375...`. The nine `permutations_1based` arrays are identical, and both artifacts independently reduce to the same stable content hash above.

The nine generators were independently closed again during hostile audit and give exact group order `1536`.

Audit verdict on stable Aut provenance: **PASS**.

## 3. Independent canonical-set check

The exact and fast canonical dumps are byte-identical and independently rehash to

`b3f7d3230626750da93725509fddc2628a6a5f6af61c8b677b909ba844697ecf`.

Hostile audit parsed all 37 binary records and verified:

- magic and record length are exact;
- all 37 records are distinct;
- norm histogram is `{0:1,2:1,4:7,6:28}`;
- the Aut group reconstructed independently from the nine source-locked generators has order 1536;
- the SHA-derived score weights were regenerated independently from seed `stage32-d16-aut-a`;
- every one of the 37 emitted pairings is the exact full-orbit `(score, lexicographic pairing)` minimum.

Thus the certified exact traversal and the existing fast implementation agree on the complete b6 orbit representative set, not merely on a survivor count.

Audit verdict on the b6 regression/cross-certificate: **PASS**.

## 4. Future-production boundary

This PASS does **not** prove the fast implementation's floating radius/dual-reach pruning safe for arbitrary bounds greater than 6. The equality at b6 is an exact regression certificate for b6 only.

Therefore Stage32-18B may advance, but any numerical credit at new production bounds must be backed by one of:

1. the exact rational traversal itself;
2. a rigorously outward-enclosed replacement for every pruning decision; or
3. an exact cross-certificate proving the fast canonical output identical to a complete certified traversal at the credited bound/range.

A successful b6 gate may justify the architecture and scheduling choice, but it is not a theorem that heuristic floating margins remain complete at all future radii.

## 5. Scope firewall

Accepted:

- exact completeness of the d16 `b=6` Hperp norm/cap census;
- exact `17,833 -> 232 -> 37` Aut compression at b6;
- stable Aut mathematical content SHA;
- exact equality of certified and fast canonical b6 sets;
- release of the next bounded-production engineering leaf.

Not accepted:

- a complete d16 g0 row;
- global completeness of the fast floating traversal for future bounds;
- the full d<=176 / d<=192 numerical-orbit census;
- effectivity or multibranch closure;
- any Stage29 receiver discharge;
- theorem credit;
- any Perfect Cuboid existence/nonexistence conclusion.

Mandatory retained state:

```text
D16_B6_TRAVERSAL_CERTIFIED=true
D16_B6_CANONICAL_ORBIT_SET_CERTIFIED=true
FAST_TRAVERSAL_GLOBAL_COMPLETENESS_CERTIFIED=false
D16_PRODUCTION_EXACT_OR_CROSS_CERTIFICATE_REQUIRED=true
FULL_D16_G0_ROW_COMPLETE=false
FULL_D176_D192_NUMERICAL_ORBIT_CENSUS=false
R29_LG2_NUMERICAL_COMPONENT_COMPLETE=false
R29_LG2=NOT_DISCHARGED
R29_LG2_EFF=NOT_DISCHARGED
R29_LG2_MB=NOT_DISCHARGED
G10_LOWGENUS_PICARD=AMBER
THEOREM_CREDIT=false
RECEIVER_CREDIT=false
STAGE32_CLOSED=false
```

Disposition:

- `merge_allowed=true` for PR #1382 as the exact b6 certification gate;
- `advance_allowed=true` to `32-18B-D16-AUT-CANONICAL-BOUNDED-PRODUCTION` under the production exactness firewall above;
- `repair_required=false` for the Stage32-18A defects;
- d8 e20/a0 remains paused and restartable at the audited `<=114186` checkpoint.

`NEXT_EXPECTED_COMMAND=Stage32-main-batch`
