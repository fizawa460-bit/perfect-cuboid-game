# Stage16-20 — finite-data baseline

Status: **SUBMITTED_FOR_FRESH_AUDIT**

## Scope

This checkpoint uses the audited Stage16-10 population without modification:

\[
0<a<b<c,\qquad \gcd(a,b,c)=1,\qquad R=\sqrt{a^2+b^2+c^2}\le B,
\]

with **exactly one** integral face diagonal and no space-diagonal integrality requirement.

The purpose of Stage16-20 is only to freeze a deterministic finite census and its replay contract. It does not infer an asymptotic law, exponent, survivor ratio, upper bound, lower bound, or causal mechanism.

## Exact enumerator

`stages/stage16/16-20/enumerate.py` enumerates the audited population as follows.

1. Generate every positive integer Pythagorean leg pair `(x,y)` by primitive Euclid parameters and a positive scale. Only pairs with face hypotenuse `h<=B` are needed because every Stage16 object satisfies `h<R<=B`.
2. For each such integral face, enumerate every positive third edge `z` satisfying `x^2+y^2+z^2<=B^2`.
3. Sort the three edges and retain only strict canonical triples `0<a<b<c` with `gcd(a,b,c)=1`.
4. Recompute all three face-square predicates and retain only triples with exact face multiplicity one.
5. Deduplicate by canonical triple and record `R^2=a^2+b^2+c^2` plus which canonical face (`ab`, `ac`, or `bc`) is integral.

### Coverage argument

Every Stage16 object has one and only one integral face. That face is an integer right triangle, so the standard primitive-Euclid-times-scale decomposition (`AR-002`) generates its two legs. Its face hypotenuse is strictly below `R`, hence lies below the census cutoff. The third-edge loop then visits the object's remaining edge. Canonicalization and the exact-one predicate are the already-audited Stage16-10 filters (`AR-001`). Thus the optimized enumerator covers the full finite Stage16 population at each listed cutoff.

## Independent replay check

The same script contains an independent small-cutoff reference path that scans canonical triples directly rather than starting from a Pythagorean face.

At `B=100` the optimized enumerator and the direct brute-force reference return exactly the same set of `2620` primitive canonical exactly-one-face triples.

The verifier also regenerates the complete frozen table through `B=2000` and requires byte-equivalent integer rows after parsing, including the identity

```text
M1 = face_ab + face_ac + face_bc
```

at every cutoff.

Replay command:

```bash
python stages/stage16/16-20/enumerate.py \
  --verify stages/stage16/16-20/counts.csv \
  --self-check-b 100
```

Expected terminal marker:

```text
STAGE16_20_VERIFY=PASS
```

## Frozen census

| B | M_1(B) | face `ab` | face `ac` | face `bc` |
|---:|---:|---:|---:|---:|
| 50 | 490 | 239 | 107 | 144 |
| 100 | 2,620 | 1,240 | 545 | 835 |
| 200 | 12,664 | 6,166 | 2,690 | 3,808 |
| 400 | 59,574 | 29,257 | 13,076 | 17,241 |
| 800 | 273,901 | 135,852 | 60,831 | 77,218 |
| 1200 | 662,207 | 329,077 | 148,905 | 184,225 |
| 1600 | 1,234,822 | 616,312 | 278,891 | 339,619 |
| 2000 | 1,997,863 | 999,707 | 453,195 | 544,961 |

Frozen CSV SHA-256:

```text
407d9e7a6ed2218e7897271b4de299d805a06ea6bf149aad09df92fb4dc5a347
```

The face columns are diagnostic labels after canonical edge ordering. Their unequal finite counts are **not** interpreted here as intrinsic arithmetic asymmetry; that would belong to a later audited analysis.

## Reuse / evidence ledger

```text
EVIDENCE_LEVEL=COMPUTED
PROVED_COMPONENT=exact finite-enumerator coverage under the audited Stage16-10 population contract
DEPENDS_ON=Stage16-10-audit,arsenal:AR-001,arsenal:AR-002
POPULATION_CONTRACT_CHANGED=NO
COMPARISON_ADAPTER_REQUIRED=NO
```

No Stage15 finite count is imported because historical Stage15 populations impose different face multiplicity and/or space-diagonal conditions. The finite census is generated directly on the Stage16 physical measure.

`AR-039` remains parked for Stage16-50 and is not charged by this checkpoint.

## Checkpoint decision

Stage16-20 introduces a new computed artifact and replay implementation. The main lane therefore stops before Stage16-30. A fresh `Stage16-audit` must certify the enumerator, frozen counts, replay coverage, and evidence boundary before any ratio/growth interpretation is attempted.

```text
MAIN_BATCH_STATUS=SUBMITTED
CURRENT_STAGE=Stage16
CURRENT_CHECKPOINT=20
CHECKPOINTS_ATTEMPTED=20
CHECKPOINTS_SUBMITTED=20
NEW_CLAIMS=deterministic finite census under the audited Stage16 population contract; no asymptotic claim
REUSED_WEAPONS=AR-001,AR-002
CODEX_REQUIRED=false
CODEX_REASON=The exact enumerator and replay verifier are small bounded deterministic artifacts implemented and cross-checked directly; no separate Codex delegation is needed.
AUDIT_REQUIRED=true
NEXT_EXPECTED_COMMAND=Stage16-audit
```
