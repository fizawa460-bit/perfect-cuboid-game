# Stage20-50 audit

Status: PASS

Fresh audit verifies that checkpoint50 gives a genuine unconditional lower-bound construction for the audited Stage20 population.

For every even integer `m>=10`, with

```text
u=m^2-1,
v=2m,
w=m^2+1,
A=u|4v^2-w^2|,
B=v|4u^2-w^2|,
C=4uvw,
```

the companion proof is self-contained and load-bearing identities check exactly:

```text
A^2+B^2=w^6,
A^2+C^2=u^2(4v^2+w^2)^2,
B^2+C^2=v^2(4u^2+w^2)^2.
```

For even `m`, the Pythagorean input `(u,v,w)` is primitive and pairwise coprime. The prime-divisor argument therefore proves `gcd(A,B,C)=1`. For `m>=10`, the displayed polynomial inequalities give `0<B<C<A`, and `A(m)` is strictly increasing, so distinct allowed parameters produce distinct canonical primitive Stage20 objects.

The height estimate `R<31m^6` is valid. Counting even parameters `10<=m<=(B/31)^(1/6)` gives

\[
M_3(B)\ge \left\lfloor\frac12(B/31)^{1/6}\right\rfloor-4
\]

for all sufficiently large `B`, hence

\[
M_3(B)\gg B^{1/6}.
\]

This proves Stage20 infinitude and a positive-power lower bound. It does not prove that `1/6` is the true exponent, does not match the Stage14-e8 upper envelope, and does not give an asymptotic. The checkpoint30 growth-law OPEN_GATE therefore remains valid. Stage18->Stage20 conditional thinning remains reserved for Stage26. No integral-space-diagonal condition or perfect-cuboid conclusion is introduced.

The reference to the classical Saunderson identity is provenance only; the proof used for this checkpoint is internal and does not depend on an external bounded-height theorem.

CHECKPOINT_STATUS=PROVED_AUDITED_PASS
STAGE20_POPULATION_INFINITE=true
POSITIVE_POWER_LOWER_BOUND_PROVED=true
CERTIFIED_LOWER_EXPONENT=1/6
MATCHING_LOWER_BOUND_PROVED=false
TRUE_EXPONENT_IDENTIFIED=false
ASYMPTOTIC_FORMULA_PROVED=false
OPEN_GATE_30=STAGE20_POPULATION_GROWTH_LAW_UNRESOLVED
OPEN_GATE_50=SHARPNESS_AND_MATCHING_LOWER_BOUND_UNRESOLVED
FINITE_DATA_USED_AS_PROOF=false
STAGE18_TO_STAGE20_RATIO=DEFER_STAGE26

AUDIT_VERDICT=PASS
AUDIT_PERSISTENCE_STATUS=PENDING_STATUS_SYNC
UNSYNCED_AUDIT_STATE=stages/stage20/20-controller.json,docs/00_CURRENT_RESEARCH_STATUS.md
ADVANCE_ALLOWED=true
NEW_INPUT_REQUIRED=false
HUMAN_DECISION_REQUIRED=false
NEXT_CHECKPOINT=60
NEXT_STAGE=
CODEX_AUDIT_REQUIRED=false
CODEX_REASON=NONE
MERGE_ALLOWED=true
