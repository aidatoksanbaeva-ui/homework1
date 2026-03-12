f = lambda d: {k: v for k, v in d.items() if v >= sum(d.values())/len(d) and v % 2 != 0}
d = {"a": 1, "b": 4, "c": 5, "d": 6, "e": 7}
print(f(d))