def filter_words(words):
    for word in words:
        if "а" in word:
            yield "c a"
        elif len(word)>4:
            yield word
words = ["кот", "машина", "арбуз", "дом"]
for w in filter_words(words):
    print(w)