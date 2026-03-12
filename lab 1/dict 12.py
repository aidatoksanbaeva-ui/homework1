f = lambda s: {x for x in s if len(x) > 4 and len(x) == len(set(x)) and all(('a' <= c <= 'z') or ('A' <= c <= 'Z') for c in x)}
words = {"apple", "banana", "abcde", "hello", "world", "abcd1"}
print(f(words))