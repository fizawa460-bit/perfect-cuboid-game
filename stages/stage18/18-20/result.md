# Stage18-20 — finite-data baseline

Status: **SUBMITTED_FOR_FRESH_AUDIT**

Stage18 counts primitive canonical `0<a<b<c`, `gcd(a,b,c)=1`, `R<=B`, with exactly two integral face diagonals and no integral-space-diagonal requirement.

## Enumerator

`enumerate.py` uses the unique shared edge of the two integral faces. It generates all Pythagorean leg adjacencies with face hypotenuse at most `B`, groups partner legs by shared edge, pairs two partners, then rechecks canonical strict ordering, global primitivity, `R<=B`, and exactly-two face multiplicity. Every Stage18 object has exactly one shared edge between its two integral faces, so this construction is complete after the explicit postfilters.

An independent direct canonical-triple brute-force enumerator is included for small-cutoff verification.

## Frozen census

Canonical file: `counts.csv`.

SHA-256:

`7873368267bbc21e5fd9ec6437d30e84a646ec4ddb14a50746575f59ac932e5a`

| B | M2 |
|---:|---:|
| 50 | 16 |
| 100 | 56 |
| 200 | 172 |
| 400 | 494 |
| 800 | 1347 |
| 1200 | 2350 |
| 1600 | 3536 |
| 2000 | 4812 |

Replay returned:

```text
SMALL_CUTOFF_CROSSCHECK_B=200:PASS
FROZEN_CENSUS_MAX_B=2000:PASS
STAGE18_20_VERIFY=PASS
```

The `B<=200` check is a set equality, not merely a count comparison.

## Evidence boundary

The frozen Stage15 theorem `M_2(B) ~ C_{M_2} B(log B)^5` is not used to manufacture or certify these finite counts. Conversely the finite table is `COMPUTED` evidence only and is not used to prove the Stage15 asymptotic.

Checkpoint20 makes no new asymptotic, ratio, causal, independence, or perfect-cuboid claim. Formal Stage16->Stage18 thinning remains Stage22.

```text
EVIDENCE_LEVEL=COMPUTED
POPULATION_CONTRACT_CHANGED=NO
FINITE_DATA_USED_AS_PROOF=NO
INDEPENDENT_SMALL_CUTOFF_CROSSCHECK=B<=200_SET_EQUALITY
AUDIT_REQUIRED=true
NEXT_CHECKPOINT_AFTER_PASS=30
CODEX_REQUIRED=false
CODEX_REASON=The exact shared-edge enumerator and independent brute-force replay were implemented and verified directly.
```