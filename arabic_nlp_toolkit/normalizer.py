import re
class ArabicNormalizer:
    def __init__(self):
        self.alef_variants = ["أ", "إ", "آ", "ٱ"]
        self.arabic_diacritics = re.compile(r"[ؗ-ًؚ-ْٰ]")
    def normalize(self, text):
        if not text: return ""
        text = self.arabic_diacritics.sub("", text)
        for v in self.alef_variants: text = text.replace(v, "ا")
        return text.strip()