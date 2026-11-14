# F-02 — slack-0 mismatch spectrum up to degree 4 (measured, 2026-11-13)

Status: **floating-point measurement, with a high-precision recheck of the borderline cases. Not a theorem.**
Zero credit. Setting as in F-01 (route-E E10 §2 / E11; k = 8, γ = 0, s₁ = s₂ = 0).

## 1. Degree-4 slack-0 maps

| item | value | file |
|---|---|---|
| branch data (fibre types 1111 / 211 / 22 over the six points of B) | 141 | `hurwitz4.py`, `hurwitz4.json` |
| isomorphism classes (S₄ tuples up to conjugation) | 680 (|Aut| = 1: 480, 2: 180, 4: 20) | `hurwitz4.json` |
| maps built | 680, every datum at its target | `build_maps.py`, `fill_orbits.py`, `maps4.json` |

- **Construction.** `build_maps.py` uses Newton's method on a square system: the coefficients of P and Q, plus the
  critical points beyond 0, ∞ and 1. Each map is then refined in mpmath (dps 45).
- **Checks on each map.** The resultant is nonzero. The Wronskian has degree 2n − 3. The critical points are distinct.
- **Duplicates.** Maps are deduplicated exactly, up to Möbius maps of the source.
- **Missing maps.** The last missing map came from closing the list under the 24 Möbius maps that permute B, together
  with complex conjugation (`fill_orbits.py`).
- **Accuracy.** Every critical value lies within 10⁻²⁰ of B.
- **Degree-3 control.** The same code rebuilds the 60 degree-3 maps (`maps3.json`).

## 2. Method

`f02_spectrum.py` measures the same quantities as F-01.

- **Which T are enumerated.** Only Möbius maps T with at least 4 coincidences.
  - They are found by matching cross-ratios. Each target quadruple goes into a KD-tree in chordal coordinates
    (RAD = 10⁻⁷).
  - A T with at most 3 coincidences has |Ω| ≥ |O₁| + |O₂| − 6, which is the bound reported for the rest.
- **Birationality degree.** This is the number of points in a generic fibre of p₁ that have the same p₂-value. It is
  tested at two points.
  - It is tested only for ω ≤ cut, and it is automatic when gcd(a,b) = 1.
  - The cut for (4,4) was lowered from 18 to 13 after ω = 12 had been found.
  - Every T with ω ≤ 13 is still enumerated and tested. Above the cut, only the ω histogram is kept.
- **Parallel and resumable.** The q maps are split into chunks on a process pool. Each finished chunk is appended to
  `spec{a}x{b}{v}.jsonl`, so a restart resumes where the run stopped.
- **Cross-checks** (`f02_par_check.out`, PASS):
  - (1,2), (2,2), (2,3) and (3,3) reproduce F-01.
  - The parallel (2,4) and (3,4) reproduce the serial run (`f02_serial_2x4_3x4.out`) exactly.

### 2.1 Precision problem at (4,4), and its resolution

The double-precision run of (4,4) failed the separation test (`f02_4x4.out`):
- accepted coincidences reached 9.98·10⁻⁹;
- rejected distances went down to 1.003·10⁻⁸;
- so there was no gap around TOL = 10⁻⁸.

The run therefore records every T with any cross value in [10⁻¹², 10⁻⁶] (`amb4x4.json`): 634,964 borderline T.

`recheck_amb.py` rebuilds each borderline T in mpmath (dps 50). It uses O-sets computed in mpmath, in the same point
order as the floating-point ones (checked). It then counts coincidences exactly.

| result of the recheck | value |
|---|---|
| largest exact coincidence | 1.3·10⁻³² |
| smallest exact non-coincidence | 4.0·10⁻¹¹ (PASS: > 10⁻¹²) |
| borderline T whose (ω, j, h) changed | 129,141 |
| … of which ω went **down** | **0** |
| … of which the new ω is ≤ 13 | 0 |
| … of which the float ω was ≤ 13 | 2,668: all (12; 6, 0) → (16; 4, 0) or (18; 3, 0), all counted birational in the float run |

`count_false12.py` recomputes these 2,668 T as the run did, and confirms that all of them were counted as birational
at ω = 12.

- **Cause.** The float run accepted false coincidences: T is built from three points, and when that is poorly
  conditioned, nearby non-coincident points come out at about 10⁻⁸.
- **Effect.** No coincidence was missed. Every correction raises ω.
- **Corrected (4,4) count.** Birational ω = 12: 13,804 − 2,668 = **11,136** = 96 · 116.
- **Unchanged.** The non-birational counts at ω ≤ 13 do not change.
- **Approximate.** The histogram above the cut is approximate, because some borderline T move upward.
- **Other bidegrees.** (2,4) and (3,4) had a clean gap:
  - accepted ≤ 7.7·10⁻¹⁴;
  - rejected ≥ 1.5·10⁻⁴.

## 3. Result

Rows (1,1) to (3,3) are from F-01.

| (a,b) | \|O₁\|+\|O₂\| | ω_min (birational) | (j, h) at the minimum | max 2j+h (birational) | # extremal T | F-01 fit |
|---|---|---|---|---|---|---|
| (1,2) | 14 | 6 | (4,0) | 8 | 96 | 6 |
| (1,3) | 16 | 8 | (4,0) | 8 | 96 | 8 |
| (2,2) | 16 | 6 | (4,2) | 10 | 192 | 6 |
| (2,3) | 18 | 10 | (4,0) | 8 | 1,152 | 10 |
| (3,3) | 20 | 10 | (4,2), (5,0) | 10 | 384 | 10 |
| **(2,4)** | 20 | **12** | (4,0) | 8 | 15,744 = 96·164 | 12 ✓ |
| **(3,4)** | 22 | **14** | (4,0) | 8 | 16,896 = 96·176 | 14 ✓ |
| **(4,4)** | 24 | **12** | (6,0) | **12** | 11,136 = 96·116 (corrected) | 14 ✗ |

Below ω_min, at (4,4), there are non-birational T with ω = 0, 4, 6, 8, 10 (bidegree (2,2) or (1,1) onto the image).
At (2,4) the non-birational ω = 12 is the same value as ω_min.

Files: `f02_serial_2x4_3x4.out`, `f02_4x4.out`, `recheck4x4.out`.

## 4. Reading

1. **Problem W is not met anywhere up to degree 4.**
   - No birational slack-0 pair has |Ω| ≤ 4 for a, b ≤ 4.
   - In measurement terms, this is G2 with N = 4. Exact certification is a separate task, as in E11 §9.
2. **The off-diagonal fit holds.**
   - ω_min = 2(a+b) for a ≠ b at all six off-diagonal points.
   - The maximum of 2j + h there stays at 8.
3. **The diagonal fit fails at (4,4).**
   - The fit predicted 14; the measured value is 12.
   - On the diagonal the maximum coincidence count grows:
     - j at the minimum is 4, 5, 6 at (2,2) → (3,3) → (4,4);
     - the maximum of 2j + h is 10, 10, 12.
   - ω_min on the diagonal is 6, 10, 12. It still grows, but by 2 instead of 4 in the last step.
   - The extremal (4,4) configuration is pure label-agreeing: (j, h) = (6, 0).
4. **What this means for the T0 shape.**
   - So far M_max(a,b) = 8 off the diagonal. On the diagonal it is 10, 10, 12 at a + b = 4, 6, 8.
   - That is a slope of 0, then 1 in a + b. Three points are not enough to tell a slope of 1/2 from a slope of 1.
   - T0 needs c₀ < 1. The diagonal is therefore the critical case: a slope of 1 would be exactly the borderline value.
   - [Estimate: pattern only.]
5. **Multiples of 96 continue.**
   - Every extremal count from (1,2) to (4,4) is a multiple of 96.
   - The symmetry group of (P¹, B), including conjugation, has order 48, which divides 96.
   - This supports the heuristic that extremal coincidences come from symmetries of B [heuristic, not checked].

## 5. Structure of the extremal pairs

See `F02-SHAPE.md`. At (4,4), all 11,136 configurations with M = 12 come from a shared degree-2 left factor or a
symmetry of B. Unstructured pairs reach M = 10 at (3,3) and (4,4).

## 6. Next

- **Theory request.** Ask the upper model why the coincidence count is bounded off the diagonal and grows on the
  diagonal. The question is whether the extremal (6,0) configurations at (4,4) come from a structural source, such as
  a common symmetry of B or a shared sub-cover.
- **Diagonal data.** (5,5) would need the degree-5 maps; that is a separate construction, of size to be estimated.
  - The cheaper step is to inspect the 11,136 extremal (4,4) configurations directly.
- **Rule for future runs.** Every T with ω ≤ cut should also be rechecked in high precision, not only the borderline
  ones. The float run is only a filter.
