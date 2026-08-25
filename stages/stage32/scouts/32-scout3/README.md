# Stage32 scout3 — b12 Aut breaker optimization

Scout-only experiment. No controller change and no b12 numerical/theorem/receiver credit.

Trigger: Stage32-18D snapshot-restored b12 profile hit the 500,000,000-node cap after 1165.48s. The inherited 64 breakers were selected by hash spread rather than pruning efficacy.

This scout keeps the exact same Aut group, exact SHA-score canonical order, exact leaf canonicalization, source-locked fast enumerator, and snapshot parent-state restoration. It changes only which valid score inequalities are used during DFS and how many are retained.

The selector ranks all nonidentity Aut elements by how early and strongly their restricted score-difference row acts on the 63-coordinate DFS order, then tests 64 / 128 / 256 breaker bundles at b12 under the same 500M-node / 1800s resource envelope.

Every selected inequality is of the form `score(v) <= score(g v)` for an actual element `g` of the same order-1536 Aut group, so adding/reordering breakers cannot remove the true full-orbit score minimum. This is nevertheless scout evidence only because the traversal still contains floating radius/reach pruning. Any COMPLETE result must preserve the hostile-audited exact b10 predecessor set byte-for-byte.

Firewalls: `SCOUT_ONLY=true`, `D16_B12_NUMERICAL_CREDIT=false`, `SNAPSHOT_FAST_GLOBAL_COMPLETENESS_CERTIFIED=false`, `THEOREM_CREDIT=false`, `RECEIVER_CREDIT=false`, `FULL_D16_G0_ROW_COMPLETE=false`.
