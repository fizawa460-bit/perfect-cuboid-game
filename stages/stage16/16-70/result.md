# Stage16-70 — intrinsic-status / closeout verdict

Status: **SUBMITTED_FOR_FRESH_AUDIT**

## Intrinsic-status verdict

Stage16 has matched certified bounds
\[
M_1(B)\ll B^2\log B,
\qquad
M_1(B)\gg B^2\log B,
\]
so
\[
\boxed{M_1(B)\asymp B^2\log B}.
\]
Therefore the Stage16 growth order is no longer merely a best-known upper or lower exponent. At the proved `Theta` resolution:

```text
TRUE_ORDER_IDENTIFIED=true
POLYNOMIAL_EXPONENT=2
LOG_POWER=1
INTRINSIC_STATUS=PROVED_AT_POWER_LOG_ORDER
LEADING_CONSTANT_PROVED=false
```

The common source population satisfies
\[
U(B)=\frac{\pi}{36\zeta(3)}B^3+O(B^2),
\]
so the Stage16 survivor ratio obeys
\[
\boxed{M_1(B)/U(B)\asymp \log(B)/B\to0}.
\]

## Causal verdict

The certified mechanism is:

1. unrestricted two-edge freedom contributes order `B^2`;
2. imposing one integral face replaces that pair by scaled primitive Pythagorean faces of order
   \[
   \sum_{k\le B}P(B/k)\asymp B\log B;
   \]
3. the remaining third edge stays free at order `B`.

Thus the power drop is caused by the one-face Pythagorean restriction and the logarithm by the harmonic face-scale sum.

If `H_1(B)` counts the same primitive canonical `R<=B` population with at least one integral face, then
\[
M_1(B)\le H_1(B)\ll B^2\log B
\]
and the sharp Stage16 lower bound gives
\[
M_1(B)\gg B^2\log B.
\]
Hence
\[
\boxed{H_1(B)\asymp M_1(B)\asymp B^2\log B}.
\]
So exactly-one does not change the proved power/log order relative to at-least-one.

This does **not** imply a global overlap little-`o` theorem or a limiting `M_1/H_1` ratio.

## Independence / double-charge verdict

- Primitivity changes density/weights but not the proved power/log order.
- Canonicalization changes multiplicity but not the proved power/log order.
- The exactly-one postfilter is order-neutral at this resolution; no stronger overlap asymptotic is claimed.
- Integral space diagonal is **not** imposed at Stage16 and is not charged to its exponent.
- AR-039 is only a narrower integral-space-diagonal regression subset with exact `R=d` cutoff adapter; its `B^(1/2)` lower bound is not mixed with the ambient sharp law.
- Finite directional `ab/ac/bc` imbalance remains diagnostic only.
- No Stage14/15 exactly-two or space-diagonal theorem is cross-promoted into the Stage16 ambient order.

```text
DOUBLE_CHARGE_CHECK=PASS
SPACE_DIAGONAL_CHARGED=false
AR039_ROLE=REGRESSION_SUBSET_ONLY
GLOBAL_OVERLAP_LITTLE_O_PROVED=false
DIRECTIONAL_LAW_PROVED=false
```

## Remaining genuine unknowns

Stage16 closes its population-order question but leaves the following genuinely open:

- leading asymptotic constant for `M_1(B)`;
- full asymptotic expansion/error term;
- limiting directional vector for the integral face position;
- whether `H_1(B)-M_1(B)=o(B^2 log B)`;
- whether `M_1(B)/H_1(B)` has a limit;
- the Stage16 -> Stage17 survival ratio after imposing integral space diagonal;
- any perfect-cuboid existence/nonexistence conclusion.

These are not unfinished internal routes required to classify Stage16 itself. The space-diagonal questions belong to Stage17 and Stage21 under the frozen common cutoff.

## Checkpoint classification

```text
CHECKPOINT_10=PROVED
CHECKPOINT_20=COMPUTED
CHECKPOINT_30=PROVED
CHECKPOINT_40=PROVED
CHECKPOINT_50=PROVED
CHECKPOINT_60=PROVED
CHECKPOINT_70=PROVED_CANDIDATE_PENDING_FRESH_AUDIT
POPULATION_CONTRACT_CHANGED=NO
COMPARISON_ADAPTER_REQUIRED=NO
EVIDENCE_LEVELS_COMPLETE=YES
DEPENDENCY_LEDGER_COMPLETE=YES
OPEN_GATE_REENTRY_JUSTIFIED=NOT_APPLICABLE
ARSENAL_SUPERSESSION_CHECK=NOT_APPLICABLE
```

## Stage-end artifact decisions

Stage16 proves a new sharp population law and a causal decomposition expected to be cited repeatedly by Stage17 and Stage21. Reconstructing the theorem from scattered checkpoints would be unsafe, so a proof-complete bundle is included at

`stages/stage16/final.md`.

The bundle follows `SELF_CONTAINED_REVIEW_STANDARD_V1` and embeds the load-bearing Stage16 proof chain.

No new arsenal item is proposed. The portable ingredients are already represented by AR-001/AR-002 and AR-039; the new synthesis is primarily the Stage16 population theorem rather than a distinct reusable weapon.

```text
SELF_CONTAINED_BUNDLE_REQUIRED=YES
SELF_CONTAINED_BUNDLE_REASON=New sharp population law and causal decomposition will be reused by Stage17/21; a single proof-complete stable interface is safer than reconstructing checkpoint fragments.
ARSENAL_PROMOTION_REQUIRED=NO
ARSENAL_CANDIDATES=NONE
```

## Proposed stage transition

A fresh `Stage16-audit` must certify this checkpoint and the self-contained bundle before Stage16 may close. If PASS:

```text
STAGE_STATUS=CLOSED
ADVANCE_ALLOWED=true
NEXT_STAGE=Stage17
```

Until that audit passes, Stage16 remains open at checkpoint 70 and Stage17 must not treat this closeout as certified.

```text
MAIN_BATCH_STATUS=SUBMITTED
CURRENT_STAGE=Stage16
CURRENT_CHECKPOINT=70
CHECKPOINTS_ATTEMPTED=70
CHECKPOINTS_SUBMITTED=70
NEW_CLAIMS=intrinsic-status verdict and stage-end artifact decisions; no stronger growth theorem than audited Stage16-30/40/50/60 chain
REUSED_WEAPONS=AR-001,AR-002,AR-039(regression only)
CODEX_REQUIRED=false
CODEX_REASON=Checkpoint 70 is a compact mathematical closeout and proof-bundle assembly; no repository-heavy implementation is required.
AUDIT_REQUIRED=true
NEXT_EXPECTED_COMMAND=Stage16-audit
MERGE_ALLOWED=false
```
