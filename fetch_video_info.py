import urllib.request
import json
import re

# 1. YouTube video info
yt_url = 'https://www.youtube.com/watch?v=vnrxk-KmIq8'
req = urllib.request.Request(yt_url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    with urllib.request.urlopen(req) as resp:
        html = resp.read().decode('utf-8', errors='ignore')
        title_m = re.search(r'<title>(.*?)</title>', html)
        print("YouTube Title:", title_m.group(1) if title_m else "Not found")
        desc_m = re.search(r'"shortDescription":"(.*?)"', html)
        if desc_m:
            print("YouTube Description:", desc_m.group(1)[:300])
except Exception as e:
    print("YouTube error:", e)

# Check if youtube_transcript_api is available
try:
    import youtube_transcript_api
    print("youtube_transcript_api is installed!")
except ImportError:
    print("youtube_transcript_api is NOT installed.")
