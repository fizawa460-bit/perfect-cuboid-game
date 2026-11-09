# d = 16, all classes: no integral curve of geometric genus ≤ 1 (multibranch-only classes included)

Date 2026-11-09. Research logs: `logs/32R-97_D16_ALL_CLASSES_CLOSED.md` (and 32R-91 for the chain). Not audited.
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
*Proof.* M_p = Σ a_i Γ_{i,p} with a_i ≥ 0. The known curves are defined over Q(ζ₈) and reduce to the Γ_{i,p}; the
specialization map Pic(S̃_0) → Pic(S̃_p) is injective (smooth proper model over the local ring at p; both of rank 64
with the same lattice of known classes), so x = Σ a_i[Γ_i] in Pic(S̃_0). Hence D₀ = Σ a_i Γ_i is an effective divisor
in |x|_0. By upper semicontinuity h⁰_0(x) ≤ h⁰_p(x) = 1, so |x|_0 = {D₀}. If Σ a_i ≥ 2, D₀ is not integral. □
- It uses only h⁰_0 ≤ h⁰_p and the injectivity of specialization; it does not use the false implication "reducible
  mod p ⇒ reducible in characteristic 0" (R2 M1).
- Implementation (`code/d16all/mklg.py`): the residual Bp of the member (script_v2); every known curve Γ_k with
  Bp ⊆ I(Γ_k) is removed by saturation; if the remainder has dimension < 2 ("LG-ONLY-KNOWN"), M_p is supported on
  known curves together with the exceptional curves and the D-part.

**Lemma P (exact genus of a plane model).** If the residual R is integral over F_p, birational to its plane image of
degree e (checked as in T3: both generic projections have degree e = deg R), and the plane image f is irreducible
over F_p, then Σ g(components of R ⊗ F̄_p) ≥ (e − 1)(e − 2)/2 − Σ_P δ_P(f), the sum over **all** singular points
(Singular `deltaLoc` on the prime components of the affine singular scheme, in a chart whose line at infinity avoids
the singular locus). If f is absolutely irreducible this is the exact genus; if it splits over F̄_p into k conjugate
curves of genus g′, the right side equals kg′ − k + 1 ≤ kg′ (the Lemma G convention, R2 §2.2). (`code/d16all/mkgx.py`)

## 3. h⁰ = 1 (4,094 new classes, `code/d16all/`)
| verdict | count | argument |
|---|---|---|
| containment prefilter negative; member integral mod p; fast genus bound ≥ 2 | 3,112 | T3 + Lemma G (one component) |
| fast bound ≤ 1, then exact genus 3 | 4 | t_21: normal.lib genus of the P³ image; t_1967, t_2090, t_2091: Lemma P (Σδ = 102, e = 16) |
| fast tail gave up, member non-reduced: 2·R, R of degree 8, genus 3 | 14 | Lemma G (`mkrr.py`: components after removing known curves) |
| containment prefilter positive (964) + the same 14: known curves removed (`mklg.py`) → | 978 | |
| — remainder integral, fast bound ≥ 3 | 494 | Lemma G |
| — supported on known curves only | 470 | Lemma K |
| — remainder reducible: the 14 above | 14 | Lemma G |
Every new h⁰ = 1 class is closed. (The prefilter `fasth0v2.contained_curves` is used only to select jobs.)

## 4. h⁰ = 2 (118 new pencils, `code/p16all/`)
- 21 have a component Γ fixed in |x|_p (fixfilt rule). As in R2 §2.3 (T2′, `fix0/`), fixedness is checked in
  characteristic 0: exact h⁰ over Q(ζ₈) gives h⁰_0(D) = h⁰_0(D + Γ) = 2 for all 21 (`mkfix0.py`), so Γ is fixed in
  |x|_0 and |x|_0 has no integral member. 97 pencils remain;
  89 with two decompositions, 8 with one; `always_hidden` is empty for all 97 (the hidden set of R2 §2.5(i)).
- Critical stage: `p16/crit_tail_v6.sing` (32R-85 v6 = R2 pencil tail with the curve-fibre removal), 186 jobs, and 89
  Möbius jobs; stage 2 with fibre matching (`stage2m.py`, p_a = 1 + (C² + 16)/2): status ok for all 97; 305 heavy
  member jobs.
- Members (305): fast genus ≥ 2: 153 (T3 + Lemma G). The other 152: Lemma G by components (`mkcg.py`): Σg ≥ 2: 83;
  4 without a result were closed by the fast Lemma G of §3 (remainder genus 5); 65 have Σg ≤ 1 (unions of conics and
  at most one quartic): R2's normal-crossings check (`cnc/` procedure, `mknc.py`): NC-OK 36 (C_0 smooth by the NC
  lemma, g(C_0) = p_a ≥ 9); NC-BAD 29 → R2's analyzer (T7: `m16/tail.sing` data via `mkt7.py`, `m16/an2.py`): OK 28
  (bound 9–10), Lemma G 1.
- Reduced members not listed by stage 2 are covered by R2 §2.5(i) (the statement holds for all reduced char-p members).
- **Non-reduced members (R2 §4.5)** (`scan.py`, `gennr.py` = m16/gen.py on the new data): h⁰_p(D + 2Γ_k) for all 97
  pencils and all 140 Γ_k: 207 entries with h⁰ = 1, 234 'cap' (beyond the generator multiplicities of fasth0), none
  with h⁰ ≥ 2 (no one-parameter family of non-reduced members). All 441 entries were run as member jobs (the member is
  searched in the ideal of Γ_k with excess multiplicity, which needs no cap): no member 232; Lemma G 50; analyzer OK 159;
  FLAG / LOW / unfinished 0.
Every new pencil is closed.

## 5. h⁰ ≥ 3
No new class has h⁰ ≥ 3.

## 6. What an audit should check
1. Lemma K: injectivity of specialization of Pic for the smooth model S̃ over Z_(p) (with Q(ζ₈) ⊂ the residue
   extension), and that "LG-ONLY-KNOWN" means the member is supported on known curves and E_p.
2. Lemma P: the genus formula for plane curves with all singular points included; the chart choice; the conjugate-split
   case.
3. The reuse of the R2 tools on new data: script_v2 member ideals (T1), the v6 pencil tail and stage 2, the cnc
   procedure, the analyzer an2.py with data from m16/tail.sing (here with the member NN given instead of searched).
4. Completeness of the non-reduced scan: R2 §4.5 used exactly h⁰_p(D + 2Γ) for Γ among the 140 curves; the 'cap'
   entries are run directly.
5. That no step uses the odd-contact (unibranch-only) filter.
