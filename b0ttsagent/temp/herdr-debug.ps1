$ErrorActionPreference = 'Continue'

Write-Host '=== config ==='
$config = Join-Path $env:APPDATA 'herdr\config.toml'
if (Test-Path $config) { Get-Content $config } else { Write-Host 'no config' }

Write-Host "`n=== herdr dir listing ==="
Get-ChildItem (Join-Path $env:APPDATA 'herdr') -Force -ErrorAction SilentlyContinue |
  Format-Table Name, Length, LastWriteTime, Mode -AutoSize

Write-Host "`n=== tail server log ==="
$serverLog = Join-Path $env:APPDATA 'herdr\herdr-server.log'
if (Test-Path $serverLog) { Get-Content $serverLog -Tail 100 } else { Write-Host 'no server log' }

Write-Host "`n=== tail client log ==="
$clientLog = Join-Path $env:APPDATA 'herdr\herdr-client.log'
if (Test-Path $clientLog) { Get-Content $clientLog -Tail 100 } else { Write-Host 'no client log' }

Write-Host "`n=== tail main log ==="
$mainLog = Join-Path $env:APPDATA 'herdr\herdr.log'
if (Test-Path $mainLog) { Get-Content $mainLog -Tail 100 } else { Write-Host 'no main log' }

Write-Host "`n=== interesting runtime files ==="
$roots = @(
  (Join-Path $env:LOCALAPPDATA 'herdr'),
  (Join-Path $env:APPDATA 'herdr'),
  $env:TEMP,
  (Join-Path $env:USERPROFILE '.herdr')
)
foreach ($root in $roots) {
  if (-not (Test-Path $root)) { continue }
  Get-ChildItem $root -Recurse -Force -ErrorAction SilentlyContinue |
    Where-Object {
      $_.Name -match 'sock|socket|session|runtime|lock|pipe' -or
      $_.Extension -match 'sock|pipe'
    } |
    Select-Object -First 40 FullName, Length, LastWriteTime
}

Write-Host "`n=== herdr status ==="
& (Join-Path $env:LOCALAPPDATA 'Programs\Herdr\bin\herdr.exe') status 2>&1

Write-Host "`n=== herdr session list if any ==="
& (Join-Path $env:LOCALAPPDATA 'Programs\Herdr\bin\herdr.exe') session --help 2>&1 | Select-Object -First 40
& (Join-Path $env:LOCALAPPDATA 'Programs\Herdr\bin\herdr.exe') session list 2>&1

Write-Host "`n=== processes ==="
Get-Process | Where-Object { $_.ProcessName -match 'herdr' } |
  Format-Table Id, ProcessName, Path -AutoSize

Write-Host "`n=== current package symlink ==="
Get-Item (Join-Path $env:USERPROFILE '.herdr\packages\standalone\current') -Force -ErrorAction SilentlyContinue |
  Format-List *
Get-ChildItem (Join-Path $env:USERPROFILE '.herdr\packages\standalone\current') -Force -ErrorAction SilentlyContinue |
  Format-Table Name, Length, Mode -AutoSize
Get-ChildItem (Join-Path $env:USERPROFILE '.herdr\packages\standalone\releases') -Recurse -Depth 2 -Force -ErrorAction SilentlyContinue |
  Format-Table FullName, Length, Mode -AutoSize
