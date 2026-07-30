$ErrorActionPreference = 'Continue'

Write-Host '=== machine PATH herdr entry ==='
$machinePath = [Environment]::GetEnvironmentVariable('Path', 'Machine')
($machinePath -split ';') | Where-Object { $_ -match 'Herdr|herdr' } | ForEach-Object { "MACHINE: $_" }

Write-Host "`n=== user PATH herdr entry ==="
$userPath = [Environment]::GetEnvironmentVariable('Path', 'User')
($userPath -split ';') | Where-Object { $_ -match 'Herdr|herdr' } | ForEach-Object { "USER: $_" }

Write-Host "`n=== current process PATH herdr entry ==="
($env:Path -split ';') | Where-Object { $_ -match 'Herdr|herdr' } | ForEach-Object { "PROC: $_" }

Write-Host "`n=== binary exists? ==="
$bin = 'C:\Users\Jonah\AppData\Local\Programs\Herdr\bin\herdr.exe'
Test-Path $bin
Get-Item $bin | Format-List FullName, Length, LastWriteTime, LinkType, Target

Write-Host "`n=== junction target contents ==="
$current = 'C:\Users\Jonah\.herdr\packages\standalone\current'
Get-Item $current -Force | Format-List FullName, LinkType, Target, Attributes
Get-ChildItem $current -Force | Format-Table Name, Length, Mode -AutoSize
Get-ChildItem 'C:\Users\Jonah\AppData\Local\Programs\Herdr\bin' -Force | Format-Table Name, Length, Mode, LinkType -AutoSize

Write-Host "`n=== simulate OpenSSH default cmd PATH (machine only) ==="
$sshishPath = $machinePath
$env:Path = $sshishPath
Write-Host "where herdr:"
& where.exe herdr 2>&1
Write-Host "herdr --version:"
& herdr --version 2>&1
Write-Host "herdr status:"
& herdr status 2>&1

Write-Host "`n=== simulate machine+user PATH ==="
$env:Path = "$machinePath;$userPath"
Write-Host "where herdr:"
& where.exe herdr 2>&1
Write-Host "herdr --version:"
& herdr --version 2>&1

Write-Host "`n=== actual SSH local probe as Jonah ==="
# Use the live sshd path via localhost if key auth works; fall back to ssh with BatchMode
$sshTests = @(
  'echo PATH=%PATH%',
  'where herdr',
  'herdr --version',
  'herdr status',
  'dir "C:\Users\Jonah\AppData\Local\Programs\Herdr\bin"',
  'dir "C:\Users\Jonah\.herdr\packages\standalone\current"'
)
foreach ($cmd in $sshTests) {
  Write-Host "`n--- ssh cmd: $cmd ---"
  # Prefer PowerShell remote command through ssh if available
  & ssh.exe -o BatchMode=yes -o ConnectTimeout=5 Jonah@127.0.0.1 $cmd 2>&1
}

Write-Host "`n=== OpenSSH config bits ==="
Get-ItemProperty 'HKLM:\SOFTWARE\OpenSSH' -ErrorAction SilentlyContinue | Format-List *
if (Test-Path 'C:\ProgramData\ssh\sshd_config') {
  Select-String -Path 'C:\ProgramData\ssh\sshd_config' -Pattern 'DefaultShell|PermitUserEnvironment|Subsystem|ForceCommand|Chroot|Match' |
    ForEach-Object { $_.Line }
}

Write-Host "`n=== recent herdr client/server after presumed moshi attempts ==="
$app = 'C:\Users\Jonah\AppData\Roaming\herdr'
Get-Content (Join-Path $app 'herdr-client.log') -Tail 40
Write-Host '--- server ---'
Get-Content (Join-Path $app 'herdr-server.log') -Tail 40

Write-Host "`n=== processes ==="
Get-CimInstance Win32_Process -Filter "Name like '%herdr%'" |
  Select-Object ProcessId, Name, ExecutablePath, CommandLine |
  Format-List
