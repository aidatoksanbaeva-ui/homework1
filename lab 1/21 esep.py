filter_strings = lambda lst: [
    s.upper()
    for s in lst
    if len(s) > 4
    and all(('a' <= c <= 'z') or ('A' <= c <= 'Z') for c in s)
    and all(s.count(c) == 1 for c in s)
]
words = ["hello", "world", "apple", "Python", "abcde", "aabbc", "hi123"]
print(filter_strings (words))