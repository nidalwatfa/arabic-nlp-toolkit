# في arabic_nlp_toolkit/__init__.py
from arabic_nlp_toolkit.utils import clean_text, remove_extra_spaces, to_lower

__all__ = [
    "normalize_text",
    "remove_stopwords",
    "tokenize",
    "stem_word",
    "word_frequency",
    "clean_text",           # جديد
    "remove_extra_spaces",  # جديد
    "to_lower",            # جديد
]
