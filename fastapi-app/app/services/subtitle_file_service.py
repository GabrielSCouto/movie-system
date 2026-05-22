from pathlib import Path

from app.core.config import settings


def save_translated_subtitle(
    movie_id: str,
    target_language: str,
    subtitle_content: str,
) -> str:
    file_name = f"{movie_id}_{target_language}.srt"
    output_path = settings.output_dir / file_name

    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(subtitle_content, encoding="utf-8")
    except OSError as exc:
        raise IOError("Could not save translated subtitle file.") from exc

    relative_path = Path("storage") / "output" / file_name
    return str(relative_path).replace("\\", "/")
