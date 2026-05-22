from app.utils.srt_utils import is_translatable_text_line, validate_srt_content


def mock_translate_text(text: str, source_language: str, target_language: str) -> str:
    # TODO: substituir esta função mockada por integração real com IA, como OpenAI, Gemini, Whisper ou outro modelo.
    _ = source_language
    _ = target_language

    phrase_replacements = {
        "to the": "ao",
        "To the": "Ao",
    }

    replacements = {
        "Hello": "Olá",
        "hello": "olá",
        "welcome": "bem-vindo",
        "Welcome": "Bem-vindo",
        "movie": "filme",
        "Movie": "Filme",
        "good": "bom",
        "Good": "Bom",
        "morning": "manhã",
        "Morning": "Manhã",
        "night": "noite",
        "Night": "Noite",
    }

    translated = text
    for source_phrase, target_phrase in phrase_replacements.items():
        translated = translated.replace(source_phrase, target_phrase)

    for source_word, target_word in replacements.items():
        translated = translated.replace(source_word, target_word)

    return translated


def translate_srt_subtitle(
    subtitle_content: str,
    source_language: str,
    target_language: str,
) -> str:
    validate_srt_content(subtitle_content)

    translated_lines = []
    for line in subtitle_content.splitlines():
        if is_translatable_text_line(line):
            translated_lines.append(
                mock_translate_text(
                    text=line,
                    source_language=source_language,
                    target_language=target_language,
                )
            )
            continue

        translated_lines.append(line)

    return "\n".join(translated_lines)
