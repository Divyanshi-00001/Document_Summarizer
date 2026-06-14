from deep_translator import GoogleTranslator

def translate_to_english(text, source_lang=None):
    # If source_lang is provided, you could use it; otherwise auto-detect
    # GoogleTranslator supports source="auto" in many cases
    return GoogleTranslator(source="auto", target="en").translate(text)

def translate_from_english(text, target_lang="en"):
    # Translate from English to the requested target language
    if not target_lang or target_lang == "en":
        return text
    return GoogleTranslator(source="en", target=target_lang).translate(text)