import math
f = lambda d: {k: math.factorial(v) if v < 6 else v for k, v in d.items()}
d = {
    "a": 3,
    "b": 5,
    "c": 6,
    "d": 2
}
print(f(d))