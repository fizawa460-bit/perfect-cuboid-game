# PR #1478 Arsenal hostile audit

Status: `PASS_MERGE_READY_AFTER_SNAPSHOT_SEMANTICS_REPAIR`

Scope: Arsenal routing/promotion semantics only. This audit does not re-prove every underlying Stage theorem or computation; it verifies that closed-stage formal promotions and active-stage provisional harvests are represented with the correct credit boundaries, provenance, and override rules.

## Audited PR

```text
PR=1478
BRANCH=arsenal-provisional-stage32-stage33-harvest
PRE_REPAIR_HEAD=1dea5e28a0db4ad7c7d6ea5e8bd59f67e7b34624
FORMAL_STAGES=Stage30,Stage31
PROVISIONAL_STAGES=Stage32,Stage33
FORMAL_SELECTOR_ADDITIONS=0
```

## Verdict

The Arsenal architecture passes hostile review.

- Stage30 and Stage31 are closed and hostile-audited; their promoted entries are formal router-only weapons/workflows, not theorem/population selectors.
- Stage32 and Stage33 remain provisional discovery aids only.
- Provisional cards cannot grant theorem, receiver, route, endpoint, or perfect-cuboid credit.
- Active Stage source/controller/MAIN authority always overrides an Arsenal snapshot.
- Revoked/reopened Stage33 named-source relations are not promoted.
- Cross-stage dedup/specialization relations are explicit rather than silently multiplying equivalent weapons.

## Active-stage snapshot semantics

A provisional harvest head is a historical extraction checkpoint, not a live authority pointer.

```text
HARVEST_SNAPSHOT_HEAD_IS_IMMUTABLE_PROVENANCE=true
LATEST_VERIFIED_ACTIVE_HEAD_IS_INFORMATIONAL_ONLY=true
LIVE_HEAD_MUST_BE_REFETCHED_AT_CARD_USE=true
ACTIVE_STAGE_AUTHORITY_OVERRIDES_PROVISIONAL_CARD=true
HEAD_DRIFT_ALONE_DOES_NOT_PROMOTE_OR_REVOKE_A_CARD=true
HEAD_DRIFT_REQUIRES_TARGETED_SOURCE_REVALIDATION_BEFORE_USE=true
```

Fresh heads observed during this audit:

```text
Stage32_PR=1474
Stage32_branch=stage32-post1473-integral-picard-support-preflight
Stage32_latest_verified_active_head=4e7865599de58d184f160d8d779ef2a024216562

Stage33_PR=1476
Stage33_branch=stage33-post1475-j2-v4-generator-adapter
Stage33_latest_verified_active_head=18f6c64dde415c235b49f7458bf44afb1f2403b5
```

These latest heads are deliberately not permanent mathematical source locks. A future consumer must refetch the live PR/branch and then validate the card's exact load-bearing source paths/hashes/hypotheses.

## Stage33 hostile-audit interaction

At the time of this audit, active Stage33 PR #1476 itself is blocked by a hostile audit on detailed-authority/source-lock consistency. That does not make PR #1478 unsafe because the Arsenal representation is fail-closed:

```text
Stage33_cards=PROVISIONAL_ONLY
historical_mask6_named_J2_source=REOPENED_EXACT_DO_NOT_USE_AS_NAMED_SOURCE
J2_named_Kummer_source_target_relation=REVOKED_EXACT_DO_NOT_USE
ACTIVE_STAGE_SOURCE_LOCK_MUST_BE_REVALIDATED=true
```

Therefore the active Stage33 failure cannot be converted into Arsenal theorem credit or restore the revoked relation. If Stage33 repairs revise any reusable method contract, the provisional Stage33 harvest must be updated or retired before final Stage33 promotion.

## Formal Stage30/31 audit boundary

Stage30 final hostile audit source:
`stages/stage30/30-10/audit.md`
with verdict `PASS_STAGE30_CLOSED_NONOBSTRUCTIVE_MODULAR_KERNEL`.

Stage31 final hostile audit source:
`stages/stage31/31-06/audit.md`
with verdict `PASS_STAGE31_CLOSED_DIRECT_QUARTIC_CERTIFICATION`.

The Arsenal formal promotions preserve the audited scope walls, including:

```text
finite certificate PASS != global theorem
adapter closure != receiver/route/endpoint closure without an explicit source-locked implication
reproducibility/audit PASS != new mathematical credit
birational equivalence != integral-point equivalence
rank proof != full Mordell-Weil group proof
complete auxiliary points != source-family closure without exact pullback
```

## Merge boundary

This audit authorizes the Arsenal PR as a merge-ready documentation/router update only after the machine-readable index explicitly distinguishes immutable harvest snapshots from informational latest-active-head observations.

It does not authorize merging Stage32 PR #1474 or Stage33 PR #1476, does not formalize their provisional cards, and does not claim a perfect-cuboid existence/nonexistence result.
