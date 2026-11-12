from youtube_transcript_api import YouTubeTranscriptApi
import json

video_id = 'vnrxk-KmIq8'
try:
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    text = " ".join([t['text'] for t in transcript])
    print(f"Retrieved YouTube transcript! Total characters: {len(text)}, Words: {len(text.split())}")
    with open("G:/My Drive/Academics/vincent_chin_transcript.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print("Saved to vincent_chin_transcript.txt")
except Exception as e:
    print(f"Error fetching transcript: {e}")
