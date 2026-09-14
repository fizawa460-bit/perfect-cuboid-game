# N398 handoff — audited survivor affine parity compression

## Authority status

N398 is **hostile-audit PASS / retained** on the bounded N391 population only.

Authoritative audit receipt:
- `AUDIT-PASS.json`
- hostile-audit verdict: `PASS`
- hostile-audited exact head: `71f078a7521b265e300a450ab129370f077ef6a1`
- hostile-audit review: `5198108138`

`STATE.json` records the earlier audit-boundary freeze and is historical with respect to audit status. For continuation, `AUDIT-PASS.json` is authoritative.

## Retained mathematical result

Scope is exactly:
- row: `g1-d008`
- `g=1, d=8, e=8`
- retained blocks: `97`
- width per block: `113`
- retained terminal identities: `10,961`
- N396 survivors: `5,459`
- N396 rejected: `5,502`

Exact retained classifier on all 97 block signatures:

`x49 = x93 + x96 (mod 2)`

Using the hostile-audited N395 relation

`x93 + x98 + x96 = 1 (mod 2)`

this is equivalently

`x49 + x98 = 1 (mod 2)`.

The N396 parity masks split as:
- `0x55`: 27 blocks
- `0xaa`: 70 blocks

The naive direct mod-2 free-image diagnostic does **not** itself produce the classifier (`left_nullspace_dimension=60`, induced fixed-relation rank `0`). Treat the classifier as the exact bounded higher-2-adic-compatible relation actually audited, not as a global direct mod-2 theorem.

## Source locks

Retain these exact identities when consuming N398:
- N398 RESULT canonical SHA256: `611632cedd9ff3515bb374a608020dd06079240db5224bb15f90845c7b90cad7`
- N398 STATE canonical SHA256: `f1146a2fda26d4d747e710b90ab829dd27b09118471a4d385046a1cb1215fcd1`
- N398 probe blob: `fa8aa54ce4c69a8b735255b53896c939bb84542f`
- N396 RESULT canonical SHA256: `e34e23e2b17063c2f51d9862af1c2a958002fdb0327e43b5e52d85bcb1a83cd1`
- N395 hostile-audited exact head: `604780ed17dbbb575f53a632a317a1308036157d`

Exact-head claim-frontier for the audited N398 boundary succeeded (`34843938538`). The MAIN-startup failure at that boundary was a separate stale expected-main freshness pin, not an N398 mathematical failure.

## Allowed continuation

Continuation is allowed only on the retained N391 `97-block / 10,961-terminal` population.

The required next work is a **materially distinct exact transport** of this audited block-level classifier to terminal identities, or another bounded FULL178 compression certificate. N399 is the current concrete continuation of that requirement.

Do **not**:
- repeat the same `97 x 8` parity census;
- infer the rule outside the retained 97 blocks;
- promote this result to new pruning or MAIN subtraction;
- claim numerical leaf-compression, FULL178, theorem, effectivity, endpoint, Stage32 closure, or Perfect Cuboid existence/nonexistence.

## Credit / process firewall

N398 licenses **bounded structural compression only**.

Additional pruning credit: `0`.
MAIN pruning/subtraction: not licensed.
Heavy compute: not authorized by N398.
Merge: not authorized.

## Consumer handoff

A consumer should read, in order:
1. `AUDIT-PASS.json`
2. `RESULT.json`
3. this `HANDOFF.md`
4. N399 `STATE.json` / `RESULT.json` when continuing the terminal-identity transport.

The audited N398 result has already been consumed by N399. Do not reopen N398 unless a later hostile audit or central authority explicitly revokes or supersedes it.
