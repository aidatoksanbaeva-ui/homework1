f = lambda d: {
    k: v for k, v in d.items()
    if len(k) % 2 != 0
    and v > 1
    and all(v % i != 0 for i in range(2, v))
}
d = {
    "one": 2,
    "two": 4,
    "three": 5,
    "four": 7,
    "five": 9
}
print(f(d))