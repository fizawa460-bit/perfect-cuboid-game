# Stage19 post-Stage24 checkpoint50 supersession

STATUS=POST_STAGE_SUPERSESSION_ADDENDUM
SOURCE_STAGE=Stage24
SOURCE_CHECKPOINT=50
SOURCE_PR=976
SOURCE_AUDIT=stages/stage24/24-50/audit.md

This addendum updates the **current consumer-facing lower interface** for Stage19 without rewriting the historical meaning of the frozen Stage19 audits. The Stage19 final bundle was correct when audited: at that time only the finite floor `N2(B)>=3495` was certified and unboundedness was unresolved.

Stage24 checkpoint50 later supplies materially new input by reopening the Stage15-2 algebraic formula outside its historical odd/odd parity specialization. Fresh Stage24 audit accepts the mixed-parity quartic lift

\[
p^4+q^4=17Z^2
\]

and the resulting primitive canonical exactly-two construction.

The current lower interface is therefore

\[
\boxed{N_2(B)\gg\sqrt{\log B}},
\]

so in particular `N2(B)->infinity` and an infinite primitive Stage19 construction are now certified.

The finite floor remains true but is no longer the strongest lower interface. No positive power of `B`, matching half-power lower bound, true exponent, or perfect-cuboid conclusion follows.

```text
HISTORICAL_STAGE19_AUDIT_REVOKED=false
HISTORICAL_CONSTANT_FLOOR_STILL_TRUE=true
CURRENT_STAGE19_LOWER_BOUND=N2(B)>>sqrt(log B)
STAGE19_UNBOUNDEDNESS_PROVED=true
INFINITE_PRIMITIVE_STAGE19_CONSTRUCTION_PROVED=true
POSITIVE_POWER_LOWER_BOUND_PROVED=false
MATCHING_HALF_POWER_LOWER_BOUND_PROVED=false
TRUE_TARGET_EXPONENT_IDENTIFIED=false
HALF_POWER_INTRINSIC_PROVED=false
PERFECT_CUBOID_CONCLUSION=NONE
SUPERSEDED_CURRENT_STATUS=FINITE_CONSTANT_FLOOR_ONLY
SUPERSESSION_SOURCE=Stage24-50_PR976
```