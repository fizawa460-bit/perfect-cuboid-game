# Stage14 auxiliary H/tH snapshot protocol

## Purpose

Stage14 uses auxiliary `H` lanes for independent theorem/literature/applicability audits that are too specialized to keep inside a fast-moving proof route.

Examples include route-specific names such as `tH23`, `sH41`, `toolbox-H*`, and a mainline `H` gate.  They are **not** second copies of the parent proof route.  Their job is to audit one precisely frozen mathematical receiver and return a durable verdict.

The governing rule is:

```text
ONE H REQUEST = ONE IMMUTABLE SOURCE SNAPSHOT = ONE AUDIT RESULT
```

Once an H request has been dispatched, later progress on the parent route does not rewrite that H request.

---

## 1. When an H stage should be emitted

A proof route should request a new H stage only when all of the following hold.

1. The route has already used the obvious exact algebraic, gcd/CRT, reconstruction, divisor, spacing, or finite-fiber reductions that it owns internally.
2. A smallest remaining analytic/geometric/arithmetic obstruction can be named explicitly.
3. An independent theorem/applicability audit could materially change the next decision.
4. The object is stable enough to describe with a fixed variable dictionary and physical masks.
5. The expected verdict fields are known in advance.

Do **not** create an H stage merely because the current proof step is difficult or because literature might exist.

The emitting stage should record at least

```text
H_NEEDED=true
H_REQUESTED_OBJECT=<exact receiver name>
H_SOURCE_STAGE=<emitting stage>
H_SOURCE_SNAPSHOT_SHA=<exact commit/head SHA>
H_TARGET_FILE=<repo path>
H_ROUTE_BLOCKED_WAITING_FOR_H=true|false
```

If no external audit is yet minimal, record `H_NEEDED=false` and continue reducing internally.

---

## 2. Required target file before dispatch

Before the H worker starts, the parent route writes a durable target file, normally

```text
stages/stage14/<source-stage>/h-target.md
```

or the route-specific equivalent such as `th23-target.md`.

The target must contain enough information that another ChatGPT instance can work from the repository without a giant chat prompt:

```text
REQUESTED_OBJECT=
AUDITED_THROUGH=
SOURCE_SNAPSHOT_SHA=
DO_NOT_REOPEN=
VARIABLE_DICTIONARY=
EXACT_KERNEL_OR_RECEIVER=
PHYSICAL_MASKS_TO_RETAIN=
CANDIDATE_THEOREM_TECHNOLOGIES=
APPLICABILITY_STANDARD=
REQUIRED_VERDICT_FIELDS=
EXPECTED_OUTPUT_DIRECTORY=
CI_REQUIREMENT=
```

The user-facing handoff may therefore be short: read the target file, audit it, record the result, run CI, and create the PR.

A `*-refinement.md` may be added **before dispatch** if the source stage itself was sharpened before the H work began.  After dispatch, the target is frozen.

---

## 3. Dispatch freezes the mathematical contract

As soon as the H task is actually started — equivalently, once its working branch/PR exists or the worker has begun the audit — record the logical state

```text
H_TARGET_FROZEN=true
H_SOURCE_SNAPSHOT_FROZEN=true
```

From that point:

- later parent stages must not ask the same H number to follow a new receiver;
- later `latest main` changes do not alter the mathematical question;
- a new downstream reduction is not a reason to rewrite the running H target;
- do not repeatedly append `refinement.md` files to make the running H chase the parent route.

This is the central parallelism rule.

---

## 4. Parent-route progression while H is running

### Non-blocking H

If

```text
H_ROUTE_BLOCKED_WAITING_FOR_H=false
```

then the parent route continues normally.

Example:

```text
t81 emits tH23
       |\
       | tH23 audits the frozen t81 receiver
       |
       +--> t82 --> t83 --> ...
```

If `t82` discovers a smaller receiver, it may record that fact for future use, but it must **not** order `tH23` to restart or update itself.

### Blocking H

Use

```text
H_ROUTE_BLOCKED_WAITING_FOR_H=true
```

only when the next mathematical step genuinely depends on the H verdict.  The route may still perform independent bookkeeping, regression, or unrelated reductions, but it must not mutate the frozen H question.

---

## 5. What the H worker audits

The H worker audits the frozen source snapshot, not an indefinitely moving latest receiver.

Every result should record

```text
H_STAGE=
AUDITED_THROUGH=
SOURCE_SNAPSHOT_SHA=
TARGET_FILE=
REQUESTED_OBJECT=
TARGET_FROZEN=true
```

The worker may inspect current `main` for context or to avoid stale bibliographic/global-ledger statements, but theorem applicability must be judged for the frozen receiver unless the source snapshot itself has been invalidated.

A later global exponent may be reported as context, but it must not silently replace the frozen local theorem question.

---

## 6. H result and required boundary

An H result is a scoped theorem/applicability certificate, not a promise that the parent route has stopped moving.

Typical final fields are

```text
H_STAGE=COMPLETE_...
AUDITED_THROUGH=...
SOURCE_SNAPSHOT_SHA=...
TARGET_FROZEN=true
FULL_REQUIRED_MASKS_RETAINED=true|false
OFF_THE_SHELF_THEOREM_APPLICABLE=true|false
CERTIFIED_B_POWER_SAVING_EXPONENT=<delta or 0>
MINIMAL_REMAINING_OBSTRUCTION=...
PREFERRED_RECEIVER=...
NEXT_H_NEEDED=true|false
NEXT_H_REQUESTED_OBJECT=...
```

A negative verdict is a valid completed result and should be preserved.

---

## 7. Merge policy: merge the completed snapshot audit

A completed H audit should normally be merged even if the parent route has advanced beyond its source stage.

The result remains valid in its stated scope:

```text
"receiver A at source snapshot S has verdict V"
```

Later `receiver B` does not make that statement false.

Therefore:

- do not discard a clean H result merely because the parent route found a later reduction;
- do not demand a re-audit of the same H number before merge;
- resolve only mechanical merge/CI conflicts when bringing the H PR onto current `main`;
- do not change the audited mathematical object during that mechanical update.

This preserves useful negative and positive theorem boundaries instead of creating an endless chase.

---

## 8. Stacked PR rule when the source stage is not merged yet

Prefer to dispatch H from a merged source stage when possible.

If true parallelism is useful before the source PR merges:

1. freeze the exact source head SHA;
2. branch the H work from that source head or otherwise make the dependency explicit;
3. keep the H PR Draft/stacked while the source is unmerged;
4. after the source merges, retarget/recreate the H PR onto `main` mechanically;
5. preserve the same target, result, audit data, and source SHA.

Do not rerun the mathematical investigation just because the PR base changed.

---

## 9. Consuming an H result on the parent route

When the H result merges, the current parent stage reads it once and decides how it applies.

There are three normal cases.

### A. Current receiver is still the audited receiver

Consume the verdict directly.

### B. Current receiver is a strict downstream reduction

Use the H result as a certified boundary for the older receiver.  Determine whether the new reduction removes the recorded obstruction.  Do not ask the old H number to rewrite itself.

### C. Current receiver is materially different and needs another independent audit

Create the **next H number**.

Example:

```text
tH23 audits receiver A
parent route later reduces A -> B
B needs a fresh external theorem audit
=> emit tH24 for B
```

Never use

```text
"please update tH23 for t82/t83/t84"
```

as the normal workflow.

---

## 10. Exception: source invalidation

The snapshot rule has one substantive exception.

If the source stage is later found mathematically incorrect in a way that invalidates the receiver itself — not merely sharpened — then the H audit may be cancelled or marked superseded.

Record explicitly

```text
H_SOURCE_INVALIDATED=true
H_INVALIDATION_REASON=...
H_RESULT_NOT_CANONICAL=true
```

A normal downstream improvement, stronger bound, smaller receiver, or newer global exponent is **not** source invalidation.

---

## 11. Numbering and naming

H numbering is monotone within its route.

```text
tH22 -> tH23 -> tH24
sH41 -> sH42
mainline H gate -> next explicitly named mainline H stage
```

A new H number means a new mathematical receiver or a genuinely new theorem question.  It is not a version number for edits to an earlier audit.

---

## 12. Short ChatGPT-to-ChatGPT request format

Because the full specification lives in the repository, the normal user handoff should be short.

Example:

```text
Stage14-tH24 を実施してください。

完全直方体リポジトリの指定された target.md を依頼仕様として読み、
記載された snapshot を固定入力として独立検算してください。
結果・deterministic audit・frozen boundary・専用CI・PR作成まで一括で実施してください。
後続の本線 stage が進んでいても、この H target は追従更新しないでください。
```

The repository target, not chat length, carries the mathematical specification.

---

## 13. Operational locks

```text
STAGE14_H_PROTOCOL=IMMUTABLE_SOURCE_SNAPSHOT_AUDIT
ONE_H_REQUEST_ONE_SNAPSHOT=true
H_TARGET_FREEZES_AT_DISPATCH=true
RUNNING_H_CHASES_LATER_PARENT_STAGES=false
RUNNING_H_REFINEMENT_AFTER_DISPATCH=false
PARENT_ROUTE_MAY_CONTINUE_WHEN_H_NONBLOCKING=true
COMPLETED_H_MERGES_AS_SCOPED_SNAPSHOT_RESULT=true
LATER_RECEIVER_REQUIRING_AUDIT_USES_NEXT_H_NUMBER=true
LATEST_MAIN_MECHANICAL_REBASE_DOES_NOT_CHANGE_H_TARGET=true
SOURCE_INVALIDATION_IS_ONLY_NORMAL_CANCELLATION_EXCEPTION=true
SHORT_CHAT_HANDOFF_USES_REPO_TARGET_FILE=true
```
