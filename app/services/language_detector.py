from langdetect import detect

class LanguageDetector:
    def detect(self, text: str):
        try:
            lang = detect(text)
            if lang == 'hi':
                return "hindi"
            elif lang == 'ta':
                return "tamil"
            else:
                return "english"
        except:
            return "english"
