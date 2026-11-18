# E23 — Problem W at slack (0, 0), max(a, b) ≤ 5: computer-assisted proof with certified enclosures (2026-11-18)

Status: research note, **computer-assisted proof (ball arithmetic + rigorous floating-point error bounds), not
independently audited, zero credit**. STATE is not changed.
Code: `slack0/rigorous-upto5-20261118/` (`sh run_all.sh`, about 9 minutes on one core; python-flint 0.9, numpy).
Upgrades E21 (numerical) for max(a, b) ≤ 5. E22 (degree 6, numerical) is **not** covered.

## 1. Result

**Theorem (computer-assisted).** There is no k = 8, γ = 0 configuration with both slacks 0, |Ω| ≤ 4 and
(p₁, p₂) birational for (a, b) ∈ {(3, 4), (4, 4), (4, 5), (5, 5)}.

With the earlier exact results this closes **max(a, b) ≤ 5** for the mixed slack (0, 0) case without numerics in
the logic:

| (a, b) | how | status |
|---|---|---|
| (1, b) | E06/E08 | exact |
| (2, 2), (2, 3), (3, 3) | E11 §9 (`slack0/exact-20261109/`, F_p + Hensel lifting) | exact, not audited |
| (2, 4), (3, 5) | E14 Theorem A⁺ (|a − b| = 2, nested type only) | proof, audited |
| \|a − b\| ≥ 3 | E10 §2 | proof |
| **(3, 4), (4, 5)** | this note: every candidate has a certified \|Ω\| ≥ 14 resp. ≥ 18 | **computer-assisted** |
| **(4, 4), (5, 5)** | this note: every candidate with \|Ω\| possibly ≤ 4 is proved to satisfy q∘M = U∘f exactly | **computer-assisted** |

## 2. The chain of the proof

### 2.1 Complete certified list of covers (`certify.py`)
- Normal form (one per profile t, one profile per Aut(B)-orbit): f = P/Q of degree n, three critical points
  c₀, c₁, c₂ at fixed dyadic points Φ in prescribed fibres, a fixed dyadic linear normalization L·(P, Q) = 1; unknowns
  (P, Q, c₃ … c_{2n−3}); equations F_y(c_k) = F_y′(c_k) = 0 with F_y = y₁P − y₀Q. Square system of size 4n − 3.
- **Existence and uniqueness:** each numerical cover (from `speedup-20261118/mono.py`, only a starting point) is
  refined at 320 bits and passes the (complex) **Krawczyk test** twice: radius 10⁻⁵⁰ (tight enclosure) and 10⁻¹⁶
  (uniqueness box Z_f). Worst Krawczyk ratio |K|/ρ: 4·10⁻⁴¹.
- **Genuine cover:** homogeneous resultant of (P, Q) excludes 0 (smallest lower bound 3·10⁻³⁰), all critical balls
  pairwise disjoint. Then f has degree n and 2n − 2 distinct ramification points over B; by Riemann–Hurwitz each is
  simple and there is no other ramification, i.e. f is a slack-0 cover of profile t.
- **Completeness:** all ordered choices of the three Φ-critical points are transported from the certified box by
  ball arithmetic (exact renormalizations). Every exact cover of profile t gives exactly m(t)/|Aut| normalized
  maps, so there are m(t)·H(t) in all (H = exact Hurwitz number, `hurwitz_exact.py`, rational arithmetic; it agrees
  with the character formula of `speedup-20261118/hurwitz_char.py`). The enclosures are clustered by overlap; the
  number of clusters is a lower bound for the number of distinct exact maps found, and it equals m(t)·H(t) in
  **every** profile (degree 3: 2 profiles, 8 covers; degree 4: 11 profiles, 158; degree 5: 7 profiles, 612). Hence
  every cover of degree ≤ 5 is U∘f for a certified base map f and U ∈ Aut(B).
- **Odd points:** for each base map and each y ∈ B, deg F_y = n is certified (leading coefficient ≠ 0), and the
  n − 2t(y) simple roots are certified by 1-D Krawczyk (uniqueness rectangle 10⁻²⁰, enclosure ≤ 3·10⁻³⁴), disjoint
  from each other and from the critical balls. So the odd points are complete and isolated.

### 2.2 Certified pair search (`search_rig.py`)
- Same logic as E21 §2.3 (E12 Lemma 0: j ≥ j_min, so four matched points among the first F odd points of f; their
  cross-ratio equals that of the matched quadruple of q). Query: all base maps of degree a; table: all base maps of
  degree b with the 6 permutations of the label classes (= all degree-b covers, since U ∈ Aut(B) acts on the
  classes through S₃ and the problem only sees classes).
- All arithmetic is midpoint–radius in double precision with rigorous rounding terms (standard IEEE error model;
  every radius inflated by 1 + 10⁻¹²). Lookup: cross-ratio λ in the unit disc (or 1/λ), window = sum of the two radii
  + 10⁻¹¹, with the |λ| ≈ 1 boundary handled by the table's largest radii, so **every** truly matched quadruple
  pair is found.
- For each found pair, M(x) = y is tested for every other (x, y) as "[num:den] of the cross-ratio with the defining
  triple agree", a ball containing 0 or not. Lower bound |Ω| ≥ n_A + n_B − Σ_x w(x) (w = 2 for a possible
  same-label partner, 1 for a possible other-label partner), and the same from the q side.

| (a, b) | quadruple pairs found | excluded (bound > 4) | left | bound histogram |
|---|---|---|---|---|
| (3, 4) | 16,128 | 16,128 | 0 | all 14 |
| (4, 5) | 34,560 | 34,560 | 0 | all 18 |
| (4, 4) | 3,483,696 | 2,206,896 | 1,276,800 | 0 or 4 for the rest |
| (5, 5) | 3,852,104 | 2,731,544 | 1,120,560 | 0 or 4 for the rest |

### 2.3 Exact proof for the remaining candidates (`prove.py`)
- **Isolation lemma.** If h is an exact map with the same branch data as the base map f, and the ball enclosure of
  h∘A_h (A_h: exact renormalization by three critical points of h) lies in the uniqueness box Z_f, then h∘A_h = f.
- **Composite proof.** For a candidate (f, q, M) with defining triple x_i ↦ y_i and U ∈ Aut(B) with
  U(f(x_i)) = q(y_i) (exact Gaussian-rational Aut(B)), take h = U⁻¹∘q∘M. Then h(x_i) = f(x_i) exactly; by the lemma
  f = h∘A_h, hence f(A_h⁻¹x_i) = f(x_i), and A_h⁻¹x_i lies in the uniqueness rectangle of x_i, so A_h⁻¹x_i = x_i
  (i = 1, 2, 3) and A_h = id: **q∘M = U∘f exactly**, so (f, q∘M) is not birational.
- **Transfer.** Candidates with the same (f, q, labels) and numerically the same M form a group (3,094 groups for
  (4, 4), 2,749 for (5, 5)). One member is proved as above; for every other member the ball of M₀(x′_i) lies in the
  uniqueness rectangle of y′_i, and M₀(x′_i) is a root of the same fibre polynomial (because q∘M₀ = U∘f), so its
  triple gives the same M₀.
- Result: (4, 4) 3,094 direct proofs + 1,273,706 transfers; (5, 5) 2,749 + 1,117,811; **no failure**. In
  particular no candidate needed the "shared degree-2 factor" type (code `prove_S`, present but not used, untested).
- Self-tests (`selftest.py`): the trivial configuration (f, f, id) is found for every query cover (158/158, 612/612);
  for random candidates the proof succeeds for exactly one U and fails for the 12 (resp. 33) other label-compatible
  U; with a perturbed triple it never succeeds.
- One (5, 5) group (f = q of profile (1,1,1,2,1,2), points 0.007 apart) first failed because the ball radii grew to
  10⁻²⁰; it passed after tightening the odd-point enclosures (second Krawczyk at 10⁻⁴⁴). Nothing was relaxed.

## 3. What the proof rests on (the remaining trust)
- Mathematics from earlier notes: E10 §2 (|Ω| formula, |a − b| ≤ 2 at slack 0), E12 Lemma 0, E11 Lemma 1 (slack 0
  ⇔ all ramification over B simple), E14 A⁺, E11 §9, E06/E08. Riemann's existence theorem (covers ↔ monodromy
  tuples, so the Hurwitz number counts covers weighted by 1/|Aut|).
- Software: arb (python-flint) ball arithmetic; IEEE double rounding in numpy for the search (generous constants);
  the exact Hurwitz-number program; and the correctness of this research code. **No independent audit yet.**
- The numerical cover lists only provide starting points; their completeness is not assumed (it is proved by the
  count in §2.1).

## 4. Degree 6 (not done here) and what it needs
- (5, 6): the degree-6 lists (27 profiles, 7,148 representatives, E22) must be recomputed or recovered; the E22
  pickles are not in the repository. Certification and the (5, 6) search with this code should take minutes; the
  E22 cover computation took ≈ 4 h on 4 cores and needed hand-holding (small braid orbits, loose `analyse`).
- (6, 6): the quadruple table of this code (≈ 7.7·10⁸ entries) is too large; the split-subset index of `search2.py`
  must be made rigorous the same way. Non-birational (6, 6) pairs can also share a factor of degree 2 (the σ-type
  proof is written but untested) or **3** (non-Galois in general; no exact proof scheme yet — a new isolation
  argument for f = h₁∘r, g = h₂∘r is needed).
- Rough estimate: one more session of several hours for (5, 6), and a new lemma plus a few hours of computation
  for (6, 6).

## 5. Reproduction
```
cd slack0/rigorous-upto5-20261118 && sh run_all.sh      # logs/ : certify_n, search_a_b, prove_a_b, selftest_a_b
```
Inputs `inputs/data{3,4,5}/cov_*.pkl` are the numerical covers from `speedup-20261118/gen.sh` (starting points only).
