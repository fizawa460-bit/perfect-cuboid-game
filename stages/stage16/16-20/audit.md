# Stage16-20 audit

Status: PASS

Audited submission: `fcc84bc56d471e29e5b81674dfaeebda5d2a3d65` (PR #894 submission head)

## Verdict

The Stage16-20 finite-data baseline is accepted under the frozen Stage16-10 population contract.

The enumerator preserves the certified population exactly:

- positive canonical edges `0<a<b<c`;
- global primitiveness `gcd(a,b,c)=1`;
- common cutoff `R=sqrt(a^2+b^2+c^2)<=B`;
- exactly one integral face diagonal;
- no space-diagonal integrality requirement.

AR-001 and AR-002 are used compatibly. Coverage is complete because the unique integral face is generated through primitive Euclid data plus scale, the third edge is exhaustively scanned within the `R<=B` bound, and canonicalization/global-primitiveness/exact face multiplicity are rechecked on the final triple. Exactly-two and exactly-three cases are excluded by the final exact-one signature test.

Independent direct canonical-triple scans agree with the frozen CSV at least at:

- `B=50`: `M_1(B)=490`;
- `B=100`: `M_1(B)=2620`;
- `B=200`: `M_1(B)=12664`;

including the diagnostic `ab/ac/bc` split. The frozen CSV SHA-256 agrees with the recorded value

`407d9e7a6ed2218e7897271b4de299d805a06ea6bf149aad09df92fb4dc5a347`.

The dedicated Stage16-20 finite-data GitHub Actions replay completed successfully, including:

```text
SMALL_CUTOFF_CROSSCHECK_B=100:PASS
FROZEN_CENSUS_MAX_B=2000:PASS
STAGE16_20_VERIFY=PASS
```

## Evidence boundary

The census remains `COMPUTED`. Stage16-20 does not promote the finite observations to an asymptotic growth law, exponent, ratio/thinning theorem, upper or lower bound, or causal mechanism. Growth/ratio interpretation belongs to checkpoint 30.

```text
AUDIT_VERDICT=PASS
ADVANCE_ALLOWED=true
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
NEXT_CHECKPOINT=30
NEXT_STAGE=
CODEX_AUDIT_REQUIRED=false
CODEX_REASON=NONE
MERGE_ALLOWED=true
```
