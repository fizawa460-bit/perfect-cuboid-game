# Stage33 MAIN transient handoff

status: UNPROMOTED_DELTA
base_main_state_canonical_sha256: 7d52c93a517fc96050b2f78583ae05e5e4ff4f983c2533c673ca008060bd0226

## Exact delta retained this batch

New exact route-audit:
- `stages/stage33/33-12/j2-marked-adapter-source-route-audit.json`
- canonical SHA256 `5fec609e3ee75fddc3833124dde81f75514de6ca8600200e594366e30022f3f8`
- verifier: `stages/stage33/33-12/verify_j2_marked_adapter_source_route_audit.py`

The current MAIN leaf remains open. No source coordinate, Kummer column, receiver, theorem, endpoint, closure, or downstream-release credit is added.

### Route audit result

1. The checked-in order-4 producer is not a live authority route under the current locked inputs. It is git-blob locked to a V2 bilinear-evaluation reduction with SHA256 `d1bb3b6f...`, while the checked-in reduction is V1 with canonical SHA256 `a5241219...`. Therefore the historical order-4/half-lift path cannot be replayed as the current named-J2 adapter.
2. Historical half-lift enumeration leaves 16384 lifts under the doubling constraint. The later quadratic filter did not source-lock the required degree-two discriminant-form transfer law, so it cannot canonically select the marked lift.
3. The current Stage33-07 actual-geometry glue certifier is the hostile-firewalled V2. It retains existence of an actual order-512 isotropic glue `H=T/L0`, but explicitly does not identify the actual integral Aut(L0) orbit, a labeled glue subgroup, or a labeled generator set. The historical rep88 claim is provenance only, not current authority.

### Refined missing datum

The next source-first input must be either:
- an actual **labeled** order-512 glue subgroup `H=T(S)/L0`, with generators in the retained coordinate-K3 discriminant basis; or
- an equivalent exact marked `NS(S) <-> T(S)` discriminant anti-isometry / basis adapter tied to the retained full-surface Smith basis.

Only after that may semantic `u1=[1,0]` / `u2` be transported and dualized into the proper-Br2 basis. V4 and raw-75D target compatibility are post-construction checks only.

next_exact_leaf:
`SOURCE_LOCK_ACTUAL_LABELED_INDEX512_GLUE_OR_EQUIVALENT_MARKED_NS_T_DISCRIMINANT_ANTI_ISOMETRY_THEN_MATERIALIZE_2x14_J2_ADAPTER`

Do not promote masks 742 or 736 from compatibility, and do not restore historical mask 6.
