from .normalizer import ArabicNormalizer
from .tokenizer import ArabicTokenizer
from .stemmer import ArabicStemmer
from .stopwords import StopwordsRemover

class ArabicTextAnalyzer:
    def __init__(self):
        self.normalizer = ArabicNormalizer()
        self.tokenizer = ArabicTokenizer()
        self.stemmer = ArabicStemmer()
        self.stopwords = StopwordsRemover()

    def analyze(self, text):
        norm_text = self.normalizer.normalize(text)
        words = self.tokenizer.tokenize_words(norm_text)
        clean_words = self.stopwords.remove(words)
        stems = [self.stemmer.stem(w) for w in clean_words]
        return {
            "stats": {"original_len": len(text), "word_count": len(words)},
            "cleaned_words": clean_words,
            "stems": stems
        }