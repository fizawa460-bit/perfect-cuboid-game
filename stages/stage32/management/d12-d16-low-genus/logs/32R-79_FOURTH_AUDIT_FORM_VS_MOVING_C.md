# 32R-79 — Fourth audit of R2 (HOLD): c of the forms vs c of the moving part

Date: 2026-11-05. Status: research log, local only (no ledger / STATE / credit / audit-master change).
Audit round 4: PASS for A3 (splitting), e = 3 fibre product (deg 1/2/3), old hub/loop withdrawal; conditional PASS M7.
MUST FIX: 28246 c ∝ u1 vanishes at the connectors Q1, Q2 (u1 = 0), against connector hypothesis (iii) c(Q) ≠ 0.

Answer: the e3h data c is the l^{oT} coefficient of the *forms* FL (degree-mm forms vanishing on the fixed curve
D = Σ DL[j]); hypothesis (iii) is about the moving part, c' = c / t_D.
Check `stoll/e3h/tr/` (t_*.sing = h_*.sing + trace block; fixed version reads DL via setring R):
for every D-curve DL[j], trace on E = std(satl(sb(DL[j]) + UJ) + l), saturated by (u1..u7); ZD = product;
compare with ZC = sat(EI + c). Result: TRACEMATCH 1 in all 16 files.
- 28246 m_29/30/118: 2 D-curves through node 17, traces (u1 = 0, u4 = ∓u7) = Q1, Q2 (connectors C3, C4 are D-curves
  with excess 1, COMP 3 2 1 1); c ∝ u1 ⇒ c' constant.
- 28246 s1_1_0_461, 28244 E17/E22: no D-curve through the node, c constant.
- 28244 E19: 4 D-curves, c ∝ u1 u7 = L M; E21: 2 D-curves, c ∝ u7 = L.
So (iii) holds for the moving part in all 16; ratios / normal form unchanged. R2: App. C.4(c) "Which c", R.5 table.
First run failed (Git Bash path conversion; then `DL` not visible in ring RL) — fixed, rerun, 0 errors.
