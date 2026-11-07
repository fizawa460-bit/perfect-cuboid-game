# 32R-80 — Fifth audit (reading audit of R2): PASS, conditional; four should-fix items

Date: 2026-11-06. Status: research log, local only (no ledger / STATE / credit / audit-master change).

Verdict received: PASS (conditional). All round-2 MUST FIX / MUST CHECK items are accepted, as are the new parts
(hub repair, A3 revised, §4.7, App. J–K). M7 is accepted as closed by App. J–K together with E04.
The auditor withdrew their own round-2 acceptance of the one-vertex hub model.
The condition: logs 32R-75…79 and the computations (881 members, μ values, etc.) were not re-executed.

Should-fix items, all wording only (R2 §R.6):
1. Stale wording (App. D "Bad directions", §2.6, §7 Q3 and Q5): rewritten to match App. D item 2 and A2 (revised).
2. App. B "how it is used": the bound is now stated with k(G′) = number of connected components; +1 stays valid.
3. App. C.4 last item (e = 3 crossing tubes, from App. F): marked as not used by the v4 certificate. Checked in
   `m16/an2.py`: the bad Z-component makes `ok_edge_dir` False. Such a crossing counts only through REFINE
   (both multiplicities 1) or as a hub connector edge.
4. §2.5(i) δ ≤ μ in char p: Deligne, SGA 7 XVI, gives μ ≥ 2δ − r + 1; with δ ≥ r − 1 this gives μ ≥ δ.

No bound or count changed.
