$ErrorActionPreference = "Continue"
$base = "C:\Users\Jonah\DevelopmentProjectTemplate"
$dirs = @("A","B","C")
$jobs = @()

foreach ($lane in $dirs) {
    $promptPath = Join-Path $base "b0ttsagent\temp\lane-$lane-prompt.txt"
    $prompt = Get-Content -Raw -LiteralPath $promptPath
    $title = "wave01-lane-$lane"
    $logFile = Join-Path $base "b0ttsagent\temp\wave01-lane-$lane.log"
    $errFile = Join-Path $base "b0ttsagent\temp\wave01-lane-$lane.err.log"
    # Use Start-Process to run opencode detached with output redirection
    $escapedPrompt = $prompt -replace '"','\"'
    # Write a small runner script per lane
    $runner = Join-Path $base "b0ttsagent\temp\runner-$lane.ps1"
    $runnerContent = @"
`$ErrorActionPreference = "Continue"
`$prompt = Get-Content -Raw -LiteralPath "$promptPath"
Set-Location -LiteralPath "$base"
& opencode run --agent b0tts-researcher --title "$title" --format json "`$prompt" 2>&1 | Out-File -LiteralPath "$logFile" -Encoding utf8
"@
    Set-Content -LiteralPath $runner -Value $runnerContent -Encoding utf8
    Write-Host "Launching lane $lane via $runner"
    $job = Start-Job -Name "wave01-$lane" -ScriptBlock {
        param($runnerPath)
        & powershell -NoProfile -ExecutionPolicy Bypass -File $runnerPath
    } -ArgumentList $runner
    $jobs += $job
    Start-Sleep -Seconds 2
}

Write-Host "All jobs launched: $($jobs.Count)"
Get-Job | Format-Table Name, State, HasMoreData -AutoSize
# Wait a bit and show status
Start-Sleep -Seconds 5
Get-Job | Format-Table Name, State -AutoSize
Get-ChildItem "b0ttsagent\temp\wave01-lane-*.log" -ErrorAction SilentlyContinue | Select-Object Name,Length | Format-Table -AutoSize
