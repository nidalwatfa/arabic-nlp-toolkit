# -*- coding: utf-8 -*-
"""
Basic tests for arabic_nlp_toolkit functions
Run with: pytest tests/
"""

import pytest
from arabic_nlp_toolkit import (
    normalize_text,
    tokenize,
    remove_stopwords,
    stem_word,
    analyze_text,
)

def test_normalize_text():
    text = "آباءٌ وأبناءٌ"
    result = normalize_text(text)
    assert "ا" in result
    assert "أ" not in result

def test_tokenize():
    text = "الطلاب يدرسون في المدرسة."
    tokens = tokenize(text)
    assert isinstance(tokens, list)
    assert "الطلاب" in tokens
    assert "المدرسة" in tokens

def test_remove_stopwords():
    text = "الطلاب يدرسون في المدرسة"
    cleaned = remove_stopwords(text)
    assert "في" not in cleaned
    assert "الطلاب" in cleaned

def test_stem_word():
    word = "والطلاب"
    stem = stem_word(word)
    assert stem == "طالب" or stem.startswith("طالب")

def test_analyze_text():
    text = "قالت آمنة: إن الأطفال يلعبون في الحدائق! هل رأيت ذلك؟"
    analysis = analyze_text(text)
    assert "word_count" in analysis
    assert "char_count" in analysis
    assert "sentence_count" in analysis
    assert analysis["word_count"] > 0
