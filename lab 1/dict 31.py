f = lambda d: {k: v for k, v in d.items() if len(v) == len(set(v)) and all(len(s) > 3 for s in v)}
d = {
    "a": ["apple", "pear", "plum"],
    "b": ["cat", "dog", "bird"],
    "c": ["tree", "tree", "bush"],
    "d": ["fish", "shark", "crab"]
}
print(f(d))