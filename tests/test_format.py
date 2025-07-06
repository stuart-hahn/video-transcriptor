from videotranscriptor.transcribe import segments_to_markdown

def test_segments_to_markdown():
    segments = [
        {"start": 0.0, "text": "Hello world"},
        {"start": 5.2, "text": "Next line"},
    ]
    expected = (
        "- [00:00:00](#t=00:00:00) Hello world\n"
        "- [00:00:05](#t=00:00:05) Next line\n"
    )
    assert segments_to_markdown(segments) == expected
