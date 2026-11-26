# E29 — Problem W at slack (0, 0) for the bidegrees (8, 9) and (9, 9) (numerical, 2026-11-26)

Status: research note, **numerically verified, not exactly certified, not audited, zero credit**. STATE is not changed.
Continues E21, E22, E24 and E28, same set-up and conventions.
Code: `slack0/degree9-20261121/` (research code; it uses `fastmono-20261119/`, `fast40-20261118/` (bircheck40,
hp_fast), `speedup-20261118/` and `degree8-20261120/`). Logs of the final runs: `slack0/degree9-20261121/logs/`.

- Question (user, after E28): do degree 9 as well. By E14 Theorem A⁺ the row (7, 9) (|a − b| = 2) is closed, so the
  open bidegrees with max(a, b) = 9 are **(8, 9) and (9, 9)**.
- The work ran on five cloud machines in parallel (four "share" threads plus this one), each in 2-hour pieces that
  resume from saved results.

## 1. Result

**Numerical proposition.** There is no k = 8, γ = 0 configuration with both slacks 0, |Ω| ≤ 4 and (p₁, p₂) birational
for (a, b) = (8, 9) or (9, 9). With E21, E22, E24, E28 and E14 A⁺: **the mixed slack (0, 0) case has no solution with
max(a, b) ≤ 9** (numerically).

| (a, b) | queries / table | \|Ω\| ≤ 4 hits | birational | core time |
|---|---|---|---|---|
| (8, 9) | 3,478,040 degree-9 orbit representatives / all degree-8 covers (E28 list, rebuilt) | 0 | 0 | 91 core-hours |
| (9, 9), pairs inside an Aut(B) class (f, U∘f) | 3,478,040 | 13,942,458 (all composite) | 0 | 17 core-hours |
| (9, 9), all other pairs | 3,478,040 / 12.0·10⁶ degree-9 covers | 1,084 after the 60-digit stage (all composite) | 0 | ≈ 400 core-hours |

- Every (9, 9) hit has |Ω| = 0 and is a composite: the pair factors through a common map (for (f, U∘f), through f
  itself). 9 = 3·3, so composites through degree-3 maps are expected, unlike the prime degree 7.
- (8, 9): 0 hits in every one of the nine runs (`logs/q98/*/s98.log`); gcd(8, 9) = 1, so any hit would have been
  birational.

## 2. The degree-9 list (11,987,122 weighted = the exact Hurwitz count)

| step | result |
|---|---|
| covers per profile (50 profiles, `hurwitz9.txt`) | `mono_par.py` (mono_dir on 4 cores, numba tracking), one profile split over machines when large (`split9.sh`, `merge9.py`: ownership by symmetry-orbit hash, no overlap) |
| stage 2 (covers that double tracking misses) | 40-digit endgame (`HPENDGAME=1`), then 80-digit finishing (`finish80`); Newton polish of the starting point before the 40/80-digit tracking |
| covers in separate braid orbits | AGL(2,3)-type primitive covers (0,3,3,3,3,4: 24, 0,4,3,3,3,3: 24) reached by `seedhunt.py` and `swapseed.py`; 3∘3 composites from `make_comp9.py` |
| 60-digit build (`build7.py`) | one refined cover per symmetry orbit, the others as exact images; orphans (an orbit where no member refines, e.g. a critical-point gap of 3·10⁻⁹) fixed by `fixorph9.sh` with a 1e-30 regen start |
| count | **every one of the 50 profiles equals its Hurwitz number**; 3,478,040 orbit representatives (Aut(B) × ⟨conj⟩) |
| backup | `pack9.py` packs (all tuples + representative positions + regen), `build7.py PACK=` rebuilds an L7 byte-identically |

Not done for degree 9: the numerical fingerprint distinctness check of E28 §2 (`distinct5.py`). The covers are distinct
as monodromy tuples by construction; a numerical check of the 60-digit maps was not run.

## 3. The (9, 9) search: the five-point key (`search7.py`, `scan7_nb.py`)

The four-point search of E28 (`search6.py`) would have needed about 5·10⁹ table entries and about nine days on four
machines. search7 keys on five points instead.

- **Table.** Every table cover once (no cosets), its C(8, 5) = 56 five-subsets of 8 key points (Fb5 = nB − jmin + 5 = 8).
  A hit leaves at most 3 of the 22 odd points unmatched (jmin = 19), so at least 5 of any 8 points of the table cover are
  matched, and the query tries all C(22, 5) five-subsets of its points. The key points are chosen per cover by greedy
  farthest-point selection (chordal distance), so covers with clustered points do not crowd one cell.
- **Key.** K = (Σ s_e, Σ z_e²), s_e the sphere point of j/1728 of the 4 points left after removing point e: symmetric
  and Möbius-invariant. Window w = 2.1·DEL7·(Φ_X + Φ_Y) + 10⁻¹³ with DEL7 = 10⁻¹² (double rounding of the 60-digit points
  measured 1.6·10⁻¹⁶) and Φ a first-order bound of the key's sensitivity; K stored in float64, Φ in float32, a dense
  (K0, K1) grid per Φ tier, sorted cells, K0 split in quantile slices (XSPLIT).
- **Candidates.** Quadruples paired by J value, the 120 orderings, two old-style four-point windows, Möbius map,
  maxfail and the one-to-one bound; then every coset of the table cover goes through search6's verification unchanged
  (labels, 60-digit points, margin check). A candidate whose |Ω| lower bound (all double distances below 10⁻⁸
  counted as matches) is above 4 is dropped before the 60-digit stage (true pairs had double distances ≤ 2·10⁻¹²).
- **Checks.** Positive control (each cover of 042433 Möbius-moved with two points replaced at random, 200 queries):
  search6 and search7 find the same 800 (f, q) pairs, and every query finds its planted copy. (9, 8) 042433: same result
  as search6. SAME run on six profiles: 12,336 hits = SELFONLY 12,336 + query-only run 0.

### Distribution over five machines
- Each machine is the table for its own profiles (local 60-digit L7 files); the queries are the orbit representatives of
  all 50 profiles, shared as query-only files (`export_q9.py`, about 390 bytes each).
- Pairs (f, U∘f) inside a query's own Aut(B) class are left to a SELFONLY run on the owner machine.
- **One side per machine pair** (`qskip9.py`): a pair is found from either side (§3 table argument), so for two
  different machines only one runs the other's queries; the orientation minimises the largest load (queries × slices:
  17.4 → 7.2 million). Every machine runs all queries of its own profiles.
- A candidate that needs the query's 60-digit points is deferred; afterwards the owner cuts those query covers into a
  mini L7 (`mkmini9.py`) and the table machine reruns them in full mode (`resolve99.sh`): 60-digit verification on both
  sides and birationality there.
- Heavy queries: the last 74 representatives of 223333 (80-digit-finished covers with points within 10⁻⁹ of each
  other) make some blocks take hours in one slice (raw key hits 1.7·10⁹ for 2,000 queries); query 2305373 alone took
  more than 2 hours. Blocks are therefore saved in parts of 100 queries, a part left unfinished is redone one query at
  a time, and a query left unfinished in its 26,334 five-subsets in 32 chunks (each about a minute); all units are
  claimed by idle workers. Splitting the five-subsets does not change the hits (tested; duplicates removed at merge).

| machine (profiles) | queries run | SELFONLY hits | table hits / deferred | after resolve: hits | deferred | margin |
|---|---|---|---|---|---|---|
| me (11) | 1,430,217 | 1,914,704 | 28 / 426 | 224 | 0 | 0 |
| part1 (22) | 1,732,141 | 3,836,088 | 16 / 500 | 304 | 0 | 0 |
| part2 (5) | 2,369,338 | 3,757,752 | 36 / 312 | 268 | 0 | 0 |
| part3 (9) | 2,191,625 | 3,108,396 | 4 / 628 | 216 | 0 | 0 |
| part4 (3) | 3,478,040 | 1,325,518 | 12 / 108 | 72 | 0 | 0 |

(The resolve runs have more hits than the query-only runs because they also see the query's own class, which the
query-only run leaves to SELFONLY; all are |Ω| = 0 composites.)

## 4. Birationality and the 80-digit recheck

- The double-precision fibre test flags 2,096 SELFONLY hits and 44 resolve hits as birational; bircheck40 (40 digits)
  calls 1,536 + 36 of them composite and leaves **568 'BIRATIONAL' or 'unclear'** (370 me, 182 part1, 8 part3 in
  SELFONLY; 8 me in resolve).
- All 568 belong to the ill-conditioned covers at the end of the profiles (regen, 80-digit finishing, seeds). Only 3–22
  of 38 points match at 40 digits, fibre distances about 10⁻²¹: the 40-digit refinement from double data stops short.
- `recheck_bir.py` (same procedure at 80 digits, 60 Newton steps, composite line 10⁻⁴⁰): **all 568 composite**, 38/38
  points matched, fibre distances 10⁻⁵¹ to 10⁻⁶⁶ (`logs/q99/*/recheck80_*.log`; part1's 182 reported by that machine).

## 5. Numerical margins

| run | 60-digit: largest accepted | 60-digit: smallest rejected |
|---|---|---|
| SELFONLY, five machines | ≤ 1.4·10⁻²⁴ | ≥ 1.1·10⁻¹⁶ |
| resolve me / part1 / part2 / part4 | 8.8·10⁻⁴², 4.3·10⁻⁴⁷, 3.8·10⁻⁴⁸, 1.1·10⁻⁴⁹ | 6.3·10⁻¹⁷, 2.6·10⁻²⁰, 5.7·10⁻¹⁹, 3.7·10⁻¹⁹ |
| resolve part3 | 4.9·10⁻²¹ | 2.4·10⁻²⁰ |

- The 10⁻²⁰ acceptance line has no clear gap for part3 (as E28 §4 at (8, 8)): the clustered covers carry about 10⁻²⁰
  accuracy at 60 digits. The **margin check** (any candidate with |Ω| > 4, rejected distances below MIDTOL = 10⁻¹⁴, and a
  one-to-one bound ≤ 4 if those counted) found **0 candidates in every run** (27 log lines, all 0). So no hit hides
  behind the 10⁻²⁰ line, as long as the 10⁻¹⁴ line holds. Accepting too much only adds hits, which were all composite.

## 6. What this is not
- Not exact (as E21 §4, E24 §4, E28 §5). Certification would need the 12·10⁶ covers certified, certified
  non-coincidences and exact proofs of the composites.
- The degree-9 list is complete by the Hurwitz counts, but the numerical distinctness check was not run (§2).
- Closes only max(a, b) ≤ 9. Degree 10 would be larger again (the weighted counts grow by about 13× per degree).

## 7. Reproduction
```
# covers: run9.sh <dir> 9 <profiles> (mono_par.py, HPENDGAME, finish80; split9.sh / merge9.py for large profiles)
python3 build7.py 9 <tag> <dir> 4                       # 60-digit L7, exit 3 = orphans -> fixorph9.sh
python3 pack9.py 9 <tag> <dir> pack_9_<tag>.npz         # backup (build7 PACK= rebuilds)
bash q98.sh <L7 dir> <work dir> <name>                  # (8,9): search6 against the degree-8 list
bash run99.sh <L7 dir> <work dir> <name> [more dirs]    # (9,9): query files, SELFONLY, table run (QSKIP from qskip9.py)
bash resolve99.sh <work dir> <name>                     # mini L7 for the other machines, then the full-mode rerun
python3 recheck_bir.py self99_<name>.pkl loc            # 80-digit recheck of 'unclear' SELFONLY flags
python3 recheck_bir.py res99r_<name>.pkl loc rmini      # the same for the resolve run
```
Pickles and L7 files are not committed (size); the packs are in the project's shared folder.
