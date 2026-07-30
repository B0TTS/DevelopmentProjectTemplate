$ErrorActionPreference = 'Continue'

$paths = @(
  'C:\Users\Jonah\AppData\Local\Programs\Herdr\bin\herdr.exe',
  'C:\Users\Jonah\.herdr\packages\standalone\current\herdr.exe',
  'C:\Users\Jonah\.herdr\packages\standalone\releases\0.7.4-preview.2026-07-17-813fec141faa-x86_64-pc-windows-msvc\herdr.exe',
  'C:\Users\Jonah\Downloads\SetupFIles\herdr-windows-x86_64.exe'
)

foreach ($p in $paths) {
  Write-Host "==== $p ===="
  if (-not (Test-Path -LiteralPath $p)) { Write-Host 'MISSING'; continue }
  cmd /c "dir /al `"$p`"" 2>&1
  fsutil hardlink list $p 2>&1 | Select-Object -First 20
  $item = Get-Item -LiteralPath $p -Force
  Write-Host ("Attributes={0} LinkType={1}" -f $item.Attributes, $item.LinkType)
  try {
    $out = & $p --version 2>&1
    Write-Host "version: $out"
  } catch {
    Write-Host "run failed: $_"
  }
  Write-Host ''
}

Write-Host '=== create durable launcher in always-on PATH location ==='
$launchDir = 'C:\ProgramData\herdr-launch'
$launchPs1 = Join-Path $launchDir 'herdr.cmd'
New-Item -ItemType Directory -Force -Path $launchDir | Out-Null

# Resolve real binary (prefer package release path, then programs bin)
$real = 'C:\Users\Jonah\.herdr\packages\standalone\releases\0.7.4-preview.2026-07-17-813fec141faa-x86_64-pc-windows-msvc\herdr.exe'
if (-not (Test-Path -LiteralPath $real)) {
  $real = 'C:\Users\Jonah\AppData\Local\Programs\Herdr\bin\herdr.exe'
}

@(
  '@echo off'
  'setlocal'
  "set `"HERDR_BIN=$real`""
  'if not exist "%HERDR_BIN%" ('
  '  echo herdr launcher: binary missing: %HERDR_BIN%'
  '  exit /b 1'
  ')'
  '"%HERDR_BIN%" %*'
) | Set-Content -Path $launchPs1 -Encoding ASCII

# Copy a stable herdr.cmd name people can type, and also put on machine path if needed
Write-Host "Launcher written: $launchPs1"
Write-Host "Target binary: $real"

$machinePath = [Environment]::GetEnvironmentVariable('Path', 'Machine')
if ($machinePath -notlike "*$launchDir*") {
  [Environment]::SetEnvironmentVariable('Path', "$machinePath;$launchDir", 'Machine')
  Write-Host "Added $launchDir to machine PATH"
} else {
  Write-Host 'launch dir already on machine PATH'
}

# Also copy real exe into ProgramData as herdr.exe for maximum dumb compatibility
$copied = Join-Path $launchDir 'herdr.exe'
Copy-Item -LiteralPath $real -Destination $copied -Force
Write-Host "Copied binary to $copied"
Get-Item $copied, $launchPs1 | Format-Table FullName, Length, LastWriteTime -AutoSize

Write-Host "`n=== verify launcher with machine-only PATH ==="
$env:Path = [Environment]::GetEnvironmentVariable('Path', 'Machine')
where.exe herdr 2>&1
& herdr --version 2>&1
& herdr status 2>&1

Write-Host "`n=== note: restart sshd so new PATH is picked up ==="
try {
  Restart-Service sshd -ErrorAction Stop
  Write-Host 'sshd restarted'
} catch {
  Write-Host "sshd restart failed (need admin?): $_"
}
