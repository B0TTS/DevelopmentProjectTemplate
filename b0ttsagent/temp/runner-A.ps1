$ErrorActionPreference = "Continue"
$prompt = Get-Content -Raw -LiteralPath "C:\Users\Jonah\DevelopmentProjectTemplate\b0ttsagent\temp\lane-A-prompt.txt"
Set-Location -LiteralPath "C:\Users\Jonah\DevelopmentProjectTemplate"
& opencode run --agent b0tts-researcher --title "wave01-lane-A" --format json "$prompt" 2>&1 | Out-File -LiteralPath "C:\Users\Jonah\DevelopmentProjectTemplate\b0ttsagent\temp\wave01-lane-A.log" -Encoding utf8
