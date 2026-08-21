# Stage29-num1 — primitive canonical Euler-cuboid finite census

Status: **ACTIVE / exact finite numerical track**

Guards:

- `NUM_REUSE_PREFLIGHT=REQUIRED`
- `FINITE_DATA_IS_NOT_ASYMPTOTIC_THEOREM=true`
- `PERFECT_CUBOID_NONEXISTENCE_CLAIM=false`

## Contract

`M3(B)` counts primitive canonical Euler cuboids with `a<=b<=c`, `gcd(a,b,c)=1`, all three face diagonals integral, and physical Euclidean cutoff

`R^2 = a^2+b^2+c^2 <= B^2`.

There is **no** integral-space-diagonal requirement in `M3`.  A simultaneous integral space diagonal is recorded separately as finite `P(B)` evidence only.

## NUM_REUSE_PREFLIGHT

Reused/inspected before writing the new search:

- `stages/stage14/scripts/14-2/shared_leg_crosscheck.py`: complete Pythagorean shared-leg construction; its final space-diagonal filter is not part of M3.
- `stages/stage14/scripts/14-2/two_face_census.py`: exact Stage14 face tests and primitive/canonical conventions.
- `docs/stage14-num-reuse-index.{md,json}` and Stage14/Stage19 `N2` manifests: comparison baseline only.  `N2` is drawn from the integral-space-diagonal population and therefore is **not** an M3 generator.

The production M3 enumerator uses the unique odd edge of a primitive Euler cuboid.  For fixed odd edge `a`, every Pythagorean even partner is generated exactly by a proper divisor `d<a` of `a^2` via `(a^2/d-d)/2`; pairs are then subjected to an exact third-face square test, primitive normalization, and exact `R<=B`.  This covers all primitive Euler cuboids rather than any selected parametrized family.

## Required regression

Independent local pre-PR runs matched all four locked values exactly:

| B | required M3(B) | observed | P(B) |
|---:|---:|---:|---:|
| 10,000 | 18 | 18 | 0 |
| 50,000 | 42 | 42 | 0 |
| 200,000 | 82 | 82 | 0 |
| 1,000,000 | 219 | 219 | 0 |

## Main checkpoints — repository enumerator

These are exact integer runs of the same complete odd-edge/divisor enumeration family.  The checked-in CI re-runs the locked regression from the committed source.

| B | M3(B) | interval increment | P(B) | local runtime note |
|---:|---:|---:|---:|---:|
| 1,000,000 | 219 | — | 0 | regression |
| 5,000,000 | 480 | 261 | 0 | 0.87 s prototype |
| 10,000,000 | 656 | 176 | 0 | 1.94 s prototype |
| 50,000,000 | 1,298 | 642 | 0 | 4.26 s, 5-thread optimized |
| 100,000,000 | 1,757 | 459 | 0 | 9.95 s, 5-thread optimized |
| 200,000,000 | 2,339 | 582 | 0 | 22.45 s, 5-thread optimized |
| 500,000,000 | pending independent exhaustive-table CI checkpoint | pending | pending | direct prototype exceeded the interactive run budget |

Runtime values above are engineering notes from the pre-PR execution host, not cross-host benchmarks.  Formal reproducibility metadata is emitted by the committed scripts/CI.

## Independent exhaustive-table cross-check

`resta_crosscheck.py` downloads the aligned OEIS A031173/A031174/A031175 tables attributed to F. Helenius / Giovanni Resta, validates every listed primitive Euler brick with exact integer arithmetic, records source SHA-256 hashes, then applies the repository's Euclidean `R<=B` cutoff.  The published table covers primitive bricks with longest edge `<5*10^8`; every positive cuboid satisfying `R<=5*10^8` has longest edge `<5*10^8`, so this is an independent complete finite cross-check for every requested checkpoint through `5*10^8`.

The CI artifact `stage29-num1-resta-crosscheck` is the machine-readable cross-check manifest.

## Matched-cutoff Stage14/Stage19 N2 diagnostic

`N2` is retained only as a finite matched-cutoff diagnostic and must not be interpreted as the M3 population or as an asymptotic ratio.

| B | M3(B) | existing N2(B) |
|---:|---:|---:|
| 1,000,000 | 219 | 5 |
| 5,000,000 | 480 | 8 |
| 10,000,000 | 656 | 10 |
| 50,000,000 | 1,298 | 15 |
| 100,000,000 | 1,757 | 17 |
| 200,000,000 | 2,339 | 18 |
| 500,000,000 | pending | 27 |

No asymptotic exponent is fitted or inferred from these finite counts.  `P(B)=0` at completed checkpoints is finite search evidence only and is explicitly separate from any global perfect-cuboid nonexistence claim.

## Reuse target

This track is intentionally separate from the Stage29 proof spine.  Its manifests/counts are intended as input to Stage29-08 parametrization coverage and later endpoint diagnostics without changing theorem status.
