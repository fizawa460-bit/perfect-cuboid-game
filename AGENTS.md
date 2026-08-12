# Repository agent instructions

## Stage14 automation PR contract

Every pull request created for one of the recurring Stage14 batches must include exactly one safety marker and exactly one route marker in its body:

```text
STAGE14_AUTOMATION_SAFE=true
STAGE14_ROUTE=<route>
```

Use the route corresponding to the requested batch:

- `Stage14-main-batch` -> `main`
- `Stage14-s-batch` -> `s`
- `Stage14-t-batch` -> `t`
- `Stage14-Work-toolbox-XQ` (integration batch) -> `xq`

Do not set `STAGE14_AUTOMATION_SAFE=true` for unrelated PRs. Do not use a route other than `main`, `s`, `t`, or `xq`. If a batch is blocked, unsafe to merge, has unresolved conflicts, or needs manual review, omit the safety marker and state the blocker in the PR body.
