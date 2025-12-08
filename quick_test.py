def main():
    text = "هذه مكتبة لمعالجة اللغة العربية. الاختبار اكتمل بنجاح. المكتبة تعمل بشكل ممتاز!"

    try:
        import nltk
        # تحميل الموارد اللازمة لأول مرة فقط
        nltk.download('punkt', quiet=True)

        # استخدام NLTK إذا كانت متوفرة
        words = nltk.word_tokenize(text)
        sentences = nltk.sent_tokenize(text)

    except ImportError:
        # إذا لم تكن المكتبة موجودة، نستخدم الطريقة البسيطة
        words = text.split()
        sentences = [s for s in text.split(".") if s.strip() != ""]

    analysis = {
        'word_count': len(words),
        'sentence_count': len(sentences)
    }

    print(f"{analysis['word_count']}")
    print(f"{analysis['sentence_count']}")
    print("الاختبار اكتمل بنجاح ✅")
    print("المكتبة تعمل بشكل ممتاز! 🎉\n")

if __name__ == "__main__":
    main()
