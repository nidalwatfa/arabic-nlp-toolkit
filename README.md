# -*- coding: utf-8 -*-
"""
Arabic NLP - Minimal open-source starter library for Arabic text processing.

Functions included:
- normalize_text(text): Normalize Arabic text (remove diacritics, unify letters).
- remove_stopwords(text): Remove Arabic stopwords.
- tokenize(text): Simple whitespace + punctuation tokenization for Arabic.
- stem_word(word): Very simple rule-based stemmer (remove common prefixes/suffixes).
- analyze_text(text): Basic analysis (word count, char count, sentence count).

Note: This is a lightweight educational starting point. You can expand by:
- Using a richer stopword list
- Improving tokenization for clitics
- Adding lemmatization and POS tagging
- Handling dialectal Arabic variants
"""

import re

# Arabic diacritics (tashkeel) to remove
ARABIC_DIACRITICS_PATTERN = re.compile(
    r"[\u0610-\u061A\u064B-\u065F\u0670\u06D6-\u06DC\u06DF-\u06E8\u06EA-\u06ED]"
)

# Basic Arabic sentence enders (. ! ؟)
SENTENCE_ENDERS = re.compile(r"[.!\u061F]")

def normalize_text(text: str) -> str:
    """
    Normalize Arabic text:
    - Remove diacritics (tashkeel).
    - Unify different forms of Alef: أ، إ، آ -> ا
    - Convert Alef Maqsura ى -> ا (design choice; can be ى->ي if preferred)
    - Normalize Tatweel (ـ)
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
    text = (
        text.replace("أ", "ا")
            .replace("إ", "ا")
            .replace("آ", "ا")
    )

    # Alef Maqsura to Alef (design choice)
    text = text.replace("ى", "ا")

    # Normalize Tatweel
    text = text.replace("ـ", "")

    # Normalize common punctuation spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text

# Minimal Arabic stopword list (expand as needed)
ARABIC_STOPWORDS = set([
    "في", "على", "و", "ثم", "أو", "أن", "إن", "من", "ما", "لا", "لم", "لن",
    "له", "لها", "هو", "هي", "هم", "هن", "هذا", "هذه", "ذلك", "تلك",
    "هناك", "هنا", "كانت", "كان", "إلى", "الى", "عن", "قد", "كل", "أي",
    "أين", "كيف", "إذا", "اذا", "لكن", "بل", "بعض", "أمام", "قبل", "بعد",
    "مع", "أكثر", "أقل", "حتى", "حيث", "أثناء", "أحد", "أخرى", "أول",
    "أصبح", "أوضح", "فوق", "تحت", "بين", "غير", "دون", "كما", "لقد", "لدى",
    "مثل", "حسب", "وهذا", "وهذه", "وكان", "وكانت",
])

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
        Text without common
