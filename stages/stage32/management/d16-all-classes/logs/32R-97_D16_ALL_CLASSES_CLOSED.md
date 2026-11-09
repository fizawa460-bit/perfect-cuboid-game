# 32R-97 — d = 16, all classes (multibranch included): no new curve of geometric genus ≤ 1 (2026-11-09)

Zero credit, working note; not audited. Status 2026-11-09: complete (no open case). Together with the R2 package (d = 12, 14 all classes; d = 16 unibranch-
compatible classes, every integral curve) this gives: **no integral non-exceptional curve of degree ≤ 16 and geometric
genus ≤ 1 other than the known ones** — pending an audit of this note.

## Pipeline (all d = 16 reps, `split/chain16all.sh`)
- Enumeration: split enumeration (32R-60 method, R2-audited), 1,737,363 geometric reps (`/root/s16all`).
- μ prefilter E05.1 (audited): 1,309,867 kept (`/root/s16allmu`).
- GLPK h0 judge (`fasth0/judge_glpk.sh`, R2 method): h0 = 0: 1,302,306; 1: 7,174; 2: 371; 3: 15; none: 1.
- Split against the unibranch-compatible reps (`/root/s16sym`, already closed by R2): new classes with h0 > 0:
  h0 = 1: 4,094; h0 = 2: 118; h0 ≥ 3: 0. The single "none" class is an old one (R2 §4.1, m = 4 gives h0 = 0;
  recomputed here: h0 = 0, `m4_16/`).
- No odd-contact filter (32R-83 is unibranch-only).

## h0 = 1 (4,094 classes, `d16all/`)
| verdict | count | argument |
|---|---|---|
| member integral mod p, fast genus bound ≥ 2 | 3,112 | T3 + Lemma G (one component) |
| fast bound 1: t_21, exact genus 3 (normal.lib, P³ image, `mkg3.py`) | 1 | T3 + Lemma G |
| fast bound 1: t_1967, t_2090, t_2091, exact genus 3 (Lemma P) | 3 | δ summed over all singular points of the birational plane image (deltaLoc), g = 105 − 102 |
| 964 contained + 14 non-reduced = 978, known curves removed (`mklg.py`): remainder integral, fast bound ≥ 3 | 494 | Lemma G (bounds 3: 108, 4: 69, 5: 243, 6: 65, 7: 9) |
| — supported only on known curves and E_p | 470 | Lemma K (all of them; no use of the genus of the known quartics) |
| — remainder reducible: 2·(genus-3 curve of degree 8) | 14 | Lemma G by components (`mkrr.py`) |
3,112 + 1 + 3 + 978 = 4,094.

**Lemma K.** If the unique member M_p of |x|_p is supported on known curves (the 92 curves and the 48 E_p), then x is
a non-negative combination of known classes (the difference has zero specialization, hence zero intersection with all
known classes, hence is 0 since the known Gram matrix is non-degenerate and Pic(S̃_0) is torsion free), so that
combination is an effective divisor of |x|_0; h⁰_0(x) ≤ h⁰_p(x) = 1, hence |x|_0 consists of that reducible divisor
and contains no integral curve. Uses only h⁰_0 ≤ h⁰_p and the preservation of intersection numbers.

## h0 = 2 (118 pencils, `p16all/`)
- 21 with a fixed component (fixfilt rule; checked in char 0 by exact h0 over Q(zeta_8), R2 T2′: h0_0(D) = h0_0(D + Γ) = 2 for all 21, p16all/mkfix0.py); 97 pencils → 186 critical jobs + 89 Möbius jobs (p18 pipeline, v6 tail,
  pa = 1 + (C² + 16)/2) → 305 member jobs (stage2m).
- Members: fast genus ≥ 2: 153; Lemma G (components, cg_): 83; fast Lemma G (known curves removed, remainder genus 5):
  4; the 65 members made of conics and ≤ 1 quartic: normal-crossings check (R2 `cnc/` procedure) OK 36, and the 29
  NC-BAD ones closed by the R2 analyzer (`m16/an2.py`, data from `m16/tail.sing`): OK 28 (bound 9–10), Lemma G 1.
- Reduced members not listed by stage 2: §2.5(i) of the R2 package (the visibility argument on all reduced members).

## Not done here / caveats
- Lemma K and the "all singular points" exact genus are new (not in R2); everything else reuses R2-audited tools.
- **Non-reduced members (R2 §4.5), done 2026-11-09** (`p16all/scan.py`, `p16all/gennr.py` = m16/gen.py on the new
  data, `p16all/nr/`): h⁰_p(D + 2Γ_k) for all 97 pencils and all 140 Γ_k: 207 entries with h⁰ = 1, 234 'cap', none
  with h⁰ ≥ 2 (no one-parameter families). All 441 member jobs (member found inside the ideal of Γ_k with excess
  multiplicity, as m16/tail.sing): no member 232; Lemma G 50; R2 analyzer (an2.py) OK 159; FLAG / LOW / unfinished 0.
- Pencil plans: always_hidden empty for all 97; stage 2 status ok for all 97.
- **So every class of degree 16 is closed** (modulo an audit of: Lemma K, the all-singular-points genus, and the reuse
  of the R2 tools on the new data).

## Audit round 1 (2026-11-09): HOLD, answered
External reading audit (head a821e14f): PASS for Lemma K, Lemma P, h⁰ = 1, the 21 fixed-component pencils; HOLD for
the 97 pencils. Answers (leaf PAPER.md revision 2, §4.2–4.7): v6 whole-fibre removal (81 members) run and closed;
R2's hidden-set / base-point / node checks and stage 2b (606 special members) run, open 0; identification of
components with known curves (299 all known, 33 closed by Lemma G); c0 = D_k for all 441 scan entries; 84 T7 jobs
with the generic-member check OK. The h⁰ = 1 counts are 3,112 + 1 (t_21) + 3 (Lemma P) + 978 (494 + 470 + 14).

## Audit round 2 (2026-11-09): HOLD (narrow), answered
No mathematical error. Completeness checks: 81 removed-whole lines (all linear), F1 jobs for all 97 pencils, mknt.py
generator (regenerates the 4 nt_ files identically); plus hidden-point evidence, 159 more generic-member checks, the
bound distribution of the 494 (leaf PAPER.md revision 3).
