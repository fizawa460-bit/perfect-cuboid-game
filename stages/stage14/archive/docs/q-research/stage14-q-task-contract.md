# 14-q — Stage14 literature radar invocation contract

Permanent invocation name:

```text
14-q
```

This short name is intentionally stable.  It is not a stage number.  The concrete output stage remains monotone (`Stage14-q11`, `Stage14-q12`, ...).

The preferred Work-side orchestration is now:

```text
Stage14-Work-toolbox-XQ
```

That invocation performs its toolbox/X audit first and then applies this q gate
to the newly frozen obstruction. If triggered, q is completed on the same branch
and in the same Draft PR. The standalone `14-q` name remains available for an
explicit literature-only run or for a `DEFERRED_SCOPED` target frozen by XQ.

On every `14-q` invocation:

1. read `stages/stage14/archive/docs/q-research/stage14-q-literature-radar-roadmap.md`;
2. inspect latest merged `main` and the latest completed q-stage;
3. identify whether the active proof routes expose a stable named obstruction whose mathematical form is materially different from the last q baseline;
4. if no such trigger exists, return `WAIT` and create no q-stage / branch / PR;
5. if a trigger exists, execute the next unused q-number, search current primary literature, classify each candidate `DIRECT / NEAR / BACKGROUND / BLOCKED`, write a falsifiable receiving-stage handoff, and open the scoped PR;
6. do not re-search a branch already covered by the previous q ledger merely because its stage number advanced;
7. never cross-promote fixed-U results to the whole-family theorem without an explicit bridge.
8. when called from `Stage14-Work-toolbox-XQ`, do not create a second branch or
   PR; return the classification and receiving-stage handoff to the Work result.

Required q10+ header:

```text
TRIGGER_STAGE=
EXACT_OBSTRUCTION=
CURRENT_BEST_BOUND=
WHY_EXISTING_Q_LEDGER_DOES_NOT_ALREADY_ANSWER_IT=
SEARCH_FAMILIES=
LAST_RADAR_BASELINE=
PROMOTION_STANDARD=
```

The user therefore only needs to send:

```text
14-q
```

and the repository state decides `WAIT` versus the next q-stage.
