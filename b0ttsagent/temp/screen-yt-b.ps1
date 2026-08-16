$ErrorActionPreference = 'SilentlyContinue'
$out = 'C:\Users\intel\DevelopmentProjectTemplate\b0ttsagent\temp\lyricscreen'
$cands = @(
  @{n='12 Jack Harlow'; u='https://www.youtube.com/channel/UC6vZl7Qj7JglLDmN_7Or-ZQ'; q='Jack Harlow'},
  @{n='13 Gracie Abrams'; u='https://www.youtube.com/gracieabrams'; q='Gracie Abrams'},
  @{n='14 Raye'; u='https://www.youtube.com/channel/UCw5z_dopYnvEL6Rc8KNKsnw'; q='RAYE singer'},
  @{n='15 Billie Eilish'; u='https://www.youtube.com/@billieeilish'; q='Billie Eilish'},
  @{n='16 Lizzo'; u='https://www.youtube.com/@LizzoMusic'; q='Lizzo'},
  @{n='17 Denzel Curry'; u='https://www.youtube.com/channel/UCiKxNv_MHAShqT2lATxG_Wg'; q='Denzel Curry'},
  @{n='18 J. Cole'; u='https://www.youtube.com/@JColeNC'; q='J. Cole'},
  @{n='19 Porter Robinson'; u='https://www.youtube.com/channel/UCKKKYE55BVswHgKihx5YXew'; q='Porter Robinson'},
  @{n='20 Laufey'; u='https://www.youtube.com/@laufey'; q='Laufey'},
  @{n='21 Maggie Rogers'; u='https://www.youtube.com/@maggierogers'; q='Maggie Rogers'},
  @{n='22 HALIENE'; u='https://www.youtube.com/@HALIENEmusic'; q='HALIENE'}
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

$i = 11
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
    $i++
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
  $i++
}
