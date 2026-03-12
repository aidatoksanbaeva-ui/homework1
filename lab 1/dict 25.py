import math
f = lambda d: {k: math.prod(x for x in v if x > 0) for k, v in d.items() if any(x > 0 for x in v)}
d = {
    "a": [1, 2, -3],
    "b": [-1, -2],
    "c": [4, 5]
}
print(f(d))