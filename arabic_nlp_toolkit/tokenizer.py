import re
class ArabicTokenizer:
    def __init__(self):
        self.word_pattern = re.compile(r"[؀-ۿ]+")
    def tokenize_words(self, text):
        return self.word_pattern.findall(text) if text else []