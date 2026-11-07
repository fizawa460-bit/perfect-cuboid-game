# 32R-78 — Third audit of R2 (HOLD): A3 splitting, e = 3 hub degrees, document cleanup

Date: 2026-11-05. Status: research log, local only (no ledger / STATE / credit / audit-master change).
Audit: independent PAPER AUDIT, round 3, HOLD. Items: A3 geometric irreducibility (MUST FIX), e = 3 hub (MUST CHECK),
history mixed with proof (DOCUMENT FIX). PASS: counts, C5, Lemma G, App. K (given F1–F3), App. J (given E04).

1. A3. The auditor is right that separable ⇒ geometrically reduced only. Irreducibility is not needed:
   Σ over connected components of (g − 1) ≥ Σ_j (h_j − 1) over the k̄-irreducible components (one Shilov point each),
   and for v^m = f the sum Σ_j (2h_j − 2) is the Riemann–Hurwitz sum of the whole cover. `an2.py` uses only
   c·(g′ − 1) (line 266, `tot += vv[0]*vv[1] - vv[0]`; vv[0] is used nowhere else), and k is counted on the model
   graph. So no bound changes and no re-run is needed. R2 App. B A3 rewritten (A3.1, A3.2).
2. e = 3 hub. deg g = 1 / 2 / 3 separated (deg 1: automorphism, fibre product ≅ E). Data check `stoll/e3h/shapes.py`
   → `shapes.out`: all 16 h_*.out OK (BE = L M c, AA = κ L M² c, GA = κ′ L c or 0; Q1 ≠ Q2; M has 2 distinct zeros on
   E; no common zero of L and M; c vanishes only on L M = 0). 28246: GA = 0 (no l¹ term) ⇒ deg g ∈ {2, 3};
   L = u1, M = u7, E: u1² + u4² = u7².
3. Document. App. D: v4 rules stated as the only rules used; v1–v3 marked history; round-2 answer marked superseded;
   §2.6 bound formula now with k; §4.4 / §4.5 cite analyzer v4 for 28246 dm_1_0 / 28255 / 28760; App. E, F headed
   "consistency check only". New R.4 response table.
