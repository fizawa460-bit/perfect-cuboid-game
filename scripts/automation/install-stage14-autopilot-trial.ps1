[CmdletBinding()]
param(
    [string]$TaskName = "PerfectCuboid-Stage14-AutoPilot-Trial",
    [int]$IntervalMinutes = 10
)

$ErrorActionPreference = "Stop"
$source = Join-Path $PSScriptRoot "stage14-autopilot-trial.ps1"
$root = Join-Path $env:LOCALAPPDATA "PerfectCuboidAutoPilot"
$target = Join-Path $root "stage14-autopilot-trial.ps1"

if (-not (Test-Path $source)) { throw "Runner not found: $source" }
if (-not (Get-Command git -ErrorAction SilentlyContinue)) { throw "git was not found" }
if (-not (Get-Command codex -ErrorAction SilentlyContinue)) { throw "codex was not found" }
if ($IntervalMinutes -lt 5) { throw "IntervalMinutes must be 5 or greater" }

New-Item -ItemType Directory -Force -Path $root | Out-Null
Copy-Item -LiteralPath $source -Destination $target -Force

$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$target`" -TaskName `"$TaskName`""
$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date).AddMinutes(1) -RepetitionInterval (New-TimeSpan -Minutes $IntervalMinutes)
$settings = New-ScheduledTaskSettingsSet -MultipleInstances IgnoreNew -StartWhenAvailable -ExecutionTimeLimit (New-TimeSpan -Hours 2)
$principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive -RunLevel Limited

Register-ScheduledTask -TaskName $TaskName -Action $action -Trigger $trigger -Settings $settings -Principal $principal -Description "One-cycle Stage14 main/s/t -> XQ Codex trial; disables itself after the new XQ merge." -Force | Out-Null

Write-Host "Registered: $TaskName"
Write-Host "Interval: $IntervalMinutes minutes"
Write-Host "Runner: $target"
Write-Host "Log: $(Join-Path $root 'trial.log')"
Write-Host "The first run starts in about one minute."
