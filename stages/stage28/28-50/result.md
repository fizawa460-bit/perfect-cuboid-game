# Stage28-50 — strongest lower-bound / construction ledger

```text
TASK_ID=Stage28-50
CHECKPOINT=50
PARENT_ROADMAP=docs/stage16-29-population-roadmap.md
COMPARISON=Stage19 -> Stage20
STATUS=SUBMITTED_PENDING_FRESH_AUDIT
```

## 1. Incoming certified source/target floors

The source remains

\[
\boxed{N_2(B)\gg B^{1/4}},
\]

with known Stage25/Stage27 quarter-power families saturated at parameter/height efficiency `2/8=1/4`.

The target entered checkpoint50 with the audited Stage26 theorem

\[
M_3(B)\gg_\varepsilon B^{1/3-\varepsilon}.
\]

## 2. New checkpoint50 theorem candidate: remove the Saunderson fiber epsilon

For the generalized Saunderson output

\[
A=u|4v^2-w^2|,\quad B=v|4u^2-w^2|,\quad C=4uvw,
\quad u^2+v^2=w^2,
\]

the distinguished `(A,B)` face diagonal is `w^3`.

Given a physical output and a choice of which of its at most three face diagonals is `w^3`, the integer `w` is fixed.  The edge opposite that face is `C`, hence `uv=C/(4w)`.  Together with `u^2+v^2=w^2`, this uniquely determines `{u,v}`; primitive parity fixes the standard orientation.

Therefore the physical output fiber is at most `3`, not merely divisor-size.  Combining this with the already-audited `>>T^2` primitive Euclid parameter count and `R<72T^6` gives

\[
\boxed{M_3(B)\gg B^{1/3}}.
\]

```text
GENERAL_SAUNDERSON_GLOBAL_FIBER_BOUND_CANDIDATE=3
M3_LOWER_EPSILON_FREE_ONE_THIRD_CANDIDATE=true
M3_LOWER_ONE_THIRD_MINUS_EPSILON_SUPERSEDED_IF_AUDITED=true
TRUE_M3_EXPONENT_IDENTIFIED=false
M3_ASYMPTOTIC_PROVED=false
```

## 3. Construction-efficiency comparison

The strongest known explicit source and target mechanisms now have

```text
Stage19 N2 known family: kappa/h = 2/8 = 1/4
Stage20 M3 Saunderson:  kappa/h = 2/6 = 1/3
```

Thus the best known target construction is polynomially more efficient in the common physical height than the best known source construction.

For selected saturated construction families this gap is `1/12` on the exponent scale.  This statement is about the **known families only**; it does not order the full populations.

```text
KNOWN_CONSTRUCTION_EXPONENT_GAP=1/12
KNOWN_CONSTRUCTION_TARGET_MORE_EFFICIENT=true
FULL_M3_VS_N2_ORDERING_PROVED=false
```

## 4. Bridge lower implication

The current Stage19 upper still gives only

\[
N_2(B)\ll_\varepsilon B^{1/2+\varepsilon}.
\]

Hence the new target floor implies, for every fixed `epsilon>0`,

\[
\boxed{
M_3(B)/N_2(B)\gg_\varepsilon B^{-1/6-\varepsilon}.
}
\]

This does not improve the checkpoint30 endpoint-free ratio exponent because the remaining epsilon is on the source upper side.

```text
CHECKPOINT30_BRIDGE_LOWER_EXPONENT_IMPROVED=false
M3_NUMERATOR_LOWER_IMPROVED=true
EPSILON_FREE_M3_OVER_N2_B_MINUS_ONE_SIXTH_PROVED=false
```

## 5. Aggressive construction rematch

Materially distinct lower-side routes checked at checkpoint50:

1. exact inverse/fiber analysis of generalized Saunderson — **SUCCESS**, candidate epsilon-free `B^(1/3)` target floor;
2. compare Stage25/Stage27 saturated quarter-power source families — confirms `2/8` source construction efficiency and no hidden old-fiber upgrade;
3. Peschmann 2026 Mordell-Weil Euler-brick generator — rigorous finite construction, but no uniform `R<=B` power lower exceeding `1/3`;
4. Peschmann 2026 master-tuple classification/fiber results — structural completeness but no stronger bounded-height construction count; perfect-cuboid fiber results are off-stage for this lower ledger;
5. Himane 2024 additional generator templates — auxiliary square conditions remain; no matched counted family above `1/3` found;
6. classical Lenhart/Himane family tags in current databases — finite generator-bound evidence only;
7. direct transfer of either source/target family by imposing the other completion condition — rejected because it lands on the deferred perfect-cuboid endpoint, not the opposite Stage28 stratum.

```text
MATERIALLY_DISTINCT_LOWER_ROUTES_TESTED=7
DEEP_EXPLORATION_RULE_SATISFIED_CANDIDATE=true
STRONGER_M3_CONSTRUCTION_GT_ONE_THIRD_FOUND=false
STRONGER_N2_CONSTRUCTION_GT_ONE_QUARTER_FOUND=false
```

## 6. Remaining lower receiver

After the bounded-fiber upgrade, further lower progress requires a genuinely higher-efficiency physical construction or a direct same-host marginal lower comparison:

```text
OPEN_GATE_50=HigherEfficiencyPhysicalConstructionOrDirectMarginalLowerComparison
M3_PROGRESS_GATE=kappa/h>1/3
N2_PROGRESS_GATE=kappa/h>1/4
DIRECT_MARGINAL_COMPARISON_MUST_AVOID_ENDPOINT=true
RESEARCH_REQUEST_READY=true
```

This gate is nonblocking for Stage28 closeout if audited: checkpoint50's job is to record the strongest certified lower/construction ledger, not to identify either true exponent.

## 7. Exit

```text
CHECKPOINT50_LOWER_LEDGER_COMPLETE_CANDIDATE=true
AUDIT_REQUIRED=true
AUDIT_STATUS=PENDING
REPAIR_REQUIRED=UNKNOWN_PENDING_AUDIT
MERGE_ALLOWED=false
ADVANCE_ALLOWED=false
NEXT_CHECKPOINT_AFTER_PASS=60
NEXT_EXPECTED_COMMAND=Stage28-audit
PERFECT_CUBOID_CONCLUSION=NONE
```
