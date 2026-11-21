# E28 — Problem W at slack (0, 0) for the bidegrees (7, 8) and (8, 8) (numerical, 2026-11-21)

Status: research note, **numerically verified, not exactly certified, not audited, zero credit**. STATE is not changed.
Continues E21, E22 and E24, same set-up and conventions.
Code: `slack0/degree8-20261120/` (research code; it uses `fastmono-20261119/` (mono_dir), `fast40-20261118/`
(bircheck40, hp_fast) and `speedup-20261118/`).

- Question (user, after E24): do degree 8, computing, cross-checking and improving the tools on the way. By E14
  Theorem A⁺ the row (6, 8) (|a − b| = 2) is closed, so the open bidegrees with max(a, b) = 8 are **(7, 8) and (8, 8)**.

## 1. Result

**Numerical proposition.** There is no k = 8, γ = 0 configuration with both slacks 0, |Ω| ≤ 4 and (p₁, p₂) birational
for (a, b) = (7, 8) or (8, 8). With E21, E22, E24 and E14 A⁺: **the mixed slack (0, 0) case has no solution with
max(a, b) ≤ 8** (numerically).

| (a, b) | queries / table covers | candidates (after window) | \|Ω\| ≤ 4 hits | birational | time (search5) |
|---|---|---|---|---|---|
| (7, 8) | 251,556 (degree 8) / 858,040 (degree 7) | 1.4·10⁵ | 0 | 0 | 0.25 core-hours |
| (8, 8) | 251,556 / 11,031,900 | 3.3·10⁶ (+ 2.3·10⁶ self part) | 1,020,276 (all composite) | 0 | ≈ 4.8 core-hours (2 h on 4 cores) |

- (7, 8): every candidate has |Ω| ≥ 28 (histogram {28: 6, 30: 6, 32: 80,317, 33: 206, 34: 113, 35: 8}).
  Consistent with the degrees: 7 is prime, so a hit at (7, 8) would always be birational (as (6, 7) in E24).
- (8, 8): the hits have |Ω| = 0 (1,020,144) or 4 (132). All are non-birational. 473 are called birational by the
  double-precision fibre test; the 40-digit recheck (bircheck40) finds 385 composite and 88 'unclear'. `bir100.py`
  redoes those 88 at 100 digits: **all 88 composite**, fibre distances ≤ 1.7·10⁻⁷⁴, and all points of f⁻¹(B) carried onto
  q⁻¹(B) (`logs/bir100_88.log`). The 'unclear' ones are covers that are ill-conditioned in double precision: the
  40-digit refinement from the double data stops near 10⁻²⁴, just above bircheck40's 10⁻²⁵ line.

## 2. The degree-8 list (918,925.25 weighted = the exact Hurwitz count)

| step | result |
|---|---|
| covers per profile (75 representatives) | `mono_dir_nb.py` (fastmono mono_dir with numba tracking `track_nb.py`, 5–10× faster) |
| 4∘2 composites f = g∘h | separate braid orbits, not reached by tracking or random seeds; built directly from the degree-4 covers (`make_comp.py`) and fed in with `--seedfile` |
| 60-digit build (`build5.py`) | symmetry images named by rule, every one confirmed by Möbius alignment (unconfirmed images are never merged); covers that slide to a degenerate map under Newton from doubles are restarted from 80-digit tracking (regen files) |
| count (`count8.py`) | 920,273 covers, weighted 918,925.25; **every one of the 75 profiles equals its Hurwitz number** (`hurwitz8.txt`) |
| distinctness (`distinct5.py`) | fibre j-invariant fingerprints over two base points: no two covers within 10⁻⁷ in any profile; smallest neighbour gap 2.7·10⁻³ (`logs/distinct5_all.txt`) |

Together, the Hurwitz counts and the distinctness check say the list is complete and has no duplicates (numerically).

Traps met and fixed on the way (details in the commit messages):
- About 9 % of the covers in the large profiles are ill-conditioned in double precision. Newton does not pass the
  1e-10 acceptance there, so tracking stalled. Fix: careful retries accept 1e-6, then 40-digit and 80-digit endgames.
- Covers with an automorphism are always 4∘2 composites; their seeds are finished by 80-digit Newton (double Newton
  stops near 10⁻⁸; this is ill-conditioning, not a singular point).
- One cover (113333 #5781) slid to a degenerate map; it is rebuilt from an 80-digit start.
- search5 itself had a rounding bug: folding the tier offset into the key lost entries at window edges (8 tiers:
  survivors 6,619 → 6,593 in a test). Fixed with exact lexsort ordering, before the production runs.

## 3. Speed (the heaviest stage)

- Cover generation: numba tracking (above). The (8, 8) table has 7.7·10⁸ key entries.
- Search: the first (8, 8) trial took 4,200 s for 2,000 queries on one code alone, so over a hundred hours in all.
  Two changes bring it to 1.74·10⁴ core-seconds: finer tiers (`TIERS`, `CELLW`, a tenth of the scan) and the
  pre-filter tolerance TOL = 10⁻⁹ → 10⁻¹¹, which is safe because the 60-digit points are exact in double precision.
  The largest window use by a true quadruple is 0.0086 of the window.
- Check: (7, 7) redone with search5 at TOL 10⁻⁹ and at TOL 10⁻¹¹ gives the same 90,546 hits, the same as E24.

## 4. Numerical margins

| (a, b) | 60-digit points: largest accepted | 60-digit points: smallest rejected | largest true-quadruple cross-ratio error |
|---|---|---|---|
| (7, 8) | 3.1·10⁻²¹ | 3.1·10⁻²⁰ | – |
| (8, 8) | 9.9·10⁻²¹ | 1.003·10⁻²⁰ | 1.0·10⁻¹⁰ (window ratio ≤ 8.6·10⁻³) |

- The (8, 8) gap at the 10⁻²⁰ line is thin: the ill-conditioned covers carry about 10⁻²⁰ accuracy at 60 digits. So
  search5 got a **margin check**: any candidate with |Ω| > 4 that has rejected distances below MIDTOL = 10⁻¹⁴, and
  whose one-to-one bound would drop to ≤ 4 if those counted as matches, is recorded. Both bidegrees were run again
  with it (and (7, 7) as a test): **0 such candidates** in every case, and the hit counts were reproduced exactly.
  So no hit can hide behind the 10⁻²⁰ line, as long as the 10⁻¹⁴ line holds.

## 5. What this is not
- Not exact (as E21 §4, E24 §4). Certification would need the 920,273 covers certified, certified non-coincidences
  and exact proofs of the composites.
- Closes only max(a, b) ≤ 8. Degree 9 would be larger again (about 10–15× by the trend 70,158 → 858,040 →
  11,012,925 weighted, all images).

## 6. Reproduction
```
# degree-8 covers: scripts/run1.sh <profile> (mono_dir_nb.py; composite seeds from make_comp.py), scripts/requeue.sh, scripts/fix_short2.sh
# 60-digit build + distinctness: scripts/builder3.sh (build5.py -> REGEN restart on exit 3 -> build5.py -> distinct5.py)
python3 count8.py <gen dir>                                            # Hurwitz count per profile
bash scripts/run78.sh                                                  # (7,8): search5.py 8 7 <deg8 dir> <deg7 dir>
bash scripts/run88.sh                                                  # (8,8): search5.py 8 8 <deg8 dir>
python3 bir100.py r88m.pkl 8 8 <deg8 dir>                               # 100-digit recheck of the 88 'unclear' flags
```
The scripts have this run's absolute paths. Pickles are not committed (size); the logs of the final runs are in `logs/`.
