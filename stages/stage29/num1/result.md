# Stage29-num1 — primitive canonical Euler-cuboid finite census

Status: **COMPLETE through `B=10^9`**

Guards: `NUM_REUSE_PREFLIGHT=REQUIRED`; `FINITE_DATA_IS_NOT_ASYMPTOTIC_THEOREM=true`; `PERFECT_CUBOID_NONEXISTENCE_CLAIM=false`.

## Contract

`M3(B)` counts primitive canonical Euler cuboids with `a<=b<=c`, `gcd(a,b,c)=1`, all three face diagonals integral, and the physical Euclidean cutoff

`R^2=a^2+b^2+c^2 <= B^2`.

There is no integral-space-diagonal requirement in `M3`. A simultaneous integral space diagonal is recorded separately as finite `P(B)` evidence only.

## NUM_REUSE_PREFLIGHT

Reused/inspected before writing the new search:

- `stages/stage14/scripts/14-2/shared_leg_crosscheck.py`: complete Pythagorean shared-leg construction; its final space-diagonal filter is not part of M3.
- `stages/stage14/scripts/14-2/two_face_census.py`: exact Stage14 face tests and primitive/canonical conventions.
- `docs/stage14-num-reuse-index.{md,json}` and Stage14/Stage19 numerical records: comparison baseline only; they are not M3 generators.

The production M3 enumerator uses the unique odd edge of a primitive Euler cuboid. For fixed odd edge `a`, every Pythagorean even partner is generated exactly by a proper divisor `d<a` of `a^2` via `(a^2/d-d)/2`; pairs are then subjected to an exact third-face square test, primitive normalization, and exact `R<=B`. This is a complete enumeration route, not a selected parametrized family.

## Required regression

The repository enumerator and the independent exhaustive-table cross-check reproduce the locked values:

| B | M3(B) | P(B) |
|---:|---:|---:|
| 10,000 | 18 | 0 |
| 50,000 | 42 | 0 |
| 200,000 | 82 | 0 |
| 1,000,000 | 219 | 0 |

The extension CI run `32445467962` re-ran all four regression points and passed before the `10^9` production census.

## Exact checkpoints

| B | M3(B) | interval increment | P(B) |
|---:|---:|---:|---:|
| 1,000,000 | 219 | 137 from 2e5 | 0 |
| 5,000,000 | 480 | 261 | 0 |
| 10,000,000 | 656 | 176 | 0 |
| 50,000,000 | 1,298 | 642 | 0 |
| 100,000,000 | 1,757 | 459 | 0 |
| 200,000,000 | 2,339 | 582 | 0 |
| 500,000,000 | 3,331 | 992 | 0 |
| 1,000,000,000 | **4,362** | **1,031** | **0** |

The new `B=10^9` point is a direct complete-enumerator result, not an extrapolation from the 3556-record Resta/Helenius table.

## `10^9` production run

CI run `32445467962`, artifact `9433940026` (`stage29-num1-m3-1e9`), artifact ZIP SHA-256 `70273cda89d28d2701bf1da77ece739dbfdff36a79a800f895a09f9e726a040a`.

```text
algorithm=stage29-num1-odd-edge-divisor-v2
B=1000000000
M3=4362
perfect_cuboid_hits=0
tested_pairs=27325274840
candidate_even_edges=1488873445
odd_edges_with_two_candidates=165306456
sieve_sec=3.84271
runtime_sec=130.952
threads=4
```

Committed source: `stages/stage29/num1/scripts/m3_census.cpp`, algorithm version `stage29-num1-odd-edge-divisor-v2`, Git blob `e3332ae876046bcbf330a01d403d79e2a260a762`.

At `B=10^9`, `a^2<=10^18` remains inside `uint64_t`; the smallest prime factor needed by the odd-only SPF table is `<sqrt(10^9)<31623`, so the existing `uint16_t` SPF representation remains exact.

## Independent validation through `5*10^8`

The independent exhaustive-table pass validates all 3556 aligned F. Helenius / Giovanni Resta records from OEIS A031173/A031174/A031175 with exact integer face-diagonal, gcd, and Euclidean-cutoff checks. It remains an independent lock through `5*10^8`; it is not claimed to cover the new `10^9` endpoint.

Original frozen source hashes:

- A031173: `c667868f058d635b5156998bd748aafc1c03245764baa285fbe669adebb1a18b`
- A031174: `9d7cb2415d0c07cf1c1148913b1c5a124242344200a21811959e9a2466586650`
- A031175: `990832f168e3a3c9b1f09e15ef1b827d99ffee179121e2ed5d0b34ad817de190`

The extension CI also re-ran this cross-check successfully (artifact `9433939649`).

## N2 comparison correction

The earlier num1 ledger carried a provisional matched-cutoff `N2` series `5,8,10,15,17,18,27`. During the `10^9` extension this was checked against the frozen Stage19 population and found not to be the canonical Stage19 `N2` census: Stage19's audited interface records `N2(500,000,000)=3495` for primitive canonical exactly-two-face cuboids with integral space diagonal.

Therefore the provisional `N2` fields and `M3/N2` ratios are **withdrawn from the M3 ledger**. This does not alter any M3 count. A fresh matched-cutoff `N2` panel is deliberately deferred to the dedicated two-face-plus-space-diagonal numerical run, where the population adapter and cutoff will be re-locked explicitly.

```text
N2_PROVISIONAL_SERIES_RETRACTED=true
M3_COUNTS_AFFECTED=false
N2_RECOMPUTE_DEFERRED=true
```

## Interpretation boundary and reuse

No Euler cuboid in this exact finite census through `R<=10^9` has integral space diagonal, so `P(10^9)=0` as finite evidence. This is explicitly separate from any global nonexistence claim.

No asymptotic exponent is inferred from the finite counts. The numerical track remains separate from the Stage29 proof spine and is reusable by Stage29-08 parametrization coverage and later endpoint diagnostics. The machine-readable checkpoint is `stages/stage29/num1/data/m3_census_manifest.json`.
