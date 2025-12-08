<div align="center">
  <img src="assets/logo.svg" alt="Arabic NLP Toolkit" width="200"/>
  
  # Arabic NLP Toolkit
  ### 🔤 مكتبة معالجة اللغة الطبيعية للغة العربية
  
  ![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
  ![License](https://img.shields.io/badge/license-MIT-green.svg)
  ![Version](https://img.shields.io/badge/version-0.1.0-orange.svg)
  ![Arabic](https://img.shields.io/badge/العربية-100%25-red.svg)
  
  [English](#english) | [العربية](#arabic)
</div>

---

## 📖 نظرة عامة

**Arabic NLP Toolkit** هي مكتبة Python شاملة لمعالجة اللغة العربية الطبيعية. توفر المكتبة مجموعة من الأدوات الأساسية للعمل مع النصوص العربية.

### ✨ المميزات

- ✅ **تطبيع النصوص العربية** - إزالة التشكيل والتنظيم
- ✅ **التقطيع** - تقسيم النص إلى كلمات وجمل
- ✅ **الاشتقاق** - استخراج جذور الكلمات
- ✅ **إزالة الكلمات الشائعة** - تصفية الكلمات غير المهمة
- ✅ **التحليل النصي** - إحصائيات شاملة عن النصوص

---

## 🚀 التثبيت

```bash
pip install arabic-nlp-toolkit
```

أو من المصدر:

```bash
git clone https://github.com/nidalwatfa/arabic-nlp-toolkit.git
cd arabic-nlp-toolkit
pip install -e .
```

---

## 💡 الاستخدام السريع

```python
from arabic_nlp_toolkit import ArabicNormalizer, ArabicTokenizer, ArabicTextAnalyzer

# تطبيع النص
normalizer = ArabicNormalizer()
text = "مَرْحَباً بِكُمْ فِي مُعَالَجَةِ اللُّغَةِ العَرَبِيَّةِ"
normalized = normalizer.normalize(text)
print(normalized)  # مرحبا بكم في معالجة اللغة العربية

# تقطيع النص
tokenizer = ArabicTokenizer()
tokens = tokenizer.tokenize(normalized)
print(tokens)  # ['مرحبا', 'بكم', 'في', 'معالجة', 'اللغة', 'العربية']

# تحليل النص
analyzer = ArabicTextAnalyzer()
analysis = analyzer.analyze(normalized)
print(f"عدد الكلمات: {analysis['word_count']}")
print(f"عدد الجمل: {analysis['sentence_count']}")
```

---

## 📚 الوثائق

للمزيد من الأمثلة والشروحات التفصيلية، راجع مجلد [examples/](examples/)

---

## 🤝 المساهمة

نرحب بمساهماتك! اطلع على [CONTRIBUTING.md](CONTRIBUTING.md) لمعرفة كيفية المساهمة.

---

## 📄 الترخيص

هذا المشروع مرخص تحت رخصة MIT - راجع ملف [LICENSE](LICENSE) للتفاصيل.

---

## 👨‍💻 المطور

**Nidal Watfa**
- GitHub: [@nidalwatfa](https://github.com/nidalwatfa)
- Email: nidalwatfa99@gmail.com

---

<div align="center">
  صُنع بـ ❤️ للمجتمع العربي
</div>

