$ErrorActionPreference = 'SilentlyContinue'
$out = 'C:\Users\intel\DevelopmentProjectTemplate\b0ttsagent\temp\lyricscreen'
$cands = @(
  @{n='01 Charlie Puth'; u='https://www.youtube.com/channel/UCwppdrjsBPAZg5_cUwQjfMQ'; q='Charlie Puth'},
  @{n='02 Mike Shinoda'; u='https://www.youtube.com/@mikeshinoda'; q='Mike Shinoda'},
  @{n='03 Jon Bellion'; u='https://www.youtube.com/@jonbellion'; q='Jon Bellion'},
  @{n='04 AJR'; u='https://www.youtube.com/@AJR'; q='AJR band'},
  @{n='05 Logic'; u='https://www.youtube.com/@logic'; q='Logic rapper'},
  @{n='06 Russ'; u='https://www.youtube.com/@russ'; q='Russ rapper'},
  @{n='07 Hanumankind'; u='https://www.youtube.com/@hanumankind'; q='Hanumankind'},
  @{n='08 mgk'; u='https://www.youtube.com/@mgk'; q='Machine Gun Kelly'},
  @{n='09 San Holo'; u='https://www.youtube.com/@sanholobeats'; q='San Holo'},
  @{n='10 Olivia Dean'; u='https://www.youtube.com/channel/UCT3cEUoL1X0_BxN6q7LVH1w'; q='Olivia Dean'},
  @{n='11 Tessa Violet'; u='https://www.youtube.com/channel/UCOw4v1j3QnzH7X4krQAS7fg'; q='Tessa Violet'}
)

function Get-Flat([string]$u, [string]$tag) {
  $f = Join-Path $out "${tag}_flat.json"
  $e = Join-Path $out "${tag}_err.txt"
  if (Test-Path $f) { Remove-Item $f -Force }
  if (Test-Path $e) { Remove-Item $e -Force }
  $u2 = $u
  if ($u2 -notmatch '/videos$') { $u2 = "$u2/videos" }
  yt-dlp --socket-timeout 15 --retries 2 --flat-playlist -J $u2 1> $f 2> $e
  if (-not (Test-Path $f)) { return $null }
  $raw = Get-Content -Raw $f
  if ([string]::IsNullOrWhiteSpace($raw)) { return $null }
  try { $j = $raw | ConvertFrom-Json } catch { return $null }
  if ($j -is [System.Array]) { return @($j) } else { return @($j.entries) }
}

function Get-Resolve([string]$query, [string]$tag) {
  $f = Join-Path $out "${tag}_search.json"
  $e = Join-Path $out "${tag}_search_err.txt"
  if (Test-Path $f) { Remove-Item $f -Force }
  if (Test-Path $e) { Remove-Item $e -Force }
  yt-dlp --socket-timeout 15 --retries 2 -j --skip-download --no-warnings --playlist-items 1 "ytsearch1:$query" 1> $f 2> $e
  if (-not (Test-Path $f)) { return $null }
  $raw = Get-Content -Raw $f
  if ([string]::IsNullOrWhiteSpace($raw)) { return $null }
  try { return ($raw | ConvertFrom-Json) } catch { return $null }
}

$i = 0
foreach ($c in $cands) {
  $tag = ('{0:d2}' -f ($i + 1))
  $entries = Get-Flat $c.u $tag
  $how = 'direct'
  if ($null -eq $entries -or $entries.Count -eq 0) {
    $how = 'FALLBACK'
    $hit = Get-Resolve "$($c.q) official" $tag
    if ($null -ne $hit -and $hit.channel_url) {
      $entries = Get-Flat ([string]$hit.channel_url) "${tag}b"
    } else { $entries = $null }
  }
  if ($null -eq $entries -or $entries.Count -eq 0) {
    Write-Output ("{0} | {1} | {2} | NO DATA" -f $tag, $c.n, $how)
    continue
  }
  $withViews = @($entries | Where-Object { $null -ne $_.view_count })
  $ge100k = @($withViews | Where-Object { $_.view_count -ge 100000 }).Count
  $maxV = 0
  if ($withViews.Count -gt 0) { $maxV = ($withViews | Measure-Object -Property view_count -Maximum).Maximum }
  $top = @($withViews | Sort-Object view_count -Descending | Select-Object -First 3 | ForEach-Object {
    $t = [string]$_.title
    if ($t.Length -gt 45) { $t = $t.Substring(0,45) + '...' }
    "{0} ({1})" -f $t, $_.view_count
  })
  Write-Output ("{0} | {1} | {2} | entries={3} | ge100k={4} | max={5} | {6}" -f $tag, $c.n, $how, $entries.Count, $ge100k, $maxV, ($top -join ' ;; '))
}
