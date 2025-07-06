#!/usr/bin/env python3
"""Command-line interface for video transcription."""

import argparse
from pathlib import Path
from videotranscriptor.transcribe import transcribe_video, segments_to_markdown


def main() -> None:
    parser = argparse.ArgumentParser(description="Transcribe an MP4 file to Obsidian markdown")
    parser.add_argument("video", help="Path to the MP4 video file")
    parser.add_argument("-m", "--model", default="base", help="Whisper model size")
    parser.add_argument("-o", "--output", help="Output markdown file")
    args = parser.parse_args()

    segments = transcribe_video(args.video, model=args.model)
    markdown = segments_to_markdown(segments)

    output_path = Path(args.output) if args.output else Path(args.video).with_suffix(".md")
    with open(output_path, "w") as f:
        f.write(markdown)

    print(f"Transcript written to {output_path}")


if __name__ == "__main__":
    main()
