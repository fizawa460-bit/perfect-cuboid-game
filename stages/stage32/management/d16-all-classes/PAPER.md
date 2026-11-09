# d = 16, all classes: no integral curve of geometric genus ≤ 1 (multibranch-only classes included)

Date 2026-11-09, revision 3 (answers to the reading audits round 1, HOLD at a821e14f, and round 2, HOLD at 4349cac6; §7). Research logs:
`logs/32R-97_D16_ALL_CLASSES_CLOSED.md` (and 32R-91 for the chain).
Zero credit. Companion of the audited leaf `management/d12-d16-low-genus/` (#1852, "R2"), whose tools and notation
(PAPER-R2.md: T1–T7, Lemma G, §2.5, §4.5, Appendices A–D) are used throughout and are not re-proved here.

## 0. Claim
Let S̃ be the minimal resolution of the cuboid surface S, K = K_S̃, d = K·C.

**Claim D16.** Every integral non-exceptional curve C ⊂ S̃ with d = 16 has geometric genus ≥ 2.

- R2 proved this for the classes of the 71,697 unibranch-compatible representatives (for every integral curve in them,
  unibranch or not). This leaf treats the remaining 1,665,666 representatives ("new classes"). Together: all classes.
- With R2 (d = 12, 14 all classes) and the leaves d8 (#1844), d10 (#1845): **no integral curve of degree ≤ 16 and
  geometric genus ≤ 1 except the known ones** (degree 2, 4; E04).

Characteristic-p computations are mod p = 10009 throughout; the directions used are those of R2 §2: h⁰_p ≥ h⁰_0,
g_p ≤ g_0 (Lemma G, T3), statements about all char-p members (§2.5), and Lemma K below.

## 1. Classes (`code/split/chain16all.sh`, `code/d16all/split_new.py`)
| step | count | method |
|---|---|---|
| geometric representatives, d = 16 | 1,737,363 | split enumeration (32R-60, R2 §1), all reps |
| after the μ filter E05.1 | 1,309,867 | `mu1820/mupre.py` (E05.1 audited) |
| GLPK h⁰ judge | h⁰ = 0: 1,302,306; 1: 7,174; 2: 371; 3: 15; none: 1 | `fasth0/judge_glpk.sh` (R2 T1) |
| of these, new classes (not in `s16sym`) | h⁰ = 0: 1,236,251; 1: **4,094**; 2: **118**; ≥ 3: 0 | `split_new.py` |
- The single "none" class (no decomposition with m ≤ 3) is an old one (R2 §4.1, rep 50489); recomputed with m = 4:
  h⁰ = 0 (`code/m4_16/`).
- The odd-contact filter 32R-83 is **not** used (it is valid only for unibranch curves).

## 2. Two arguments not in R2
**Lemma K (support on known curves).** Let x be a class with h⁰_p(x) = 1, and suppose the unique member M_p of
|x|_p is supported on known curves (the 92 known curves and the 48 E_p). Then |x|_0 contains no integral curve, unless
x is the class of a single known curve.
*Proof.* At p = 10009 the reduction S_p is again a complete intersection of four quadrics whose singular locus is
exactly 48 A₁ points (p ≡ 1 mod 8, ζ₈ ↦ 792 with 792⁴ ≡ −1), so S̃ has a smooth proper model over the local ring, and
the 140 known curves (defined over Q(ζ₈)) reduce to the Γ_{i,p}. Write M_p = Σ a_i Γ_{i,p} (a_i ≥ 0) and
v = x − Σ a_i[Γ_i] ∈ Pic(S̃_0). Its specialization is 0, and **intersection numbers are preserved by specialization**
(a separate fact from semicontinuity), so v·Γ_j = 0 for all 140 known curves. The Gram matrix of the known classes is
non-degenerate of rank 64, hence v is numerically trivial; Pic(S̃_0) is torsion free and equals Num (S is a complete
intersection and S̃ its resolution of nodes: π₁ = 1, q = 0), so v = 0 and x = Σ a_i[Γ_i]. Thus D₀ = Σ a_i Γ_i is an
effective divisor in |x|_0. By upper semicontinuity h⁰_0(x) ≤ h⁰_p(x) = 1, so |x|_0 = {D₀}. At d = 16 every known
curve has K·Γ ∈ {0, 2, 4}, so Σ a_i ≥ 4 and D₀ is not integral. □
- The only semicontinuity used is h⁰_0 ≤ h⁰_p; the other input is the preservation of intersection numbers. No
  statement of the form "reducible mod p ⇒ reducible in characteristic 0" (R2 M1) is used. (Revision 2: the earlier
  phrase "both of rank 64" is withdrawn; the Picard number of S̃_p may be larger and is not needed.)
- Implementation (`code/d16all/mklg.py`): the residual Bp of the member (script_v2); every known curve Γ_k with
  Bp ⊆ I(Γ_k) is removed by saturation; if the remainder has dimension < 2 ("LG-ONLY-KNOWN"), M_p is supported on
  known curves together with the exceptional curves and the D-part.

**Lemma P (exact genus of a plane model).** If the residual R is integral over F_p, birational to its plane image of
degree e (checked as in T3: both generic projections have degree e = deg R), and the plane image f is irreducible
over F_p, then Σ g(components of R ⊗ F̄_p) ≥ (e − 1)(e − 2)/2 − Σ_P δ_P(f), the sum over **all** singular points
(Singular `deltaLoc` on the prime components of the affine singular scheme, in a chart whose line at infinity avoids
the singular locus; the chart coefficient c₀ ≠ 0 is assumed, and a zero would only stop the job). If f is absolutely irreducible this is the exact genus; if it splits over F̄_p into k conjugate
curves of genus g′, the right side equals kg′ − k + 1 ≤ kg′ (the Lemma G convention, R2 §2.2). (`code/d16all/mkgx.py`)

## 3. h⁰ = 1 (4,094 new classes, `code/d16all/`)
Selection (`prep_h1.py`): all 4,094 classes pass x·E ≥ 0 and μ ≥ 18; the containment prefilter
(`fasth0v2.contained_curves`) only splits them into 3,130 fast-genus jobs and 964 "contained" classes.

| verdict | count | argument |
|---|---|---|
| fast genus bound ≥ 2 (member integral mod p) | 3,112 | T3 + Lemma G (one component) |
| fast bound 1, exact genus 3: t_21 | 1 | normal.lib genus of the birational P³ image (degree 16 = deg R; `mkg3.py`) |
| fast bound 1, exact genus 3: t_1967, t_2090, t_2091 | 3 | Lemma P (Σδ = 102, e = 16; `mkgx.py`) |
| fast tail gave up (non-reduced members) | 14 | treated with the 964 below |
| 964 + 14 = 978, known curves removed (`mklg.py`, `tally_lg.py`): remainder integral, fast bound ≥ 3 | 494 | Lemma G (the remainder alone has genus ≥ 3: bounds 3: 108, 4: 69, 5: 243, 6: 65, 7: 9, `results/lg_remainder_bounds.txt`) |
| — supported on known curves and E_p only | 470 | Lemma K (no use of the genus of the known quartics) |
| — remainder reducible (the 14 classes 666–679) | 14 | Lemma G by components (`mkrr.py`): Σg = 3 (`results/rr_results.txt`) |

3,112 + 1 + 3 + 978 = 4,094. Every new h⁰ = 1 class is closed.

## 4. h⁰ = 2 (118 new pencils, `code/p16all/`)
**4.1 Fixed components (21).** A component Γ fixed in |x|_p (fixfilt rule) is checked in characteristic 0 as in R2
§2.3 (T2′): exact h⁰ over Q(ζ₈) gives h⁰_0(D) = h⁰_0(D + Γ) = 2 for all 21 (`mkfix0.py`, `results/fix0_char0.txt`;
all Γ are exceptional curves E_p). So Γ is fixed in |x|_0 and |x|_0 has no integral member. 97 pencils remain (89 with
two decompositions, 8 with one).

**4.2 Critical stage.** `p16/crit_tail_v6.sing` (32R-85, later than R2; not an R2 tool) on 186 jobs, 89 Möbius jobs,
stage 2 with fibre matching (`stage2m.py`, p_a = 1 + (C² + 16)/2): status ok for all 97; 305 member jobs.
- **Fibres removed whole by v6 (audit MUST FIX).** v6 removes a fibre containing a critical curve, arguing that the
  member is non-reduced. That is a char-p statement and cannot exclude a characteristic-0 curve reducing to it (the M1
  pattern). It happened in 61 of the 186 jobs: 81 removed members. All 81 were run as member jobs
  (`audit_r1_steps.py rf`; the 186 critical outputs contain exactly 81 'removed whole' lines, all with a linear
  factor u ± c, `results/b_removed_fibres.txt`): Lemma G by components 23; Σg ≤ 1: 58, every component a known curve (§4.5), of which
  NC-OK 38 and analyzer (T7) OK 20 (`results/b_removed_fibres.txt`).

**4.3 Members of stage 2 (305).** Fast genus ≥ 2: 153 (T3 + Lemma G). The other 152: Lemma G by components (`mkcg.py`)
Σg ≥ 2: 83; 4 without a result: known curves removed, remainder genus 5 (`mklg.py`); 65 with Σg ≤ 1 (unions of conics
and at most one quartic, every component a known curve, §4.5): NC-OK 36 (R2 C.3: C_0 smooth, g(C_0) = p_a ≥ 9);
NC-BAD 29 → analyzer (T7; data from `m16/tail.sing` with the member NN given, `mkt7.py`): OK 28 (bounds 9–10),
Lemma G 1 (the tail also lists the excess D-curves, so its SIGMAG can exceed the Σg of the residual alone).

**4.4 The rest of R2's pencil procedure (audit MUST CHECK (c)).** R2 §2.5(i) covers reduced members not listed by
stage 2 only together with R2's further checks; they are now run on the 97 pencils with R2's scripts
(`hidden_check.py`, `hidden_pts.py`, `basepts.py`, `node_jobs.py`, `stage2b.py`, paths p16 → p16all; node profile
`pencil_profile.json` from Pn·x), `results/c_hidden_base_node.txt`:
- hidden set H = ∩_D (∪ hidden curves of D) off the nodes (point-wise): empty for 44 pencils, non-empty for 53 →
  hidden-point fibres (`hidden_pts.py`): for all 53, no hidden point on the chart hyperplane (dim −1) and finitely
  many members through the hidden points (dim 0), 105 special factors (`results/c_hidden_points.txt`);
- base points off the nodes: none 73, all simple 24 (no member singular at a base point);
- nodes with x·E ≥ 2 (every one of the 97 pencils has such nodes, 281 in total): blow-up charts, 562 jobs; the 4 jobs
  with "ramification not finite" were redone with R2's direct version (`nt_`, `mknt.py`; cE = multiplicity of the node
  in D, the division by s^cE is checked; R2's template is included as `code/p16all/R2_nt_template_27522_122_1.sing`):
  special factor u = −329 each;
- stage 2b, the special members (node branch values, hidden-point fibres, and u = ∞): 606 jobs; every one of the 97
  pencils has special factors, so the u = ∞ member (F1) was run for all 97 (97 F1 jobs);
  (`results/c_stage2b_accounting.txt`): fast ≥ 2: 509; quadratic factors as one member over F_p(w): 12 (bounds 8–10);
  known curves removed, remainder genus ≥ 2: 30; supported on known curves: NC-OK 20, analyzer OK 26 + Lemma G 9.
  Open: 0.

**4.5 Identification of components with known curves (audit MUST CHECK (d)).** Every member sent to the NC check or
the analyzer has all components equal to known curves (containment of the known-curve ideal and equal degree;
`audit_r1_steps.py idc`, `results/d_identification.txt`): the 65 + 58 members of §4.2–4.3 and 176 of the 209 non-reduced
members of §4.6; members found supported on known curves by `mklg` are so by construction. The other 33 non-reduced
members contain an unknown component of degree 8 or 12 and are closed by Lemma G alone (Σg = 3–5); the analyzer is not
used for them. (The m16 tail declares an int b1 that shadows the ring variable b1, as noted in R2; the identification
jobs kill it first.)

**4.6 Non-reduced members (R2 §4.5).** h⁰_p(D + 2Γ_k) for all 97 pencils and all 140 Γ_k (`scan.py`): 207 entries
with h⁰ = 1, 234 'cap' (all at nodes). All 441 entries run as member jobs (`gennr.py` = m16/gen.py): the order c0 of the
generic member equals D_k in all 441 cases (`audit_r1_steps.py c0`, `results/e_c0_vs_Dk.txt`), so the search at order
c0 + 2 is exactly "excess ≥ 2", and a family of non-reduced members would appear as MEMBERDIM ≥ 2 (none: MEMBERDIM 0:
232, 1: 209). Results: no member 232; Lemma G 50; analyzer OK 159.

**4.7 Generic member in the T7 jobs (audit MUST CHECK (f)).** Every T7 job (29 + 20 + 35) checks that F0 and F0 + 7F1
have exactly the multiplicities DLc along all D-curves and that NN ≠ F0: 84 × EXG-CHECK OK
(`results/f_generic_member_checks.txt`). The same check on the 159 analyzer cases of the non-reduced scan (§4.6, random
  generic member FL[1]): 159 × EXG-CHECK OK (`results/f_generic_member_checks_nr.txt`).

Every new pencil is closed.

## 5. h⁰ ≥ 3
No new class has h⁰ ≥ 3.

## 6. What an audit should check
1. Lemma K and Lemma P (§2).
2. The reuse of R2 tools on new data, including the substitution of the given member NN into `m16/tail.sing` (§4.3).
3. The answers of §4.2 (v6 removed fibres), §4.4 (hidden / base / node / stage 2b), §4.5–4.7.
4. That no step uses the odd-contact (unibranch-only) filter.

## 7. Audit history
- **Round 1** (external hostile reading audit, head a821e14f): HOLD. PASS: Lemma K, Lemma P, the h⁰ = 1 table, the 21
  fixed-component pencils. MUST FIX: the v6 whole-fibre removal (M1 pattern) → §4.2 (81 members run and closed).
  MUST CHECK: (c) R2's hidden / base-point / node checks → §4.4; (d) identification with known curves → §4.5; (e) cap
  entries, c0 vs D_k → §4.6; (f) generic member F0 in T7 → §4.7; t_21 generator and birationality → §3 (`mkg3.py`;
  the P³ image has degree 16 = deg R); split_new output → `results/split_new.txt` (s16sym = the 71,697 representatives
  of R2). SHOULD FIX: Lemma K wording (§2); c₀ ≠ 0 (§2); the h⁰ = 1 table and the log made consistent (§3); v6 is
  32R-85, not an R2 tool (§4.2); the prep_all.py docstring corrected.
- **Round 2** (head 4349cac6): HOLD with a narrow scope; no mathematical error, no M1 pattern. (b), (d), (e), (f) PASS.
  MUST CHECK 1: 81 'removed whole' lines in the 186 outputs, all linear (§4.2). MUST CHECK 2: F1 jobs for all 97
  pencils (§4.4). MUST CHECK 3: `mknt.py` now contains the generator (it regenerates the 4 nt_ files byte for byte)
  and R2's template is attached. SHOULD FIX: hidden-point evidence (§4.4), the generic-member check on the 159
  analyzer cases of §4.6 (§4.7), the bound distribution of the 494 (§3), the log table (32R-97).
- **Round 3** (head 6e22aef1): **PASS** (reading level). The three completeness checks and four should-fix items of round 2
  are resolved; no remaining item. Singular outputs were not re-executed (the audit relies on the submitted tallies).
  Combined with R2, d8 (#1844) and d10 (#1845): no integral curve of degree ≤ 16 and geometric genus ≤ 1 other than
  the known ones (degree 2, 4; E04), at reading level. No credit flag is changed.
