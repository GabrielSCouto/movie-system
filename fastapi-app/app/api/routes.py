from fastapi import APIRouter, HTTPException, status

from app.core.config import settings
from app.schemas.subtitle_schema import (
	HealthResponse,
	SubtitleTranslationRequest,
	SubtitleTranslationResponse,
)
from app.services.subtitle_file_service import save_translated_subtitle
from app.services.translation_service import translate_srt_subtitle

router = APIRouter(prefix="/ai", tags=["ai"])


@router.get("/health", response_model=HealthResponse)
def health_check() -> HealthResponse:
	return HealthResponse(
		status="ok",
		service=settings.service_name,
		message="AI service is running",
	)


@router.post("/translate-subtitle", response_model=SubtitleTranslationResponse)
def translate_subtitle(
	payload: SubtitleTranslationRequest,
) -> SubtitleTranslationResponse:
	try:
		translated_subtitle = translate_srt_subtitle(
			subtitle_content=payload.subtitle_content,
			source_language=payload.source_language,
			target_language=payload.target_language,
		)

		file_path = save_translated_subtitle(
			movie_id=payload.movie_id,
			target_language=payload.target_language,
			subtitle_content=translated_subtitle,
		)

		return SubtitleTranslationResponse(
			movie_id=payload.movie_id,
			source_language=payload.source_language,
			target_language=payload.target_language,
			format="srt",
			status="success",
			translated_subtitle=translated_subtitle,
			file_path=file_path,
		)
	except ValueError as exc:
		raise HTTPException(
			status_code=status.HTTP_400_BAD_REQUEST,
			detail=str(exc),
		) from exc
	except IOError as exc:
		raise HTTPException(
			status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
			detail=str(exc),
		) from exc
	except Exception as exc:
		raise HTTPException(
			status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
			detail="Unexpected internal error.",
		) from exc

