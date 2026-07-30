$ErrorActionPreference = 'Continue'
$app = Join-Path $env:APPDATA 'herdr'

Write-Host '=== recent client log ==='
Get-Content (Join-Path $app 'herdr-client.log') -Tail 30

Write-Host "`n=== session.json ==="
Get-Content (Join-Path $app 'session.json') -Raw

Write-Host "`n=== socket files ==="
Get-ChildItem $app -Force | Format-Table Name, Length, LastWriteTime -AutoSize

Write-Host "`n=== PATH contains Herdr? ==="
($env:Path -split ';') | Where-Object { $_ -match 'Herdr|herdr' }

Write-Host "`n=== user vs machine path herdr ==="
'User: ' + (([Environment]::GetEnvironmentVariable('Path','User') -split ';') | Where-Object { $_ -match 'Herdr' })
'Machine: ' + (([Environment]::GetEnvironmentVariable('Path','Machine') -split ';') | Where-Object { $_ -match 'Herdr' })

Write-Host "`n=== OpenSSH DefaultShell ==="
Get-ItemProperty 'HKLM:\SOFTWARE\OpenSSH' -ErrorAction SilentlyContinue | Format-List *

Write-Host "`n=== try herdr with TERM set like mobile ==="
$env:TERM = 'xterm-256color'
& (Join-Path $env:LOCALAPPDATA 'Programs\Herdr\bin\herdr.exe') status 2>&1

Write-Host "`n=== process owners ==="
Get-CimInstance Win32_Process -Filter "Name like '%herdr%'" |
  Select-Object ProcessId, Name, ExecutablePath, CommandLine |
  Format-List
