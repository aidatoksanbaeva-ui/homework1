f = lambda d: {k: v for k, v in d.items() if sum(v)/len(v) > sum([num for lst in d.values() for num in lst])/sum([len(lst) for lst in d.values()])}
d = {
    "a": [1, 2, 3],
    "b": [4, 5, 6],
    "c": [7, 8, 9]
}
print(f(d))