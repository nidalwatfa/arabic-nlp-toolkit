"""
Utils Module
------------
دوال مساعدة إضافية لمعالجة النصوص العربية:
- تنظيف النصوص من الرموز والأرقام
- إزالة المسافات الزائدة
- تحويل النصوص إلى حروف صغيرة
"""

import re

def clean_text(text: str) -> str:
    """إزالة الرموز والأرقام من النص العربي."""
    text = re.sub(r"[0-9]", "", text)            # إزالة الأرقام
    text = re.sub(r"[^\w\s]", "", text)          # إزالة الرموز
    return text.strip()

def remove_extra_spaces(text: str) -> str:
    """إزالة المسافات الزائدة من النص."""
    return re.sub(r"\s+", " ", text).strip()

def to_lower(text: str) -> str:
    """تحويل النصوص إلى حروف صغيرة (مفيد عند دمج نصوص عربية/إنجليزية)."""
    return text.lower()
