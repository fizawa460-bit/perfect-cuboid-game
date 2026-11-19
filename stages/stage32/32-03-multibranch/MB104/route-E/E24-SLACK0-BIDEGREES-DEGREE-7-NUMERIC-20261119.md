# E24 — Problem W at slack (0, 0) for the bidegrees (6, 7) and (7, 7) (numerical, 2026-11-19)

Status: research note, **numerically verified, not exactly certified, not audited, zero credit**. STATE is not changed.
Continues E21 and E22, same set-up and conventions.
Code: `slack0/degree7-20261119/` (research code; it uses `speedup-20261118/` (PR #1881), `fast40-20261118/` (PR #1885,
search4 of PR #1889) and `fastmono-20261119/` (PR #1886, #1888)).

- Question (user, after E22): do degree 7 with the tools of PR #1881. By E14 Theorem A⁺ the row (5, 7) (|a − b| = 2)
  is closed, so the open bidegrees with max(a, b) = 7 are **(6, 7) and (7, 7)**.

## 1. Result

**Numerical proposition.** There is no k = 8, γ = 0 configuration with both slacks 0, |Ω| ≤ 4 and (p₁, p₂) birational
for (a, b) = (6, 7) or (7, 7). With E21, E22 and E14 A⁺: **the mixed slack (0, 0) case has no solution with
max(a, b) ≤ 7** (numerically).

| (a, b) | query covers / table covers | candidates | \|Ω\| ≤ 4 hits | birational | time (search4) |
|---|---|---|---|---|---|
| (6, 7) | 7,148 / 858,040 | 6.9·10⁶ | 0 | 0 | 0.3 core-hours |
| (7, 7) | 118,568 / 858,040 | 1.28·10⁸ | 475,421 (all composite) | 0 | ≈ 4.1 core-hours |

- (6, 7): every candidate has |Ω| ≥ 28 or a lower bound > 4. (Consistent with FAST40: a hit at (6, 7) is always
  birational because 7 is prime, so there are none.)
- (7, 7): all hits have |Ω| = 0 or 4. **2,075** hits are called birational by the double-precision fibre test; the
  automatic 40-digit recheck (bircheck40) finds 2,073 composite (every fibre of f carries a second point with the same
  value of q∘M, distance ≤ 7·10⁻²⁶ < 10⁻²⁵) and 2 'unclear' (the pair f = 5342, rep 51522 with U = 2, 3; the fibre
  distances were 2·10⁻²⁶ to 2·10⁻²⁵, just above the 10⁻²⁵ line). `birhi.py` redoes them at 100 digits (refinement at
  100 digits): **composite**, fibre distances ≤ 2.6·10⁻⁸⁵ and all 30 points of f⁻¹(B) carried onto q⁻¹(B).
  Since 7 is prime, a non-birational pair of degree-7 covers is q∘M = V∘f, as found.

## 2. The degree-7 list (858,040 = the exact Hurwitz number)

| step | result |
|---|---|
| covers per profile (21 representatives) | 13 profiles from `mono_p.py` (speedup mono.py with checkpoints and error handling), 8 from `fastmono` (mono_dir) |
| 60-digit build (`fast40/build_all.py`, DPS = 60) | 115,938 representatives, worst residual 3·10⁻⁴⁶ |
| covers failing `analyse` in double precision (nearly colliding points) | 408 from `extra_7_*.pkl` (fastmono) and 8 hard covers of 1,1,2,2,3,3 (`rejchk3.py`, `hardclose.py`); refined separately at 60 digits (`extras40.py`, worst residual 9·10⁻⁵¹, smallest point distance 5.9·10⁻⁸) |
| 2,2,2,2,2,2 | build_all regenerates the 2,221 covers missing from the cov file as Aut(B) images, with 24 invariant duplicates; removed exactly by `fastmono/exact_dedupe.py` (66,640 classes = the run's tuple list) |
| merge (`merge7.py`) | 118,568 representatives (weighted 118,568), 858,040 covers (one image per coset of Stab(t)); **every one of the 21 profiles equals its Hurwitz number** (`count.py`, `countall.py`) |

- One extra entry was **spurious**: extra #21 of 1,1,2,3,2,3 drifts under refinement to a degenerate solution
  (smallest critical-point distance 1.7·10⁻⁶ → 4.9·10⁻⁹ at 40 digits → 3·10⁻²¹ at 80 digits, residual stuck at
  10⁻¹⁷, 10⁻²⁹; `driftall.py` checked all 408 extras, only this one drifts). Its tuple is genuine: by the fastmono
  symmetry rules it is the Aut(B) image of the regular covers 1537 and 1541 of the same profile. `merge7.py` takes the
  image of 1541 instead and confirms its tuple by 40-digit numbering (`md_hp.py`).
- Accuracy of the stored points (`ptacc.py`: refinement again at 100 digits, Möbius-aligned): ≤ 1.1·10⁻⁵⁴ on a sample
  of 260 representatives, ≤ 3.5·10⁻⁴⁶ on all 409 extra representatives.
- Degree 6 for (6, 7): rebuilt in the same format (`build_all.py 6`, DPS = 60): 7,148 / 71,508 covers, weighted
  70,158 = the Hurwitz number, residual 2·10⁻⁵³. One cover failed `analyse` until the critical points of the
  generated rej_6 files were polished by Newton at 40 digits (`polish_rej.py`, largest move 1.8·10⁻⁷).

## 3. Numerical margins

| (a, b) | double: largest accepted | 60-digit points: largest accepted | 60-digit points: smallest rejected | largest true-quadruple cross-ratio error |
|---|---|---|---|---|
| (6, 7) | – | 2.3·10⁻⁴⁹ | 1.8·10⁻¹⁵ | – |
| (7, 7) | 9.96·10⁻¹² | 8.8·10⁻²¹ | 8.6·10⁻¹⁹ | 8.4·10⁻¹¹ (window ratio ≤ 2.8·10⁻⁵) |

- The (7, 7) 60-digit gap is thin (accepted 8.8·10⁻²¹ just below the 10⁻²⁰ line). The stored points are accurate to
  ≤ 10⁻⁴⁶, so these values are geometric near-coincidences, not rounding. To make sure that no rejected pair could
  hide a hit, all four shards were run again recording every 60-digit distance in (10⁻³², 10⁻¹⁴)
  (`search4_mid.py`, `midcheck.py`): only 16 values lie in (10⁻²⁵, 10⁻²⁰), none in [10⁻²⁰, 10⁻¹⁹), and **even if every
  rejected pair in that range were accepted, the candidate would still have |Ω| ≥ 20**. The rerun reproduced the
  hit counts exactly.
- Memory: JOBS = 4 on a 15 GB machine lost two workers to the memory limit (each grows to ~10 GB); those shards were
  rerun one process at a time (`logs/s4_77_sh1.log`, `sh2`).

## 4. What this is not
- Not exact (as E21 §4, E22 §5). Certification would need the 858,040 covers certified, certified non-coincidences
  and exact proofs of the composites.
- Closes only max(a, b) ≤ 7. Degree 8 (Hurwitz number 11,012,925 weighted) is about 13 times larger again.

## 5. Reproduction
```
# covers (13 profiles): mono_p.py 7 t1..t6 maxloops seed  (+ rejchk3.py, hardclose.py for 1,1,2,2,3,3)
# covers (8 profiles): fastmono-20261119 (mono_dir.py), files cov/rej/full/extra_7_*.pkl
DPS=60 python3 ../fast40-20261118/build_all.py 7 2                    # -> all_7.pkl (renamed all_7_buildall.pkl)
SKIP=112323:21 XDPS=60 IT=60 python3 extras40.py extras_all.pkl extra_7_*.pkl hard:112233:rejhp_112233.pkl:hardall_112233.pkl
python3 merge7.py                                                     # -> all_7m.pkl (used as all_7.pkl)
python3 polish_rej.py; DPS=60 python3 ../fast40-20261118/build_all.py 6 2      # degree 6, in its own folder
JOBS=4 python3 ../fast40-20261118/search4.py 7 7 2.5e-6 - 0 1
JOBS=4 python3 ../fast40-20261118/search4.py 6 7 2.5e-6 - 0 1 dir6 dir7
python3 birhi.py res4_7_7_2of4.pkl                                    # 100-digit recheck of the 2 unclear flags
python3 search4_mid.py 7 7 2.5e-6 - k 4 (from fast40-20261118); python3 midcheck.py mid_7_7_*of4.pkl  # margin check
```
Pickles are not committed (size); the logs of the final runs are in `logs/`.
