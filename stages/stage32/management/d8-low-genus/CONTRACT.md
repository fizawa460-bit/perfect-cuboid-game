# Stage32 D8-LOW-GENUS — no curves of degree 8 and geometric genus ≤ 1 on the cuboid surface (proof + exact computation, research cycles 32R-20..23)

```text
CLAIM: Every integral curve C on S̃ (the minimal resolution of the cuboid surface S) with d = K·C = 8 has geometric
       genus ≥ 2. Equivalently, there are no rational or elliptic curves of degree 8.
       Degree ≤ 6 was classified by Stoll–Testa (arXiv 1009.0388), so this is the next degree.
STATUS: Proof + exact computer algebra. First hostile audit (head 817845ce): FAIL on (1) floating-point enumeration
        not certified and (2) verifier scope; both repaired here (§2 certified enumeration, §8). Needs re-audit.
        No credit flags are changed.
SCOPE: A geometric fact about the d = 8 strata. MAIN (V52) and all formal counts are unchanged.
BUILDS ON: #1842 §0–§3a (FSM model, Bolza curve Y, Δ = Δ(2,3,8) = normalizer of the Bolza maximal order,
           Hecke product formula h ≥ 8 for g ∈ Comm(Δ) \ Δ) and #1843 §6 (Γ_Y acts transitively on Δ/K).
           Both were audited.
SIDE RESULT (remark only, not part of the claim): the curve F* = (x−y)⁴ + (x⁴−1)(y⁴−1) lifts to 8 curves of
           genus 3 on S. With its 4 matching variants this gives 32, the number of C² = −4, e = 12 classes.
```

## 0. Model and notation
- **Model (FSM, #1842 §0).**
  - B̄ = X(8)²/G with G = (Z/2)³ acting diagonally. It is the normalization of the (Z/2)³ cover of P¹_x × P¹_y given by
    w_j² = h_j(x)h_j(y), with h_1 = x, h_2 = x²−1, h_3 = x²+1 (homogeneously x0x1, x0²−x1², x0²+x1²).
  - Cusps: {0, ∞, ±1, ±i}, in the classes {0,∞}, {±1}, {±i}.
  - S has 48 A1 nodes. They lie over the 12 same-class cusp pairs (c, c′), 4 over each pair. The stabilizer of such a point is the common inertia involution.
  - f : S̃ → P¹×P¹ is finite of degree 8 away from the exceptional curves.
- **Boundary curves.**
  - For a cusp c, write ℓ_c = {x = c} and ℓ′_c = {y = c}.
  - f*ℓ_c = 2E_c + Σ_{8 nodes on ℓ_c} Exc_j. Here E_c is the boundary elliptic curve over ℓ_c (labels 33–44), and Exc_j are the exceptional curves (labels 93–140).
  - Coefficients: x − c = s² on X(8)² near a node (local coordinates s, u, quotient by ±1). So s² vanishes to order 2 along {s = 0} and to order 1 on the exceptional curve.
  - F1 = f*ℓ_c is the fibre class of x. In the repository lattice this is exactly `2E + Σ_{Exc meeting E} Exc` (checked in the verifier, F).
- **Invariants of a curve.** For C ⊂ S̃ integral, not a fibre component:
  - n1 = F1·C = deg(x|C̃) and n2 = F2·C, with n1 + n2 = d;
  - m_j = C·Exc_j, and e = Σ m_j;
  - g = geometric genus.
  - Each node lies on exactly one vertical and one horizontal cusp line.
  - For a point P ∈ C̃ over ℓ_c: ord_P(x − c) = 2(C·E_c)_P + Σ_j (C·Exc_j)_P.
- **Fibre components.** A fibre of x over a non-cusp is (G-orbit × X(8))/G ≅ X(8), of genus 5. Fibres over cusps consist of E_c and Exc_j (known curves). So from now on n1, n2 ≥ 1.

## 1. Hurwitz bound (self-contained)
Let k_c = #(points of C̃ over ℓ_c). Then:
- k_c ≤ C·E_c + B_c, where B_c is the number of points of C̃ over ℓ_c that meet some Exc_j.
- Σ_c C·E_c = (6n1 − e)/2, summed over the 6 vertical lines, since each node lies on exactly one of them.
- B := Σ_c B_c ≤ e.
- By Riemann–Hurwitz for x: 2g − 2 + 2n1 = R_x ≥ Σ_c (n1 − k_c).
- Combining these gives **e ≥ 2n_i − 4g + 4** (i = 1, 2, by symmetry).
- max(n1, n2) ≥ 4, so **e ≥ 12 − 4g**. Also e ≤ 6·min(n1, n2) ≤ 24.

## 2. Complete enumeration of numerical classes (32R-21; enumeration/)
- **Constraints:**
  - K·C = 8 and F1·C = n1 ∈ {1..7};
  - Σ m_j = e ∈ [12 − 4g, 24];
  - C² ≥ 2g − 2 − 8, since p_a ≥ g;
  - C² ≤ d²/K² = 4 (Hodge);
  - C·Γ ≥ 0 for all 140 known curves.
- **Slices (generated inventory, `enumeration/run_certified.py`):**
  - n1 = 1..7 with (C² ≥ −10, e = 12..24) and (C² ≥ −8, e = 8..11).
  - Genus-1 classes with e ≥ 12 lie inside the first family.
  - The constraint "Σm_j = e" is imposed for every integer e in range, so no parity argument is needed.
- **Certified enumeration** (`certified_driver.py` + `certified_enum.c`; replaces the floating-point pipeline audited at 817845ce):
  - **Exact data.** All data are exact rationals (python-flint): the affine slice (HNF), the LLL basis, M = UᵀDU, the centre zs, the radius R, and the linear forms f0 + g·y with Cauchy–Schwarz constants S_k(i) = Σ_{j<i} g_kj²/d_j. R < 0 is decided exactly.
  - **Enclosures.** Each rational is passed as an enclosing double interval (degenerate if exactly representable).
  - **Rigorous pruning.** The C program keeps rigorous bounds: [c_i] for the centres, [y_i], an upper bound on the remaining radius, and upper bounds on the linear forms. Every operation is rounded outward (UP/DN, justified in the file header). A branch is discarded only if the exact discarding condition is implied: radius < 0, or f_k < 0 with f_k² > rem·S_k(i). Candidate ranges are supersets of the exact ranges.
  - **Exact leaf check.** The leaves are therefore a superset of the exact solutions. Every leaf is rechecked in exact integer arithmetic.
  - **Floating point.** No floating-point quantity is trusted beyond these enclosures. The build flags forbid FMA contraction and fast-math.
  - **Range/conversion guards (audit 2).** The program aborts with ERROR (and the job is then not COMPLETE) if:
    - any input or computed bound is non-finite (this covers NaN from 0·∞ or ∞−∞);
    - any candidate range leaves [−2⁵², 2⁵²], so every integer↔double conversion is exact;
    - the node counter reaches 2⁶², or an allocation or write fails.
    The COMPLETE line reports max|z| and max|centre bound|. In the actual run max|z| = 23 and max|centre bound| = 21.2, far inside 2⁵².
- **Splitting by v = C·Γ49.**
  - Every slice is split into v = 0..10. Here v ≥ 0 is one of the constraints (Γ49 is a known curve).
  - For every slice a BOUND job certifies exactly that sup Γ49·x ≤ 10 on its real ellipsoid: f0_49 + √(R·S_49) ≤ 10, checked squared in Q. It records the rational witness (f0_49, R, S49).
  - The verifier recomputes this witness independently and requires exact equality. The three values are intrinsic to the real ellipsoid, so they do not depend on the basis used.
  - An a-priori bound also exists (auditor): Γ49² = −4, K·Γ49 = 4 and C² ≥ −10 give C·Γ49 ≤ 2 + √70 < 11 by Hodge.
- **Job status:** 1428 jobs (119 slices × (1 BOUND + 11 splits)) (`certified_results.jsonl`; verifier G).
  - The records are exactly the generated inventory, and every record carries the current producer id (a sha256 of the three producer files).
  - Every CONGRUENCE_EMPTY / EMPTY claim and every BOUND witness is recomputed independently.
  - All splits are COMPLETE, EMPTY or CONGRUENCE_EMPTY.
- **Result (1830 classes, all with n1 = n2 = 4; verifier F):**

| e | C² | C·E per line | m per cusp pair | count |
|---|----|--------------|-----------------|-------|
| 12 | −8 | all 12 lines: 1 | 6 pairs (1,1), a bijection σ between V and H lines | 64 |
| 12 | −4 | same | same | 32 |
| 8 | −8 | 0 on 4 lines, 2 on 8 lines | 2 pairs (2,2) | 192 |
| 8 | −8 | 0 on 2, 1 on 4, 2 on 6 | 2 pairs (2), 1 pair (2,2) | 384 |
| 8 | −8 | 1 on 8, 2 on 4 | 4 pairs (2) | 960 |
| 8 | −4 | 1 on 8, 2 on 4 | 4 pairs (1,1) | 192 |
| 8 | 0 | 0 on 4, 2 on 8 | 2 pairs (1,1,1,1) | 6 |

- There are no classes with e = 10 or 14–24, and none with n1 ≠ 4.
- e = 8 occurs only in the g = 1 jobs, as required by §1.

## 3. The e = 8 classes: equality, étale covers, Hecke
Let C be in an e = 8 class. By §1, g = 1 (g = 0 needs e ≥ 12). Then all the inequalities of §1 are equalities for both x and y:
- Σ_c k_c = 16 = Σ C·E_c + B.
- Hence each point of C̃ on some E_c has (C·E_c)_P = 1 and lies on no Exc, so ord_P(x − c) = 2.
- Each point meeting some Exc meets exactly one, with intersection 1, so ord_P = 1. Also B = e = 8.
- x and y are unramified outside the cusps.

**Double cover.** Let Y : w² = x(x⁴−1) be the Bolza curve, with σ its hyperelliptic involution. Let D̄ be the normalization of C̃ in C(C̃)(√h(x)), where h = h_1h_2h_3.
- This is the normalization of π⁻¹(C̄) in the FSM double cover X → B̄.
- On C̃, h(x)h(y) = Π g_j = (w_1w_2w_3)² is a square. So √h(y) ∈ C(D̄).
- D̄ → C̃ is branched exactly at the 8 points with odd ord h(x), namely the node points. So D̄ is connected, and 2g(D̄) − 2 = 8.
- f_1 = (x, √h(x)) and f_2 = (y, √h(y)) are maps D̄ → Y of degree 4. Both are **étale**:
  - at a node point (ord 1), D̄ → C̃ has index 2 and Y → X(4) has index 2;
  - at an E-point (ord 2), D̄ → C̃ is unramified and both points of D̄ have index 2 over X(4);
  - elsewhere x is unramified.
- Check: 8 = 4·(2·2 − 2).

**Hecke step** (#1842 §2–§3a, #1843 §6).
- Write Y = 𝔥/Γ_Y and D̄ = 𝔥/Γ_D, with Γ_D ⊂ Γ_Y of index 4 via f_1.
- f_2 lifts to g ∈ Comm(Δ) with gΓ_Dg⁻¹ ⊂ Γ_Y.
- If g ∉ Δ:
  - put K = Δ ∩ g⁻¹Δg and h = [Δ : K] ≥ 8;
  - Γ_Y acts transitively on Δ/K, so [Γ_Y : Γ_Y ∩ K] = h;
  - Γ_D ⊂ Γ_Y ∩ K, so h ≤ [Γ_Y : Γ_D] = 4. **Contradiction.**
- So g ∈ Δ = N(Γ_Y), and f_2 = α∘f_1 with α ∈ Aut(Y).

**Graph step.**
- α induces an octahedral Möbius map ᾱ on X(4) = Y/σ, and y = ᾱ(x) on C̃.
- So C is a component of f⁻¹(graph of ᾱ). For the cover of the graph ≅ P¹ given by the characters h_j(t)h_j(ᾱt) (verifier E), let r be its rank:
  - the components have degree 2^r over the graph, so n1 = 2^r;
  - their genus satisfies 2g − 2 = 2^{r−1}(B − 4).
- Over the 24 octahedral graphs, (r, B, g) is (0, 0, 0) ×4, (1, 4, 1) ×12 or (2, 6, 3) ×8.
- n1 = 4 forces r = 2, so g = 3 ≠ 1. **Contradiction.** ∎(e = 8)

## 4. The e = 12 classes: the image curve and exact algebra
Let C be in an e = 12 class with g ≤ 1. Put Z0 = f(C) ⊂ P¹×P¹ (irreducible), and m = deg(C̃ → Z̃0). Then Z0 has bidegree (4/m, 4/m), so m ∈ {1, 2, 4}.
- From the classes: on each vertical line ℓ_c, C·E_c = 1, and C meets exactly two nodes on ℓ_c, both with m = 1 and both over the same point (c, σ(c)). The same holds for horizontal lines.
- σ is a class-preserving bijection, since nodes lie only over same-class pairs.
- So the points of C̃ over ℓ_c are P_E (ord 2, or ord 3 if it lies on an Exc too) and N_1, N_2 (ord 1), with f(N_1) = f(N_2) = (c, σ(c)).
- The only points of S̃ over (c, σ(c)) lie on the 4 Exc curves there. So f(P_E) ≠ (c, σ(c)) unless P_E ∈ Exc.

**m = 4.**
- Z0 is the graph of a Möbius map μ through all 6 points (c, σ(c)). So μ permutes the cusps: it is octahedral and class-preserving, hence of rank 0.
- Then the components over it have degree 2⁰ = 1 ≠ 4. **Contradiction.**

**m = 2.**
- For P ∈ C̃, ord_P(x − c) = e_P·ord_{z(P)}(x − c), where e_P is the ramification index of C̃ → Z̃0. The points of Z̃0 over ℓ_c have total order 2.
- The ord pattern (3, 1) is impossible: 3 = e·o would need o = 3 > 2.
- So the pattern is (2, 1, 1):
  - N_1 and N_2 have e = 1. If they went to different points z_1 ≠ z_2, then P_E would map to one of them with e = 2, and that fibre would have degree 3 > 2.
  - So N_1 and N_2 map to one point z, unramified, and P_E is a ramification point.
- This gives one ramification point over each of the 6 vertical lines.
- Then 2g − 2 ≥ 2(2g(Z̃0) − 2) + 6 ≥ 2, so g ≥ 2. **Contradiction.**

**m = 1.**
- Z0 = {F = 0} with F of bidegree (4,4). C̃ → Z̃0 is birational, so (Z0·ℓ_c)_q = Σ_{P ↦ q} ord_P(x − c).
- (c, σ(c)) carries the two branches N_1 and N_2, so **F is singular at the 6 points (c, σ(c))**.
- F|ℓ_c = const·(t − σ(c))²·(t − r)², with r = σ(c) allowed. In words, F|ℓ_c is (t − σc)² times a square. The same holds on horizontal lines.
- Hence [F] lies in V(T_σ): F ∈ L_σ (singular at the 6 points), and the 12 discriminants of the residual quadratics vanish. Note that disc = 0 includes a double root at σ(c) or at ∞.

**Reduction of σ.**
- The class-preserving bijections form (Z/2)³. The Möbius ones, {id, −y, 1/y, −1/y} (verifier E: exactly the 4 class-preserving octahedral maps), form a subgroup of index 2.
- y ↦ μ(y) for these μ lifts to an automorphism of B̄, since h_j(μ y) = const·(square)·h_j(y).
- So up to symmetry σ ∈ {id, swap 0↔∞}.

**Exact algebra** (singular/, Singular 4.4.1 minAssGTZ over Q(i); the verifier rechecks the classification of every prime):
- **σ = swap** (dim L = 7): 3 minimal primes.
  - The square locus {G²}, with G a (2,2) form through the 6 points. It is closed and every member is non-reduced.
  - The point F = (x−y)(x+y)(xy−1)(xy+1), which is reducible.
  - The point **F\* = (x−y)⁴ + (x⁴−1)(y⁴−1)**.
- **σ = id** (dim L = 10): 17 minimal primes.
  - The square locus.
  - 16 primes (12 points and 4 conics) on which x − y divides F (an ideal-membership check). These are reducible.
- **F\***: its singular points are exactly the 6 points, all ordinary nodes (verifier C).
  - It is irreducible over Q(i) (verifier C), and absolutely irreducible (Singular absFactorize).
  - Independent argument (auditor): a nontrivial Galois-conjugate splitting over Q̄ would force at least 8 intersection nodes, contradicting the six-node count.
  - So its geometric genus is 9 − 6 = **3**.
- So for m = 1, C̃ ≅ Z̃0 has genus 3. **Contradiction.** ∎(e = 12)

The classes of §2 are exhaustive. So §3 and §4 prove the CLAIM.

## 5. Remark: F* lifts (not part of the claim)
- On F* = 0 the three g_j are squares: F* divides B_j² − 4(x−y)²g_j for explicit B_j (verifier D). For example, √(xy) = (x²y² − 1)/(2(x − y)).
- So f⁻¹(Z0*) splits into 8 curves of genus 3 with n = (4,4).
- The 4 non-Möbius matchings give 32 such curves. This matches the 32 classes with C² = −4, e = 12, but the class identification was not checked.
- Pitfall (32R-22): least-squares numerical searches converged only to the non-reduced square locus. This is why the exact primary decomposition is used.

## 6. Points to audit
1. §0: the formula f*ℓ_c = 2E_c + ΣExc_j, and its identification with the repository fibre class (lattice labels 33–44 / 93–140).
2. §1: the inequality chain, especially k_c ≤ C·E_c + B_c and Σ_c C·E_c = (6n1 − e)/2.
3. §2: the certified enumeration. Check:
   - the outward rounding (UP/DN) in certified_enum.c;
   - that each discard condition is implied by the bounds;
   - the exact UᵀDU / Cauchy–Schwarz data in certified_driver.py;
   - the BOUND certificates;
   - the generated inventory.
4. §3: the equality consequences, the étaleness of f_i, and the Hecke step (h ≤ 4 against h ≥ 8). Check that #1842/#1843 apply to any étale pair of degree n, not only the boundary setting.
5. §3: the identification of the α case with the octahedral graphs, and n1 = 2^r.
6. §4: the local analysis on cusp lines (cases P_E ∈ Exc), the m = 2 ramification count, and the reduction of σ to two types.
7. §4: the Singular primary decompositions (rerun singular/run_all.sh). The covering argument uses the fact that the square locus is closed.
8. Verifier scope: `verify_d8_low_genus.py` checks A–G of its docstring only. The enumeration and the Singular runs are reproduced by their own scripts.

## 7. Files
- `verify_d8_low_genus.py`: the exact checks A–G (sympy, numpy, repository lattice). Run `PYTHONUTF8=1 python verify_d8_low_genus.py`; it prints ALL PASS in a few minutes.
- `singular/`:
  - make_tangency_ideals.py writes tangency_{swap,id}.sing;
  - primes_{swap,id}.sing and fstar.sing are the Singular scripts, with logs *.log and dumps primes_*.txt.
  - `bash run_all.sh` reruns them (set -euo pipefail). It fails if Singular fails or an expected line is missing.
  - The order of primes in primes_id.txt can vary between runs, as can the sign or component chosen for the square-root elements in fstar.log (verifier D squares them).
- `enumeration/`:
  - certified_driver.py: exact slice data and exact leaf check;
  - certified_enum.c: the rigorous interval enumerator; build line in its header;
  - run_certified.py: the generated inventory and parallel runner (portable: `--repo`, `--enum CMD`);
  - certified_results.jsonl: one record per job.
  - The full rerun takes about 3 hours on 11 cores.

## 8. Changes after the first hostile audit (head 817845ce: FAIL)
- **Must-fix 1 (floating-point enumeration not certified).** Replaced by the certified enumeration of §2. The old fp_enum pipeline and its outputs were removed.
- **Must-fix 2 (verifier overstated).**
  - B now checks the square locus symbolically: G² makes every generator vanish identically, and the parametrisation has Jacobian rank = dim.
  - G now requires the result records to equal the generated inventory exactly, with the BOUND certificates.
  - The docstring lists precisely what is and is not checked.
- **Should-fix.**
  - The exact Γ49 bound replaces "≈ 9.3".
  - run_all.sh uses pipefail and validates its output.
  - The runners are portable.

## 9. Changes after the second hostile audits (head 05bb278b: FAIL by two auditors)
- **Must-fix: integer→double conversion not enclosed.** Auditor counterexample: centre 10¹⁸, which lost 72 solutions.
  - Repaired by the guards in §2: abort outside [−2⁵², 2⁵²], abort on non-finite values, check the node counter, check allocations and writes.
  - The counterexample input now aborts with ERROR. A small-centre version returns exactly the 201 solutions.
  - The whole enumeration was rerun with the guarded binary. No job aborted; max|z| per job is recorded.
- **Must-fix: verifier G trusted the BOUND flag.** BOUND jobs now record exact rational witnesses, and G recomputes them by an independent method:
  - G recomputes them and requires equality plus the inequality;
  - it independently re-derives every CONGRUENCE_EMPTY and EMPTY claim;
  - it checks that each record's fields match its job key.
- **Should-fix.**
  - Resumption reuses only records with the current producer id.
  - Range diagnostics are recorded.
  - The Cauchy–Schwarz comment now uses the maximum f + √(rem·S) < 0.
  - run_all.sh detects every "?" error line and every non-library "// **" warning; tested on a deliberately broken script.
