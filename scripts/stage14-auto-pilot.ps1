param(
    [string]$Repository = "fizawa460-bit/perfect-cuboid-game",
    [string]$Owner = "fizawa460-bit",
    [switch]$WhatIf
)

$ErrorActionPreference = "Stop"
$safeMarker = "STAGE14_AUTOMATION_SAFE=true"
$routePattern = "(?m)^STAGE14_ROUTE=(main|s|t|xq)\s*$"
$stopPattern = "(?im)\b(BLOCKED|DO_NOT_MERGE|AUTOMATION_STOP)\b"

function Write-Log([string]$Message) {
    $stamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Output "[$stamp] $Message"
}

if (-not (Get-Command gh -ErrorAction SilentlyContinue)) {
    throw "GitHub CLI (gh) is not installed or is not on PATH."
}

gh auth status | Out-Null
if ($LASTEXITCODE -ne 0) {
    throw "GitHub CLI is not authenticated. Run: gh auth login"
}

$json = gh pr list --repo $Repository --state open --author $Owner --limit 100 `
    --json number,title,body,author,isDraft,mergeStateStatus,statusCheckRollup,baseRefName,url
if ($LASTEXITCODE -ne 0) {
    throw "Could not list pull requests for $Repository."
}

$pullRequests = @($json | ConvertFrom-Json)
$candidates = @($pullRequests | Where-Object {
    $_.author.login -eq $Owner -and
    $_.baseRefName -eq "main" -and
    $_.body -match "(?m)^$([regex]::Escape($safeMarker))\s*$" -and
    $_.body -match $routePattern
})

if ($candidates.Count -eq 0) {
    Write-Log "No automation-safe PR is open."
    exit 0
}

foreach ($pr in ($candidates | Sort-Object number)) {
    $routeMatches = [regex]::Matches($pr.body, $routePattern)
    if ($routeMatches.Count -ne 1) {
        throw "PR #$($pr.number) must contain exactly one STAGE14_ROUTE marker."
    }
    $route = $routeMatches[0].Groups[1].Value
    Write-Log "Inspecting PR #$($pr.number) route=${route}: $($pr.title)"

    if ($pr.body -match $stopPattern) {
        throw "PR #$($pr.number) contains a stop marker. Manual review is required: $($pr.url)"
    }

    if ($pr.mergeStateStatus -notin @("CLEAN", "HAS_HOOKS", "UNSTABLE")) {
        Write-Log "PR #$($pr.number) is not merge-ready (mergeStateStatus=$($pr.mergeStateStatus)); leaving it open."
        continue
    }

    $checks = @($pr.statusCheckRollup)
    if ($checks.Count -eq 0) {
        Write-Log "PR #$($pr.number) has no reported checks; refusing automatic merge."
        continue
    }

    $pending = @($checks | Where-Object {
        ($_.status -and $_.status -ne "COMPLETED") -or
        ($_.conclusion -and $_.conclusion -notin @("SUCCESS", "NEUTRAL", "SKIPPED")) -or
        ($_.state -and $_.state -notin @("SUCCESS", "NEUTRAL", "EXPECTED"))
    })
    if ($pending.Count -gt 0) {
        Write-Log "PR #$($pr.number) has pending or unsuccessful checks; leaving it open."
        continue
    }

    if ($WhatIf) {
        Write-Log "WhatIf: PR #$($pr.number) would be marked ready and squash-merged."
        continue
    }

    if ($pr.isDraft) {
        gh pr ready $pr.number --repo $Repository | Out-Null
        if ($LASTEXITCODE -ne 0) {
            throw "Could not mark PR #$($pr.number) ready."
        }
    }

    gh pr merge $pr.number --repo $Repository --squash --delete-branch
    if ($LASTEXITCODE -ne 0) {
        throw "Merge failed for PR #$($pr.number). Automatic processing stopped."
    }
    Write-Log "Merged PR #$($pr.number)."

    # Merge one PR per invocation. This lets GitHub recompute conflicts and CI
    # against the new main before another branch is accepted.
    exit 0
}

Write-Log "No open automation-safe PR currently satisfies every merge gate."
