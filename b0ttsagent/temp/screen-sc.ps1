$ErrorActionPreference = 'SilentlyContinue'
$out = 'C:\Users\intel\DevelopmentProjectTemplate\b0ttsagent\temp\lyricscreen'

Write-Output '=== TIER-2 CREDIT CHECKS (ytsearch1: credited song, official upload views) ==='
$credits = @(
  @{n='23 Ryan S. Jhun'; q='IVE ELEVEN'},
  @{n='24 Toby Gad'; q='John Legend All of Me'},
  @{n='25 Ross Golan'; q='Ariana Grande Dangerous Woman'},
  @{n='26 Nicolle Galyon'; q='Dan + Shay Tequila'},
  @{n='27 Brent Baxter'; q='Alan Jackson Monday Morning Church'},
  @{n='28 ADORA'; q='BTS Spring Day'}
)
foreach ($c in $credits) {
  $f = Join-Path $out ("{0}_credit.json" -f ($c.n.Substring(0,2)))
  $e = Join-Path $out ("{0}_credit_err.txt" -f ($c.n.Substring(0,2)))
  if (Test-Path $f) { Remove-Item $f -Force }
  if (Test-Path $e) { Remove-Item $e -Force }
  yt-dlp --socket-timeout 15 --retries 2 -j --skip-download --no-warnings --playlist-items 1 "ytsearch1:$($c.q)" 1> $f 2> $e
  if (-not (Test-Path $f)) { Write-Output ("{0} | NO DATA" -f $c.n); continue }
  $raw = Get-Content -Raw $f
  if ([string]::IsNullOrWhiteSpace($raw)) { Write-Output ("{0} | EMPTY" -f $c.n); continue }
  try { $j = $raw | ConvertFrom-Json } catch { Write-Output ("{0} | PARSE FAIL" -f $c.n); continue }
  $t = [string]$j.title
  if ($t.Length -gt 60) { $t = $t.Substring(0,60) + '...' }
  Write-Output ("{0} | query={1} | views={2} | date={3} | channel={4} | {5}" -f $c.n, $c.q, $j.view_count, $j.upload_date, $j.channel, $t)
}

Write-Output ''
Write-Output '=== SOUNDCLOUD TRACK LISTS (flat-playlist) ==='
$scs = @(
  @{n='Charlie Puth'; h='charlieputh'},
  @{n='San Holo'; h='sanholobeats'},
  @{n='Toby Gad'; h='tobygadmusic'},
  @{n='HALIENE'; h='halienemusic'}
)
foreach ($s in $scs) {
  $f = Join-Path $out ("sc_{0}.json" -f $s.h)
  $e = Join-Path $out ("sc_{0}_err.txt" -f $s.h)
  if (Test-Path $f) { Remove-Item $f -Force }
  if (Test-Path $e) { Remove-Item $e -Force }
  yt-dlp --socket-timeout 15 --retries 2 --ignore-no-formats-error --flat-playlist -J "https://soundcloud.com/$($s.h)" 1> $f 2> $e
  if (-not (Test-Path $f)) { Write-Output ("{0} | NO DATA" -f $s.n); continue }
  $raw = Get-Content -Raw $f
  if ([string]::IsNullOrWhiteSpace($raw)) { Write-Output ("{0} | EMPTY" -f $s.n); continue }
  try { $j = $raw | ConvertFrom-Json } catch { Write-Output ("{0} | PARSE FAIL" -f $s.n); continue }
  $entries = if ($j -is [System.Array]) { @($j) } else { @($j.entries) }
  $top = @($entries | Select-Object -First 5 | ForEach-Object { [string]$_.title })
  Write-Output ("{0} | tracks={1} | first: {2}" -f $s.n, $entries.Count, ($top -join ' ;; '))
}
