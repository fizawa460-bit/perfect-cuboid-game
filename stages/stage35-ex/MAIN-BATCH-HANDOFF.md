# Stage35-EX MAIN batch handoff — Goal4AK audit-ready provisional exact result

Authority remains **V73 / audited Goal4AJ**. This handoff records an unpromoted Goal4AK result only. It grants no authoritative explicit-F_B, local-evaluation, Brauer-Manin, E1, Stage35, receiver, theorem, endpoint, or perfect-cuboid credit.

## Provisional Goal4AK result

PR: `#1720`
Branch: `stage35-ex-goal4aj-audited-sync-fb-assembly`

The fixed class-B representative has been materialized provisionally as

`F_B := A31 / B31`

with both `A31` and `B31` homogeneous of degree 31 in

`(a1,a2,a3,b1,b2,b3,c)=(h,x,y,z,q,p,w)`.

The corresponding class is `(-1,F_B)` modulo `Br_0(U)`. Multiplying this fixed representative by `q in Q^*` changes the quaternion symbol only by the constant class `(-1,q)`, so the independently fixed numerator/denominator Q-normalizations are compatible with the Goal4Z modulo-constants target. Downstream local evaluation must nevertheless keep this exact normalization unless a constant-class adjustment is explicitly tracked.

### Exact permanent inputs

Numerator:
- permanent manifest: `stages/stage35-ex/35ex-35/goal4aj-degree31-qcandidate-gen24-gzip-chunks.json`
- manifest blob: `85b52e921f36fc445fd243db1a3b3f65bb298966`
- raw text bytes: `208802`
- support count: `5924`
- SHA256: `358ee320a7d28b790ee9267aad3f95e8ff35af15d002976720622bd2b6e8decb`

Denominator:
- transport: `stages/stage35-ex/35ex-35/goal4ak-degree31-denominator.txt.gz.b64`
- repaired transport blob: `5e25d4db44249f6eba0c03863e49f2522c8e54c8`
- transport manifest: `stages/stage35-ex/35ex-35/goal4ak-degree31-denominator-transport.json`
- manifest blob: `586a37bfe90a5fd3773c7d3525dde7c873ddedca`
- manifest canonical SHA256: `f0e1187b89c3c7ea577e6404c75d3459a3d343d9b4bf56cdc4053a50f40a2522`
- base64 SHA256: `ef7d9c7a360807a85b10a45b150a1636f01ed78bfc0f3b5ca05584eaf2749e1e`
- gzip bytes: `8346`
- gzip SHA256: `43b1ef891c21e3ec4279c70da0661d7987051b3eaaaf418db2158ede481a822d`
- raw text bytes: `42489`
- support count: `1542`
- raw polynomial SHA256: `28d738a7a23df1ace371cabe3a476c270a54c6b7798e8172bd7111b14e25fc29`

The first repo-side denominator Base64 copy was operationally corrupt (gzip CRC failure). It was replaced byte-for-byte from the retained successful gen1 Actions artifact. This was a transport defect only, not a mathematical failure.

### Goal4AK assembly/evaluator

- artifact: `stages/stage35-ex/35ex-35/goal4ak-explicit-fb-assembly.json`
- artifact blob: `5c543b8e5172e19cdb143ba69fcaa55098e5920f`
- artifact canonical SHA256: `105060a54ae5c64ba4d3d978fce5a7b76e890ee1516268b09ac96c4722d982d9`
- exact loader/evaluator: `stages/stage35-ex/35ex-35/goal4ak_explicit_fb.py`
- loader blob: `3c5814fd98375f1eeeefd33f7fb99d9c888fbb9a`
- denominator verifier: `stages/stage35-ex/verify_stage35_ex_35_goal4ak_denominator_transport.py`
- denominator verifier blob: `5d91bb21f139fa6d79e75d4b400af517b7638a90`
- top verifier: `stages/stage35-ex/verify_stage35_ex_35_goal4ak_explicit_fb.py`
- top verifier blob: `72e6cf5da10fc6ff72e5712a0647bce603525b6c`

Exact CI:
- run: `34225212517`
- job: `102057540758`
- checked head: `84a9906500e2b3f0c71a48cb1b162930888b6db2`
- conclusion: `SUCCESS`
- markers:
  - `STAGE35_EX_GOAL4AJ_QCANDIDATE_CHUNKS=PASS`
  - `STAGE35_EX_GOAL4AK_DENOMINATOR_TRANSPORT=PASS`
  - `STAGE35_EX_GOAL4AK_EXPLICIT_FB=PASS`
  - `downstream_local_evaluation_released=false`

The verifier reconstructs both permanent coefficient streams, parses all `5924 + 1542` terms exactly over `Fraction`, checks degree 31 on both sides, evaluates `F_B` exactly, and verifies projective scaling cancellation `A(2P)/B(2P)=A(P)/B(P)`.

## Authority / freshness firewall

- authoritative `MAIN-STATE.json` remains V73 with Goal4AJ as `last_audited_authority` (review `5140644783`).
- Goal4AK remains provisional pending hostile audit.
- a byte-identical V73 snapshot was added at `stages/stage35-ex/snapshots/MAIN-STATE-V73-84a9906500e2.json`, blob `9dfb9f44b1c84ae774f80ce5021193a5d6cd8807`, snapshot commit `c34fc5510b74032df7feaf583400e5fd05021b91`.
- current main observed after Goal4AK CI: `538913633330a8414c87931d3c52f93e4aaf5d0f` (Stage33 merge), while PR merge-base remains the Stage35-EX #1698 merge `e98b06455d34bf2f346d297d9370e82fc2a71970`.
- therefore PR freshness is behind by one unrelated-main commit and must be synchronized/rechecked before hostile-audit credit or promotion.

## Next legal action

`HOSTILE_AUDIT_GOAL4AK_BEFORE_LOCAL_EVALUATION_RELEASE`

Do **not** continue to local evaluation, Brauer-Manin, E1, Stage35 closure, or endpoint credit from this handoff without the audit/release required by the active Research OS credit firewall.
