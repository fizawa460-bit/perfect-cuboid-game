# Stage32-18AN — p436/s5 progressive breakthrough scout

Target: the single remaining wall `p436/s5`.

This stage replaces COMPLETE-only short scouting with a high-recall progressive scout. Every weapon is measured at 1M, 3M and 6M exact DFS nodes. A three-point baseline is included strictly as a control. The primary structural progress metric is `split_prefixes_seen / nodes`: how much of the exact secondary-prefix work has actually been consumed for the same node budget.

Weapons:
- `baseline` — AF scheduler 1.0, control only;
- `pair-capcap` — exact two-constraint cap/cap Gram-KKT lower bound;
- `triple-cap` — exact 3x3 cap-only active set;
- `triple-sym` — exact 3x3 symmetry-only active set;
- `triple-mixed` — exact 3x3 mixed cap/symmetry active set.

Classification:
- `BREAKTHROUGH`: exact COMPLETE at any checkpoint;
- `PROMISING`: not COMPLETE, but structural prefix progress per node is at least 1.10x baseline at at least two checkpoints;
- `NO_SIGNAL`: neither condition.

PROMISING is not a winner and gives no numerical credit. It only prevents a potentially useful 2x-ish weapon from being discarded because a short scout did not finish the whole wall.

Aut is not treated as a new family here: the immutable b16 source already contains 256 exact Aut-derived symmetry breakers. Existing failed families are recorded in `weapon-history.md` to prevent name-churn loops.

No finer splitting. All numerical/theorem/receiver/controller firewalls remain false.
