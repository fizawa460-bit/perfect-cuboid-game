# N399 handoff — terminal parity predicate transport

## Authority status

N399 is **AUDIT_BOUNDARY_FROZEN / hostile audit pending**.

Mathematical frozen head:
- `288dbc668894a5e356770abff0109d89d16ba6b3`

Generation exact head:
- `22f1c8e3fe9ac587a62b4321c9a49cba5dc310f0`

Next mandatory gate:

`HOSTILE_AUDIT_N399_N398_TERMINAL_PARITY_PREDICATE_TRANSPORT`

This handoff is documentation only. It does not advance the mathematical frontier, grant credit, or authorize N400.

## Audited predecessor

N399 consumes the hostile-audited N398 result:
- N398 hostile-audit verdict: `PASS`
- N398 audited exact head: `71f078a7521b265e300a450ab129370f077ef6a1`
- N398 hostile-audit review: `5198108138`
- N398 audit receipt canonical SHA256: `aa616a76bff47b9352c7eaa5397236e672b8b9d3f6552a85dc6b8c5905365499`

No N399 claim may exceed the N398 retained scope.

## Candidate result to audit

Scope is exactly:
- row: `g1-d008`
- `g=1, d=8, e=8`
- retained blocks: `97`
- block width: `113`
- terminal identities: `10,961`

N399 transports the N398 block-level classifier to every terminal identity in those retained blocks using the predicate:

`(x49 + x98) mod 2 = 1`

Exact reconstructed identity counts:
- SAT / N396 survivors: `5,459`
- UNSAT / N396 rejected: `5,502`

Exact terminal-rank stream hashes:
- SAT: `00204cd76766c48e7502cb8091de1fe307f34b7486fa161c6c58f7cdb8e36fd4`
- UNSAT: `6648c3a246b71f74dec275012f0218d8a44477cd756229e6e3bc3eda965ca262`

Transport checks recorded as true:
- every non-`x49` coordinate is invariant within each retained block;
- N398 `x49=x93+x96 (mod 2)` agrees with the N395-reduced `x49+x98=1 (mod 2)` on all 97 blocks;
- the terminal predicate matches the block parity on all `10,961` identities;
- the predicate reconstructs both N396 SAT and UNSAT terminal-rank streams exactly.

This is a terminal-identity transport candidate, not a new pruning theorem.

## Source locks / certificate

Retain these exact identities:
- N399 RESULT canonical SHA256: `3446990aa48dfcce12032b157cd10ed853e059e42d803561c41d4a8ed91bf4c2`
- N399 STATE canonical SHA256: `d25aa7a3b4d6e5265cc1098d1c6d97b3546eef3d0d8aa76f59b60d9e5886e1b0`
- N399 verifier blob: `2ee0908ceee066a3f84cce93b20444c2d8a054bc`
- certificate canonical SHA256: `4be132e95c65614931227b167f9217b1d240e76ba84a0c9a2ad8ea0e305cbb1c`
- block stream SHA256: `b28506a8c959f521f4299338cc49899078e28ab5faa73b0736d9e1c877d12f56`
- required parity stream SHA256: `016ea206020c0c049497be3f87430cb1ea9b3ff2c53794f62b5961a7854b2e21`

Generation replay:
- claim-frontier run `34848789135`
- job `103991169643`
- conclusion: `SUCCESS`

Frozen-boundary exact-head CI at `288dbc668894a5e356770abff0109d89d16ba6b3`:
- claim-frontier `34849560269`: `SUCCESS`
- stale-run sweeper `34849560282`: `SUCCESS`
- MAIN startup `34849560290`: failure only at research-freshness resolution because of the known stale expected-main pin (`expected 4c51b4ea...`, current at that run `117310b6...`). This is separate from N399 mathematics.

## Hostile-audit checklist

The hostile audit must independently verify:
1. source-lock integrity and exact-head replay;
2. exact reconstruction of the N396 SAT and UNSAT terminal-rank streams;
3. invariance of all non-`x49` coordinates within each retained block;
4. agreement of the N398 primary rule and N395-reduced rule on all 97 blocks;
5. no inferred transport outside the retained N391 97-block population;
6. no double charging or promotion to pruning/MAIN/numerical/theorem/effectivity/endpoint credit;
7. workflow lifecycle and freshness separation.

## Stop conditions / firewalls

Until hostile audit PASS:
- **do not start N400**;
- do not repeat the same `97 x 8` parity census;
- do not infer the predicate beyond the retained 97 blocks;
- additional pruning credit remains `0`;
- MAIN pruning/subtraction remains unlicensed;
- numerical leaf-compression credit remains false;
- FULL178 remains incomplete;
- theorem/effectivity/endpoint/Stage32 closure remain false;
- heavy compute remains unauthorized by this node;
- merge remains unauthorized.

## Consumer handoff

A hostile-audit consumer should read, in order:
1. `N399/STATE.json`
2. `N399/RESULT.json`
3. `N399/HANDOFF.md`
4. `N398/AUDIT-PASS.json`
5. the N399 verifier and locked predecessor artifacts as needed.

The only valid next transition is: hostile audit N399 -> PASS/FAIL receipt. Mainbatch must remain stopped at this boundary until that receipt exists.
