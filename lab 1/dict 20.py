f = lambda d: [k for k, v in sorted(d.items(), key=lambda x: (x[1], len(x[0])))][:3]
d = {
    "apple": 3,
    "kiwi": 2,
    "banana": 3,
    "fig": 1,
    "pear": 2
}
print(f(d))