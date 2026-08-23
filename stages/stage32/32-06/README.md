# Stage32-06 — d=4, g=0 exact MITM pilot

This is a bounded Stage32-main-batch continuation after merged Stage32-05.

It does **not** generalize the d=6 fixed-weight MITM blindly to the full d<=176/192 windows. The current exact dual caps give, at d=4,

- each of the 92 nonexceptional intersections <=2;
- each of the 48 exceptional intersections <=1.

Thus the exceptional block is still genuinely binary and the Stage32-05 fixed-weight split remains exact there.

The selected-normal q-tail is different: legal values are now 0..2, while Stage32-05 used 0..3 and therefore spanned the full order<=4 q-tail subgroup. Stage32-06 deliberately keeps the HNF subgroup quotient only as a **necessary over-relaxation**. It may admit extra candidates, but cannot discard a legal d=4 candidate. Every admitted exceptional candidate is then checked with the exact 16-variable QF_NIA system using the true 0..2 normal bounds, all 140 intersection bounds, all 64 mod-8 lattice-image congruences, fixed degree/mass identities, and the exact adjunction inequality.

Pilot parents are chosen from the exact aggregate-feasible d=4,g=0 set:

- e=0, a=30;
- e=5, a=14;
- e=10, a=0.

Success means all three close exactly with zero survivors and no UNKNOWN. If that happens with tractable candidate counts, the next main-batch may expand to the full exact aggregate-feasible d=4,g=0 parent list. Failure or timeout stops the expansion and records the smaller Class-2 computational wall.

Firewalls remain unchanged:

```text
THEOREM_CREDIT=false
AUDIT_STATUS=PENDING
RECEIVER_CREDIT=false
LOW_DEGREE_PREFIX_COMPLETE=false
FULL_D176_D192_NUMERICAL_ORBIT_CENSUS=false
R29_LG2=NOT_DISCHARGED
R29_LG2_EFF=NOT_DISCHARGED
R29_LG2_MB=NOT_DISCHARGED
G10_LOWGENUS_PICARD=AMBER
```
