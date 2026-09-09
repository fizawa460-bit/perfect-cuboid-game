# N104 — FULL178 completeness and replay certificate architecture

## Scope and credit ceiling

This note defines a machine-checkable final coverage/replay contract for the 178-row FULL178 production domain. It does not certify that the numerical census is complete, does not promote prefix completion to numerical-row completion, and grants no theorem, receiver, route, B18, or perfect-cuboid credit.

## Reuse decision

Decision: `PARTIAL_REUSE`.

The production tree already contains the authoritative domain and several useful hash/checkpoint contracts:

- `stages/stage32/residual-32-01-production/full178-manifest.json` fixes the audited 183-row source, the exact five degree-<=6 exclusions, the 178 residual rows, m-class decomposition, and `coarse_strata_count = 64111`; its canonical payload SHA-256 is locked.
- `full178-production-preflight.json` fixes the production semantics that a row is complete only when all disjoint work units are complete with zero unknown, and that node-ceiling exhaustion is a resource event rather than UNSAT.
- `verify_full178_preflight.py` already supplies the canonical JSON hash convention (`sort_keys=True`, compact separators), reconstructs the 178 rows from the audited 183-row source, verifies uniqueness, and recomputes the 64,111 exact `(row,e)` coarse strata.
- `run_full178_resumable_work_unit.py` already emits self-hashed exact work-unit payloads, canonical work-unit identities, completed partition records, continuation cursors, segment-chain hashes, and explicit `unknown_count`; it also keeps `numerical_row_complete = false` at the prefix-only layer.
- `full178-prefix-indexed-compression-main-checkpoint.json` supplies the current exact indexed terminal-family representation, records a canonical terminal order, retains terminal-set semantics across the DFS-to-indexed reparameterization, and explicitly records that numerical Picard leaf checks are not complete.

No existing artifact found in the bounded Stage32 production search closes all 178 rows by aggregating every required stratum, rejecting overlap/gaps, and replay-checking the load-bearing producer evidence. Therefore the domain/hash machinery is reusable, but a new aggregate completeness/replay certificate layer is required.

## Authoritative domain

The final verifier MUST derive the domain; it MUST NOT infer completeness from filenames, workflow success, shard counts, or a production summary flag.

1. Load and verify `full178-manifest.json` using the same canonical hash convention as `verify_full178_preflight.py`.
2. Reconstruct the audited 183 source rows and remove exactly the five locked degree-<=6 row IDs.
3. Require exactly 178 distinct residual row IDs.
4. For each row `(genus, degree)`, derive the required exceptional-mass interval
   - genus 0: `e = 8 .. floor(19*degree/5)`;
   - genus 1: `e = 4 .. floor(19*degree/5)`.
5. Enumerate the canonical coarse stratum key `S = (row_id,e)` in row-id/e order and require exactly 64,111 distinct keys.

This canonical set is `EXPECTED_STRATA`. A certificate is incomplete unless every member is accounted for exactly once at the aggregate level.

## Route-independent normalization

The final certificate MUST normalize route-specific output into the current exact indexed terminal-family coordinate system rather than treating a route's internal shard/work-unit IDs as global identities.

For each coarse stratum `S=(row_id,e)`, let `N(S)` be the exact symbolic terminal count produced by the retained compressed terminal-family counter under the same source/marking locks used by production. The indexed terminal family gives a canonical rank domain `[0,N(S))`.

Every load-bearing producer emits one or more normalized coverage blocks:

```text
(row_id, e, rank_lo, rank_hi, disposition, producer_contract_sha256, evidence_sha256)
```

with half-open interval semantics `[rank_lo,rank_hi)`. `disposition` is restricted to a verifier-owned vocabulary such as `NUMERICAL_CHECKED` or `EXACT_PRUNED`; route-local names do not grant credit. A producer that naturally proves a non-contiguous subset emits multiple canonical intervals. A producer unable to map its claim into this canonical rank domain receives no completeness credit.

This is the integration seam that makes the aggregate certificate independent of whether the winning implementation is legacy/resumable DFS, indexed random access, a direct Picard finite-state reduction, or another exact pruning route.

## Minimal final aggregate schema

The eventual machine artifact should have a schema equivalent to:

```json
{
  "schema": "STAGE32_FULL178_COMPLETENESS_REPLAY_CERTIFICATE_V1",
  "source_locks": {
    "full178_manifest_sha256": "...",
    "audited_source_payload_sha256": "...",
    "terminal_family_contract_sha256": "...",
    "terminal_indexer_contract_sha256": "..."
  },
  "domain": {
    "residual_row_count": 178,
    "coarse_strata_count": 64111,
    "expected_strata_canonical_sha256": "..."
  },
  "producers": [],
  "strata": [],
  "aggregate": {
    "missing_strata": 0,
    "duplicate_strata": 0,
    "overlap_blocks": 0,
    "gap_blocks": 0,
    "unknown_count": 0,
    "replay_failures": 0,
    "numerical_rows_complete": 178
  },
  "firewalls": {
    "prefix_completion_is_numerical_completion": false,
    "theorem_credit": false,
    "receiver_credit": false
  },
  "verdict": "PASS_FULL178_NUMERICAL_CENSUS_COMPLETENESS_REPLAY"
}
```

The illustrative zero values above are schema placeholders, not current Stage32 facts. A production certificate MUST be generated from retained producer evidence; no field may be hand-promoted from this architecture note.

## Coverage invariants

For each `S=(row_id,e)` the verifier MUST:

1. Recompute `N(S)` from the locked terminal-family contract.
2. Canonically sort all normalized blocks by `(rank_lo,rank_hi,producer_id,evidence_sha256)`.
3. Require integer bounds `0 <= rank_lo < rank_hi <= N(S)` except that `N(S)=0` is represented by an explicit empty-stratum evidence record.
4. Require exact disjoint union of the rank domain: first `rank_lo=0`, adjacent blocks satisfy `prev.rank_hi == next.rank_lo`, and final `rank_hi=N(S)`.
5. Reject overlap even when two producers report the same mathematical object. Duplicate evidence is not additional coverage.
6. Require `unknown_count=0` for every credited block and every stratum.
7. Require every block disposition to be supported by a registered exact verifier contract. Telemetry, timeout, node-ceiling exhaustion, heuristic pruning, or workflow success alone is not a disposition.
8. Require all 64,111 expected strata and no extra `(row_id,e)` keys.

A row is numerically complete iff every expected stratum belonging to that row passes these checks and every terminal rank is either numerically checked or eliminated by an exact registered prune. Prefix-stage completion alone is insufficient.

## Duplicate / orbit accounting

The aggregate verifier MUST make duplicate control structural rather than statistical:

- the authoritative outer key is the unique `(row_id,e)` stratum key derived from the manifest;
- the authoritative inner identity is canonical indexed terminal rank under the locked terminal-family/indexer contract;
- route-local work-unit IDs and legacy DFS stream position are evidence metadata only;
- any route changing symmetry normalization or terminal-set semantics must provide a separately audited bijection into the locked canonical rank domain before its blocks are creditable;
- changing enumeration order without changing the represented terminal set is acceptable only after that bijection/contract lock passes.

## Replay contract

Each credited producer contract MUST expose deterministic replay inputs sufficient to reconstruct its normalized coverage blocks and verdicts. The aggregate verifier MUST check source/module/manifest/indexer hashes, canonical producer hashes, deterministic normalized block reconstruction, equality of evidence-root hashes, and exact reproduction of fail-closed fields including `unknown_count` and numerical-completion status. Timestamp/workflow/job/artifact IDs are provenance only, not mathematical coverage identity.

## Fail-closed conditions

The final verifier returns nonzero / non-PASS on any manifest/source/hash mismatch; wrong row or stratum counts; missing/extra/duplicate strata; rank-domain gap/overlap; unregistered disposition; producer evidence/replay mismatch; any `unknown_count > 0`; any use of resource exhaustion as UNSAT; any promotion of prefix/indexed completion to numerical completion; or any producer that cannot map bijectively into the locked canonical rank domain.

## Implementation seam for MAINBATCH

Later implementation should be two small layers, not a new search engine:

1. `build_full178_completeness_certificate.py`: ingest registered producer certificates, normalize into canonical rank blocks, emit aggregate certificate.
2. `verify_full178_completeness_certificate.py`: independently reconstruct `EXPECTED_STRATA`, recompute terminal counts/domain locks, verify exact block union and replay contracts, fail closed.

Producer-specific adapters stay outside the aggregate verifier and expose only the normalized block contract.

## Retained result

`PASS_N104_COMPLETENESS_REPLAY_ARCHITECTURE_DEFINED`.

This is an architecture checkpoint only. Current production state remains incomplete: the indexed-compression checkpoint explicitly has `numerical_picard_leaf_checks_complete = false`, and no FULL178 completeness credit is granted here.
