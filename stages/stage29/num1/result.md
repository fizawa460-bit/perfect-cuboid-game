# Stage29-num1 — primitive canonical Euler-cuboid finite census

Status: **COMPLETE for requested checkpoints through `B=5*10^8`**

Guards: `NUM_REUSE_PREFLIGHT=REQUIRED`; `FINITE_DATA_IS_NOT_ASYMPTOTIC_THEOREM=true`; `PERFECT_CUBOID_NONEXISTENCE_CLAIM=false`.

## Contract

`M3(B)` counts primitive canonical Euler cuboids with `a<=b<=c`, `gcd(a,b,c)=1`, all three face diagonals integral, and the physical Euclidean cutoff

`R^2=a^2+b^2+c^2 <= B^2`.

There is no integral-space-diagonal requirement in `M3`. A simultaneous integral space diagonal is recorded separately as finite `P(B)` evidence only.

## NUM_REUSE_PREFLIGHT

Reused/inspected before writing the new search:

- `stages/stage14/scripts/14-2/shared_leg_crosscheck.py`: complete Pythagorean shared-leg construction; its final space-diagonal filter is not part of M3.
- `stages/stage14/scripts/14-2/two_face_census.py`: exact Stage14 face tests and primitive/canonical conventions.
- `docs/stage14-num-reuse-index.{md,json}` and Stage14/Stage19 `N2` manifests: comparison baseline only. `N2` is drawn from the integral-space-diagonal population and is not an M3 generator.

The production M3 enumerator uses the unique odd edge of a primitive Euler cuboid. For fixed odd edge `a`, every Pythagorean even partner is generated exactly by a proper divisor `d<a` of `a^2` via `(a^2/d-d)/2`; pairs are then subjected to an exact third-face square test, primitive normalization, and exact `R<=B`. This is a complete enumeration route, not a selected parametrized family.

## Required regression

Both the repository enumerator and the independent exhaustive-table cross-check reproduce the locked values:

| B | M3(B) | P(B) |
|---:|---:|---:|
| 10,000 | 18 | 0 |
| 50,000 | 42 | 0 |
| 200,000 | 82 | 0 |
| 1,000,000 | 219 | 0 |

CI run `32444158502` re-ran the committed enumerator at all four points and passed.

## Exact requested checkpoints

| B | M3(B) | interval increment | P(B) | existing N2(B) |
|---:|---:|---:|---:|---:|
| 1,000,000 | 219 | 137 from 2e5 | 0 | 5 |
| 5,000,000 | 480 | 261 | 0 | 8 |
| 10,000,000 | 656 | 176 | 0 | 10 |
| 50,000,000 | 1,298 | 642 | 0 | 15 |
| 100,000,000 | 1,757 | 459 | 0 | 17 |
| 200,000,000 | 2,339 | 582 | 0 | 18 |
| 500,000,000 | **3,331** | **992** | **0** | 27 |

`M3/N2` is a finite matched-cutoff diagnostic only; it is not an asymptotic ratio and no exponent is fitted or inferred.

## Runtime and reproducibility

Committed source: `stages/stage29/num1/scripts/m3_census.cpp`, algorithm version `stage29-num1-odd-edge-divisor-v1`, Git blob `ce64df5be6c6abf3cf5356113dbfad5827f2b848`.

Pre-PR exact engineering runs of the same enumeration family recorded approximately 0.87 s at `5e6`, 1.94 s at `1e7`, 4.26 s at `5e7`, 9.95 s at `1e8`, and 22.45 s at `2e8` on the interactive host; cross-host performance is not inferred from these timings.

The independent exhaustive-table pass validated all 3556 aligned F. Helenius / Giovanni Resta records from OEIS A031173/A031174/A031175 with exact integer arithmetic and applied the repository `R<=B` cutoff. CI runtime for the single pass covering every checkpoint was 0.494 s. Source SHA-256 hashes and CI/artifact identifiers are frozen in `data/m3_census_manifest.json`.

Independent source hashes:

- A031173: `c667868f058d635b5156998bd748aafc1c03245764baa285fbe669adebb1a18b`
- A031174: `9d7cb2415d0c07cf1c1148913b1c5a124242344200a21811959e9a2466586650`
- A031175: `990832f168e3a3c9b1f09e15ef1b827d99ffee179121e2ed5d0b34ad817de190`

CI artifact: `stage29-num1-resta-crosscheck`, run `32444158502`, artifact `9433468039`.

## Interpretation boundary and reuse

No Euler cuboid in this finite census through `R<=5*10^8` has integral space diagonal, so `P(5*10^8)=0` as finite evidence. This is explicitly separate from any global nonexistence claim.

No asymptotic exponent is inferred from the finite fits/counts. The numerical track remains separate from the Stage29 proof spine and is reusable by Stage29-08 parametrization coverage and later endpoint diagnostics. The machine-readable checkpoint is `stages/stage29/num1/data/m3_census_manifest.json`.
