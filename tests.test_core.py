from arabic_nlp_toolkit.core import normalize, tokenize, remove_stopwords, stem

def test_normalize():
    assert normalize("مَرْحَبًا!! 123 أَنا أَكْتُبُ") == "مرحبا انا اكتب"
    assert normalize("الكتــاب") == "الكتاب"

def test_tokenize():
    assert tokenize("مرحبا بك في العالم العربي") == ["مرحبا", "بك", "في", "العالم", "العربي"]

def test_remove_stopwords():
    tokens = ["مرحبا", "في", "العالم", "و", "أنا"]
    assert remove_stopwords(tokens) == ["مرحبا", "العالم"]

def test_stem():
    assert stem("الكتاب") == "كتاب"
    assert stem("والكتب") == "كتب"
    assert stem("يكتبون") == "كتب"
