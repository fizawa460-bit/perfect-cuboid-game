# Stage15-6 ChatGPT-first operating contract

Stage15-6 is operated primarily from ordinary ChatGPT with the GitHub connector. Codex is an exception for repository-scale execution or repair, not the default mathematical researcher.

## The only two normal commands

### `Stage15-6-main-batch`

Run in the continuing main research chat. Start from current `main`, read the latest Stage15-6 cycle exit and candidate ledger, ingest the most recent audit verdict, and advance three substantive work units (at most five) or stop earlier on a material receiver change. Apply the [Cycle Exploration Safety Protocol](cycle-exploration-safety-protocol.md). Before parking, run every triggered exhaustive-view, blind-rediscovery, Arsenal, exact-reconstruction, measure, and quantifier audit. Create a PR and finish with the controller fields.

The main chat may repair mathematical text identified by the preceding audit. It must not approve its own PR.

### `Stage15-6-audit`

Run in a fresh ChatGPT chat after the main-batch PR exists. Read the PR, its immediate canonical dependencies, the current candidate ledger, and the exact receiver; do not replay all Stage15 history. Perform an adversarial review of the implication chain, physical population/cutoff, measure, quantifiers, double charging, cross-promotion, completeness of generated candidates, and merge safety. Do not modify files. Finish with exactly:

```text
AUDIT_VERDICT=PASS|FIX_REQUIRED|BLOCKED
INTERNAL_ROUTE_REMAINS=true|false
NEXT_MAIN_TASK=<exact next task>
CODEX_AUDIT_REQUIRED=true|false
CODEX_REASON=<NONE or exact reason>
MERGE_ALLOWED=true|false
```

`FIX_REQUIRED` is consumed by the next `Stage15-6-main-batch`; there is no third normal repair command.

## When Codex is actually required

Set `CODEX_AUDIT_REQUIRED=true` only for repository execution risk: broken aggregate verification/CI, repo-wide mechanical consistency work, large multi-file repairs, source volume exceeding a reliable connector audit, two consecutive fresh audits that reverse the same verdict, or a reproduction requiring local execution unavailable to ChatGPT. A difficult theorem gate alone is not a Codex trigger.

When transfer is required, the audit chat must produce a bounded task containing the exact files, failing command, expected invariant, and return condition. After Codex repairs or reproduces it, control returns to `Stage15-6-audit`, then to the normal two-command loop.

## Split decision

Do not split merely because several ideas exist. Recommend a split only when two live obstructions are proved non-equivalent and independent, pointwise and averaged routes require a separate exceptional-set adapter, the same kernel occurs under distinct charged measures, or an upstream normal-form change invalidates several downstream branches. The audit output explains the trigger; the human decides whether to launch the extra chat.

## Normal loop

```text
Stage15-6-main-batch
  -> Stage15-6-audit (fresh chat)
  -> merge if PASS
  -> Stage15-6-main-batch
```

The machine controller is `python stages/stage15/replay/verify_stage15_6_controller.py`. It discovers all two-letter Stage15-6 substages and their verifiers, runs the complete regression chain, identifies the latest exit, and prints the recommended owner. It does not replace mathematical audit judgment.
