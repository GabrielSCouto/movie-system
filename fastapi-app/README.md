# Movie System - AI Service

This folder contains the AI microservice of Movie System.

It is an isolated FastAPI service responsible for translating movie subtitles in `.srt` format using a mocked AI translation function.

## MVP scope

- Receives subtitle `.srt` content
- Receives `movie_id`, `source_language`, and `target_language`
- Translates only text lines and preserves SRT structure
- Returns translated subtitle
- Saves translated subtitle to local folder `storage/output`

Out of scope:

- Frontend integration
- Spring Boot integration
- Real storage integration
- Authentication integration
- Database integration
- Audio extraction and subtitle generation from video

## Endpoints

### GET /ai/health

Response:

```json
{
  "status": "ok",
  "service": "ai-service",
  "message": "AI service is running"
}
```

### POST /ai/translate-subtitle

Request:

```json
{
  "movie_id": "movie-001",
  "source_language": "en",
  "target_language": "pt-BR",
  "subtitle_content": "1\n00:00:01,000 --> 00:00:03,000\nHello, welcome to the movie."
}
```

Response:

```json
{
  "movie_id": "movie-001",
  "source_language": "en",
  "target_language": "pt-BR",
  "format": "srt",
  "status": "success",
  "translated_subtitle": "1\n00:00:01,000 --> 00:00:03,000\nOlá, bem-vindo ao filme.",
  "file_path": "storage/output/movie-001_pt-BR.srt"
}
```

## Install and run

1. Install dependencies:

```bash
pip install -r requirements.txt
```

2. Run FastAPI service:

```bash
uvicorn app.main:app --reload
```

3. Open docs:

- http://127.0.0.1:8000/docs

## Notes

- Translation is currently mocked by `mock_translate_text`.
- This function is intentionally simple to allow future replacement with a real AI provider.
