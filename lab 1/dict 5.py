top5 = lambda d: sorted(
    d,
    key=lambda k: (-d[k], k)
)[:5]
d = {
    "apple": 10,
    "banana": 15,
    "pear": 10,
    "orange": 7,
    "grape": 20,
    "kiwi": 15
}
print(top5(d))