f = lambda d: [k for k, v in sorted(d.items(), key=lambda x: (x[1] % 10, x[0]))]
d = {
    "apple": 23,
    "banana": 12,
    "cat": 35,
    "door": 42
}
print(f(d))