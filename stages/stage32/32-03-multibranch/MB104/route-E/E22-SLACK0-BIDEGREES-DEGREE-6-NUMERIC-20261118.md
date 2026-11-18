# E22 — Problem W at slack (0, 0) for the bidegrees (5, 6) and (6, 6) (numerical, 2026-11-18)

Status: research note, **numerically verified, not exactly certified, not audited, zero credit**. STATE is not changed.
Continues E21 (`E21-SLACK0-BIDEGREES-UP-TO-5-NUMERIC-20261118.md`), same set-up and conventions.
Code: `slack0/degree6-20261118/` (research code, run from that folder).

- Question (user, after E21): push the direct computation to degree 6. By E14 Theorem A⁺ the rows |a − b| = 2 are
  closed, so the open bidegrees with max(a, b) = 6 are **(5, 6) and (6, 6)**. The user stopped this thread at degree 6;
  degree 7 uses the tools of `slack0/speedup-20261118/` (PR #1881).

## 1. Result

**Numerical proposition.** There is no k = 8, γ = 0 configuration with both slacks 0, |Ω| ≤ 4 and (p₁, p₂) birational
for (a, b) = (5, 6) or (6, 6). With E21 and E14 A⁺: **the mixed slack (0, 0) case has no solution with
max(a, b) ≤ 6** (numerically).

| (a, b) | covers (query reps / table) | candidate M | \|Ω\| ≤ 4 hits | birational | time |
|---|---|---|---|---|---|
| (5, 6) | 612 / 71,508 | 4,481,248 | 0 | 0 | 6 min (1 core) |
| (6, 6) | 7,148 / 71,508 | 3.08·10⁸ | 33,759 (all non-birational) | 0 | ≈ 5.9 core-hours (see §4) |

- (5, 6): every candidate either has a lower bound |Ω| > 4 before any distance is computed, or (6,767 cases) |Ω| = 24.
- (6, 6): the hits are repeated descriptions of composites. The double-precision birationality test (three random
  fibres, threshold 10⁻⁷) flagged **12 hits (7 distinct pairs) as birational**; all are false alarms, see §3.

## 2. The degree-6 covers

- 27 profile representatives up to Aut(B), weighted 7,040; the full list has 71,508 covers, **weighted 70,158 =
  the exact Hurwitz number** (E21 §2.1). Every profile matches its Hurwitz number exactly (also checked against the
  braid-orbit census of `speedup-20261118/census_6.txt`).
- Method (`mono.py`, `mono_loose.py`, `track.py`, `closure.py`):
  - monodromy solving: the branch values move in a generic chart (`MS` in `mono.py`), along pure-braid loops,
    half-twist swaps of equal-t points and random half-twist words that preserve the profile; all known covers of a
    profile are tracked together; new covers are closed under Stab(t) × complex conjugation.
  - seeds: random-start Newton, plus the **decomposable covers h∘g** built explicitly (`construct.py`, (deg g, deg h)
    = (2, 3), (3, 2)), which are the small braid orbits that no loop from the big orbit reaches.
  - every accepted cover is refined to 40 digits (`hp.py`; residual < 10⁻²⁸ and the points move < 10⁻⁶), and
    duplicates are removed with the Möbius invariant computed from the 40-digit points (smallest separation between
    distinct covers of (1,1,2,2,2,2): 0.026 relative, tolerance 10⁻⁵).
  - the last 4 covers of (1,1,2,2,2,2) were found only after relaxing the |f′| test of `covers.analyse` from 10⁻⁶ to
    10⁻¹⁰ (the cause found in PR #1881; `mono_loose.py` also retries `analyse` after a random source Möbius map and
    polishes each tracked endpoint by Newton). With the strict test, about 12 % of the tracked endpoints were
    rejected, and the missing covers were among them.
- 40-digit odd points of all 7,148 representatives are precomputed (`hp_pre.py`, max residual 5·10⁻³⁵).

## 3. The 12 "birational" flags

All 7 pairs are of the form (f, U∘f∘M) with U ∈ Aut(B) (the table cover is an Aut(B) image of the query cover itself), and f has
nearly colliding points, so the double-precision M is only accurate to ~10⁻⁶ and the fibre test misses the matches.
`birchk.py` + `birhp.py` redo them at 40 digits:

| hit | \|Ω\| | 40 digits |
|---|---|---|
| (4391, 39982), (4391, 256), (1816, 42833), (3598, 32043) | 0 | M (rebuilt from three odd points) carries all 26 points of f⁻¹(B) (odd and double) onto q⁻¹(B), labels consistent, distance ≤ 2.6·10⁻³⁵. Six shared fibres ⇒ q∘M = V∘f with V Möbius ⇒ not birational |
| (4386, 57139), (4386, 66137), (4386, 39874), (4386, 68337), 2 hits each | 4 | f has |Aut| = 2. Fibre test at 40 digits: all 6 points of a fibre of f have the same value of q∘M (distance ≤ 1.4·10⁻³⁴, 3 fibres) ⇒ q∘M = V∘f ⇒ not birational |

(The (1816, 42833) flag is not even reproducible in double precision: a rerun with another random fibre gives
non-birational.) For degree 7 the birationality test should be done at 40 digits whenever double precision says
"birational".

## 4. Numerical margins and cost

| (a, b) | double: largest accepted | 40 digits: largest accepted | 40 digits: smallest rejected | largest cross-ratio error of a true quadruple |
|---|---|---|---|---|
| (5, 6) | 9.6·10⁻¹² | 2.8·10⁻³⁵ | 2.2·10⁻¹³ | – |
| (6, 6) | 1.0·10⁻¹¹ | 5.8·10⁻²⁸ | 4.8·10⁻¹⁷ | 8.6·10⁻¹² |

- The lookup window (10⁻⁵ chordal) exceeds the largest true-quadruple error by 6 orders. The 40-digit gap at (6, 6)
  is 11 orders (E21 had ≥ 20); the smallest rejected distances come from covers with nearly colliding points.
- Pair search (`search2.py`): the index holds the quadruples of the query representatives' first F odd points (24
  orderings), and all degree-b covers are streamed against it in chunks of 64, with vectorised Möbius maps and
  distances, de-duplication of (f, M) before the distances, and the 40-digit points read from the precomputed table.
  (6, 6): 1.2·10⁷ index entries, 7.1·10⁴ streamed covers; about 5.9 core-hours (Python, 3–4 processes).
  One shard was killed twice by the memory limit (a single process can reach ~10 GB); it was rerun in smaller
  shards: shard 2 of 3 (chunks ≡ 2 mod 3) = chunks ≡ 8 mod 9 ∪ chunks ≡ 2, 11, 5, 14 mod 18 (`logs/res2_66_r_8.log`,
  `logs/res2_66_r18_*.log`).
- Completeness bookkeeping: the main (6, 6) run used the list before the last covers of (1,1,2,2,2,2) were added
  (7,116 reps, 71,256 covers). `mkextra.py` then ran (i) the 32 new representatives against the full new table and
  (ii) all 7,148 representatives against every cover of the new table whose coefficients are not in the old one
  (2,939 covers, a superset of the new ones). Together this covers the full product.
- Degree-6 covers: about 4 h on 4 cores in total, most of it on (1,1,2,2,2,2) and (1,2,1,2,2,2) (2,556 covers each).

## 5. What this is not
- Not exact (as E21 §4). Certification would need the 71,508 covers certified (e.g. interval Newton), certified
  non-coincidences, and exact proofs of the composites.
- Closes only max(a, b) ≤ 6. At degree 7, (5, 7) is covered by E14 A⁺ (|a − b| = 2); (6, 7) and (7, 7) remain.

## 6. Reproduction (from `slack0/degree6-20261118/`)
```
python3 construct.py                         # decomposable seeds -> seeds6/
python3 mono_loose.py 6 t1,..,t6 seed target maxtime   # per profile representative -> mono/cov_6_*.pkl
python3 allcovers2.py 6                      # full list -> all2_6.pkl
python3 hp_pre.py 6 3                        # 40-digit odd points -> hp_6.pkl
python3 search2.py 5 6 2.5e-6
python3 search2.py 6 6 2.5e-6 k 3            # k = 0, 1, 2
python3 birchk.py fi:qi ...; (search2.py on the bk_*.pkl pairs, see logs); python3 birhp.py fi:qi ...   # 40-digit recheck
```
Pickles are not committed (size); the logs of the final runs are in `logs/`.
