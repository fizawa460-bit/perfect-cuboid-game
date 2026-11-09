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
| member integral mod p, fast genus bound ≥ 2 | 3,113 | T3 + Lemma G (one component); includes t_21: exact genus 3 |
| exact genus 3 of the plane model (t_1967, t_2090, t_2091) | 3 | δ summed over all singular points of the birational plane image (deltaLoc), g = 105 − 102 |
| known curves removed, remainder integral, fast bound ≥ 5 (Σg ≥ 3) | 494 | Lemma G |
| support only known curves, ≥ 2 of the 60 quartics (genus 1, R2 convention) | 173 | Lemma G |
| support only known curves, ≤ 1 quartic | 297 | Lemma K (below) |
| non-reduced: 2·(genus-3 curve of degree 8) | 14 | Lemma G |

**Lemma K.** If the unique member M_p of |x|_p is supported on known curves (the 92 curves and the 48 E_p), then x is
a non-negative combination of known classes (specialization Pic(S̃_0) → Pic(S̃_p) is injective), so that combination
is an effective divisor of |x|_0; h⁰_0(x) ≤ h⁰_p(x) = 1, hence |x|_0 consists of that reducible divisor and contains
no integral curve (x is not itself a known curve: total multiplicity ≥ 2). Uses only h⁰_0 ≤ h⁰_p, not the M1-type
"reducible mod p ⇒ reducible".

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
