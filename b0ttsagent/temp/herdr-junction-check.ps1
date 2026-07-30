$ErrorActionPreference = 'Continue'

Write-Host '=== TYPE OF Programs\Herdr\bin ==='
$herdrBin = 'C:\Users\Jonah\AppData\Local\Programs\Herdr\bin'
(Get-Item $herdrBin -Force) | Format-List FullName, Attributes, LinkType, Target, ReparsePoint

Write-Host "`n=== TYPE OF herdr.exe inside it (from programs dir) ==="
$herdrExeProg = Join-Path $herdrBin 'herdr.exe'
(Get-Item $herdrExeProg -Force) | Format-List FullName, Attributes, LinkType

Write-Host "`n=== TYPE OF .herdr\packages\standalone\current ==="
(Get-Item 'C:\Users\Jonah\.herdr\packages\standalone\current' -Force) |
  Format-List FullName, Attributes, LinkType, Target

Write-Host "`n=== TYPE OF .herdr\packages\standalone\current\herdr.exe ==="
(Get-Item 'C:\Users\Jonah\.herdr\packages\standalone\current\herdr.exe' -Force) |
  Format-List FullName, Attributes, LinkType

Write-Host "`n=== real binary hardlinks? ==="
$real = 'C:\Users\Jonah\.herdr\packages\standalone\releases\0.7.4-preview.2026-07-17-813fec141faa-x86_64-pc-windows-msvc\herdr.exe'
fsutil hardlink list $real 2>&1

Write-Host "`n=== can we see the Programs directory itself from 'outside'? ==="
$psi = New-Object System.Diagnostics.ProcessStartInfo
$psi.FileName = 'cmd.exe'
$psi.Arguments = '/c dir "C:\Users\Jonah\AppData\Local\Programs\Herdr\bin" 2>&1'
$psi.UseShellExecute = $false
$psi.RedirectStandardOutput = $true
$psi.RedirectStandardError = $true
$psi.LoadUserProfile = $false  # simulate SSH-ish noninteractive
$p = [Diagnostics.Process]::Start($psi)
$out = $p.StandardOutput.ReadToEnd()
$err = $p.StandardError.ReadToEnd()
$p.WaitForExit()
Write-Host "stdout: $out"
Write-Host "stderr: $err"
Write-Host "exit: $($p.ExitCode)"

Write-Host "`n=== can we run absolute path through noninteractive? ==="
$psi2 = New-Object System.Diagnostics.ProcessStartInfo
$psi2.FileName = $real
$psi2.Arguments = '--version'
$psi2.UseShellExecute = $false
$psi2.RedirectStandardOutput = $true
$psi2.RedirectStandardError = $true
$psi2.LoadUserProfile = $false
$p2 = [Diagnostics.Process]::Start($psi2)
$out2 = $p2.StandardOutput.ReadToEnd()
$err2 = $p2.StandardError.ReadToEnd()
$p2.WaitForExit()
Write-Host "stdout: $out2"
Write-Host "stderr: $err2"
Write-Host "exit: $($p2.ExitCode)"

Write-Host "`n=== SSH shell type ==="
Get-ItemProperty 'HKLM:\SOFTWARE\OpenSSH' -ErrorAction SilentlyContinue | Format-List DefaultShell
try {
  $regUser = [Microsoft.Win32.Registry]::CurrentUser.OpenSubKey('SOFTWARE\OpenSSH')
  if ($regUser) { $regUser.GetValue('DefaultShell'); $regUser.Close() }
} catch { }
