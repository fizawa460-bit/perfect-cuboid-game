# Stage14-num6 — rolling exact observatory append through B=150,000,000

> STATUS: `STAGE14_NUM6=COMPLETE_ROLLING_EXACT_B150M_APPEND`
>
> CLASSIFICATION: exact finite census append + derived finite diagnostics + explicitly non-theorem heuristic anomaly gates.
>
> Historical B<=100m rows are append-only and reproduce the merged Stage14-num5 prefix exactly.

## 1. Exact B=150,000,000 census

The existing Stage14-num3 exact enumerator was run in 48 deterministic shared-hypotenuse residue chunks and independently aggregated by both the num3 merger and the num6 rolling-observatory layer.

```text
N_a^(2) = 859
N_b^(2) = 892
N_c^(2) = 462
N_2     = 2213
T       = 0

physical objects       = 2213
raw pair edges         = 2213
active oriented faces  = 3187
max graph degree       = 11
```

Exact ledger locks:

```text
object key         e4fdfc2172aa17cb376bee512d354436c1c5cf00a24f0d3649eaf2b3be3b7e41
object key + mask  02f7d8576f1d0c8b2abc6e8ea07afec340e0349f980a1ef56d427d8182b56438
active face        ddcd0e20d6ba913256a66493033b81987f381f792cf859afb18f7b9fe3d2b536
raw-pair edge      8500a753d0d159f79a5198a3b760a49931988f921983dbd7df69e09b70d7f1f8
```

The B=100m anchor reproduces all frozen num4/num3 hashes before any append is accepted. The independent num3 aggregate summary matches the num6 aggregate exactly.

## 2. Rolling finite diagnostics

The B=100m value was

```text
N2/sqrt(B) = 0.1875
latest 5-point effective alpha = 0.371872865972
```

At B=150m:

```text
N2/sqrt(B) = 0.180690693359306
change from B100m = -3.6316%
latest 5-point effective alpha = 0.433497153444
alpha shift from the B100m terminal window = +0.061624287472
```

The normalized count continues downward, but the newest rolling effective exponent turns upward strongly enough to cross the predeclared finite anomaly threshold. Therefore num6 emits a **material-change handoff** with reason `LATEST_ROLLING_ALPHA_SHIFT`. This is a finite/pre-asymptotic diagnostic, not evidence for a limiting exponent.

No other num6 material gate fired:

- no new graph max-degree increase (`max degree = 11`);
- new-shell direction deviations stay below 0.04;
- adjacent-shell local six-state TVD stays below 0.05 for every monitored prime;
- no all-three-face object appears (`T=0`).

## 3. Compact frozen source

The canonical 2,213-row B150m object ledger is stored as bzip2 + Base64 rather than as raw chunk output.

```text
CSV SHA-256   cbe49b52fa958344687c13664f8cfe7878a915402a1b013dcca665968f5d7442
bz2 SHA-256   d6a644f6901b76bff6a7d0599fbd12c17311cb955767ca0b860c47bb6123a3cd
Base64 SHA-256 a059975437b28a3153bcccef65f40414defefcc3e4a989b13960d70ce3c0d2cd
CSV bytes      78134
bz2 bytes      32555
```

After this source is committed, the num6 workflow switches from the one-time 48-chunk bootstrap to deterministic replay validation.

## 4. Handoff

```text
OBSERVATION_ID=stage14-num6-b150m-material-change
CUTOFF_RANGE=100000000<B<=150000000
EXACT_OR_HEURISTIC=EXACT + DERIVED_EXACT + FINITE_HEURISTIC_ONLY
OBJECT_COUNT=2213
AFFECTED_TRACKS=14-4 | 14-s | 14-t | 14-e
OBSERVATION=LATEST_ROLLING_ALPHA_SHIFT
THEOREM_CLAIM=false
```

The proof tracks may use this only as steering information. It does not promote a power-law, square-root law, directional limit, or perfect-cuboid existence/nonexistence statement.

## 5. Reproduction

Bootstrap Actions run: `31307391666`.

Canonical files:

```text
stages/stage14/scripts/14-num6/rolling_observatory.py
stages/stage14/data/14-num6/rolling_append_manifest.json
stages/stage14/data/14-num6/b150m_objects.csv.bz2.b64.parts/
.github/workflows/stage14-num6-rolling-b150m.yml
```

Exit lock:

```text
STAGE14_NUM6=COMPLETE_ROLLING_EXACT_B150M_APPEND
HISTORICAL_B100M_PREFIX_UNCHANGED=true
B150M_EXACT_CENSUS_FROZEN=true
APPEND_ONLY_HISTORY=true
MATERIAL_CHANGE_HANDOFF=true
PERFECT_CUBOID_EMERGENCY=false
FINITE_DIAGNOSTIC_ONLY=true
ASYMPTOTIC_CLAIM=false
PERFECT_CUBOID_EXISTENCE_CLAIM=false
PERFECT_CUBOID_NONEXISTENCE_CLAIM=false
NEXT=Stage14-num7 rolling observatory / next materially larger exact cutoff
```
