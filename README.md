# Video Transcriptor

This project provides a simple command line tool to convert an MPEG-4 video into a text transcript formatted in Obsidian‑friendly markdown.

## Requirements

* Python 3.11+
* [FFmpeg](https://ffmpeg.org/) installed and available on the system path
* Python dependencies from `requirements.txt`

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
./transcribe.py path/to/video.mp4
```

The command will create `video.md` beside the input file. Use the `-o` option to specify another output file and `-m` to choose a Whisper model size.

The resulting markdown contains timestamped bullet points that link to the corresponding time in the video, making it convenient to use with Obsidian.

