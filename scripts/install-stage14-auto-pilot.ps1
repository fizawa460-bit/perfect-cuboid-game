param(
    [string]$RepositoryPath = (Resolve-Path (Join-Path $PSScriptRoot "..")),
    [int]$Minutes = 30,
    [switch]$WhatIf
)

$ErrorActionPreference = "Stop"
$taskName = "PerfectCuboid-Stage14-AutoPilot"
$worker = Join-Path $RepositoryPath "scripts\stage14-auto-pilot.ps1"

if (-not (Test-Path $worker)) {
    throw "Worker script was not found: $worker"
}
if ($Minutes -lt 5) {
    throw "The interval must be at least 5 minutes."
}

$arguments = "-NoProfile -ExecutionPolicy Bypass -File `"$worker`""
if ($WhatIf) {
    $arguments += " -WhatIf"
}

$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument $arguments -WorkingDirectory $RepositoryPath
$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date).AddMinutes(1) `
    -RepetitionInterval (New-TimeSpan -Minutes $Minutes)
$settings = New-ScheduledTaskSettingsSet -MultipleInstances IgnoreNew -StartWhenAvailable `
    -ExecutionTimeLimit (New-TimeSpan -Minutes 20)
$principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -LogonType Interactive -RunLevel Limited

Register-ScheduledTask -TaskName $taskName -Action $action -Trigger $trigger `
    -Settings $settings -Principal $principal -Force | Out-Null

Write-Output "Installed scheduled task: $taskName"
Write-Output "Interval: $Minutes minutes"
Write-Output "Mode: $(if ($WhatIf) { 'WhatIf (no merges)' } else { 'live' })"
Write-Output "The task runs only while this Windows user is logged on."

