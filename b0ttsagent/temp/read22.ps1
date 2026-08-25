$j = Get-Content -Raw 'C:\Users\intel\DevelopmentProjectTemplate\b0ttsagent\temp\lyricscreen\22_search.json' | ConvertFrom-Json
Write-Output ('channel=' + $j.channel)
Write-Output ('url=' + $j.channel_url)
Write-Output ('subs=' + $j.channel_follower_count)
Write-Output ('title=' + $j.title)
Write-Output ('views=' + $j.view_count)
