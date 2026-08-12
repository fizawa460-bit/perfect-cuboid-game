# Stage14 AutoPilot one-cycle trial

This Windows trial uses merged GitHub PR history as the source of truth. The latest merged safe XQ PR is recorded as the cycle boundary. It then launches only missing `main`, `s`, and `t` batches, waits for their safe PRs to merge, launches one XQ batch, and disables its own scheduled task after that new XQ PR is merged.

## Safety behavior

- One isolated clone per route prevents cross-route working-tree collisions.
- At most one missing route is launched per poll.
- An open route PR suppresses duplicate execution.
- An open route PR without exactly one safety marker blocks the trial.
- `main`, `s`, and `t` must all be merged after the recorded XQ boundary before XQ starts.
- Codex never merges a PR; the existing merge monitor remains responsible for CI, conflict, draft, marker, and merge checks.
- A lock prevents overlapping scheduler instances.
- The scheduler gives each poll a two-hour execution limit and ignores a new trigger while the prior instance is running.
- The task disables itself only after a newly merged XQ is observed.

## Install

From the repository root in PowerShell:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\automation\install-stage14-autopilot-trial.ps1
```

Inspect progress:

```powershell
Get-Content "$env:LOCALAPPDATA\PerfectCuboidAutoPilot\trial.log" -Tail 30
Get-ScheduledTask -TaskName "PerfectCuboid-Stage14-AutoPilot-Trial"
```

Emergency stop:

```powershell
Disable-ScheduledTask -TaskName "PerfectCuboid-Stage14-AutoPilot-Trial"
```

The trial does not enable, disable, or modify the separate merge-monitor task.
