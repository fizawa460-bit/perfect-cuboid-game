# E21 — Problem W at slack (0, 0) for all bidegrees with max(a, b) ≤ 5 (numerical, 2026-11-18)

Status: research note, **numerically verified, not exactly certified, not audited, zero credit**. STATE is not changed.
Code: `slack0/numeric-upto5-20261118/` (research code, run from that folder).

- Question (E19 roadmap, user request "1と2をすすめる", item 2): how far can the small bidegrees of the mixed slack (0, 0)
  case be closed by direct computation, and how does the cost grow?
- Scope: k = 8, γ = 0 (g ≤ 1), both slacks 0, |Ω| ≤ 4, birational pair (p₁, p₂), as in E11 §4/§4b. At slack 0
  |a − b| ≤ 2 (E10 §2); (1, b) is E06/E08. The open cases with max(a, b) ≤ 5 were
  **(2, 4), (3, 4), (4, 4), (3, 5), (4, 5), (5, 5)**. (2, 2), (2, 3), (3, 3) are exact in E11 §9 and are rerun here as
  controls.
- Correction to the roadmap memo "E12 は (2,2) のみ": E11 §9 already settles (2, 2), (2, 3), (3, 3) exactly.

## 1. Result

**Numerical proposition.** There is no k = 8, γ = 0 configuration with both slacks 0, |Ω| ≤ 4 and (p₁, p₂) birational
for any bidegree (a, b) with 2 ≤ a ≤ b ≤ 5, |a − b| ≤ 2. With E06/E08 (a = 1) and E10 §2 (|a − b| ≤ 2):
**the mixed slack (0, 0) case has no solution with max(a, b) ≤ 5** (numerically).

| (a, b) | covers (query / table) | candidate M | smallest \|Ω\| found | \|Ω\| ≤ 4 | birational | time |
|---|---|---|---|---|---|---|
| (2, 2) control | 15 / 15 | 92,736 | 0 | 326 (all non-birational) | 0 | 11 s |
| (2, 3) control | 15 / 60 | 2,304 | 10 | 0 | 0 | <1 s |
| (3, 3) control | 8 / 60 | 37,824 | 0 | 51 (all non-birational) | 0 | 6 s |
| (2, 4) | 15 / 680 | 6,528 | 12 | 0 | 0 | 1 s |
| (3, 4) | 8 / 680 | 20,480 | 14 | 0 | 0 | 10 s |
| (4, 4) | 158 / 680 | 1,062,176 | 0 | 767 (all non-birational) | 0 | 10 min |
| (3, 5) | 8 / 6,090 | 9,216 | 16 | 0 | 0 | 11 s |
| (4, 5) | 158 / 6,090 | 177,464 | 18 | 0 | 0 | 18 min |
| (5, 5) | 612 / 6,090 | 4,817,400 | 0 | 2,474 (all non-birational) | 0 | 47 min (4 cores) |

- "\|Ω\| ≤ 4" counts distinct (f, q, M) found; they are repeated descriptions of composite pairs (q∘M = U∘f, or a
  shared degree-2 factor for (4, 4)), not distinct curves.
- The controls agree with E11 §9: (2, 3) has nothing, (2, 2) and (3, 3) have only non-birational hits.
- The unbalanced pairs are far from the threshold: the smallest |Ω| is 10–18, i.e. the two legs share far fewer odd
  points than needed. Only a = b produces |Ω| ≤ 4, and only through composites.

## 2. Method

### 2.1 Counting the slack-0 covers (exact, `hurwitz.py`)
- By E11 Lemma 1 a slack-0 map of degree n is a cover of (P¹; B) with every ramification point of index 2 over B.
  Monodromy: six involutions σ_y ∈ S_n (σ_y has t(y) transpositions), product 1, transitive, Σ t(y) = 2n − 2.
- A dynamic programme over (partial product, orbit partition) gives the Hurwitz numbers Σ 1/|Aut| per profile t:

| n | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|
| covers (weighted) | 7.5 (15 covers, Aut = 2) | 60 | 575 (680 covers) | 6,090 | 70,158 |
| profiles / up to Aut(B) | 15 / 1 | 15 / 2 | 141 / 11 | 90 / 7 | 546 / – |

Growth ≈ ×11.5 per degree (70,158 at n = 6; the roadmap memo gives ≈ 6·10¹⁰ at n = 11).

### 2.2 Computing the covers (numerical, `covers.py`, `run_covers.py`, `allcovers.py`)
- Unknowns: the coefficients of P, Q and the 2n − 2 critical points c_k (three of them fixed, killing the source
  Möbius group). Conditions y₁P(c_k) − y₀Q(c_k) = 0 and the same for the derivative: a square system, solved by Newton
  from random starts (complex double precision).
- A solution is accepted only if every fibre over B has exactly the prescribed type (t(y) double points, all other
  points simple) and all points of p⁻¹(B) are distinct.
- Duplicates are removed by a Möbius-invariant fingerprint (label-weighted sums of a bounded function of the
  j-invariant of every 4-subset of p⁻¹(B)). New solutions are closed under Stab(t) ⊂ Aut(B) and complex conjugation.
- **Completeness check:** for every profile (one per Aut(B)-orbit), Σ 1/|Aut| of the found covers equals the Hurwitz
  number of §2.1 exactly. The full lists (apply the 24 elements of Aut(B), deduplicate) have weighted sizes 7.5, 60,
  575, 6,090, as they must.
- Every cover is refined to 40 digits (mpmath Newton on the same system with three critical points fixed; residual
  < 10⁻²⁵), and its odd points are refined by Newton to 40 digits.

### 2.3 Searching the pairs (`search.py`)
- p₁ = f (degree a), p₂ = q∘M (degree b), M Möbius. By E12 Lemma 0, j ≥ j_min := max(n_A, n_B) − 4 with
  n_A = 2a + 4, n_B = 2b + 4 (odd points). So among any F := n_A − j_min + 4 fixed odd points of f, at least **four**
  are label-matched to odd points of q, with the same cross-ratio.
- **Quadruple index instead of pairs:** one table of all ordered (modulo the Klein four-group) 4-tuples of odd points
  of all degree-b covers, keyed by (four labels, cross-ratio). Each 4-subset of the first F odd points of f (all 24
  orderings) is looked up. A hit gives M from three points; then all n_A × n_B distances are computed.
- So the cost is **linear** in the number of covers (table size N_b·6·C(n_B, 4) plus a few lookups per query), not the
  product N_a·N_b. This is what makes (5, 5) cheap: 3.66·10⁷ table entries.
- Symmetry: Aut(B) acts on both legs at once (labels move together), so f runs only over the profile representatives
  (612 of the 6,090 degree-5 covers).
- Classification of a coincidence: chordal distance < 10⁻¹¹ in double precision is a match, > 10⁻⁴ is not; anything
  in between is recomputed with the 40-digit points (M rebuilt from the same triple), where matches are < 10⁻³³ and
  non-matches > 10⁻¹³ (table in §3). Cases that cannot reach |Ω| ≤ 4 even if every ambiguous pair matched are skipped.
- Then |Ω| = n_A + n_B − 2j − h (E10 §2). For |Ω| ≤ 4: birationality test on three random fibres of f (q∘M takes the
  value of the base point at a second point of the fibre in all three ⇔ non-birational).

## 3. Numerical margins

| (a, b) | double: largest accepted | 40 digits: largest accepted | smallest rejected | largest cross-ratio error of a true quadruple (window 10⁻⁵) |
|---|---|---|---|---|
| (2, 2) | 1.1·10⁻¹⁴ | – | 6.0·10⁻³ | 1.5·10⁻¹⁵ |
| (2, 3) | 4.6·10⁻¹⁵ | – | 3.5·10⁻³ | 9.4·10⁻¹⁶ |
| (3, 3) | 3.8·10⁻¹³ | 9.5·10⁻³⁸ | 2.6·10⁻⁵ | 1.4·10⁻¹⁴ |
| (2, 4) | 3.5·10⁻¹⁵ | – | 1.3·10⁻³ | 6.2·10⁻¹⁶ |
| (3, 4) | 2.2·10⁻¹⁴ | 7.2·10⁻³⁹ | 2.1·10⁻¹⁰ | 1.1·10⁻¹⁵ |
| (4, 4) | 9.9·10⁻¹² | 4.2·10⁻³⁴ | 2.0·10⁻¹¹ | 1.7·10⁻¹³ |
| (3, 5) | 1.5·10⁻¹³ | 3.9·10⁻³⁶ | 1.9·10⁻¹⁰ | 4.8·10⁻¹⁵ |
| (4, 5) | 1.0·10⁻¹² | 3.9·10⁻³⁶ | 5.4·10⁻¹³ | 4.8·10⁻¹⁵ |
| (5, 5) | 8.7·10⁻¹² | 2.4·10⁻²⁹ | 2.1·10⁻¹³ | 5.6·10⁻⁹ |

- The lookup window (10⁻⁵ in the chordal coordinate of the cross-ratio) is larger than the error of any true quadruple
  by at least 3 orders ((5, 5): 5.6·10⁻⁹) and by 8 orders for max(a, b) ≤ 4, so no coincidence is lost by the index.
- The smallest rejected distances (down to ~10⁻¹³) are genuine near-misses seen at 40 digits; the gap to the accepted
  ones is ≥ 20 orders of magnitude.

## 4. What this is not
- **Not exact.** Like E11 revision 2, every decision is numerical with a large gap. The exact route of E11 §9 (one
  prime where all covers and odd points split, plus a lifting argument for composites) does not transfer directly:
  for n = 4, 5 the field of definition of the covers is large and no such prime was searched. Needed for a theorem:
  (i) the 680 + 6,090 covers certified (e.g. Krawczyk/interval Newton on the square system, whose count matches the
  exact Hurwitz numbers), (ii) non-coincidences by certified enclosures, (iii) the composite hits proved exactly
  (q∘M = U∘f, or a shared degree-2 factor).
- Completeness of the cover lists rests on the exact Hurwitz numbers plus the numerical deduplication.
- It closes only max(a, b) ≤ 5; the roadmap target is a ≲ 11.

## 5. Cost and how far this goes

| step | n = 4 | n = 5 | n = 6 (estimate) | n = 11 (estimate) |
|---|---|---|---|---|
| covers | 680 | 6,090 | 70,158 | ≈ 6·10¹⁰ |
| computing them (Newton multistart, 4 cores) | ~1 min | ~30 min (slow tail: last few of 240) | hours–a day; needs monodromy/homotopy solving instead of random starts | impossible this way |
| quadruple table (entries) | 2.0·10⁶ | 3.7·10⁷ | 7.7·10⁸ (stream it instead of storing) | ≈ 10¹⁵ |
| pair search (a, a) | 10 min | 47 min (4 cores, Python) | hours (C rewrite) | impossible |

- The bottleneck is **computing the covers** (numerical algebraic geometry), not the pairing: the quadruple index
  made the pair search linear in the number of covers.
- Symmetry used: Aut(B) of order 24 on the query side (×≈10), Klein four-group on the table (×4). Not yet used:
  complex conjugation (×2), leg swap for a = b (×2), and Stab(t) on the table. These give constant factors only; the
  ×11.5 growth per degree stays.
- Realistic reach with a monodromy solver and C: n = 6, perhaps 7 (≈ 8·10⁵ covers). n = 11 (≈ 6·10¹⁰ covers, each
  needing a polynomial solve) is out of reach by enumeration. Closing the gap 6 … 11 needs structure (e.g. only covers
  whose triangulation has a large Hecke-type region can pair, E19 §13–§14) rather than brute force.

## 6. Reproduction
```
python3 hurwitz.py 6                       # counts (§2.1), ~25 s
sh run_all.sh 4 | sh; sh run_all.sh 5 | sh # covers per profile representative (§2.2); see run_covers.py usage
python3 allcovers.py 2 3 4 5               # full lists + 40-digit refinement -> all_n.pkl
python3 search.py a b 2.5e-6 [1e-6 shard nshards]   # §2.3
```
Intermediate pickles are not committed (size); the logs of the final runs are in `logs/`.
