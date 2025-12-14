class ArabicStemmer:
    def __init__(self):
        self.prefixes = ["ال", "وال", "بال", "فال"]
        self.suffixes = ["ون", "ين", "ات", "ه", "ة"]
    def stem(self, word):
        if len(word) < 4: return word
        for p in self.prefixes:
            if word.startswith(p): word = word[len(p):]; break
        for s in self.suffixes:
            if word.endswith(s): word = word[:-len(s)]; break
        return word