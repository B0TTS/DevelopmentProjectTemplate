$ErrorActionPreference = 'Continue'
$app = 'C:\Users\Jonah\AppData\Roaming\herdr'
$bin = 'C:\Users\Jonah\AppData\Local\Programs\Herdr\bin\herdr.exe'

Write-Host '=== PATH herdr entries ==='
([Environment]::GetEnvironmentVariable('Path','Machine') + ';' + [Environment]::GetEnvironmentVariable('Path','User') -split ';') |
  Where-Object { $_ -match 'Herdr' } | ForEach-Object { $_ }

Write-Host "`n=== where / version / status ==="
$env:Path = [Environment]::GetEnvironmentVariable('Path','Machine') + ';' + [Environment]::GetEnvironmentVariable('Path','User')
where.exe herdr
& $bin --version
& $bin status
& $bin session list

Write-Host "`n=== try attach-like noninteractive (may fail without TTY) ==="
$psi = New-Object System.Diagnostics.ProcessStartInfo
$psi.FileName = $bin
$psi.Arguments = ''
$psi.UseShellExecute = $false
$psi.RedirectStandardOutput = $true
$psi.RedirectStandardError = $true
$psi.RedirectStandardInput = $true
$psi.CreateNoWindow = $true
$psi.Environment['TERM'] = 'xterm-256color'
$psi.Environment['COLORTERM'] = 'truecolor'
try {
  $p = [Diagnostics.Process]::Start($psi)
  Start-Sleep -Milliseconds 1500
  if (-not $p.HasExited) {
    Write-Host "still running after 1.5s pid=$($p.Id) - killing (expected without real TTY maybe)"
    $p.Kill()
  } else {
    Write-Host "exited quickly code=$($p.ExitCode)"
    Write-Host 'stdout:'; $p.StandardOutput.ReadToEnd()
    Write-Host 'stderr:'; $p.StandardError.ReadToEnd()
  }
} catch {
  Write-Host "start failed: $_"
}

Write-Host "`n=== latest client log ==="
Get-Content (Join-Path $app 'herdr-client.log') -Tail 30
Write-Host "`n=== latest server log ==="
Get-Content (Join-Path $app 'herdr-server.log') -Tail 40

Write-Host "`n=== OpenSSH auth log recent ==="
try {
  Get-WinEvent -LogName 'OpenSSH/Operational' -MaxEvents 15 |
    Format-Table TimeCreated, Message -Wrap
} catch {
  Write-Host $_
}
