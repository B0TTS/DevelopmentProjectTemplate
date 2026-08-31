$ErrorActionPreference = "Continue"
$prompt = Get-Content -Raw -LiteralPath "C:\Users\Jonah\DevelopmentProjectTemplate\b0ttsagent\temp\lane-C-prompt.txt"
Set-Location -LiteralPath "C:\Users\Jonah\DevelopmentProjectTemplate"
& opencode run --agent b0tts-researcher --title "wave01-lane-C" --format json "$prompt" 2>&1 | Out-File -LiteralPath "C:\Users\Jonah\DevelopmentProjectTemplate\b0ttsagent\temp\wave01-lane-C.log" -Encoding utf8
