# -*- coding: utf-8 -*-
"""
Arabic NLP - Minimal open-source starter library for Arabic text processing.

Functions included:
- normalize_text(text): Normalize Arabic text (remove diacritics, unify letters).
- remove_stopwords(text): Remove Arabic stopwords.
- tokenize(text): Simple whitespace + punctuation tokenization for Arabic.
- stem_word(word): Very simple rule-based stemmer (remove common prefixes/suffixes).
- analyze_text(text): Basic analysis (word count, char count, sentence count).

Note:
This is a lightweight educational starting point. You can expand by:
- Using a richer stopword list
- Improving tokenization for clitics
- Adding lemmatization and POS tagging
- Handling dialectal Arabic variants
"""

import re

# ------------------------------
# Utilities: Arabic character ranges and diacritics
# ------------------------------

# Arabic diacritics (tashkeel) to remove
ARABIC_DIACRITICS_PATTERN = re.compile(
    r"[\u0610-\u061A\u064B-\u065F\u0670\u06D6-\u06DC\u06DF-\u06E8\u06EA-\u06ED]"
)

# Basic Arabic sentence enders
SENTENCE_ENDERS = re.compile(r"[\.!\u061F]")  # . ! ؟


# ------------------------------
# 1) normalize_text(text)
# ------------------------------
def normalize_text(text: str) -> str:
    """
    Normalize Arabic text:
    - Remove diacritics (tashkeel).
    - Unify different forms of Alef: أ، إ، آ -> ا
    - Convert Alef Maqsura ى -> ا (project choice; can be ى->ي if preferred)
    - Convert Hamza-on-Waw and Hamza-on-Ya to standalone hamza or keep as is (minimal here).
    - Normalize Ta Marbuta ة -> ه (optional; here we keep it as ة).
    - Remove extra spaces.

    Args:
        text: Arabic text input.

    Returns:
        Normalized Arabic text string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Remove diacritics
    text = ARABIC_DIACRITICS_PATTERN.sub("", text)

    # Unify Alef variants
    text = text.replace("أ", "ا").replace("إ", "ا").replace("آ", "ا")

    # Alef Maqsura to Alef (design choice)
    text = text.replace("ى", "ا")

    # Optional normalizations (commented out for conservative approach):
    # text = text.replace("ؤ", "و")  # might lose information
    # text = text.replace("ئ", "ي")  # might lose information
    # text = text.replace("ة", "ه")  # might distort morphology

    # Normalize Tatweel
    text = text.replace("ـ", "")

    # Normalize common punctuation spaces
    text = re.sub(r"\s+", " ", text).strip()
    return text


# ------------------------------
# 2) remove_stopwords(text)
# ------------------------------
# Minimal Arabic stopword list (expand as needed)
ARABIC_STOPWORDS = set([
    "في", "على", "و", "ثم", "أو", "أن", "إن", "من", "ما", "لا", "لم", "لن", "له", "لها",
    "هو", "هي", "هم", "هن", "هذا", "هذه", "ذلك", "تلك", "هناك", "هنا", "كانت", "كان",
    "إلى", "الى", "عن", "قد", "قد", "كل", "أي", "أين", "كيف", "إذا", "اذا", "لكن",
    "بل", "بعض", "أمام", "قبل", "بعد", "مع", "أكثر", "أقل", "حتى", "حيث", "أثناء",
    "أحد", "أخرى", "أول", "أصبح", "أوضح", "فوق", "تحت", "بين", "غير", "دون", "كما",
    "لقد", "لدى", "مثل", "حسب", "وهذا", "وهذه", "وكان", "وكانت"
])

def remove_stopwords(text: str) -> str:
    """
    Remove Arabic stopwords from text after a light normalization.

    Steps:
    - Normalize text (without aggressive letter losses).
    - Tokenize into words.
    - Filter out stopwords.
    - Return a cleaned string.

    Args:
        text: Arabic text input.

    Returns:
        Text without common stopwords.
    """
    norm = normalize_text(text)
    tokens = tokenize(norm)
    filtered = [t for t in tokens if t not in ARABIC_STOPWORDS]
    return " ".join(filtered)


# ------------------------------
# 3) tokenize(text)
# ------------------------------
def tokenize(text: str) -> list:
    """
    Tokenize Arabic text using a simple regex:
    - Split on any character that is not Arabic letter or digit.
    - Keep Arabic letters and numbers contiguous.

    Args:
        text: Arabic text input.

    Returns:
        List of tokens (strings).
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Keep Arabic letters (0600–06FF approx), extended Arabic, and digits
    tokens = re.split(r"[^\u0600-\u06FF0-9]+", text)
    # Remove empty tokens
    return [t for t in tokens if t]


# ------------------------------
# 4) stem_word(word)
# ------------------------------
# Common Arabic prefixes and suffixes (minimal sets)
PREFIXES = ["ال", "و", "ف", "ب", "ك", "ل", "س"]
HEAVY_PREFIXES = ["وال", "فال", "بال", "كال", "لل"]  # handle clitics + definite article
SUFFIXES = ["ه", "ها", "هم", "هن", "كما", "كم", "نا", "ي", "ك", "ا", "ات", "ون", "ين", "ان", "ة"]

def stem_word(word: str) -> str:
    """
    Very simple rule-based stemmer:
    - Remove heavy prefixes (e.g., وال، فال، بال، كال، لل).
    - Remove single-letter clitic prefixes (و، ف، ب، ك، ل، س) if word length allows.
    - Remove definite article "ال" if present.
    - Remove common suffixes (plural, pronouns, feminine marker).
    - Do not reduce below length 2 to avoid over-stemming.

    Args:
        word: Single Arabic word.

    Returns:
        A crude stem form of the word.
    """
    if not isinstance(word, str):
        raise TypeError("word must be a string")

    w = word

    # Remove heavy prefixes first
    for p in HEAVY_PREFIXES:
        if w.startswith(p) and len(w) - len(p) >= 2:
            w = w[len(p):]
            break  # remove only one

    # Remove single-letter clitics
    while len(w) > 2 and w[0] in PREFIXES:
        w = w[1:]

    # Remove definite article
    if w.startswith("ال") and len(w) - 2 >= 2:
        w = w[2:]

    # Remove suffixes
    removed = True
    while removed:
        removed = False
        for s in sorted(SUFFIXES, key=len, reverse=True):
            if w.endswith(s) and len(w) - len(s) >= 2:
                w = w[:-len(s)]
                removed = True
                break

    return w


# ------------------------------
# 5) analyze_text(text)
# ------------------------------
def analyze_text(text: str) -> dict:
    """
    Provide a basic analysis of the Arabic text:
    - word_count: number of tokens
    - char_count: number of characters (excluding spaces)
    - sentence_count: number of sentences separated by ., !, ؟

    Args:
        text: Arabic text input.

    Returns:
        Dictionary with analysis metrics.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    norm = normalize_text(text)
    tokens = tokenize(norm)
    word_count = len(tokens)
    char_count = len(re.sub(r"\s+", "", norm))
    # Count sentence boundaries by splitting on enders and filtering empties
    sentences = [s for s in SENTENCE_ENDERS.split(norm) if s.strip()]
    sentence_count = len(sentences)

    return {
        "word_count": word_count,
        "char_count": char_count,
        "sentence_count": sentence_count,
    }


# ------------------------------
# Example usage
# ------------------------------
if __name__ == "__main__":
    sample_text = "قالت آمنة: إنَّ الأطفال يلعبون في الحدائق! هل رأيت ذلك؟"

    print("Original:", sample_text)

    norm = normalize_text(sample_text)
    print("Normalized:", norm)

    tokens = tokenize(norm)
    print("Tokens:", tokens)

    cleaned = remove_stopwords(sample_text)
    print("Without stopwords:", cleaned)

    # Stem each token (demonstration)
    stems = [stem_word(t) for t in tokens]
    print("Stems:", stems)

    analysis = analyze_text(sample_text)
    print("Analysis:", analysis)
