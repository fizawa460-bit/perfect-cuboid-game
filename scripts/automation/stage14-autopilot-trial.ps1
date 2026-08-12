[CmdletBinding()]
param(
    [string]$Repository = "fizawa460-bit/perfect-cuboid-game",
    [string]$TaskName = "PerfectCuboid-Stage14-AutoPilot-Trial",
    [string]$Root = (Join-Path $env:LOCALAPPDATA "PerfectCuboidAutoPilot"),
    [int]$PollMinutes = 10
)

$ErrorActionPreference = "Stop"
$ProgressPreference = "SilentlyContinue"

$statePath = Join-Path $Root "trial-state.json"
$logPath = Join-Path $Root "trial.log"
$lockPath = Join-Path $Root "trial.lock"
$workspaceRoot = Join-Path $Root "workspaces"
$repoUrl = "https://github.com/$Repository.git"

New-Item -ItemType Directory -Force -Path $Root, $workspaceRoot | Out-Null

function Write-Log([string]$Message) {
    $line = "{0:u} {1}" -f (Get-Date), $Message
    Add-Content -LiteralPath $logPath -Value $line -Encoding UTF8
    Write-Host $line
}

function Stop-Trial([string]$Reason, [bool]$Completed = $false) {
    Write-Log $Reason
    if ($Completed) {
        try { Disable-ScheduledTask -TaskName $TaskName | Out-Null } catch { Write-Log "Task disable warning: $($_.Exception.Message)" }
    }
    exit 0
}

function Get-GitHubJson([string]$Uri) {
    $headers = @{ Accept = "application/vnd.github+json"; "User-Agent" = "PerfectCuboid-Stage14-AutoPilot-Trial" }
    if ($env:GITHUB_TOKEN) { $headers.Authorization = "Bearer $env:GITHUB_TOKEN" }
    Invoke-RestMethod -Uri $Uri -Headers $headers -Method Get
}

function Get-Route([string]$Body) {
    if (-not $Body) { return $null }
    $matches = [regex]::Matches($Body, '(?m)^STAGE14_ROUTE=(main|s|t|xq)\s*$')
    if ($matches.Count -ne 1) { return $null }
    $matches[0].Groups[1].Value
}

function Is-Safe([string]$Body) {
    if (-not $Body) { return $false }
    ([regex]::Matches($Body, '(?m)^STAGE14_AUTOMATION_SAFE=true\s*$')).Count -eq 1
}

function Get-MergedRoutePrs {
    $uri = "https://api.github.com/repos/$Repository/pulls?state=closed&sort=updated&direction=desc&per_page=100"
    @(Get-GitHubJson $uri) | Where-Object {
        $_.merged_at -and (Is-Safe $_.body) -and (Get-Route $_.body)
    }
}

function Get-OpenRoutePrs {
    $uri = "https://api.github.com/repos/$Repository/pulls?state=open&sort=updated&direction=desc&per_page=100"
    @(Get-GitHubJson $uri) | Where-Object { Get-Route $_.body }
}

function Save-State($State) {
    $State | ConvertTo-Json -Depth 5 | Set-Content -LiteralPath $statePath -Encoding UTF8
}

function Ensure-Workspace([string]$Route) {
    $path = Join-Path $workspaceRoot $Route
    if (-not (Test-Path (Join-Path $path ".git"))) {
        Write-Log "Cloning isolated workspace for route=$Route"
        & git clone --quiet $repoUrl $path
        if ($LASTEXITCODE -ne 0) { throw "git clone failed for $Route" }
    }
    & git -C $path fetch --quiet origin main
    if ($LASTEXITCODE -ne 0) { throw "git fetch failed for $Route" }
    & git -C $path switch --quiet main
    if ($LASTEXITCODE -ne 0) { throw "git switch main failed for $Route" }
    & git -C $path reset --quiet --hard origin/main
    if ($LASTEXITCODE -ne 0) { throw "git reset failed for $Route" }
    & git -C $path clean -quiet -fd
    if ($LASTEXITCODE -ne 0) { throw "git clean failed for $Route" }
    return $path
}

function Start-Route([string]$Route) {
    $batch = switch ($Route) {
        "main" { "Stage14-main-batch" }
        "s"    { "Stage14-s-batch" }
        "t"    { "Stage14-t-batch" }
        "xq"   { "Stage14-Work-toolbox-XQ" }
        default { throw "Unknown route: $Route" }
    }
    $path = Ensure-Workspace $Route
    $prompt = @"
$batch を1回だけ実行してください。

この実行はStage14自動試運転の一工程です。リポジトリ内のAGENTS.md、最新Stage14契約、引き継ぎ、直近成果を読み、次の規定バッチだけを実施してください。

必須条件:
- 現在のorigin/mainから専用ブランチを作成する
- 実施は1バッチだけ
- 必要な検算とテストを実行する
- コミットしてpushし、main向けDraft PRを1件作成する
- PR本文に次の2行を各1回だけ記載する
  STAGE14_AUTOMATION_SAFE=true
  STAGE14_ROUTE=$Route
- 自動マージや手動マージは禁止
- 競合、既存同一ルートPR、テスト失敗、判断不能なら変更せず停止する
- 完了時にPR番号、URL、コミットSHA、実施Stage名を回答する
"@
    Write-Log "Running route=$Route batch=$batch workspace=$path"
    $argList = @("--ask-for-approval", "never", "--sandbox", "danger-full-access", "exec", "--ephemeral", $prompt)
    Push-Location $path
    try {
        & codex @argList 2>&1 | Tee-Object -FilePath (Join-Path $Root "$Route.out.log") -Append
        if ($LASTEXITCODE -ne 0) { throw "codex failed for route=$Route with exit code $LASTEXITCODE" }
    } finally {
        Pop-Location
    }
    Write-Log "Codex completed route=$Route; GitHub state will be verified on the next poll."
}

$lock = $null
try {
    $lock = [System.IO.File]::Open($lockPath, 'OpenOrCreate', 'ReadWrite', 'None')
} catch {
    Stop-Trial "Another trial instance is running; waiting for the next poll."
}

try {
    if (-not (Get-Command git -ErrorAction SilentlyContinue)) { throw "git was not found" }
    if (-not (Get-Command codex -ErrorAction SilentlyContinue)) { throw "codex was not found" }

    $merged = @(Get-MergedRoutePrs)
    $open = @(Get-OpenRoutePrs)
    $latestXq = $merged | Where-Object { (Get-Route $_.body) -eq "xq" } | Sort-Object { [datetime]$_.merged_at } -Descending | Select-Object -First 1
    if (-not $latestXq) { throw "No merged safe XQ boundary was found in the latest 100 closed PRs" }

    if (Test-Path $statePath) {
        $state = Get-Content -LiteralPath $statePath -Raw | ConvertFrom-Json
    } else {
        $state = [pscustomobject]@{
            schema = 1
            baseline_xq_number = [int]$latestXq.number
            baseline_xq_merged_at = [string]$latestXq.merged_at
            started_at = (Get-Date).ToUniversalTime().ToString("o")
            launched = @()
        }
        Save-State $state
        Write-Log "Trial boundary recorded: XQ PR #$($state.baseline_xq_number) at $($state.baseline_xq_merged_at)"
    }

    $boundary = [datetime]$state.baseline_xq_merged_at
    $newXq = $merged | Where-Object { (Get-Route $_.body) -eq "xq" -and [datetime]$_.merged_at -gt $boundary } | Select-Object -First 1
    if ($newXq) { Stop-Trial "Trial completed: new XQ PR #$($newXq.number) is merged. AutoPilot trial task disabled." $true }

    $cycleMerged = @{}
    foreach ($pr in $merged) {
        if ([datetime]$pr.merged_at -gt $boundary) { $cycleMerged[(Get-Route $pr.body)] = $true }
    }
    $openByRoute = @{}
    foreach ($pr in $open) { $openByRoute[(Get-Route $pr.body)] = $pr }

    foreach ($route in @("main", "s", "t", "xq")) {
        if ($openByRoute[$route] -and -not (Is-Safe $openByRoute[$route].body)) {
            Stop-Trial "Blocked: route=$route has open PR #$($openByRoute[$route].number) without exactly one safety marker."
        }
    }

    $required = @("main", "s", "t")
    $missing = @($required | Where-Object { -not $cycleMerged[$_] -and -not $openByRoute[$_] })
    if ($missing.Count -gt 0) {
        $route = $missing[0]
        Start-Route $route
        $state.launched = @($state.launched) + [pscustomobject]@{ route = $route; at = (Get-Date).ToUniversalTime().ToString("o") }
        Save-State $state
        Stop-Trial "Completed Codex invocation for missing route=$route; next poll will re-evaluate GitHub state."
    }

    $pendingMst = @($required | Where-Object { -not $cycleMerged[$_] })
    if ($pendingMst.Count -gt 0) {
        Stop-Trial "Waiting for main/s/t PR merge: $($pendingMst -join ',')"
    }

    if ($openByRoute["xq"]) { Stop-Trial "Waiting for XQ PR #$($openByRoute['xq'].number) to merge." }
    Start-Route "xq"
    $state.launched = @($state.launched) + [pscustomobject]@{ route = "xq"; at = (Get-Date).ToUniversalTime().ToString("o") }
    Save-State $state
    Stop-Trial "Completed Codex invocation for XQ; trial will stop automatically after its merge is observed."
} catch {
    Write-Log "ERROR: $($_.Exception.Message)"
    exit 1
} finally {
    if ($lock) { $lock.Dispose() }
}
