from pydantic import BaseModel, Field, field_validator


class SubtitleTranslationRequest(BaseModel):
    movie_id: str = Field(..., min_length=1)
    source_language: str = Field(..., min_length=1)
    target_language: str = Field(..., min_length=1)
    subtitle_content: str = Field(..., min_length=1)
    format: str = Field(default="srt")

    @field_validator("movie_id", "source_language", "target_language", "subtitle_content")
    @classmethod
    def validate_not_blank(cls, value: str) -> str:
        cleaned = value.strip()
        if not cleaned:
            raise ValueError("field cannot be empty")
        return cleaned

    @field_validator("format")
    @classmethod
    def validate_format(cls, value: str) -> str:
        normalized = value.strip().lower()
        if normalized != "srt":
            raise ValueError("Only .srt format is supported in this MVP.")
        return normalized


class SubtitleTranslationResponse(BaseModel):
    movie_id: str
    source_language: str
    target_language: str
    format: str
    status: str
    translated_subtitle: str
    file_path: str


class HealthResponse(BaseModel):
    status: str
    service: str
    message: str
