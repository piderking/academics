import urllib.request
import json

url = 'https://archive.org/metadata/Japanese1943/files'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    with urllib.request.urlopen(req) as resp:
        files = json.loads(resp.read().decode('utf-8')).get('result', [])
        for f in files:
            name = f.get('name', '')
            fmt = f.get('format', '')
            if any(ext in name.lower() for ext in ['.srt', '.vtt', '.txt', '.xml', 'transcript']):
                print(f"Transcript/Sub file: {name} ({fmt})")
except Exception as e:
    print("Error:", e)
