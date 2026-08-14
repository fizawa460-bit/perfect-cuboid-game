# Stage23-60 post-Stage24 checkpoint50 supersession

STATUS=POST_STAGE_SUPERSESSION_ADDENDUM
SOURCE_STAGE=Stage24
SOURCE_CHECKPOINT=50
SOURCE_PR=976
SOURCE_AUDIT=stages/stage24/24-50/audit.md

Stage23 checkpoint60 R60-01 remains mathematically correct under its stated historical source hypothesis: the Stage15-2 family there used coprime **odd** parameters `p,q`. For that odd/odd subfamily,

\[
17(p^4+q^4)\equiv2\pmod{16}
\]

and therefore no integral space diagonal is possible.

Stage24 checkpoint50 supplies new input by reopening the same algebraic formulas without the odd/odd restriction. The mixed-parity slice

\[
p^4+q^4=17Z^2
\]

has positive-rank genus-one structure and yields an infinite primitive exactly-two Stage19 construction. Accordingly, R60-01 must now be read with the following narrowed scope:

```text
R60_01_ODD_ODD_DEATH=STILL_VALID
R60_01_BROADER_FORMULA_DEATH=SUPERSEDED
REVIVED_VARIANT=MIXED_PARITY_C17
STAGE23_AUDIT_PASS_REVOKED=false
```

This is a later supersession/addendum, not a claim that the historical mod-16 proof was false. It corrects only the downstream interpretation of how broadly that death certificate may be applied.

Current downstream target lower status inherited from Stage24 checkpoint50 is:

```text
CURRENT_STAGE19_LOWER_BOUND=N2(B)>>sqrt(log B)
STAGE19_UNBOUNDEDNESS_PROVED=true
INFINITE_PRIMITIVE_STAGE19_CONSTRUCTION_PROVED=true
POSITIVE_POWER_LOWER_BOUND_PROVED=false
MATCHING_HALF_POWER_LOWER_BOUND_PROVED=false
PERFECT_CUBOID_CONCLUSION=NONE
```