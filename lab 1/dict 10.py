d = {
    "a": [1,2,3,4],
    "b": [2,4,6],
    "c": [7,5,8]
}
f = lambda d: {k: sorted([x for x in v if x % 2 != 0]) for k, v in d.items() if [x for x in v if x % 2 != 0]}
print(f(d))