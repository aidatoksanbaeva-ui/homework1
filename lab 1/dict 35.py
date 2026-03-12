f = lambda d: {k: v for k, v in d.items() if v % 3 != 0 and len(k) % 2 != 0}
d = {
    "a": 2,
    "bb": 4,
    "cat": 6,
    "door": 5,
    "ele": 7
}
print(f(d))