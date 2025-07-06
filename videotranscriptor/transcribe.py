from pathlib import Path
from typing import List, Dict

try:
    import whisper
except ImportError as e:
    whisper = None


def transcribe_video(video_path: str, model: str = "base") -> List[Dict]:
    """Transcribe a video file using OpenAI Whisper."""
    if whisper is None:
        raise ImportError("whisper package is required for transcription")
    model = whisper.load_model(model)
    result = model.transcribe(video_path)
    return result.get("segments", [])


def format_timestamp(seconds: float) -> str:
    hours = int(seconds // 3600)
    minutes = int((seconds % 3600) // 60)
    secs = int(seconds % 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


def segments_to_markdown(segments: List[Dict]) -> str:
    """Convert transcription segments to Obsidian-friendly markdown."""
    lines = []
    for seg in segments:
        timestamp = format_timestamp(seg.get("start", 0))
        text = seg.get("text", "").strip()
        lines.append(f"- [{timestamp}](#t={timestamp}) {text}")
    return "\n".join(lines) + "\n"
