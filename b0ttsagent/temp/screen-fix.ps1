$ErrorActionPreference = 'SilentlyContinue'
$out = 'C:\Users\intel\DevelopmentProjectTemplate\b0ttsagent\temp\lyricscreen'
$cands = @(
  @{n='Lizzo'; q='Lizzo official channel'; t='16c'},
  @{n='J. Cole'; q='J. Cole official channel'; t='18c'},
  @{n='HALIENE'; q='HALIENE official channel'; t='22c'}
)
foreach ($c in $cands) {
  $f = Join-Path $out ($c.t + '_search.json')
  $e = Join-Path $out ($c.t + '_search_err.txt')
  if (Test-Path $f) { Remove-Item $f -Force }
  yt-dlp --socket-timeout 15 --retries 2 -j --skip-download --no-warnings --playlist-items 1 "ytsearch1:$($c.q)" 1> $f 2> $e
  if (-not (Test-Path $f)) { Write-Output ($c.n + ' | NO DATA'); continue }
  $raw = Get-Content -Raw $f
  if ([string]::IsNullOrWhiteSpace($raw)) { Write-Output ($c.n + ' | EMPTY'); continue }
  try { $j = $raw | ConvertFrom-Json } catch { Write-Output ($c.n + ' | PARSE FAIL'); continue }
  $t = [string]$j.title
  if ($t.Length -gt 60) { $t = $t.Substring(0,60) + '...' }
  Write-Output ($c.n + ' | channel=' + $j.channel + ' | url=' + $j.channel_url + ' | subs=' + $j.channel_follower_count + ' | ' + $t + ' | views=' + $j.view_count)
}

Write-Output ''
Write-Output '=== FLAT FOR RESOLVED LIZZO + J COLE ==='
$resolve = @(
  @{n='Lizzo'; q='Lizzo official channel'; t='16d'},
  @{n='J. Cole'; q='J. Cole official channel'; t='18d'}
)
foreach ($c in $resolve) {
  $sf = Join-Path $out ($c.t + '_search.json')
  $se = Join-Path $out ($c.t + '_search_err.txt')
  if (Test-Path $sf) { Remove-Item $sf -Force }
  yt-dlp --socket-timeout 15 --retries 2 -j --skip-download --no-warnings --playlist-items 1 "ytsearch1:$($c.q)" 1> $sf 2> $se
  $raw = Get-Content -Raw $sf
  try { $j = $raw | ConvertFrom-Json } catch { Write-Output ($c.n + ' | SEARCH PARSE FAIL'); continue }
  $cu = [string]$j.channel_url
  $ff = Join-Path $out ($c.t + '_flat.json')
  $fe = Join-Path $out ($c.t + '_err.txt')
  if (Test-Path $ff) { Remove-Item $ff -Force }
  yt-dlp --socket-timeout 15 --retries 2 --flat-playlist -J ($cu + '/videos') 1> $ff 2> $fe
  if (-not (Test-Path $ff)) { Write-Output ($c.n + ' | FLAT NO DATA | channel=' + $j.channel); continue }
  $fraw = Get-Content -Raw $ff
  try { $fj = $fraw | ConvertFrom-Json } catch { Write-Output ($c.n + ' | FLAT PARSE FAIL'); continue }
  $entries = if ($fj -is [System.Array]) { @($fj) } else { @($fj.entries) }
  $withViews = @($entries | Where-Object { $null -ne $_.view_count })
  $ge100k = @($withViews | Where-Object { $_.view_count -ge 100000 }).Count
  $maxV = 0
  if ($withViews.Count -gt 0) { $maxV = ($withViews | Measure-Object -Property view_count -Maximum).Maximum }
  $top = @($withViews | Sort-Object view_count -Descending | Select-Object -First 3 | ForEach-Object {
    $t2 = [string]$_.title
    if ($t2.Length -gt 45) { $t2 = $t2.Substring(0,45) + '...' }
    "{0} ({1})" -f $t2, $_.view_count
  })
  Write-Output ($c.n + ' | channel=' + $j.channel + ' | entries=' + $entries.Count + ' | ge100k=' + $ge100k + ' | max=' + $maxV + ' | ' + ($top -join ' ;; '))
}
