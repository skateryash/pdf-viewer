import googletrans
from deep_translator import GoogleTranslator


class TextTranslator:
    def __init__(self):
        self.langdict = googletrans.LANGUAGES

    def translate_text(self, text, target_language):
        translated_text = GoogleTranslator(source='auto', target=target_language).translate(text)
        return translated_text
