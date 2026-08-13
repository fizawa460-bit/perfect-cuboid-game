# Stage16S-20 — finite-data baseline

Status: **SUBMITTED_FOR_FRESH_AUDIT**

## Purpose

Freeze a deterministic finite census for the audited Stage16S population contract before any asymptotic or causal interpretation is attempted.

The audited populations are:

```text
SPACE_AT_LEAST = primitive canonical 0<a<b<c, gcd(a,b,c)=1, R<=B, R integral
SPACE_ONLY     = SPACE_AT_LEAST with zero integral face diagonals
```

On every Stage16S object the positive space diagonal is `d=R`, so the finite census may equivalently be indexed by `d<=B`.

## Enumerator

`enumerate.py` uses an exact sum-of-two-squares join rather than a cubic scan. It indexes all pairs `a<b` by `a^2+b^2`, then for each integral `d<=B` and candidate `c<d` looks up pairs satisfying

\[
a^2+b^2=d^2-c^2.
\]

After enforcing `a<b<c` and `gcd(a,b,c)=1`, every surviving triple is classified by the exact number `0,1,2,3` of integral face diagonals. Completeness follows directly because every Stage16S object satisfies the displayed identity for its unique canonical `(a,b,c)` and its integral `d=R`.

## Frozen census

The canonical file is `counts.csv` with SHA-256

`0752d021b9df40c8035b10d1e8ed3cfd58a84086e64dca0ce0256492df63af2c`.

| B | SPACE_AT_LEAST | SPACE_ONLY | exactly 1 face | exactly 2 faces | exactly 3 faces |
|---:|---:|---:|---:|---:|---:|
| 50 | 76 | 69 | 7 | 0 | 0 |
| 100 | 324 | 299 | 25 | 0 | 0 |
| 200 | 1320 | 1253 | 67 | 0 | 0 |
| 400 | 5394 | 5220 | 174 | 0 | 0 |
| 800 | 21658 | 21204 | 453 | 1 | 0 |
| 1200 | 48921 | 48152 | 764 | 5 | 0 |
| 1600 | 87045 | 85963 | 1077 | 5 | 0 |
| 2000 | 136060 | 134621 | 1434 | 5 | 0 |

At each threshold,

```text
SPACE_AT_LEAST = SPACE_ONLY + face1 + face2 + face3.
```

At `B=2000`, `SPACE_ONLY/SPACE_AT_LEAST = 134621/136060 ≈ 0.98942`. This is a finite diagnostic only; no limiting density or asymptotic law is inferred here.

## Independent replay checks

The verifier embedded in `enumerate.py` performs three checks:

1. optimized enumeration equals a direct canonical-triple brute-force enumeration through `B=200`;
2. regeneration reproduces the full frozen `counts.csv` through `B=2000` exactly;
3. the `face1` column equals the already-audited Stage17-20 `N1` census at every shared threshold: `7,25,67,174,453,764,1077,1434`.

The third check is the finite-data form of the audited interface `Stage17 = Stage16 ∩ SPACE_AT_LEAST`; it is a regression check, not a new asymptotic theorem.

Local replay before submission returned:

```text
SMALL_CUTOFF_CROSSCHECK_B=200:PASS
FROZEN_CENSUS_MAX_B=2000:PASS
STAGE17_EXACT_ONE_INTERFACE=PASS
STAGE16S_20_VERIFY=PASS
```

## Evidence boundary

```text
EVIDENCE_LEVEL=COMPUTED
DEPENDS_ON=stages/stage16s/16s-10/audit.md,stages/stage17/17-20/counts.csv
POPULATION_CONTRACT_CHANGED=NO
COMPARISON_ADAPTER_REQUIRED=NO
FINITE_DATA_USED_AS_PROOF=NO
PARALLEL_LANE=YES
```

Checkpoint 20 makes no claim about the asymptotic order of either Stage16S count, a limiting `SPACE_ONLY/SPACE_AT_LEAST` density, causal strength of the space-diagonal condition, or independence from face conditions.

## Checkpoint decision

Checkpoint 20 is submitted for fresh audit. Checkpoint 30 would interpret the census through a ratio/thinning law, so the main lane stops here.

```text
MAIN_BATCH_STATUS=SUBMITTED
CURRENT_STAGE=Stage16S
CURRENT_CHECKPOINT=20
CHECKPOINTS_ATTEMPTED=20
CHECKPOINTS_SUBMITTED=20
NEW_CLAIMS=deterministic finite SPACE_AT_LEAST/SPACE_ONLY census through B=2000 with exact face-multiplicity split; no asymptotic claim
REUSED_WEAPONS=Stage16S-10,Stage17-20 finite interface
CODEX_REQUIRED=false
CODEX_REASON=The bounded sum-of-two-squares join, direct B<=200 cross-check, and frozen replay were implemented and independently verified directly; no separate Codex delegation is needed.
AUDIT_REQUIRED=true
NEXT_EXPECTED_COMMAND=Stage16S-audit
```
