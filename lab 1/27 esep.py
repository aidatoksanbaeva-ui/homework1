f = lambda strings: sorted(
    strings,
    key=lambda s: (-len(s), s)
)[:5]
words = ["apple", "banana", "kiwi", "orange", "pear", "grape", "melon"]
print(f(words))