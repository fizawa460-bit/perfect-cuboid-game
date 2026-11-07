# 32R-77 — M7: the μ filter written into the R2 package

Date: 2026-11-05. Status: research log, local only (no ledger / STATE / credit / audit-master change).

- Question (user): route-E E03/E04 are merged — does M7 close?
- GitHub STATE (32-03, head 499d89c67): E02, E04 `EXECUTING_AUDIT_PASS_CONDITIONAL_ZERO_CREDIT`; E03
  `AUDIT_FAIL_FIXED_PENDING_RECHECK_ZERO_CREDIT` (round 2 must-fix: hypothesis "C̄ ⊂ B, d ≥ 1"; revision 2 not
  re-audited); E05 (the μ-filter corollary E05.1) `UNAUDITED_RESEARCH_NOTE_ZERO_CREDIT`.
- Done: E05.1 for d = 16 proved in full in R2 Appendix J (hypotheses checked: C̃ ≠ E_p since d ≥ 1; d ∉ {2, 4};
  r even, r ≤ M = μ since C̃·E_p ≥ 0). Recomputed μ for the 23 nets / webs of `n16/plan.json` with exact integers
  (`stoll/mu_nets.py` → `stoll/mu_nets.out`, PASS): μ = 16 for exactly 13 (9379, 25329, 27523, 27685, 27769, 27986,
  28244, 28386, 28525, 28760, 28997, 46958, 58647); μ = 18 for 3, μ = 20 for 7 (closed otherwise, §4.4).
  Agrees with `stoll/mu_filter.py` / E05 §1.
- M7 status: reduced to one external item, the re-audit of E03 revision 2. Closes when that passes.
- Follow-up (user: put E03 into this md and re-audit together): R2 Appendix K reproduces E03 (1) (the only part used;
  d = 16 ≤ 85) with its standing hypothesis and full proof (E02 §2–§3 steps, class-independent). M7 now closes if
  App. J–K pass the 32-02 re-audit; recording that as an E03 rev 2 re-audit on GitHub STATE is the user's decision.
