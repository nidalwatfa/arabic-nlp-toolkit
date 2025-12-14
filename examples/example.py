import sys
import os
from datetime import datetime

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

try:
    from arabic_nlp_toolkit.analyzer import ArabicTextAnalyzer
    print("✅ تم تحديث النظام: ميزة الحفظ التلقائي مفعلة!")
except ImportError as e:
    print(f"❌ خطأ في الاستيراد: {e}")
    sys.exit(1)

def save_to_file(text, result):
    with open("results.txt", "a", encoding="utf-8") as f:
        f.write(f"\n--- تحليل بتاريخ: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---\n")
        f.write(f"النص الأصلي: {text}\n")
        f.write(f"عدد الكلمات: {result['stats']['word_count']}\n")
        f.write(f"الكلمات النظيفة: {', '.join(result['cleaned_words'])}\n")
        f.write(f"الجذور: {', '.join(result['stems'])}\n")
        f.write("-" * 40 + "\n")

def main():
    analyzer = ArabicTextAnalyzer()
    print("\n" + "="*40)
    text = input("أدخل النص العربي لتحليله وحفظه: ")
    print("="*40 + "\n")
    
    if not text.strip():
        print("⚠️ يرجى إدخال نص صحيح.")
        return

    result = analyzer.analyze(text)
    
    # عرض النتائج على الشاشة
    print(f"📊 النتائج المباشرة:")
    print(f"- الكلمات المهمة: {result['cleaned_words']}")
    print(f"- الجذور المستخرجة: {result['stems']}")
    
    # حفظ النتائج في ملف
    save_to_file(text, result)
    print(f"\n💾 تم حفظ التقرير في ملف: results.txt")

if __name__ == "__main__":
    main()
