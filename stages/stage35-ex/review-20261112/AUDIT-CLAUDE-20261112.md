# Audit of CONTINUATION-JUDGEMENT.md (Claude, 2026-11-12, main 38fe6416)

Status: reading audit. Proposal only. No STATE, ledger or credit change.

## Verdict: PASS. I agree with the recommendation to freeze Stage35-EX.

| Item | Verdict | Note |
|---|---|---|
| Script `check_e1_equivalence.py` | PASS | Reran. The identity H = e²+x²+y² holds. Small example: brick (280, 960, 1386). |
| Q5: E1 ⇔ no perfect cuboid | PASS | Matches my own check (29-08 audit and crosswalk). The word "weaker" in `MAIN-START-HERE.md` is wrong about strength. |
| Q2: line (a) cannot decide | PASS | (−1, F_B) lives in the finite H¹(Pic) part on an open U of the same Stoll–Testa surface. P0 is a smooth Q-point of S, so Stage33 Theorem 1 applies directly. The Master-Hit argument is only an outline, but the conclusion does not need it, because perfect cuboids are points of U itself. |
| Q3: −30 unconditional is out of reach | PASS | The prime count below 2^94 (≈3.0e26) is correct. The Odlyzko constants also check out: unconditional 4πe^{γ+r1/n} ≈ 23.9 and GRH 8πe^{γ+(π/2)r1/n} ≈ 49.7, with r1/n = 7/105. With rd ≈ 44.5, an unramified quadratic L of degree 210 can be excluded only under GRH. This is consistent with row381. |
| Q1: the reduction is incomplete (non-indexed) | PASS | `06-cross-lane.md` states this gap itself. This is the decisive point: even a full indexed closure would not give E1. |
| Q4: classification table | PASS as estimate | The degree-growth extrapolation uses two data points; it is labelled [estimate]. HIGH has the same shape as the Stage32 wall (finite for each fixed m, no bound on m). |

## Notes (not blocking)

1. Stage33 Theorem 1 and F2 have so far been audited only by Claude. Theorem 1 is a direct application of Harari's formal lemma (statement checked against Harpaz–Wittenberg, arXiv:1409.0993, §3), so the risk is low.
2. Part of the freeze rationale belongs in Stage35 MAIN as well: T35-R3-PHYS-EMPTY is also the full problem in disguise. Stage35 itself is already parked.
3. Results worth keeping as scoped and conditional: ±18, the listed Ward 3/5/7 exponents, +12, +30, −30 under GRH (row381, audited PASS_SCOPED_DEPENDENT), and the 155/197 lower bounds. Each is limited to "indexed points, the given exponent".

## Net

Freeze Stage35-EX. Restart only with one of these: a theorem that reduces non-indexed points to indexed ones, or a uniform upper bound for HIGH. Do not resume the P953 relation search or the (−1, F_B) local evaluation.
