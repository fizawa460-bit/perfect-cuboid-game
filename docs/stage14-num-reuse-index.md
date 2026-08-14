# Stage14 numerical observatory reuse index

`STATUS=ACTIVE_REUSE_INTERFACE`

This index promotes the completed Stage14-num work from archived chronology to a reusable finite-evidence interface. It does not promote finite observations to asymptotic theorems. Every consumer must match population, cutoff, canonicalization, face multiplicity, and space-diagonal requirements before reuse.

## Frozen population contract

The principal census is the primitive canonical integral-space-diagonal population
\[
0<a<b<c,\qquad \gcd(a,b,c)=1,\qquad d^2=a^2+b^2+c^2,\qquad d\le B,
\]
with at least two integral face diagonals. Records retain the exact face mask, so exactly-two objects and triple-face objects remain distinguishable. This is the Stage14 `A_2`-side population, not the ambient Stage15/18 `M_2` population.

## Reusable asset classes

| ID | Asset | Evidence | Canonical source | Valid direct consumers |
|---|---|---|---|---|
| NUM-R01 | Exact census oracle through `B=500,000,000`, nested locks, `T=0` within the finite cutoff | `EXACT_FINITE_CENSUS` | `14-num-alpha11/result.md`; `data/14-num-alpha11/b500m_manifest.json` | Stage19/20 finite regression after exact population adapter; Stage24/26/28 numerator diagnostics |
| NUM-R02 | Independent enumerator equality and canonical SHA locks | `EXACT_REGRESSION_ORACLE` | `14-num1`, `14-num3`, `14-num-alpha4`, `14-num-alpha6` | Any later two-face integral-space enumerator; CI/regression validation |
| NUM-R03 | Accelerated safe diagonal-first enumeration kernel | `PROVED_ALGORITHM + EXACT_REGRESSION` | `14-num-alpha1` through `14-num-alpha8` | Larger finite censuses; independent replay; candidate verification |
| NUM-R04 | Unified object/face/edge fingerprint ledger | `DERIVED_EXACT` | `14-num4/result.md` | Graph, multiplicity, family and local-state diagnostics |
| NUM-R05 | Moving-window scaling and direction diagnostics | `FINITE_DIAGNOSTIC_ONLY` | `14-num5`, `14-num6`, `14-num-alpha9`–`alpha11` | Hypothesis generation and pre-asymptotic warning only |
| NUM-R06 | Matched Stage13 one-face to Stage14 two-face comparison | `DERIVED_EXACT_FINITE` | `14-num-alpha11-diag6`–`diag9` | Stage22, Stage24, Stage25 and Stage28 causal diagnostics |
| NUM-R07 | Conditional second-face survival panel through `B=1,000,000` | `EXACT_FINITE_PANEL` | `14-num-alpha11-diag7`–`diag11` | Stage22 transition diagnostics; source-versus-survival decomposition |
| NUM-R08 | Local/congruence and cluster controls, including the finite-field `p=7` fact | `MIXED_EXACT_LOCAL_AND_FINITE_DIAGNOSTIC` | `14-num-alpha11-diag4`, `diag5`, `diag10` | Local-obstruction tests and anti-overinterpretation checks |

All abbreviated task sources above live under `stages/stage14/archive/tasks/`; data sources live under `stages/stage14/data/`.

## Stage16–28 routing

| Stage | Reuse decision | Assets | Required adapter |
|---|---|---|---|
| 16 / 17 | Optional historical cross-check only | NUM-R06, NUM-R07 | Their primary populations were settled independently; do not replace proofs |
| 18 | Use as negative-control and enumerator regression | NUM-R02, NUM-R06 | Stage18 lacks the integral-space condition; compare only matched intersections or shared small-cutoff records |
| 19 | Primary finite regression oracle | NUM-R01, NUM-R02, NUM-R03 | Verify Stage19 face multiplicity and cutoff equal the selected Stage14 mask |
| 20 | Candidate/triple emergency oracle | NUM-R01, NUM-R03 | `T=0` is finite only; never infer global nonexistence |
| 21 | Auxiliary diagnostic | NUM-R06, NUM-R07 | Combine only with audited Stage16S and matched cutoff |
| 22 | Primary causal diagnostic | NUM-R06, NUM-R07, NUM-R08 | Match one-face source convention and distinguish object counts from oriented-face counts |
| 23–25 | Intersection diagnostics | NUM-R01, NUM-R06, NUM-R07 | Build exact set/intersection adapter before ratio comparison |
| 26–27 | Third-face finite regression | NUM-R01, NUM-R03, NUM-R08 | Preserve exactly-two versus triple masks |
| 28 | Synthesis evidence panel | NUM-R04–NUM-R08 | Label every statement exact finite, derived exact, or heuristic |

## Consumer protocol

Before new computation, every Stage16–28 main batch must inspect this index and emit:

```text
NUM_REUSE_CHECK=PASS
NUM_ASSETS_REUSED=<IDs or NONE>
NUM_POPULATION_MATCH=<EXACT | ADAPTER_PROVED | NO_MATCH>
NUM_EVIDENCE_LEVEL=<level or NOT_APPLICABLE>
NUM_NEW_COMPUTATION_JUSTIFIED=<reason or NOT_REQUIRED>
```

`DIRECT_REUSE` is allowed only for the same primitive/canonical population, height cutoff, face mask, and counting measure. `ADAPTER_PROVED` must name the exact set map or intersection. `NO_MATCH` may still use an asset as a negative control or software regression, never as mathematical evidence for the target population.

## Nonclaims

- `T=0` through a finite cutoff is not perfect-cuboid nonexistence.
- Directional proportions and effective exponents are not limiting laws.
- The Stage14 integral-space census is not the Stage15/18 ambient exactly-two population.
- A SHA/count match validates implementation and population transcription; it does not prove an asymptotic theorem.

Machine-readable companion: `docs/stage14-num-reuse-index.json`.
