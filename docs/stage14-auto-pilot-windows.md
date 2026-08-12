# Stage14 automatic loop — Windows trial

This trial splits responsibility deliberately:

- ChatGPT Scheduled task reads GitHub once per hour and creates only the next
  required Stage14 route PRs or the integrated XQ PR.
- Windows Task Scheduler runs `scripts/stage14-auto-pilot.ps1` every 30 minutes.
  It performs deterministic PR/CI checks and merges at most one PR per run.
- GitHub is the durable shared state. No browser-click RPA is used.

## Safety gates

The Windows worker considers a PR only when all of these are true:

- repository and author are exactly the configured values;
- base branch is `main`;
- the PR body contains `STAGE14_AUTOMATION_SAFE=true` on its own line;
- the PR body contains exactly one supported `STAGE14_ROUTE` marker;
- no `BLOCKED`, `DO_NOT_MERGE`, or `AUTOMATION_STOP` marker is present;
- GitHub reports a mergeable state;
- at least one check exists and every reported check has completed successfully,
  neutrally, or as skipped.

The worker squash-merges at most one PR per invocation, then exits so GitHub can
recompute the remaining branches against the new `main`. Any failed command
stops the run. PRs without the safety marker are never auto-merged.

## One-time setup

Install GitHub CLI, sign in, and clone this repository on Windows. From an
ordinary PowerShell window in the repository, run:

```powershell
gh auth login
powershell -ExecutionPolicy Bypass -File .\scripts\install-stage14-auto-pilot.ps1 -WhatIf
```

`-WhatIf` is the recommended first check. Inspect the task's output manually by
running:

```powershell
.\scripts\stage14-auto-pilot.ps1 -WhatIf
```

When the output identifies only intended automation PRs, switch the scheduled
task to live mode:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\install-stage14-auto-pilot.ps1
```

To pause or remove it:

```powershell
Disable-ScheduledTask -TaskName PerfectCuboid-Stage14-AutoPilot
Unregister-ScheduledTask -TaskName PerfectCuboid-Stage14-AutoPilot -Confirm:$false
```

The initial ChatGPT task is separately capped at two newly created XQ cycles
after PR #771. Review those two cycles before removing the cap.
