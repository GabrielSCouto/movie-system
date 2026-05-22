import re

TIMESTAMP_PATTERN = re.compile(
    r"^\d{2}:\d{2}:\d{2},\d{3}\s-->\s\d{2}:\d{2}:\d{2},\d{3}$"
)


def is_sequence_number_line(line: str) -> bool:
    return line.strip().isdigit()


def is_timestamp_line(line: str) -> bool:
    return bool(TIMESTAMP_PATTERN.match(line.strip()))


def is_empty_line(line: str) -> bool:
    return not line.strip()


def is_translatable_text_line(line: str) -> bool:
    if is_empty_line(line):
        return False
    if is_sequence_number_line(line):
        return False
    if is_timestamp_line(line):
        return False
    return True


def validate_srt_content(content: str) -> None:
    if not content or not content.strip():
        raise ValueError("subtitle_content cannot be empty.")

    lines = content.splitlines()
    has_sequence = any(is_sequence_number_line(line) for line in lines)
    has_timestamp = any(is_timestamp_line(line) for line in lines)

    if not has_sequence or not has_timestamp:
        raise ValueError("Invalid SRT content. Missing sequence number or timestamp.")
