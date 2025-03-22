from youtube_transcript_api import YouTubeTranscriptApi

def get_video_transcript(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        text = " ".join([t['text'] for t in transcript])
        return text
    except Exception as e:
        return f"Error: {str(e)}"

# Example Usage
video_id = "v=liJVSwOiiwg"  # Replace with your YouTube video ID
print(get_video_transcript(video_id))
