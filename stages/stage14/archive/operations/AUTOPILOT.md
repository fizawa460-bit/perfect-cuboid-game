# Stage14 three-lane autopilot

This file is the durable control contract for the initial three-lane ChatGPT automation trial. Conversation history is never authoritative; every run must reconstruct state from GitHub.

## Safety boundary

- Repository: `fizawa460-bit/perfect-cuboid-game`
- Base branch: `main`
- Polling: at most once per hour per lane.
- One active work PR per lane.
- A closed-but-unmerged PR does not unlock the next task.
- If the active PR is open, draft, awaiting review, conflicted, or not merged, exit without starting work.
- If required CI/checks fail, mark the lane `BLOCKED` in the run report and do not start work.
- Before starting `NEXT`, verify that no open PR or branch already implements it.
- Work starts from current `main`, uses a new branch, one coherent commit, and a Draft PR.
- Do not merge mathematical work automatically during the initial trial.
- Never change the research goal, weaken a theorem boundary, promote finite evidence to an asymptotic theorem, or declare a proof complete.
- Stop with `APPROVAL_REQUIRED` when the next task is absent, ambiguous, changes direction, conflicts with the roadmap, asserts a new theorem/proof completion, or when independent reviews disagree.
- Do not dispatch the numerical or Stage13 lanes during this three-lane trial.

## Initial lanes

| Lane | Route | Active PR at initialization | Expected next task |
|---|---|---:|---|
| main-proof | Stage14 main proof | #225 (`14-4an`) | `14-4ao` |
| q2-local | Stage14 2-adic/local descent | #229 (`s5f`) | `s5g` |
| three-face | Stage14 three-face locus | #228 (`t15`) | Read the merged PR and canonical roadmap; do not guess |

The PR numbers above are bootstrap pointers only. After a merge, the lane must discover its current active PR from the canonical roadmap, merged predecessor, open PRs, and exact task identifier.

## Per-run state machine

1. Fetch this file from `main`, the canonical Stage14 roadmap, and the lane's active/open PRs.
2. Identify exactly one current task and predecessor for the assigned lane.
3. If an open PR already exists for the current/next task, exit silently.
4. If the predecessor is not merged into `main`, exit silently.
5. Verify required checks on the merged predecessor. On failure, report `BLOCKED` and exit.
6. Read `NEXT` from the merged PR and cross-check it against the canonical roadmap.
7. If missing, ambiguous, duplicated, or direction-changing, report `APPROVAL_REQUIRED` in Japanese and exit.
8. Otherwise execute exactly that one bounded task using the repository's existing conventions and theorem-status boundaries.
9. Validate relevant scripts/tests, create one coherent commit, and open one Draft PR.
10. The Draft PR body must include the Japanese handoff below and an exact `NEXT=` field.
11. End the run. Never start a second task in the same run.

## Required Japanese PR handoff

```markdown
## 日本語まとめ
- 進んだ方向:
- ロードマップ上の現在地:
- 今回変更した数学的主張:
- 検証・レビュー結果:
- 次に進む方向:
- 方向判定: 通常進行 / 方向転換あり
- 推奨: マージ可 / 要確認
```

Use `通常進行` only when the task is the unique next item already prescribed by the merged predecessor and canonical roadmap. Any uncertainty is `方向転換あり` and `要確認`.

## Trial graduation

Expand from three to five lanes only after at least three consecutive dispatch cycles per lane complete without duplicate PRs, wrong-route dispatch, skipped merge gates, or theorem-status drift. Auto-merge remains a separate opt-in phase after the trial.
