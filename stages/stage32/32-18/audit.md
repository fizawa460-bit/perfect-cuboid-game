# Stage32-18 hostile audit — PR #1379

Verdict: `PASS_IMPLEMENTATION_CHECKPOINT__BLOCK_D16_NUMERICAL_CREDIT_ON_UNCERTIFIED_FLOATING_TRAVERSAL`.

Audited functional head: `d71eed2f6b527079edfb4c82f15a78abf46293bf`.
Authoritative workflow: `32802105606` / job `97664859199` (SUCCESS).
Authoritative artifact: `stage32-18-d16-aut-canonical-b6`, id `9546896868`, ZIP SHA256 `baee03244acbe98646a9252daf88f9d548e5f19b16a8f22bcf1eb6826e506b1d`.

This audit accepts PR #1379 only as a **main-path implementation checkpoint** for Aut symmetry breaking plus exact full-group leaf canonicalization. It does **not** certify the d16 numerical row, because traversal completeness still depends on uncertified `long double` LDL / reach pruning.

## 1. Source lock and exact H-perp reduction

The functional run independently rebuilds the locked Stage32 Picard core from

- upstream repository `MichaelStollBayreuth/Verification`;
- commit `51233ed5ef2bf228fac9416c66db9adc0ebcaadd`;
- `Cuboids/cuboids.magma` blob `0422b69847f2afb97cb7b3ed02ebef91279f61b1`;
- Picard-core canonical SHA256 `de84f4511ea2ea747fd712e2f5f09c7f8d94ae3633e55678b81cfe63f6ed2870`.

The d16 preparation constructs the primitive rank-63 `H^perp` lattice, applies an integral unimodular LLL transform, and produces prepared-input SHA256

`7cd24466752b21a30b4f523c04892215d5ad0f33d1cc61bc09fa8f6dc815edd3`.

The 140 restricted pairing rows have exact rank `63/63`, so the 140-pairing map is injective on the H-perp coordinates used by the enumerator. The exact preparation log also records hyperplane-row content `2`, LLL determinant `-1`, and positive reduced quadratic-form diagonal range `2..12`.

Audit verdict on this layer: **PASS**.

## 2. Aut action and canonical augmentation

The nine source-locked geometric permutations close exactly to a group of order `1536`. The production preparation chooses 64 deterministic full-group hash-spread breakers and writes their restrictions as exact integer score-difference inequalities.

At an exact leaf, PR #1379 does not use floating arithmetic for canonicality. It recomputes the norm and all 140 pairings in `__int128`, then compares the pairing vector against all 1536 group elements using the exact order

`(SHA-derived integer score, lexicographic 140-pairing)`.

The independent Python verifier reconstructs the 1536-element group from the nine source-locked generators and verifies every emitted pairing against the full orbit. The authoritative b6 output is:

- DFS nodes: `584475`;
- pre-canonical survivors: `232`;
- full-group canonical rejects: `195`;
- canonical survivors: `37` including zero / `36` nonzero;
- norm histogram: `{0:1, 2:1, 4:7, 6:28}`;
- all 37 emitted pairing vectors distinct;
- every emitted pairing is the exact full-orbit score-then-lex minimum.

The artifact files independently rehash as follows:

- `d16-b6-aut-canonical.json`: `ac5b6673de387ee9b5ac3b299848cc411ae92f435965f5437a5cf84c71e99221`;
- `d16-b6-canonical.bin`: `b3f7d3230626750da93725509fddc2628a6a5f6af61c8b677b909ba844697ecf`;
- `d16-b6-canonical-verify.json`: `3db0ff723434de613d43151b2a8060abf2347c76b1aaad301376c291c72f54a2`;
- `stage32-18-summary.json`: `0e6d7be3a8e8fd0a6246c6fb126cef52eba92d6fe4f010122b8ce3dcbaa4f8af`.

Audit verdict on the symmetry/canonicalization implementation: **PASS**.

## 3. Independent scout comparison

The prior merged d16 Aut scout gives a useful regression but not a traversal-completeness proof.

The exact same prepared H-perp SHA appears in the scout. The full-group hash64 scout produced exactly the same traversal counters before leaf canonicalization:

- nodes `584475`;
- coordinate trials `1192788`;
- constraint prunes `316433`;
- symmetry prunes `291881`;
- pre-canonical survivors `232`.

The separate orbit-profile run `32800507152`, artifact `9546364102`, ZIP SHA256 `50092d62ecc6a69930367a43a3df5de66373ec28b65abf4a7c0f98d69b05a520`, profiled the baseline set of `17833` emitted survivors into exactly `37` Aut orbits and checked that all generator images of those emitted survivors were present.

This supports the implementation regression `17833 -> 37`, but it is **not independent evidence that all b6 lattice survivors were enumerated**: the 17,833 baseline set and the 232 symmetry-pruned set both come from the same floating LDL / dual-reach traversal architecture.

## 4. Blocking exactness issue: floating traversal

The production C++ enumerator performs exact leaf verification, but the search tree itself uses `long double` quantities for:

- LDL decomposition;
- coordinate radius and interval construction;
- cap dual-reach pruning;
- symmetry dual-reach pruning;
- accumulated used norm.

The current guards are fixed heuristic margins (`1e-8` / `1e-9` scale factors). No rational enclosure, directed-rounding interval proof, exact Schur-complement certificate, or independent exact norm-ball enumeration proves that these margins dominate all accumulated floating error on every explored/pruned node.

Therefore an exact leaf recheck cannot rule out the only hostile failure mode that matters here: a valid integer branch could in principle be rejected **before reaching the leaf** by an underestimated floating reach/radius.

Consequently:

`FLOATING_REACH_TRAVERSAL_COMPLETENESS_CERTIFIED=false`

and the b6 result cannot yet receive numerical-row completeness credit. The program's internal `status=COMPLETE` means the implemented traversal exhausted without hitting its runtime/node/survivor caps; it is not an externally certified mathematical completeness statement.

Audit verdict on the requested next gate: **BLOCKED**.

## 5. Secondary provenance defect: runtime-dependent Aut canonical hash

The inherited `export_aut_action_locked.py` computes `canonical_sha256_without_this_field` over a payload that includes `magma_elapsed_seconds`. This makes the advertised Aut “canonical” SHA runtime-dependent even when the exact source and all nine permutations are unchanged.

Observed exact-permutation-identical runs include:

- orbit-profile Aut SHA `444432097bc41a5f23ba2964d4b35825db851dee33075dc5339de5542df354bf`;
- scout-final Aut SHA `69220fab5ab2452bf16aec796a4cf4adc4102d71eb2943f218a14f2604261715`;
- PR #1379 Aut SHA `48c10caf30ebfc4ccddab3576929b2fdc8780acac7ffb047fe1146d8f5b53aec`.

The nine `permutations_1based` arrays are byte-for-byte equal after JSON parsing; only the runtime receipt and the derived canonical field differ. Removing the canonical field and `magma_elapsed_seconds` gives the same stable content SHA256 for the compared runs:

`7aa6c9be4a91a25549950e1e45c2349146c6ea4cd035ff9133b41e9de3032bc3`.

Because `d16_aut_canonical_prepare.py` incorporates that runtime-dependent Aut SHA into the bundle payload, the recorded bundle SHA is also rerun-dependent. This does **not** invalidate the group action or the 37 emitted canonical pairings, but it must be repaired before these hashes are treated as durable canonical provenance identifiers.

## 6. Scope firewall and disposition

Accepted from PR #1379:

- the Aut symmetry-breaking route is successfully moved from scout code into the Stage32 main implementation path;
- the rank-63 pairing representation is injective;
- exact full-group leaf canonicalization is implemented and independently checked;
- the b6 functional regression emits 37 canonical representatives under the implemented traversal.

Not accepted:

- exact completeness of the b6 traversal;
- any complete d16 numerical row;
- any d<=176/d<=192 numerical-orbit census;
- effectivity or multibranch closure;
- any Stage29 receiver discharge;
- theorem credit;
- any perfect-cuboid existence/nonexistence conclusion.

Mandatory retained state:

`THEOREM_CREDIT=false`
`RECEIVER_CREDIT=false`
`FULL_D16_G0_ROW_COMPLETE=false`
`FULL_D176_D192_NUMERICAL_ORBIT_CENSUS=false`
`R29_LG2_NUMERICAL_COMPONENT_COMPLETE=false`
`R29_LG2=NOT_DISCHARGED`
`G10_LOWGENUS_PICARD=AMBER`

Disposition:

- `merge_allowed=true` for PR #1379 **only as the implementation checkpoint it claims**;
- `advance_allowed=false` for d16 numerical-row credit;
- `repair_required=true` before numerical completeness is promoted;
- the next d16 gate must independently certify the traversal (for example by exact/certified norm-ball enumeration or rigorous interval/rational reach bounds) and should stabilize the Aut provenance hash by excluding runtime metadata from the canonical payload.

This audit deliberately does not update `stages/stage32/controller.json`, because PR #1379 is a side implementation checkpoint while the audited controller continuation and concurrent Stage32-17 work remain separate.

`NEXT_EXPECTED_COMMAND=Stage32-main-batch`
