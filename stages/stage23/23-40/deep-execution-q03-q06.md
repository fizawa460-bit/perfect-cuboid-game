# Stage23-40 — deep execution of selected Q03/Q06 attacks

Status: **REPAIR SUBMISSION**

This artifact addresses only the audit repair scope `DEEP_EXECUTION_OF_SELECTED_Q06_AND_Q03_ATTACKS_ONLY`. Q04/Q11 remain deferred.

## Q03 — genus-one slice, corrected and driven to an arithmetic obstruction

The selected Stage17-originating slice is

\[
w^2=(t^2+1)(t^2+2t+2).
\]

The previous checkpoint40 text incorrectly stated that `(t,w)=(0,1)` is a rational point. In fact the right side at `t=0` is `2`, so that assertion is false and is withdrawn.

A useful symmetric substitution is

\[
s=2t+1,
\qquad W=4w.
\]

Then

\[
\boxed{W^2=s^4+6s^2+25}.
\]

This is a genus-one quartic torsor. Its binary-quartic invariants are

\[
I=21,
\qquad J=162,
\]

so the associated Jacobian is an elliptic curve over `Q` (up to the standard scaling convention). However a Jacobian model does **not** imply that the quartic torsor itself has a rational point.

For Stage23 the required parameter `t` is integral, and here a complete elementary obstruction is available. For every integer `t`, exactly one of `t` and `t+1` is odd. Every odd square is `1 mod 8`. Therefore one of

\[
t^2+1,\qquad (t+1)^2+1=t^2+2t+2
\]

is congruent to `2 mod 8`, while the other is odd and congruent to `1` or `5 mod 8`. Hence their product is always

\[
\boxed{2\pmod 8}.
\]

But an integer square modulo `8` is only `0,1,4`. Thus

\[
\boxed{(t^2+1)(t^2+2t+2)\text{ is never an integer square for any }t\in\mathbf Z.}
\]

Consequently the entire consecutive-parameter AR-039 slice is rigorously excluded from Stage19, including the required congruence class `t=1 mod 14`.

```text
Q03_PREVIOUS_RATIONAL_POINT_CLAIM=RETRACTED
Q03_GENUS_ONE_TORSOR=true
Q03_JACOBIAN_EXISTS=true
Q03_INTEGER_PULLBACK_RESOLVED=true
Q03_MOD8_OBSTRUCTION=true
Q03_STAGE19_HITS_FOR_INTEGER_T=0_PROVED
Q03_INFINITE_STAGE19_FAMILY=false
Q03_STATUS=EXHAUSTED_FOR_THIS_SLICE_BY_GLOBAL_INTEGER_CONGRUENCE_OBSTRUCTION
```

No finite scan is used in this proof.

## Q06 — Kummer receiver, deep execution boundary

Q06 was selected as the upper-side attack because a `(4,4)` Kummer receiver could in principle improve the Stage19 ceiling. For an actual Stage23 improvement, the receiver must provide all of the following on the literal primitive/canonical target population:

1. an explicit receiver map from Stage19 coordinates to a Kummer/K3 model;
2. a proved fiber-multiplicity bound away from explicit exceptional loci;
3. a quantitative comparison between the receiver height and the physical height `d=R`;
4. a point-count theorem on that receiver under the transferred height;
5. after translating back, an exponent `<1/2` or a genuine logarithmic saving relative to `N2(B)<<_epsilon B^(1/2+epsilon)`.

The Stage23 queue/ledger identifies Q06 as a reusable component, but the currently materialized Stage23 repository artifacts do **not** contain a concrete Q06 receiver equation plus physical-height point-count theorem satisfying items 1–5. Repository search by the selected queue identifier and Kummer/physical-height terms did not expose an additional materialized theorem interface beyond the queue classification itself.

Thus Q06 has now been pushed to the precise internal-input boundary rather than stopped at a checklist:

```text
Q06_RECEIVER_ID=(4,4)_KUMMER
Q06_STAGE23_COMPATIBILITY=PASS
Q06_EXPLICIT_RECEIVER_EQUATION_MATERIALIZED_IN_STAGE23=false
Q06_PHYSICAL_HEIGHT_COMPARISON_THEOREM_MATERIALIZED=false
Q06_UNIFORM_FIBER_MULTIPLICITY_THEOREM_MATERIALIZED=false
Q06_RECEIVER_POINT_COUNT_STRONGER_THAN_HALF_POWER_MATERIALIZED=false
Q06_EXPONENT_IMPROVEMENT_PROVED=false
Q06_LOG_SAVING_PROVED=false
Q06_INTERNAL_DEEP_EXECUTION_STATUS=BLOCKED_AT_MISSING_MATERIALIZED_RECEIVER_HEIGHT_COUNT_INTERFACE
Q06_REOPEN_CONDITION=NEW_CONCRETE_RECEIVER_EQUATION_OR_HEIGHT_OR_POINT_COUNT_INPUT
```

This is not a proof that Q06 cannot improve the upper bound. It is a proof-state statement: there is no certified theorem in the currently materialized Stage23 interface that can be composed to improve the bound without introducing new mathematical input.

## Checkpoint40 repair verdict

Q03 is no longer merely "an elliptic model may exist". The selected slice is killed completely for integral parameters by a mod-8 obstruction. Q06 is no longer merely "height/multiplicity are needed"; the exact missing interface has been isolated and the current repository does not materialize the receiver/height/count package required for a stronger bound.

```text
REPAIR_SCOPE=DEEP_EXECUTION_OF_SELECTED_Q06_AND_Q03_ATTACKS_ONLY
Q03_EXECUTION_DEPTH_INSUFFICIENT=false
Q06_EXECUTION_DEPTH_INSUFFICIENT=false
Q04_Q11_ACTIVATION_DEFERRED=true
ZERO_DENSITY_THEOREM_REOPENED=false
FINITE_DATA_USED_AS_PROOF=false
NEXT_CHECKPOINT=40
AUDIT_REQUIRED=true
ADVANCE_ALLOWED=false
MERGE_ALLOWED=false
```
