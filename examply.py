# -*- coding: utf-8 -*-
"""
Example usage of arabic_nlp_toolkit.py
"""

from arabic_nlp_toolkit import (
    normalize_text,
    tokenize,
    remove_stopwords,
    stem_word,
    analyze_text,
)

def main():
    # نص تجريبي
    text = "قالت آمنة: إنَّ الأطفال يلعبون في الحدائق! هل رأيت ذلك؟"

    print("النص الأصلي:")
    print(text)
    print("-" * 40)

    # تجربة التطبيع
    norm = normalize_text(text)
    print("النص بعد التطبيع:")
    print(norm)
    print("-" * 40)

    # تجربة التجزئة
    tokens = tokenize(norm)
    print("التوكنز:")
    print(tokens)
    print("-" * 40)

    # تجربة إزالة كلمات الوقف
    cleaned = remove_stopwords(text)
    print("النص بعد إزالة كلمات الوقف:")
    print(cleaned)
    print("-" * 40)

    # تجربة التجذير
    stems = [stem_word(t) for t in tokens]
    print("الجذور:")
    print(stems)
    print("-" * 40)

    # تجربة التحليل
    analysis = analyze_text(text)
    print("التحليل:")
    print(analysis)
    print("-" * 40)

if __name__ == "__main__":
    main()
